# Overall Position

> Source: https://developer.hdfcsec.com/ir-docs/docs/overall_position

## Description

The overall position provides users with a comprehensive view of all positions, including both day and overnight carry forwarded positions.

## EndPoint

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/portfolio/cumulative-positions?api_key=<api_key>`
```

> **Path discrepancy:** the endpoint block documents `/oapi/v1/portfolio/cumulative-positions`
> while the curl sample below calls `/oapi/v1/portfolio/overall_positions`. Both are reproduced
> verbatim from the official page.

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

| Key | Description |
| --- | --- |
| client_id | Unique identifier for the client |
| security_id | Unique identifier for the security (if applicable) |
| instrument_segment | Type of segment (Equity, Derivatives, Currency) |
| underlying_symbol | Symbol of the underlying asset |
| product | Product code or type of trading (e.g., INTRADAY) |
| exchange | Exchange where the security is traded |
| expiry_date | Expiry date of the transaction (format: yyyy-mm-dd) |
| option_type | Type of option (CE for Call, PE for Put) |
| strike_price | Strike price of the option |
| total_buy_quantity | Total buy quantity (CF buy Qty + T-day Buy Qty) |
| total_sell_qty | Total sell quantity (CF Sell Qty + T-day Sell Qty) |
| net_qty | Net Quantity (Total buy qty - Total sell qty) |
| t_day_net_qty | Today's Net Quantity (Today Total buy qty - Today Total sell qty) |
| average_buy_price | Average buy price considering Carry Forward price |
| average_sell_price | Average sell price considering Carry Forward price |
| total_buy_value | Total buy value |
| total_sell_value | Total sell value |
| t_day_buy_quantity | Today's buy quantity |
| t_day_sell_qty | Today's sell quantity |
| t_day_average_buy_price | Today's average buy price |
| t_day_avg_sell_price | Today's average sell price |
| t_day_buy_value | Today's buy value |
| t_day_sell_value | Today's sell value |
| cf_buy_qty | Carry forward buy quantity |
| cf_sell_qty | Carry forward sell quantity |
| cf_average_buy_price | Carry forward buy price |
| cf_average_sell_price | Carry forward sell price |
| cf_buy_value | Carry forward buy value |
| cf_sell_value | Carry forward sell value |
| realised_pl_overall_position | Realised P&L for todays and carry forwared positions |
| realised_pl_t_day_position | Realised P&L for todays transactions |

## Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/portfolio/overall_positions?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

## API Response

```js
{
  "status": "success",
  "data": {
      "net": [
          {
                "client_id": "123456",
                "security_id": "43382",
                "instrument_segment": "OPTIDX",
                "underlying_symbol": "NIFTY",
                "product": "OVERNIGHT",
                "exchange": "NSE",
                "expiry_date": "27-JUN-24",
                "option_type": "Put",
                "strike_price": 14000.0,
                "total_buy_quantity": 100,
                "total_sell_qty": 25,
                "net_qty": 75,
                "average_buy_price": 2.3,
                "average_sell_price": 2.5,
                "total_buy_value": 230.0,
                "total_sell_value": 62.5,
                "t_day_buy_quantity": 0,
                "t_day_sell_qty": 25,
                "t_day_net_qty": -25,
                "t_day_average_buy_price": 0.0,
                "t_day_avg_sell_price": 2.5,
                "t_day_buy_value": 0.0,
                "t_day_sell_value": 62.5,
                "cf_buy_qty": 100,
                "cf_sell_qty": 0,
                "cf_average_buy_price": 2.3,
                "cf_average_sell_price": 0.0,
                "cf_buy_value": 230.0,
                "cf_sell_value": 0.0,
                "realised_pl_overall_position": 5.000000000000004,
                "realised_pl_t_day_position": 0.0
          }
      ]
  }
}
```

> The official sample has a trailing comma after the position object. It is removed above so the
> sample parses as JSON.

## Response field notes

- Positions are nested under `data.net` — an object wrapping an array, not a bare array.
- `expiry_date` is documented as `yyyy-mm-dd` but the sample returns `DD-MON-YY` (`"27-JUN-24"`).
- `option_type` is documented as `CE` / `PE` but the sample returns `Put`.
- There is no unrealised P&L or LTP field; mark-to-market must be computed from
  [Fetch LTP](16-market-data-ltp.md).
