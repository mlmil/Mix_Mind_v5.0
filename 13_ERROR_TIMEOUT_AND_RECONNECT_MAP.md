# ERROR_TIMEOUT_AND_RECONNECT_MAP

## OSC_REQUESTS
Default timeout 1.5s, retries=2 → three attempts / about 4.5s per unanswered request. Per-key event registered before send, removed in finally. No sequence IDs; receiver matches only address or shared __node__ key. No source-IP filtering. Concurrent requests to the same key can overwrite waiters; a late reply can satisfy a different request. Concurrent node dumps share __node__; serialize them. start() socket creation is not locked. connect() replaces client without stopping old receiver. stop() does not join thread or resolve pending waiters. No automatic reconnection/backoff supervisor exists.

## READBACK_AND_ORDER
Set confirmation waits 50ms then reads; it does not compare expected and actual. Batch and macros preserve order only within that call; another tool may interleave. UDP send success is not mixer acknowledgement. Multi-read tools are sequential, not atomic. overview stops at first timeout; detail/routing keep per-node errors. input_config blocks the event loop during native reads.

## HTTP
Each REST call creates an AsyncClient with 5s timeout, raises HTTP errors, then returns JSON or text. No retries or pooled client. URL path segments are quoted for data reads and definitions. Unknown formats are not validated locally. Most MS tool wrappers flatten parse, HTTP, socket and server errors into generic connection-help strings.

## WEBSOCKET
A fresh socket per call at derived /ws. open_timeout=5s; recv has no explicit timeout. Only first reply read; no path/method correlation and no broadcast demultiplexing. Nonzero error raises RuntimeError; missing body returns None. The separate read probes used external 3s bounds; production client does not. Persistent subscription, renewal, reconnect and topology re-discovery are absent. Browser code contains a 1s reconnect loop, but that does not implement reconnection in this MCP.

## PARSER_FAILURES
Unknown OSC tags are skipped without consuming their payload. Truncated strings/scalars may raise. Invalid meter count/length can raise outside receiver decode catch and kill receive thread. Node dump joins strings from the first matched response, with no multi-packet collection. Routing token parser assumes final fields. Nonfinite dB JSON may emit -Infinity, invalid in strict JSON. All should remain explicit limitations until corrected and tested.
