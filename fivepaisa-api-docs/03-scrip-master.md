# Scrip Master

The instrument master dump — segment-wise CSV of every tradable scrip, plus the `ScripData` symbol format.

> Source: https://xstream.5paisa.com/dev-docs/docFundamentals/scrip-master

The scrip master URL can be used to fetch the scrip details of all the equity, derivates and commodities for NSE, BSE and MCX . The details are fetched in the form of CSV dump which can be imported to a database. Scrip master is updated regularly and can be accessed through the URL mentioned below.

## SCRIP MASTER URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/ScripMaster/segment/{segment}
```

## Query Param

| KEY | VALUE |
|---|---|
| Segment | all - scrips across all segments<br>bse_eq - BSE Equity,<br>nse_eq - NSE Equity<br>nse_fo - NSE Derivatives<br>bse_fo - BSE Derivatives<br>ncd_fo - NSE Currecny<br>mcx_fo - MCX |

## ScripData Format

Please find below format for ScripData. The same is populated in API response for each instrument.

**EQUITY**  
Format: SYMBOL_EQ  
Ex. ScriptData :RELIANCE_EQ  
**FUTURE**  
Format - SYMBOL_yyyymmdd  
Ex.NIFTY 30 Sep 2021_20210930  
**OPTION**  
Symbol : BANKNIFTY 24 Nov 2022 CE 41600.00  
Format : SYMBOL_YYYYMMDD_CE/PE_STRIKE  
Ex. BANKNIFTY 24 Nov 2022 CE 41600.00_20221124_CE_41600  
BANKNIFTY 29 Mar 2023 CE 41600.00_20230329_CE_41600

## CSV Columns

| **FIELD NAME** | **DESCRIPTION** |
|---|---|
| Exch<br>STRING | It contains the exchange like<br>N : NSE<br>B : BSE<br>M : MCX (ExchType will be D) |
| ExchType<br>STRING | It contains segments like<br>C : Equity<br>D : Derivative (F&O) (But if Exch is M then Commodity)<br>U : Currency Derivative |
| ScripCode<br>INTEGER | Unique number for particular instrument - Used to Place Order |
| ScripData<br>INTEGER | Trading Symbol for a instrument - Used to Place Order<br>EQUITY<br>Format: SYMBOL_EQ<br>Ex. ScriptData :RELIANCE_EQ<br>FUTURE<br>Format - SYMBOL_yyyymmdd<br>Ex.NIFTY 30 Sep 2021_20210930<br>OPTION<br>Symbol : BANKNIFTY 24 Nov 2022 CE 41600.00<br>Format : SYMBOL_YYYYMMDD_CE/PE_STRIKE<br>Ex. BANKNIFTY 24 Nov 2022 CE 41600.00_20221124_CE_41600<br>BANKNIFTY 29 Mar 2023 CE 41600.00_20230329_CE_41600 |
| Name<br>STRING | Contract Name: It is the symbol but in case of F&O it is the combination of <br>Symbol, Expiry, OptionType, StrikePrice |
| Expiry<br>INTEGER | Contains expiry of F&O contract (ignore in case equity) |
| ScripType<br>STRING | Option type like<br>CE : Call Option<br>PE : Put Option<br>EQ : For NSE Indices<br>XX : Other contracts (Cash & Futures) |
| StrikeRate<br>INTEGER | Strike rate of F&O contracts |
| ISIN<br>STRING | ISIN of stock (valid for equity only) |
| LotSize<br>INTEGER | Specifies the lot size for each of the instrument. |
| FullName<br>STRING | Provides the full name of any instrument or contract. |
| QtyLimit<br>INTEGER | It provides the maximum quantity allowed in a particular trade. |
| TickSize<br>INTEGER | It provides the tick size for the respective instrument or contract.<br>**Note:** The tick size provided in the scrip master is in rupees. |
| Multiplier<br>INTEGER | It provides the multiplier for the respective instrument or contract. It is used to calculate the total quantity.<br>For example, for any USDINR currency contract, if quantity is 1 and multiplier is 1000, then total quantity is (quantity*multiplier), i.e. 1000. |
| BOCOAllowed<br>STRING | It describes if the bracket/cover order is allowed in the respective instrument.<br>**Values:**<br>Y: Bracket/cover order allowed<br>N: Bracket/cover order not allowed<br>**Note:** For options, BO & CO are allowed for a few strike rates near the spot price and changes with time, the scrip master shows default value “N” for all option contracts. |
| SymbolRoot<br>STRING | It provides the symbol name for the underlying index or cash security of the derivative contract.<br>**Note:** For Cash stock it will be same as stock Name, for Derivatives it will underlying index or stock name. |
| Series<br>STRING | It contain the series of equity symbol like EQ (for equity only), XX for Derivatives. |
