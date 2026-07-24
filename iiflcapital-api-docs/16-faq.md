# FAQs

**What are IIFL Markets Trading APIs?**
They let individual traders and fintech platforms connect directly to IIFL's broker systems for order placement, market data retrieval, and portfolio management.

**Is there a cost to use the APIs?**
No — free for individual traders, developers, and platforms.

**How do I get access?**
IIFL Capital clients log in to the developer portal with their trading account credentials, create an application, and start using the APIs immediately. Fintech platforms register on the portal and go through IIFL's review/approval process.

**How does client login work?**
Follow the [Login Flow](03-user.md#login-flow) steps; a video walkthrough is also available.

**Do I need to log in daily, and is a new session token generated each time?**
Yes — a fresh login is required every trading day, generating a new unique session token.

**How does authentication work?**
After login, a session token (`userSession`) is generated and must be sent as a Bearer token in the `Authorization` header of every subsequent request.

**What do the `status`/`message` fields in responses mean?**
See [Request and Response Structure](02-request-response-structure.md).

**Can I convert MIS (intraday) trades to CNC (delivery) or vice versa via the API?**
No — product conversion between MIS and CNC/NRML isn't supported through the API; use the IIFL Markets mobile app instead.

**Where can I get real-time market data, and can I use third-party sources?**
Via the [Market Data APIs](09-market-data-apis.md) and the Bridge package, or via authorized third-party data vendors.

**Is the Bridge package mandatory for the Market Data Stream?**
Yes — it provides the pre-built functions and sample implementations needed to consume the [binary streaming events](08-market-data-stream.md).

**What languages is the Bridge package available in?**
Multiple; check the developer portal for the current list, or request a language via your RM/POC if yours is missing.

**How do I get the full list of tradable instruments?**
The [Instrument Details](01-introduction.md#instrument-details) CSV/JSON files provide the complete, segment-wise instrument master.
