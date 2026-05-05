"""PowerShell Gallery download-count fetcher.

Hits the public OData v2 endpoint (no auth required) and returns a
{package_id: download_count} mapping. Failures for individual packages
are surfaced via the `failures` list rather than aborting the whole run,
so one transient error doesn't blank out the rest of the home page.
"""

from __future__ import annotations

import re
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "merill.net-stats-updater/1.0 (+https://merill.net)"
TIMEOUT_SECONDS = 30

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


def fetch_download_count(package_id: str) -> int:
    """Return the cumulative DownloadCount for a PSGallery package.

    Uses the OData v2 endpoint with $filter=Id eq '...' and IsLatestVersion
    so we get a single entry back. Raises RuntimeError on failure.
    """
    query = f"Id eq '{package_id}' and IsLatestVersion"
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


def fetch_all() -> tuple[dict[str, int], list[str]]:
    """Fetch every tracked package; return (counts, failed_ids)."""
    counts: dict[str, int] = {}
    failures: list[str] = []
    for package_id in PACKAGES:
        try:
            counts[package_id] = fetch_download_count(package_id)
        except RuntimeError as exc:
            print(f"WARN  psgallery: {exc}")
            failures.append(package_id)
    return counts, failures
