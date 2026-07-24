# Scrip Master

Daily contract master files, one CSV per exchange segment.

| Scrip Group | Download |
| --- | --- |
| NSE — Equity | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/NSE_Equity.csv> |
| NSE — Equity Derivatives | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/Nfo_Equity_Derivatives.csv> |
| NSE — Index Derivatives | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/Nfo_Index_Derivatives.csv> |
| NSE — Currency Derivatives | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/Currency_Derivatives.csv> |
| MCX — Commodity | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/Commodity.csv> |
| BSE — Equity | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/BSE_Equity.csv> |
| BSE — Index Derivatives | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/Bfo_Index_Derivatives.csv> |
| BSE — Equity Derivatives | <https://flattrade.s3.ap-south-1.amazonaws.com/scripmaster/Bfo_Equity_Derivatives.csv> |

These files map `tsym` (trading symbol) to `token` for each exchange segment and are the recommended way to resolve symbols/tokens in bulk, rather than calling [Search Scrips](11-scrips.md#search-scrips) or [Get Quotes](11-scrips.md#get-quotes) per contract.
