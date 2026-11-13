# Modified by CrisisAlpha-Lab, 2026-11-12: new module (not in upstream openbb-cboe 1.6.1).
# Part of a modified version of openbb-cboe 1.6.1 (AGPL-3.0-only, (c) OpenBB Inc.). See LICENSE / NOTICE.
"""Standard OCC option symbol filtering (pure logic; no openbb imports)."""
from __future__ import annotations

import re


def occ_re(symbol: str) -> re.Pattern[str]:
    """Pattern of a standard OCC option code: <ROOT><YYMMDD><C|P><strike x 1000, 8 digits>.

    ROOT is the underlying symbol upper-cased with '.' and '-' removed (BRK.B -> BRKB).
    """
    root = re.sub(r"[.\-]", "", symbol.upper())
    return re.compile(rf"^{re.escape(root)}[0-9]{{6}}[CP][0-9]{{8}}\Z")


def filter_standard(options: list[dict], symbol: str) -> tuple[list[dict], int]:
    """Drop non-standard contracts (e.g. the NVDA chain's adjusted "B1VDA..." codes, which the upstream parser
    splits into expiration "1" and then fails on). Returns (kept, number dropped)."""
    pat = occ_re(symbol)
    kept = [o for o in options if isinstance(o, dict) and pat.match(str(o.get("option") or ""))]
    return kept, len(options) - len(kept)
