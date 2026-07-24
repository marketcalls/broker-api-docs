# Change Log

## API & WebSocket Configuration Update

This release introduces breaking changes to the API and WebSocket endpoints. Clients must update their configuration as described below.

### 1. Base URL Endpoint Change

The base URL for all REST API requests changed from `PiConnectTP` to `PiConnectAPI`:

```
https://piconnect.flattrade.in/PiConnectTP/
                    ↓
https://piconnect.flattrade.in/PiConnectAPI/
```

All existing REST endpoints (Holdings, Orders, Positions, etc.) must now be accessed using the updated base URL.

### 2. WebSocket URL Endpoint Change

The WebSocket connection URL changed from `PiConnectWSTp` to `PiConnectWSAPI`:

```
wss://piconnect.flattrade.in/PiConnectWSTp/
                    ↓
wss://piconnect.flattrade.in/PiConnectWSAPI/
```

Connections to the old WebSocket URL are rejected.

### 3. Socket Connection Payload Change

The socket connection initialization payload changed as follows:

**Previous payload:**

```json
{
  "t": "c",
  "uid": "FZ00000",
  "actid": "FZ00000",
  "source": "API",
  "susertoken": "<token>"
}
```

**Updated payload:**

```json
{
  "t": "a",
  "uid": "FZ00000",
  "actid": "FZ00000",
  "source": "API",
  "accesstoken": "<token>"
}
```

### Summary of Changes

| Item | Change |
| --- | --- |
| Base URL Endpoint | REST API base endpoint updated |
| WebSocket URL Endpoint | WebSocket endpoint updated |
| Payload Field | `"t": "c"` → `"t": "a"` — socket connection type updated |
| Auth Field | `"susertoken"` → `"accesstoken"` — authentication token field renamed |

### Action Required

- Update the Base URL configuration in your application
- Update the WebSocket connection URL
- Use the updated socket connection payload
