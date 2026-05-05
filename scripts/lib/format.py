"""Shared formatting helpers used by every stats source."""

from __future__ import annotations


def format_short(n: int) -> str:
    """Format an integer as a short, human-friendly string.

    Examples:
        303_721   -> "304k"
          5_577   -> "5.6k"
        1_000_000 -> "1.0m"
            842   -> "842"
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


def yaml_quote(s: str) -> str:
    """Return a YAML double-quoted string, escaping the bare minimum."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
