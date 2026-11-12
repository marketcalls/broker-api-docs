# FAQ

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/FAQ

Frequently asked questions from the MOFSL Trading API documentation portal (94 questions).

## Contents

- [Login & Auth](#login-auth) — 9 questions
- [Orders](#orders) — 9 questions
- [Tokens & Keys](#tokens-keys) — 6 questions
- [Endpoints & URLs](#endpoints-urls) — 8 questions
- [Vendors & Partners](#vendors-partners) — 12 questions
- [Errors & Troubleshooting](#errors-troubleshooting) — 8 questions
- [Static IP & Regulatory](#static-ip-regulatory) — 32 questions
- [OPS Limit](#ops-limit) — 10 questions

## Login & Auth

### Q1. Do we need to re-login every day?

Yes, you need to login every day. Every time you start the application, MO API maintains a session token for **24 hours OR until logout is called** — whichever is earlier.

### Q2. Will there be a unique token for each login?

Yes, there will be a **unique session token** generated for each login.

### Q3. What are tokens?

A token is generated only after a valid user login and is valid only for a defined period of time, after which it becomes invalid/expired. For any API call other than login, you need to provide the **authentication token in the request header** to receive a response.

### Q4. Do I need to login to MO Investor / Orion Lite if logged in to API?

Both login sessions are maintained **separately**. If you are logged in to the API, you can also log in to Orion Lite if you want — but it is not mandatory.

### Q5. Will my MO Investor and API login credentials differ?

No. You can use the **same login credentials** for both MO Investor and the API.

### Q8. What is MO Trading API?

Trading APIs allow you to **integrate your own trading system** with the MO Trading Platform for placing orders and accessing other account information programmatically.

### Q34. What parameters need to be entered in 2FA?

**2FA** accepts either of the following:

- **PAN** — in capital letters
- **Date of Birth** — in `dd/mm/yyyy` format

### Q37. What needs to be verified in Header Parameters?

A sample is mentioned in the API documentation where all the required **Header Parameters** and their formats are detailed. Please refer to the *Header Parameters* section of the API Documentation on the developer portal.

### Q49. How can a retail user activate their Client ID for live trading under the new policy?

Once retail users **agree to the consent form** and generate the API key, it will **activate automatically**. No separate email or manual process is required for retail client activation.

## Orders

### Q6. What order functions does the API support?

1. Place Order
2. Modify Order
3. Cancel Order
4. Order Book
5. Order History
6. Index LTP Data
7. Trade Book
8. Net Positions

### Q7. What product types does the API support?

1. **Normal**
2. **Delivery**
3. **Value Plus** (Intraday)

### Q10. What do NRML and Value Plus product types mean?

**NRML (Normal):** You can carry forward positions to the next trading day. This is the product type used for overnight F&O positions.

**Value Plus:** Stands for Margin Intraday Square Off (MIS). The user must compulsorily square off all positions before the end of the trading session. Referred to as "Value Plus" in MO API (equivalent to "Intraday" in Q7).

### Q25. What are the possible order statuses after executing an order?

The following order statuses can be received:

```text
Unknown / Sent / Confirm / Cancel / Partial / Traded / Rejected / Error
```

### Q44. Can we place Bulk Orders with a Dealer Code? Is there a separate API for this?

There is **no separate API** for bulk orders.

### Q46. What exchange segments are supported in Open API?

- **NSE:** CM (Cash Market) / CD (Currency Derivatives) / FO (Futures & Options)
- **BSE:** CD (Currency Derivatives) / CM (Cash Market)
- **MCX**
- **NCDEX**

### Q47. What product type should be used for intraday orders?

**Value Plus** should be used as the product type for intraday orders.

### Q50. Up to what depth is the Order Book visible on a custom platform built using the API?

The Order Book will show **all data based on the orders placed** through your API integration. There is no artificial depth limit — all orders placed via your API key will be visible.

### Q51. What order types does the API support?

- **Limit** — Allowed
- **SL (Stop Loss — Limit)** — Allowed
- **SL-M (Stop Loss — Market)** — Allowed
- **Market** — Not permitted via API from 1st April 2026 as per the SEBI Retail Algo Framework

All API orders must specify a price. Market Order requests sent via API will be rejected at the exchange level.

## Tokens & Keys

### Q14. How do I generate the API key?

You need to **log in to the API portal** at [invest.motilaloswal.com/moapi/](https://invest.motilaloswal.com/moapi/) to create and manage your API key.

### Q21. Where can I get the TOTP Secret Key?

The TOTP Secret Key (32-character unique identifier) is available on the **dashboard of the API portal** after logging in.

### Q29. Can I use multiple API keys for trading?

**Yes**, you can use multiple API keys for trading.

### Q30. How many API keys can I create for Open API?

You can create **multiple API keys** in Open API.

### Q33. What is the Unique Identifier number / TOTP?

The Unique Identifier / TOTP secret key is available on the **Motilal Oswal API portal dashboard** after logging in.

### Q42. What is the Time to Live (TTL) or expiration period of the Auth Token?

The Auth Token is valid for **up to 24 hours**, OR until logout is called — whichever is earlier. Additionally, all tokens expire at **6:00 AM daily** as a mandatory exchange compliance reset, regardless of when they were generated. A fresh login and token generation is required each trading day.

## Endpoints & URLs

### Q17. What are the endpoints for the Live and UAT API platforms?

ProductionLogin endpoint:

```text
https://invest.motilaloswal.com/OpenAPI/Login.aspx?apikey={apikey}
```

UATLogin endpoint:

```text
http://uattrade.motilaloswal.com:83/OpenAPI/Login.aspx?apikey={apikey}
```

### Q19. Where can I get LTP data for Live and UAT traded via API?

Production

```text
https://openapi.motilaloswal.com/rest/report/v1/getindexltpdata
```

UAT

```text
https://uatopenapi.motilaloswal.com/rest/report/v1/getindexltpdata
```

### Q22. Where can I get Margin details?

Production

```text
https://openapi.motilaloswal.com/rest/report/v1/getreportmargindetail
```

UAT

```text
https://uatopenapi.motilaloswal.com/rest/report/v1/getreportmargindetail
```

### Q23. Can I get Scrip / Instrument data through the API?

Yes. You can get scrip/instrument details in the following formats:

Production

```text
https://openapi.motilaloswal.com/getscripmastercsv?name=NSEFO
```

UAT

```text
https://uatopenapi.motilaloswal.com/getscripmastercsv?name=NSEFO
```

### Q26. What is the WebSocket URL for Live and UAT?

Live

```text
wss://openapi.motilaloswal.com/ws
```

UAT

```text
wss://uatopenapi.motilaloswal.com/ws
```

### Q27. How do I get the Webhook URL in API?

Production

```text
https://openapi.motilaloswal.com/webhook
```

UAT

```text
https://uatopenapi.motilaloswal.com/webhook
```

### Q28. Where can I get Index data?

Production

```text
https://openapi.motilaloswal.com/getindexdatacsv?name=NSE
```

UAT

```text
https://uatopenapi.motilaloswal.com/getindexdatacsv?name=NSE
```

### Q41. Does Motilal Oswal provide a Fund API endpoint?

**No.** Motilal Oswal does not provide a Fund API endpoint as part of its API services.

## Vendors & Partners

### Q13. What kinds of platforms are available for Open API?

There are 2 platform types:

- **Vendor-based:** Clients using a vendor-based application must provide the vendor name for further processing.
- **Self-based:** Clients using a self-built application are requested to provide same-day UAT order logs once the application has been tested in UAT.

### Q15. Does a vendor need to send an email for Vendor API activation?

Yes, for Vendor API activation, you need to send an email to [tradingapi@motilaloswal.com](mailto:tradingapi@motilaloswal.com) in the following format:

```text
Live Enable JSON API
Client ID – ANC001
AppName = TestApp
Vendor Name = Xyz
API Key = abcdefgho
```

### Q16. Does the client need to send an email for Client API activation?

**No.** Client API will **activate automatically** after the API key is created in the portal. No email is required.

### Q18. What programming languages does the API support?

1. C# / .NET
2. Python
3. Node.js
4. Java

### Q20. Is UAT log mandatory for activating a Client ID?

**Yes**, UAT order logs are mandatory for activating Vendor and Dealer APIs. Retail clients using a self-built application must also send an email to the Trading API team for activation.

Note: Retail clients who generate an API key directly on the portal (without a self-built application) are activated automatically as per Q17.

### Q31. How does a vendor register itself with the Motilal Oswal platform?

We require details of the Vendor along with the **undertaking consent form** (duly signed) and the following information:

- Contact Name
- Phone Number
- Email ID
- Redirect URL
- Callback URL

### Q32. Is Consent compulsory before using Open API?

**Yes**, consent is mandatory before proceeding to generate an API key.

### Q35. What is Vendor Tag Info?

**For Vendors:** Vendor Tag Info is the short name of the vendor (e.g. `ABC`), which needs to be added in the vendor field while building the strategy.

**For Clients:** Vendor Tag Info is the client code (e.g. `abc123`), which needs to be added in the vendor field while building the strategy.

### Q38. What is the difference between Callback URL and Redirect URL?

**Callback URL:** A server-to-server POST response sent to a pre-defined HTTPS URL with full transaction/trade information once the trade process concludes — regardless of whether the customer cancels, completes, or fails the trade.

**Redirect URL:** The location where the authorization server sends the user after successful authorization. A redirect URI, or reply URL, is where the authorization code or access token is delivered after the app is successfully authorized.

### Q39. How do I implement WebSocket into my algo platform?

A sample implementation with all required parameters for WebSocket integration is mentioned in the **WebSocket Broadcast** section of the MO API Documentation on the developer portal.

### Q43. Can a connection using DTC protocol be established using the MO API?

The MO API works with **HTTPS protocol**. DTC protocol-based connections are not supported.

### Q45. What is the procedure to become a partner (third-party vendor) for Algo trading?

To become a partner or integrate as a vendor with Motilal Oswal:

- Sign the **Undertaking/Consent Form**
- Provide the details in the format shared by the Trading API team
- Submit the required information (Contact Name, Phone Number, Email ID, Redirect URL, Callback URL)

Email: [tradingapi@motilaloswal.com](mailto:tradingapi@motilaloswal.com)

## Errors & Troubleshooting

### Q9. I am facing an "invalid session" or "unrecognized token / session not found" error.

This happens because you are not sending **a valid token received in the login response** in all subsequent message headers. To resolve:

- Call logout or force-disconnect the application
- Re-login to fetch a valid token
- Monitor token usage by adding sufficient logs to your application

### Q11. I am getting "User data not found" error. What does this mean?

You are either providing an **invalid User ID** or an **invalid API Key**. Please verify both and try again.

### Q12. I am getting "Invalid Credentials" error. What does this mean?

You are either providing an **invalid User ID** or an **invalid password**. Double-check your credentials and ensure the User ID is in capital letters.

### Q24. What is the meaning of error codes while executing a strategy?

All details of error codes are mentioned in the **API Documentation — Error Codes and Description** section available on the developer portal.

### Q36. What if a DNS issue persists?

Change the global DNS IP and flush the DNS from the command prompt using the following command:

```text
ipconfig /flushdns
```

### Q40. I'm getting "Insufficient Margin" in the UAT environment. How do I fix it?

Insufficient margin errors are common in the UAT/testing environment. You need to **request margin assignment on the UAT environment** from the Trading API team at [tradingapi@motilaloswal.com](mailto:tradingapi@motilaloswal.com).

### Q48. What does the error "Not a valid account number" mean?

This error means your **PAN is not linked with your Aadhaar card**. Please ensure your PAN-Aadhaar linking is complete before retrying.

### Q52. I am getting the error "Invalid User ID or Password". How do I fix it?

Please check the following:

- Enter your User ID in **CAPITAL LETTERS**
- Date of Birth must be in **DD/MM/YYYY** format
- If using PAN for 2FA, enter the PAN in **CAPITAL LETTERS**
- The 2FA field accepts either **PAN No.** or **Date of Birth**

## Static IP & Regulatory

### Q53. What is a Static IP?

A **static IP** is a fixed, non-changing IP address assigned to your internet connection by your Internet Service Provider (ISP). Unlike a dynamic IP (which changes every time you connect), a static IP remains the same permanently — making it identifiable and registerable with MO API for secure, compliant trading.

### Q54. What is the difference between a Static IP and a Dynamic IP?

**Static IP:** A permanent, fixed internet address that does not change. It is assigned by your ISP and stays the same every time you connect. Suitable for API-based trading as it can be whitelisted with the broker.

**Dynamic IP:** An address that changes each time you connect to the internet or restart your router. Dynamic IPs cannot be used for API trading under the new SEBI regulations as they cannot be reliably whitelisted.

### Q55. Is it mandatory to provide a Static IP for API-based trading?

**Yes.** As per the SEBI Retail Algo Framework (effective 1st April 2026), providing a registered static IP address is **mandatory** for all clients using MO API for order placement. API requests originating from an unregistered or dynamic IP will be rejected.

### Q56. Is a Static IP mandatory for retail clients?

**Yes.** The static IP requirement applies to all API users including retail clients. There are no exemptions based on account size, trading volume, or client type. All clients placing orders via MO API must register a static IP.

### Q57. What is the purpose of a Static IP address in algo trading?

A static IP serves two key regulatory purposes in algo trading:

- **Identification & Accountability:** It allows the exchange and broker to trace every API order back to a specific, verified internet source — creating a clear audit trail as required by SEBI.
- **Security:** By whitelisting only approved IPs, it prevents unauthorised access to the trading API from unknown or unverified locations.

### Q58. Who provides a Static IP?

Static IPs are provided by your **Internet Service Provider (ISP)**. You can request a static IP as an add-on to your existing broadband or leased-line connection. Popular options include:

- Residential broadband providers (Jio Fiber, Airtel, BSNL, ACT, etc.) — available as a paid upgrade
- Cloud/VPS providers (AWS, Google Cloud, Azure, DigitalOcean, Hetzner) — where server IPs are static by default
- Dedicated server providers offering fixed IP addresses

### Q59. How do I register my Static IP with MO API?

1. Log in to the MO API Developer Portal at [invest.motilaloswal.com/moapi/](https://invest.motilaloswal.com/moapi/)
2. Navigate to **My APIs** and select your application
3. Go to the **IP Whitelist / Security Settings** section
4. Enter your static IP address and save
5. The IP will be activated and validated within the portal

Only requests originating from this registered IP will be accepted for API order placement.

### Q60. How many Static IPs can I register?

You can register **exactly 2 Static IPs** per application — a **Primary IP** and a **Secondary IP**.

| IP Type | Mandatory? | Purpose |
| --- | --- | --- |
| Primary IP | ✅ Mandatory | The main registered IP from which all API orders are placed. Required for SEBI compliance. All API requests must originate from this IP. |
| Secondary IP | ⚠ Optional | A backup/failover IP. Used if the primary connection is unavailable. Recommended for uninterrupted live trading but not compulsory. |

Both IPs must be **static** — dynamic IPs are not accepted for either slot. Register both in your application's IP Whitelist settings in the MO API Developer Portal.

### Q61. What is a Secondary IP and how does it help?

A **Secondary IP** is an additional backup static IP registered alongside your primary IP. It acts as a failover — if your primary connection is unavailable, your algo can continue operating from the secondary IP without disruption. Registering a secondary IP is recommended for production strategies to ensure continuity.

### Q62. Is it mandatory to provide a Secondary IP address?

No, a secondary IP is **not mandatory** — it is optional but recommended for redundancy and uninterrupted trading. Only the primary static IP is required for compliance.

### Q63. What is the Primary IP address and how do I check it?

Your primary IP is the public IP address of the machine or server from which your API calls are made. To check your current public IP:

- Visit [whatismyip.com](https://whatismyip.com) or [ipinfo.io](https://ipinfo.io) from the machine running your algo
- Or run `curl ifconfig.me` in a terminal

This is the IP you need to register in the MO API portal. Confirm it is static (does not change after router restarts) before registering it.

### Q64. Can I update (change) my Static IP if needed?

**Yes.** You can update your registered static IP through the MO API Developer Portal. Log in, navigate to your application's IP Whitelist settings, remove the old IP, and add the new one. The change takes effect within a few minutes.

Ensure your new IP is active and confirmed as static before removing the old one to avoid any gap in API access.

### Q65. Can family members share a Static IP?

If family members are trading from the same internet connection (e.g. same home network with one static IP from the ISP), they may share that IP address. However, each individual trading account must separately register the IP in their respective MO API application settings. Contact MO API support to confirm the current policy on shared household IPs.

### Q66. Can we use the unique Static IP from any location or device?

**No.** A static IP is tied to a specific internet connection or server — it is not portable across locations or devices. If you move to a different network or connect from a different location, your public IP will be different from the registered static IP, and your API requests will be blocked. For portability, use a cloud VPS with a static IP and connect to it remotely from any device.

### Q67. Can I use a VPN to generate a Static IP?

Some VPN providers offer dedicated static IP addresses as a paid feature. However, using a VPN-provided static IP may introduce latency and may not be fully compliant with exchange requirements. It is strongly recommended to use a static IP directly from your ISP or from a cloud/VPS provider for API trading rather than relying on a VPN.

### Q68. Can I use a Static IP with Wi-Fi?

**Yes**, as long as your broadband router has been assigned a static IP by your ISP. The Wi-Fi network in your home or office uses that same external (public) static IP regardless of whether your device is connected via Wi-Fi or ethernet cable. The static IP is a property of your ISP connection, not of the device's network interface.

### Q69. What happens if I change networks? How does a Static IP work?

A static IP is bound to a specific ISP connection or server. If you change networks (e.g. switch from home broadband to a mobile hotspot, or connect from a different office), your public IP will change and will no longer match your registered static IP. API requests from the new IP will be **blocked**.

For this reason, algo strategies should always run from a fixed, dedicated connection (home broadband with static IP or a cloud VPS) rather than from mobile data or changing networks.

### Q70. If I change my Internet Service Provider, will my registered Static IP still work?

**No.** When you change your ISP, your static IP address will change — it is assigned by the ISP. You must obtain a new static IP from your new ISP and update it in the MO API Developer Portal before resuming API trading. Plan this transition in advance to minimise downtime.

### Q71. Do I need to update the IP if I change my router?

In most cases, **no** — your static IP is assigned to your ISP account/line, not to the physical router. Replacing the router hardware should not change your static IP. However, if you also change your broadband plan or switch ISPs at the same time, the IP may change. Verify your public IP after any router change to confirm it remains the same before resuming API trading.

### Q72. How often do I need to renew a Static IP?

Static IPs from ISPs are generally active for as long as your subscription remains active — there is no separate renewal process for the IP itself. For cloud/VPS providers, the static IP is retained as long as you keep the server running and the IP reserved. You do not need to periodically renew the IP registration in the MO API portal unless you change providers or IPs.

### Q73. Does MO API log my Static IP during trading?

**Yes.** As required under the SEBI Retail Algo Framework, all API order requests are logged with the originating IP address. This creates a traceable audit trail linking every order to a verified, registered source. This logging is a regulatory requirement and applies to all API users.

### Q74. Do I need different IPs for multiple strategies?

**No.** You do not need a separate static IP for each strategy. Multiple strategies running from the same server or connection will all operate under the same registered static IP. What matters is that all API requests originate from a whitelisted IP — not that each strategy has a unique IP.

### Q75. What happens if I try to place more than 10 Orders Per Second (OPS)?

The maximum permitted OPS for retail API users is **10 Orders Per Second**. If your application exceeds this threshold:

- Excess orders will be **throttled** (delayed) or **rejected** by the system
- Repeated violation may result in temporary API restrictions or a requirement to register the strategy

If your strategy genuinely requires more than 10 OPS, you must register it as an algo strategy with MO API and obtain exchange approval for a higher OPS limit.

### Q76. How many orders per second are allowed before a strategy has to be classified as an algo?

Under the SEBI Retail Algo Framework, **any strategy exceeding 10 Orders Per Second (OPS)** must be formally classified and registered as an algorithmic trading strategy with the broker and approved by the exchange. Below 10 OPS, the strategy can operate under the standard retail API framework without requiring algo registration.

### Q77. What happens if my algo exceeds the OPS threshold?

If your algo consistently exceeds the 10 OPS threshold without being registered as an approved algo strategy:

- Orders above the threshold will be rejected or throttled at the broker/exchange level
- The API access may be restricted or suspended
- You may be required to register the strategy before further high-OPS trading is permitted

Contact MO API support immediately if your strategy requires high OPS to initiate the Strategy Registration process.

### Q78. What are the changes mentioned in the SEBI circular on API trading?

The SEBI Retail Algo Framework circular introduces the following key requirements for all API-based retail trading:

- **All API orders are classified as Algo Orders** by the exchange
- **Market Orders are prohibited** via API — only Limit, SL, and SL-M orders are permitted
- **Static IP registration is mandatory** — all API requests must originate from a whitelisted static IP
- **OPS capped at 10** for general retail users; higher OPS requires strategy registration and exchange approval
- **Mandatory headers** must be passed with every API request
- **OAuth authentication** is required for all API sessions

All changes are effective **1st April 2026**.

### Q79. What are the objectives of the new API regulations?

The new SEBI regulations for API trading aim to:

- Bring **transparency and accountability** to retail algorithmic trading
- Ensure every API order can be traced to a **verified, identifiable source**
- Reduce systemic risk from unregulated high-frequency retail order flow
- Align retail API trading standards with the existing institutional algo framework
- Protect the integrity of the exchange's order matching system

### Q80. Who will be covered under the new API regulations?

The new SEBI API regulations apply to **all retail clients** using any broker's trading API, including MO API. This covers:

- Individual retail traders using the API directly
- Third-party algo platforms and vendors integrated with MO API
- Developers building custom trading applications on MO API

There are no exemptions based on account type, trading volume, or user category.

### Q81. Where do I find the SEBI circular on the regulatory update for API trading?

The SEBI circular on the Retail Algo Framework is available on the official SEBI website at [www.sebi.gov.in](https://www.sebi.gov.in). The circular is also referenced in MO API's official communications and in the compliance section of the developer portal. For the exact circular reference and document, visit the SEBI website and search for "Retail Algo" or "API Trading Framework".

### Q82. Is there any change to the MO API code due to the Static IP requirement?

The core API endpoints and request structure remain unchanged. However, you may need to:

- Ensure your API requests include all **mandatory headers** (including source IP headers where required)
- Ensure your authentication uses the **OAuth flow** — this is mandatory as per SEBI circular
- Remove any **Market Order** calls and replace them with Limit Orders

No changes are needed specifically because of the static IP registration — that is a portal configuration step, not a code change. Refer to the MO API Documentation for the full list of updated mandatory headers.

### Q83. Do I need to include the Static IP in the MO API request header?

The static IP itself does not need to be manually passed in the request header in most cases — it is validated at the network level based on the originating IP of the request. However, certain mandatory headers may include a `x-source-ip` field that should reflect your registered static IP. Refer to the **Header Parameters** section of the MO API Documentation for the exact required headers and their formats.

### Q84. Do I need a technical person to set up the Static IP?

For most users, no technical expertise is required:

- **ISP static IP:** Simply call your ISP, request a static IP upgrade, and they will provision it. Once active, your public IP will not change. Register it in the MO API portal yourself.
- **Cloud VPS:** Basic cloud setup requires some technical familiarity, but cloud providers offer step-by-step guides. If you are not comfortable with this, a technical person or IT support can help set it up once.

For any assistance with portal configuration, contact MO API support at [tradingapi@motilaloswal.com](mailto:tradingapi@motilaloswal.com).

## OPS Limit

### Q85. What is OPS and what does the SEBI circular say about it?

**OPS** stands for **Orders Per Second** — the number of orders your API application sends to the exchange within a single second.

As per **SEBI Circular SEBI/HO/MIRSD/MIRSD-PoD/P/2025/0000013 dated February 4, 2025**, a Threshold OPS (TOPS) of **10 orders per second per exchange/segment** has been established for retail API users. This threshold determines whether a client's trading activity is classified as standard API trading or algorithmic (algo) trading requiring formal registration.

The threshold is applied on a **calendar clock second basis** and may be revised by stock exchanges after due notice to the market.

### Q86. What is the OPS limit for MO API users?

The maximum permitted OPS for retail MO API users is **10 Orders Per Second per exchange/segment**. This is the threshold set by SEBI and operationalised by NSE/BSE.

| OPS Level | Classification | Registration Required? |
| --- | --- | --- |
| Below 10 OPS | Regular API / Tech-Savvy Retail User | No algo registration needed — exchange issues a generic Algo ID for tagging |
| 10 OPS or above | Algorithmic Trading | Mandatory — strategy must be registered with broker and approved by exchange |

Note: MO API (as broker) may set its own OPS limit at the client level, which may be lower than 10 — but cannot exceed the exchange-prescribed threshold of 10 OPS.

### Q87. What happens if I exceed 10 OPS via MO API?

If your API application sends more than 10 orders per second without a registered and exchange-approved algo strategy:

- Orders exceeding the threshold will be **rejected or throttled** by MO API / the exchange in real time
- The broker is required by SEBI to implement systems to **detect and categorise** algos crossing the OPS threshold
- Repeated violations may result in **temporary suspension of API access**
- The activity may be flagged for **regulatory review** under the SEBI Algo Framework

Using multiple API keys to circumvent the OPS limit is **not permitted** — SEBI circular clarifies that only one API key per user can run an unregistered algo below 10 OPS.

### Q88. How do I get approval to trade above 10 OPS?

To trade above the 10 OPS threshold, your strategy must be formally registered as an algorithmic strategy. The process is:

1. Submit your strategy details to **MO API / Motilal Oswal** for internal review
2. MO API registers the strategy with the relevant **exchange (NSE/BSE/MCX)** for approval
3. The exchange reviews and, upon approval, issues a **unique Algo ID** for your strategy
4. All orders placed under this strategy must be **tagged with the Algo ID**
5. Any changes to the approved strategy require a **fresh approval cycle**

Contact MO API support at [tradingapi@motilaloswal.com](mailto:tradingapi@motilaloswal.com) to initiate the Strategy Registration process well in advance of the deadline.

### Q89. What is an Algo ID and is it mandatory for all API orders?

An **Algo ID** is a unique identifier issued by the exchange (NSE/BSE) that must be tagged to every algo order. As per the SEBI circular:

- **All algo orders — both below and above 10 OPS** — must carry an exchange-issued Algo ID to establish a complete audit trail
- For orders **below 10 OPS**: the exchange issues a **generic Algo ID** — no individual strategy registration is required
- For orders **above 10 OPS**: a **strategy-specific Algo ID** is issued only after formal registration and exchange approval

MO API handles Algo ID tagging as part of the API infrastructure in coordination with the exchange. Refer to the MO API Developer Portal for the latest implementation details on Algo ID tagging in your order requests.

### Q90. What is the difference between a White Box and Black Box algo under SEBI rules?

| Type | Description | Regulatory Requirement |
| --- | --- | --- |
| White Box (Execution Algo) | Logic is fully transparent and disclosed. E.g. VWAP, TWAP, moving average crossover, momentum strategies. | Exchange registration required above 10 OPS. No SEBI RA license needed. |
| Black Box (Advisory / Signal Algo) | Proprietary logic — the internal rules are not disclosed to the end user. | Provider must hold a SEBI Research Analyst (RA) licence and periodically disclose performance metrics and methodology. |

Most self-built strategies used by retail traders via MO API fall under the **White Box** category and do not require SEBI RA registration.

### Q91. Does the OPS limit apply per exchange or in total across all exchanges?

The OPS limit of **10 orders per second applies per exchange/segment** — not as a combined total across all exchanges. This means:

- You can place up to 10 OPS on **NSE** and simultaneously up to 10 OPS on **BSE** without triggering the registration requirement on either
- The threshold is evaluated independently for each exchange/segment (NSE CM, NSE FO, BSE CM, MCX, etc.)
- The threshold is measured on a **calendar clock second** basis

### Q92. Can I use multiple API keys to bypass the 10 OPS limit?

The **10 Orders Per Second (OPS) threshold** for unregistered algorithms is applicable at the **client level (UCC — Unique Client Code)**, and not at the API key level.

As per the guidelines issued by the Securities and Exchange Board of India, all API activity mapped to a single client is **aggregated and evaluated collectively**. This means:

- The **total order rate across all API keys linked to a UCC** must remain within the 10 OPS limit for unregistered algos
- The limit **cannot be applied or interpreted individually per API key** — splitting orders across multiple keys does not reset or multiply the threshold

### Q93. Is there a daily order limit in addition to the OPS limit?

The SEBI circular and exchange circulars define OPS (Orders Per Second) as the primary threshold. Individual brokers may additionally impose their own **daily order limits** at the client level as part of their risk management framework — these are broker-set limits and may vary.

For MO API's current daily order limits and any broker-level restrictions, refer to the **MO API Developer Portal** or contact MO API support at [tradingapi@motilaloswal.com](mailto:tradingapi@motilaloswal.com).

### Q94. Do all API sessions need to be logged out before the next trading day?

**Yes.** As per the SEBI/NSE circular requirements, all API sessions must be terminated before the start of the next trading day's pre-open session. For MO API specifically:

- The **Auth Token expires daily at 6:00 AM** — enforcing a mandatory daily session reset
- A fresh login and token generation is required each trading day, recommended between **8:30 AM and 8:55 AM**
- This ensures session continuity, security, and compliance with the exchange mandate for daily re-authentication
