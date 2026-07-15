# Get Order Book API

## Overview

Retrieves all orders placed for the current trading day. Orders are automatically cleared at the end of the trading session.

## Endpoint

**GET** `https://api.upstox.com/v2/order/retrieve-all`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Response (200)

Returns an array of order objects, each containing: exchange, product, price, quantity, status, order_type, transaction_type, filled_quantity, pending_quantity, order_id, exchange_order_id.
