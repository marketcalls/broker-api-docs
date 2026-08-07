# User Profile

> Source: https://developer.hdfcsec.com/ir-docs/docs/user_profile

## Description

This API assists in retrieving details of the logged-in users.

## EndPoint

```js
Method: POST 
`https://developer.hdfcsec.com/oapi/v3/user/profile?api_key=<api_key>`
```

> **Note:** this is the only endpoint in the documentation on the `/oapi/v3/` prefix, and the only
> read-only endpoint documented as `POST`.

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Glossary of constants

| Constant | Description |
| --- | --- |
| user_id | Unique identifier for the user. |
| user_type | Type of user, such as individual or corporate. |
| user_name | Full name of the user. |
| broker | Broker associated with the user account. |
| accountSettlementType | Account settlement classification (e.g. RETAIL). |
| exchanges | List of exchanges enabled for trading. |
| products | List of trading products available for the user. |
| order_types | List of order types available for trading. |
| depository_details | Depository account information (NSDL/CDSL, flags, etc.). |
| bank_details | Bank-related flags for the account. |

## Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v3/user/profile?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

## API Response

```js

{
    "status": "success",
    "data": [
        {
            "user_id": "123456",
            "user_type": "Normal Client",
            "user_name": "TESTING",
            "broker": "HDFC Securities InvestRight",
            "accountSettlementType": "RETAIL",
            "exchanges:NSE": [
                "FUTIDX",
                "FUTSTK",
                "EQUITY",
                "OPTIDX",
                "OPTSTK",
                "MF",
                "FUTIVX",
                "FUTCUR",
                "OPTCUR"
            ],
            "exchanges:BSE": [
                "EQUITY",
                "MF",
                "FUTIDX",
                "FUTSTK",
                "OPTSTK",
                "OPTIDX"
            ],
            "exchanges:MCX": [
                "FUTIDX",
                "OPTIDX"
            ],
            "products": [
                "COVER",
                "OVERNIGHT",
                "INTRADAY",
                "MTF",
                "DELIVERY"
            ],
            "order_types": [
                "MARKET",
                "LIMIT",
                "SL",
                "SL-M"
            ],
            "depository_details": [
                {
                    "depository_code": "12345678",
                    "depository_account_number": "12345678",
                    "depository_account_settlement_type": 0,
                    "depository": "NSDL",
                    "edis_flag": "Y",
                    "ddpi_flag": "N"
                }
            ],
            "bank_details": {
                "bank_power_of_attorney_flag": "Y"
            }
        }
    ]
}
```

> **Note:** the enabled-segment keys are literal composite strings — `"exchanges:NSE"`,
> `"exchanges:BSE"`, `"exchanges:MCX"` — not a nested `exchanges` object.
