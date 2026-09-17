# MIXING_STATION_API_MAP

## EVIDENCE
Full OpenAPI schema captured from local `/openapi.json`; operations below are advertised, not all executed. Parameters, request bodies, response schemas and component references are preserved in `mixing_station_mcp_map.json` and the raw OpenAPI evidence.

## REST_AND_WEBSOCKET
HTTP reads return JSON; leaf read shape is `{format:"val",value:...}`. `definitions2` returns `{value:{...}}` for leaves and `{node:{...}}` for nodes. Live WS probes verified `/ws` works with `{path,method,body}` frames and current `/console/data/get/{path}/{format}`. The current client opens/closes a socket per request and returns the first frame body without path correlation. The app browser uses a root WS connection; that route was source-inspected, not separately probed.

## VERIFIED_PATH_DEFECT
`ms_value` builds `/console/data/{fmt}/{data_path}`: live probe returned Path not found. Current advertised paths are GET `/console/data/get/{path}/{format}` and POST `/console/data/set/{path}/{format}`. Only GET was probed. No implementation change made. `ms_api` is WS passthrough despite its generic name; there is no general REST MCP tool. REST definition helper is internal only.

## SUBSCRIPTIONS
Data subscribe/unsubscribe are WS-only. Subscriptions are connection-scoped; the one-shot client cannot provide a continuing stream. Null value/format events mean a path disappeared after console reconfiguration. Metering subscriptions also require a persistent consumer. Exact body shapes are in the schema.

## SAFETY_EXCEPTIONS
GET `/app/ui/selectedChannel/{nameOrIndex}` changes UI selection; GET `/development/crashTest` triggers a crash test. Neither was called. GET is not a read-only safety rule. Preset creation endpoints export current state but are conservatively classed write-capable and were not called.

## OPERATION_CATALOG
| Method | Path | Class | Summary |
| --- | --- | --- | --- |
| POST | /app/idcas | write-capable | Creates a new IDCA |
| POST | /app/idcas/rearrange | write-capable | Updates the IDCAs order |
| POST | /app/idcas/{index} | write-capable | Modifies a IDCA |
| POST | /app/idcas/{index}/delete | write-capable | Deletes an IDCA |
| GET | /app/mixers/available | read-only | Get mixer models |
| POST | /app/mixers/connect | write-capable | Connect |
| GET | /app/mixers/current | read-only | Get currently selected mixer |
| POST | /app/mixers/disconnect | write-capable | Disconnect |
| POST | /app/mixers/offline | write-capable | Start offline mode |
| POST | /app/mixers/search | write-capable | Start mixer search |
| GET | /app/mixers/searchResults | read-only | Get search results |
| GET | /app/network/interfaces | read-only | Get network interfaces |
| POST | /app/network/interfaces/primary | write-capable | Override primary interface |
| POST | /app/presets/channel/apply | write-capable | Recalls the given MS Preset data |
| POST | /app/presets/channel/create | write-capable | Returns the state of a single channel as MS Preset |
| GET | /app/presets/lastError | read-only | Returns any error messages that occurred during the last  recall |
| POST | /app/presets/scenes/apply | write-capable | Recalls the given MS Scene data |
| POST | /app/presets/scenes/create | write-capable | Returns the current mixer state as MS Scene |
| GET | /app/presets/scopes | read-only | Returns all available scopes |
| GET | /app/presets/state | read-only | Get preset recall state |
| POST | /app/save | write-capable | Saves the current app settings |
| GET | /app/state | read-only | Get app state |
| GET | /app/ui/selectedChannel | read-only | Returns the currently selected channel |
| GET | /app/ui/selectedChannel/{nameOrIndex} | write-capable | Sets the currently selected channel, either by name or index |
| GET | /console/auth/info | read-only | Returns the security details about this mixer |
| POST | /console/auth/login | write-capable | Logs in to the mixer using the given credentials. |
| GET | /console/data/categories | read-only | Returns all data categories. |
| GET | /console/data/definitions/{path} | read-only | Returns the data definitions for the given path |
| GET | /console/data/definitions2/{path} | read-only | Returns the data definitions for the given paths |
| GET | /console/data/get/{path}/{format} | read-only | Returns the current value at the given path. |
| GET | /console/data/paths | read-only | Returns all data paths available for the current mixer |
| GET | /console/data/paths/{path} | read-only | Returns a sub-path |
| POST | /console/data/set/{path}/{format} | write-capable | Sets the value at the given path. |
| POST | /console/data/subscribe | diagnostic | Subscribe data |
| POST | /console/data/unsubscribe | diagnostic | Unsubscribe data |
| GET | /console/information | read-only | Returns details about the channel architecture of this mixer. |
| POST | /console/metering/subscribe | diagnostic | Subscribe metering |
| POST | /console/metering/unsubscribe | diagnostic | Unsubscribe metering |
| POST | /console/metering2/subscribe | diagnostic | Subscribe metering |
| GET | /console/mixTargets | read-only | Returns all signal sinks which can be used as mix target for the channels |
| GET | /console/onConfigChanged | diagnostic | Mixer config changed event |
| GET | /convert/{path}/ntov/{val} | read-only | Converts from normalized to unit format. |
| GET | /convert/{path}/vton/{val} | read-only | Converts from a unit value to a normalized value. |
| GET | /development/crashTest | write-capable | Crash test |
| GET | /rf/connectors | read-only | Get connectors |
| GET | /rf/devices | read-only | Get all RF device config |
| POST | /rf/devices/add | write-capable | Adds a new RF device |
| POST | /rf/devices/remove/{uid} | write-capable | Removes a RF device |
| GET | /rf/search/results | read-only | Get search results |
| POST | /rf/search/start | write-capable | Start search |
| POST | /rf/search/stop | write-capable | Stop search |

## POST_/app/idcas
```json
{
  "summary": "Creates a new IDCA",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-d"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-bz-b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "This will add a new IDCA with the given members.Afterwards the new IDCA will appear in the data tree as 'idca.X' where X is the index of the newly created IDCA returned in the reply."
}
```

## POST_/app/idcas/rearrange
```json
{
  "summary": "Updates the IDCAs order",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-f"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-bz-b$a"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "This will update the position of the IDCAs. The given list represents the source indices of the existing IDCAs"
}
```

## POST_/app/idcas/{index}
```json
{
  "summary": "Modifies a IDCA",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-d"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-bz-b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Modifies the members of an existing IDCA with the given index.",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "index",
      "required": true
    }
  ]
}
```

## POST_/app/idcas/{index}/delete
```json
{
  "summary": "Deletes an IDCA",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "This will delete the existing IDCA with the given index. Note that this might change the index of all IDCAs after the given index.",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "index",
      "required": true
    }
  ]
}
```

## GET_/app/mixers/available
```json
{
  "summary": "Get mixer models",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ce-d"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns all supported mixer models."
}
```

## POST_/app/mixers/connect
```json
{
  "summary": "Connect",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-ce-b"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Connects to the mixer with the given IP/Hostname and model id"
}
```

## GET_/app/mixers/current
```json
{
  "summary": "Get currently selected mixer",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ce-d$b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns the meta-data of the currently used mixer."
}
```

## POST_/app/mixers/disconnect
```json
{
  "summary": "Disconnect",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Stops the network stack and return to the initial app state"
}
```

## POST_/app/mixers/offline
```json
{
  "summary": "Start offline mode",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-ce-h"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Starts the offline mode for mixers of the given series and model."
}
```

## POST_/app/mixers/search
```json
{
  "summary": "Start mixer search",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-ce-g"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Starts searching for mixers of the given variant."
}
```

## GET_/app/mixers/searchResults
```json
{
  "summary": "Get search results",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ce-e"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns a list of all mixers found in the network (of the current selected series)"
}
```

## GET_/app/network/interfaces
```json
{
  "summary": "Get network interfaces",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ce-f"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns all network interfaces and their current status"
}
```

## POST_/app/network/interfaces/primary
```json
{
  "summary": "Override primary interface",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-e"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ce-f"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Enforces the NIC with the given name as primary. This must be set before starting any search / connection process"
}
```

## POST_/app/presets/channel/apply
```json
{
  "summary": "Recalls the given MS Preset data",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cc-b"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": ""
}
```

## POST_/app/presets/channel/create
```json
{
  "summary": "Returns the state of a single channel as MS Preset",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cc-c"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cc-b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/app/presets/lastError
```json
{
  "summary": "Returns any error messages that occurred during the last  recall",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-i"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## POST_/app/presets/scenes/apply
```json
{
  "summary": "Recalls the given MS Scene data",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cc-d"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": ""
}
```

## POST_/app/presets/scenes/create
```json
{
  "summary": "Returns the current mixer state as MS Scene",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cc-d"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/app/presets/scopes
```json
{
  "summary": "Returns all available scopes",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cc-f"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/app/presets/state
```json
{
  "summary": "Get preset recall state",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ca-c"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns the current state of the preset recall subsystem"
}
```

## POST_/app/save
```json
{
  "summary": "Saves the current app settings",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "This will persist all app settings"
}
```

## GET_/app/state
```json
{
  "summary": "Get app state",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-ca-b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns the current state of the app."
}
```

## GET_/app/ui/selectedChannel
```json
{
  "summary": "Returns the currently selected channel",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-a"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/app/ui/selectedChannel/{nameOrIndex}
```json
{
  "summary": "Sets the currently selected channel, either by name or index",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-a"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "nameOrIndex",
      "required": true
    }
  ]
}
```

## GET_/console/auth/info
```json
{
  "summary": "Returns the security details about this mixer",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cd-c"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## POST_/console/auth/login
```json
{
  "summary": "Logs in to the mixer using the given credentials.",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cd-b"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cd-a"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/console/data/categories
```json
{
  "summary": "Returns all data categories.",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-c"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/console/data/definitions/{path}
```json
{
  "summary": "Returns the data definitions for the given path",
  "deprecated": true,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-d"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    }
  ]
}
```

## GET_/console/data/definitions2/{path}
```json
{
  "summary": "Returns the data definitions for the given paths",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-e"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    }
  ]
}
```

## GET_/console/data/get/{path}/{format}
```json
{
  "summary": "Returns the current value at the given path.",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-m"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Format can be 'val' or 'norm' representing the actual value or a normalized value ranging from 0-1",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    },
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "format",
      "required": true
    }
  ]
}
```

## GET_/console/data/paths
```json
{
  "summary": "Returns all data paths available for the current mixer",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-f"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/console/data/paths/{path}
```json
{
  "summary": "Returns a sub-path",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-f"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    }
  ]
}
```

## POST_/console/data/set/{path}/{format}
```json
{
  "summary": "Sets the value at the given path.",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cb-m"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-m"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "See 'get' for format parameter description. If the given numeric value isn't supported by the mixer it will be rounded to the closest matching value.",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    },
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "format",
      "required": true
    }
  ]
}
```

## POST_/console/data/subscribe
```json
{
  "summary": "Subscribe data",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-h"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Subscribes to the data matching the given pattern. Can only be called from a websocket.\n\nCreating a subscription will cause the app to send the values if a new subscription was created, as well as on every change.\nA single * may be used to indicate a wildcard for a single path segment.\n\nIf a value doesn't exist anymore due to a mixer configuration change (for example stereo bus gets unlinked) a value update with value=null, format=null will be sent."
}
```

## POST_/console/data/unsubscribe
```json
{
  "summary": "Unsubscribe data",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-h"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Unsubscribes the data matching the given pattern. The path must match 1:1 the path used for the subscription. Can only be called from a websocket."
}
```

## GET_/console/information
```json
{
  "summary": "Returns details about the channel architecture of this mixer.",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## POST_/console/metering/subscribe
```json
{
  "summary": "Subscribe metering",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-i"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": true,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Subscribes to the metering values of channels. The metering data will be sent to '/console/metering/{id}'. If a channel is stereo two values will be included (L/R). You can call this request multiple times, either to update an existing subscription or to subscribe to different channels with a different id.\n\nThe interval parameter defines the data rate in milliseconds (global per client).\n\nSetting 'binary' to true will cause the reply to contain a base64 encoded string (non-padded). The format is the following:\n\nint16 fixed float point (factor 100) big endian"
}
```

## POST_/console/metering/unsubscribe
```json
{
  "summary": "Unsubscribe metering",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-a"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Unsubscribes the metering request with the given id"
}
```

## POST_/console/metering2/subscribe
```json
{
  "summary": "Subscribe metering",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-bz-j"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Subscribes to the metering values. The detailed description about this endpoint is in the manual"
}
```

## GET_/console/mixTargets
```json
{
  "summary": "Returns all signal sinks which can be used as mix target for the channels",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-bz-g"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## GET_/console/onConfigChanged
```json
{
  "summary": "Mixer config changed event",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Websocket only. Gets broadcast to all clients if the mixer configuration has been changed. This may happen for mixers which have configurable mono/stereo channel counts."
}
```

## GET_/convert/{path}/ntov/{val}
```json
{
  "summary": "Converts from normalized to unit format.",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-m"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Converts the given normalized value using the convertion used at the given path to the actual value",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    },
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "val",
      "required": true
    }
  ]
}
```

## GET_/convert/{path}/vton/{val}
```json
{
  "summary": "Converts from a unit value to a normalized value.",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cb-m"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Converts the given unit value using the convertion used at the given path to a normalized value",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "path",
      "required": true
    },
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "val",
      "required": true
    }
  ]
}
```

## GET_/development/crashTest
```json
{
  "summary": "Crash test",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Creates an unhandled exception to test the crash behavior"
}
```

## GET_/rf/connectors
```json
{
  "summary": "Get connectors",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cf-b"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns all RF connectors that are available"
}
```

## GET_/rf/devices
```json
{
  "summary": "Get all RF device config",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cf-c"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": ""
}
```

## POST_/rf/devices/add
```json
{
  "summary": "Adds a new RF device",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cf-a"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "When adding via search use the searchId!"
}
```

## POST_/rf/devices/remove/{uid}
```json
{
  "summary": "Removes a RF device",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "",
  "parameters": [
    {
      "schema": {
        "exampleSetFlag": false,
        "types": [
          "string"
        ],
        "type": "string"
      },
      "in": "path",
      "name": "uid",
      "required": true
    }
  ]
}
```

## GET_/rf/search/results
```json
{
  "summary": "Get search results",
  "deprecated": false,
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "exampleSetFlag": false,
            "$ref": "#/components/schemas/blob-cf-d"
          },
          "exampleSetFlag": false
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/apiError"
    },
    "500": {
      "$ref": "#/components/responses/unhandledError"
    },
    "404": {
      "$ref": "#/components/responses/apiNotFound"
    }
  },
  "description": "Returns a list of all rf devices found in the network (of the currently selected connector)"
}
```

## POST_/rf/search/start
```json
{
  "summary": "Start search",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "exampleSetFlag": false,
          "$ref": "#/components/schemas/blob-cf-e"
        },
        "exampleSetFlag": false
      }
    }
  },
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Starts searching for rf devices using the given connector id"
}
```

## POST_/rf/search/stop
```json
{
  "summary": "Stop search",
  "deprecated": false,
  "responses": {
    "204": {
      "$ref": "#/components/responses/noResponse"
    }
  },
  "description": "Stops searching for devices"
}
```

## OFFICIAL_DOCUMENTATION
[Mixing Station API documentation](https://mixingstation.app/ms-docs/use-cases/apis/) describes the desktop API and WebSocket envelope. Exact endpoint availability and schemas in this map come from the captured local OpenAPI, which takes precedence over generic examples.
