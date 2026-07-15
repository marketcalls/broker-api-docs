# Get Order Details API

## Overview

Retrieves the current status of a specific order. Orders remain available for one trading day and are automatically removed at the end of the session.

## Endpoint

**GET** `https://api.upstox.com/v2/order/details`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| order_id | No | string | The order reference ID |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| exchange | string | NSE, BSE, etc. |
| product | string | D (Delivery), I (Intraday), CO, MTF |
| price | float | Placement price |
| quantity | int32 | Order quantity |
| status | string | Current order status |
| trading_symbol | string | Instrument symbol |
| average_price | float | Average execution price |
| filled_quantity | int32 | Executed quantity |
| pending_quantity | int32 | Remaining quantity |
| transaction_type | string | BUY or SELL |
| order_type | string | MARKET, LIMIT, SL, SL-M |
| validity | string | DAY or IOC |
| trigger_price | float | Stop loss trigger price |
| disclosed_quantity | int32 | Quantity shown in market depth |
| order_id | string | Internal unique order ID |
| exchange_order_id | string | Exchange-assigned order ID |
| variety | string | Order complexity level |
| order_timestamp | string | Placement time |
| exchange_timestamp | string | Exchange update time |
| is_amo | boolean | After Market Order status |
| order_ref_id | string | Internal reference identifier |
| status_message | string | Rejection/cancellation reason |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1010 | Order ID accepts only alphanumeric characters and '-' |
| UDAPI100059 | At least one of 'order_id' or 'tag' is required |
| UDAPI100010 | Order not found |

## Python Example

```python
import requests
url = 'https://api.upstox.com/v2/order/details'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer {your_access_token}'
}
params = {'order_id': '240108010445130'}
response = requests.get(url, headers=headers, params=params)
print(response.json())
```
