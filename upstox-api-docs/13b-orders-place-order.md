# Place Order API (V2 - Deprecated)

## Overview

The Place Order API allows developers to submit orders to the exchange. Upon successful placement, the system returns a unique `order_id` for subsequent modifications or cancellations.

## Endpoint

**POST** `https://api-hft.upstox.com/v2/order/place`

**Status:** Sandbox Enabled | Deprecated

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`
- `X-Algo-Name` (optional, for registered apps with exchange-approved algo strategies)

## Request Body Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| quantity | Yes | integer | Number of units/lots to order |
| product | Yes | string | `D` (Delivery), `I` (Intraday), `MTF` |
| validity | Yes | string | `DAY` or `IOC` |
| price | Yes | number | Order price |
| tag | No | string | Custom identifier for order retrieval |
| instrument_token | Yes | string | Security identifier (format: `NSE_EQ\|INE669E01016`) |
| order_type | Yes | string | `MARKET`, `LIMIT`, `SL`, `SL-M` |
| transaction_type | Yes | string | `BUY` or `SELL` |
| disclosed_quantity | Yes | integer | Quantity visible in market depth |
| trigger_price | Yes | number | Price trigger for stop-loss orders |
| is_amo | Yes | boolean | After-market order flag (auto-inferred) |
| market_protection | No | integer | Protection percentage (-1 to 25) |

## Key Business Rules

- **AMO Flag Behavior:** The system automatically infers market session status, ignoring `is_amo` during active trading hours.
- **Market Protection:** Applicable only to MARKET and SL-M orders. Defaults to `-1` (automatic), accepts `0-25` percent.
- **API Availability:** The Place order API is accessible from 5:30 AM to 12:00 AM IST daily.

## Response Format

```json
{
  "status": "success",
  "data": {
    "order_id": "1644490272000"
  }
}
```

## Supported Order Types

1. **Market Orders** - Executes at current market price
2. **Limit Orders** - Executes at specified price or better
3. **Stop-Loss (SL)** - Triggers at specified price, then executes as limit
4. **Stop-Loss Market (SL-M)** - Triggers at specified price, then executes as market

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1026 | Missing instrument key |
| UDAPI1004 | Invalid order type |
| UDAPI1052 | Order quantity cannot be zero |
| UDAPI1161 | MCX orders disabled for API users |
| UDAPI1158 | Market orders blocked; use limit orders |
| UDAPI1159 | Market protection exceeds 25% |
| UDAPI100049 | Access restricted; use Uplink Business |
| UDAPI100074 | API only accessible 5:30 AM - 12:00 AM IST |
