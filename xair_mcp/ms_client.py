"""Client for the Mixing Station Desktop app APIs (REST + WebSocket).

Mixing Station (desktop only) exposes:
- REST/HTTP + an interactive API explorer at http://localhost:<port>
- WebSocket with JSON frames: {"path": "...", "method": "GET|POST", "body": ...}
- Data paths like 'ch.0.mix.lvl' (0-based!), formats 'val' (plain) / 'norm'

Enable in Mixing Station: global app settings -> APIs -> enable REST.
Default port used here: 8080 (configurable via MS_API_URL env).
"""
from __future__ import annotations

import json
from typing import Any

import httpx

DEFAULT_URL = "http://127.0.0.1:8080"


class MixingStationClient:
    def __init__(self, base_url: str = DEFAULT_URL, timeout: float = 5.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    async def rest(self, path: str, method: str = "GET", body: Any = None) -> Any:
        """Raw REST passthrough to any Mixing Station endpoint."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.request(method.upper(), url,
                                        json=body if body is not None else None)
            resp.raise_for_status()
            try:
                return resp.json()
            except json.JSONDecodeError:
                return resp.text

    async def ws_call(self, path: str, method: str = "GET", body: Any = None) -> Any:
        """Single request/response over the WebSocket API."""
        import websockets  # lazy import
        ws_url = self.base_url.replace("http", "ws", 1) + "/ws"
        async with websockets.connect(ws_url, open_timeout=self.timeout) as ws:
            await ws.send(json.dumps({"path": path, "method": method.upper(),
                                      "body": body}))
            raw = await ws.recv()
            reply = json.loads(raw)
            if reply.get("error"):
                raise RuntimeError(f"Mixing Station API error: {reply['error']}")
            return reply.get("body")

    async def app_state(self) -> Any:
        return await self.ws_call("/app/state")

    async def get_value(self, data_path: str, fmt: str = "val") -> Any:
        """Read a console value, e.g. data_path='ch.0.mix.lvl' (0-based index)."""
        return await self.ws_call(f"/console/data/{fmt}/{data_path}", "GET")

    async def set_value(self, data_path: str, value: Any, fmt: str = "val") -> Any:
        return await self.ws_call(f"/console/data/{fmt}/{data_path}", "POST",
                                  {"value": value})


def connection_help(err: Exception, base_url: str) -> str:
    return (
        f"Could not reach Mixing Station API at {base_url} ({type(err).__name__}: {err}). "
        "Checklist: 1) Mixing Station DESKTOP app is running (APIs are desktop-only), "
        "2) REST API is enabled in global app settings -> APIs, "
        "3) the port matches (open http://localhost:<port> in a browser to see the API explorer), "
        "4) if a different port is configured, set env MS_API_URL, e.g. http://127.0.0.1:8080. "
        "Note: direct mixer control via the xair_* tools works without the app."
    )
