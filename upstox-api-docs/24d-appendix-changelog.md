# Changelog

Official log of Upstox API updates, new endpoints, deprecations, and breaking changes — newest first.

Source: https://upstox.com/developer/api-documentation/announcements

## September 4, 2026 — CAS Market Data

A new Full Market Quotes V3 API and an update to the Market Data Feed V3 WebSocket now lets you read live Closing Auction Session data — the indicative equilibrium price and quantity, the total and market imbalance quantities, the reference price, and CAS eligibility — plus each market segment's current closing auction and pre-open session status.

## August 11, 2026 — IPO Application APIs *(Beta)*

Four new IPO APIs are now available — apply for a mainboard or SME issue with up to three bids, list your applications with pagination, fetch a single application by its order ID, and cancel an application while the bidding window is still open.

## August 01, 2026 — Closing Auction Session (CAS) Support

Effective August 3, 2026, the Upstox API supports the exchange Closing Auction Session (CAS) — a new `cas_eligible` flag in the Instruments JSON and Instrument Search API identifies participating securities, and the Exchange Status API returns a `cas_eligible_status` object for CAS-eligible segments. Track the CAS status transitions to align your order flow, and note the F&O segment now closes at 3:40 PM IST.

## July 7, 2026 — Upstox Plugin Marketplace for Claude

The Upstox MCP server and Agent Skill are now installable from a single Claude plugin marketplace — run `/plugin marketplace add upstox/upstox-plugin-marketplace` , then install `upstox-mcp` (read-only account access) or `upstox-skill` (trading workflows). Now supported in Claude Code and the Claude Desktop and web app, with no config file or Node.js for the plugin path.

## June 6, 2026 — Analytics Token now Supports Portfolio & Trade APIs via Static IP

The Analytics Token — a single read-only token with 1-year validity — now unlocks account-specific APIs via Static IP, so you can analyze your portfolio, positions, holdings, orders, and profit & loss without daily re-authorization.

## June 6, 2026 — Payout Management APIs

New Payout Management APIs are available to initiate, modify, and cancel fund withdrawals via NEFT or IMPS, and check payout mode eligibility for your account.

## June 6, 2026 — Upstox Agent Skills Launch

The Upstox Agent Skill is now available — install it in Claude Code, Codex, or any SKILL.md-compatible agent to place orders, stream market data, and manage your portfolio across NSE, BSE, and MCX, built on the official upstox-python-sdk.

## May 29, 2026 — Smartlist APIs Launch

Three new Smartlist APIs are now available — Get Futures Smartlist, Get Options Smartlist, and Get MTF Smartlist — delivering curated, real-time ranked lists of F&O contracts and MTF-eligible stocks.

## May 23, 2026 — IPO API Launch

IPO APIs are now available — fetch a paginated list of IPOs by status and issue type, and retrieve detailed per-IPO data including price band, lot size, timeline, registrar info, and subscription figures.

## May 11, 2026 — Global Instruments Support

A new Global Instruments file is now available, providing instrument keys for major global indices and indicators — GIFT NIFTY, Dow Jones, S&P, FTSE 100, and more — for use with market quote and historical candle data APIs.

## May 11, 2026 — New Market Information APIs Launch

Six new Market Information APIs are now available — FII activity, DII activity, Open Interest, Change in OI, Max Pain, and Put-Call Ratio — providing institutional-grade market data for F&O analysis and trading tools.

## May 11, 2026 — Company Fundamentals API Launch

New Company Fundamentals APIs are available to retrieve financial statements, key ratios, shareholding patterns, corporate actions, and competitor data for any listed company by ISIN. The suite includes 8 endpoints: Company Profile, Balance Sheet, Cash Flow, Income Statement, Share Holdings, Key Ratios, Corporate Actions, and Competitors.

## May 4, 2026 — Payments API Launch

New Payments APIs are available to retrieve the pay-in and payout transactions, including amount, mode, status, bank name, and charge details.

## April 24, 2026 — Mutual Funds API Launch

New Mutual Fund APIs are available to retrieve the order book, order details, SIPs, and holdings.

## April 17, 2026 — Webhook URL Security Policy

All webhook URLs registered on the Upstox Developer Platform are validated against a security filter before an app can be created, protecting user accounts from dynamic DNS, phishing, malware, spam, and proxy bypass threats.

## April 17, 2026 — News API Launch

Introducing the News API — fetch news articles for specific instrument keys, your current positions, or your holdings portfolio with pagination support.

## April 10, 2026 — Get Fund and Margin V3 API

We have released the new Get Fund and Margin V3 API, offering a detailed balance breakdown including cash available, pledged margin, and unsettled profit components — without requiring a segment parameter.

## April 10, 2026 — Kill Switch API Launch

Introducing the Kill Switch API — two new endpoints to programmatically enable or disable specific trading segments, helping traders avoid impulsive decisions by temporarily halting activity in one or more segments.

## April 10, 2026 — Static IP Management APIs

Two new endpoints — GET and PUT `/user/ip` — are now available for reading and updating user-level static IP addresses required for algo trading compliance.

## April 10, 2026 — Important Updates – Algo Registration & Static IP Requirement *(Important)*

The Exchange has issued a significant circular dated [May 5, 2025](https://nsearchives.nseindia.com/content/circulars/INVG67858.pdf) , to enhance the safety of retail investors participating in Algo trading.

## March 20, 2026 — Analytics Token

Introducing the Analytics Token — a long-lived, read-only access token with 1-year validity for programmatic access to market data, holdings, positions, and historical records without the standard OAuth flow.

## March 17, 2026 — Search API for Instruments *(Beta)*

Search for instruments by query and apply filters like exchanges, segments, instrument types, expiry, or ATM offset.

## March 11, 2026 — Market Protection for Market and Stoploss Market Orders *(Beta)*

Optional `market_protection` parameter is now available when placing or modifying Market or Stoploss Market orders.

## December 6, 2025 — NSE's Pre-Open Session for Futures LIVE from 8 December

NSE's pre-open session for futures is now live from December 8, 2025. This session allows traders to place and modify orders before the regular trading hours begin, providing an opportunity to react to overnight news and market developments.

## August 22, 2025 — V2 Websocket Discontinued *(Discontinued)*

The Market Data Feeder V2 Websocket service will become discontinued on August 22, 2025, and will be completely stopped after this date. All users should migrate to the V3 Websocket service to avoid any disruption in market data streaming.

## July 19, 2025 — Fund and Margin API Response Change

Starting July 19, 2025, the [Fund and Margin API](https://upstox.com/developer/api-documentation/get-user-fund-margin) will return combined funds for both Equity and Commodity segments in the `equity` object. This change affects applications that process segment specific fund data separately.

## Jun 30, 2025 — Launch of Trailing Stop Loss order *(Beta)*

We've introduced Trailing Stop Loss functionality to our GTT Order API, allowing your stop-loss orders to automatically adjust as the market moves in your favor, providing dynamic risk management.

## June 30, 2025 — Deprecation of several V2 APIs *(Deprecated)*

We are deprecating several v2 APIs to streamline our offerings and encourage users to migrate to the corresponding v3 endpoints.

## Jun 20, 2025 — Support for MTF in GTT Order

We have enabled support for the Margin Trading Facility (MTF) product within the GTT order placement API. This enables the placement of GTT orders with margin funding directly through the API.

## May 13, 2025 — Expired Instruments APIs Launch *(Upstox Plus)*

We are rolling out new Expired Instruments APIs under the Upstox Plus plan. This suite of APIs provides access to historical data for expired instruments, offering the following features:

## May 13, 2025 — Websocket Plus Features *(Upstox Plus)*

We are rolling out new websocket features under the Upstox Plus plan, enhancing our v3 websocket with:

## Apr 17, 2025 — Enhanced Historical Candle Data APIs - V3 Launch

We're excited to introduce enhanced V3 versions of both standard [Intraday](https://upstox.com/developer/api-documentation/get-intra-day-candle-data) and [Historical](https://upstox.com/developer/api-documentation/get-historical-candle-data) Candle Data APIs with expanded intervals and improved flexibility. These APIs support customizable time units from `minutes` to `months` with flexible intervals, offering more granular control for technical analysis.

## Apr 17, 2025 — Market Quote V3 API

We have released the new Market Quote V3 APIs, which include additional features and enhancements based on user feedback.

## Apr 17, 2025 — Margin Intraday Square-off (MIS) File Now Available

We have provided **Margin Intraday Square-off (MIS) file** , which you can now download directly from the [Instruments Section](https://upstox.com/developer/api-documentation/instruments#mis-instruments) of our Developer Documentation.

## Apr 4, 2025 — Support for MTF Order

We have enabled the support for Margin Trading Facility (MTF) product in the order placement API. This enables placing orders with margin funding directly through the API.

## Feb 28, 2025 — Introduction of GTT Order API

A new GTT Order API has been introduced, allowing users to create, modify, and cancel Good Till Trigger (GTT) orders seamlessly.

## Feb 12, 2025 — Minor Update to Put/Call Option Chain API

A new field **pop** has been added to the **option_greeks** object of the Put/Call Option Chain API response.

## Jan 16, 2025 — Beta Launch of Access Token Flow for User

Beta release of an access token flow for an individual users. This feature empowers Initiators to effortlessly generate access tokens for their customers, ensuring a seamless and efficient trading experience.

## Jan 16, 2025 — Sandbox Mode for API Integration

We are bringing convenience to your API integration. Introducing sandbox mode to test integrations safely before going live.

## Jan 3, 2025 — Market Data Feeder V3 Launch & V2 Deprecation *(Important)*

The Market Data Feeder V3 has been launched, offering improved stability and deeper insights. **Feeder V2 will be deprecated by March 2, 2025** , with only the V3 version available starting March 3, 2025.

## Nov 11, 2024 — Beta Launch of Order API V3

We are excited to announce the beta release of enhanced version of Order API V3 to support the order slicing and latency information tracking.

## Oct 8, 2024 — Beta Launch of Highly Requested APIs

We are excited to announce the beta release of three highly requested APIs: Place Multi Order, Cancel All Open Orders, and Exit All Positions.

## Sep 10, 2024 — Deprecation of Fields in Market Data Feed

Several fields in the market data feed will be discontinued on **Oct 10, 2024** .

## Aug 30, 2024 — Update on ZERO brokerage via Upstox API *(Discontinued)*

Starting 31 August 2024, we will no longer offer zero-brokerage API trades. However, new Upstox API users from 1 September 2024 will be eligible for 90 days of zero brokerage.

## Jul 26, 2024 — Faster order execution via API

Order execution over APIs is now significantly faster. Use the new endpoint for place, modify, and cancel operations to take advantage of this improvement.

## Apr 25, 2024 — CSV Instruments File Deprecation Notice

The [CSV format](https://upstox.com/developer/api-documentation/instruments#csv-files) for the instruments file will soon be deprecated. We recommend users to transition to the [JSON version](https://upstox.com/developer/api-documentation/instruments#json-files) for improved functionality and support.

## Mar 7, 2024 — New URL and Simplified Headers

Upstox API now accessible at a new URL `https://api.upstox.com/v2` with simplified header requirements. Old and new URLs operational during transition. Migration advised.
