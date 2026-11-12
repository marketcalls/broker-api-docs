<!-- Source: https://vortex.rupeezy.in/docs/2.2/alerts/ -->

# Alerts

Use the below apis to place and manage alerts:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/alerts](#fetching-alerts) | Fetch list of alerts | 10/sec |
| `POST` | [{{base_url}}/alerts](#create-an-alert) | Create an alert | 10/sec |
| `PUT` | [{{base_url}}/alerts/{alert_id}](#modifying-an-alert) | Modify alert | 10/sec |
| `DELETE` | [{{base_url}}/alerts/{alert_id}](#cancel-an-alert) | Cancel an alert | 10/sec |

## Fetching Alerts

```
Endpoint: {{base_url}}/alerts
```

### Alert list Response

```
{
    "status": "success",
    "message": "",
    "data": [
        {
            "DeletedAt": null,
            "clientCode": "DEMOUSER",
            "condition": "LE",
            "createdAt": "2025-04-08T03:43:14.953422Z",
            "expiry": "2026-04-08T03:43:14.952617Z",
            "id": 1,
            "isExecuted": false,
            "lastExecutedAt": "2025-04-15T04:38:28.149247Z",
            "marketSegmentId": 1,
            "name": "Your alert name",
            "note": "",
            "property": "LTP",
            "source": "user_alert",
            "status": "",
            "stock_data": {
                "eligibility": 1,
                "hasOptionChain": false,
                "has_icon": true,
                "industry": "Electric Equipment - Gensets / Turbines",
                "instrumentName": "EQUITIES",
                "isinCode": "INE040H01021",
                "lotSize": 1,
                "marketSegmentId": 1,
                "scripToken": 12018,
                "sectorName": "CDGS (Consumer Discretionary Goods And Services)",
                "securityDesc": "SUZLON ENERGY LIMITED",
                "series": "EQ",
                "symbol": "SUZLON",
                "tick": 1
            },
            "token": 12018,
            "triggerValue": 55.44,
            "updatedAt": "2025-06-26T06:38:08.558656Z"
        }
    ]
}
```

## Create an Alert

```
Endpoint: {{base_url}}/alerts
```

### Create Alert Object

```
{
    "basketId": null,
    "condition": "LE",
    "marketSegmentId": 1,
    "name": "Test Alert",
    "note": "",
    "property": "AVGPRICE",
    "token": 12018,
    "triggerValue": 64
}
```

| field | Required | description |
| --- | --- | --- |
| basketId | O | The basket of orders that will be placed automatically when the alert condition is met. Refer basket docs [here](11-basket.md#creating-a-basket). Please create a basket before attaching alert. |
| condition | Y | Possible value: [`LE`,`GE`]. `LE` indicates less than equsl to and `GE` indicates greater than equal to. |
| marketSegmentId | Y | Market segment id value of the exchange. Possible values: [1, 2, 13 or 5] |
| name | Y | Name of the alert. |
| note | O | Note to be attached to the alert. |
| property | Y | Property of the scrip that has to be used for the alert. Possible values: [`LTP`,`AVGPRICE`,`VOLUME`]. `LTP` uses the last trade price, `AVGPRICE` uses the average trade price and `VOLUME` uses the volume. |
| token | Y | Security token of the scrip. It can be found in the scripmaster file. |
| triggerValue | Y | The trigger value is used to calculate the condition specified. |

### Create Alert Response

#### Success

```
{
    "status": "success",
    "message": "",
    "data": {
        "alertId": 628065
    },
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
| data | Contains alert id of the alert created. This alert id can be used to identify/modify alert in list of alerts |

## Modifying an Alert

```
Endpoint: {{base_url}}/alerts/{alert_id}
```

### Modify Alert Object

```
{
    "basketId": 131434,
    "condition": "LE",
    "marketSegmentId": 1,
    "name": "suzlon ",
    "note": "suzlon ",
    "property": "LTP",
    "token": 12018,
    "triggerValue": 55.44
}
```

| field | Required | description |
| --- | --- | --- |
| basketId | O | The basket of orders that will be placed automatically when the alert condition is met. Refer basket docs [here](11-basket.md#creating-a-basket). Please create a basket before attaching alert. |
| condition | Y | Possible value: [`LE`,`GE`]. `LE` indicates less than equsl to and `GE` indicates greater than equal to. |
| marketSegmentId | Y | Market segment id value of the exchange. Possible values: [1, 2, 13 or 5] |
| name | Y | Name of the alert. |
| note | O | Note to be attached to the alert. |
| property | Y | Property of the scrip that has to be used for the alert. Possible values: [`LTP`,`AVGPRICE`,`VOLUME`]. `LTP` uses the last trade price, `AVGPRICE` uses the average trade price and `VOLUME` uses the volume. |
| token | Y | Security token of the scrip. It can be found in the scripmaster file. |
| triggerValue | Y | The trigger value is used to calculate the condition specified. |

### Modify Alert Response

```
{
    "message": "",
    "response": "Successfully Updated Alerts",
    "status": "success"
}
```

## Cancel an Alert

```
Endpoint: {{base_url}}/alerts/{alert_id}
```

### Cancel Alert Response

```
{
    "message": "",
    "response": "Successfully deleted alert",
    "status": "success"
}
```
