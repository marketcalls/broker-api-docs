<!-- Source: https://ant.aliceblueonline.com/productdocumentation/Option%20Chain/ -->

# Option Chain

| Type | APIs | Details |
| --- | --- | --- |
| POST | {{BASE_URL}}/obrest/optionChain/getUnderlying | Fetches the list of available underlyings (indices or symbols) for which Option Chain data can be retrieved. |
| POST | {{BASE_URL}}/obrest/optionChain/getUnderlyingExp | Retrieves the list of available expiry dates for a given underlying symbol. |
| POST | {{BASE_URL}}/obrest/optionChain/getOptionChain | Fetches the complete Option Chain data for a specific underlying and expiry. |

## Get Underlying List

**Request Structure**

```
{ 
  "exch": "nse_fo" 
} 
```

**Input parameters**

| Field | Type | Criticality | Description |
| --- | --- | --- | --- |
| exch | String | Required | Exchange code. Possible values: • nse_fo – NSE Options • bse_fo – BSE Options • mcx_fo – MCX Options |

**Response Structure**

```
{ 
  "status": "Ok", 
  "message": "Success", 
  "result": [ 
    { 
      "list_underlying": [ 
        "NIFTY", 
        "BANKNIFTY", 
        "FINNIFTY" 
      ] 
    } 
] 
} 
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| list_underlying | String | List of underlying symbols available for Option Chain data. |

## Get Underlying Expiry

**Request Structure**

```
{  
"underlying": "NIFTY", 
"exch": "nse_fo"
}
```

**Request Parameters**

| Field | Type | Description |
| --- | --- | --- |
| underlying | String | Underlying symbol. Get the list from /getUnderlying API. |
| exch | String | Exchange code (nse_fo, bse_fo, mcx_fo). |

**Response Structure**

```
{ 
"status": "Ok", 
"message": "Success", 
"result": [ 
            { 
            "underlying": "NIFTY", 
            "underlying_expiry": [ 
                "04NOV25", 
                "11NOV25" 
                ] 
            } 
        ] 
} 
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| underlying | String | Name of the underlying. |
| underlying_expiry | String | List of expiry dates for the given underlying. |

## Get Option Chain

**Request Structure**

```
{ 
"underlying": "NIFTY", 
"expiry": "04NOV25", 
"interval": 10, 
"exch": "nse_fo"
}
```

**Input Parameters**

| Field | Type | Description |
| --- | --- | --- |
| underlying | String | Underlying symbol (e.g., NIFTY). |
| expiry | String | Expiry date from /getUnderlyingExp API. |
| interval | String | Strike price interval. Possible values: 5, 10, 15, 20, 25. |
| exch | String | Exchange code (nse_fo, bse_fo, mcx_fo). |

**Response Structure**

```
{ 
  "status": "Ok", 
  "message": "Success", 
  "result": [ 
    { 
      "data": [ 
        { 
          "CE": { 
            "forInsName": "EURUSD 26th NOV 1.1 CE", 
            "gval": "0", 
            "ltp": "0", 
            "oi": "0", 
            "pdc": "0.0775", 
            "pdoi": "0.0000", 
            "token": "4800", 
            "tradingsymbol": "EURUSD26NOV25C1.1" 
          }, 
          "PE": { 
            "forInsName": "EURUSD 26th NOV 1.1 PE", 
            "gval": "0", 
            "ltp": "0", 
            "oi": "0", 
            "pdc": "0.0028", 
            "pdoi": "0.0000", 
            "token": "4801", 
            "tradingsymbol": "EURUSD26NOV25P1.1" 
          } 
        } 
      ] 
    } 
  ] 
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| CE | String | Call option details. |
| PE | String | Put option details. |
| gval | String | Greeks or calculated value (if applicable). |
| ltp | String | Last traded price |
| oi | String | Open interest. |
| pdc | String | Previous day close. |
| pdoi | String | Previous day open interest. |
| token | String | Unique token ID for the contract. |
| tradingsymbol | String | Trading symbol for the contract. |
