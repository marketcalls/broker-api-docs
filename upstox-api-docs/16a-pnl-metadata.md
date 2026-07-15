# Get Report Meta Data API

## Endpoint

**GET** `https://api.upstox.com/v2/trade/profit-loss/metadata`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| from_date | No | string | Start date (dd-mm-yyyy), must align with financial year |
| to_date | No | string | End date (dd-mm-yyyy), must align with financial year |
| segment | Yes | string | `EQ` (Equity), `FO` (Futures/Options), `COM` (Commodity), `CD` (Currency) |
| financial_year | Yes | string | Concatenated digits (e.g., "2324" for 2023-2024) |

## Response

```json
{
  "status": "success",
  "data": {
    "trades_count": 10,
    "page_size_limit": 5000
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1067 | Segment parameter required |
| UDAPI1066 | Invalid segment value |
| UDAPI1070 | Financial year parameter required |
| UDAPI1074 | Invalid financial year format |
| UDAPI100051 | Unrecognized financial year |
| UDAPI1075 | to_date must be >= from_date (dd-mm-yyyy) |
| UDAPI1105 | Dates fall outside specified financial year |
