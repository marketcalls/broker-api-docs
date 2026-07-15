> Source: https://docs.arrow.trade/python-sdk/orders/

# Orders

The PyArrow SDK provides comprehensive order management capabilities including placing, modifying, and canceling orders across all supported exchanges.

## Order Parameters

### Exchanges

Exchange | Code | Description
---|---|---
NSE | `Exchange.NSE` | National Stock Exchange - Equity
BSE | `Exchange.BSE` | Bombay Stock Exchange - Equity
NFO | `Exchange.NFO` | NSE Futures & Options
BFO | `Exchange.BFO` | BSE Futures & Options
MCX | `Exchange.MCX` | Multi Commodity Exchange
INDEX | `Exchange.INDEX` | Index segment (utility / option-chain APIs)

### Order Types

Type | Code | Description | Use Case
---|---|---|---
Market | `OrderType.MARKET` (alias: `OrderType.MKT`) | Plain market orders are disabled by default on the API (regulatory). Use `mpp=True` on `place_order` / `modify_order` to mimic a market order (Upper Limit or DPR, by instrument) | Immediate-style execution via `mpp`
Limit | `OrderType.LIMIT` | Execute at specified price or better | Price control priority
Stop Loss Limit | `OrderType.STOP_LOSS_LIMIT` (alias: `OrderType.SL_LMT`) | Limit order activated at trigger | Risk management with price control
Stop Loss Market | `OrderType.STOP_LOSS_MARKET` (alias: `OrderType.SL_MKT`) | Market order activated at trigger | Risk management with speed priority

### Product Types

Product | Code | Description | Settlement
---|---|---|---
Intraday | `ProductType.MIS` | Same-day position closure | Auto-squared off at 3:15 PM
Cash & Carry | `ProductType.CNC` | Equity delivery orders | T+1 settlement
Normal | `ProductType.NRML` | F&O margin orders | Standard margin

### Order Validity

Validity | Code | Description
---|---|---
Day | `Retention.DAY` | Valid until market close
IOC | `Retention.IOC` | Immediate or Cancel

### Transaction Types

Type | Code | Description
---|---|---
Buy | `TransactionType.BUY` | Buy transaction
Sell | `TransactionType.SELL` | Sell transaction

Market orders and `mpp`

Under current regulations, **plain`MKT` orders are disabled by default** on the API. Pass **`mpp=True`** to **`place_order()`** or **`modify_order()`** to send a **`LIMIT`** order at the **Upper Limit** or **DPR** , **depending on instrument type** , and mimic market-style execution. In rare cases of **extreme volatility or sharp price movement** , this can still leave the order **open** (fully or partially unfilled).

Cover orders

`Variety.COVER` may be used when **placing** orders. **`modify_order()`** and **`cancel_order()`** always target **`/order/regular/{id}`** in the current SDK.

## Place Order

Place a new trading order with full parameter control.

### Basic Example

```python
from pyarrow_client import (
    ArrowClient, Exchange, OrderType, ProductType,
    TransactionType, Variety, Retention
)

client = ArrowClient(app_id="your_app_id")
# ... authenticate ...

# Place a limit buy order
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

print(f"Order placed: {order_id}")
```

### Market-style order (`mpp`)

```python
# Regulatory default: plain MKT is disabled. Use mpp=True to mimic a market order
# (order priced at Upper Limit or DPR per instrument type).
order_id = client.place_order(
    exchange=Exchange.NSE,
    symbol="RELIANCE-EQ",
    quantity=10,
    disclosed_quantity=0,
    product=ProductType.MIS,  # Intraday
    order_type=OrderType.MARKET,
    variety=Variety.REGULAR,
    transaction_type=TransactionType.BUY,
    price=0,
    validity=Retention.DAY,
    mpp=True,
)
```

### Limit Order

```python
# Limit order - executes at specified price or better
order_id = client.place_order(
    exchange=Exchange.NSE,
    symbol="INFY-EQ",
    quantity=5,
    disclosed_quantity=0,
    product=ProductType.CNC,  # Delivery
    order_type=OrderType.LIMIT,
    variety=Variety.REGULAR,
    transaction_type=TransactionType.BUY,
    price=1500.50,
    validity=Retention.DAY
)
```

### Stop Loss Order

```python
# Stop Loss Limit order
order_id = client.place_order(
    exchange=Exchange.NSE,
    symbol="TCS-EQ",
    quantity=2,
    disclosed_quantity=0,
    product=ProductType.CNC,
    order_type=OrderType.STOP_LOSS_LIMIT,
    variety=Variety.REGULAR,
    transaction_type=TransactionType.SELL,
    price=3400.0,        # Limit price
    trigger_price=3410.0, # Trigger price
    validity=Retention.DAY
)
```

### F&O Order

```python
# Futures & Options order on NFO
order_id = client.place_order(
    exchange=Exchange.NFO,
    symbol="NIFTY02JAN25C26000",  # NIFTY Call Option
    quantity=75,  # Lot size
    disclosed_quantity=0,
    product=ProductType.NRML,
    order_type=OrderType.LIMIT,
    variety=Variety.REGULAR,
    transaction_type=TransactionType.BUY,
    price=150.0,
    validity=Retention.DAY
)
```

### Iceberg Order (Disclosed Quantity)

```python
# Large order with disclosed quantity
order_id = client.place_order(
    exchange=Exchange.NSE,
    symbol="RELIANCE-EQ",
    quantity=1000,
    disclosed_quantity=100,  # Only 100 visible at a time
    product=ProductType.CNC,
    order_type=OrderType.LIMIT,
    variety=Variety.REGULAR,
    transaction_type=TransactionType.BUY,
    price=1450.0,
    validity=Retention.DAY
)
```

## Modify Order

Modify an existing open order's price, quantity, or other parameters.

```python
# Modify an existing order
message = client.modify_order(
    order_id="24012400000321",
    exchange=Exchange.NSE,
    symbol="RELIANCE-EQ",
    quantity=2,             # Changed quantity
    price=1500.0,           # New price
    disclosed_qty=0,
    product=ProductType.CNC,
    transaction_type=TransactionType.BUY,
    order_type=OrderType.LIMIT,
    validity=Retention.DAY,
    remarks="Modified order",
    trigger_price=1480.0,   # Optional: for SL orders (sent as triggerPrice)
)

print(f"Modification result: {message}")
```

Modification Restrictions

  * Cannot modify executed orders
  * Cannot change exchange or symbol
  * Cannot change transaction type (Buy/Sell)

## Cancel Order

Cancel a pending or open order.

### Cancel Single Order

```python
# Cancel a specific order
message = client.cancel_order(order_id="24012400000321")
print(f"Cancel result: {message}")
```

### Cancel All Orders

Cancel all open/pending orders in bulk using threading for faster execution:

```python
# Cancel all open orders
results = client.cancel_all_orders()

for order_id, status, result in results:
    print(f"Order {order_id}: {status} - {result}")
```

Bulk Cancel

The `cancel_all_orders()` method is an SDK convenience wrapper (not a single REST route). It fetches the order book, filters standing orders, and cancels them in parallel (up to 9 workers).

## Margin helpers

`order_margin()` and `basket_margin()` are documented in the [API Reference](../api-reference/). The SDK sends `symbol` (trading symbol) in margin requests; some REST examples use numeric instrument `token` instead — use symbols when calling the Python client. Basket margin is sent as `{ "orders": [...], "includePositions": bool }`, not a bare JSON array.

Live `order_margin` response: `requiredMargin`, `minimumCashRequired`, `marginUsedAfterTrade`, `charge`.

Live `basket_margin` response: `final_margin`, `initial_margin`, `orders` (each with `margin`, `symid`, `charge`).

## Order Tracking

### Get Order Details

Retrieve comprehensive order history and execution details:

```python
# Get specific order details
order_details = client.get_order_details(order_id="24012400000321")

for detail in order_details:
    print(f"Status: {detail['orderStatus']}")
    print(f"Report Type: {detail['reportType']}")
    print(f"Filled: {detail['cumulativeFillQty']}/{detail['quantity']}")
    print(f"Average Price: {detail['averagePrice']}")
```

### Order Status Types

Status | Description | Next Action
---|---|---
`PENDING` | Order submitted, awaiting confirmation | Monitor for updates
`OPEN` | Order active in the market | Can modify or cancel
`COMPLETE` | Order fully executed | Review execution details
`CANCELLED` | Order cancelled by user/system | No further action
`REJECTED` | Order rejected by exchange | Check rejection reason

### Get Order Book

Access your complete order book:

```python
# Get all orders for the day
orders = client.get_order_book()

for order in orders:
    print(f"Order ID: {order['id']}")
    print(f"Symbol: {order['symbol']}")
    print(f"Status: {order['orderStatus']}")
    print(f"Type: {order['transactionType']} {order['order']}")
    print(f"Qty: {order['quantity']} @ ₹{order['price']}")
    print("-" * 40)
```

### Get Trade Book

Review all executed trades:

```python
# Get all trades for the day
trades = client.get_trade_book()

for trade in trades:
    print(f"Order ID: {trade['id']}")
    print(f"Symbol: {trade['symbol']}")
    print(f"Fill Price: ₹{trade['fillPrice']}")
    print(f"Fill Qty: {trade['fillQuantity']}")
    print(f"Fill Time: {trade['fillTime']}")
    print("-" * 40)
```

## Order Response Fields

### Order Book Response

Field | Type | Description
---|---|---
`id` | string | Order ID
`exchange` | string | Exchange code
`symbol` | string | Trading symbol
`price` | string | Order price
`quantity` | string | Order quantity
`product` | string | Product type (I/C/M)
`orderStatus` | string | Current status
`transactionType` | string | Buy (B) / Sell (S)
`order` | string | Order type
`cumulativeFillQty` | string | Quantity filled
`averagePrice` | string | Average fill price
`exchangeOrderID` | string | Exchange order number
`orderTime` | string | Order timestamp
`rejectReason` | string | Rejection reason (if any)

## Complete Example

```python
from pyarrow_client import (
    ArrowClient, Exchange, OrderType, ProductType,
    TransactionType, Variety, Retention
)

def trading_example():
    # Initialize and authenticate
    client = ArrowClient(app_id="your_app_id")
    client.auto_login(
        user_id="your_user_id",
        password="your_password",
        app_secret="your_app_secret",
        totp_secret="your_totp_secret"
    )

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
    print(f"✓ Order placed: {order_id}")

    # Check order status
    details = client.get_order_details(order_id)
    print(f"✓ Order status: {details[0]['orderStatus']}")

    # Modify order price
    if details[0]['orderStatus'] == 'OPEN':
        client.modify_order(
            order_id=order_id,
            exchange=Exchange.NSE,
            symbol="RELIANCE-EQ",
            quantity=1,
            price=1455.0,
            disclosed_qty=0,
            product=ProductType.CNC,
            transaction_type=TransactionType.BUY,
            order_type=OrderType.LIMIT,
            validity=Retention.DAY
        )
        print("✓ Order modified")

    # View order book
    orders = client.get_order_book()
    print(f"✓ Total orders today: {len(orders)}")

    # View trade book
    trades = client.get_trade_book()
    print(f"✓ Total trades today: {len(trades)}")

if __name__ == "__main__":
    trading_example()
```

## Error Handling

```python
try:
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
    print(f"Order placed: {order_id}")

except Exception as e:
    print(f"Order failed: {e}")
```

### Common Order Errors

Error | Cause | Solution
---|---|---
Insufficient margin | Not enough funds | Add funds or reduce quantity
Price outside DPR | Price beyond daily range | Adjust price within limits
Invalid symbol | Symbol not found | Verify symbol format
Market closed | Outside trading hours | Wait for market hours
Quantity not in lot | F&O lot size mismatch | Use correct lot multiples

Best Practices

  * Always validate order parameters before submission
  * Implement proper error handling for all order operations
  * Monitor position limits and margin requirements
  * Use `remarks` for order identification in bulk operations (max 16 characters)
