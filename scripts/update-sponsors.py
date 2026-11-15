#!/usr/bin/env python3
"""Update _data/sponsor_wall.json, the consolidated sponsor wall on /sponsor/.

Three sources, shown on the page in this order:

  company  Company sponsors of Maester. Kept by hand in the Maester repo at
           website/sponsors/featured.yml (name, url, logo).
  cloud    Maester Cloud supporters who opted in to the public wall
           (https://maester.cloud/founders), from its public API.
  github   Public GitHub sponsors of @merill (GraphQL). The tier name comes
           from https://github.com/merill/sponsors (sponsors.json) when that
           feed lists the sponsor; otherwise it defaults to "Backers".

A sponsor is listed once: a company sponsor is left out of the cloud and
github groups.

Maester Cloud supporters upload their own images, which can be large, so
they are saved as small thumbnails in assets/images/sponsors/ (needs Pillow:
`pip install pillow`). Without Pillow the page links to the original image.

Designed to run from .github/workflows/update-sponsors.yml on a daily
schedule, but also runnable locally with no external Python dependencies.

Usage:
    python3 scripts/update-sponsors.py [--dry-run]
    GH_TOKEN=$(gh auth token) python3 scripts/update-sponsors.py

Environment:
    GH_TOKEN / GITHUB_TOKEN  Any GitHub token. Only public sponsors are
                             requested. Without one, the github group keeps
                             what is already in the file.

Exit codes:
    0  every source was read
    1  one or more sources failed; their groups keep the previous data, so
       a failed lookup never empties the wall
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "sponsor_wall.json"
IMAGE_DIR = REPO_ROOT / "assets" / "images" / "sponsors"
IMAGE_URL_PATH = "/assets/images/sponsors"
THUMB_SIZE = 144  # pixels; shown at 36px, so sharp on high-density screens
MAX_IMAGE_BYTES = 8 * 1024 * 1024

GITHUB_LOGIN = "merill"
FEATURED_URL = "https://raw.githubusercontent.com/maester365/maester/main/website/sponsors/featured.yml"
FEATURED_ASSET_BASE = "https://raw.githubusercontent.com/maester365/maester/main/website/public"
CLOUD_BASE = "https://maester.cloud"
CLOUD_API = f"{CLOUD_BASE}/api/founding-members"
TIER_FEED_URL = "https://raw.githubusercontent.com/merill/sponsors/main/sponsors.json"
GRAPHQL_URL = "https://api.github.com/graphql"

# Largest first. Anything else (or unknown) sorts last as a backer.
TIER_ORDER = ["Lead Sponsors", "Company Sponsors", "Sponsors", "Backers"]

USER_AGENT = "merill.net-sponsor-wall"
TIMEOUT = 30


def fetch(url: str, *, data: bytes | None = None, headers: dict[str, str] | None = None) -> bytes:
    request = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return response.read()


def safe_url(value: object, base: str | None = None) -> str | None:
    """Return an absolute http(s) URL, or None. Sponsor data is untrusted."""
    if not isinstance(value, str) or not value.strip():
        return None
    url = urljoin(base, value.strip()) if base else value.strip()
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return None
    return url


def clean_text(value: object, limit: int = 80) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", value).strip()[:limit]


def initials(name: str) -> str:
    words = [w for w in re.split(r"[^\w]+", name) if w]
    return "".join(w[0].upper() for w in words[:2]) or "+"


def name_key(name: str) -> str:
    """Comparable form of a sponsor name: 'CyberDrain / CIPP' -> 'cyberdrain'."""
    return re.sub(r"[^a-z0-9]", "", name.split("/")[0].lower())


# --- company: Maester repo, website/sponsors/featured.yml -------------------

def parse_featured(text: str) -> list[dict[str, str]]:
    """Parse the flat list of maps in featured.yml (no YAML dependency)."""
    items: list[dict[str, str]] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^(-\s+|\s+)([A-Za-z]+):\s*(.*)$", line)
        if not match:
            continue
        marker, key, value = match.groups()
        value = re.sub(r"\s+#.*$", "", value).strip().strip("'\"")
        if marker.startswith("-"):
            items.append({})
        if items:
            items[-1][key] = value
    return items


def fetch_company() -> list[dict]:
    sponsors = []
    for item in parse_featured(fetch(FEATURED_URL).decode("utf-8")):
        name = clean_text(item.get("name"))
        logo = safe_url(item.get("logo"), FEATURED_ASSET_BASE + "/")
        if not name or not logo:
            continue
        sponsors.append({
            "name": name,
            "url": safe_url(item.get("url")),
            "logo": FEATURED_ASSET_BASE + item["logo"] if item["logo"].startswith("/") else logo,
            "github": clean_text(item.get("github")),
        })
    if not sponsors:
        raise ValueError("featured.yml listed no sponsors")
    return sponsors


# --- cloud: Maester Cloud supporters wall -----------------------------------

def fetch_cloud() -> list[dict]:
    body = json.loads(fetch(CLOUD_API, headers={"Accept": "application/json"}))
    members = body.get("members") if isinstance(body, dict) else None
    if not isinstance(members, list):
        raise ValueError("Maester Cloud wall API did not return a members list")
    members = sorted(
        (m for m in members if isinstance(m, dict)),
        key=lambda m: str(m.get("optedInAt") or ""),
    )
    sponsors = []
    for member in members:
        name = clean_text(member.get("displayName"))
        if not name:
            continue
        image = safe_url(member.get("imageUrl"), CLOUD_BASE)
        if image and not urlparse(image).path.startswith("/api/founding-members/images/"):
            image = None
        sponsors.append({
            "name": name,
            "url": safe_url(member.get("url")),
            "image": image,
            "initials": initials(name),
        })
    return sponsors


# --- github: public GitHub sponsors -----------------------------------------

SPONSORS_QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    sponsorshipsAsMaintainer(first: 100, after: $cursor, activeOnly: true, includePrivate: false) {
      pageInfo { hasNextPage endCursor }
      nodes {
        sponsorEntity {
          __typename
          ... on User { login name avatarUrl(size: 160) websiteUrl url }
          ... on Organization { login name avatarUrl(size: 160) websiteUrl url }
        }
      }
    }
  }
}
"""


def fetch_tiers() -> dict[str, str]:
    """login -> tier name, from the merill/sponsors feed. Best effort."""
    try:
        feed = json.loads(fetch(TIER_FEED_URL))
    except (urllib.error.URLError, ValueError, TimeoutError) as error:
        print(f"  tier feed unavailable ({error}); using default tiers", file=sys.stderr)
        return {}
    tiers = {}
    for entry in feed if isinstance(feed, list) else []:
        if isinstance(entry, dict) and entry.get("tier") in TIER_ORDER:
            tiers[str(entry.get("login", "")).lower()] = entry["tier"]
    return tiers


def fetch_github(token: str) -> list[dict]:
    tiers = fetch_tiers()
    sponsors: list[dict] = []
    cursor = None
    while True:
        payload = json.dumps({"query": SPONSORS_QUERY, "variables": {"login": GITHUB_LOGIN, "cursor": cursor}})
        body = json.loads(fetch(
            GRAPHQL_URL,
            data=payload.encode("utf-8"),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        ))
        if body.get("errors"):
            raise ValueError(f"GitHub GraphQL: {body['errors'][0].get('message')}")
        page = body["data"]["user"]["sponsorshipsAsMaintainer"]
        for node in page["nodes"]:
            entity = node.get("sponsorEntity") or {}
            login = clean_text(entity.get("login"))
            if not login:
                continue
            is_org = entity.get("__typename") == "Organization"
            sponsors.append({
                "login": login,
                "name": clean_text(entity.get("name")) or login,
                "url": safe_url(entity.get("url")) or f"https://github.com/{login}",
                "website": safe_url(entity.get("websiteUrl")),
                "avatar": safe_url(entity.get("avatarUrl")),
                "org": is_org,
                "tier": tiers.get(login.lower(), "Backers"),
            })
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    sponsors.sort(key=lambda s: (TIER_ORDER.index(s["tier"]), s["name"].lower()))
    return sponsors


# --- thumbnails for Maester Cloud supporter images ---------------------------

def cache_cloud_images(cloud: list[dict]) -> None:
    """Save each supporter image as a small local thumbnail and point to it.

    Files are named after the image URL, so a changed image gets a new file
    and thumbnails no supporter uses any more are removed.
    """
    try:
        from PIL import Image
    except ImportError:
        print("  Pillow not installed; linking to the original supporter images", file=sys.stderr)
        return

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    keep = set()
    for sponsor in cloud:
        source = sponsor.get("image")
        if not source or source.startswith(IMAGE_URL_PATH):
            if source:
                keep.add(source.rsplit("/", 1)[-1])
            continue
        name = hashlib.sha256(source.encode("utf-8")).hexdigest()[:20] + ".webp"
        target = IMAGE_DIR / name
        if not target.exists():
            try:
                raw = fetch(source)
                if len(raw) > MAX_IMAGE_BYTES:
                    raise ValueError("image too large")
                image = Image.open(io.BytesIO(raw))
                image = image.convert("RGBA")
                image.thumbnail((THUMB_SIZE, THUMB_SIZE))
                image.save(target, "WEBP", quality=85)
            except Exception as error:  # noqa: BLE001 - keep the remote image
                print(f"  thumbnail failed for {sponsor['name']}: {error}", file=sys.stderr)
                continue
        sponsor["image"] = f"{IMAGE_URL_PATH}/{name}"
        keep.add(name)

    for stale in IMAGE_DIR.glob("*.webp"):
        if stale.name not in keep:
            stale.unlink()


# --- consolidate -------------------------------------------------------------

def consolidate(data: dict) -> dict:
    """List each sponsor once: company first, then cloud, then github."""
    company = data.get("company", [])
    company_names = {name_key(s["name"]) for s in company}
    company_logins = {s["github"].lower() for s in company if s.get("github")}
    cloud = [s for s in data.get("cloud", []) if name_key(s["name"]) not in company_names]
    github = [
        s for s in data.get("github", [])
        if s["login"].lower() not in company_logins and name_key(s["name"]) not in company_names
    ]
    return {"company": company, "cloud": cloud, "github": github}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="print the result instead of writing the file")
    args = parser.parse_args()

    try:
        previous = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        previous = {}

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    sources = {
        "company": fetch_company,
        "cloud": fetch_cloud,
        "github": (lambda: fetch_github(token)) if token else None,
    }

    data: dict = {}
    failed = []
    for key, fetcher in sources.items():
        if fetcher is None:
            print(f"{key}: no GH_TOKEN/GITHUB_TOKEN set; keeping previous data", file=sys.stderr)
            data[key] = previous.get(key, [])
            continue
        try:
            data[key] = fetcher()
            print(f"{key}: {len(data[key])} fetched")
        except Exception as error:  # noqa: BLE001 - any failure keeps the previous group
            print(f"{key}: FAILED ({error}); keeping previous data", file=sys.stderr)
            data[key] = previous.get(key, [])
            failed.append(key)

    result = consolidate(data)
    print("wall: " + ", ".join(f"{len(v)} {k}" for k, v in result.items()))

    if not args.dry_run and "cloud" not in failed:
        cache_cloud_images(result["cloud"])
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"

    if args.dry_run:
        print(output)
    else:
        DATA_FILE.write_text(output, encoding="utf-8")
        print(f"wrote {DATA_FILE.relative_to(REPO_ROOT)}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
