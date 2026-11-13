# Modified by CrisisAlpha-Lab, 2026-11-12: new module (not in upstream openbb-cboe 1.6.1).
# Part of a modified version of openbb-cboe 1.6.1 (AGPL-3.0-only, (c) OpenBB Inc.). See LICENSE / NOTICE.
"""HTTP status classification for the CBOE quote request (pure logic; no openbb imports)."""
from __future__ import annotations

from typing import Optional


def classify_status(status: int) -> Optional[str]:
    """429 -> "quota"; any other status >= 400 -> "upstream"; otherwise None (not an error)."""
    if status == 429:
        return "quota"
    if status >= 400:
        return "upstream"
    return None
