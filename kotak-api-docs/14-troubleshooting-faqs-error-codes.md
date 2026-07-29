# Troubleshooting — FAQs / Error Codes

## Tokens & Authentication

**Q1. What is an access token, and what's new about it?**
The access token now comes from Neo app/web → Invest → TradeAPI → API Dashboard (not via `/oauth2/token`). Send it as a plain string (no `Bearer`). Resetting it immediately invalidates all sessions.

**Q2. What happens if I reset the token?**
All active sessions break instantly. Re-login (TOTP → MPIN validate) to obtain a new session token (`Auth`) and session sid (`sid`).

**Q3. Demystify tokens: access token, view token, session token (trade token), view sid, session sid, neo-fin-key**

- **Access Token** — From Neo dashboard. Used for login APIs and Quotes/Scripmaster.
- **View Token + View SID** — Returned by `/login/1.0/tradeApiLogin` (TOTP step).
- **Session Token (aka Trade Token) + Session SID** — Returned by `/login/1.0/tradeApiValidate` (MPIN step). Use these as `Auth` and `sid` headers for all post-login APIs.
- **neo-fin-key** — Always send `neotradeapi` (static) except in Quotes/Scripmaster, where it is not required.

## Login & baseUrl

**Q4. What are the login endpoints (fixed)?**

- TOTP Login: `https://mis.kotaksecurities.com/login/1.0/tradeApiLogin`
- MPIN Validate: `https://mis.kotaksecurities.com/login/1.0/tradeApiValidate` → returns `baseUrl`, session token (header `Auth`) and session sid (header `sid`).

**Q5. Is baseUrl static or dynamic?**
It's stable for the day and even after that rarely changes. Always capture it after MPIN validate and use it for that session.

**Q6. Which APIs need baseUrl?**
All post-login APIs: Orders, Reports, Portfolio, Limits, Margins, Quotes, Scripmaster. (Only login endpoints are fixed.)

**Q7. Show me how to replace `{{baseUrl}}` with a real example.**
Suppose `baseUrl` returned is `https://neo-gw.kotaksecurities.com/xyz` and the specified endpoint is `{{baseUrl}}/quick/order/cancel`. Final URL to call: `https://neo-gw.kotaksecurities.com/xyz/quick/order/cancel` (just replace `{{baseUrl}}` with the full string — no braces remain).

## Headers & Endpoint Usage

**Q8. Which headers do I pass for each category?**

| API Category | Required Headers |
| --- | --- |
| Login (TOTP + MPIN) | `Authorization: <access token>` + `neo-fin-key: neotradeapi` |
| Orders / Reports / Portfolio / Limits / Margins | `Auth: <session token>` + `sid: <session sid>` + `neo-fin-key: neotradeapi` |
| Quotes / Scripmaster | `Authorization: <access token>` (no neo-fin-key, no Auth/sid) |

**Q9. Do I use Bearer with Authorization?**
No. Always pass the token without `Bearer`.

## TOTP Registration & Troubleshooting

**Q10. How do I register for TOTP?**
Dashboard → TOTP Registration in menu → verify mobile OTP + client code → scan QR (Google/Microsoft Authenticator) → enter TOTP → success toast.

**Q11. I reinstalled my authenticator. What now?**
Deregister via the same route, then register again with a new QR.

**Q12. I see "Invalid TOTP" / "Service error"**

- Invalid TOTP: sync device time (auto time), use the latest code.
- Service error: there's a 5-minute cooldown if you reattempt too quickly — wait and then re-scan QR.

## Static IP & Family Mapping

**Q13. Where do I find the network IP?**

- Windows: open Command Prompt from the Start menu, type `ipconfig` and press enter. Use the IPv4 address to whitelist on the NEO API dashboard.
- Mac: open Terminal and type `ipconfig getifaddr en0` for Wi-Fi or `ipconfig getifaddr en1` for Ethernet to see your local IP.

**Q14. Where can I get a static IP?**
Request one from your ISP (Airtel, Jio, ACT, etc.) — usually needs Aadhaar/KYC. Another option is an IP-over-VPN service that provides a fixed address. Kotak Securities is not associated with any provider; do your own due diligence.

**Q15. Why static IP?**
For SEBI compliance and security. Ensures only trusted infra can call your APIs. Optional now, but will become mandatory once the circular is effective.

**Q16. How many IPs can I set and how often can I change?**
One primary & one secondary (backup). Each can be changed once per week.

**Q17. Can I reuse the IP for family accounts?**
Yes — self-serve UI lets you link up to 10 family members to the same whitelisted IP.

**Q18. I don't have a static IP.**
Consider using a registered third-party platform (e.g., smallcase) that manages whitelisting with Kotak.

## API Changes

**Q19. Portfolio Holdings response — what changed?**
The new response adds richer fields such as `commonScripCode`, `logoUrl`, `cmotCode`, `unrealisedGainLoss`, `sqGainLoss`, `delGainLoss`, `marketLot`, `securitySubType`, etc.

**Q20. What are the new endpoints for Quotes & Scripmaster?**

- Quotes → `{{baseUrl}}/script-details/1.0/quotes/` (headers: `Authorization: <access token>` only)
- Scripmaster files → `{{baseUrl}}/script-details/1.0/masterscrip/file-paths` (headers: `Authorization: <access token>` only)

## Third-Party & SDKs

**Q21. I'm on a third-party platform. What should I do?**
Check with your provider if they've migrated to v2. If they have, no action is required on your end.

**Q22. I use the Python SDK. Any changes?**
No changes needed currently; old endpoints remain valid. For direct REST calls, follow the migration guide.

**Q23. Do you provide SDKs in other languages?**
For now, use cURL + Postman codegen to generate language stubs.

## Rate Limits & Cutover

**Q24. What are the rate limits?**
10 requests/second across APIs. Exceeding this returns rate limit errors.

**Q25. What happens after v1 retires?**
Calls to old endpoints will fail.

## Error Handling

### Login API (common)

- **Invalid TOTP** → The code is wrong/expired. Sync device time and retry with a fresh code.
- **Invalid MPIN** → MPIN incorrect. Verify or reset MPIN, then retry.
- **Session expired (after token reset)** → Resetting your access token immediately ends existing sessions. Re-login (TOTP → MPIN).
- **Dependency error (424)** → Temporary backend issue. Retry after a few seconds.

### Orders API (common)

| Code | Meaning | Fix |
| --- | --- | --- |
| 1006 | Invalid Exchange | Wrong exchange segment. Use correct NSE/BSE segment. |
| 1007 | Invalid Symbol | Scrip not found/unsupported. Validate with the scrip master. |
| 1009 | Invalid Quantity | Below min or wrong lot step. Match the instrument's lot size/rules. |
| 1005 | Internal Error | Transient issue. Retry; if persistent, raise a support ticket. |

### Reports API (common)

| Code | Meaning | Fix |
| --- | --- | --- |
| 400 | Request format error | Check payload schema, types, and required fields. |
| 424 | Dependency failure | Upstream dependency issue. Retry later. |
| 401 / Expired session | Session token/sid expired or missing | Re-login and pass `Auth` + `sid`. |
