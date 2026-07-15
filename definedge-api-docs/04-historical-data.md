# Historical Data

| Particular | Details |
| --- | --- |
| API Name | Historical Data API |
| URL | `https://data.definedgesecurities.com/sds/history/{segment}/{token}/{timeframe}/{from}/{to}` |
| Method | GET |
| Produces | text/csv |

## Request Header

| Header | Value |
| --- | --- |
| Authorization | Actual value of `api_session_key` (received from token response) |

## Description

Data for various timeframes is available as follows:

| Timeframe | Availability |
| --- | --- |
| Daily | Last 20 years |
| Intraday | Last 6 months |
| Tick | Last 2 trading sessions |

## Request URL format

| Parameter | Values / Format |
| --- | --- |
| `segment` | NSE / BSE / NFO / BFO / CDS / MCX |
| `token` | Token from the Master file |
| `timeframe` | day / minute / tick |
| `from` | `ddMMyyyyHHmm` format |
| `to` | `ddMMyyyyHHmm` format |

### Example

```
https://data.definedgesecurities.com/sds/history/NSE/22/day/010620230000/010620231530
```

## Response Message Format

Fields in the response appear in the following format (CSV without headers):

**For `day` and `minute` timeframe:**

```
Dateandtime, Open Price, High Price, Low Price, Close, Volume, Open Interest
```

> Open Interest (OI) is present only for derivatives segments.

**For `tick` timeframe:**

```
UTC(in seconds), LTP(Last Traded Price), LTQ(Last Traded Quantity), Open Interest
```

> OI will be 0 for Equity segments.
