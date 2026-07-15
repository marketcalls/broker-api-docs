# Portfolio Stream Feed (WebSocket)

## Overview

Real-time updates for orders, GTT orders, holdings, and positions via WebSocket.

## Connection

**Protocol:** `wss:` (WebSocket Secure)
**HTTP Status:** 302 (Redirect to WebSocket endpoint)

## Required Headers

| Header | Required | Value |
|--------|----------|-------|
| Authorization | Yes | `Bearer access_token` |
| Accept | Yes | `*/*` |

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| update_types | No | string | Comma-separated: `order`, `gtt_order`, `position`, `holding` |

**Example:** `wss://api.upstox.com/v2/feed/portfolio-stream-feed?update_types=order%2Cposition%2Cholding`

## Message Types

### Order Updates
Fields: order_id, status, filled_quantity, average_price, exchange_order_id

### GTT Order Updates
Contains strategy rules (ENTRY, TARGET, STOPLOSS) with status tracking

### Holding Updates
Inventory data: average_price, quantity, collateral, haircut

### Position Updates
Intraday/overnight positions with buy/sell values

## Cross-Platform Sync

Orders placed via mobile app, web application, or API all sync through the WebSocket connection.
