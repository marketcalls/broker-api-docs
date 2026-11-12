<!-- Source: https://vortex.rupeezy.in/docs/2.2/margin/ -->

# Margins

Use the below apis to fetch margin requirements:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/margins/basket](#basket-margin) | Fetch margin requirement for a collection for orders | 1/sec |
| `POST` | [{{base_url}}/margins/order](#order-margin) | Fetch margin requirement for one order | 1/sec |

## Basket Margin

Use this api to calculate final margin and required margin for a collection of orders

```
Endpoint: {{base_url}}/margins/basket
```

### Basket Margin Object

```
{
    "orders": [
        {
            "ticker": "NSE:ACC",
            "transaction_type": "BUY",
            "product": "INTRADAY",
            "variety": "RL",
            "quantity": 1,
            "price": 1122.35
        }
    ]
}
```

| field | description |
| --- | --- |
| `ticker` | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:ACC`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| `exchange` | Exchange code (e.g. `NSE_EQ`, `NSE_FO`). Required if `ticker` is not provided. |
| `token` | Security token of the scrip. Required if `ticker` is not provided. |
| `quantity` | Quantity of the order. For `NSE_FO` segments, quantity is `lots` * `lot_size`. For all others, enter just the number of lots |
| `price` | Total margin which will be blocked in the system after executing all the orders |

### Basket Margin Response

```
{
    "status": "success",
    "initial_margin": 224.47,
    "required_margin": 224.47,
}
```

| field | description |
| --- | --- |
| `initial_margin` | Total margin which is required to place all orders |
| `required_margin` | Total margin which will be blocked in the system after executing all the orders |

> [!NOTE]
>
> Initial margin is dependent on the sequence in which you have passed the orders. This is particularly visible in orders that create a spread.

## Order Margin

Use this api to find the margin required to place a single order

```
Endpoint: {{base_url}}/margins/order
```

### Order Margin Object

```
{
    "ticker": "NSE:NIFTY26JUL25000CE",
    "transaction_type": "BUY",
    "product": "INTRADAY",
    "variety": "RL",
    "quantity": 50,
    "price": 80,
    "mode": "MODIFY",
    "old_quantity": 50,
    "old_price": 50
}
```

| field | description |
| --- | --- |
| `ticker` | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:NIFTY26JUL25000CE`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| `exchange` | Exchange code (e.g. `NSE_EQ`, `NSE_FO`). Required if `ticker` is not provided. |
| `token` | Security token of the scrip. Required if `ticker` is not provided. |
| `mode` | Possible values: [NEW, MODIFY] , Whether you are trying to modify an existing order or placing a new order. |
| `price` | Price in INR |
| `old_price` | Old Price in INR. Required if mode is `MODIFY` |
| `quantity` | For `NSE_FO` segments, quantity is `lots` * `lot_size`. For all others, enter just the number of lots |
| `old_quantity` | For `NSE_FO` segments, old_quantity is `lots` * `lot_size`. For all others, enter just the number of lots. Required if mode is `MODIFY` |
