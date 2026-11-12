# Option Chain

- [Option Chain](#option-chain)
- [Option Chain Config](#option-chain-config)

## Option Chain

Source: https://developer.paytmmoney.com/docs/api/option-chain/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/fno/v1/option-chain?type=PUT&symbol=NIFTY&expiry=23-02-2023`  

### Description

> Using Option Chain API one can get **Option Contracts**

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | optional | Success/Error Code generated depending upon the success/failure of the API Request. |
| `message` | string | optional | Message to be displayed in the frontend |
| `displayMessage` | string | optional | Message to be displayed |
| `pml_id` | string | optional | PML unique ID |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `underlaying_scrip_code` | string | optional | Underlaying Scrip Code |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_symbol` | string | optional | PML Symbol |
| `vega` | string | optional | Vega |
| `fresh_pos` | string | optional | Fresh Position |
| `iv` | string | optional | Invest Value |
| `square_off_pos` | string | optional | Square Off Position |
| `desc` | string | optional | Description |
| `theta` | string | optional | Time Decay |
| `gamma` | string | optional | Gamma |
| `spot_price` | string | optional | Spot Price |
| `delta` | string | optional | Delta |
| `price` | string | optional | Price at which order is to be placed |
| `stk_price` | string | optional | Strike Price |
| `net_chg` | string | optional | Net Change |
| `oi` | string | optional | Cumulative Open Interest (For Futures and Option segments only) |
| `oi_per_chg` | string | optional | Open Interest per Change |
| `oi_net_chg` | string | optional | Open Interest net Change |
| `per_chg` | string | optional | Per Change |
| `traded_vol` | string | optional | Traded Volume |
| `symbol` | string | optional | Symbol for Security ID |
| `expiry_date` | string | optional | The expiry date of an option is the date at which option expires |
| `option_type` | string | optional | Option Type PE - Put Option CE - Call Option |
| `instrument` | string | optional | EQUITY(Cash)/FUTSTK/OPTSTK |
| `name` | string | optional | Custom Symbol Name |
| `tick_size` | string | optional | Minimum price change between different bid and offer prices of an asset traded on an exchange platform |
| `lot_size` | string | optional | The no of contracts in a derivative security |
| `exch_feed_time` | string | optional | Exchange Feed Time |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/fno/v1/option-chain?type=PUT&symbol=NIFTY&expiry=23-02-2023' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "meta": {
        "code": "PM_FNO_200",
        "message": "Success",
        "displayMessage": "Success"
    },
    "data": {
        "results": [
            {
                "pml_id": 5000825313,
                "exchange": "NSE",
                "underlaying_scrip_code": 26000,
                "segment": "D",
                "security_id": 58445,
                "pml_symbol": "NIFTY-Feb2023-17800-PE",
                "vega": "14.26",
                "fresh_pos": "0",
                "iv": "13.54",
                "square_off_pos": "5293",
                "desc": "NIFTY23FEB17800PE",
                "theta": "-9.64",
                "gamma": "0.0004",
                "spot_price": "17860.75",
                "delta": "-0.43",
                "price": "135.55",
                "stk_price": 17800.0,
                "net_chg": "-67.35",
                "oi": "1874500.00",
                "oi_per_chg": "0.01",
                "oi_net_chg": "100.00",
                "per_chg": "-33.19",
                "traded_vol": "90048.00",
                "symbol": "NIFTY",
                "expiry_date": "2023-02-23T00:00:00",
                "option_type": "PE",
                "instrument": "OPTIDX",
                "name": "NIFTY 23 FEB 17800 PUT",
                "tick_size": 5,
                "lot_size": 50,
                "exch_feed_time": "2023-02-08T13:44:01"
            }
        ],
        "pg_cxt": {
            "res_at": 1675844067
        }
    }
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| type  string  mandatory | Call or Put option |
| symbol  string  mandatory | Symbol |
| expiry  string  mandatory | Expiry in DD-MM-YYYY format |

---

## Option Chain Config

Source: https://developer.paytmmoney.com/docs/api/option-chain-config/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/fno/v1/option-chain/config?symbol=NIFTY`  

### Description

> Using Option Chain Config API one can get **option contracts expiry date**

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | optional | Success/Error Code generated depending upon the success/failure of the API Request. |
| `message` | string | optional | Message to be displayed in the frontend |
| `displayMessage` | string | optional | Message to be displayed |
| `exch_symbol` | string | optional | Option Contract Symbol |
| `expires` | string | optional | Expiry Dates in Epoch format |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/fno/v1/option-chain/config?symbol=NIFTY' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "meta": {
        "code": "PM_FNO_200",
        "message": "Success",
        "displayMessage": "Success"
    },
    "data": {
        "exch_symbol": "NIFTY",
        "expires": [
            1675931400000,
            1676536200000,
            1677141000000,
            1677745800000,
            1678350600000,
            1680078600000,
            1682584200000,
            1688027400000,
            1695889800000,
            1703752200000,
            1719477000000,
            1735201800000,
            1750926600000,
            1766565000000,
            1782376200000,
            1798705800000,
            1813825800000,
            1830155400000
        ]
    }
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| symbol  string  mandatory | Symbol |
