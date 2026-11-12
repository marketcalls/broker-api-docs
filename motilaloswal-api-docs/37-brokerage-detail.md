# Brokerage Detail

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

This API is used to get Brokerage and Other Charges Detail

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getbrokeragedetail |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getbrokeragedetail |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String | N | Client ID Mandatory in case of Dealer |
| ExchangeName | String | Y | Name of the Exchange E.g. NSE,BSE,NSEFO,NSECD,MCX and Others |
| Series | String | Y | Name of ScripGroup E.g.F,O,A,EQ,BE and Others |

## Sample Request (Body)

```json
{
"clientcode":"AA020"//in case of dealer else not required
“exchangename”:”NSEFO”,
“series”:”F”
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Brokerage Detail"
"errorcode": "",
"data": [
{
“clientcode”:”EAOP2917”,
“segment”:”FO”,
“exchange” :”NSEFO”,
“scripgroup”:”F”,
“futurebrokeragevaluetype” : “PER”,
“futurebuy”:”0.0350”,
“futuresell”:”0.0350”,
“optionbrokeragevaluetype”:”LOT”,
“optionbuy”:”45.0000”,
“optionsell” :”45.0000”,
“gst” : “18.0000”,
“sebi”:”0.0001”,
“futurebuystt”:”0.0000”,
“futuresellstt” :”0.0100”,
“optionbuystt” :”0.0000”,
“optionsellstt” :”0.0500”,
“futurebuystamp”:”0.0020”,
“futuresellstamp” :”0.0000”,
“optionbuystamp” :”0.0030”,
“optionsellstamp”:”0.0000”,
“transactioncharge”:”0.0020”
}
]
}
```

## Example Two

## Sample Request (Body)

```json
{
"clientcode":"AA020"//in case of dealer else not required
“exchangename”:”NSE”,
“series”:”A”
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Brokerage Detail"
"errorcode": "",
"data": [
{
“clientcode”:”EAOP2917”,
“segment”:”EQ”,
“exchange” :”NSE”,
“scripgroup”:”A”,
“tradingbuy”:”0.0350”,
“tradingsell”:”0.0350”,
“deliverybuy”:”0.0350”,
“deliverysell” :”0.0350”,
“gst” : “18.0000”,
“sebi”:”0.0001”,
“intrabuystt”:”0.0000”,
“intrasellstt” :”0.0250”,
“delbuystt” :”0.1000”,
“delsellstt” :”0.1000”,
“intrabuystamp”:”0.0030”,
“intrasellstamp” :”0.0000”,
“delbuystamp” :”0.0150”,
“delsellstamp”:”0.0000”,
“transactioncharge”:”0.0028”
}
]
}
```
