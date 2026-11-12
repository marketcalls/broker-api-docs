<!-- Source: https://vortex.rupeezy.in/docs/2.2/iceberg-order/ -->

# Iceberg Orders

Use the below apis to place and manage order:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/trading/orders/iceberg](#placing-an-iceberg-order) | Place iceberg order | 1/sec |
| `PUT` | [{{base_url}}/trading/orders/iceberg/{iceberg_order_id}](#modifying-an-iceberg-order) | Modify Order | 1/sec |
| `DELETE` | [{{base_url}}/trading/orders/iceberg/{iceberg_order_id}](#cancel-an-iceberg-order) | Cancel an Order | 10/sec |

> [!NOTE]
>
> An iceberg order creates a sequence of sub orders after the previous sub order is fully executed.

## Placing an Iceberg order

```
Endpoint: {{base_url}}/trading/orders/iceberg
```

### Place Order Object

```
{
    "ticker": "NSE:IDEA",
    "transaction_type": "BUY",
    "product": "INTRADAY",
    "variety": "RL",
    "quantity": 2,
    "price": 10.5,
    "trigger_price": 10.2,
    "disclosed_quantity": 0,
    "validity": "DAY",
    "order_identifier": "Your identifier",
    "legs": 2
    "tag_ids": [1,2,3]
}
```

| field | Required | description |
| --- | --- | --- |
| ticker | Y* | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:RELIANCE`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| exchange | Y* | Possible values: [NSE_EQ, NSE_FO, NSE_CUR or MCX_FO]. Required if `ticker` is not provided. |
| token | Y* | Security token of the scrip, found in the scripmaster file. Required if `ticker` is not provided. |
| transaction_type | Y | Possible values: [BUY , SELL] |
| product | Y | Possible values: [INTRADAY, DELIVERY, BTST, MTF].MTF & BTST product can only be used in NSE_EQ exchange. |
| variety | Y | Possible values: [RL, SL]. Market orders are not allowed in this order type. |
| quantity | Y | For exchange NSE_FO, if you want to trade in 2 lots and lot size is 50, you should pass 100. In all other exchanges, you should pass just the number of lots. For example, in MCX_FO, if you want to trade 5 lots, you should pass just 5. |
| price | Y | Price should be an integer multiple of Tick Size. For example, IDEA's tick size is 0.05. So the price entered can be 9.5 or 9.65. It cannot be 9.67. In case of market orders, you should send the Last Trade Price as 0 |
| trigger_price | Y | To be used for Stop loss orders. For BUY side SL orders, trigger_price should be lesser than price. for SELL side SL orders, trigger_price should be greater than price. |
| disclosed_quantity | Y | Can be any number lesser than or equal to quantity, including 0 |
| validity | Y | Can be only **DAY** |
| order_identifier | O | This is any value that you want to associate with this order for your reference. It does not need to be unique. Max length 50. |
| legs | Y | The number of legs in which the order should be split. Can be any integer between [2,10] |
| tag_ids | O | Array of tag ids that you want to be associated with this order. Refer [Tags](23-tags.md) to know more |

### Place Order Response

#### Success

```
{
    "data": {
        "first_order_id": "NXAAE0001851",
        "iceberg_order_id": "aafdfdvs-1231231-1231232"
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
    "message": "invalid price"
}
```

| field | description |
| --- | --- |
| status | Possible values: [success,error] |
| code | Error Code |
| message | Description of the error, if any |
| data | Contains iceberg order id and the order id of the first leg placed |

> [!WARNING]
>
> If user's POA is not completed, and an order to sell holdings is sent, the API will return with an additional parameter `url`. It will have the url that needs to be opened to complete user's E-DIS authorization. Post authorization, the order needs to be retried.

## Modifying an iceberg order

```
Endpoint: {{base_url}}/trading/orders/iceberg/{iceberg_order_id}
```

- Only a subset of fields can be modified for iceberg orders.
- `traded_quantity` is the quantity already traded in the latest leg of the order. You must pass the latest value here as received in the orderbook.
- `price` and `trigger_price` modification is applied to only the remaining quantity that is not yet traded in the current leg, and on all the subsequent legs.
- RL orders cannot become SL orders. If an SL order is triggered, it cannot be modified as SL order again. You must cancel the previous order and create a new order.

### Modify Order Object

```
{
    "price": 11.5,
    "trigger_price": 10.2,
    "traded_quantity":1
}
```

### Modify Order Response

#### Success

```
{
    "message": "Order modified successfully",
    "status":  "success",
}
```

#### Error

```
{
    "status": "error",
    "message": "order is fully executed"
}
```

## Cancel an Iceberg Order

```
Endpoint: {{base_url}}/trading/orders/iceberg/{iceberg_order_id}
```

### Cancel Order Response

```
{
    "message": "Order cancelled successfully",
    "status":  "success",
}
```
