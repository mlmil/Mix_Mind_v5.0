# SNAPSHOT_SCENE_MACRO_MAP

## NATIVE_SNAPSHOTS
`/-snap/NN/name` slots 1..64; `/-snap/save` and `/-snap/load` are actions. Listing returns only nonempty names, but timeout placeholders can appear as used slots. Save reports name readback, not full-state validation. Load reports command sent, not observed recall completion. Slot-64 protection caveat exists in source but was not independently verified. No list/save/load called.

## MIXING_STATION_PRESETS
Current advertised endpoints are `/app/presets/scenes/create`, `/app/presets/scenes/apply`, `/app/presets/channel/create`, `/app/presets/channel/apply`, `/app/presets/scopes`, `/app/presets/state`, `/app/presets/lastError`. Exact bodies/scopes are in OpenAPI. Browser bundle contains older `/app/scenes/*` references; these are not the authoritative current schema. No presets exported or recalled.

## MCP_MACROS
Local JSON stores `macros[name]={description,operations}`. Operations have address, value, optional unit and repeat_ch inclusive range. Expansion replaces two-digit `/ch/NN/`; no transaction, rollback, range validation or confirmation exists. Save rewrites the file without a lock/atomic rename. Macro run sends operations serially with 2ms pauses. Macros are not native snapshots or MS presets.

## LOCAL_MACRO_CATALOG
| Name | Description | Stored ops |
| --- | --- | --- |
| line_check_safe | Safe starting point for line check: all channel faders to -30dB, unmuted, LR master at -20dB, phantom untouched. | 3 |
| mute_all_inputs | Mute every input channel 1-16 (does not touch LR, buses or FX returns). | 1 |
| unmute_all_inputs | Unmute every input channel 1-16. | 1 |
| break_music | Set break: mute all inputs, unmute aux/USB return (ch 17/18 playback) and set it to -12dB into LR. | 4 |
| show_mode | Back from break: mute the aux/USB playback, unmute all inputs. | 2 |
| kill_fx | Panic: mute all 4 FX returns (kills reverb/delay tails instantly, e.g. for talking between songs). | 4 |
| restore_fx | Unmute all 4 FX returns. | 4 |

## BACKUP_BOUNDARY
`xair_backup_dump` writes text from a fixed BACKUP_NODES list; despite ENTIRE wording it is not a proven exhaustive snapshot. It omits some send detail for return families and future/unknown nodes. No restore tool exists. Existing backups were listed only; no new console backup was requested or executed.
