# Source: https://groww.in/trade-api/docs/curl/user

# User Profile

## Get User Profile

`GET https://api.groww.in/v1/user/detail`

Returns identifiers, exchange enablement, active segments, and DDPI status.

```bash
curl -X GET 'https://api.groww.in/v1/user/detail' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Example response:

```json
{
  "status": "SUCCESS",
  "payload": {
    "vendor_user_id": "d86890d1-c60d-4ebd-9730-4f451670",
    "ucc": "924189",
    "nse_enabled": true,
    "bse_enabled": true,
    "ddpi_enabled": false,
    "active_segments": ["CASH", "FNO"]
  }
}
```

`vendor_user_id` is the user identifier; `ucc` is the Unique Client Code. `nse_enabled` and `bse_enabled` indicate exchange trading access. `ddpi_enabled` reports DDPI status. `active_segments` lists enabled segments. Groww notes that commodity may appear in this list, but API trading currently supports only `CASH` and `FNO`.
