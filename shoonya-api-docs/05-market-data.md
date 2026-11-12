# Market Data

> Source: https://shoonya.com/api-documentation (Market Data)

## Contents

- [Get Quotes](#get-quotes)
- [Get Option Chain](#get-option-chain)

---

## Get Quotes

> Request to be POSTed to URL : /NorenWClientAPI/GetQuotes

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User id |
| exch | - | Exchange |
| token | - | Contract Token |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Watch list update success or failure indication. |
| request_time | - | It will be present only in a successful response. |
| exch | NSE, BSE, NFO ... | Exchange |
| tsym | - | Trading Symbol |
| pp | - | Price precision |
| ls | - | Lot Size |
| ti | - | Tick Size |
| mult | - | Multiplier |
| sptprc | - | Spot Price [ # ] |
| lut | - | Feed Time |
| lp | - | LTP |
| uc | - | Upper circuit limitc |
| lc | - | Lower circuit limit |
| wk52_h | - | Week52 High Price [ # ] |
| wk52_l | - | Week52 Low Price [ # ] |
| oi | - | Open Interest |
| toi | - | Total Open Interest |
| strprc | - | Strike Price |
| cname | - | Company Name |
| symname | - | Symbol Name |
| seg | - | Segment |
| exd | - | Expiry Date |
| instname | - | Intrument Name |
| optt | - | Option Type |
| isin | - | ISIN |
| prcftr_d | - | Price factor ((GN / GD) * (PN/PD)) |
| token | - | Token |
| nav | - | nav |
| o | - | Open Price |
| c | - | Close Price |
| h | - | Day High Price |
| l | - | Day Low Price |
| v | - | Volume |
| ap | - | Average trade price or VWAP for day |
| ltq | - | Last trade quantity |
| ltt | - | Last trade time |
| ltd | dd-mm-yy | Last Trade Date |
| tbq | - | Trade Buy Quantity |
| tsq | - | Trade Sell Quantity |
| bp1 | - | Best Buy Price 1 |
| sp1 | - | Best Sell Price 1 |
| bp2 | - | Best Buy Price 2 |
| sp2 | - | Best Sell Price 2 |
| bp3 | - | Best Buy Price 3 |
| sp3 | - | Best Sell Price 3 |
| bp4 | - | Best Buy Price 4 |
| sp4 | - | Best Sell Price 4 |
| bp5 | - | Best Buy Price 5 |
| sp5 | - | Best Sell Price 5 |
| bq1 | - | Best Buy Quantity 1 |
| sq1 | - | Best Sell Quantity 1 |
| bq2 | - | Best Buy Quantity 2 |
| sq2 | - | Best Sell Quantity 2 |
| bq3 | - | Best Buy Quantity 3 |
| sq3 | - | Best Sell Quantity 3 |
| bq4 | - | Best Buy Quantity 4 |
| sq4 | - | Best Sell Quantity 4 |
| bq5 | - | Best Buy Quantity 5 |
| sq5 | - | Best Sell Quantity 5 |
| bo1 | - | Best Buy Quantity 1 |
| so1 | - | Best Sell Quantity 1 |
| bo2 | - | Best Buy Quantity 2 |
| so2 | - | Best Sell Quantity 2 |
| bo3 | - | Best Buy Quantity 3 |
| so3 | - | Best Sell Quantity 3 |
| bo4 | - | Best Buy Quantity 4 |
| so4 | - | Best Sell Quantity 4 |
| bo5 | - | Best Buy Quantity 5 |
| so5 | - | Best Sell Quantity 5 |
| und_exch | - | Underlying Exch seg |
| und_tk | - | Underlying Token |
| ord_msg | - | Order Message |
| scrip_base_prc | - | Scrip Base Price |
| issuecap | - | issue capital |
| e_date | - | end date |
| cutof_all | - | Cut off All |

**Sample Success Response:**

```json
{
"request_time":"12:05:21 18-05-2021",
"stat":"Ok"
,"exch":"NSE",
"tsym":"ACC-EQ",
"cname":"ACC LIMITED",
"symname":"ACC",
"seg":"EQT",
"instname":"EQ",
"isin":"INE012A01025",
"pp":"2",
"ls":"1",
"ti":"0.05",
"mult":"1",
"uc":"2093.95",
"lc":"1713.25",
"prcftr_d":"(1 / 1 ) * (1 / 1)",
"token":"22",
"lp":"0.00",
"h":"0.00",
"l":"0.00",
"v":"0",
"ltq":"0",
"ltt":"05:30:00",
"bp1":"2000.00",
"sp1":"0.00",
"bp2":"0.00",
"sp2":"0.00",
"bp3":"0.00",
"sp3":"0.00",
"bp4":"0.00",
"sp4":"0.00",
"bp5":"0.00",
"sp5":"0.00",
"bq1":"2",
"sq1":"0",
"bq2":"0",
"sq2":"0",
"bq3":"0",
"sq3":"0",
"bq4":"0",
"sq4":"0",
"bq5":"0",
"sq5":"0",
"bo1":"2",
"so1":"0",
"bo2":"0",
"so2":"0",
"bo3":"0",
"so3":"0",
"bo4":"0",
"so4":"0",
"bo5":"0",
"So5":"0"
}
```

**Sample Failure Response:**

```json
{
"stat":"Not_Ok",
"request_time":"10:50:54 10-12-2020",
"emsg":"Error Occurred : 5 "no data""
}
```

**Example:**

```
jData={"uid":"{{USER_ID}}", "exch":"NSE", "token":"22"}
```

## Get Option Chain

> Request to be POSTed to uri : /NorenWClientAPI/GetOptionChain

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| tsym* | - | Trading symbol of any of the option or future. Option chain for that underlying will be returned. (use url encoding to avoid special char error for symbols like M&M) |
| exch* | - | Exchange (UI need to check if exchange in NFO / CDS / MCX / or any other exchange which has options, if not don't allow) |
| strprc* | - | Mid price for option chain selection |
| cnt* | - | Number of strike to return on one side of the mid price for PUT and CALL. (example cnt is 4, total 16 contracts will be returned, if cnt is 5 total 20 contract will be returned) |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| values | - | Array of json objects. (object fields given in below table) |
| emsg | - | This will be present only in case of errors. That is: 1) Invalid Input 2) Session Expired |

**Json Fields of object in values Array**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch | CDS, NFO ... | Exchange |
| tsym | - | Trading symbol of the scrip (contract) |
| token | - | Token of the scrip (contract) |
| optt | - | Option Type |
| strprc | - | Strike price |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
