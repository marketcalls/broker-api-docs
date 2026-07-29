# Portfolio — Holdings

## 1. Introduction

The Holdings API provides a detailed summary of the securities (stocks, ETFs, etc.) held in your account, including current market value, average price, quantity, and sellable quantity. Use this API to display or manage the current equity portfolio.

## 2. API Endpoint

```
GET <Base URL>/portfolio/v1/holdings
```

Replace `<Base URL>` with the relevant Kotak environment base URL provided in the response from the `/tradeApiValidate` API.

## 3. Headers

| Name | Type | Description |
| --- | --- | --- |
| accept | string | Should always be `application/json` |
| Sid | string | session sid generated on login |
| Auth | string | session token generated on login |
| neo-fin-key | string | static value: `neotradeapi` |
| Content-Type | string | Always `application/x-www-form-urlencoded` |

## 4. Request

```bash
curl -X GET "<baseUrl>/portfolio/v1/holdings" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"
```

No request body or parameters required.

## 5. Response

Example Success Response:

```json
{
  "data": [
    {
      "instrumentType": "Equity",
      "sector": "Others",
      "instrumentToken": 18974,
      "commonScripCode": "NIPPON_ETF_NIFTYIT",
      "instrumentName": "Nippon India ETF Nifty IT",
      "quantity": 45,
      "averagePrice": 38.7162,
      "holdingCost": 1742.2293,
      "closingPrice": 39.36,
      "mktValue": 1771.2,
      "scripId": "",
      "isAlternateScrip": "",
      "unrealisedGainLoss": 28.9707,
      "sqGainLoss": -5.6,
      "delGainLoss": -7.074,
      "subTotal": 0,
      "prevDayLtp": 0,
      "subType": "ETF",
      "instrumentStatus": "ACTV",
      "marketLot": 1,
      "expiryDate": "",
      "optType": "",
      "strikePrice": "0.00",
      "symbol": "ITBEES",
      "displaySymbol": "ITBEES",
      "exchangeSegment": "nse_cm",
      "series": "EQ",
      "exchangeIdentifier": "19084",
      "sellableQuantity": 45,
      "securityType": "ETF",
      "securitySubType": "ETF",
      "logoUrl": "https://www.kotaksecurities.com/stockit/stock_logos/74813.png",
      "cmotCode": "74813"
    }
  ]
}
```

### 200 Response Fields

| Field | Type | Description |
| --- | --- | --- |
| instrumentType | string | Type of instrument (e.g., Equity, Debt, ETF, Derivative). |
| sector | string | Industry/sector classification of the company/security. |
| instrumentToken | integer | Unique token ID for the instrument (used in trading/order APIs). |
| commonScripCode | string | Common identifier for the instrument across systems. |
| instrumentName | string | Full name of the instrument/security. |
| quantity | integer | Total number of units/shares held. |
| averagePrice | float | Average acquisition price per share/unit. |
| holdingCost | float | Total cost of acquisition for this holding. |
| closingPrice | float | Previous closing price from the exchange. |
| mktValue | float | Current market value of the holding (closingPrice × quantity). |
| scripId | string | Internal scrip identifier (may be blank for some securities). |
| isAlternateScrip | string | Flag indicating if this is an alternate scrip (blank if not applicable). |
| unrealisedGainLoss | float | Unrealized profit/loss based on current market value. |
| sqGainLoss | float | Square-off gain/loss (intraday MTM component, if applicable). |
| delGainLoss | float | Delivery gain/loss (applicable for deliveries). |
| subTotal | float | Additional subtotal field (value = 0 if unused). |
| prevDayLtp | float | Previous day's Last Traded Price (LTP). |
| subType | string | Subtype of instrument (e.g., ETF, EQUITY). |
| instrumentStatus | string | Status of the instrument (e.g., ACTV = Active). |
| marketLot | integer | Market lot size (minimum tradable unit). |
| expiryDate | string | Expiry date (applicable for derivatives, else blank). |
| optType | string | Option type (CE/PE for derivatives, else blank). |
| strikePrice | string | Option strike price (string format, "0.00" for non-derivatives). |
| symbol | string | Symbol code of the instrument (e.g., IDEA). |
| displaySymbol | string | Symbol displayed in UI (e.g., ITBEES). |
| exchangeSegment | string | Exchange segment (e.g., nse_cm, bse_cm). |
| series | string | Series of the instrument (e.g., EQ). |
| exchangeIdentifier | string | Exchange-provided identifier for the scrip. |
| sellableQuantity | integer | Quantity available for selling at the moment. |
| securityType | string | Type of security (e.g., EQUITY STOCK, ETF). |
| securitySubType | string | Subtype of security (e.g., EQUITY STOCK, ETF). |
| logoUrl | string | URL for the company/logo image. |
| cmotCode | string | Internal Kotak code mapped for margin/holdings tracking. |

Example Error Response:

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid session",
  "stCode": 1003
}
```

## 6. Notes

- Only securities currently held in the portfolio are reported.
- `sellableQuantity` reflects what can be sold on the current trading day.
- Fields like `instrumentToken` and `exchangeSegment` are useful for placing new orders.
- Use valid session and auth tokens to avoid authentication errors.

## 7. Response change from v1 API

This API (along with its endpoint) has undergone response field changes. If you were a user of the older API, map the new key names as needed. New fields added include `commonScripCode`, `logoUrl`, `cmotCode`, `unrealisedGainLoss`, `sqGainLoss`, `delGainLoss`, `marketLot`, `securitySubType`, `instrumentType`, `sector`, and more.

Example v1 → v2 field mapping (representative):

| Field — OLD API | Example | Field — NEW API | Example |
| --- | --- | --- | --- |
| displaySymbol | ITBEES | instrumentType | Equity |
| averagePrice | 38.7162 | sector | Others |
| quantity | 45 | instrumentToken | 18974 |
| exchangeSegment | nse_cm | commonScripCode | NIPPON_ETF_NIFTYIT |
| exchangeIdentifier | 19084 | instrumentName | Nippon India ETF Nifty IT |
| holdingCost | 1742.2293 | quantity | 45 |
| mktValue | 1771.2 | averagePrice | 38.7162 |
| scripId | | holdingCost | 1742.2293 |
| instrumentToken | 18974 | closingPrice | 39.36 |
| instrumentType | Equity | mktValue | 1771.2 |
| isAlternateScrip | false | scripId | |
| closingPrice | 39.36 | isAlternateScrip | |
| | | unrealisedGainLoss | 28.9707 |
| | | sqGainLoss | -5.6 |
| | | delGainLoss | -7.074 |
| | | subTotal | 0 |
