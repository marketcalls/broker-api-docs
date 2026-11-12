# Modify Order

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Orders

As long as an order is open or pending in the system, certain attributes of it may be modified.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/trans/v5/modifyorder |
| Test URL | https://openapi.motilaloswaluat.com/rest/trans/v5/modifyorder |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |
| uniqueorderid | String(50) | Y | Unique Order ID as received in Order Entry Response |
| newordertype | String(10) | Y | Order Type(LIMIT, MARKET, STOPLOSS) |
| neworderduration | String(10) | Y | Order duration (DAY,GTC,GTD,IOC) |
| newprice | Decimal(15,4) | Y | Price in Rupees. Up to 4 decimal places. |
| newtriggerprice | Decimal(15,4) | N | Price in Rupees. Up to 4 decimal places. |
| newquantityinlot | Number | Y | Quantity to transact in terms of lot |
| newdisclosedquantity | Number | N | Quantity to disclose (for equity) |
| newgoodtilldate | String(11) | N | DD-MMM-YYYY |
| lastmodifiedtime | String(20) | Y | dd-MMM-yyyy HH:mm:ss |
| qtytradedtoday | Number | Y | Number of quantity traded today |

## Sample Request (Body)

```json
{
"clientcode":"", // Client code required only in case of Dealer
"uniqueorderid ":"1101823KAL005",
"newordertype":"LIMIT",
"neworderduration":"DAY",
" newquantityinlot ":100,
"newdisclosedquantity":0,
"newprice":235.50,
"newtriggerprice":0,
"newgoodtilldate":"",
"lastmodifiedtime": "14-May-2022 11:31:25",
"qtytradedtoday": 0
}
```

## Sample Response (Success)

```json
{
“status": "SUCCESS",
"message": "Modify Order Request Sent Successfully",
"errorcode": ""
}
```

## Sample Response (Failure)

```json
{
“status": "ERROR",
"message": "Invalid Order Duration Parameter",
"errorcode": "MO1054"
}
```
