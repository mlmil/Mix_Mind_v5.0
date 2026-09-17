# USB_ROUTING_MAP

## SIGNAL_DOMAINS
| Domain | Meaning | Evidence boundary |
| --- | --- | --- |
| Physical analog input | XR18 connector/A-D source | Reference or source enum; cabling not inspected |
| Channel source | Selected analog or USB input to processing | MS three fields and native source nodes |
| USB send XR18→host | Global source/tap feeding recording stream | routing/usb/01..18; separate from return selection |
| Ableton track input | Host selection from incoming USB stream | Not inspected |
| Ableton track output | Host stream sent back to mixer | Not inspected |
| USB return host→XR18 | U1..U18 candidate strip source | routing.srcCfg.1 / native rtnsrc |
| Active selector | Chooses A/D versus USB candidate | cfg.srcSel / preamp/rtnsw |
| Strip processing | Gate/dynamics/EQ/insert/mix etc. | Schema only |
| Bus/monitor path | Send target, bus processing and physical output routing | Separate graph edges; no flow test |

## GLOBAL_ROUTING_API_PATHS
Current MS output-routing definitions follow. These paths coexist with native routing nodes; do not infer absence from a legacy tree inspection.

| Path | Definition |
| --- | --- |
| outRouting.aux.0.src | {"type":"integer"} |
| outRouting.aux.0.tap | {"type":"integer"} |
| outRouting.aux.1.src | {"type":"integer"} |
| outRouting.aux.1.tap | {"type":"integer"} |
| outRouting.aux.2.src | {"type":"integer"} |
| outRouting.aux.2.tap | {"type":"integer"} |
| outRouting.aux.3.src | {"type":"integer"} |
| outRouting.aux.3.tap | {"type":"integer"} |
| outRouting.aux.4.src | {"type":"integer"} |
| outRouting.aux.4.tap | {"type":"integer"} |
| outRouting.aux.5.src | {"type":"integer"} |
| outRouting.aux.5.tap | {"type":"integer"} |
| outRouting.main.0.src | {"type":"integer"} |
| outRouting.main.1.src | {"type":"integer"} |
| outRouting.ultranet.0.src | {"type":"integer"} |
| outRouting.ultranet.0.tap | {"type":"integer"} |
| outRouting.ultranet.1.src | {"type":"integer"} |
| outRouting.ultranet.1.tap | {"type":"integer"} |
| outRouting.ultranet.10.src | {"type":"integer"} |
| outRouting.ultranet.10.tap | {"type":"integer"} |
| outRouting.ultranet.11.src | {"type":"integer"} |
| outRouting.ultranet.11.tap | {"type":"integer"} |
| outRouting.ultranet.12.src | {"type":"integer"} |
| outRouting.ultranet.12.tap | {"type":"integer"} |
| outRouting.ultranet.13.src | {"type":"integer"} |
| outRouting.ultranet.13.tap | {"type":"integer"} |
| outRouting.ultranet.14.src | {"type":"integer"} |
| outRouting.ultranet.14.tap | {"type":"integer"} |
| outRouting.ultranet.15.src | {"type":"integer"} |
| outRouting.ultranet.15.tap | {"type":"integer"} |
| outRouting.ultranet.2.src | {"type":"integer"} |
| outRouting.ultranet.2.tap | {"type":"integer"} |
| outRouting.ultranet.3.src | {"type":"integer"} |
| outRouting.ultranet.3.tap | {"type":"integer"} |
| outRouting.ultranet.4.src | {"type":"integer"} |
| outRouting.ultranet.4.tap | {"type":"integer"} |
| outRouting.ultranet.5.src | {"type":"integer"} |
| outRouting.ultranet.5.tap | {"type":"integer"} |
| outRouting.ultranet.6.src | {"type":"integer"} |
| outRouting.ultranet.6.tap | {"type":"integer"} |
| outRouting.ultranet.7.src | {"type":"integer"} |
| outRouting.ultranet.7.tap | {"type":"integer"} |
| outRouting.ultranet.8.src | {"type":"integer"} |
| outRouting.ultranet.8.tap | {"type":"integer"} |
| outRouting.ultranet.9.src | {"type":"integer"} |
| outRouting.ultranet.9.tap | {"type":"integer"} |
| outRouting.usbIf.0.src | {"type":"integer"} |
| outRouting.usbIf.0.tap | {"type":"integer"} |
| outRouting.usbIf.1.src | {"type":"integer"} |
| outRouting.usbIf.1.tap | {"type":"integer"} |
| outRouting.usbIf.10.src | {"type":"integer"} |
| outRouting.usbIf.10.tap | {"type":"integer"} |
| outRouting.usbIf.11.src | {"type":"integer"} |
| outRouting.usbIf.11.tap | {"type":"integer"} |
| outRouting.usbIf.12.src | {"type":"integer"} |
| outRouting.usbIf.12.tap | {"type":"integer"} |
| outRouting.usbIf.13.src | {"type":"integer"} |
| outRouting.usbIf.13.tap | {"type":"integer"} |
| outRouting.usbIf.14.src | {"type":"integer"} |
| outRouting.usbIf.14.tap | {"type":"integer"} |
| outRouting.usbIf.15.src | {"type":"integer"} |
| outRouting.usbIf.15.tap | {"type":"integer"} |
| outRouting.usbIf.16.src | {"type":"integer"} |
| outRouting.usbIf.16.tap | {"type":"integer"} |
| outRouting.usbIf.17.src | {"type":"integer"} |
| outRouting.usbIf.17.tap | {"type":"integer"} |
| outRouting.usbIf.2.src | {"type":"integer"} |
| outRouting.usbIf.2.tap | {"type":"integer"} |
| outRouting.usbIf.3.src | {"type":"integer"} |
| outRouting.usbIf.3.tap | {"type":"integer"} |
| outRouting.usbIf.4.src | {"type":"integer"} |
| outRouting.usbIf.4.tap | {"type":"integer"} |
| outRouting.usbIf.5.src | {"type":"integer"} |
| outRouting.usbIf.5.tap | {"type":"integer"} |
| outRouting.usbIf.6.src | {"type":"integer"} |
| outRouting.usbIf.6.tap | {"type":"integer"} |
| outRouting.usbIf.7.src | {"type":"integer"} |
| outRouting.usbIf.7.tap | {"type":"integer"} |
| outRouting.usbIf.8.src | {"type":"integer"} |
| outRouting.usbIf.8.tap | {"type":"integer"} |
| outRouting.usbIf.9.src | {"type":"integer"} |
| outRouting.usbIf.9.tap | {"type":"integer"} |

## NATIVE_GLOBAL_HELPER
`xair_routing_overview` reads 18 USB, 6 aux and 2 main-family nodes; parses final whitespace tokens as source/tap. Full native source/tap grammar and all outlet labels remain unverified. The static OSC dictionary lacks these global routing entries. No fresh global routing value audit was performed.

## REFERENCE_ONLY
Input 1 / strips 2 and 7 / U17 and U18 / L and R are intended associations. USB-send assignment and Ableton I/O are unknown in this pass. Do not reverse USB send and return direction, or label U17/U18 as monitor buses.
