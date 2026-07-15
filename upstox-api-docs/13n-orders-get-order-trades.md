# Get Order Trades API

## Overview

Retrieves all trades executed for a specific order.

## Endpoint

**GET** `https://api.upstox.com/v2/order/trades?order_id={order_id}`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| order_id | Yes | string | The order identifier |

## Response (200)

Same structure as Get Trades API but filtered to a specific order.

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1023 | Order ID is required |
| UDAPI1010 | Order ID accepts only alphanumeric characters and '-' |
