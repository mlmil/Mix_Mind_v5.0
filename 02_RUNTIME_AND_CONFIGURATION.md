# RUNTIME_AND_CONFIGURATION

## ENTRYPOINTS
`venv/bin/python -m xair_mcp.server` or installed console command `xair-mcp`. Distribution `xair-mcp` version 0.1.0; README branding Mix Mind v5.0. Python >=3.10, setuptools >=68 build backend. Declared dependencies: mcp>=1.2.0, httpx>=0.27, websockets>=12.0. No lockfile; pytest is used by tests but not declared as a runtime dependency.

## ENVIRONMENT
| Variable | Default | Use |
| --- | --- | --- |
| XAIR_HOST | unset | Lazy native target; required unless xair_connect called |
| MS_API_URL | http://127.0.0.1:8080 | HTTP base and derived WS URL |
| XAIR_PRESETS | project/presets/band_presets.json | Local macro read/write path |

## VERIFIED_LOCAL_CONFIGURATION
Codex config's xair entry points to this project's `venv/bin/python3`, module `xair_mcp.server`, cwd this project, XAIR_HOST=192.168.1.2 and MS_API_URL=http://127.0.0.1:8080. Config inspected, not edited; running process import freshness was not proven. The legacy `/Volumes/Kenobi/Mix Station MCP` does not exist and Kenobi is not mounted.

## INSTALLED_RUNTIME
```json
{
  "python": "3.12.13",
  "packages": {
    "mcp": "1.28.1",
    "httpx": "0.28.1",
    "websockets": "16.0",
    "pytest": "9.1.1",
    "xair-mcp": "0.1.0"
  }
}
```

## APP_IDENTITY
Local app reported XR18, IP 192.168.1.2, firmware 1.18. These are app-reported metadata, not a firmware query to the hardware. No app restart, server restart, package install or startup configuration changes were performed. API access depends on Mixing Station's desktop HTTP API setting; no enablement was changed.
