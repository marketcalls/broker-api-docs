> Source: https://docs.arrow.trade/rest-api/symbols/

# Symbols

* * *

The Arrow Trade Instrument API provides comprehensive access to all tradable instruments available on supported exchanges. This unified interface delivers market data in a structured CSV format, enabling seamless integration for algorithmic trading, portfolio management, and market analysis applications.

## Real-Time Instrument Data

### Complete Instrument Universe

Access the complete catalog of tradable instruments across all supported exchanges and segments with a single API call. The instrument database is refreshed daily at **8:00 AM IST** to ensure accuracy and relevance for each trading session.

**Example Request**

```bash
curl --location 'https://edge.arrow.trade/all' \
--header 'appID: <YOUR_APPLICATION_ID>' \
--header 'token: <YOUR_AUTHENTICATION_TOKEN>'
```

> **Important:** Download instrument data only after 8:00 AM IST to ensure you receive the most current trading session tokens. Accessing the data before this time may result in stale instrument tokens from the previous trading session.

## Response Format

The API returns comprehensive instrument data in CSV format with the following structure:

```
Exchange,Segment,ExchSeg,Token,FullName,Symbol,TradingSymbol,Series,ISIN,LotSize,TickSize,PricePrecision,OptionType,Underlying,UnderlyingToken,StrikePrice,Expiry,FreezeQty,Lower Band,Upper Band,SurCodes,Events,ExchangeID
NSE,CM,NSECM,3045,STATE BANK OF INDIA,SBIN,SBIN-EQ,EQ,INE062A01020,1,0.10,2,,,0,0.00,,0,1073.20,1311.60,,,3045
NSE,CM,NSECM,2885,RELIANCE INDUSTRIES LTD,RELIANCE,RELIANCE-EQ,EQ,INE002A01018,1,0.10,2,,,0,0.00,,0,1304.10,1593.70,,,2885
NSE,FO,NSEFO,104034,DIVISLAB,DIVISLAB,DIVISLAB30MAR26C6450,XX,,100,0.05,2,CE,DIVISLAB,10940,6450.00,30-Mar-2026,4000,61.75,301.55,,,104034
NSE,FO,NSEFO,104190,DIVISLAB,DIVISLAB,DIVISLAB28APR26P5800,XX,,100,0.05,2,PE,DIVISLAB,10940,5800.00,28-Apr-2026,4000,70.95,230.45,,,104190
NSE,FO,NSEFO,163082,TITAN,TITAN,TITAN30MAR26C3720,XX,,175,0.05,2,CE,TITAN,3506,3720.00,30-Mar-2026,7000,434.15,751.75,,,163082
NSE,FO,NSEFO,59577,BANKNIFTY,BANKNIFTY,BANKNIFTY24FEB26C43800,XX,,30,0.05,2,CE,BANKNIFTY,26009,43800.00,24-Feb-2026,600,15527.25,18524.05,,,59577
NSE,INDEX,NSEIDX,26016,,HangSeng BeES-NAV,,,,,1,,,,,,,,,,,,26016
NSE,INDEX,NSEIDX,26017,,India VIX,,,,,1,,,,,,,,,,,,26017
NSE,INDEX,NSEIDX,26000,,Nifty 50,,,,,1,,,,,,,,,,,,26000
NSE,INDEX,NSEIDX,26008,,Nifty IT,,,,,1,,,,,,,,,,,,26008
NSE,INDEX,NSEIDX,26013,,Nifty Next 50,,,,,1,,,,,,,,,,,,26013
NSE,INDEX,NSEIDX,26009,,Nifty Bank,,,,,1,,,,,,,,,,,,26009
```

## Different file Endpoints

The following endpoints allows you to download file Segment wise

Segment | Endpoint
---|---
ALL | `/all`
NSE | `/nse`
BSE | `/bse`
MCX | `/mcx`

## Field Specifications

### Core Trading Fields ⭐

The following fields are essential for most trading operations and API interactions:

Field | Data Type | Description
---|---|---
**ExchSeg** ⭐ | `string` | Exchange segment identifier: `NFO` (NSE F&O), `NSE` (NSE Equity), `BFO` (BSE F&O), `BSE` (BSE Equity)
**Token** ⭐ | `int64` | Unique instrument identifier required for all API operations
**TradingSymbol** ⭐ | `string` | Primary trading symbol used in order placement and market data APIs
**StrikePrice** ⭐ | `int64` | Option strike price (multiplied by 100 for precision)

### Comprehensive Instrument Data

Field | Data Type | Description
---|---|---
**LotSize** | `int64` | Minimum tradable quantity per lot
**Symbol** | `string` | Exchange-recognized symbol identifier
**CompanyName** | `string` | Complete registered company name
**Exchange** | `string` | Primary exchange: `NSE` or `BSE`
**Segment** | `string` | Market segment: `EQT` (Equity), `DER` (Derivatives)
**Instrument** | `string` | Instrument classification: `EQ`, `FUTIDX`, `OPTIDX`, `FUTSTK`, `OPTSTK`, `BE`, `BL`, `SM`
**ExpiryDate** | `string` | Contract expiration date (derivatives only)
**Isin** | `string` | International Securities Identification Number
**TickSize** | `decimal` | Minimum price movement in paisa
**PricePrecision** | `int` | Decimal places supported in price quotations
**Multiplier** | `decimal` | Contract multiplier for position sizing
**PriceMultiplier** | `decimal` | Price calculation multiplier
**OptionType** | `string` | Option classification: `CE` (Call European), `PE` (Put European)
**UnderlyingExchange** | `string` | Exchange of the underlying asset (derivatives)
**UnderlyingToken** | `int64` | Token identifier of the underlying instrument
**ExchExpiryDate** | `int64` | Exchange expiry timestamp (add 10 years to epoch time)
**UpdateTime** | `int64` | Last modification timestamp (epoch time)
**MessageFlag** | `string` | Internal processing flag

## Implementation Guidelines

**Header:** All requests require valid `appID` and `token` headers for secure access to market data.

**Data Freshness:** The instrument database is synchronized daily at 8:00 AM IST. Applications should refresh their local cache accordingly.

**Performance:** The API delivers the complete instrument universe in a single response, optimizing for high-frequency trading applications that require comprehensive market coverage.

**Integration:** The CSV format enables direct import into popular trading platforms, database systems, and analytical tools without additional processing overhead.

* * *

_For additional ISIN lookups and verification, reference the[ NSDL Master Search ](https://nsdl.co.in/master_search.php) portal._
