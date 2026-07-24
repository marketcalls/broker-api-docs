# PNL Data

> Source: https://developer.hdfcsky.com/sky-docs/docs/PNL_Data

This API is used to fetch PNL Data.

## HTTP Request

```js
     Method: POST
     Endpoint: /oapi/v1/reports/pnl
```

## Headers

```json
{
    "Authorization": "<access_token>",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

## Data Body

```js
 {
  "tradingAccountDetails": {
        "accountSettlementType": 0
    },
    "portfolioProfitLossDetails": {
        "portfolioName": "DEFAULT",
        "userOwner": 1,
        "assetClass": "Asset Class eg 99",
        "product": "Product Type eg. 99",
        "reportType": "Type of Report eg 1",
        "chargesType": "N",
        "initialType": "Y",
        "fromDate": "From Date of Data",
        "toDate": "End Date of Data"
    },
    "send_mail": true
}
```

## Request Curl to fetch all PNL Reports

```js
 curl --location --request POST 'https://uat-developer.hdfcsky.com/oapi/v1/reports/pnl?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--data '{
    "tradingAccountDetails": {
        "accountSettlementType": 0
    },
    "portfolioProfitLossDetails": {
        "portfolioName": "DEFAULT",
        "userOwner": 1,
        "assetClass": 99,
        "product": 99,
        "reportType": 1,
        "chargesType": "N",
        "initialType": "Y",
        "fromDate": "06052025",
        "toDate": "13052025"
    },
    "send_mail": true
}'
```

## Response for all PNL Reports

```js
{
    "status": "queued",
    "message": "",
    "reportId": "6d872b1e-4817-472a-9a44-10ebfa22cd79",
    "data": null,
    "errorMessage": ""
}
```

## Poll Request Curl to Fetch Report ID wise (5 Seconds)

```js
curl --location --request POST 'https://uat-developer.hdfcsky.com/oapi/v1/reports/pnl?api_key=api_key&reportId=reportId' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--data '{
    "tradingAccountDetails": {
        "accountSettlementType": 0
    },
    "portfolioProfitLossDetails": {
        "portfolioName": "DEFAULT",
        "userOwner": 1,
        "assetClass": 99,
        "product": 99,
        "reportType": 1,
        "chargesType": "N",
        "initialType": "Y",
        "fromDate": "06052025",
        "toDate": "13052025"
    },
    "send_mail": true
}'
```

## Polling response for report fetched according to ID

```json
{
  "status": "success",
  "message": "Profit and Loss InterestRate Report Fetched",
  "reportId": "c5baea4d-3fc9-490f-a700-8e9cfbbc5e28",
  "data": {
    "responseCode": 0,
    "result": {
      "profitLossDetailsList": [
        {
          "tradeableFlag": "Y",
          "exchangeIdentity": {
            "exchangeId": "NA",
            "exchangeIdType": 2
          },
          "instrumentIdentity": {
            "assetClass": 1,
            "instrumentType": 1,
            "instrumentIdType": 42,
            "instrumentId": "ALSTONE",
            "isin": "INE184S01024"
          },
          "subAsset": "EQ",
          "transactionType": "NORMAL",
          "underlyingSymbol": "NA",
          "companyName": "ALSTONE TEXTILES (INDIA) LIMITED",
          "sectorName": "TRADING",
          "uniqueCode": "SHALINIEQ",
          "expiryDate": "",
          "optionType": 0,
          "strikePrice": 0,
          "buyValue": 0.67,
          "sellValue": 0.49,
          "profitLoss": -0.18,
          "dividendInterest": 0,
          "totalProfitLoss": -0.18,
          "quantity": 1,
          "buyDate": "20250214",
          "buyQuantity": 1,
          "sellDate": "20250507",
          "sellQuantity": 1,
          "securitiesTransactionTax": 0,
          "otherIncome": 0,
          "category": "NA",
          "subCategory": "NA"
        }

      ]
    }
  },
  "errorMessage": ""
}
```
