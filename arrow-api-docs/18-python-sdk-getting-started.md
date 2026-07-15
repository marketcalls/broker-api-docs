> Source: https://docs.arrow.trade/python-sdk/getting-started/

# Getting Started

Welcome to PyArrow, the official Python SDK for the Arrow Trading Platform. This SDK provides comprehensive access to trading APIs, real-time market data, and order management capabilities built for traders, quants, and fintech developers.

## Key Features

  * **Market Data & Analytics**

* * *

Real-time quotes, OHLC, LTP, market depth, historical candles, option chains, and more.

  * **Order Management**

* * *

Place, modify, and cancel orders across NSE, BSE, NFO, BFO exchanges with support for all order types.

  * **Real-time Streaming**

* * *

WebSocket-based live market data feeds with automatic reconnection and thread-safe event handling.

  * **Secure Authentication**

* * *

OAuth-based authentication with TOTP integration and automatic session management.

## Installation

Install the PyArrow client using pip:

```bash
pip install pyarrow-client
```

The package is published on PyPI as `pyarrow-client` (hyphen). In Python, import it as `pyarrow_client` (underscore)—not `pyarrow`, which is the [Apache Arrow](https://pypi.org/project/pyarrow/) library and is unrelated to this SDK.

### Requirements

Package | Version
---|---
Python | 3.8+
requests | Latest
websocket-client | Latest
pyotp | Latest
python-dateutil | Latest
zstandard | Latest
urllib3 | Latest

## Quick Start

### 1\. Initialize the Client

```python
from pyarrow_client import ArrowClient

# Initialize with your application ID
client = ArrowClient(app_id="your_app_id")
```

### 2\. Authenticate

Web-based LoginAutomated Login

```python
# Get the login URL
login_url = client.login_url()
print(f"Visit: {login_url}")

# After user authorizes, extract request_token from callback URL
client.login(
    request_token="token_from_callback",
    api_secret="your_app_secret"  # also accepts app_secret=
)
```

```python
# Fully automated login with credentials
client.auto_login(
    user_id="your_user_id",
    password="your_password",
    api_secret="your_app_secret",  # also accepts app_secret=
    totp_secret="your_totp_secret"
)
```

### 3\. Place Your First Order

```python
from pyarrow_client import Exchange, OrderType, ProductType, TransactionType, Variety, Retention

# Place a buy order
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

print(f"Order placed successfully: {order_id}")
```

### 4\. Get Market Data

```python
from pyarrow_client import QuoteMode, Exchange

# Get real-time quote
quote = client.get_quote(QuoteMode.LTP, "RELIANCE-EQ", Exchange.NSE)
print(f"Last Traded Price: ₹{quote['ltp']}")

# Get detailed OHLCV data
ohlcv = client.get_quote(QuoteMode.OHLCV, "RELIANCE-EQ", Exchange.NSE)
print(f"Open: {ohlcv['open']} | High: {ohlcv['high']} | Low: {ohlcv['low']} | Close: {ohlcv['close']}")
```

### 5\. Stream Live Data

```python
from pyarrow_client import ArrowStreams, DataMode

# Initialize WebSocket streams
streams = ArrowStreams(
    appID="your_app_id",
    token="your_access_token",
    debug=True
)

# Handle incoming market data
def on_tick(tick):
    print(f"Token: {tick.token} | LTP: ₹{tick.ltp} | Change: {tick.net_change}%")

streams.data_stream.on_ticks = on_tick

# Connect and subscribe
streams.connect_all()
streams.subscribe_market_data(DataMode.QUOTE, [3045, 1594])  # RELIANCE, INFY tokens

# Keep the connection alive
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    streams.disconnect_all()
```

## What's Next?

Now that you have the basics, explore the detailed documentation:

Topic | Description
---|---
[Authentication](../authentication/) | Detailed authentication flows and session management
[Orders](../orders/) | Complete order placement, modification, and cancellation
[Portfolio](../portfolio/) | Positions, holdings, order book, and trade book
[Market Data](../market-data/) | Quotes, instruments, and historical data
[WebSocket Streaming](../websocket-streaming/) | Real-time market data and order updates
[API Reference](../api-reference/) | Complete method reference and constants

## Support

Resource | Link
---|---
Documentation | <https://docs.arrow.trade>
Support Email | [support@arrow.trade](mailto:support@arrow.trade)
GitHub Issues | Report bugs or request features

Pro Tip

Start with the [Authentication](../authentication/) guide to understand the complete login flow before integrating with your trading application.
