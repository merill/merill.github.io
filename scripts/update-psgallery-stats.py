#!/usr/bin/env python3
"""Update _data/stats.yml with the latest PowerShell Gallery download counts.

Fetches DownloadCount for each tracked package from the PSGallery OData v2
API (no auth required) and rewrites _data/stats.yml in-place. Designed to
run from .github/workflows/update-stats.yml on a daily schedule, but also
runnable locally with no external Python dependencies.

Usage:
    python3 scripts/update-psgallery-stats.py [--dry-run]

Exit codes:
    0  success (file written, or --dry-run completed)
    1  one or more packages could not be fetched

To track a different set of packages, edit PACKAGES below.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Packages to track. The Id must match the PowerShell Gallery package Id
# exactly (case-insensitive on the Gallery, but we keep canonical casing
# so the YAML keys match what _pages/home.md looks up).
PACKAGES: list[str] = [
    "Maester",
    "EntraExporter",
    "Uninstall-Graph",
    "MSIdentityTools",
    "ZeroTrustAssessment",
]

REPO_ROOT = Path(__file__).resolve().parent.parent
STATS_FILE = REPO_ROOT / "_data" / "stats.yml"
USER_AGENT = "merill.net-stats-updater/1.0 (+https://merill.net)"
TIMEOUT_SECONDS = 30


def fetch_download_count(package_id: str) -> int:
    """Return the cumulative DownloadCount for a PSGallery package.

    Uses the OData v2 endpoint with $filter=Id eq '...' and IsLatestVersion
    so we get a single entry back. Raises RuntimeError on failure.
    """
    query = (
        f"Id eq '{package_id}' and IsLatestVersion"
    )
    url = (
        "https://www.powershellgallery.com/api/v2/Packages()"
        f"?$filter={urllib.parse.quote(query)}"
        "&$select=Id,DownloadCount"
        "&$top=1"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            body = resp.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"network error fetching {package_id}: {exc}") from exc

    match = re.search(r"<d:DownloadCount[^>]*>(\d+)</d:DownloadCount>", body)
    if not match:
        raise RuntimeError(
            f"DownloadCount not found in response for {package_id}; "
            "package may not exist or response shape changed"
        )
    return int(match.group(1))


def format_short(n: int) -> str:
    """Format an integer as a short, human-friendly string.

    Examples:
        303_721 -> "304k"
          5_577 -> "5.5k"
          1_000_000 -> "1.0m"
            842 -> "842"
    """
    if n < 1000:
        return str(n)
    if n < 10_000:
        # 1.0k - 9.9k: one decimal place feels right
        return f"{n / 1000:.1f}k"
    if n < 1_000_000:
        # 10k - 999k: round to nearest thousand
        return f"{round(n / 1000)}k"
    if n < 10_000_000:
        return f"{n / 1_000_000:.1f}m"
    return f"{round(n / 1_000_000)}m"


def write_stats(counts: dict[str, int], updated: str) -> str:
    """Render the YAML payload and return it as a string.

    Hand-written rather than using PyYAML so we don't add a runtime
    dependency to the workflow. The format matches what the existing
    _data/stats.yml uses.
    """
    lines = [
        "# PowerShell Gallery download stats.",
        "#",
        "# This file is auto-updated daily by .github/workflows/update-stats.yml",
        "# and consumed by _pages/home.md to render install counts on project cards.",
        "#",
        "# Manual edits will be overwritten by the next workflow run. To change which",
        "# packages are tracked, edit scripts/update-psgallery-stats.py.",
        "#",
        "# Each entry uses the PowerShell Gallery package Id as the key.",
        "#   downloads: integer total download count from the Gallery",
        '#   display:   pre-formatted short string (e.g. "458k") used in templates',
        "#   updated:   ISO 8601 UTC timestamp of the last successful refresh",
        "",
        "psgallery:",
    ]
    for package_id in PACKAGES:
        if package_id not in counts:
            # Skip packages we failed to fetch — leaves the YAML without
            # them, which makes the Liquid {%- if s.display -%} guard
            # silently hide the stat on the card.
            continue
        downloads = counts[package_id]
        display = format_short(downloads)
        lines.append(f"  {package_id}:")
        lines.append(f"    downloads: {downloads}")
        lines.append(f'    display: "{display}"')
        lines.append(f'    updated: "{updated}"')
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the new YAML to stdout instead of writing it",
    )
    args = parser.parse_args(argv)

    counts: dict[str, int] = {}
    failures: list[str] = []
    for package_id in PACKAGES:
        try:
            count = fetch_download_count(package_id)
        except RuntimeError as exc:
            print(f"WARN  {exc}", file=sys.stderr)
            failures.append(package_id)
            continue
        counts[package_id] = count
        print(f"OK    {package_id}: {count:,} downloads -> {format_short(count)}")

    if not counts:
        print("ERROR no packages fetched successfully; aborting", file=sys.stderr)
        return 1

    updated = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = write_stats(counts, updated)

    if args.dry_run:
        print()
        print("--- would write to", STATS_FILE, "---")
        print(payload, end="")
        return 1 if failures else 0

    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATS_FILE.write_text(payload, encoding="utf-8")
    print(f"\nWrote {STATS_FILE.relative_to(REPO_ROOT)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
