# Get Profit and Loss Report API

## Endpoint

**GET** `https://api.upstox.com/v2/trade/profit-loss/data`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| from_date | No | string | Start date (dd-mm-yyyy) |
| to_date | No | string | End date (dd-mm-yyyy) |
| segment | Yes | string | `EQ`, `FO`, `COM`, `CD` |
| financial_year | Yes | string | e.g., "2324" for 2023-2024 |
| page_number | Yes | integer | Starting from 1 |
| page_size | Yes | integer | Max 5000 |

## Response Trade Fields

| Field | Type | Description |
|-------|------|-------------|
| quantity | float | Stock quantity traded |
| isin | string | Security ISIN code |
| scrip_name | string | Security name |
| trade_type | string | FUT, OPT, or EQ |
| buy_date | string | Purchase date (dd-mm-yyyy) |
| buy_average | float | Average buy rate |
| sell_date | string | Sale date (dd-mm-yyyy) |
| sell_average | float | Average sell rate |
| buy_amount | float | Total purchase amount |
| sell_amount | float | Total sale amount |

## Python Example

```python
import requests
url = 'https://api.upstox.com/v2/trade/profit-loss/data'
headers = {'Authorization': 'Bearer {your_access_token}'}
params = {
    'from_date': '05-11-2023',
    'to_date': '19-12-2023',
    'segment': 'EQ',
    'financial_year': '2324',
    'page_number': '1',
    'page_size': '4'
}
response = requests.get(url, headers=headers, params=params)
print(response.json())
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1067 | Segment is required |
| UDAPI1070 | Financial year is required |
| UDAPI1071 | Page number is required |
| UDAPI1072 | Page size is required |
| UDAPI1106 | Page size must be >= 1 |
| UDAPI1107 | Page size must be <= 5000 |
