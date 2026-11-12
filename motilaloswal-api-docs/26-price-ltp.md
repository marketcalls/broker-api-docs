# Price/LTP

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Limit/Margin

This API is used to get market data

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getltpdata |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getltpdata |
| Request | None or JSON (in case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |
| exchange | String(10) | Y | Name of the Exchange |
| scripcode | Number | Y | Scrip code or Symbol Token is unique identifier |

## Sample Request (Body)

```json
{
"clientcode":"AA020", // In case of dealer else not required
"exchange":"BSE",
"scripcode":500317
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "LTP DATA",
"errorcode": "",
"data": {
"exchange": "BSE",
"scripcode": 500317,
"open": 3131,
"high": 3249,
"low": 3131,
"close": 3189,
"ltp": 3224,
"volume": 7017,
"ask": 3239,
"bid": 3230
}
}
```

Note : The values of open, high, low, close and ltp are in paisa
