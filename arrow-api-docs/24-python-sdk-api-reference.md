> Source: https://docs.arrow.trade/python-sdk/api-reference/

# API Reference

Complete reference documentation for all PyArrow SDK classes, methods, and constants.

## ArrowClient

The main client class for interacting with Arrow Trading APIs.

### Initialization

```python
from pyarrow_client import ArrowClient

client = ArrowClient(
    app_id="your_app_id",
    timeout=10,       # optional, default 10 seconds
    debug=False,      # optional request/response logging
    root_url=None,    # optional, default https://edge.arrow.trade
)
```

Parameter | Type | Required | Description
---|---|---|---
`app_id` | string | ✓ | Your application identifier
`timeout` | int | - | HTTP timeout in seconds (default: 10)
`debug` | bool | - | Log requests and responses
`root_url` | string | - | Override trading API base URL
`pool_config` | dict | - | HTTP adapter pool/retry settings

* * *

## Authentication Methods

### login()

Exchange request token for access token.

```python
response = client.login(request_token="token", api_secret="secret")
# also accepts app_secret=
```

Parameter | Type | Required | Description
---|---|---|---
`request_token` | string | ✓ | Token from OAuth callback
`api_secret` | string | ✓ | Your application secret (alias: `app_secret`)

**Returns:** `Dict[str, str]` \- User data with access token

* * *

### auto_login()

Automated login with credentials and TOTP.

```python
response = client.auto_login(
    user_id="user_id",
    password="password",
    api_secret="app_secret",  # alias: app_secret=
    totp_secret="totp_secret"
)
```

Parameter | Type | Required | Description
---|---|---|---
`user_id` | string | ✓ | User ID
`password` | string | ✓ | Account password
`api_secret` | string | ✓ | Application secret (alias: `app_secret`)
`totp_secret` | string | ✓ | Base32 TOTP secret

**Returns:** `Dict[str, str]` \- User data with access token

* * *

### login_url()

Get the OAuth login URL.

```python
url = client.login_url()
```

**Returns:** `str` \- Login URL

* * *

### set_token()

Manually set the access token.

```python
client.set_token("your_access_token")
```

Parameter | Type | Required | Description
---|---|---|---
`token` | string | ✓ | Access token

**Returns:** `None`

* * *

### get_token()

Get the current access token.

```python
token = client.get_token()
```

**Returns:** `str` \- Current access token

* * *

### token (property)

Read-only alias for `get_token()`.

```python
access_token = client.token
```

**Returns:** `str` \- Current access token (empty string if not set)

* * *

### invalidate_session()

Clear the current session.

```python
client.invalidate_session()
```

**Returns:** `None`

* * *

## Order Methods

### place_order()

Place a new trading order.

```python
order_id = client.place_order(
    exchange=Exchange.NSE,
    symbol="RELIANCE-EQ",
    quantity=1,
    disclosed_quantity=0,
    product=ProductType.CNC,
    order_type=OrderType.LIMIT,
    variety=Variety.REGULAR,
    transaction_type=TransactionType.BUY,
    price=1450.0,
    validity=Retention.DAY
)
```

Parameter | Type | Required | Description
---|---|---|---
`exchange` | Exchange | ✓ | Exchange (NSE, BSE, NFO, BFO)
`symbol` | string | ✓ | Trading symbol
`quantity` | int | ✓ | Order quantity
`disclosed_quantity` | int | ✓ | Disclosed quantity (0 for none)
`product` | ProductType | ✓ | Product type (MIS, CNC, NRML)
`order_type` | OrderType | ✓ | Order type (MARKET, LIMIT, STOP_LOSS_LIMIT, STOP_LOSS_MARKET; aliases: MKT, SL_LMT, SL_MKT)
`variety` | Variety | ✓ | Order variety (REGULAR, COVER)
`transaction_type` | TransactionType | ✓ | Buy or Sell
`price` | float | ✓ | Order price (0 for market)
`validity` | Retention | ✓ | Order validity (DAY, IOC)
`trigger_price` | float | - | Trigger price for SL orders (sent as `triggerPrice`)
`remarks` | string | - | Custom order tag (max 16 characters)
`mpp` | bool | - | When `True`, mimics a market order (Upper Limit or DPR by instrument). Plain `MKT` is disabled by default on the API; see Orders guide

**Returns:** `str` \- Order number (`orderNo` from the API)

* * *

### modify_order()

Modify an existing open order.

```python
message = client.modify_order(
    order_id="24012400000321",
    exchange=Exchange.NSE,
    symbol="RELIANCE-EQ",
    quantity=2,
    price=1500.0,
    disclosed_qty=0,
    product=ProductType.CNC,
    transaction_type=TransactionType.BUY,
    order_type=OrderType.LIMIT,
    validity=Retention.DAY,
    remarks="Modified"
)
```

Parameter | Type | Required | Description
---|---|---|---
`order_id` | string | ✓ | Order ID to modify
`exchange` | Exchange | ✓ | Exchange
`symbol` | string | ✓ | Trading symbol
`quantity` | int | ✓ | New quantity
`price` | float | ✓ | New price
`disclosed_qty` | int | ✓ | Disclosed quantity
`product` | ProductType | ✓ | Product type
`transaction_type` | TransactionType | ✓ | Transaction type
`order_type` | OrderType | ✓ | Order type
`validity` | Retention | ✓ | Order validity
`remarks` | string | - | Custom order tag (max 16 characters)
`mpp` | bool | - | When `True`, mimics a market order (Upper Limit or DPR by instrument). See Orders guide
`trigger_price` | float | - | Trigger price for SL orders (sent as `triggerPrice`)

**Returns:** `str` \- Modification message

* * *

### cancel_order()

Cancel a pending order.

```python
message = client.cancel_order(order_id="24012400000321")
```

Parameter | Type | Required | Description
---|---|---|---
`order_id` | string | ✓ | Order ID to cancel

**Returns:** `str` \- Cancellation message

* * *

### cancel_all_orders()

Cancel all open/pending orders. SDK convenience wrapper: fetches `GET /user/orders`, filters standing orders, then issues parallel `DELETE /order/regular/{id}` calls. There is no single REST route for bulk cancel.

```python
results = client.cancel_all_orders()
# Returns: List[Tuple[order_id, status, result]]
```

**Returns:** `List[Tuple]` \- List of (order_id, status, result) tuples

* * *

### get_order_details()

Get detailed order history.

```python
details = client.get_order_details(order_id="24012400000321")
```

Parameter | Type | Required | Description
---|---|---|---
`order_id` | string | ✓ | Order ID

**Returns:** `List[Dict]` \- Order history with status changes

* * *

### get_order_book()

Get all orders for the day.

```python
orders = client.get_order_book()
```

**Returns:** `List[Dict]` \- All user orders

* * *

### get_trade_book()

Get all executed trades.

```python
trades = client.get_trade_book()
```

**Returns:** `List[Dict]` \- All user trades

* * *

## Portfolio Methods

### get_positions()

Get current positions.

```python
positions = client.get_positions()
```

**Returns:** `List[Dict]` \- Current positions

* * *

### get_holdings()

Get delivery holdings.

```python
holdings = client.get_holdings()
```

**Returns:** `List[Dict]` \- Holdings list (unwrapped API `data`)

* * *

## User Methods

### get_user_details()

Get user profile information.

```python
user = client.get_user_details()
```

**Returns:** `Dict` \- User profile data

* * *

### get_user_limits()

Get margin and trading limits.

```python
limits = client.get_user_limits()
```

**Returns:** `Dict` \- Object with `allocations` and `margin` keys

* * *

## Margin Methods

### order_margin()

Calculate margin for a single order.

```python
margin = client.order_margin(
    exchange=Exchange.NSE,
    symbol="RELIANCE-EQ",
    quantity=100,
    product=ProductType.CNC,
    order_type=OrderType.LIMIT,
    transaction_type=TransactionType.BUY,
    price=1500.0,
    include_positions=False
)
```

Parameter | Type | Required | Description
---|---|---|---
`exchange` | Exchange | ✓ | Exchange
`symbol` | string | ✓ | Trading symbol
`quantity` | int | ✓ | Order quantity
`product` | ProductType | ✓ | Product type
`order_type` | OrderType | ✓ | Order type
`transaction_type` | TransactionType | ✓ | Buy or Sell
`price` | float | ✓ | Order price
`include_positions` | bool | - | Include existing positions

Symbol vs token

The Python SDK sends `symbol` (trading symbol, e.g. `RELIANCE-EQ`). Some REST margin examples use `token` (numeric instrument token). Use the symbol form with `ArrowClient`.

**Returns:** `Dict` \- Margin requirement (e.g. `requiredMargin`, `charge`)

* * *

### basket_margin()

Calculate margin for multiple orders.

```python
orders = [
    {
        "exchange": "NSE",
        "symbol": "RELIANCE-EQ",
        "quantity": "100",
        "product": ProductType.CNC,
        "order": OrderType.LIMIT,
        "transactionType": TransactionType.BUY,
        "price": "1500.00"
    }
]
margin = client.basket_margin(orders, include_positions=False)
```

Request body shape

Some REST curl examples show a top-level JSON **array** of orders. The Python SDK (and Go client) wrap the payload as `{ "orders": [...], "includePositions": bool }`. Each order dict should use `symbol` (trading symbol), not the numeric instrument `token` field shown in some REST examples.

Parameter | Type | Required | Description
---|---|---|---
`orders` | List[Dict] | ✓ | List of order dictionaries
`include_positions` | bool | - | Include existing positions

**Returns:** `Dict` with keys such as:

Field | Description
---|---
`final_margin` | Final margin after netting
`initial_margin` | Initial margin requirement
`orders` | Per-leg breakdown: `margin`, `symid`, `charge`

* * *

## Market Data Methods

### get_quote()

Get quote for a single instrument.

```python
quote = client.get_quote(QuoteMode.LTP, "RELIANCE-EQ", Exchange.NSE)
```

Parameter | Type | Required | Description
---|---|---|---
`mode` | QuoteMode | ✓ | Quote mode (LTP, OHLCV, FULL)
`symbol` | string | ✓ | Trading symbol
`exchange` | Exchange | ✓ | Exchange

**Returns:** `Dict` \- Quote data

* * *

### get_quotes()

Get quotes for multiple instruments.

```python
quotes = client.get_quotes(
    QuoteMode.LTP,
    symbols=[("RELIANCE-EQ", Exchange.NSE), ("INFY-EQ", Exchange.NSE)]
)
```

Parameter | Type | Required | Description
---|---|---|---
`mode` | QuoteMode | ✓ | Quote mode
`symbols` | List[Tuple] | ✓ | List of (symbol, exchange) tuples

**Returns:** `List[Dict]` \- Quote data for all symbols

* * *

### candle_data()

Get historical candle data.

```python
candles = client.candle_data(
    exchange=Exchange.NSE,
    token="3045",
    interval="5min",
    from_timestamp="2024-01-15T09:15:00",
    to_timestamp="2024-01-15T15:30:00",
    oi=False
)
```

Parameter | Type | Required | Description
---|---|---|---
`exchange` | Exchange | ✓ | Exchange
`token` | string | ✓ | Instrument token
`interval` | string | ✓ | Candle interval
`from_timestamp` | string | ✓ | Start time (`YYYY-MM-DDTHH:MM:SS`, e.g. `2024-01-15T09:15:00`)
`to_timestamp` | string | ✓ | End time (same ISO format)
`oi` | bool | - | Include Open Interest (F&O only)

**Intervals:** `min`, `3min`, `5min`, `10min`, `15min`, `30min`, `hour`, `2hours`, `3hours`, `4hours`, `day`, `week`, `month` (use `min` for 1-minute, not `1`)

**Host:** `https://historical-api.arrow.trade`. The SDK uppercases `exchange` in the URL path (e.g. `NSE`).

**Returns:** `List` \- Candle rows as `[timestamp, open, high, low, close, volume, (oi)]` (prices in paise)

* * *

### get_instruments()

Download the full instrument master from `GET /all` (CSV bytes or text). Segment-specific downloads (`/nse`, `/bse`, `/mcx`) are available via REST but not exposed as separate SDK methods.

```python
instruments = client.get_instruments()
```

**Returns:** `Any` \- Instrument master (typically CSV)

* * *

### get_holidays()

Get market holidays.

```python
holidays = client.get_holidays()
```

**Returns:** `Dict` \- Holiday calendar

* * *

### get_index_list()

Get available indices.

```python
indices = client.get_index_list()
```

**Returns:** `List[Dict]` \- Index listings

* * *

### get_option_chain_symbols()

Get option chain symbols.

```python
symbols = client.get_option_chain_symbols()
```

**Returns:** `Any` \- Option chain symbols

* * *

### get_option_chain()

Fetch option chain for an underlying and expiry.

```python
chain = client.get_option_chain("NIFTY", Exchange.INDEX, 10, "16-JUN-2026")
```

Parameter | Type | Required | Description
---|---|---|---
`underlying` | string | ✓ | Underlying symbol (e.g. `NIFTY`, `BANKNIFTY`) or equity key from `get_option_chain_symbols()`
`exchange` | Exchange | ✓ | `Exchange.INDEX` for indices; `Exchange.NSE` for equity underlyings
`count` | int | ✓ | Strikes around ATM
`expiry` | string | ✓ | Expiry (`DD-MMM-YYYY`); must exist in `get_option_chain_symbols()`

**Returns:** `List[Dict]` — each leg includes `symbol`, `token`, `strikePrice`, `optionType`, `segment`, `lotSize`, `tickSize`, `pricePrecision`, `openingOI`.

* * *

### get_stock_option_symbols()

Returns a static local list of equity symbols with listed options (~500 symbols).

```python
symbols = client.get_stock_option_symbols()
```

* * *

### get_greeks()

Calculate option Greeks for multiple option instrument tokens.

```python
greeks = client.get_greeks(["66652", "66654"])
```

Parameter | Type | Required | Description
---|---|---|---
`tokens` | List[str] | ✓ | Option instrument tokens (from option chain or symbols master)

API availability

The Greeks endpoint may be disabled or return errors on some environments. Verify with your account before relying on it in production.

**Returns:** `Any` \- List of Greek objects (`iv`, `delta`, `gamma`, `theta`, `vega`)

* * *

### get_expiry_dates()

Get expiry dates for options (static method).

```python
expiries = ArrowClient.get_expiry_dates("NIFTY", 2024)
```

Parameter | Type | Required | Description
---|---|---|---
`symbol` | string | ✓ | Underlying symbol
`year` | int or str | ✓ | Year

**Returns:** `Any` \- Expiry dates

* * *

## ArrowStreams

WebSocket streaming class for real-time data.

### Initialization

```python
from pyarrow_client import ArrowStreams

streams = ArrowStreams(
    appID="your_app_id",
    token="your_access_token",
    debug=True
)
```

Parameter | Type | Required | Description
---|---|---|---
`appID` | string | ✓ | Application ID
`token` | string | ✓ | Access token
`debug` | bool | - | Enable debug logging

* * *

### Connection Methods

Method | Description
---|---
`connect_order_stream()` | Connect to order updates
`connect_data_stream()` | Connect to market data
`connect_hft_data_stream()` | Connect to HFT market data
`connect_all()` | Connect order, data, and HFT streams
`disconnect_all()` | Disconnect all streams
`get_status()` | Get connection status

* * *

### Subscription Methods

Method | Description
---|---
`subscribe_market_data(mode, tokens)` | Subscribe to market data (Data Stream)
`unsubscribe_market_data(mode, tokens)` | Unsubscribe from data
`subscribe_hft_data(mode, symbols, latency=1000)` | Subscribe to HFT stream
`unsubscribe_hft_data(mode, symbols)` | Unsubscribe from HFT stream

* * *

### Event Handlers

#### Data Stream Events

Event | Parameters | Description
---|---|---
`on_ticks` | `MarketTick` | Market data received
`on_connect` | None | Connection established
`on_disconnect` | None | Connection lost
`on_error` | `Exception` | Error occurred
`on_close` | `close_status_code`, `close_msg` | Connection closed
`on_reconnect` | `attempt`, `delay` | Reconnection attempt
`on_no_reconnect` | None | Max attempts reached

#### Order Stream Events

Event | Parameters | Description
---|---|---
`on_order_update` | `Dict` | Order status changed

* * *

## Constants

### Exchange

```python
from pyarrow_client import Exchange

Exchange.NSE   # National Stock Exchange
Exchange.BSE   # Bombay Stock Exchange
Exchange.NFO   # NSE F&O
Exchange.BFO   # BSE F&O
Exchange.MCX   # Multi Commodity Exchange
Exchange.INDEX # Index segment
```

* * *

### OrderType

```python
from pyarrow_client import OrderType

OrderType.MARKET          # Market order (alias: OrderType.MKT)
OrderType.LIMIT           # Limit order
OrderType.STOP_LOSS_LIMIT # Stop loss limit (alias: OrderType.SL_LMT)
OrderType.STOP_LOSS_MARKET# Stop loss market (alias: OrderType.SL_MKT)
```

* * *

### ProductType

```python
from pyarrow_client import ProductType

ProductType.MIS   # Intraday
ProductType.CNC   # Cash and Carry (Delivery)
ProductType.NRML  # Normal (F&O)
```

* * *

### TransactionType

```python
from pyarrow_client import TransactionType

TransactionType.BUY   # Buy (B)
TransactionType.SELL  # Sell (S)
```

* * *

### Variety

```python
from pyarrow_client import Variety

Variety.REGULAR  # Regular order
Variety.COVER    # Cover order
```

* * *

### Retention

```python
from pyarrow_client import Retention

Retention.DAY  # Day order
Retention.IOC  # Immediate or Cancel
```

* * *

### QuoteMode

```python
from pyarrow_client import QuoteMode

QuoteMode.LTP    # Last Traded Price
QuoteMode.OHLCV  # OHLC + Volume
QuoteMode.FULL   # Full market depth
```

* * *

### DataMode

```python
from pyarrow_client import DataMode

DataMode.LTP    # Last traded price only (13 bytes)
DataMode.LTPC   # LTP + Close (17 bytes)
DataMode.QUOTE  # Detailed quote (93 bytes)
DataMode.FULL   # Full depth (249 bytes)
```

* * *

## MarketTick Properties

Property | Type | Mode | Description
---|---|---|---
`token` | int | All | Instrument token
`ltp` | float | All | Last traded price
`mode` | str | All | Data mode
`close` | float | All | Previous close
`net_change` | float | All | % change
`change_flag` | int | All | 43(+), 45(-), 32(=)
`open` | float | Quote+ | Open price
`high` | float | Quote+ | High price
`low` | float | Quote+ | Low price
`volume` | int | Quote+ | Volume
`ltq` | int | Quote+ | Last traded qty
`avg_price` | float | Quote+ | Average price
`total_buy_quantity` | int | Quote+ | Total buy qty
`total_sell_quantity` | int | Quote+ | Total sell qty
`ltt` | int | Quote+ | Last trade time (Unix seconds)
`time` | int | Quote+ | Exchange timestamp (Unix seconds)
`oi` | int | Quote+ | Open interest
`oi_day_high` | int | Quote+ | OI day high
`oi_day_low` | int | Quote+ | OI day low
`upper_limit` | float | Full | Upper circuit
`lower_limit` | float | Full | Lower circuit
`bids` | List | Full | 5 bid levels
`asks` | List | Full | 5 ask levels

* * *

## Error Codes

Code | Description
---|---
`INVALID_TOKEN` | Invalid or expired access token
`INVALID_APP_ID` | Invalid application ID
`MARGIN_ERROR` | Insufficient margin
`INVALID_ORDER` | Invalid order parameters
`ORDER_NOT_FOUND` | Order ID not found
`RATE_LIMIT` | API rate limit exceeded
`EXCHANGE_ERROR` | Exchange connectivity issue

* * *

## Package Utilities

### enable_logging()

Enable library log output (silent by default):

```python
import logging
import pyarrow_client

pyarrow_client.enable_logging(logging.INFO)
```

* * *

## Import Reference

Commonly imported symbols from `pyarrow_client`:

```python
from pyarrow_client import (
    ArrowClient,
    ArrowStreams,
    ConnectionConfig,
    DataMode,
    Exchange,
    HFTDataStream,
    MarketTick,
    OrderType,
    ProductType,
    QuoteMode,
    Retention,
    TransactionType,
    Variety,
    enable_logging,
)
```
