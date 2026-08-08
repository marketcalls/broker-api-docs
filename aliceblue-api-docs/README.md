# Aliceblue ANT API Documentation

Unofficial Markdown conversion of the official Aliceblue ANT API (v2) documentation.

> Source: https://v2api.aliceblueonline.com/

## Contents

1. [Introduction](01-introduction.md) — https://v2api.aliceblueonline.com/
2. [Authentication](02-authentication.md) — https://v2api.aliceblueonline.com/Authentication/
3. [Portfolio](03-portfolio.md) — https://v2api.aliceblueonline.com/portfolio/
4. [Orders](04-orders-management.md) — https://v2api.aliceblueonline.com/orders%20Management/
5. [GTT Order](05-gtt-order.md) — https://v2api.aliceblueonline.com/orders%20GTT/
6. [Option Chain](06-option-chain.md) — https://v2api.aliceblueonline.com/Option%20Chain/
7. [Funds](07-funds.md) — https://v2api.aliceblueonline.com/Funds/
8. [Profile](08-profile.md) — https://v2api.aliceblueonline.com/Profile/
9. [Vendors](09-vendors.md) — https://v2api.aliceblueonline.com/Vendors/
10. [Order Updates](10-webhooks.md) — https://v2api.aliceblueonline.com/Webhooks/
11. [Websocket](11-websocket.md) — https://v2api.aliceblueonline.com/Websocket/
12. [Contract Master](12-contract-master.md) — https://v2api.aliceblueonline.com/Contract%20Master/
13. [Historical Data](13-historical-data.md) — https://v2api.aliceblueonline.com/Historical%20Data/
14. [HTML 5 Buttons](14-html5-button.md) — https://v2api.aliceblueonline.com/HTML%205%20Button/
15. [Error Code](15-error-code.md) — https://v2api.aliceblueonline.com/Error%20Code/
16. [Appendix](16-appendix.md) — https://v2api.aliceblueonline.com/Appendix/
17. [Rates Limits](17-rate-limits.md) — https://v2api.aliceblueonline.com/Rates%20Limits/
18. [Reference Libraries](18-reference-libraries.md) — https://v2api.aliceblueonline.com/Reference%20Libraries/
19. [Postman Scripts](19-postman-scripts.md) — https://v2api.aliceblueonline.com/Postman%20Scrips/
20. [Terms & Conditions](20-terms-and-conditions.md) — https://v2api.aliceblueonline.com/Terms%26conditions/

## Base URL

```
https://a3.aliceblueonline.com
```

## Notes

- The BASE URL, endpoint paths, and payload JSON keys are **case-sensitive**. Use the exact format shown in the docs.
- Session creation goes through the vendor SSO flow (`/open-api/od/v1/vendor/getUserDetails`) using a SHA-256 checksum of `userId + authCode + apiSecret`.
- Rate limits: order placement/modification/cancellation is unlimited; all other endpoints are capped at 1800 requests per 15 minutes.
- Example tokens / session IDs in the response samples are illustrative values copied verbatim from the official docs — they are not live credentials.
