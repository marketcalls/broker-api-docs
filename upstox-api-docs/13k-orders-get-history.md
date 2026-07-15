# Get Order History API

## Overview

Retrieves the detailed progression of a specific order through its various execution stages.

## Endpoint

**GET** `https://api.upstox.com/v2/order/history`

## Query Parameters

| Parameter | Required | Type | Purpose |
|-----------|----------|------|---------|
| order_id | No | string | Order reference ID |
| tag | No | string | Unique tag identifier |

**Note:** At least one of `order_id` or `tag` is required.

## Response (200)

Returns an array of order objects showing progression details with fields: exchange, price, product, quantity, status, order_id, exchange_order_id, filled_quantity, transaction_type, order_timestamp, average_price.

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1010 | Order ID accepts only alphanumeric and hyphens |
| UDAPI100059 | Missing required order_id or tag |
| UDAPI100010 | Order not found |
