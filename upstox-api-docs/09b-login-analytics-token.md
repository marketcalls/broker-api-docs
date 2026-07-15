# Analytics Token

## Overview

The Analytics Token serves as a long-lived access credential with a one-year validity period. It provides read-only access to a defined set of Upstox APIs without requiring authorization redirects.

## Key Characteristics

- 1-year expiration from generation date
- Read-only access exclusively
- One token permitted per account simultaneously
- No trading or account operations supported

**Restrictions:** The token explicitly cannot facilitate placing or modifying orders, and retrieving positions, holdings, funds, profile, or trade details.

## Generation Process

1. Access the Upstox Developer Apps Analytics tab
2. Select the Generate Token button
3. Confirm the generation request
4. Copy the complete token value using the provided copy function

## Supported API Endpoints

| Category | API Name |
|----------|----------|
| Market Data | Quotes, OHLC V3, LTP V3 |
| Historical Data | HistoricalCandle V3, MarketDataFeed V3 |
| Derivatives | OptionGreek, PutCallOptionChain, OptionContracts |
| System | Brokerage, MarketStatus, CalculateMargin |
| Search | SearchInstruments, MarketDataFeedAuthorize V3 |

## Security Guidance

Users should avoid sharing tokens and maintain secure storage practices for this sensitive credential.
