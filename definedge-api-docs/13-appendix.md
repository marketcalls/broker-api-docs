# Appendix — Reference Constants

This appendix collects the enumerated constants used across the INTEGRATE API request/response payloads.

## Exchanges

| Value | Description |
| --- | --- |
| `NSE` | NSE Cash (Equity) |
| `BSE` | BSE Cash (Equity) |
| `NFO` | NSE Futures & Options |
| `BFO` | BSE Futures & Options |
| `CDS` | Currency Derivatives |
| `MCX` | MCX Commodities |

> Master file segment codes: `NSE / BSE / NFO / CDS / MCX`.
> Historical data segment codes: `NSE / BSE / NFO / BFO / CDS / MCX`.

## Order Type (`order_type`)

| Value | Description |
| --- | --- |
| `BUY` | Buy order |
| `SELL` | Sell order |

## Price Type (`price_type`)

| Value | Description |
| --- | --- |
| `LIMIT` | Limit order |
| `MARKET` | Market order (price should be 0) |
| `SL-LIMIT` | Stop-loss limit order (requires `trigger_price`) |
| `SL-MARKET` | Stop-loss market order (requires `trigger_price`) |

## Product Type (`product_type`)

| Value | Description |
| --- | --- |
| `CNC` | Cash & Carry (Equity only) |
| `INTRADAY` | Intraday (both equity and derivatives) |
| `NORMAL` | Normal / carry-forward (Derivatives only) |

## Validity (`validity`)

| Value | Description |
| --- | --- |
| `DAY` | Valid for the day (default) |
| `EOS` | End of session |
| `IOC` | Immediate Or Cancel |

## Order Status (`order_status`)

| Value |
| --- |
| `NEW` |
| `OPEN` |
| `COMPLETE` |
| `CANCELED` |
| `REJECTED` |
| `REPLACED` |

## Order Variety (`variety`)

| Value | Description |
| --- | --- |
| `REGULAR` | Regular order |
| `AMO` | After Market Order |
| `SQUAREOFF` | Square-off order |

## GTT / OCO Conditions (`condition`)

| Value | Description |
| --- | --- |
| `LTP_ABOVE` | Trigger when LTP goes above the alert price (GTT) |
| `LTP_BELOW` | Trigger when LTP goes below the alert price (GTT) |
| `LMT_OCO` | One Cancels Other (OCO) limit order |

## Option Type (`option_type`)

| Value | Description |
| --- | --- |
| `CE` | Call option |
| `PE` | Put option |

## WebSocket Task Codes (`t`)

### Requests

| Value | Description |
| --- | --- |
| `c` | Connect |
| `h` | Heartbeat |
| `t` | Subscribe touchline |
| `u` | Unsubscribe touchline |
| `d` | Subscribe depth |
| `ud` | Unsubscribe depth |
| `o` | Subscribe order update |
| `uo` | Unsubscribe order update |

### Responses / Feeds

| Value | Description |
| --- | --- |
| `ck` | Connect acknowledgement |
| `tk` | Touchline subscription acknowledgement |
| `tf` | Touchline feed |
| `uk` | Unsubscribe touchline acknowledgement |
| `dk` | Depth subscription acknowledgement |
| `df` | Depth feed |
| `udk` | Unsubscribe depth acknowledgement |
| `ok` | Order update subscription acknowledgement |
| `om` | Order update feed message |
| `uok` | Unsubscribe order update acknowledgement |

## Common URL / Header Placeholders

| Placeholder | Meaning |
| --- | --- |
| `{{api_token}}` | API token from MyAccount → Account → API Config |
| `api_secret` | API secret from MyAccount → Account → API Config |
| `api_session_key` | Session key returned by Login Step 2; passed in the `Authorization` header |
| `susertoken` | Websocket session token returned by Login Step 2 |
| `{exchange}` | Exchange code (see [Exchanges](#exchanges)) |
| `{token}` | Scrip token from the [Master File](03-master-file.md) |
| `{orderid}` | Order ID |
| `{alert_id}` | GTT/OCO alert ID |
