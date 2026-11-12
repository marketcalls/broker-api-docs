<!-- Source: https://vortex.rupeezy.in/docs/2.2/regular-order/ -->

# Orders

Use the below apis to place and manage order:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/trading/orders/regular](#placing-an-order) | Place order | 10/sec |
| `PUT` | [{{base_url}}/trading/orders/regular/{order_id}](#modifying-an-order) | Modify Order | 10/sec |
| `DELETE` | [{{base_url}}/trading/orders/regular/{order_id}](#cancel-an-order) | Cancel an Order | 10/sec |
| `POST` | [{{base_url}}/trading/orders/regular/multi_delete](#cancel-multiple-orders) | Cancel multiple orders | 1/sec |
| `GET` | [{{base_url}}/trading/orders](#fetching-order-book) | Fetch the entire order book | 10/sec |
| `GET` | [{{base_url}}/trading/orders/{order_id}](#fetching-order-history) | Fetch order history | 10/sec |
| `PUT` | [{{base_url}}/trading/orders/{order_id}/tags](#modify-order-tags) | Modify Order Tags | 10/sec |

## Placing an order

```
Endpoint: {{base_url}}/trading/orders/regular
```

### Place Order Object

```
{
    "ticker": "NSE:IDEA",
    "transaction_type": "BUY",
    "product": "INTRADAY",
    "variety": "SL",
    "quantity": 2,
    "price": 10.5,
    "trigger_price": 10.2,
    "disclosed_quantity": 0,
    "validity": "DAY",
    "is_amo": false,
    "order_identifier": "Your identifier",
    "gtt": {
        "profit_trigger_percent": 1,
        "profit_variety": "RL-MKT",
        "sl_trigger_percent": -1,
        "sl_variety": "RL-MKT",
        "trail_jump_point": 2,
        "trail_jump_type": "Point"
    },
    "tag_ids": [1,2,3]
}
```

| field | Required | description |
| --- | --- | --- |
| ticker | Y* | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:RELIANCE`, `NSE:NIFTY26JUL25000CE`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| exchange | Y* | Possible values: [NSE_EQ, NSE_FO, NSE_CUR or MCX_FO]. Required if `ticker` is not provided. |
| token | Y* | Security token of the scrip. Found in the [scripmaster](16-instrument-list.md) file. Required if `ticker` is not provided. |
| transaction_type | Y | Possible values: [BUY , SELL] |
| product | Y | Possible values: [INTRADAY , DELIVERY ,BTST , MTF].MTF & BTST product can only be used in NSE_EQ exchange. |
| variety | Y | Possible values: [RL, RL-MKT, SL, SL-MKT]. RL means regular orders, SL means Stop Loss order. MKT means that the trade will happen at market price |
| quantity | Y | For exchange NSE_FO, if you want to trade in 2 lots and lot size is 50, you should pass 100. In all other exchanges, you should pass just the number of lots. For example, in MCX_FO, if you want to trade 5 lots, you should pass just 5. |
| price | Y | Price should be an integer multiple of Tick Size. For example, IDEA's tick size is 0.05. So the price entered can be 9.5 or 9.65. It cannot be 9.67. In case of market orders, you should send the Last Trade Price as 0 |
| trigger_price | Y | To be used for Stop loss orders. For BUY side SL orders, trigger_price should be lesser than price. for SELL side SL orders, trigger_price should be greater than price. |
| disclosed_quantity | Y | Can be any number lesser than or equal to quantity, including 0 |
| validity | Y | Can be **DAY** for orders which are valid throughout the day, or **IOC**. IOC order will be cancelled if it is not traded immediately |
| is_amo | Y | Possible values: [true,false]. Should be set to true if order is being placed after market hours |
| order_identifier | O | This is any value that you want to associate with this order for your reference. It does not need to be unique. Max length 50. |
| gtt | O | Refer [here](#gtt-order-while-order-placement) for GTT Order functioning. |
| tag_ids | O | Array of tag ids that you want to be associated with this order. Refer [Tags](23-tags.md) to know more |

### Place Order Response

#### Success

```
{
    "data": {
        "order_id": "NXAAE0001851"
    },
    "message": "Order placed successfully",
    "status": "success"
}
```

#### Error

```
{
    "status": "error",
    "code": "e-103",
    "message": "Only AMO allowed in AMO timing for segment : 1"
}
```

| field | description |
| --- | --- |
| status | Possible values: [success,error] |
| code | Error Code |
| message | Description of the error, if any |
| data | Contains order id of the order placed. This order id can be used to identify order in order book |

> [!WARNING]
>
> If user's POA is not completed, and an order to sell holdings is sent, the API will return with an additional parameter `url`. It will have the url that needs to be opened to complete user's E-DIS authorization. Post authorization, the order needs to be retried.

### GTT Order while order placement

- We take `sl_trigger_percent`, `sl_variety`, `profit_trigger_percent` and `profit-variety`. You can specify both stoploss and profit or either of them.
- We optionally take `trail_jump_point` and `trail_jump_type` to enable Trailing SL on the GTT. Read more ([here](https://support.rupeezy.in/support/solutions/articles/21000003800-trailing-stop-loss))
- If the transaction type of main order is `BUY` then `sl_trigger_percent` is negative and `profit_trigger_percent` is positive, and vice-versa.
- When your main order is fully executed, the system creates corresponding GTT orders based on the average trade price of the main order. For example, if the main order is of BUY and the average trade price is 100 with `profit_trigger_percent` as 15, then a GTT sell order with limit price 115 is placed.
- If both SL and Profit percentages were given, the GTT orders are placed in `OCO` fashion.
- The `trail_jump_point` should be positive. If the main order is `SELL` then the stoploss moves down when the condition is met and vice versa for `BUY` order.
- If the main order is not executed, you will not see the corresponding GTT orders in [GTT Order book](09-gtt-order.md#fetching-gtt-order-book)
- If the product is `INTRADAY`, then the GTT orders placed will not be cancelled at the end of the day. You have to manage their cancellation/retention yourself.

## Fetching Order Book

```
Endpoint: {{base_url}}/trading/orders
```

### Order Book Response

```
{
    "status": "success",
    "orders": [
        {
            "order_id": "NXAAE00003K3",
            "ticker": "NSE:IDEA",
            "exchange": "NSE_EQ",
            "token": 14366,
            "order_number": "0",
            "status": "PENDING",
            "error_reason": "",
            "transaction_type": "BUY",
            "product": "DELIVERY",
            "variety": "SL",
            "total_quantity": 1,
            "pending_quantity": 1,
            "traded_quantity": 0,
            "disclosed_quantity": 0,
            "disclosed_quantity_remaining": 0,
            "order_price": 9.50,
            "trigger_price": 9.20,
            "traded_price": 0.0,
            "validity": "DAY",
            "symbol": "IDEA",
            "series": "EQ",
            "instrument_name": "",
            "expiry_date": "",
            "strike_price": 0.00,
            "option_type": "  ",
            "lot_size": 1,
            "order_created_at": "2023-03-27 18:47:41",
            "initiated_by": "MOBILE-Ex",
            "modified_by": "MOBILE-Ex",
            "is_amo": true,
            "order_identifier": "Your identifier"
            "tag_ids":[1,2,3], 
            "middleware_order_id": 12341
        }
    ],
    "metadata": {
        "total_records": 1,
        "all_records": 1,
        "completed_records": 0,
        "open_records": 1
    }
}
```

## Fetching order history

```
Endpoint: {{base_url}}/trading/orders/{order_id}
```

### Order History Response

```
{
    "status": "success",
    "code": "s-101",
    "message": "Order history data fetched successfully",
    "data": [
        {
            "order_id": "NXAAE00022D6",
            "ticker": "NSE:IOC",
            "exchange": "NSE_EQ",
            "token": 1624,
            "order_number": "1100000030057376",
            "status": "EXECUTED",
            "error_reason": "",
            "transaction_type": "SELL",
            "product": "INTRADAY",
            "variety": "RL-MKT",
            "total_quantity": 1,
            "pending_quantity": 0,
            "traded_quantity": 1,
            "disclosed_quantity": 0,
            "order_price": 91.95,
            "trigger_price": 0.00,
            "validity": "DAY",
            "validity_days": 0,
            "symbol": "IOC",
            "series": "EQ",
            "instrument_name": "",
            "expiry_date": "",
            "strike_price": 0.00,
            "option_type": "",
            "order_created_at": "2023-06-20 15:14:39",
            "exchange_order_created_at": "2023-06-20 15:14:39",
            "initiated_by": "MOBILE-Ex",
            "modified_by": "MOBILE-Ex",
            "is_amo": false,
            "order_identifier": ""
        },
        {
            "order_id": "NXAAE00022D6",
            "ticker": "NSE:IOC",
            "exchange": "NSE_EQ",
            "token": 1624,
            "order_number": "1100000030057376",
            "status": "PENDING",
            "error_reason": "",
            "transaction_type": "SELL",
            "product": "INTRADAY",
            "variety": "RL-MKT",
            "total_quantity": 1,
            "pending_quantity": 1,
            "traded_quantity": 0,
            "disclosed_quantity": 0,
            "order_price": 92.00,
            "trigger_price": 0.00,
            "validity": "DAY",
            "validity_days": 0,
            "symbol": "IOC",
            "series": "EQ",
            "instrument_name": "",
            "expiry_date": "",
            "strike_price": 0.00,
            "option_type": "",
            "order_created_at": "2023-06-20 15:14:39",
            "exchange_order_created_at": "2023-06-20 15:14:39",
            "initiated_by": "MOBILE-Ex",
            "modified_by": "MOBILE-Ex",
            "is_amo": false,
            "order_identifier": ""
        },
        {
            "order_id": "NXAAE00022D6",
            "ticker": "NSE:IOC",
            "exchange": "NSE_EQ",
            "token": 1624,
            "order_number": "0",
            "status": "OMSXMITTED",
            "error_reason": "",
            "transaction_type": "SELL",
            "product": "INTRADAY",
            "variety": "RL-MKT",
            "total_quantity": 1,
            "pending_quantity": 1,
            "traded_quantity": 0,
            "disclosed_quantity": 0,
            "order_price": 92.00,
            "trigger_price": 0.00,
            "validity": "DAY",
            "validity_days": 0,
            "symbol": "IOC",
            "series": "EQ",
            "instrument_name": "",
            "expiry_date": "",
            "strike_price": 0.00,
            "option_type": "",
            "order_created_at": "2023-06-20 15:14:39",
            "exchange_order_created_at": "1900-01-01 00:00:10",
            "initiated_by": "MOBILE-Ex",
            "modified_by": "MOBILE-Ex",
            "is_amo": false,
            "order_identifier": ""
        }
    ],
    "metadata": {
        "total_records": 3
    }
}
```

## Modifying an order

- Only a subset of fields can be modified for a particular order. If for example you want to change the product from INTRADAY to DELIVERY, you must cancel the previous order and place a new order.
- `traded_quantity` is the quantity already traded in the order. You must pass the latest value here as received in the orderbook. If for example you have placed an order for 100 quantity out of which 20 are already traded, and in the modify order object, you pass quantity as 100 and traded_quantity as 0, the order shall then become of total quanity 120 and traded_quantity 20.
- `price` and `trigger_price` modification is applied to only the remaining quantity that is not yet traded.
- RL orders cannot become SL orders. If an SL order is triggered, it cannot be modified as SL order again. You must cancel the previous order and create a new order.

### Modify Order Object

```
{
    "variety": "SL",
    "quantity": 100,
    "traded_quantity": 20 , 
    "price": 10.5,
    "trigger_price": 10.2,
    "disclosed_quantity": 0,
    "validity": "DAY"
}
```

### Modify Order Response

#### Success

```
{
    "status": "success",
    "code": "s-101",
    "message": "Order Entry Sent to OMS",
    "data": {
        "order_id": "NXAAE00002K3"
    }
}
```

#### Error

```
{
    "status": "error",
    "code": "e-103",
    "message": "Only AMO allowed in AMO timing for segment : 1"
}
```

## Cancel an Order

```
Endpoint: {{base_url}}/trading/orders/regular/{order_id}
```

### Cancel Order Response

```
{
    "status": "success",
    "code": "s-101",
    "message": "Order Cancellation Sent to OMS",
    "data": {
        "order_id": "NXAAE00003K3"
    }
}
```

## Cancel Multiple Orders

```
Endpoint: {{base_url}}/trading/orders/regular/multi_delete
```

> [!NOTE]
>
> At max 10 orders can be sent together for cancellation

### Cancel Multiple Orders Request

```
{
    "order_ids": ["NXAAE00007N1", "NXAAE00006N1"]
}
```

### Cancel Multiple Orders Response

```
{   "status": "success",
    "data": 
        [
            {
                "message": "Order Cancellation Sent to OMS",
                "code": "s-101",
                "status": "success",
                "data": {
                    "order_id": "NXAAE00007N1"
                }
            },
            {
                "message": "Order Cancellation Sent to OMS",
                "code": "s-101",
                "status": "success",
                "data": {
                    "order_id": "NXAAE00006N1"
                }
            }
        ]
}
```

## Modify Order Tags

```
Endpoint: {{base_url}}/trading/orders/{order_id}/tags
```

### Modify Tags Object

```
{
    "tag_ids": [3,4,5]
}
```
