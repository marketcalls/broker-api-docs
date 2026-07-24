# Holdings and Limits

## Holdings

`POST /Holdings`

```bash
curl --location 'https://BaseURL/Holdings' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"prd": "C"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `actid`* | Account ID of the logged-in user |
| `prd`* | Product name |

### Response

```json
[
  {
    "stat": "Ok",
    "exch_tsym": [{ "exch": "NSE", "token": "13", "tsym": "ABB-EQ" }],
    "holdqty": "2000000", "colqty": "200", "btstqty": "0",
    "btstcolqty": "0", "usedqty": "0", "upldprc": "1800.00"
  }
]
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `exch_tsym` | Array of `{ exch, tsym, token, pp, ti, ls }` objects |
| `holdqty` | Holding quantity |
| `dpqty` | DP holding quantity |
| `npoadqty` | Non-POA display quantity |
| `colqty` | Collateral quantity |
| `benqty` | Beneficiary quantity |
| `unplgdqty` | Unpledged quantity |
| `brkcolqty` | Broker collateral |
| `btstqty` / `btstcolqty` | BTST quantity / BTST collateral quantity |
| `usedqty` | Holding used today |
| `upldprc` | Average price uploaded with holdings |

**Valuation** = `btstqty + holdqty + brkcolqty + unplgdqty + benqty + Max(npoadqty, dpqty) - usedqty`

**Salable** = `btstqty + holdqty + unplgdqty + benqty + dpqty - usedqty`

On failure: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "..." }`

---

## Limits

`POST /Limits`

```bash
curl --location 'https://BaseURL/Limits' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `actid`* | Account ID of the logged-in user |

### Response

```json
{
  "request_time": "18:07:31 29-05-2020", "stat": "Ok",
  "cash": "1500000000000000.00", "payin": "0.00", "payout": "0.00",
  "brkcollamt": "0.00", "unclearedcash": "0.00", "daycash": "0.00",
  "turnoverlmt": "50000000000000.00", "pendordvallmt": "2000000000000000.00",
  "turnover": "3915000.00", "pendordval": "2871000.00", "marginused": "3945540.00",
  "mtomcurper": "0.00", "urmtom": "30540.00", "grexpo": "3915000.00",
  "uzpnl_e_i": "15270.00", "uzpnl_e_m": "61080.00", "uzpnl_e_c": "-45810.00"
}
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `actid` | Account ID |
| `prd` | Product name |
| `seg` | Segment: CM / FO / FX |
| `exch` | Exchange |

#### Cash — Primary Fields

| Field | Description |
| --- | --- |
| `cash` | Cash margin available |
| `payin` | Total amount transferred via payins today |
| `payout` | Total amount requested for withdrawal today |

#### Cash — Additional Fields

| Field | Description |
| --- | --- |
| `brkcollamt` | Pre-valued collateral amount |
| `unclearedcash` | Uncleared cash (cheque payins) |
| `daycash` | Additional leverage / broker-added error-handling amount |

#### Margin Utilized

| Field | Description |
| --- | --- |
| `marginused` | Total margin / fund used today |
| `mtomcurper` | MTOM current percentage |

#### Margin Used Components

| Field | Description |
| --- | --- |
| `cbu` | CAC buy used |
| `csc` | CAC sell credits |
| `rpnl` | Current realized PNL |
| `unmtom` | Current unrealized MTOM |
| `marprt` | Covered product margins |
| `span` | Span used |
| `expo` | Exposure margin |
| `premium` | Premium used |
| `varelm` | Var Elm margin |
| `grexpo` / `greexpo_d` | Gross exposure / gross exposure derivative |
| `scripbskmar` / `addscripbskmrg` | Scrip basket margin / additional scrip basket margin |
| `brokerage` | Brokerage amount |
| `collateral` | Collateral from uploaded holdings |
| `cash_coll` | Cash collateral |
| `grcoll` | Valuation of uploaded holdings pre-haircut |

#### Additional Risk Limits / Indicators

| Field | Description |
| --- | --- |
| `turnoverlmt` / `pendordvallmt` | Turnover / pending order value limits |
| `turnover` | Turnover |
| `pendordval` | Pending order value |

#### Margin Used — Detailed Breakup

Realized PNL, unrealized MTOM, span, exposure, and premium are broken out per segment/leverage using the naming convention `<metric>_<segment>_<leg>`, where segment is `e` (Equity), `d` (Derivative), `f` (FX), or `c` (Commodity), and leg is `i` (Intraday), `m` (Margin), `c` (Cash & Carry), `h` (High Leverage), or `b` (Bracket Order). For example:

| Field | Description |
| --- | --- |
| `rzpnl_e_i` / `rzpnl_e_m` / `rzpnl_e_c` | Realized PNL — Equity Intraday / Margin / Cash n Carry |
| `rzpnl_d_i` / `rzpnl_d_m` | Realized PNL — Derivative Intraday / Margin |
| `rzpnl_f_i` / `rzpnl_f_m` | Realized PNL — FX Intraday / Margin |
| `rzpnl_c_i` / `rzpnl_c_m` | Realized PNL — Commodity Intraday / Margin |
| `uzpnl_e_i` / `uzpnl_e_m` / `uzpnl_e_c` | Unrealized MTOM — Equity Intraday / Margin / Cash n Carry |
| `uzpnl_d_i` / `uzpnl_d_m` / `uzpnl_f_i` / `uzpnl_f_m` / `uzpnl_c_i` / `uzpnl_c_m` | Unrealized MTOM — Derivative / FX / Commodity |
| `span_d_i` / `span_d_m` / `span_f_i` / `span_f_m` / `span_c_i` / `span_c_m` | Span margin per segment |
| `expo_d_i` / `expo_d_m` / `expo_f_i` / `expo_f_m` / `expo_c_i` / `expo_c_m` | Exposure margin per segment |
| `premium_d_i` / `premium_d_m` / `premium_f_i` / `premium_f_m` / `premium_c_i` / `premium_c_m` | Option premium per segment |
| `varelm_e_i` / `varelm_e_m` / `varelm_e_c` | Var Elm — Equity |
| `marprt_e_h` / `marprt_e_b` / `marprt_d_h` / `marprt_d_b` / `marprt_f_h` / `marprt_f_b` / `marprt_c_h` / `marprt_c_b` | Covered product margins — High Leverage / Bracket, per segment |
| `scripbskmar_e_i` / `scripbskmar_e_m` / `scripbskmar_e_c` | Scrip basket margin — Equity |
| `addscripbskmrg_d_i` / `addscripbskmrg_d_m` / `addscripbskmrg_f_i` / `addscripbskmrg_f_m` / `addscripbskmrg_c_i` / `addscripbskmrg_c_m` | Additional scrip basket margin |
| `brkage_e_i` / `brkage_e_m` / `brkage_e_c` / `brkage_e_h` / `brkage_e_b` | Brokerage — Equity |
| `brkage_d_i` / `brkage_d_m` / `brkage_d_h` / `brkage_d_b` | Brokerage — Derivative |
| `brkage_f_i` / `brkage_f_m` / `brkage_f_h` / `brkage_f_b` | Brokerage — FX |
| `brkage_c_i` / `brkage_c_m` / `brkage_c_h` / `brkage_c_b` | Brokerage — Commodity |

#### MR (Margin Report) Fields

| Field | Description |
| --- | --- |
| `mr_fx_u` | MR FX used |
| `mr_sell` | MR sell credit |
| `mr_t1sell` | MR T1 sell credit |
| `mr_eqt_a` | MR equity allocated |
| `mr_der_a` | MR derivatives allocated |
| `mr_fx_a` | MR FX allocated |
| `mr_com_a` | MR commodity allocated |

On failure: `{ "stat": "Not_Ok", "emsg": "Server Timeout : " }`
