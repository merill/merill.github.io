"""Cloudflare GraphQL Analytics fetcher.

Pulls 30-day pageView counts per zone from the public GraphQL Analytics API
and returns a {zone_key: count} mapping.

Only zones where the project domain == the zone are tracked here. Cloudflare
Free's httpRequests1dGroups dataset is aggregated at the zone level and does
NOT support hostname filtering, so subdomains of a shared zone (e.g.
*.merill.net) cannot be split out without the Web Analytics beacon or a
paid plan with adaptiveGroups retention. Those cards intentionally don't
get a Cloudflare badge.

Authentication is via a Bearer token in CLOUDFLARE_API_TOKEN, scope:
  Zone -> Analytics -> Read  (on All zones, or on the specific zones below)

Reference:
  https://developers.cloudflare.com/analytics/graphql-api/
  Dataset: httpRequests1dGroups (daily aggregated, 30+ days retention on Free)
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass

GRAPHQL_ENDPOINT = "https://api.cloudflare.com/client/v4/graphql"
USER_AGENT = "merill.net-stats-updater/1.0 (+https://merill.net)"
TIMEOUT_SECONDS = 60
WINDOW_DAYS = 30


@dataclass(frozen=True)
class Site:
    """A single tracked Cloudflare zone.

    `key`     Stable identifier used as the YAML key under cloudflare:.
              Equal to the public hostname / zone name.
    `zone_id` Cloudflare zone ID (32-char hex).
    """

    key: str
    zone_id: str


# Zone IDs come from `cloudflare zones list`. To track an additional card,
# add a new Site() entry here AND wire the matching key into _pages/home.md.
#
# Subdomains (*.merill.net) are intentionally NOT tracked individually here
# — see module docstring for the reasoning. As a single exception, the
# merill.net zone total is attributed to the Graph Permissions Explorer
# card (graphpermissions.merill.net is the dominant subdomain by traffic).
SITES: list[Site] = [
    Site(key="maester.dev", zone_id="a153599f0ecad99b19f2e71986a761f7"),
    Site(key="cmd.ms", zone_id="c9a63474a8b4304664a85b352cb8519b"),
    Site(key="getyako.com", zone_id="628baf20d90649a562b19d3b2e0c319e"),
    Site(key="bluesky.ms", zone_id="482b18b12d6730727612a4719c665a5b"),
    Site(key="lokka.dev", zone_id="a0e07884417766a7fd5edf97ecd06eed"),
    Site(key="graph.pm", zone_id="86e542369b5c343bb4348aba345d3f92"),
    Site(key="vscodemcp.com", zone_id="7d31153d3161ca5058f6f1784c183671"),
    Site(key="cybersecpods.com", zone_id="827dcf45b712b711ea49e9bad1a92cd5"),
    # merill.net zone total -> Graph Permissions Explorer card.
    Site(
        key="graphpermissions.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
    ),
]


# httpRequests1dGroups query. We sum pageViews across the 30-day window.
# We deliberately avoid `groupBy` so a single row comes back per zone (faster
# and keeps the parsing dead simple).
_QUERY_ZONE_TOTALS = """
query ZoneTotals($zone: String!, $since: Date!, $until: Date!) {
  viewer {
    zones(filter: { zoneTag: $zone }) {
      httpRequests1dGroups(
        limit: 365
        filter: { date_geq: $since, date_lt: $until }
      ) {
        sum { pageViews }
      }
    }
  }
}
""".strip()


def _post_graphql(token: str, query: str, variables: dict) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        GRAPHQL_ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # Surface the response body — Cloudflare returns useful error JSON
        # that explains things like "no such zone" or "rate limited".
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(
            f"HTTP {exc.code} from Cloudflare GraphQL: {detail}"
        ) from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"network error talking to Cloudflare: {exc}") from exc

    if payload.get("errors"):
        raise RuntimeError(f"GraphQL errors: {payload['errors']}")
    return payload


def _sum_pageviews(payload: dict) -> int:
    """Walk a GraphQL response and sum pageViews across daily buckets."""
    try:
        zones = payload["data"]["viewer"]["zones"]
    except (KeyError, TypeError) as exc:
        raise RuntimeError(f"unexpected response shape: {payload}") from exc
    if not zones:
        # Token doesn't have access to this zone, or zone ID is wrong.
        return 0
    total = 0
    for zone in zones:
        for group in zone.get("httpRequests1dGroups", []):
            total += int(group["sum"]["pageViews"])
    return total


def fetch_pageviews(site: Site, token: str, since: str, until: str) -> int:
    """Return the 30-day summed pageViews for a single Site."""
    payload = _post_graphql(
        token,
        _QUERY_ZONE_TOTALS,
        {"zone": site.zone_id, "since": since, "until": until},
    )
    return _sum_pageviews(payload)


def fetch_all(token: str | None = None) -> tuple[dict[str, int], list[str]]:
    """Fetch pageviews for every tracked site.

    Returns (counts_by_key, failed_keys). When the token is missing or
    empty, returns ({}, []) and prints a notice — useful for local dev
    where you don't want to set the secret just to test PSGallery.
    """
    token = token if token is not None else os.environ.get("CLOUDFLARE_API_TOKEN", "")
    if not token:
        print("INFO  cloudflare: CLOUDFLARE_API_TOKEN not set; skipping section")
        return {}, []

    today = _dt.date.today()
    # httpRequests1dGroups is keyed by completed UTC days, so we end the
    # window at "today" (exclusive) to avoid a partial-day bucket.
    until = today.isoformat()
    since = (today - _dt.timedelta(days=WINDOW_DAYS)).isoformat()

    counts: dict[str, int] = {}
    failures: list[str] = []
    for site in SITES:
        try:
            count = fetch_pageviews(site, token, since, until)
        except RuntimeError as exc:
            print(f"WARN  cloudflare {site.key}: {exc}")
            failures.append(site.key)
            continue
        counts[site.key] = count
        print(f"OK    cloudflare {site.key}: {count:,} pageviews (last {WINDOW_DAYS}d)")
    return counts, failures
