# Historical Candle Data

## Endpoint

**GET** `/instruments/historical/:instrument_token/:interval`

Retrieves archived candle records spanning several years.

## URI Parameters

| Parameter | Description |
|-----------|-------------|
| `:instrument_token` | Instrument ID from instrument list API |
| `:interval` | `minute`, `3minute`, `5minute`, `10minute`, `15minute`, `30minute`, `60minute`, `day` |

## Query Parameters

| Parameter | Description |
|-----------|-------------|
| `from` | Start date: `yyyy-mm-dd hh:mm:ss` |
| `to` | End date: `yyyy-mm-dd hh:mm:ss` |
| `continuous` | `1` for continuous futures data (NFO/MCX); default `0` |
| `oi` | `1` to include Open Interest; default `0` |

## Response

Each candle: `[timestamp, open, high, low, close, volume]`

With `oi=1`: `[timestamp, open, high, low, close, volume, open_interest]`

```json
{
  "status": "success",
  "data": {
    "candles": [
      ["2017-12-15T09:15:00+0530", 1704.5, 1705, 1699.25, 1702.8, 2499],
      ["2017-12-15T09:16:00+0530", 1702, 1702, 1698.15, 1698.15, 1271]
    ]
  }
}
```

## Continuous Data

Exchanges flush `instrument_token` for F&O contracts every expiry. Use `continuous=1` with a live contract token to get day candles across contract rollovers for expired contracts.

## Rate Limit

3 requests/second
