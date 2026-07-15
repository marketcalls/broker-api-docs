# Kite Connect 3 API - Overview

Kite Connect is a set of REST-like HTTP APIs that expose many capabilities required to build a complete stock market investment and trading platform. It enables real-time order execution, portfolio management, live market data streaming via WebSockets, and additional trading functionalities.

## Technical Details

- **Input format:** Form-encoded parameters
- **Output format:** JSON (with rare exceptions)
- **Response compression:** May be Gzipped
- **Root endpoint:** `https://api.kite.trade`
- **Current version:** 3 (specify via `X-Kite-version: 3` header)

## Authentication

- An `api_key` and `api_secret` pair are issued to developers
- Developers must register a redirect URL for post-login user routing
- The `api_secret` must never be embedded in client applications

## Getting Started

1. Visit the Kite Connect Developer Portal and register
2. Log in and create a new application to obtain API credentials
3. Configure the redirect URL for post-authentication user routing
4. Complete the authentication flow
5. Select from official SDKs (Python, Go, Java, PHP, Node.js, .NET)

## Prerequisites

- Active Zerodha trading account with 2FA TOTP enabled
- Developer account at https://developers.kite.trade

## Documentation Sections

| Section | Description |
|---------|-------------|
| SDKs | Client libraries for Python, Go, Java, PHP, Node.js, .NET |
| Response Structure | JSON response formats |
| Exceptions | Error types and HTTP status codes |
| User | Authentication, profile, margins |
| Orders | Place, modify, cancel, retrieve orders |
| GTT | Good Till Triggered orders |
| Alerts | Price alerts and notifications |
| Portfolio | Holdings and positions |
| Market Quotes | Instruments, quotes, OHLC, LTP |
| WebSocket | Real-time streaming |
| Historical | Candle data |
| Postbacks | WebHooks for order updates |
| Mutual Funds | SIPs and MF orders |
| Margins | Margin calculation |
| Basket/Publisher | Offsite order execution |
| Apps | Mobile and desktop integration |

Source: https://kite.trade/docs/connect/v3/
