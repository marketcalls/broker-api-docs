> Source: https://docs.arrow.trade/python-sdk/market-data/

# Market Data

The PyArrow SDK provides comprehensive market data access including real-time quotes, historical candles, instruments, and option chain information.

## Quote Modes

Mode | Code | Description | Data Included
---|---|---|---
LTP | `QuoteMode.LTP` | Last Traded Price | `ltp`, `close`, `token`
OHLCV | `QuoteMode.OHLCV` | OHLC & Volume | `open`, `high`, `low`, `close`, `ltp`, `volume`, `ltt`, `oi`, `token`
FULL | `QuoteMode.FULL` | Complete market depth | OHLCV-style fields plus `bids`, `asks`, `symbol`, etc.

Price scaling

REST quote endpoints return prices as **integers in paise** (×100). Divide by `100` for rupees. See [Instrument Quotes](../../rest-api/symbol-quotes/).

## Single Instrument Quote

Get real-time market data for a single instrument.

### LTP Quote

```python
from pyarrow_client import ArrowClient, QuoteMode, Exchange

client = ArrowClient(app_id="your_app_id")
# ... authenticate ...

# Get last traded price (values in paise)
quote = client.get_quote(QuoteMode.LTP, "RELIANCE-EQ", Exchange.NSE)
print(f"LTP: ₹{quote['ltp'] / 100:.2f}")
print(f"Close: ₹{quote['close'] / 100:.2f}")
print(f"Token: {quote['token']}")
```

### OHLCV Quote

```python
# Get OHLC and volume data
quote = client.get_quote(QuoteMode.OHLCV, "RELIANCE-EQ", Exchange.NSE)

print(f"Open:   ₹{quote['open'] / 100:.2f}")
print(f"High:   ₹{quote['high'] / 100:.2f}")
print(f"Low:    ₹{quote['low'] / 100:.2f}")
print(f"Close:  ₹{quote['close'] / 100:.2f}")
print(f"Volume: {quote['volume']}")
```

### Full Quote (Market Depth)

```python
# Get complete market depth
quote = client.get_quote(QuoteMode.FULL, "RELIANCE-EQ", Exchange.NSE)

print(f"LTP: ₹{quote['ltp'] / 100:.2f}")
print(f"Volume: {quote['volume']}")
print(f"Open Interest: {quote.get('oi', 'N/A')}")

# Bid-Ask spread (prices in paise)
print(f"\nBest Bid: ₹{quote['bids'][0]['price'] / 100:.2f} x {quote['bids'][0]['quantity']}")
print(f"Best Ask: ₹{quote['asks'][0]['price'] / 100:.2f} x {quote['asks'][0]['quantity']}")

# Full depth (5 levels)
print("\n--- BID DEPTH ---")
for i, bid in enumerate(quote['bids'][:5]):
    print(f"Level {i+1}: ₹{bid['price'] / 100:>10.2f} x {bid['quantity']:>8}")

print("\n--- ASK DEPTH ---")
for i, ask in enumerate(quote['asks'][:5]):
    print(f"Level {i+1}: ₹{ask['price'] / 100:>10.2f} x {ask['quantity']:>8}")
```

## Multiple Instrument Quotes

Get quotes for multiple instruments in a single API call.

### LTP for Multiple Symbols

```python
# Get LTP for multiple symbols
quotes = client.get_quotes(
    QuoteMode.LTP,
    symbols=[
        ("RELIANCE-EQ", Exchange.NSE),
        ("INFY-EQ", Exchange.NSE),
        ("TCS-EQ", Exchange.NSE),
        ("IDEA-EQ", Exchange.BSE)
    ]
)

# Batch responses are keyed by token — map tokens back to your request list
requested = [
    ("RELIANCE-EQ", Exchange.NSE, 2885),
    ("NIFTY", Exchange.INDEX, 26000),
]
quotes = client.get_quotes(
    QuoteMode.LTP,
    symbols=[(s, e) for s, e, _ in requested],
)

for quote in quotes:
    ltp_rupees = quote["ltp"] / 100
    print(f"Token {quote['token']}: LTP ₹{ltp_rupees:.2f}")
```

Batch quote shape

`get_quotes()` returns rows with **`token`** , **`ltp`** , and **`close`** only for LTP mode. There is no `symbol` or `exchange` field in batch responses — match rows using `token`.

### OHLCV for Multiple Symbols

```python
quotes = client.get_quotes(
    QuoteMode.OHLCV,
    symbols=[("RELIANCE-EQ", Exchange.NSE)],
)

for quote in quotes:
    print(f"Token {quote['token']}")
    print(f"  O: {quote['open']} H: {quote['high']} L: {quote['low']} C: {quote['close']}")
    print(f"  Volume: {quote['volume']}")
```

### Full Quote for Multiple Symbols

```python
quotes = client.get_quotes(
    QuoteMode.FULL,
    symbols=[("RELIANCE-EQ", Exchange.NSE)],
)

for quote in quotes:
    print(f"{quote.get('symbol', quote['token'])} - LTP: ₹{quote['ltp'] / 100:.2f}")
    print(f"  Bid: ₹{quote['bids'][0]['price'] / 100:.2f} | Ask: ₹{quote['asks'][0]['price'] / 100:.2f}")
```

## Historical Candle Data

Retrieve historical OHLCV candle data for technical analysis.

### Available Intervals

Interval | Code | Description
---|---|---
1 Minute | `min` | 1-minute candles
3 Minutes | `3min` | 3-minute candles
5 Minutes | `5min` | 5-minute candles
15 Minutes | `15min` | 15-minute candles
30 Minutes | `30min` | 30-minute candles
1 Hour | `hour` | Hourly candles
1 Day | `day` | Daily candles
10 Minutes | `10min` | 10-minute candles
2 Hours | `2hours` | 2-hour candles
3 Hours | `3hours` | 3-hour candles
4 Hours | `4hours` | 4-hour candles
1 Week | `week` | Weekly candles
1 Month | `month` | Monthly candles

See [Historical Data API](../../rest-api/historical-candle-data/) for full details. The SDK passes `exchange` as uppercase in the URL path (e.g. `NSE`); REST curl examples may show lowercase (`nse`). Use ISO datetimes for `from_timestamp` / `to_timestamp` (`YYYY-MM-DDTHH:MM:SS`). Interval codes are strings such as `min`, `5min`, and `day` — not numeric shorthand like `1`.

### Basic Usage

```python
from pyarrow_client import Exchange

# Get 5-minute candle data
candles = client.candle_data(
    exchange=Exchange.NSE,
    token="3045",  # RELIANCE token
    interval="5min",
    from_timestamp="2024-01-15T09:15:00",
    to_timestamp="2024-01-15T15:30:00",
    oi=False  # Include Open Interest (for F&O)
)

print(f"Candles: {candles}")
```

### Intraday Candles

```python
from datetime import datetime, timedelta

# Get today's 5-minute candles
today = datetime.now()
market_open = today.replace(hour=9, minute=15, second=0)
market_close = today.replace(hour=15, minute=30, second=0)

candles = client.candle_data(
    exchange=Exchange.NSE,
    token="3045",
    interval="5min",
    from_timestamp=market_open.strftime("%Y-%m-%dT%H:%M:%S"),
    to_timestamp=market_close.strftime("%Y-%m-%dT%H:%M:%S"),
    oi=False
)

# Each candle: [timestamp, open, high, low, close, volume] or with OI as 7th element
# Prices are in paise (×100)
for candle in candles:
    ts, o, h, l, c, vol = candle[:6]
    print(f"{ts} O:{o} H:{h} L:{l} C:{c} V:{vol}")
```

### Daily Candles

```python
# Get daily candles for the past month
from datetime import datetime, timedelta

end_date = datetime.now()
start_date = end_date - timedelta(days=30)

candles = client.candle_data(
    exchange=Exchange.NSE,
    token="3045",
    interval="day",
    from_timestamp=start_date.strftime("%Y-%m-%dT09:15:00"),
    to_timestamp=end_date.strftime("%Y-%m-%dT15:30:00"),
    oi=False
)

print(f"Retrieved {len(candles)} daily candles")
```

### F&O Candles with Open Interest

```python
# Get F&O candles with OI data
candles = client.candle_data(
    exchange=Exchange.NFO,
    token="46799",  # NIFTY option token
    interval="15min",
    from_timestamp="2024-01-15T09:15:00",
    to_timestamp="2024-01-15T15:30:00",
    oi=True  # Include Open Interest
)

for candle in candles:
    ts = candle[0]
    oi = candle[6] if len(candle) > 6 else None
    print(f"Time: {ts} | OI: {oi}")
```

## Instruments

Download the full instrument master as **CSV** (or raw bytes) from `/all`:

```python
import csv
import io

raw = client.get_instruments()

# If the API returns CSV bytes/text, parse locally:
if isinstance(raw, (bytes, str)):
    text = raw.decode() if isinstance(raw, bytes) else raw
    reader = csv.DictReader(io.StringIO(text))
    for row in reader:
        if row.get("TradingSymbol") == "RELIANCE-EQ":
            print(f"Token: {row['Token']}, Lot: {row['LotSize']}")
            break
```

See [Symbols API](../../rest-api/symbols/) for CSV column definitions. Refresh after **8:00 AM IST** daily.

## Option Chain

Get option chain symbols and data.

### Get Option Chain Symbols

Returns `{ "equity": {...}, "indices": {...} }` maps of underlyings to expiry lists.

```python
chains = client.get_option_chain_symbols()
# Keys look like "INDEX:NIFTY", "INDEX:BANKNIFTY", "NSE:RELIANCE-EQ"
print(list(chains["indices"].keys())[:3])
```

### Get Option Chain

Pass the **underlying** symbol and `Exchange.INDEX` for indices (e.g. `"NIFTY"`, `"BANKNIFTY"`). Pick an expiry from `get_option_chain_symbols()`.

```python
chain = client.get_option_chain(
    "NIFTY",
    Exchange.INDEX,
    count=10,
    expiry="16-JUN-2026",
)

# Each leg includes fields such as:
# symbol, token, strikePrice, optionType, segment, lotSize, tickSize, openingOI
for leg in chain[:2]:
    print(leg["symbol"], leg["strikePrice"], leg["optionType"], leg["token"])
```

### Option chain leg fields (live)

Field | Description
---|---
`symbol` | Contract symbol (e.g. `NIFTY16JUN26C23150`)
`token` | Option instrument token
`strikePrice` | Strike price string
`optionType` | `CE` or `PE`
`segment` | e.g. `NSEFO`
`lotSize` | Lot size
`tickSize` | Tick size
`pricePrecision` | Price precision
`openingOI` | Opening open interest

### Get Expiry Dates

```python
# Get expiry dates for NIFTY options (static method)
expiries = ArrowClient.get_expiry_dates("NIFTY", 2024)
print(f"NIFTY Expiries: {expiries}")
```

## Index List

Get available index listings (used for quotes and streaming tokens, not for option-chain requests).

```python
# Get all indices
indices = client.get_index_list()

for index in indices:
    # API may return display name as `name` or `indexName`
    display = index.get("name") or index.get("indexName")
    print(f"{display}: token {index['token']}")
```

## Market Holidays

Get market holiday calendar.

```python
# Get market holidays
holidays = client.get_holidays()

holidays_map = holidays.get("holidays", holidays)
for date, name in holidays_map.items():
    print(f"  {date}: {name}")
```

## Example: Market Scanner

```python
from pyarrow_client import ArrowClient, QuoteMode, Exchange

def market_scanner(client, symbol_token_pairs):
    """Scan multiple stocks — pass (symbol, token) because batch quotes return token only."""

    symbol_list = [(sym, Exchange.NSE) for sym, _ in symbol_token_pairs]
    token_to_symbol = {tok: sym for sym, tok in symbol_token_pairs}

    quotes = client.get_quotes(QuoteMode.OHLCV, symbols=symbol_list)

    gainers = []
    losers = []
    high_volume = []

    for quote in quotes:
        symbol = token_to_symbol.get(quote["token"], str(quote["token"]))
        close = float(quote.get("close", 0))
        ltp = float(quote.get("ltp", 0))
        change_pct = ((ltp - close) / close * 100) if close else 0.0
        volume = int(quote.get("volume", 0))

        if change_pct > 2:
            gainers.append((symbol, change_pct))
        elif change_pct < -2:
            losers.append((symbol, change_pct))

        if volume > 1_000_000:
            high_volume.append((symbol, volume))

    # Display results
    print("\n📈 TOP GAINERS (>2%)")
    for sym, chg in sorted(gainers, key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {sym}: +{chg:.2f}%")

    print("\n📉 TOP LOSERS (<-2%)")
    for sym, chg in sorted(losers, key=lambda x: x[1])[:5]:
        print(f"  {sym}: {chg:.2f}%")

    print("\n📊 HIGH VOLUME")
    for sym, vol in sorted(high_volume, key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {sym}: {vol:,}")

# Usage — include instrument tokens from the symbols master
watchlist = [
    ("RELIANCE-EQ", 2885),
    ("TCS-EQ", 11536),
    ("INFY-EQ", 1594),
]
market_scanner(client, watchlist)
```

## Example: Technical Analysis Setup

```python
from pyarrow_client import ArrowClient, Exchange
from datetime import datetime, timedelta

def get_technical_data(client, symbol, token, days=30):
    """Fetch data for technical analysis."""

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    # Get daily candles
    candles = client.candle_data(
        exchange=Exchange.NSE,
        token=token,
        interval="day",
        from_timestamp=start_date.strftime("%Y-%m-%dT09:15:00"),
        to_timestamp=end_date.strftime("%Y-%m-%dT15:30:00"),
        oi=False
    )

    if not candles:
        print(f"No data for {symbol}")
        return None

    # candles: list of [timestamp, open, high, low, close, volume, ...]
    closes = [float(c[4]) for c in candles]

    def sma(prices, period):
        if len(prices) < period:
            return None
        return sum(prices[-period:]) / period

    sma_5 = sma(closes, 5)
    sma_20 = sma(closes, 20)

    latest = candles[-1]

    print(f"\n📊 {symbol} Technical Summary")
    print("=" * 40)
    print(f"Latest Close: {latest[4]}")
    print(f"5-Day SMA:    ₹{sma_5:.2f}" if sma_5 else "5-Day SMA: N/A")
    print(f"20-Day SMA:   ₹{sma_20:.2f}" if sma_20 else "20-Day SMA: N/A")

    # Simple trend detection
    if sma_5 and sma_20:
        if sma_5 > sma_20:
            print("Trend: 📈 BULLISH (5 SMA > 20 SMA)")
        else:
            print("Trend: 📉 BEARISH (5 SMA < 20 SMA)")

    # 52-week high/low from available data
    highs = [float(c[2]) for c in candles]
    lows = [float(c[3]) for c in candles]

    print(f"\n{days}-Day High: ₹{max(highs):.2f}")
    print(f"{days}-Day Low:  ₹{min(lows):.2f}")

    return {
        'symbol': symbol,
        'close': float(latest[4]),
        'sma_5': sma_5,
        'sma_20': sma_20,
        'period_high': max(highs),
        'period_low': min(lows)
    }

# Usage
tech_data = get_technical_data(client, "RELIANCE-EQ", "3045", days=30)
```

## Quote Response Fields

### LTP Mode Fields

Field | Type | Description
---|---|---
`symbol` | string | Trading symbol
`ltp` | number | Last traded price
`close` | number | Previous close
`netChange` | number | Net change

### OHLCV Mode Fields

Field | Type | Description
---|---|---
`open` | number | Opening price
`high` | number | Day's high
`low` | number | Day's low
`close` | number | Previous close
`ltp` | number | Last traded price
`volume` | number | Traded volume

### Full Mode Additional Fields

Field | Type | Description
---|---|---
`oi` | number | Open Interest
`oi_day_high` | number | OI day high
`oi_day_low` | number | OI day low
`upper_limit` | number | Upper circuit limit
`lower_limit` | number | Lower circuit limit
`bids` | array | 5 bid levels
`asks` | array | 5 ask levels
`total_buy_quantity` | number | Total buy quantity
`total_sell_quantity` | number | Total sell quantity
