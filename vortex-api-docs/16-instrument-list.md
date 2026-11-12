<!-- Source: https://vortex.rupeezy.in/docs/2.2/instrument-list/ -->

# Instrument List

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| File Download | <https://static.rupeezy.in/master.csv> | Download a CSV file of all instruments in NSE & BSE | N/A |
| `GET` | [{{base_url}}/data/instruments](#fetch-all-instruments) | Fetch all Instruments | 1/sec |

## File Download

The csv file is refreshed every morning. To ensure fresh data, download the file every day after 8:30 AM.

## Fetch All Instruments

Endpoint: /data/instruments

A CSV of all available instruments. You must download the csv at the start of your trading session and keep it saved
locally. Prefer downloading the file about an hour before start of the trading session.

| field | description |
| --- | --- |
| token | Token assigned to the scrip. Use this for placing orders, fetching quotes etc. |
| exchange | Exchange in which the token is listed. Possible values: [NSE_EQ,NSE_FO,NSE_CUR,MCX_FO] |
| symbol | Symbol of the scrip |
| instrument_name | The kind of instrument represented in the scrip |
| series | Series of the stock |
| expiry_date | Expiry date of the option in format YYYYMMDD |
| option_type | Whether the option is CE or PE |
| strike_price | Strike price of the option in rupees |
| tick | Tick size of the scrip |
| lot_size | Lot size of the scrip |
| eligibility | Whether the symbol is eligibile to trade or not. 1 means eligible.[1,0] |
| security_desc | Description of the security |
| asm_gsm_stage | Surveillance stage under SEBI/exchange ASM (Additional Surveillance Measure) or GSM (Graded Surveillance Measure) frameworks. Indicates restricted-trading state — typically higher margin, price bands, or T2T settlement. Empty means the scrip is under normal trading. |
| last_trading_date | Last date on which this contract can be traded |
| isin_code | 12-character International Securities Identification Number that uniquely identifies the security globally |
| ticker | Canonical `<exchange>`:`<symbol>` identifier (e.g. NSE:RELIANCE, NSE:NIFTYIDX, NSE:ASHOKLEY26JUL135PE) |
