# Positions and Holdings

- [Position API](#position-api)
- [Position details API](#position-details-api)
- [Holdings Value API](#holdings-value-api)
- [User Holdings Data API](#user-holdings-data-api)

## Position API

Source: https://developer.paytmmoney.com/docs/api/position-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/position`  

### Description

> Positions contain the user's portfolio of short to medium term derivatives (futures and options contracts) and intraday equity stocks.  
> Derivative Instruments in the positions portfolio remain there until they're sold, or until expiry, which, for derivatives, is typically three months.  
> Equity positions carried overnight moves to the holdings portfolio the next day. This is useful for computing intraday profits and losses for trading strategies.  
> If any position change happens on your account Paytm Money platform will raise this event to indicate that position.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | string | optional | Unique customer identification number by PML |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `display_name` | string | optional | Custom Symbol Name |
| `tot_buy_qty` | string | optional | Total Quantity bought |
| `tot_buy_val` | string | optional | Total Value of the bought quantity |
| `buy_avg` | string | optional | Average price at which buy order got executed |
| `tot_sell_qty` | string | optional | Total Quantity sold off from the position |
| `tot_sell_val` | string | optional | Net value of the sold quantities |
| `sell_avg` | string | optional | Average price at which sell order got executed |
| `net_qty` | string | optional | Net quantity bought and sold |
| `net_val` | string | optional | Net value bought and sold |
| `net_avg` | string | optional | Net average price bought and sold |
| `last_traded_price` | string | optional | Last traded price of the security |
| `realised_profit` | string | optional | Realised Profit is mainly the capital gain or loss |
| `isin` | string | optional | The International Securities Identification Number is a code that uniquely identifies a specific security |
| `display_pos_type` | string | optional | Type of Position |
| `display_pos_status` | string | optional | Status of the Product Position |
| `display_product` | string | optional | Full name of the product |
| `tick_size` | string | optional | Minimum price change between different bid and offer prices of an asset traded on an exchange platform |
| `lot_size` | string | optional | The no of contracts in a derivative security |
| `strike_price` | string | optional | Strike Price of option at which it is to be bought/sold |
| `expiry_date` | string | optional | The expiry date of an option is the date at which option expires |
| `opt_type` | string | optional | Option Type: Call/Put |
| `instrument` | string | optional | EQUITY(Cash)/FUTSTK/OPTSTK |
| `tot_buy_qty_cf` | string | optional | Total Buy Quantity Carry Forward: Buy Quantity held previously and carried forward over night |
| `tot_sell_qty_cf` | string | optional | Total Sell Quantity Carry Forward: Sold Quantity held previously and carried forward over night |
| `tot_buy_val_cf` | string | optional | Total Buy Value Carry Forward: value of buy Quantity held previously and carried forward overnight |
| `tot_sell_val_cf` | string | optional | Total Sell Value Carry Forward: value of sold Quantity held previously and carried forward over night |
| `tot_buy_qty_day` | string | optional | Total Buy Quantity Day: Total quantities were bought during the day from the position |
| `tot_sell_qty_day` | string | optional | Total Sell Quantity Day: Total quantities were sold during the day from the position |
| `tot_buy_val_day` | string | optional | Total Buy Value Day: Value of bought quantities during the day from the position |
| `tot_sell_val_day` | string | optional | Total Sell Value Day: Value of sold quantities during the day from the position |
| `cost_price` | string | optional | Average cost price: Average price at which the net position quantity was acquired |
| `instrument_type` | string | optional | Script Type like ES= Equity Stock ETF= Exchange Traded Fund FUTIDX= Future Index FUTSTK= Future Stock OPTIDX= Option Index OPTSTK= Option Stock |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/orders/v1/position' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### None

```json
{
   "status":"success",
   "message":"",
   "data":[
      {
         "client_id":"1194654",
         "exchange":"NSE",
         "segment":"D",
         "product":"I",
         "security_id":"35000",
         "mkt_type":"NL",
         "display_name":"BANKNIFTY 15 OCT 18700 CALL",
         "tot_buy_qty":0,
         "tot_buy_val":0,
         "buy_avg":0,
         "tot_sell_qty":25,
         "tot_sell_val":50000,
         "sell_avg":2000,
         "net_qty":-25,
         "net_val":50000,
         "net_avg":2000,
         "last_traded_price":3538,
         "realised_profit":0,
         "isin":"NA",
         "display_pos_type":"S",
         "display_pos_status":"Open",
         "display_product":"Intraday",
         "tick_size":5,
         "lot_size":25,
         "strike_price":18700,
         "expiry_date":"2020-10-15",
         "opt_type":"CE",
         "instrument":"FUTSTK",
         "tot_buy_qty_cf":0,
         "tot_sell_qty_cf":0,
         "tot_buy_val_cf":0,
         "tot_sell_val_cf":0,
         "tot_buy_qty_day":0,
         "tot_sell_qty_day":25,
         "tot_buy_val_day":0,
         "tot_sell_val_day":50000,
         "cost_price":0.00000,
         "instrument_type": "ES"
      }
   ]
}
```

---

## Position details API

Source: https://developer.paytmmoney.com/docs/api/position-details-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/position-details?security_id=2885&product=V&exchange=NSE`  

### Description

> Position details API contains all the **information of users instruments** including both equity and derivatives segments.  
> Shows all available open- positions for the day and also describes the changes in the position that occurred.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `traded_quantity` | string | optional | Quantities got traded out of the ordered quantities |
| `average_traded_price` | string | optional | Average price at which security got traded |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `last_updated_time` | string | optional | Recent date and time at which order got updated |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/orders/v1/position-details?security_id=2885&product=V&exchange=NSE' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "",
"data": [
{
"traded_qty": 10,
"avg_traded_price": 718.2,
"txn_type": "B",
"last_updated_time": "2019-11-15 13:05:09"
}
]
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| security\_id  string  mandatory | security\_id of scrip in NSE / BSE |
| product  string  mandatory | Type of product are C/I/B/V/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), I=Intraday Trading. This is Valid for Segment= E/D (Equity and Derivatives both) B=Bracket order. Valid for Segment= E (Equity) V=Cover Order. Valid for Segment= E (Equity) |
| exchange  string  mandatory | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |

---

## Holdings Value API

Source: https://developer.paytmmoney.com/docs/api/holdings-value-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/holdings/v1/get-holdings-value`  

### Description

> Holdings contain the user's portfolio of long term equity delivery stocks.  
> An instrument in a holdings portfolio remains there indefinitely until its sold or is delisted or changed by the exchanges. All these stocks will reside in users DEMAT account with CDSL or NSDL.  
>   
> Holding Value API **gives Current Value and Invested Value** of Holdings or Portfolio.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cv` | string | optional | Current Value |
| `iv` | string | optional |  |
| `timestamp` | string | optional | Execution Time |
| `displayMessage` | string | optional | Message to be displayed |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/holdings/v1/get-holdings-value' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "results": [
            {
                "cv": "5745803.88",
                "iv": "4845177.13",
                "timestamp": "2021-08-09T06:36:59.280Z"
            }
        ]
    },
    "meta": {
        "displayMessage": null
    }
}
```

---

## User Holdings Data API

Source: https://developer.paytmmoney.com/docs/api/user-holdings-data-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/holdings/v1/get-user-holdings-data`  

### Description

> Holdings contain the user's portfolio of long term equity delivery stocks.  
> An instrument in a holdings portfolio remains there indefinitely until it is sold or is delisted or changed by the exchanges.  
> All these stocks will reside in users DEMAT account with CDSL or NSDL.  
>   
> User Holding Data API gives **details of all the Stocks Holding** in the Portfolio.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `nse_symbol` | string | optional | NSE Symbol |
| `nse_security_id` | string | optional | NSE Security Id |
| `bse_symbol` | string | optional | BSE Symbol |
| `bse_security_id` | string | optional | BSE Security Id |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `isin_code` | string | optional | The International Securities Identification Number is a code that uniquely identifies a specific security |
| `security_source_type` | string | optional | Security Source Type |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `utilized_quantity` | string | optional | Utilized Quantity |
| `remaining_quantity` | string | optional | Quantities yet to be traded out of the ordered quantities |
| `last_traded_price` | string | optional | Last traded price of the security |
| `row_no` | string | optional | Row Number |
| `cost_price` | string | optional | Average cost price: Average price at which the net position quantity was acquired |
| `display_name` | string | optional | Custom Symbol Name |
| `exchange_inst_name` | string | optional | Exchange Inst Name |
| `bse_pml_id` | string | optional | BSE PML Id |
| `nse_pml_id` | string | optional | NSE PML Id |
| `xirr` | string | optional | Extended Internal Rate of Return |
| `cagr` | string | optional | Compound Annual Growth Rate |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `nse_tick_size` | string | optional | NSE Tick Size |
| `bse_tick_size` | string | optional | BSE Tick Size |
| `is_quantity_mismatch` | string | optional | Is Quantity Mismatch |
| `quantity_mismatch` | string | optional | Quantity Mismatch |
| `pc` | string | optional | PC |
| `sector` | string | optional | Sector |
| `mcap_type` | string | optional | Market Capitalization Type |
| `displayMessage` | string | optional | Message to be displayed |
| `nse_series` | string | optional | EQ |
| `bse_series` | string | optional | A |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/holdings/v1/get-user-holdings-data' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "results": [
            {
                "nse_symbol": "SAIL",
                "nse_security_id": "2963",
                "bse_symbol": "SAIL",
                "bse_security_id": "500113",
                "exchange": "ALL",
                "isin_code": "INE114A01011",
                "security_source_type": "HLD",
                "quantity": "2004",
                "utilized_quantity": "0",
                "remaining_quantity": "2004",
                "last_traded_price": "137.65",
                "row_no": "0",
                "cost_price": "123.0276",
                "display_name": "Steel Authority Of India",
                "exchange_inst_name": "ES",
                "bse_pml_id": "1000003742",
                "nse_pml_id": "1000002812",
                "xirr": "0.0",
                "cagr": "0.0",
                "segment": "E",
                "nse_tick_size": "5.0",
                "bse_tick_size": "5.0",
                "is_quantity_mismatch": false,
                "quantity_mismatch": 0,
                "pc": 141.0,
                "sector": "Steel",
                "mcap_type": "Large Cap",
                "nse_series”:”EQ",
                "bse_series":"A”
            }
        ]
    },
    "meta": {
        "displayMessage": null
    }
}
```
