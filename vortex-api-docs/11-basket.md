<!-- Source: https://vortex.rupeezy.in/docs/2.2/basket/ -->

# Basket

Use the below apis to place and manage baskets:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/basket](#fetching-baskets) | Fetch all the baskets | 10/sec |
| `POST` | [{{base_url}}/basket](#creating-a-basket) | Create a basket | 10/sec |
| `PUT` | [{{base_url}}/basket/{basket_id}](#modifying-a-basket) | Modify basket | 10/sec |
| `DELETE` | [{{base_url}}/basket/{basket_id}](#delete-a-basket) | Delete a basket | 10/sec |

## Fetching Baskets

```
Endpoint: {{base_url}}/basket
```

### Baskets Response

```
{
    "status": "success",
    "message": "",
    "response": [
        {
            "id": 1,
            "clientCode": "DEMOUSER",
            "basketName": "Test Basket",
            "basketOrders": [
                {
                    "id": 1,
                    "orderPosition": 0,
                    "token": 2885,
                    "marketSegmentId": 1,
                    "stockData": {
                        "scripToken": 2885,
                        "marketSegmentId": 1,
                        "symbol": "RELIANCE",
                        "securityDesc": "RELIANCE INDUSTRIES LTD",
                        "instrumentName": "EQUITIES",
                        "series": "EQ",
                        "eligibility": 1,
                        "lotSize": 1,
                        "tick": 10,
                        "industry": "Refineries",
                        "sectorName": "Energy",
                        "hasOptionChain": true,
                        "isinCode": "INE002A01018",
                        "has_icon": true
                    },
                    "buySell": 1,
                    "productType": "3",
                    "orderType": "2",
                    "quantity": 1,
                    "price": 1450.8,
                    "disclosedQuantity": 0,
                    "validity": "1",
                    "validityDays": 0,
                    "isAmo": false,
                    "orderIdentifier": "",
                    "orderId": "",
                    "triggerPrice": 0,
                    "createdAt": "2025-06-24T11:45:41.879769Z",
                    "updatedAt": "2025-06-24T11:45:41.879769Z",
                    "tag_ids": [],
                    "metadata": {}
                }
            ],
            "ordersCount": 1,
            "createdAt": "2025-06-24T11:45:12.917014Z",
            "updatedAt": "2025-06-24T11:45:41.879431Z",
            "lastExecutedAt": "0001-01-01T00:00:00Z",
            "alertId": null,
            "alert": null,
            "isExecuted": false,
            "tag_ids": []
        },
        {
            "id": 1,
            "clientCode": "DEMOUSER",
            "basketName": "My First Basket",
            "basketOrders": [],
            "ordersCount": 0,
            "createdAt": "2024-12-18T09:26:09.2368Z",
            "updatedAt": "2024-12-18T09:26:09.2368Z",
            "lastExecutedAt": "0001-01-01T00:00:00Z",
            "alertId": null,
            "alert": null,
            "isExecuted": false,
            "tag_ids": null
        }
    ]
}
```

## Creating a Basket

```
Endpoint: {{base_url}}/basket
```

### Create a basket

```
{
    "name": "First basket"
}
```

| field | Required | description |
| --- | --- | --- |
| name | Y | Name of the basket to create |

### Create Basket Response

#### Success

```
{
    "alert": null,
    "alertId": null,
    "basketName": "Test basket",
    "basketOrders": [],
    "clientCode": "DEMOUSER",
    "createdAt": "2025-06-24T11:39:31.211867781Z",
    "id": 1,
    "isExecuted": false,
    "lastExecutedAt": "0001-01-01T00:00:00Z",
    "ordersCount": 0,
    "tag_ids": null,
    "updatedAt": "2025-06-24T11:39:31.211867781Z"
}
```

#### Error

```
{
    "status": "error",
    "message": "invalid parameters",
    "response": ""
}
```

| field | description |
| --- | --- |
| alert | Alert object used as trigger for the basket. To attach a trigger condition refer alert docs [here](10-alerts.md#create-an-alert) |
| alertId | ID of the trigger alert placed on the basket. |
| basketName | Name of the basket created. |
| basketOrders | Array of orders associated with the basket. |
| clientCode | Client code of the user creating the basket. |
| createdAt | Time of creation of the basket. |
| id | ID of the basket created. This basket id can be used to identify basket in list of baskets. |
| isExecuted | Flag to indicate basket execution status. |
| lastExecutedAt | Time of last execution. |
| ordersCount | Count of orders associated with basket. |
| tag_ids | Array of tag ids associated with basket if any. |
| updatedAt | Last updated at time. |

## Modifying a Basket

```
Endpoint: {{base_url}}/basket/{basket_id}
```

### Modify Basket

```
{
    "basketName": "Test Basket",
    "orders": [
        {
            "buySell": 1,
            "disclosedQuantity": 0,
            "isAmo": false,
            "marketSegmentId": 1,
            "orderId": "",
            "orderIdentifier": "Your identifier",
            "orderType": "2",
            "price": 1450.8,
            "productType": "3",
            "quantity": 1,
            "tag_ids": [],
            "token": 2885,
            "triggerPrice": 0,
            "validity": "1",
            "validityDays": 0
        },
        {
            "buySell": 1,
            "disclosedQuantity": 0,
            "isAmo": false,
            "marketSegmentId": 1,
            "orderId": "",
            "orderIdentifier": "Your identifier",
            "orderType": "1",
            "price": 1609.9,
            "productType": "2",
            "quantity": 1,
            "tag_ids": [],
            "token": 1594,
            "triggerPrice": 0,
            "validity": "1",
            "validityDays": 0
        }
    ],
    "tag_ids": []
}
```

| field | Required | description |
| --- | --- | --- |
| basketName |  | To keep the same name, pass the existing one; to update it, pass a new name. |
| orders | Y | Array of orders place in the basket. Maximum 10 orders can be created in a basket. You can refer to placing orders section [here](07-regular-order.md#placing-an-order) |
| orders.buySell | Y | Possible values: [1,2]. 1 indicates Buy and 2 indicates Sell. |
| orders.disclosedQuantity | Y | Can be any number lesser than or equal to quantity, including 0 |
| orders.isAmo | Y | Possible values: [true,false]. Should be set to true if order is being placed after market hours |
| orders.marketSegmentId | Y | Market segment id value of the exchange. Possible values: [1, 2, 13 or 5] |
| orders.orderId | O | In case of executed order you can send order id else can leave empty. |
| orders.orderIdentifier | O | This is any value that you want to associate with this order for your reference. It does not need to be unique. Max length 50. |
| orders.orderType | Y | Possible values: [1,2]. 1 indicates `RL` and 2 indicated `RL-MKT` order limit type. |
| orders.price | Y | Price should be an integer multiple of Tick Size. For example, IDEA's tick size is 0.05. So the price entered can be 9.5 or 9.65. It cannot be 9.67. In case of market orders, you should send the Last Trade Price as 0. |
| orders.productType | Y | Possible values: [1 , 2 , 3]. 1 indicates INTRADAY, 2 indicates MTF and 3 indicates DELIVERY. MTF product can only be used in NSE_EQ exchange. |
| orders.quantity | Y | For exchange NSE_FO, if you want to trade in 2 lots and lot size is 50, you should pass 100. In all other exchanges, you should pass just the number of lots. For example, in MCX_FO, if you want to trade 5 lots, you should pass just 5. |
| orders.tag_ids | O | Array of tag ids associated with order if any. |
| orders.token | Y | Security token of the scrip. It can be found in the scripmaster file. |
| orders.triggerPrice | O | To be used for Stop loss orders. For BUY side SL orders, trigger_price should be lesser than price. for SELL side SL orders, trigger_price should be greater than price. |
| orders.validity | Y | Can be **DAY** for orders which are valid throughout the day, or **IOC**. IOC order will be cancelled if it is not traded immediately. |
| orders.validityDays | Y | Can be any number lesser than or equal to quantity, including 0. |
| tag_ids | O | Array of tag ids associated with basket if any. |

### Modify Basket Response

#### Success

```
{
    "status": "success",
    "message": "Successfully Updated Basket.",
    "response": {
        "alert": null,
        "alertId": null,
        "basketName": "Second Basket",
        "basketOrders": [
            {
                "buySell": 1,
                "createdAt": "2025-06-24T11:45:41.879769Z",
                "disclosedQuantity": 0,
                "id": 1641916,
                "isAmo": false,
                "marketSegmentId": 1,
                "metadata": {},
                "orderId": "",
                "orderIdentifier": "",
                "orderPosition": 0,
                "orderType": "2",
                "price": 1450.8,
                "productType": "3",
                "quantity": 1,
                "stockData": {
                    "eligibility": 1,
                    "hasOptionChain": true,
                    "has_icon": true,
                    "industry": "Refineries",
                    "instrumentName": "EQUITIES",
                    "isinCode": "INE002A01018",
                    "lotSize": 1,
                    "marketSegmentId": 1,
                    "scripToken": 2885,
                    "sectorName": "Energy",
                    "securityDesc": "RELIANCE INDUSTRIES LTD",
                    "series": "EQ",
                    "symbol": "RELIANCE",
                    "tick": 10
                },
                "tag_ids": [],
                "token": 2885,
                "triggerPrice": 0,
                "updatedAt": "2025-06-24T11:45:41.879769Z",
                "validity": "1",
                "validityDays": 0
            }
        ],
        "clientCode": "DEMOUSER",
        "createdAt": "2025-06-24T11:45:12.917014Z",
        "id": 131434,
        "isExecuted": false,
        "lastExecutedAt": "0001-01-01T00:00:00Z",
        "ordersCount": 1,
        "tag_ids": [],
        "updatedAt": "2025-06-24T11:45:41.879431Z"
    }
}
```

#### Error

```
{
    "status": "error",
    "message": "Basket not found",
    "response": ""
}
```

## Delete a Basket

```
Endpoint: {{base_url}}/basket/{basket_id}
```

### Delete Basket Response

```
{
    "message": "",
    "response": "Successfully Deleted Basket",
    "status": "success"
}
```
