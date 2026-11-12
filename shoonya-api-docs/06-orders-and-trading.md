# Orders & Trading

> Source: https://shoonya.com/api-documentation (Orders & Trading)

## Contents

- [Place Order](#place-order)
- [Modify Order](#modify-order)
- [Cancel Order](#cancel-order)
- [Product Conversion](#product-conversion)

---

## Place Order

> Request to be POSTed to URL : /NorenWClientAPI/PlaceOrder

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| actid* | - | Login users account ID |
| exch* | NSE / NFO / BSE / MCX/CDS/NCX/BFO /BCD | Exchange (Select from 'exarr' Array provided in User Details response) |
| tsym* | - | Unique id of contract on which order to be placed. (Use the Results from Search Script to get the trading symbol & use url encoding to avoid special char error for symbols like M&M) |
| qty* | - | Order Quantity |
| prc* | - | Order Price(if prctyp = 'MKT/ SL-MKT' then the price will be '0') |
| trgprc | - | Only to be sent in case of SL-LMT / SL-MKT order. |
| dscqty | - | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |
| prd* | C / M / I / B / H | Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT / SL-LMT / SL-MKT / DS / 2L / 3L | - |
| mkt_protection | - | Market order protection percentage. Applicable only for MKT orders in BSE/BFO/BCS and MCX segments |
| ret* | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| remarks | - | Any tag by user to mark order. |
| ordersource | MOB / WEB / TT | Used to generate exchange info fields. [Optional field else it will take login access type] |
| bpprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc | - | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc | - | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| ext_remarks | - | External remarks |
| cl_ord_id | - | Cli Order Id |
| channel | - | Channel |
| usr_agent | - | User Agent |
| app_inst_id | - | App Install Id |
| amo | Yes | The message "Invalid AMO" will be displayed if the "amo" field is not sent with a "Yes" value. If amo is not required, do not send this field |
| tsym2 | - | Trading symbol of second leg, mandatory for price type 2L and 3L (use url encoding to avoid special char error for symbols like MSM) |
| trantype2 | - | Transaction type of second leg, mandatory for price type 2L and 3L |
| qty2 | - | Quantity for second leg, mandatory for price type 2L and 3L |
| prc2 | - | Price for second leg, mandatory for price type 2L and 3L |
| tsym3 | - | Trading symbol of third leg, mandatory for price type 3L (use url encoding to avoid special char error for symbols like M&M) |
| trantype3 | - | Transaction type of third leg, mandatory for price type 3L |
| qty3 | - | Quantity for third leg, mandatory for price type 3L |
| prc3 | - | Price for third leg, mandatory for price type 3L |
| instname | - | Instrument Name |
| ordersource | - | Order Source |
| channel | - | channel ("for more details ref: NSE/COMP/53164, NSE/INVG/64567, NSE/COMP/54007") |
| usr_agent | - | client user agent ("for more details ref: NSE/COMP/53164, NSE/INVG/64567, NSE/COMP/54007") |
| app_inst_id | - | client APP installed ID ("for more details ref: NSE/COMP/53164, NSE/INVG/64567, NSE/COMP/54007") |
| ipaddr | - | client IP address ("for more details ref: NSE/COMP/53164, NSE/INVG/64567, NSE/COMP/54007") |
| cau_msg | - | cautionary msg |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Place order success or failure indication. |
| request_time | - | Response received time. |
| norenordno | - | It will be present only on successful Order placement to OMS. |
| emsg | - | This will be present only if Order placement fails |

**Sample Success Response:**

```json
{
  "request_time": "10:48:03 20-05-2020",
  "stat": "Ok",
  "norenordno": "200520000000017"
}
```

**Sample Failure Response:**

```json
{
  "stat": "Not_Ok",
  "request_time": "20:40:01 19-05-2020",
  "emsg": "Error Occured : 2 \"invalid input\""
}
```

**Example:**

```bash
curl https://apitest.kambala.co.in/NorenWClientAPI/PlaceOrder -d "jData={"uid":"VIDYA", "actid":"CLIENT1", "exch":"NSE", "tsym":"ACC-EQ",
"qty":"50", "price":"1400", "prd":"H", "trantype":"B", "prctyp":"LMT", "ret":"DAY"}“
```

## Modify Order

> Request to be POSTed to URL : /NorenWClientAPI/ModifyOrder

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch* | - | Exchange |
| norenordno* | - | Noren order number, which needs to be modified |
| prctyp* | LMT / MKT / SL-MKT / SL-LMT | This can be modified. |
| prc* | - | Modified / New price (if prctyp = 'MKT/ SL-MKT' then the price will be '0') |
| qty* | - | Modified / New Quantity Quantity to Fill / Order Qty - This is the total qty to be filled for the order. Its Open Qty/Pending Qty plus Filled Shares (cumulative for the order) for the order. * Please do not send only the pending qty in this field |
| tsym* | - | Unique id of contract on which order was placed. Can't be modified, must be the same as that of original order. (use url encoding to avoid special char error for symbols like M&M) |
| ret | DAY / IOC / EOS | New Retention type of the order |
| mkt_protection |   | Market order protection percentage. Applicable only for MKT orders in BSE/BFO/BCS and MCX segments. |
| trgprc | - | New trigger price in case of SL-MKT or SL-LMT |
| dscqty | - | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |
| ext_remarks | - | External remarks |
| cl_ord_id | - | Cli Order Id |
| channel | - | Channel |
| usr_agent | - | User Agent |
| app_inst_id | - | App Install Id |
| uid* | - | User id of the logged in user. |
| bpprc | - | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc | - | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| ipaddr | - | global Ip of internet access |
| ordersource | MOB / WEB / TT | Used to generate exchange info fields. [Optional field else it will take login access type] |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Modify order success or failure indication. |
| result | - | Noren Order number of the order modified. |
| request_time | - | Response received time. |
| emsg | - | This will be present only if Order modification fails |

**Sample Success Response:**

```json
{
  "request_time": "14:14:08 26-05-2020",
  "stat": "Ok",
  "result": "200526000000103"
}
```

**Sample Failure Response:**

```json
{
  "request_time": "16:03:29 28-05-2020",
  "stat": "Not_Ok",
  "emsg": "Rejected : ORA:Order not found"
}
```

## Cancel Order

> Request to be POSTed to URL : /NorenWClientAPI/CancelOrder

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| norenordno* | - | Noren order number, which needs to be modified |
| uid* | - | User id of the logged in user. |
| ext_remarks | - | External remarks |
| cl_ord_id | - | Cli Order Id |
| channel | - | Channel |
| usr_agent | - | User Agent |
| app_inst_id | - | App Install Id |
| ordersource | - | Order Source |
| ipaddr | - | global Ip of internet access |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Cancel order success or failure indication. |
| result | - | Noren Order number of the canceled order. |
| request_time | - | Response received time. |
| emsg | - | This will be present only if Order cancelation fails |

**Sample Success Response:**

```json
{
  "request_time": "14:14:10 26-05-2020",
  "stat": "Ok",
  "result": "200526000000103"
}
```

**Sample Failure Response:**

```json
{
  "request_time": "16:01:48 28-05-2020",
  "stat": "Not_Ok",
  "emsg": "Rejected : ORA:Order not found to Cancel"
}
```

## Product Conversion

> Request to be POSTed to URL : /NorenWClientAPI/ProductConversion

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch* | - | Exchange |
| tsym* | - | Unique id of contract on which order was placed. Can’t be modified, must be the same as url encoding to avoid special char error for symbols like M&M |
| qty* | - | Quantity to be converted. |
| uid* | - | User id of the logged in user. |
| actid* | - | Account id |
| prd* | - | Product to which the user wants to convert position. |
| prevprd* | - | Original product of the position. |
| trantype* | - | Transaction type |
| postype* | Day / CF | Converting Day or Carry forward position |
| ordersource* | MOB | For Logging |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Position conversion success or failure indication. |
| emsg | - | This will be present only if Position conversion fails. |

**Sample Success Response:**

```json
{
  "request_time":"10:52:12 02-06-2020",
  "stat":"Ok"
}
```

**Sample Failure Response:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Invalid Input : Invalid Position Type"
}
```
