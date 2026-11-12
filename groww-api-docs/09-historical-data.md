# Source: https://groww.in/trade-api/docs/curl/historical-data

# Historical Data

## Legacy Candle Range Endpoint (Deprecated)

> Groww marks this API as deprecated and says it will not work in the future. Use [Get Historical Candle Data](10-backtesting.md#get-historical-candle-data) instead.

`GET https://api.groww.in/v1/historical/candle/range`

Required query parameters: `exchange`, `segment`, `trading_symbol`, `start_time`, and `end_time`. Times accept `yyyy-MM-dd HH:mm:ss` or epoch seconds. `interval_in_minutes` specifies the candle interval.

```bash
curl -G 'https://api.groww.in/v1/historical/candle/range' \
  --data-urlencode 'exchange=NSE' --data-urlencode 'segment=CASH' \
  --data-urlencode 'trading_symbol=WIPRO' \
  --data-urlencode 'start_time=2021-01-01 09:15:00' \
  --data-urlencode 'end_time=2021-01-01 15:15:00' \
  --data-urlencode 'interval_in_minutes=5' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

The response `payload.candles` is an array of arrays. Each candle contains timestamp in epoch seconds, open, high, low, close, and volume, in that order. Prices are rupees.

| Candle interval | Maximum request range | Data availability |
| --- | --- | --- |
| 1 minute | 7 days | Last 3 months |
| 5 minutes | 15 days | Last 3 months |
| 10 minutes | 30 days | Last 3 months |
| 1 hour (60 minutes) | 150 days | Last 3 months |
| 4 hours (240 minutes) | 365 days | Last 3 months |
| 1 day (1440 minutes) | 1080 days (~3 years) | Full history |
| 1 week (10080 minutes) | No limit | Full history |

For the current endpoint and FNO historical workflows, see [Backtesting](10-backtesting.md).
