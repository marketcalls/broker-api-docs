<!-- Source: https://vortex.rupeezy.in/docs/2.2/postbacks/ -->

# Postbacks

Order updates and trade notifications are sent as webhooks to the developer application. The webhook url is configured at the time of application registration.

> [!NOTE]
>
> To safely consume the webhook, you must verify the webhook payload with the `x-astha-signature` header.

### Webhook Payload

```
{
    "type": "trade",
    "data": {
      "order_id": "NXAAE0001AC4",
      "order_number": "1100000014117098",
      "amo_order_id": "",
      "placed_by": "APIMOBILE",
      "modified_by": "APIMOBILE",
      "status": "COMPLETED",
      "status_message": "",
      "symbol": "ITC",
      "series": "EQ",
      "instrument_name": "",
      "ticker": "NSE:ITC",
      "token": 1660,
      "exchange": "NSE_EQ",
      "expiry_date": "",
      "strike_price": 0,
      "option_type": "",
      "transaction_type": "BUY",
      "validity": "",
      "validity_days": 0,
      "product": "INTRADAY",
      "variety": "RL",
      "disclosed_quantity": 0,
      "disclosed_quantity_remaining": 0,
      "total_quantity": 1,
      "pending_quantity": 0,
      "traded_quantity": 1,
      "market_type": "",
      "order_price": 40020,
      "trigger_price": 0,
      "traded_price": 40020,
      "is_amo": false,
      "order_identifier": "-1",
      "order_created_at": "19-Apr-2023 12.32.59",
      "order_updated_at": "19-Apr-2023 12.32.59",
      "trade_number": "27511919",
      "trade_time": "19-Apr-2023 12.32.59",
      "market_segment_id": 1,
      "gtd_order_status": ""
    },
    "client_code":"DEMO"
}
```

| field | description |
| --- | --- |
| `type` | Type of message received. Possible values: [`order`, `trade`, `sl_trigger`, `gtt_order` or `position_conversion`] |
| `data` | Contains the payload for the type. Structure remains the same for all types. |
| `order_id` | Rupeezy's order id |
| `order_number` | Exchange order number |
| `amo_order_id` | Rupeezy's after market order id |
| `placed_by` | Source of order placement |
| `modified_by` | Source of order modification |
| `status` | Status of the order |
| `status_message` | Error reason if any |
| `symbol` | Symbol of the order |
| `series` | Series of the stock |
| `instrument_name` | Instrument name like EQ, OPTFUT, OPTCUR etc. |
| `ticker` | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:ITC`) |
| `token` | Token of the security |
| `exchange` | Exchange of the security |
| `expiry_date` | Expirry date of the option contract |
| `strike_price` | Strike price of the option contract |
| `option_type` | CE or PE |
| `transaction_type` | BUY or SELL |
| `validity` | For a pending order, for how long is the order valid. Possible values: [`DAY`, `IOC` or `AMO`] |
| `validity_days` | Number of days for which order is valid |
| `product` | Possible values: [INTRADAY, DELIVERY, BTST, MTF].MTF & BTST product can only be used in NSE_EQ exchange. |
| `variety` | Possible values: [RL, RL-MKT, SL, SL-MKT]. RL means regular orders, SL means Stop Loss order. MKT means that the trade will happen at market price |
| `disclosed_quantity` | Disclosed quantity of the order |
| `disclosed_quantity_remaining` | Remaining disclosed quantity of the order |
| `total_quantity` | Total quantity in the order |
| `pending_quantity` | Pending quantity in the order |
| `traded_quantity` | Traded quantity |
| `market_type` | Market type. Possible values: [`NORMAL`,`AUCTION` or `PREOPEN`] |
| `order_price` | Limit price of the order |
| `trigger_price` | Trigger price of the order |
| `traded_price` | Traded Price |
| `is_amo` | Whether it is an AMO Order |
| `order_created_at` | Order created at |
| `order_updated_at` | Order updated at |
| `trade_number` | Trade number |
| `trade_time` | Trade time |
| `market_segment_id` | Market segment id of the exchange |
| `gtd_order_status` | GTD order status |
| `trail` | If trailing stoploss is enabled, it will be attached to the stoploss leg in `gtt_order` |
| `trail.id` | ID of the trail leg |
| `trail.trail_first_jump` | The reference point from where the trail starts |
| `trail.trail_jump_point` | The jump amount specified |
| `trail.trail_jump_type` | The jump type specified. Possible values: [`Percent`,`Point`] |
| `trail.trigger_trail` | The price that is used as the trigger to jump |

### Signature Verification

To verify the authenticity of the payload and to make sure it has originated from Rupeezy's servers, you should create a HMAC-SHA256 signature of the payload that you have received using the `x-api-key` generated for the application on the developer portal. Then you should match the generated signature with `x-astha-signature` header value.

> [!NOTE]
>
> Some languages may generate signature in uppercase. To be on the safe side you can always convert uppercase to lowercase and then compare.

**golang**

```
    func signRequest(body []byte, key string) string {
        h := hmac.New(sha256.New, []byte(key))
        h.Write(body)
        return hex.EncodeToString(h.Sum(nil))
    }
```
