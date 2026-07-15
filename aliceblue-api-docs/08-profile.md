<!-- Source: https://ant.aliceblueonline.com/productdocumentation/Profile/ -->

# Profile

| Type | Apis | Details |
| --- | --- | --- |
| GET | {{BASE_URL}}/open-api/od/v1/profile/ | To get a clientdetails |

## Profile

While a successful token exchange returns the full user profile, it's possible to retrieve it any point of time with the /user/profile API. Do note that the profile API does not return any of the tokens.

**Response Structure**

```
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "clientId": "123456",
            "clientName": "XXXXXXX",
            "isTotpEnabled": "Y",
            "isPoaProvided": "N",
            "accountStatus": "Activated",
            "exchanges": [
                "BSE",
                "BFO",
                "BCD",
                "CDS",
                "MCX",
                "NSE",
                "NFO",
                "NCOM"
            ],
            "products": [
                "LONGTERM",
                "INTRADAY",
                "MTF",
                "CO",
                "BO"
            ],
            "orderComplexity": [
                "REGULAR",
                "AMO",
                "BO",
                "CO"
            ]
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| clientId | String | Unique identifier assigned to the client. |
| clientName | String | Full name of the account holder. |
| isTotpEnabled | String | Indicates if TOTP (Time-based OTP) is enabled or not("Y" = Yes or "N" = No). |
| isPoaProvided | String | Indicates if Power of Attorney (POA) documents are submitted or not("Y" = Yes or "N" = No). |
| accountStatus | String | Current status of the trading account (e.g., Activated). |
| exchanges | String | [Code representing the exchange where the trade is executed.](../Appendix/#exchange) |
| products | String | Types of products the client can trade in (e.g., LONGTERM, INTRADAY). |
| orderComplexity | String | Supported order types the client can place (e.g., REGULAR, AMO). |
