"""Cloudflare GraphQL Analytics fetcher.

Pulls 30-day pageView counts per site from the public GraphQL Analytics API
and returns a {key: count} mapping where `key` is whatever string is used
as a card lookup in stats.yml — usually a hostname.

A SITES list below maps each tracked card to a (zone_name, zone_id, hostname)
triple. When `hostname` is None we sum the entire zone (one zone == one site).
When `hostname` is set we filter to that exact hostname inside the shared zone
(used for *.merill.net subdomains).

Authentication is via a single Bearer token passed in CLOUDFLARE_API_TOKEN.
The token only needs Zone:Analytics:Read scope.

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
    """A single tracked site.

    `key`       Stable identifier used as the YAML key under cloudflare:.
                Usually equal to the public hostname.
    `zone_id`   Cloudflare zone ID (32-char hex).
    `hostname`  If set, restrict the query to this exact request hostname
                (needed when several sites share one zone, e.g. *.merill.net).
                If None, sum the entire zone.
    """

    key: str
    zone_id: str
    hostname: str | None = None


# Zone IDs come from `cloudflare zones list`. To track an additional card,
# add a new Site() entry here AND wire the matching key into _pages/home.md.
SITES: list[Site] = [
    # --- One zone == one site (no hostname filter) ---
    Site(key="maester.dev", zone_id="a153599f0ecad99b19f2e71986a761f7"),
    Site(key="cmd.ms", zone_id="c9a63474a8b4304664a85b352cb8519b"),
    Site(key="getyako.com", zone_id="628baf20d90649a562b19d3b2e0c319e"),
    Site(key="bluesky.ms", zone_id="482b18b12d6730727612a4719c665a5b"),
    Site(key="lokka.dev", zone_id="a0e07884417766a7fd5edf97ecd06eed"),
    Site(key="graph.pm", zone_id="86e542369b5c343bb4348aba345d3f92"),
    Site(key="vscodemcp.com", zone_id="7d31153d3161ca5058f6f1784c183671"),
    # --- Subdomains of merill.net (shared zone, filtered by hostname) ---
    Site(
        key="mc.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
        hostname="mc.merill.net",
    ),
    Site(
        key="graphpermissions.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
        hostname="graphpermissions.merill.net",
    ),
    Site(
        key="uninstall-graph.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
        hostname="uninstall-graph.merill.net",
    ),
    Site(
        key="idpowertoys.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
        hostname="idpowertoys.merill.net",
    ),
    Site(
        key="signin.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
        hostname="signin.merill.net",
    ),
    Site(
        key="zerotrustexplorer.merill.net",
        zone_id="c41e33746f7a903ec87f23ac3f991943",
        hostname="zerotrustexplorer.merill.net",
    ),
]


# httpRequests1dGroups query. We sum pageViews across the 30-day window.
# When a hostname filter is needed we add `clientRequestHTTPHost` to the
# filter object — it's an indexable dimension on this dataset.
#
# We deliberately avoid `groupBy` so a single row comes back per zone (faster
# and keeps the parsing dead simple).
_QUERY_WHOLE_ZONE = """
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

_QUERY_HOSTNAME = """
query HostnameTotals($zone: String!, $since: Date!, $until: Date!, $host: String!) {
  viewer {
    zones(filter: { zoneTag: $zone }) {
      httpRequests1dGroups(
        limit: 365
        filter: {
          date_geq: $since,
          date_lt: $until,
          clientRequestHTTPHost: $host
        }
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
    if site.hostname is None:
        payload = _post_graphql(
            token,
            _QUERY_WHOLE_ZONE,
            {"zone": site.zone_id, "since": since, "until": until},
        )
    else:
        payload = _post_graphql(
            token,
            _QUERY_HOSTNAME,
            {
                "zone": site.zone_id,
                "since": since,
                "until": until,
                "host": site.hostname,
            },
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
        label = site.hostname or site.key
        try:
            count = fetch_pageviews(site, token, since, until)
        except RuntimeError as exc:
            print(f"WARN  cloudflare {label}: {exc}")
            failures.append(site.key)
            continue
        counts[site.key] = count
        print(f"OK    cloudflare {label}: {count:,} pageviews (last {WINDOW_DAYS}d)")
    return counts, failures
