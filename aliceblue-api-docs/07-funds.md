> Source: https://v2api.aliceblueonline.com/Funds/

> **Note**
>
> The BASE URL, Endpoint, and Payload JSON key values are case-sensitive. Please use the format which we have given in the documentation.

# Funds

| Type | Apis | Details |
| --- | --- | --- |
| GET | {{BASE_URL}}/open-api/od/v1/limits/ | Get available funds |

## Get Limits

Get all information of your trading account like balance, margin utilised, collateral, etc.

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "tradingLimit": 0,
            "openingCashLimit": 50.0000,
            "intradayPayin": 0,
            "collateralMargin": 0,
            "creditForSell": 0,
            "adhocMargin": 0,
            "utilizedMargin": 0,
            "blockedForPayout": 0,
            "utilizedSpanMargin": 0,
            "utilizedExposureMargin": 0
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| tradingLimit | Float | Maximum limit available for trading. |
| openingCashLimit | Float | Cash available at the start of the trading day. |
| intradayPayin | Float | Funds received during the day from intraday trade settlements. |
| collateralMargin | Float | Margin available from pledged securities or collateral. |
| creditForSell | Float | Proceeds receivable from securities sold. |
| adhocMargin | Float | Extra margin added manually (usually by broker). |
| utilizedMargin | Float | Total margin used for current open positions and orders. |
| blockedForPayout | Float | Funds held back, not available for trading or withdrawal. |
| utilizedSpanMargin | Float | SPAN margin used for derivative positions. |
| utilizedExposureMargin | Float | Exposure margin utilized over and above SPAN margin. |
