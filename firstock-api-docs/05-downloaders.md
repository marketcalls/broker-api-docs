# Downloaders

> Source: https://firstock.in/api/docs/downloaders/

> This section provides the downloadable file that is necessary for symbol details

## Overview

To efficiently interact with Firstock’s trading services, it’s crucial to use the correct symbol identifiers. Firstock provides downloadable symbol files containing comprehensive, up-to-date references for various segments. This dedicated section highlights these files and explains how to use them in your trading applications.

## Symbol Files

Each file corresponds to a specific exchange or segment. You can find the latest symbol files at the links below:

**NSE**

 Includes equity symbols listed on the National Stock Exchange (NSE).
 [NSE Symbol](https://api.firstock.in/V1/symbols/NSE?ref=firstock.in)

**BSE**

 Includes equity symbols listed on the National Stock Exchange (NSE).
 [BSE Symbol](https://api.firstock.in/V1/symbols/BSE?ref=firstock.in)

**NFO**

 Covers NSE Futures & Options (derivatives) symbols and contract details.
 [NFO Symbol](https://api.firstock.in/V1/symbols/NFO?ref=firstock.in)

**BFO**

 Contains BSE Futures & Options (derivatives) symbols.
 [BFO Symbol](https://api.firstock.in/V1/symbols/BFO?ref=firstock.in)

**Index Symbols**

 Features major market indices (NFO and BFO).
 [Indices Derivatives](https://api.firstock.in/V1/symbols/Indices?ref=firstock.in)

## File Format and Contents

1. File Type: Typically provided in CSV or similar delimited format.
2. Columns: Common fields may include symbol name, exchange code, instrument type, expiry date (for derivatives), and other contract specifications.
3. Usage: Integrate these symbols into your application’s watchlists, order placement systems, or charting tools.

## Example Fields (may vary by file):

- Symbol
- Instrument
- Expiry Date
- Lot Size
- Tick Size
- ISIN (for equities)

## Downloader Section

- Location: These files are hosted on the Firstock API server, ensuring you always have the latest symbol details.
- Frequency: Symbol files are updated periodically to reflect new listings, symbol changes, contract expirations, or any delistings.

**Integration Tip:** Automate the download and parsing process to keep your local database in sync with current market offerings.

## Best Practices

1. Regular Updates

  a. Schedule automated checks and downloads to capture newly listed or expired contracts, renamed symbols, or corporate actions.
2. Data Validation

  a. Confirm that the downloaded file’s data fields align with your internal data structures (e.g., check for format changes).
3. Version Control

  a.Retain previous versions of the symbol files (if necessary) for reference and audit purposes.
4. Error Handling

  a. Incorporate failsafes in case the download is temporarily unavailable or if the data contains unexpected values.

## Common Use Cases

- Trading Applications: Ensure correct symbol mapping for order placement and portfolio tracking.
- Market Analysis Tools: Display current symbol data in dashboards, charts, or scanning tools.
- Backtesting Platforms: Use the updated symbol list for historical data retrieval and simulation.

**Conclusion**

Keeping your symbol list current is integral to maintaining accurate and efficient trading operations. By using the downloadable files provided for NFO, BFO, NSE, BSE, and Index symbols, you can streamline your development process, reduce symbol mismatch errors, and stay aligned with evolving market structures.
