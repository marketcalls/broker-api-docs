# Market Holidays API

## Endpoint

**GET** `https://api.upstox.com/v2/market/holidays`

Optional date-specific: `https://api.upstox.com/v2/market/holidays/{date}` (YYYY-MM-DD)

## Response

```json
{
  "status": "success",
  "data": [
    {
      "date": "2024-01-01",
      "description": "New Year Day",
      "holiday_type": "TRADING_HOLIDAY",
      "closed_exchanges": [],
      "open_exchanges": [
        {
          "exchange": "MCX",
          "start_time": 1704079800000,
          "end_time": 1704108600000
        }
      ]
    }
  ]
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| date | string | Holiday date (YYYY-MM-DD) |
| description | string | Holiday name |
| holiday_type | string | SETTLEMENT_HOLIDAY, TRADING_HOLIDAY, SPECIAL_TIMING |
| closed_exchanges | array | Exchanges closed |
| open_exchanges | array | Exchanges with modified hours |
| open_exchanges[].exchange | string | Exchange identifier |
| open_exchanges[].start_time | number | Opening timestamp (ms) |
| open_exchanges[].end_time | number | Closing timestamp (ms) |
