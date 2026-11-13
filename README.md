# openbb-cboe (CrisisAlpha-Lab modified)

A modified copy of openbb-cboe 1.6.1 ([PyPI](https://pypi.org/project/openbb-cboe/1.6.1/); the CBOE provider extension
for OpenBB Platform), published as the corresponding source of the OpenBB sidecar that runs it. Package version
`1.6.1+crisis1`, git tag `v1.6.1+crisis1`. It replaces upstream `openbb-cboe`; do not install both.

License: AGPL-3.0-only, same as upstream (see `LICENSE` and `NOTICE`).

## What changed

Only the CBOE options-chain path (`models/options_chains.py`) and the provider description differ from upstream
(every changed block is marked `CrisisAlpha-Lab`; all other upstream files are byte-identical):

- Non-standard OCC contracts are dropped before parsing (`utils/occ.py`). Some chains, for example NVDA's, contain
  adjusted codes such as `B1VDA261113C00160000`; the upstream parser splits them into a bogus expiration and the
  whole request fails. Standard codes are `<ROOT><YYMMDD><C|P><strike x 1000, 8 digits>`, with the root being the
  underlying symbol without `.` / `-` (`BRK.B` -> `BRKB`). The number of dropped contracts is reported as
  `dropped_nonstandard` in the result metadata.
- The CBOE snapshot time (UTC) is exposed as `quote_timestamp_utc` in the result metadata. A single symbol's snapshot
  can be hours old; upstream's `last_trade_timestamp` is US/Eastern local time, so the two must not be mixed.
- The quote request checks the HTTP status (`utils/status.py`): 429 raises `[cboe:quota] ...`, any other status
  >= 400 raises `[cboe:upstream] HTTP <status>`, and network-layer exceptions are re-raised as the class name only
  (`[cboe:upstream] <ExceptionClass>`). Upstream used a default callback that never looked at the status code.
- The `Provider` description names this repository.

## Integrity

`PUBLISHED.json` records `repo`, `tag`, `commit` and `tree_sha256`. `tree_sha256` is the SHA-256 over, for every file
except `PUBLISHED.json` (and any `__pycache__/` or `*.pyc`) in POSIX path order, `relative path + NUL + content with
LF line endings + NUL`, stored as a decimal integer. In this public copy `commit` is `null` (a commit cannot contain
its own hash).

## Install

```bash
uv pip install --no-deps .
```
