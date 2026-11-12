# Position Conversion

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Portfolio

As long as an order is open or pending in the system, it can be cancelled.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/trans/v2/positionconversion |
| Test URL | https://openapi.motilaloswaluat.com/rest/trans/v2/positionconversion |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |
| exchange | String(10) | Y | Name of the Exchange |
| scripcode | Number | Y | Scrip code or Symbol Token is unique identifier |
| quantity | Number | Y | Quantity for position conversion |
| oldproduct | String(15) | Y | Type of Old Product |
| newproduct | String(15) | Y | Type of new Product |

## Sample Request (Body)

```json
{
"clientcode":"KAL005", // in case of dealer else not required
"exchange":"NSE",
"scripcode":1660,
"quantity":100,
"oldproduct":"Normal",
"newproduct":"ValuePlus"
}
```

## Sample Response (Success)

```json
{
"status": "SUCCESS",
"message": "Position Conversion Request Sent Successfully",
"errorcode": ""
}
```

## Sample Response (Failure)

```json
{
"status": "ERROR",
"message": "Invalid Product Type Parameter",",
"errorcode": "MO1057"
}
```

This API is used to get Position Detail for a clientcode.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/book/v4/getpositiondetail |
| Test URL | https://openapi.motilaloswaluat.com/rest/book/v4/getpositiondetail |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Sample Request (Body)

```json
{
"clientcode":"AA020" // In case of dealer only
}
```

## Sample Response (Success)

```json
{
"status": "SUCCESS",
"message": "Position Data in Detail",
"errorcode": "",
"data": [
{
"clientcode": "AA020",
"transactiondate": "23-Jun-2023",
"exchange": "NSECD",
"symbol": "USDINR 29-Aug-2023 PE 81",
"expirydate": "29-Aug-2023",
"strikeprice": 81,
"optiontype": "PE",
"symboltoken": 13330,
"openquantity": -2000,
"openprice": 0.05
},
{
"clientcode": "AA020",
"transactiondate": "04-Jul-2023",
"exchange": "NSECD",
"symbol": "USDINR 27-Dec-2023 PE 82",
"expirydate": "27-Dec-2023",
"strikeprice": 82,
"optiontype": "PE",
"symboltoken": 12302,
"openquantity": -5000,
"openprice": 0.44
}
]
}
```
