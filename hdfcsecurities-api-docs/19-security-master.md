# Security Master

> Source: https://developer.hdfcsec.com/ir-docs/docs/security_master

## Description

The Security Master API serves as a crucial tool for trading applications by offering a comprehensive catalog of securities and instruments traded across various exchanges and segments. This API provides a neatly consolidated CSV list that can be effortlessly imported, ensuring easy access to the wide array of securities available for trading.

## Download

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/security-master`
```

The official page exposes this only as a "Download CSV" link. The endpoint is unauthenticated —
no `api_key`, `Authorization` or `User-Agent` header is required — and responds with
`Content-Disposition: attachment; filename=ir-security-master.csv`.

```bash
curl -L -o ir-security-master.csv \
  'https://developer.hdfcsec.com/oapi/v1/security-master'
```

---

## CSV Schema

> Everything below this line is **not** in the official documentation. It was derived by
> downloading and inspecting the live CSV (~117,500 rows, ~8 MB, observed 2026-08-05). Treat it as
> observed behaviour rather than a published contract.

Header row:

```
exchange,security_id,instrument_segment,expiry_date,strike_price,option_type,lot_size,tick_size,close_price,exch_security_id,symbol_name,underline_symbol,open_price
```

| # | Column | Description |
| --- | --- | --- |
| 1 | `exchange` | `NSE`, `BSE` or `MCX` |
| 2 | `security_id` | The identifier to send as `security_id` in [Place Order](07-place-order.md). Alphanumeric for cash/commodity rows (`WIPLTDEQNR`, `SILVER100`), numeric token for derivative rows (`68180`) |
| 3 | `instrument_segment` | Segment code — see the table below |
| 4 | `expiry_date` | `YYYY-MM-DD` for derivatives, empty for cash/commodity underlyings |
| 5 | `strike_price` | Strike for options; sentinel values for futures (`-.01` for NSE equity/index futures, `-.0000001` for currency futures, `0` for MCX) |
| 6 | `option_type` | `CE`, `PE`, `XX` (futures) or empty (cash) |
| 7 | `lot_size` | Contract/board lot size; `1` for cash |
| 8 | `tick_size` | Minimum price increment, e.g. `5`, `.0025` |
| 9 | `close_price` | Previous close |
| 10 | `exch_security_id` | Numeric exchange token — this is the `token` value for [Fetch LTP](16-market-data-ltp.md) and the `(TOKEN)` in the [WebSocket](17-websocket.md) `scripId` prefixes |
| 11 | `symbol_name` | Trading symbol / display name |
| 12 | `underline_symbol` | Underlying identifier for derivatives (matches the `underlying_symbol` field in derivative order payloads); empty for cash |
| 13 | `open_price` | Opening price |

### Instrument segments present

| `instrument_segment` | Meaning | Observed row count |
| --- | --- | --- |
| `OPTSTK` | Stock options | 63,788 |
| `OPTIDX` | Index options | 16,831 |
| `OPTFUT` | Options on futures (MCX) | 15,078 |
| `EQUITY` | Cash equity | 13,880 |
| `OPTCUR` | Currency options | 7,041 |
| `FUTSTK` | Stock futures | 622 |
| `FUTCOM` | Commodity futures | 146 |
| `FUTCUR` | Currency futures | 129 |
| `FUTIDX` | Index futures | 33 |
| `COM` | Commodity underlying | 30 |
| `UNDCUR` | Currency underlying | 7 |

Row counts by exchange: NSE 87,188 · MCX 15,846 · BSE 14,551.

> `OPTFUT`, `FUTCOM`, `COM` and `UNDCUR` appear in the master but are **not** listed among the
> accepted `instrument_segment` values in [Place Order](07-place-order.md).

### Sample rows

```csv
exchange,security_id,instrument_segment,expiry_date,strike_price,option_type,lot_size,tick_size,close_price,exch_security_id,symbol_name,underline_symbol,open_price
BSE,IIF863NBNR,EQUITY,,,,1,1,1118.25,961796,863IIFCL28,,0
NSE,BHAENGEQNR,EQUITY,,,,1,1,122.94,419,BEPL,,121.32
NSE,48705,FUTIDX,2026-10-27,-.01,XX,25,20,73186.8,48705,NIFTYNXT50,NIFTYNXT50EQ,0
NSE,48796,FUTSTK,2026-10-27,-.01,XX,425,10,1481.4,48796,CIPLA,CIPLTDEQNR,1473.1
NSE,70528,OPTIDX,2026-09-29,71000,PE,30,5,0,70528,BANKNIFTY,BANKNIFTEQNR,0
NSE,91436,OPTSTK,2026-09-29,1720,CE,475,5,189.5,91436,BHARTIARTL,BHAAIREQNR,0
NSE,1273,FUTCUR,2026-10-28,-.0000001,XX,1,.0025,108.1675,1273,EURINR,EURINR,0
NSE,6506,OPTCUR,2026-08-07,126.25,PE,1,.0025,0,6506,GBPINR,GBPINR,0
NSE,EURINR,UNDCUR,,,,1,.0025,0,25,EURINR,,0
MCX,575691,FUTCOM,2027-06-04,0,XX,1,100,0,575691,GOLD,GOLD,0
MCX,575385,OPTFUT,2027-04-23,244000,CE,5,50,0,575385,SILVERM,SILVERM,0
MCX,SILVER100,COM,,,,100,100,0,637,SILVER100,,0
```

### Identifier cheat sheet

| You need to… | Use this column |
| --- | --- |
| Place / modify an order | `security_id` |
| Set `underlying_symbol` on a derivative order | `underline_symbol` |
| Fetch LTP | `exch_security_id` |
| Build a WebSocket `scripId` | prefix + `exch_security_id`, e.g. `NFO_70528` |

For cash equity rows the two identifiers differ (`security_id` = `BHAENGEQNR`,
`exch_security_id` = `419`). For derivative rows they are usually the same numeric token.
