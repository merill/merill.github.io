#!/usr/bin/env python3
"""Update _data/stats.yml from every configured stats source.

Currently fetches:
  * PowerShell Gallery download counts  (lib/psgallery.py)
  * Cloudflare 30-day pageviews         (lib/cloudflare.py)

Designed to run from .github/workflows/update-stats.yml on a daily
schedule, but also runnable locally with no external Python dependencies.

Usage:
    python3 scripts/update-stats.py [--dry-run]

Environment:
    CLOUDFLARE_API_TOKEN  Bearer token with Zone:Analytics:Read scope.
                          Optional locally; required in CI for the
                          cloudflare: section to populate.

Exit codes:
    0  success (file written, or --dry-run completed) with no failures
    1  one or more sources reported a failure, OR no sources produced data

To track a different package or site, edit lib/psgallery.py / lib/cloudflare.py.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path

# Make `lib.*` importable regardless of how the script is invoked.
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib import cloudflare, psgallery  # noqa: E402
from lib.format import format_short, yaml_quote  # noqa: E402

REPO_ROOT = SCRIPT_DIR.parent
STATS_FILE = REPO_ROOT / "_data" / "stats.yml"


def _render_section(
    name: str,
    description: str,
    keys_in_order: list[str],
    counts: dict[str, int],
    updated: str,
    *,
    count_label: str = "downloads",
) -> list[str]:
    """Render one top-level section (psgallery: or cloudflare:) as YAML lines.

    If `counts` is empty, returns an empty list so the section is omitted
    from the output entirely. That avoids producing `cloudflare:` with a
    `null` value, which Liquid lookups (`site.data.stats.cloudflare["x"]`)
    would otherwise blow up on.
    """
    if not counts:
        return []
    lines = [f"{name}:", f"  # {description}"]
    for key in keys_in_order:
        if key not in counts:
            # Skip keys we failed to fetch — leaves the YAML without
            # them, which makes the Liquid `{%- if s.display -%}` guard
            # silently hide the stat on the card.
            continue
        n = counts[key]
        # Quote the key if it contains characters YAML would otherwise
        # parse weirdly (dots, hyphens). Cheap and always correct.
        safe_key = yaml_quote(key) if any(c in key for c in ".-") else key
        lines.append(f"  {safe_key}:")
        lines.append(f"    {count_label}: {n}")
        lines.append(f"    display: {yaml_quote(format_short(n))}")
        lines.append(f"    updated: {yaml_quote(updated)}")
    return lines


def write_stats(
    psg_counts: dict[str, int],
    cf_counts: dict[str, int],
    updated: str,
) -> str:
    """Render the full YAML payload and return it as a string.

    Hand-written rather than using PyYAML so we don't add a runtime
    dependency to the workflow. Section ordering and key ordering are
    stable so diffs only show real value changes.
    """
    header = [
        "# Auto-generated stats consumed by _pages/home.md.",
        "#",
        "# This file is rewritten daily by .github/workflows/update-stats.yml",
        "# (which runs scripts/update-stats.py). Manual edits will be overwritten",
        "# on the next run.",
        "#",
        "# To change which packages or sites are tracked, edit",
        "# scripts/lib/psgallery.py and scripts/lib/cloudflare.py.",
        "",
    ]

    psg_section = _render_section(
        "psgallery",
        "PowerShell Gallery cumulative download counts.",
        psgallery.PACKAGES,
        psg_counts,
        updated,
        count_label="downloads",
    )

    cf_section = _render_section(
        "cloudflare",
        f"Cloudflare pageViews summed over the last {cloudflare.WINDOW_DAYS} days.",
        [s.key for s in cloudflare.SITES],
        cf_counts,
        updated,
        count_label="pageviews",
    )

    body = list(header)
    body.extend(psg_section)
    if psg_section and cf_section:
        body.append("")  # blank line between non-empty sections
    body.extend(cf_section)
    return "\n".join(body) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the new YAML to stdout instead of writing it",
    )
    args = parser.parse_args(argv)

    psg_counts, psg_failures = psgallery.fetch_all()
    cf_counts, cf_failures = cloudflare.fetch_all()

    if not psg_counts and not cf_counts:
        print("ERROR no sources produced any data; aborting", file=sys.stderr)
        return 1

    updated = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = write_stats(psg_counts, cf_counts, updated)

    if args.dry_run:
        print()
        print("--- would write to", STATS_FILE, "---")
        print(payload, end="")
    else:
        STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATS_FILE.write_text(payload, encoding="utf-8")
        print(f"\nWrote {STATS_FILE.relative_to(REPO_ROOT)}")

    return 1 if (psg_failures or cf_failures) else 0


if __name__ == "__main__":
    raise SystemExit(main())
