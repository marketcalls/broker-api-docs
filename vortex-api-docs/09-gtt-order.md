<!-- Source: https://vortex.rupeezy.in/docs/2.2/gtt-order/ -->

# Gtt Orders

Use the below apis to place and manage order:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/trading/orders/gtt](#fetching-gtt-order-book) | Fetch the entire GTT order book | 10/sec |
| `POST` | [{{base_url}}/trading/orders/gtt](#placing-a-gtt-order) | Place GTT order | 10/sec |
| `PUT` | [{{base_url}}/trading/orders/gtt/{order_id}](#modifying-a-gtt-order) | Modify GTT Order | 10/sec |
| `DELETE` | [{{base_url}}/trading/orders/gtt/{order_id}](#cancel-a-gtt-order) | Cancel an Order | 10/sec |
| `PUT` | [{{base_url}}/trading/orders/gtt/{order_id}/tags](#modify-order-tags) | Modify Order Tags | 10/sec |

## Fetching Gtt Order Book

```
Endpoint: {{base_url}}/trading/orders/gtt
```

### Order Book Response

```
{
    "status": "success",
    "data": 
    [
        {
            "ticker": "NSE:5PAISA",
            "exchange": "NSE_EQ",
            "expiry_date": "",
            "id": "8f141670-59b3-4754-81c7-a072f3598475",
            "instrument_name": "EQUITIES",
            "lot_size": 1,
            "market_segment_id": 1,
            "option_type": "",
            "orders": [
                {
                    "created_at": "2025-06-24T12:24:32.610719Z",
                    "error_reason": "",
                    "expires_at": "2025-06-24T23:59:59Z",
                    "id": 719460,
                    "price": 0,
                    "quantity": 190,
                    "status": "active",
                    "trail": null,
                    "transaction_type": "SELL",
                    "trigerred_at": "0001-01-01T05:53:28+05:53",
                    "trigger_price": 421,
                    "updated_at": "2025-06-24T12:24:32.610719Z",
                    "variety": "RL-MKT"
                },
                {
                    "created_at": "2025-06-24T12:24:32.61525Z",
                    "error_reason": "",
                    "expires_at": "2025-06-24T23:59:59Z",
                    "id": 719461,
                    "price": 0,
                    "quantity": 190,
                    "status": "active",
                    "trail": null,
                    "transaction_type": "SELL",
                    "trigerred_at": "0001-01-01T05:53:28+05:53",
                    "trigger_price": 396,
                    "updated_at": "2025-06-24T12:24:32.61525Z",
                    "variety": "RL-MKT"
                }
            ],
            "parent_middleware_id": null,
            "product": "INTRADAY",
            "series": "EQ",
            "strike_price": 0,
            "symbol": "5PAISA",
            "tag_ids": [],
            "token": 445,
            "transaction_type": "SELL",
            "trigger_type": "oco"
        },
        {
            "ticker": "NSE:IDEA",
            "exchange": "NSE_EQ",
            "expiry_date": "",
            "id": "5959c2e6-db95-40c6-8c45-153399ea3311",
            "instrument_name": "EQUITIES",
            "lot_size": 1,
            "market_segment_id": 1,
            "option_type": "",
            "orders": [
                {
                    "created_at": "2025-06-24T13:21:21.288839Z",
                    "error_reason": "",
                    "expires_at": "2025-06-24T23:59:59Z",
                    "id": 719625,
                    "price": 0,
                    "quantity": 1,
                    "status": "active",
                    "trail": null,
                    "transaction_type": "SELL",
                    "trigerred_at": "0001-01-01T05:53:28+05:53",
                    "trigger_price": 7.35,
                    "updated_at": "2025-06-24T13:21:21.288839Z",
                    "variety": "RL-MKT"
                },
                {
                    "created_at": "2025-06-24T13:21:21.29279Z",
                    "error_reason": "",
                    "expires_at": "2025-06-24T23:59:59Z",
                    "id": 719626,
                    "price": 0,
                    "quantity": 1,
                    "status": "active",
                    "trail": {
                        "id": 719624,
                        "trail_first_jump": 7,
                        "trail_jump_point": 2,
                        "trail_jump_type": "Point",
                        "trigger_trail": 9
                    },
                    "transaction_type": "SELL",
                    "trigerred_at": "0001-01-01T05:53:28+05:53",
                    "trigger_price": 6.65,
                    "updated_at": "2025-06-24T13:21:21.29279Z",
                    "variety": "RL-MKT"
                }
            ],
            "parent_middleware_id": null,
            "product": "INTRADAY",
            "series": "EQ",
            "strike_price": 0,
            "symbol": "IDEA",
            "tag_ids": [],
            "token": 14366,
            "transaction_type": "SELL",
            "trigger_type": "oco"
        }
    ]
}
```

## Placing a GTT order

```
Endpoint: {{base_url}}/trading/orders/gtt
```

### Place Single GTT Order Object

```
{
    "ticker": "NSE:RELIANCE",
    "transaction_type": "BUY",
    "product": "DELIVERY",
    "gtt_trigger_type": "single",
    "price": 2500,
    "trigger_price": 2505,
    "quantity": 1,
    "variety": "RL",
    "tag_ids": [1,2,3],
    "trail": {
        "trail_jump_point": 2,
        "trail_jump_type": "Point"
    }
}
```

| field | Required | description |
| --- | --- | --- |
| ticker | Y* | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:RELIANCE`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| exchange | Y* | Possible values: [NSE_EQ, NSE_FO, NSE_CUR or MCX_FO]. Required if `ticker` is not provided. |
| token | Y* | Security token of the scrip, found in the scripmaster file. Required if `ticker` is not provided. |
| transaction_type | Y | Possible values: [BUY , SELL] |
| product | Y | Possible values: [INTRADAY, DELIVERY, BTST, MTF].MTF & BTST product can only be used in NSE_EQ exchange. |
| quantity | Y | For exchange NSE_FO, if you want to trade in 2 lots and lot size is 50, you should pass 100. In all other exchanges, you should pass just the number of lots. For example, in MCX_FO, if you want to trade 5 lots, you should pass just 5. |
| variety | O | Variety of the GTT order placed. Can be [`RL`,`RL-MKT`]. If you dont send anything, `RL` will be considered |
| price | O | Limit price at which the order will be executed. Should be an integer multiple of Tick Size. Optional if variety is `RL-MKT` |
| trigger_price | Y | Price at which the GTT order should be placed. It can either be greater or lower than current price. |
| trail | O | Trail object to be passed in stoploss GTT object for enabling trailing sl |
| trail.trail_jump_point | Y (if trail is present) | Trail jump amount. For example, 2 Point would jump the price of the stoploss by ₹2 |
| trail.trail_jump_type | Y (if trail is present) | Possible values: [`Point`,`Percent`] |

### Place OCO GTT Order Object

```
{
    "ticker": "NSE:RELIANCE",
    "transaction_type": "BUY",
    "gtt_trigger_type": "oco",
    "tag_ids": [1,2,3],
    "stoploss": {
        "quantity": 1, 
        "price": 2600,
        "trigger_price": 2650, 
        "variety": "RL",
        "trail": {
            "trail_jump_point": 2,
            "trail_jump_type": "Point"
        }
    },
    "profit": {
        "quantity": 1, 
        "price": 2500,
        "trigger_price": 2505, 
        "variety": "RL-MKT"
    }
}
```

| field | Required | description |
| --- | --- | --- |
| ticker | Y* | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:RELIANCE`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| exchange | Y* | Possible values: [NSE_EQ, NSE_FO, NSE_CUR or MCX_FO]. Required if `ticker` is not provided. |
| token | Y* | Security token of the scrip, found in the scripmaster file. Required if `ticker` is not provided. |
| transaction_type | Y | Possible values: [BUY , SELL] |
| quantity | Y | For exchange NSE_FO, if you want to trade in 2 lots and lot size is 50, you should pass 100. In all other exchanges, you should pass just the number of lots. For example, in MCX_FO, if you want to trade 5 lots, you should pass just 5. |
| variety | O | Variety of the GTT order placed. Can be [`RL`,`RL-MKT`]. If you dont send anything, `RL` will be considered |
| price | O | Price should be an integer multiple of Tick Size. For example, IDEA's tick size is 0.05. So the price entered can be 9.5 or 9.65. It cannot be 9.67. Optional if variety is `RL-MKT` |
| trigger_price | Y | Price at which the GTT order should be placed. If `transaction_type` = `BUY`, `stoploss`.`trigger_price` should be > `ltp` and `profit`.`trigger_price` should be < `ltp`, and vice versa. |
| trail | O | Trail object to be passed in stoploss GTT object for enabling trailing sl |
| trail.trail_jump_point | Y (if trail is present) | Trail jump amount. For example, 2 Point would jump the price of the stoploss by ₹2 |
| trail.trail_jump_type | Y (if trail is present) | Possible values: [`Point`,`Percent`] |

### Place Order Response

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
    "message": "invalid parameters"
}
```

| field | description |
| --- | --- |
| status | Possible values: [success,error] |
| code | Error Code |
| message | Description of the error, if any |
| data | Contains order id of the order placed. This order id can be used to identify order in order book |

## Modifying a GTT order

### Modify Order Object

```
[
    {
        "id": 719698,
        "price": 0,
        "quantity": 1,
        "trail": {
            "id": 719696,
            "trail_jump_point": 5,
            "trail_jump_type": "Point"
        },
        "trigger_price": 6.57,
        "variety": "RL-MKT"
    },
    {
        "id": 719697,
        "price": 0,
        "quantity": 1,
        "trigger_price": 7.27,
        "variety": "RL-MKT"
    }
]
```

| field | Required | description |
| --- | --- | --- |
| id | Y | ID of the GTT order |
| quantity | Y | For exchange NSE_FO, if you want to trade in 2 lots and lot size is 50, you should pass 100. In all other exchanges, you should pass just the number of lots. For example, in MCX_FO, if you want to trade 5 lots, you should pass just 5. |
| variety | O | Variety of the GTT order placed. Can be [`RL`,`RL-MKT`]. If you dont send anything, `RL` will be considered |
| price | O | Price should be an integer multiple of Tick Size. For example, IDEA's tick size is 0.05. So the price entered can be 9.5 or 9.65. It cannot be 9.67. Optional if variety is `RL-MKT` |
| trigger_price | Y | Price at which the GTT order should be placed. If `transaction_type` = `BUY`, `stoploss`.`trigger_price` should be > `ltp` and `profit`.`trigger_price` should be < `ltp`, and vice versa. |
| trail | O | Trail object to be passed in stoploss GTT object if it has a trailing sl |
| trail.id | Y (if trail is present) | ID of the trail order |
| trail.trail_jump_point | Y (if trail is present) | Trail jump amount. For example, 2 Point would jump the price of the stoploss by ₹2 |
| trail.trail_jump_type | Cannot be modified | Type of trail jump (Point). Cannot be changed once the order is created. |

### Modify Order Response

#### Success

```
{
    "status": "success",
    "message": "GTT  Modified",
    "data": {
        "order_id": "570cd30c-9a72-4c98-99e6-7fc7e6fe4452"
    }
}
```

#### Error

```
{
    "status": "error",
    "message": "Error while updating GTT order",
    "data": {
        "order_id": "570cd30c-9a72-4c98-99e6-7fc7e6fe4452"
    }
}
```

## Cancel a GTT Order

```
Endpoint: {{base_url}}/trading/orders/gtt/{order_id}
```

### Cancel Order Response

```
{
    "status": "success",
    "message": "GTT Deleted successfully",
    "data": {
        "order_id": "570cd30c-9a72-4c98-99e6-7fc7e6fe4452"
    }
}
```

## Modify Order Tags

```
Endpoint: {{base_url}}/trading/orders/gtt/{{uuid}}/tags
```

- Use the 36 character UUID received in GTT order book response

### Modify Tags Object

```
{
    "tag_ids": [3,4,5]
}
```
