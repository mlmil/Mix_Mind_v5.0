# KNOWN_LIMITATIONS

## REGISTER
| ID | Evidence | Limitation |
| --- | --- | --- |
| L01 | VERIFIED_READ | ms_value uses rejected legacy WS data path; current get route works. |
| L02 | VERIFIED_SOURCE | WS first-frame handling lacks correlation and recv deadline; subscriptions cannot persist. |
| L03 | VERIFIED_SOURCE | Concurrent same-address and __node__ reads collide in shared pending map. |
| L04 | VERIFIED_SOURCE | Invalid meter blobs may terminate RX thread; freshness and equal-frame dedup bias meter summaries. |
| L05 | VERIFIED_SOURCE | OSC unknown types, truncated blobs and bundles not safely supported. |
| L06 | VERIFIED_SOURCE | Source selector maps every non-1 number to A/D; hardcoded labels and unchecked int(float(...)) accept invalid data. |
| L07 | VERIFIED_READ | MS and native names differ on strips 2/7; cache/translation cause unknown. Source choice agrees after decoding. |
| L08 | VERIFIED_SOURCE | Native rtnsrc and global routing missing from static dictionary; routing helper token semantics not exhaustively verified. |
| L09 | VERIFIED_SOURCE | Channel detail assumes physical headamp index equals strip index, invalid as a general source association. |
| L10 | VERIFIED_SOURCE | DCA fader/mute helpers append /mix/* but dictionary describes /dca/N/fader and /dca/N/on. |
| L11 | VERIFIED_SOURCE | FX high enum indices are explicitly approximate; expansion claims headamps 1..24 on an XR18 without validation. |
| L12 | VERIFIED_SOURCE | readOnlyHint is advisory; arbitrary GET can select UI or crash app. |
| L13 | VERIFIED_SOURCE | Backup is fixed coverage, snapshot timeout looks used, writes lack complete validation/rollback. |
| L14 | VERIFIED_SOURCE | No MS tests, schema regression tests, concurrent request tests or malformed-packet tests. |
| L15 | VERIFIED_SOURCE | README tool inventory is stale and clipping-detection wording exceeds meter summarizer implementation. |
| L16 | UNKNOWN | Full native counterpart of MS analog None, all physical output routing enum semantics and every FX algorithm schema not established. |
| L17 | VERIFIED_SOURCE | Negative enum indices can decode to final colors/FX labels; upper-bound-only tests omit lower bound. |
| L18 | VERIFIED_SOURCE | Unit laws are generic source assumptions; roundtrip tests do not establish hardware calibration. |
| L19 | VERIFIED_SOURCE | HTTP clients have no authentication configuration; base URL can target nonlocal hosts. Existing local API uses no explicit auth in these reads. |

## CHANGE_POLICY
No source patches or restarts in this mapping pass. Existing modified source files were preserved. Findings are documented so future corrections can be individually backed up, tested offline and reviewed without coupling reads to writes.
