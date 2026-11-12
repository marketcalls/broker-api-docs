<!-- Source: https://vortex.rupeezy.in/docs/2.2/positions/ -->

# Positions

Use the below apis to see and manage positions:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/trading/portfolio/positions](#fetch-all-positions) | Fetch all positions | 10/sec |
| `PUT` | [{{base_url}}/trading/portfolio/positions](#convert-position) | Convert Position | 10/sec |

## Fetch All Positions

Positions returns the open and closed outstanding positions carried forward from the previous days and scrips that are traded today. In the below sections we explain what the position api returns and how to use them to calculate different type of [gains](#calculating-gains)

### Sample Response

```
{
   "status": "success",
   "data": {
       "net": [
           {
               "ticker": "NSE:ITC",
               "exchange": "NSE_EQ",
               "symbol": "ITC",
               "expiry_date": "",
               "option_type": "",
               "token": 1660,
               "product": "MTF",
               "quantity": 2,
               "overnight_buy_value": 380.00,
               "overnight_sell_value": 0.00,
               "overnight_average_price": 190.00,
               "lot_size": 1,
               "multiplier": 1.00,
               "average_price": 357.30,
               "value": -714.60,
               "buy_value": 714.60,
               "sell_value": 0.00,
               "buy_quantity": 2,
               "sell_quantity": 0,
               "buy_price": 357.30,
               "sell_price": 0.00,
           },
       ],
       "day": [
           {
               "ticker": "NSE:ITC",
               "exchange": "NSE_EQ",
               "symbol": "ITC",
               "expiry_date": "",
               "option_type": "",
               "token": 1660,
               "product": "MTF",
               "quantity": 1,
               "overnight_buy_value": 0.00,
               "overnight_sell_value": 0.00,
               "overnight_average_price": 0.00,
               "lot_size": 1,
               "multiplier": 1.00,
               "average_price": 380.00,
               "value": -380.00,
               "buy_value": 380.00,
               "sell_value": 0.00,
               "buy_quantity": 1,
               "sell_quantity": 0,
               "buy_price": 380.00,
               "sell_price": 0.00,
           }
       ]
   }
}
```

> [!NOTE]
>
> There are two arrays, `net` and `day`. The `day` array contains information of positions entered today while the `net` array gives information of positions carried forward plus the positions taken today.

#### Net Position

| field | description |
| --- | --- |
| `product` | Can be [INTRADAY, DELIVERY, MTF] |
| `quantity` | Total outstanding quantity from carried forward position and today's position |
| `overnight_buy_value` | Value of long carried forward position |
| `overnight_sell_value` | Value of short carried forward position |
| `overnight_average_price` | Average price of carried forward position |
| `lot_size` | Should be used for exchange NSE_CUR & MCX_FO. For these exchanges,actual quantity = quantity * lot_size * multiplier |
| `multiplier` | Should be used for exchange NSE_CUR & MCX_FO. For these exchanges,actual quantity = quantity * lot_size * multiplier |
| `average_price` | Average price of the entire outstanding quantity from carried forward position and today's position |
| `value` | Equal to `sell_value` - `buy_value` |
| `buy_value` | Total buy value of the entire outstanding quantity from carried forward position and today's position |
| `sell_value` | Total sell value of the entire outstanding quantity from carried forward position and today's position |
| `buy_quantity` | Total buy quantity from carried forward position and today's position |
| `sell_quantity` | Total sell quantity from carried forward position and today's position |
| `buy_price` | Average buy price of all quantity from carried forward position and today's position |
| `sell_price` | Average sell price of all quantity from carried forward position and today's position |

#### Day Position

| field | description |
| --- | --- |
| `product` | Can be [INTRADAY, DELIVERY, MTF] |
| `quantity` | Total outstanding quantity from today's position |
| `overnight_buy_value` | Default: 0. Should be omitted |
| `overnight_sell_value` | Default: 0. Should be omitted |
| `overnight_average_price` | Default: 0. Should be omitted |
| `lot_size` | Should be used for exchange NSE_CUR & MCX_FO. For these exchanges,actual quantity = quantity * lot_size * multiplier |
| `multiplier` | Should be used for exchange NSE_CUR & MCX_FO. For these exchanges,actual quantity = quantity * lot_size * multiplier |
| `average_price` | Average price of the outstanding quantity from today's position |
| `value` | Equal to `sell_value` - `buy_value` |
| `buy_value` | Total buy value of today's position |
| `sell_value` | Total sell value of today's position |
| `buy_quantity` | Total buy quantity of today's position |
| `sell_quantity` | Total sell quantity of today's position |
| `buy_price` | Average buy price of today's position |
| `sell_price` | Average sell price of today's position |

#### Calculating Gains:

- To calculate **overall gain**, use only the `net` array.

  ```
  For Long Position:

  Gain = (last_trade_price * quantity * lot_size * multiplier +overnight_sell_value ) - overnight_buy_value

  For Short Position:

  Gain = overnight_sell_value - (overnight_buy_value + last_trade_price * quantity * lot_size * multiplier)

  For Exited Position:

  Gain = sell_value - buy_value
  ```
- To calculate **today's gain**, use only the `day` array.
- Let's say you bought 1 lot of NIFTY 18000 CE yesterday at 70 rupees. At the end of the day, system will debit 70 * 50 = 3500 Rupees from your ledger. Today when you see the position, its MTM will start from 0. This pattern is valid for all Futures and Options.
- Let's say you sold bought 1 lot of NIFTY 18000 CE yesterday at 70 rupees. The market closed at 65. At the end of the day, system will credit 70 * 50 = 3500 Rupees in your ledger. Today when you see the position, its MTM will start from 65. This pattern is valid for all Futures and Options.
- If a position has both `net` and `day` positions, during squaroff the system will first square off `day` position and then carried forward position.

## Convert Position

Using this api, you can change the product of the position. `INTRADAY` product can be converted to `DELIVERY` and vice versa.

> [!NOTE]
>
> - Like order placement, a success returned from position conversion API doesnt mean that the position is converted. It simply means that the request has been accepted and the fate of the request will be decided later.
> - Positions in `MTF` product cannot be converted to any other product. You need to square off `MTF` position and then take another position in any product of your choosing.

> [!WARNING]
>
> Position conversion is currently disabled at risk management level

### Convert Position Object

```
{
    "ticker": "NSE:NIFTY26JUL25000CE",
    "transaction_type": "BUY",
    "quantity": 250,
    "old_product": "DELIVERY",
    "new_product": "INTRADAY"
}
```

#### Success Response

```
{
    "status": "success",
    "code": "s-101",
    "message": "Position Conversion Request Sent to OMS"   
}
```
