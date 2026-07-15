> Source: https://docs.arrow.trade/python-sdk/portfolio/

# Portfolio

Access and manage your portfolio including positions, holdings, order book, and trade book through the PyArrow SDK.

The SDK returns the API **`data`** payload directly (not wrapped in `{ "status", "data" }`). Field names below were verified against live `edge.arrow.trade` responses.

## Positions

`get_positions()` returns a **list** of position objects (day and carry-forward activity per instrument).

```python
from pyarrow_client import ArrowClient

client = ArrowClient(app_id="your_app_id")
# ... authenticate ...

positions = client.get_positions()

for position in positions:
    print(f"{position['symbol']} ({position['exchange']})")
    print(f"  Net qty: {position['qty']} | Product: {position['product']}")
    print(f"  Day buy: {position['dayBuyQty']} @ avg {position['dayBuyAvgPrice']}")
    print(f"  Day sell: {position['daySellQty']} @ avg {position['daySellAvgPrice']}")
    ltp = position.get("ltp") or "0"
    if ltp and ltp != "0":
        print(f"  LTP: {ltp}")
    print("-" * 40)
```

### Sample response

```json
{
  "userID": "AJ0001",
  "token": "1398464",
  "exchange": "MCXFO",
  "symbol": "GOLDPETAL30JUN26F",
  "segment": "FO",
  "product": "M",
  "qty": "0",
  "avgPrice": "0",
  "dayBuyQty": "1",
  "daySellQty": "1",
  "dayBuyAmount": "14675",
  "dayBuyAvgPrice": "14675",
  "daySellAmount": "14673",
  "daySellAvgPrice": "14673",
  "carryForwardBuyQty": "0",
  "carryForwardSellQty": "0",
  "carryForwardBuyAmount": "0",
  "carryForwardBuyAvgPrice": "0",
  "carryForwardSellAmount": "0",
  "carryForwardSellAvgPrice": "0",
  "carryForwardAvgPrice": "",
  "ltp": "0",
  "tickSize": "1",
  "lotSize": "1",
  "close": "0",
  "optionType": "XX"
}
```

### Position fields

Field | Type | Description
---|---|---
`userID` | string | User identifier
`token` | string | Instrument token
`exchange` | string | Exchange code (e.g. `NSE`, `NFO`, `MCXFO`)
`symbol` | string | Trading symbol
`segment` | string | Segment (e.g. `CM`, `FO`)
`product` | string | Product type (`I` / `C` / `M`)
`qty` | string | Net position quantity
`avgPrice` | string | Average entry price
`dayBuyQty` | string | Intraday buy quantity
`daySellQty` | string | Intraday sell quantity
`dayBuyAmount` | string | Intraday buy notional
`dayBuyAvgPrice` | string | Intraday buy average price
`daySellAmount` | string | Intraday sell notional
`daySellAvgPrice` | string | Intraday sell average price
`carryForwardBuyQty` | string | Carry-forward buy quantity
`carryForwardSellQty` | string | Carry-forward sell quantity
`carryForwardBuyAmount` | string | Carry-forward buy amount
`carryForwardBuyAvgPrice` | string | Carry-forward buy average price
`carryForwardSellAmount` | string | Carry-forward sell amount
`carryForwardSellAvgPrice` | string | Carry-forward sell average price
`carryForwardAvgPrice` | string | Carry-forward average price (may be empty)
`ltp` | string | Last traded price (may be `"0"` or empty off-hours)
`tickSize` | string | Tick size
`lotSize` | string | Lot size
`close` | string | Previous close
`optionType` | string | Option type for derivatives (e.g. `CE`, `PE`, `XX`)

Optional fields

Older REST samples also list `realisedPnL`, `unrealisedMarkToMarket`, `breakEvenPrice`, `accountID`, and upload-price fields. Those keys were **not present** on a live MCXFO position row (flat `qty: "0"`). They may appear on other segments or when P&L is populated — use `.get()` when reading them.

See also [Positions API](../../rest-api/positions/).

## Holdings

`get_holdings()` returns a **list** of delivery holdings.

```python
holdings = client.get_holdings()

for holding in holdings:
    symbols = holding.get("symbols", [])
    primary = symbols[0] if symbols else {}
    print(f"Symbol: {primary.get('tradingSymbol', 'N/A')}")
    print(f"Qty: {holding['qty']} | Sellable: {holding.get('sellableQty', '0')}")
    print(f"Avg price: {holding['avgPrice']}")
    print("-" * 40)
```

### Holdings fields

Field | Type | Description
---|---|---
`symbols` | list | Per-exchange entries: `symbol`, `tradingSymbol`, `exchange`, `token`, `isin`
`qty` | string | Total quantity
`avgPrice` | string | Average purchase price
`usedQty` | string | Quantity already used
`t1Qty` | string | T+1 quantity
`depositoryQty` | string | Depository quantity
`collateralQty` | string | Collateral quantity
`pendingCollateralQty` | string | Pending collateral quantity
`brokerCollateralQty` | string | Broker collateral quantity
`authorizedQty` | string | Authorized quantity
`unPledgedQty` | string | Unpledged quantity
`nonPOAQty` | string | Non-POA quantity
`haircut` | string | Collateral haircut
`effectiveQty` | string | Effective holding quantity
`sellableQty` | string | Quantity available to sell
`ltp` | string | Last traded price (may be empty off-hours)
`pnl` | string | P&L (may be empty until LTP is populated)
`close` | string | Previous close

## Order Book

`get_order_book()` returns a **list** of order events for the day. The SDK parses `orderTime` to epoch seconds when it matches `YYYY-MM-DDTHH:MM:SS`.

```python
orders = client.get_order_book()

for order in orders:
    print(f"Order ID: {order['id']}")
    print(f"Symbol: {order['symbol']} ({order['exchange']})")
    print(f"Type: {order['transactionType']} {order['order']}")
    print(f"Qty: {order['quantity']} @ {order['price']}")
    print(f"Status: {order['orderStatus']}")
    if order.get("rejectReason"):
        print(f"Reason: {order['rejectReason']}")
    print("-" * 40)
```

### Order book fields (common)

Field | Type | Description
---|---|---
`id` | string | Order identifier (use for modify/cancel)
`userID` | string | User identifier
`accountID` | string | Account identifier
`exchange` | string | Exchange code
`symbol` | string | Trading symbol
`token` | string | Instrument token
`orderStatus` | string | `PENDING`, `OPEN`, `COMPLETE`, `CANCELLED`, `REJECTED`, etc.
`reportType` | string | Event type (e.g. `Fill`, `Rejected`)
`transactionType` | string | `B` (buy) or `S` (sell)
`order` | string | `LMT`, `MKT`, etc.
`product` | string | `I`, `C`, `M`
`quantity` | string | Order quantity
`price` | string | Order price
`disclosedQuantity` | string | Disclosed quantity
`cumulativeFillQty` | string | Filled quantity so far
`fillShares` | string | Fill quantity in this update
`fillPrice` | string | Fill price in this update
`averagePrice` | string | Average execution price
`orderTime` | int | Order time (epoch seconds after SDK parsing)
`rejectReason` | string | Present when rejected
`remarks` | string | Order tag
`validity` | string | `DAY`, `IOC`, etc.
`orderTriggerPrice` | string | Trigger price for stop orders
`tickSize` | string | Tick size
`lotSize` | string | Lot size
`pricePrecision` | string | Price decimal precision
`orderSource` | string | e.g. `API`, `WEB`
`algoType` | string | e.g. `NONE`

## Trade Book

`get_trade_book()` returns a **list** of executed trades. The SDK may parse `fillTime` when present.

```python
trades = client.get_trade_book()

for trade in trades:
    print(f"Order ID: {trade.get('orderID', 'N/A')}")
    print(f"Symbol: {trade['symbol']} ({trade['exchange']})")
    print(f"Fill: {trade.get('fillQuantity', trade.get('quantity'))} @ {trade.get('fillPrice')}")
    print(f"Time: {trade.get('fillTime', '')}")
    print("-" * 40)
```

### Trade book fields

Field | Type | Description
---|---|---
`orderID` | string | Related order identifier
`userID` | string | User identifier
`accountID` | string | Account identifier
`exchange` | string | Exchange code
`symbol` | string | Trading symbol
`token` | string | Instrument token
`quantity` | string | Trade quantity
`product` | string | Product type
`transactionType` | string | `B` or `S`
`order` | string | Order type
`fillID` | string | Exchange fill identifier
`fillPrice` | string | Execution price
`fillQuantity` | string | Executed quantity
`fillShares` | string | Fill shares
`averagePrice` | string | Average price
`fillTime` | string | Fill timestamp (`YYYY-MM-DD HH:MM:SS`)
`exchangeOrderID` | string | Exchange order ID
`tickSize` | string | Tick size
`lotSize` | string | Lot size
`pricePrecision` | string | Price precision
`orderSource` | string | Order source
`algoType` | string | Algorithm type

Note

Trade rows use **`orderID`** , not `orderNo`. Use `trade.get("orderID")`.

## User Limits & Funds

`get_user_limits()` returns a **dict** with `allocations` (per segment) and `margin` (account summary).

```python
limits = client.get_user_limits()

for allocation in limits.get("allocations", []):
    print(f"Segment: {allocation.get('segment')}")
    print(f"  Cash current: {allocation.get('cashCurrent')}")

margin = limits.get("margin", {})
print(f"Allocated: {margin.get('allocated')}")
print(f"Usable margin: {margin.get('usableMargin')}")
print(f"Net PnL: {margin.get('netPnl')}")
```

### Margin summary fields (live)

Field | Description
---|---
`allocated` | Total allocated margin
`utilized` | Margin utilized
`usableMargin` | Margin available for trading
`netPnl` | Net P&L
`mtmLoss` | Mark-to-market loss
`totalCash` | Total cash
`totalCashEq` | Total cash equivalent
`totalNoncash` | Total non-cash collateral
`cashAvailableForCNC` | Cash available for CNC
`cashAvailableForOptionBuy` | Cash available for option buys
`brokerage` | Brokerage component
`spanMargin` | SPAN margin
`exposureMargin` | Exposure margin
`totalMargin` | Total margin

### Allocation fields

Field | Description
---|---
`segment` | `CM`, `FO`, `MCX`, etc.
`cashCurrent` | Current cash
`cashOpening` | Opening cash
`cashEqCurrent` | Current cash equivalent
`cashEqOpening` | Opening cash equivalent
`nonCashCurrent` | Current non-cash
`nonCashOpening` | Opening non-cash

See [Funds API](../../rest-api/funds/) for additional REST reference.

## User Details

```python
user = client.get_user_details()

print(f"User ID: {user.get('id')}")
print(f"Name: {user.get('name')}")
print(f"Email: {user.get('email')}")
```

## Complete Example

```python
from pyarrow_client import ArrowClient

def portfolio_dashboard(client):
    user = client.get_user_details()
    print(f"Welcome, {user.get('name', 'Trader')}!")

    limits = client.get_user_limits()
    margin = limits.get("margin", {})
    print(f"Usable margin: {margin.get('usableMargin', '0')}")

    holdings = client.get_holdings()
    print(f"Holdings: {len(holdings)} instruments")

    positions = client.get_positions()
    print(f"Position rows: {len(positions)}")

    orders = client.get_order_book()
    open_orders = [o for o in orders if o.get("orderStatus") in ("PENDING", "OPEN")]
    print(f"Today's orders: {len(orders)} ({len(open_orders)} open)")

    trades = client.get_trade_book()
    print(f"Trades executed: {len(trades)}")

client = ArrowClient(app_id="your_app_id")
# ... authenticate ...
portfolio_dashboard(client)
```
