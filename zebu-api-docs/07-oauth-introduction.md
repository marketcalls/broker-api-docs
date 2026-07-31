# Introduction

> Source: <https://zebumyntapi.web.app/OAuth/>

> **OAuth 2.0 API Documentation**
>
> This documentation covers the OAuth 2.0 version of the Zebu APIs. All API requests require OAuth authentication using Bearer tokens.

## Overview

Zebu APIs are a comprehensive set of REST-based web services designed to provide seamless integration with trading and investment platforms. Built on robust infrastructure, these APIs enable developers to create feature-rich applications for order execution, portfolio management, market data streaming, and fund tracking across equities, derivatives, commodities, and currency segments.

The Zebu API suite offers a simplified interface to interact with complex order management and risk systems, making it easy for developers to build custom applications without worrying about the underlying complexity. All API endpoints follow REST principles with JSON-based request and response formats, ensuring platform independence and ease of integration.

## Key Features

- **Real-time Order Execution**: Place, modify, and cancel orders across multiple exchanges and segments
- **Portfolio Management**: Track holdings, positions, and profit & loss in real-time
- **Market Data Access**: Stream live quotes, market depth, and historical data
- **Fund Management**: View available margins, balances, and fund allocation
- **Order Book & Trade Book**: Access complete order history and executed trades
- **WebSocket Streaming**: Subscribe to real-time market feeds with low latency
- **Multi-segment Support**: Trade across NSE, BSE and MCX

## Base URL

All API requests should be prefixed with the base URL:

| Environment | URL |
| --- | --- |
| Production | `https://go.mynt.in` |
| Sandbox | `https://uat.mynt.in` |

## Getting Started

### Obtain API Credentials

Before you can start using Zebu APIs, you need to generate your API credentials (Client ID and Secret Key) from the MYNT application (Mobile/Web).

**Step 1: Login to MYNT**

1. Navigate to the MYNT web portal
2. Enter your Client ID
3. Complete authentication (Password + OTP/TOTP)

**Step 2: Access Profile Settings**

Click on the Profile Client ID button located in the top right corner of the navigation bar

**Step 3: Generate API Key**

1. Click on the API Key button
2. Configure your Redirect URL (the URL where users will be redirected after login)
3. Enter your Primary IP Address (mandatory)
4. Optionally, add a Secondary IP Address for backup
5. Click the Update button

> **Security Best Practices**
>
> - Never share your Secret Key publicly or commit it to version control system
> - Store credentials in environment variables or secure vaults
> - Rotate your Secret Key periodically
> - Use IP whitelisting to restrict API access

## OAuth 2.0 Flow

The OAuth 2.0 authentication process involves the following steps:

1. **Generate API Credentials**: Create Client ID and Secret Key in MYNT
2. **Redirect User to Login**: Direct users to the Zebu OAuth login page
3. **User Authorization**: User logs in and authorizes your application
4. **Receive Authorization Code**: Your application receives an authorization code
5. **Exchange Code for Token**: Exchange the authorization code for an access token
6. **Make API Calls**: Use the access token to make authenticated API requests

For detailed OAuth implementation, see the [Authentication](08-oauth-authentication.md) section.
