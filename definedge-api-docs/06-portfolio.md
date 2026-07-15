# Portfolio

All APIs require the request header:

```
Authorization: <api_session_key>
```

| Method | Relative URL | Description |
| --- | --- | --- |
| GET | `/positions` | Get position book |
| GET | `/holdings` | Get holdings |

---

## Position Book

| Particular | Details |
| --- | --- |
| API Name | Get Position book |
| Relative URL | `/positions` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API returns all Positions of the current day.

### Request message format

NA

### Position Book Response

| Field | Description |
| --- | --- |
| `message` | Shows the status message |
| `status` | Shows the status for the request |
| `positions` | Refer to the **Position Book Response Item** table below |

### Position Book Response Item

| Field | Possible values | Description |
| --- | --- | --- |
| `break_even_point` | | |
| `broker_name` | | Broker specific contract display name, present only if applicable |
| `carry_buy_amt` | | Amount for carry forward Buy amount |
| `carry_buy_avg` | | Buy average for carry forward quantity |
| `carry_buy_qty` | | Total Carry forward Buy quantity |
| `carry_sell_amt` | | Amount for carry forward Sell amount |
| `carry_sell_avg` | | Sell average for carry forward quantity |
| `carry_sell_qty` | | Total Carry forward Sell quantity |
| `cf_sell_quantity` | | |
| `day_averageprice` | | |
| `day_buy_amt` | | Amount for quantity bought today |
| `day_buy_avg` | | Average for quantity bought today |
| `day_buy_qty` | | Quantity bought today |
| `day_sell_amt` | | Amount for quantity sold today |
| `day_sell_avg` | | Average for quantity sold today |
| `day_sell_qty` | | Quantity sold today |
| `exchange` | | Exchange to which order will be placed |
| `lastPrice` | | |
| `lotsize` | | For Derivatives symbols, specifies its lot size |
| `multiplier` | | Contract price multiplier (used for order value calculation) |
| `net_averageprice` | | |
| `net_quantity` | | |
| `net_uploadprice` | | |
| `open_buy_amount` | | Indicates the Open Buy Amount |
| `open_buy_averageprice` | | Indicates the Open Buy Average Price |
| `open_buy_quantity` | | Indicates the Open Buy Quantity |
| `open_sell_amount` | | Indicates the Open Sell Amount |
| `open_sell_averageprice` | | Indicates the Open Sell Average Price |
| `open_sell_quantity` | | Indicates the Open Sell Quantity |
| `order_id` | | Shows Order ID |
| `original_average_price` | | |
| `price_factor` | | Contract price factor (GNPN)/(GDPD) |
| `price_precision` | | Indicates the price precision |
| `product_type` | CNC / INTRADAY / NORMAL | Product type |
| `realized_pnl` | | Realised Returns |
| `request_time` | | |
| `status` | | Shows the status for the request |
| `ticksize` | | Tick size for the mentioned symbol |
| `token` | | Unique token ID for each symbol |
| `total_buy_amt` | | Amount for total Buy amount |
| `total_buy_avg` | | Average for total Buy quantity |
| `total_sell_amt` | | Amount for total Sell amount |
| `total_sell_avg` | | Average for total Sell quantity |
| `tradingsymbol` | | Trading symbol as per master file |
| `unrealized_pnl` | | Unrealised Returns |
| `upload_price` | | |

### Response Message Format

```json
{
  "status": "SUCCESS",
  "positions": [
    {
      "exchange": "NFO",
      "tradingsymbol": "NIFTY23FEB23F",
      "product_type": "NORMAL",
      "token": "48757",
      "price_precision": "2",
      "lotsize": "50",
      "ticksize": "0.05",
      "multiplier": "1",
      "price_factor": "1.000000",
      "day_buy_qty": "0",
      "day_sell_qty": "50",
      "day_buy_amt": "0.00",
      "day_buy_avg": "0.00",
      "day_sell_amt": "883250.00",
      "day_sell_avg": "17665.00",
      "carry_buy_qty": "0",
      "carry_sell_qty": "0",
      "open_buy_quantity": "0",
      "open_sell_quantity": "0",
      "open_buy_amount": "0.00",
      "open_buy_averageprice": "0.00",
      "open_sell_amount": "0.00",
      "open_sell_averageprice": "0.00",
      "day_averageprice": "17665.00",
      "net_quantity": "-50",
      "net_averageprice": "17665.00",
      "upload_price": "0.00",
      "net_uploadprice": "17665.00",
      "lastPrice": "17665.00",
      "unrealized_pnl": "-0.00",
      "break_even_point": "17665.00",
      "realized_pnl": "0.00",
      "total_buy_amt": "0.00",
      "total_sell_amt": "883250.00",
      "total_sell_avg": "17665.00"
    }
  ]
}
```

---

## Holdings

| Particular | Details |
| --- | --- |
| API Name | Get Holdings |
| Relative URL | `/holdings` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API provides holdings along with their details.

### Request message format

NA

### Holding Response

| Field | Description |
| --- | --- |
| `avg_buy_price` | Average Buy price |
| `broker_collateral_qty` | Non-POA Pledged Quantity |
| `collateral_qty` | POA pledged Collateral Quantity |
| `cusa_qty` | CUSA qty |
| `dp_qty` | DP Holding Quantity |
| `haircut` | Haircut for that symbol |
| `holding_used` | Quantity placed to sell today |
| `message` | Error message |
| `non_poa_qty` | Non POA Quantity |
| `sell_amt` | Amount for quantity sold today |
| `status` | Holding request success or failure indication |
| `t1_qty` | T1 Quantity |
| `trade_qty` | Quantity Sold today |
| `tradingsymbol` | Refer to the **Holdings Response Item** table below |
| `unpledged_qty` | Unpledged quantity |

### Holdings Response Item

| Field | Description |
| --- | --- |
| `exchange` | Exchange to which order will be placed |
| `isin` | Specifies ISIN code for the given scrip, in case of Equity Scrips |
| `lotsize` | For Derivatives symbols, specifies its lot size |
| `message` | Shows the status message |
| `price_precision` | Price Precision |
| `requestTime` | |
| `ticksize` | Tick size for the mentioned symbol |
| `token` | Unique token ID for each symbol |
| `tradingsymbol` | Trading symbol as per master file |

### Response Message Format

```json
{
  "status": "SUCCESS",
  "data": [
    {
      "dp_qty": "0",
      "t1_qty": "25",
      "holding_used": "0",
      "avg_buy_price": "197.30",
      "sell_amt": "0.000000",
      "trade_qty": "0",
      "tradingsymbol": [
        {
          "exchange": "NSE",
          "tradingsymbol": "CUB-EQ",
          "token": "5701",
          "price_precision": "2",
          "ticksize": "0.05",
          "lotsize": "1",
          "isin": "INE491A01021"
        },
        {
          "exchange": "BSE",
          "tradingsymbol": "CUB",
          "token": "532210",
          "price_precision": "2",
          "ticksize": "0.05",
          "lotsize": "1",
          "isin": "INE491A01021"
        }
      ]
    },
    {
      "dp_qty": "0",
      "t1_qty": "300",
      "holding_used": "0",
      "avg_buy_price": "21.80",
      "sell_amt": "0.000000",
      "trade_qty": "0",
      "tradingsymbol": [
        {
          "exchange": "NSE",
          "tradingsymbol": "IOB-EQ",
          "token": "9348",
          "price_precision": "2",
          "ticksize": "0.05",
          "lotsize": "1",
          "isin": "INE565A01014"
        },
        {
          "exchange": "BSE",
          "tradingsymbol": "IOB",
          "token": "532388",
          "price_precision": "2",
          "ticksize": "0.05",
          "lotsize": "1",
          "isin": "INE565A01014"
        }
      ]
    }
  ]
}
```
