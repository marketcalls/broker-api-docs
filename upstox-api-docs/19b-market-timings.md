# Market Timings API

## Endpoint

**GET** `https://api.upstox.com/v2/market/timings/{date}`

## Path Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| date | Yes | string | YYYY-MM-DD format |

## Response

| Field | Type | Description |
|-------|------|-------------|
| exchange | string | Exchange identifier |
| start_time | number | Opening timestamp (ms) |
| end_time | number | Closing timestamp (ms) |

## Supported Exchanges

MCX, NSE, NFO, CDS, BSE, BCD, BFO

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1088 | Invalid date format |
