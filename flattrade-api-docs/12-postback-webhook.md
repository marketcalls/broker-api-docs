# Postback / Webhook

You receive order updates for orders placed through the API on the **Postback URL** registered against your API key (see [Introduction](01-introduction.md#registering-your-app)).

## Sample Payload

```json
{
  "norenordno": "23010500000376",
  "kidid": "1",
  "uid": "ASHWATHINV123",
  "actid": "ASHWATHINV",
  "exch": "NSE",
  "tsym": "ACC-EQ",
  "qty": "1",
  "rorgqty": "0",
  "ipaddr": "117.248.82.174",
  "ordenttm": "1672921211",
  "sno_fillid": "",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "amo": "Yes",
  "token": "22",
  "prc": "2500.00",
  "pcode": "C",
  "remarks": "",
  "status": "OPEN",
  "rpt": "New",
  "ls": "1",
  "ti": "0.05",
  "rprc": "2500.00",
  "dscqty": "0",
  "norentm": "17:50:11 05-01-2023",
  "checksum": "619521a541ff3e634ecb02147f0cb77e822ea415c9b79259cd5e40592a73b810"
}
```

## Fields

| Field | Description |
| --- | --- |
| `norenordno` | Noren order number |
| `uid` / `actid` | User ID / Account ID |
| `exch` / `tsym` | Exchange / trading symbol |
| `qty`* | Order quantity |
| `prc`* | Order price (cannot be zero) |
| `prd` | Product |
| `status` | Order status (New, Replaced, Complete, Rejected, ...) |
| `reporttype` | Order event that triggered this postback (Fill, Rejected, Canceled) |
| `trantype`* | `B` / `S` |
| `prctyp` | Order price type (LMT, SL-LMT) |
| `ret`* | Retention type (DAY / EOS / IOC) |
| `fillshares` | Total filled shares |
| `avgprc` | Average fill price |
| `fltm` / `flid` / `flqty` / `flprc` | Fill time / ID / quantity / price — present only when `reporttype` is `Fill` |
| `rejreason` | Rejection reason, if rejected |
| `exchordid` | Exchange order ID |
| `cancelqty` | Cancelled quantity |
| `remarks` | User tag from order entry |
| `dscqty`* | Disclosed quantity |
| `trgprc` | Trigger price for SL orders |
| `snonum` | Present for cover/bracket child orders — send during exit |
| `snoordt` | Indicates whether a cover/bracket child order is the profit or stoploss leg |
| `blprc` | Cover/bracket parent — differential stop-loss trigger price |
| `bpprc` | Bracket parent — differential profit price |
| `trailprc` | Cover/bracket parent — required if trailing ticks enabled |
| `exch_tm` | Exchange update time (`dd-mm-YYYY hh:MM:SS`) |
| `amo`* | `Yes` if an After Market Order |
| `tm` | Timestamp |
| `kidid` | Kid ID |
| `sno_fillid` | BO sequence ID |
| `checksum` | `sha256(norenordno + norentm + vendor_key)` — verify this matches to reject spoofed postbacks from third parties |

> Always verify `checksum` before trusting a postback payload.
