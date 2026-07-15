# Order Update WebSocket

Real-time streaming of order status updates. Uses the same WebSocket connection as the [WebSocket API](10-websocket.md):

```
wss://trade.definedgesecurities.com/NorenWSTRTP/
```

Connect and send heartbeats as described in the [WebSocket API](10-websocket.md) document before subscribing to order updates.

---

## Subscribe Order Update

### Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | o | `o` represents the order update subscription task |
| `actid` | | Account id based on which order updates are to be sent |

### Subscription Acknowledgement

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | ok | `ok` represents order update subscription acknowledgement |
| `t` | om | `om` represents order update feed message |
| `norenordno` | | Noren Order Number |
| `uid` | | User Id |
| `actid` | | Account ID |
| `exch` | | Exchange |
| `tsym` | | Trading symbol |
| `qty` | | Order quantity |
| `prc` | | Order Price |
| `prd` | | Product |
| `status` | | Order status (New, Replaced, Complete, Rejected etc.) |
| `reporttype` | | Order event for which this message is sent out (Fill, Rejected, Canceled) |
| `trantype` | | Order transaction type, buy or sell |
| `prctyp` | | Order price type (LMT, MKT, SL-LMT, SL-MKT) |
| `ret` | | Order retention type (DAY, EOS, IOC, …) |
| `fillshares` | | Total Filled shares for this order |
| `avgprc` | | Average fill price |
| `fltm` | | Fill Time (present only when `reporttype` is Fill) |
| `flid` | | Fill ID (present only when `reporttype` is Fill) |
| `flqty` | | Fill Qty (present only when `reporttype` is Fill) |
| `flprc` | | Fill Price (present only when `reporttype` is Fill) |
| `rejreason` | | Order rejection reason, if rejected |
| `exchordid` | | Exchange Order ID |
| `cancelqty` | | Canceled quantity, in case of canceled order |
| `remarks` | | User added tag, while placing order |
| `dscqty` | | Disclosed quantity |
| `trgprc` | | Trigger price for SL orders |
| `snonum` | | Present for child orders in case of cover and bracket orders; if present needs to be sent during exit |
| `snoordt` | | Present for child orders in case of cover and bracket orders; indicates whether the order is profit or stoploss |
| `blprc` | | Present for cover and bracket parent order. Differential stop loss trigger price to be entered |
| `bpprc` | | Present for bracket parent order. Differential profit price to be entered |
| `trailprc` | | Present for cover and bracket parent order. Required if trailing ticks is to be enabled |
| `exch_tm` | | Exchange update time |

---

## Unsubscribe Order Update

### Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | uo | `uo` represents Unsubscribe Order update |

### Response

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | uok | `uok` represents Unsubscribe Order update acknowledgement |
