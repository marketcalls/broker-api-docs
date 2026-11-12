# Cancel Order

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Orders

As long as an order is open or pending in the system, it can be cancelled.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/trans/v2/cancelorder |
| Test URL | https://openapi.motilaloswaluat.com/rest/trans/v2/cancelorder |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |
| uniqueorderid | String(50) | Y | Unique Order ID as received in Order Entry Response |

## Sample Request (Body)

```json
{
"clientcode":"", // Client code required only in case of Dealer
"uniqueorderid":"1101823KAL005"
}
```

## Sample Response (Success)

```json
{
"status": "SUCCESS",
"message": "Cancel Order Request Sent",
"errorcode": ""
}
```

## Sample Response (Failure)

```json
{
"status": "ERROR",
"message": "Invalid Order Id Input Parameter",
"errorcode": "MO1060"
}
```
