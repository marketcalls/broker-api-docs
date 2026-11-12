# Edis

- [eDIS - Authorisation Status API](#edis---authorisation-status-api)
- [eDIS - Generate Tpin](#edis---generate-tpin)
- [eDIS - Validate Tpin](#edis---validate-tpin)

## eDIS - Authorisation Status API

Source: https://developer.paytmmoney.com/docs/api/edis-authorisation-status-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/edis/v1/status?edis_request_id=10131`  

### Description

> You can see if a stock is approved and ready to sell by looking at its status.  
> The stock's ISIN must be entered by the user.  
> An ISIN (International Securities Identification Number) is a 12-digit alphanumeric identifier that identifies a particular security.  
> In response to the holdings API, you can get the ISIN of portfolio equities.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `displayMessage` | string | optional | Describes the authorisation confirmation |
| `edis_request_id` | string | optional | Edis Transaction Request Id |
| `trading_date` | string | optional | Date of the trade |
| `isin` | string | optional | The International Securities Identification Number is a code that uniquely identifies a specific security |
| `status` | string | optional | Boolean value |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/edis/v1/status?edis_request_id=10131' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "meta": {
        "displayMessage": "eDIS authorisation confirmation has been received from CDSL"
    },
    "data": {
        "edis_request_id": 10131,
        "trading_date": "2021-11-24",
        "isin_list": [
            {
                "isin": "INE002A01018",
                "status": true
            },
            {
                "isin": "INE016A01026",
                "status": true
            }
        ]
    }
}
```

---

## eDIS - Generate Tpin

Source: https://developer.paytmmoney.com/docs/api/edis-generate-tpin/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/edis/v1/generate/tpin`  

### Description

> When executing sell transactions on equity holdings, where shares have to be debited from a user's demat account, required an electronic authorisation at the depository from the user, to debit shares and settle the transactions.  
>   
> To sell holding stocks, one needs to complete the CDSL eDIS flow, generate T-PIN & mark stock to complete the sell action  
>   
> Users have to Authenticate Sell orders through Tpin and OTP sent on registered mobile number. Users may Authenticate required number quantities or Multiple stocks which they want to sell from the holdings.  
> If users e-DIS authenticate after 5.30 pm then authorization will be accepted for the next trading day Holding Sell transaction.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `displayMessage` | string | optional | Message to be displayed |
| `data` | string | optional | Always empty |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/edis/v1/generate/tpin' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "meta": {
        "displayMessage": "TPIN is shared on your registered mobile number and email address. It takes 6 minutes for TPIN to get activated. Please wait for 6 minutes and then proceed."
    },
    "data": {}
}
```

---

## eDIS - Validate Tpin

Source: https://developer.paytmmoney.com/docs/api/edis-validate-tpin/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/edis/v2/validate/tpin`  

### Description

> This API checks the Tpin entered by the user, and redirects him to the depository page if it is a valid T-pin.  
> Users have to enter OTP to complete the authorization which they get on Mobile and email.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trade_type` | string | optional | PRE |
| `isin` | string | optional | The International Securities Identification Number is a code that uniquely identifies a specific security |
| `qty` | string | optional | Quantity |
| `product` | string | mandatory | Product type (e.g., C for Cash & Carry, F for Margin Trading Funding). |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `displayMessage` | string | optional | Describes the validation of TPIN |
| `DPId` | string | optional | "10200" |
| `ReqId` | string | optional | Edis Transaction Request Id |
| `Version` | string | optional | "1.1” |
| `TransDtls` | string | optional | - |
| `redirection_url` | string | optional | Redirecting URL |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/edis/v2/validate/tpin' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
–header ‘Cookie:dev-id=2f89587e-0960-457c-b157-91db8df443f8’\
--data-raw '{
    "trade_type": "PRE",
    "isin_list":
     [  {
            "isin": "INE405Y01013",
            "qty": 2,
            "product":"C"
        },
        {
            "isin": "INE421A01028",
            "qty": 3,
            "product":"C"
        }
    ]
}'
```

### Sample Responses

#### SUCCESS

```json
{
    "meta": {
        "displayMessage": "Validate Bulk TPIN response success"
    },
    "data": {
        "param": {
            "DPId": "10200",
            "ReqId": “16204829",
            "Version": "1.1",
            "TransDtls": "wMugPMJ9MV3G4QuplKKrCZoj0qmZdbMeo/muuGTn6/F4LfgFqKdHYsk1QrEV1hNT5Qqs9I68XwX2XaRHTVtjIKcB0Rm44JP4d8IRYkLi4W6rR7F/5hG63kiHOn8R9z385go1yaT8w5iLLyHQscvPo6/20GJABKcwUL0e515eVI7jBazzvX+bFCfxpDEsxE14G8+glAag8cDBdhCI5v3GWa1omEhfogVM/dRqmZiT/QE2fytQ/jYWbOm7OdJJ/w4XgYr6AqE8Atob/GiMiU0fF+Hft1VK+0bVNQjHwewMvwbuWghwHi5SG2pP9+gHD53ZA2L3O5ln/yc2orqoP01QgMfMdec1vTlAwXEDV+WowngFalyxvWTL8Eov/rALCuMKSwnGvKQFIAXVdSaFr7sPi7TGWirMh4YYKisMcfFFC3NcArASu+gJK2MvHhzUpE73rsfqPl7AMfjOWa48Z1auEQgv3H6iong9xpya0606dohmpyY5TX7ObcPtT0fe8ew8b75p6RITw94I7V/5ULtP7A==”
        },
        "redirection_url": "http://mockedis.cdslindia.com/EDIS/VerifyDIS"
    }
}
```
