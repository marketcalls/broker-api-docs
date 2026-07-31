# Master Files

> Source: <https://zebumyntapi.web.app/OAuth/Masters/>

> **OAuth Authentication Required**
>
> Master file downloads require OAuth authentication. You must first obtain an access token through the OAuth flow before accessing these files.

## Overview

Master files contain comprehensive trading instrument data for all supported exchanges and segments. These files are essential for:

- **Symbol Lookup**: Finding trading symbols, tokens, and instrument details
- **Market Data Integration**: Mapping symbols to real-time market data feeds
- **Order Placement**: Validating trading symbols before placing orders
- **Portfolio Management**: Identifying instruments in your holdings and positions

## Available Master Files

The following master files are available for download:

### Equity Markets

**NSE Cash Market**
- **URL**: [https://go.mynt.in/NSE_symbols.txt.zip](https://go.mynt.in/NSE_symbols.txt.zip)
- **Content**: All equity instruments traded on NSE
- **Format**: Compressed text file with symbol details

**BSE Cash Market**
- **URL**: [https://go.mynt.in/BSE_symbols.txt.zip](https://go.mynt.in/BSE_symbols.txt.zip)
- **Content**: All equity instruments traded on BSE
- **Format**: Compressed text file with symbol details

### Derivatives Markets

**NSE F&O (Futures & Options)**
- **URL**: [https://go.mynt.in/NFO_symbols.txt.zip](https://go.mynt.in/NFO_symbols.txt.zip)
- **Content**: All futures and options contracts on NSE
- **Format**: Compressed text file with contract details

**BSE F&O (Futures & Options)**
- **URL**: [https://go.mynt.in/BFO_symbols.txt.zip](https://go.mynt.in/BFO_symbols.txt.zip)
- **Content**: All futures and options contracts on BSE
- **Format**: Compressed text file with contract details

### Currency Derivatives

**NSE CDS (Currency Derivatives Segment)**
- **URL**: [https://go.mynt.in/CDS_symbols.txt.zip](https://go.mynt.in/CDS_symbols.txt.zip)
- **Content**: All currency derivative instruments on NSE
- **Format**: Compressed text file with currency pair details

### Commodity Markets

**MCX (Multi Commodity Exchange)**
- **URL**: [https://go.mynt.in/MCX_symbols.txt.zip](https://go.mynt.in/MCX_symbols.txt.zip)
- **Content**: All commodity instruments traded on MCX
- **Format**: Compressed text file with commodity details

## File Format

All master files are provided as compressed ZIP files containing text files with the following structure:
- **Symbol**: Trading symbol identifier
- **Token**: Unique numeric identifier for the instrument
- **Exchange**: Exchange code (NSE, BSE, MCX, etc.)
- **Segment**: Market segment (EQ, F&O, CDS, etc.)
- **Instrument Type**: Type of instrument (EQ, FUT, OPT, etc.)
- **Lot Size**: Minimum trading quantity
- **Tick Size**: Minimum price movement
- **Expiry Date**: For derivatives (if applicable)
- **Strike Price**: For options (if applicable)

## Usage Guidelines

1. **Download Frequency**: Master files are updated daily. Download fresh files before market hours
2. **File Size**: Files are compressed to minimize download time and bandwidth usage
3. **Parsing**: Extract and parse the text files to build your local symbol database
4. **Caching**: Cache the parsed data locally for faster symbol lookups
5. **Validation**: Always validate symbols against the latest master file before trading

## Integration Example

```python
import requests
import zipfile
import io

# Download and extract master file
url = "https://go.mynt.in/NSE_symbols.txt.zip"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

response = requests.get(url, headers=headers)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))
symbols_data = zip_file.read("NSE_symbols.txt").decode('utf-8')

# Parse symbols data
for line in symbols_data.split('\n'):
    if line.strip():
        # Process each symbol line
        parts = line.split('|')
        symbol = parts[0]
        token = parts[1]
        # ... process other fields
```

## Important Notes

- Master files are updated daily after market hours
- Always use the latest version for accurate symbol information
- Symbol formats may vary between exchanges
- Some symbols may be delisted or suspended - check status before trading
- File download requires valid OAuth access token
