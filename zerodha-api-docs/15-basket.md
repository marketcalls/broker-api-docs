# Offsite Order Execution (Basket)

Redirect users to Kite's exchange-approved order interface for placing trades, similar to a payment gateway.

## Flow

1. Prepare JSON list with order parameters
2. POST data as form field `data` with `api_key` to `https://kite.zerodha.com/connect/basket`
3. User sees order basket on Kite

**Login not required.** Unauthenticated users get login prompt; authenticated users proceed directly.

## Request Parameters

| Parameter | Description |
|-----------|-------------|
| variety | regular, amo, co (default: regular) |
| tradingsymbol | Instrument symbol |
| exchange | Exchange name |
| transaction_type | BUY or SELL |
| order_type | MARKET, LIMIT, etc. |
| quantity | Transaction quantity |
| product | CNC, MIS, NRML |
| price | For LIMIT orders |
| trigger_price | For SL/SL-M |
| disclosed_quantity | Public quantity |
| validity | Order validity |
| readonly | Boolean; prevents user editing |
| tag | Alphanumeric (max 20 chars) |

## Response

After order placement, redirects to your `redirect_login` with `status` and `request_token`.
