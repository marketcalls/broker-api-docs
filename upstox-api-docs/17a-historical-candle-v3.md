# Historical Candle Data V3 API

## Overview

Fetch historical OHLC data with expanded interval options and custom timeframes.

## Endpoint

**GET** `https://api.upstox.com/v3/historical-candle/{instrument_key}/{unit}/{interval}/{to_date}/{from_date}`

## Time Units & Intervals

| Unit | Interval Options | Historical Availability | Max Records |
|------|------------------|------------------------|------------|
| minutes | 1-300 | January 2022 | 1 month (1-15 min); 1 quarter (>15 min) |
| hours | 1-5 | January 2022 | 1 quarter |
| days | 1 | January 2000 | 1 decade |
| weeks | 1 | January 2000 | Unlimited |
| months | 1 | January 2000 | Unlimited |

## Path Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | String | Financial instrument identifier |
| unit | Yes | String | `minutes`, `hours`, `days`, `weeks`, or `months` |
| interval | Yes | String | Numeric (1-300 for minutes, 1-5 for hours, 1 for others) |
| to_date | Yes | String | End date (YYYY-MM-DD, inclusive) |
| from_date | No | String | Start date (YYYY-MM-DD) |

## Response

```json
{
  "status": "success",
  "data": {
    "candles": [
      [
        "2025-01-01T00:00:00+05:30",
        53.1,    // open
        53.95,   // high
        51.6,    // low
        52.05,   // close
        235519861, // volume
        0        // open interest
      ]
    ]
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1021 | Invalid instrument key format |
| UDAPI1022 | to_date is required |
| UDAPI100011 | Invalid instrument key |
| UDAPI1015 | to_date must be >= from_date |
| UDAPI1146 | Invalid unit |
| UDAPI1147 | Invalid interval for unit |
| UDAPI1148 | Invalid date range |

## Python Example

```python
import requests
url = 'https://api.upstox.com/v3/historical-candle/NSE_EQ%7CINE848E01016/minutes/1/2025-01-02/2025-01-01'
headers = {
    'Authorization': 'Bearer {your_access_token}'
}
response = requests.get(url, headers=headers)
print(response.json())
```
