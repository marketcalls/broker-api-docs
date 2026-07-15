# Master File

| Particular | Details |
| --- | --- |
| API Name | Download link for Master file of Symbols |
| Method | GET |
| Produces | application/zip |

## Download URLs

| Segment | URL |
| --- | --- |
| NSE Cash | `https://app.definedgesecurities.com/public/nsecash.zip` |
| NSE FNO | `https://app.definedgesecurities.com/public/nsefno.zip` |
| NSE CDS | `https://app.definedgesecurities.com/public/cdsfno.zip` |
| BSE Cash | `https://app.definedgesecurities.com/public/bsecash.zip` |
| BSE FNO | `https://app.definedgesecurities.com/public/bsefno.zip` |
| MCX FNO | `https://app.definedgesecurities.com/public/mcxfno.zip` |
| All Segments | `https://app.definedgesecurities.com/public/allmaster.zip` |

## Description

This link downloads the master file consisting of all the symbols of all segments, in zip format.

- You should download this file **every morning after 7:30 AM** for the latest trading symbols.
- These trading symbols are arranged as per different exchanges and segments. An application that consumes the trading API needs to update the master file on a daily basis.
- The extracted zip file produces a CSV file which can be imported in your trading software.

## Response Message Format

Fields in the downloaded CSV file appear in the following sequence:

| # | Field | Type | Notes |
| --- | --- | --- | --- |
| 1 | SEGMENT | STRING | NSE / BSE / NFO / CDS / MCX |
| 2 | TOKEN | INT | |
| 3 | SYMBOL | STRING | |
| 4 | TRADINGSYM | STRING | |
| 5 | INSTRUMENT TYPE | STRING | |
| 6 | EXPIRY | DDMMYYYY | Only for derivatives |
| 7 | TICKSIZE | INT | |
| 8 | LOTSIZE | INT | |
| 9 | OPTIONTYPE | STRING | |
| 10 | STRIKE | INT | Actual Strike price = `STRIKE / (MULTIPLIER * 10 ^ PRICEPREC)` |
| 11 | PRICEPREC | INT | Use this for calculating strike price |
| 12 | MULTIPLIER | INT | Use this for calculating strike price |
| 13 | ISIN | STRING | Empty when not applicable |
| 14 | PRICEMULT | FLOAT | |
| 15 | COMPANY | STRING | Company name |
