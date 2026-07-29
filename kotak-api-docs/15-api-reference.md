# API Reference

## Downloads & Links

- **Postman collection:** https://bit.ly/3W4x7oO
- **Migration guide (v1 → v2):** https://bit.ly/46nKKpg
- **Python SDK (GitHub):** https://github.com/Kotak-Neo/Kotak-neo-api-v2
- **Report issues (REST/SDK):** https://github.com/Kotak-Neo/Kotak-neo-api-v2/issues

---

## cURL Examples

### Login Flow (fixed endpoints)

**1) TOTP Login → returns viewToken + viewSid**

```bash
curl -X POST "https://mis.kotaksecurities.com/login/1.0/tradeApiLogin" \
-H "Authorization: <access_token>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/json" \
-d '{
  "mobileNumber": "<+91XXXXXXXXXX>",
  "ucc": "<client_code>",
  "totp": "<6_digit_totp>"
}'
```

**2) MPIN Validate → returns session token (Auth) + session sid (Sid) + baseUrl**

In your collection, `viewSid` and `viewToken` are sent as headers to this call.

```bash
curl -X POST "https://mis.kotaksecurities.com/login/1.0/tradeApiValidate" \
-H "Authorization: <access_token>" \
-H "neo-fin-key: neotradeapi" \
-H "sid: <viewSid_from_previous_step>" \
-H "Auth: <viewToken_from_previous_step>" \
-H "Content-Type: application/json" \
-d '{
  "mpin": "<mpin>"
}'
```

Response gives you: `baseUrl` (use it for all post-login APIs), `Auth` = session token, `Sid` = session sid.

### Using baseUrl (important)

If MPIN validate returned `"baseUrl": "https://neo-gw.kotaksecurities.com/xyz"` and the spec shows `{{baseUrl}}/quick/order/cancel`, then your final URL is:

```
https://neo-gw.kotaksecurities.com/xyz/quick/order/cancel
```

Just replace `{{baseUrl}}` with the returned string. No braces in the final URL.

### Orders (Postman: urlencoded, jData body)

**Place Order**

```bash
curl -X POST "<baseUrl>/quick/order/rule/ms/place" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={
  "am": "NO",
  "dq": "0",
  "es": "nse_cm",
  "mp": "0",
  "pc": "CNC",
  "pf": "N",
  "pr": "0",
  "pt": "MKT",
  "qt": "1",
  "rt": "DAY",
  "tp": "0",
  "ts": "ITBEES-EQ",
  "tt": "B"
}'
```

**Modify Order**

```bash
curl -X POST "<baseUrl>/quick/order/vr/modify" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={
  "am": "NO",
  "dq": "0",
  "es": "nse_cm",
  "mp": "0",
  "pc": "NRML",
  "pf": "N",
  "pr": "0",
  "pt": "MKT",
  "qt": "1",
  "rt": "DAY",
  "tp": "0",
  "ts": "TATAPOWER-EQ",
  "tt": "B",
  "no": "<orderNo>"
}'
```

**Cancel / Exit (Cover / Bracket)**

> Note: Cover and Bracket orders were discontinued on Trade APIs since 1 April 2026; the exit endpoints are retained here from the source collection for reference.

```bash
# Cancel
curl -X POST "<baseUrl>/quick/order/cancel" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={"on":"<orderNo>","am":"NO"}'

# Exit Cover
curl -X POST "<baseUrl>/quick/order/co/exit" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={"on":"<orderNo>","am":"NO"}'

# Exit Bracket
curl -X POST "<baseUrl>/quick/order/bo/exit" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={"on":"<orderNo>","am":"NO"}'
```

### Reports

**Order Book (GET)**

```bash
curl -X GET "<baseUrl>/quick/user/orders" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"
```

**Order History (POST, urlencoded)**

```bash
curl -X POST "<baseUrl>/quick/order/history" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={"nOrdNo":"250720000007242"}'
```

**Trade Book / Positions / Holdings (GET)**

```bash
# Trade Book
curl -X GET "<baseUrl>/quick/user/trades" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"

# Position Book
curl -X GET "<baseUrl>/quick/user/positions" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"

# Portfolio Holdings (new response shape)
curl -X GET "<baseUrl>/portfolio/v1/holdings" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"
```

### Quotes (GET; no neo-fin-key, no Auth/Sid)

```bash
curl -X GET "<baseUrl>/script-details/1.0/quotes/neosymbol/nse_cm|26000/all" \
-H "Authorization: <access_token>"
```

Only the `Authorization` header is required here (plain access token). Do **not** send `neo-fin-key`, `Auth`, or `Sid`.

### Scripmaster Files (GET; no neo-fin-key, no Auth/Sid)

```bash
curl -X GET "<baseUrl>/script-details/1.0/masterscrip/file-paths" \
-H "Authorization: <access_token>"
```

## Notes

- **Headers:** Post-login APIs (Orders/Reports/Portfolio/etc.) use `Auth` (session token) + `Sid` (session sid). `neo-fin-key: neotradeapi` is required except for Quotes and Scripmaster.
- **Bodies** for Orders and some Reports are `application/x-www-form-urlencoded` with a `jData` parameter containing JSON.
