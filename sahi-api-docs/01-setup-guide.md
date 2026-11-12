# Set up your Sahi API

> Source: *Sahi API Setup Guide* (Sahi Direct API · Quick start), updated from https://docs.sahi.com/quick-start/ on 2026-11-11 (TOTP keys). Full reference: https://docs.sahi.com/

Six steps to your first API order. You need a **Sahi account**, and a **fixed public IP** if you will place orders.

There are two key types. A **Regular** key is approved in the dashboard each trading day (Step 3); a **TOTP** key approves itself with an authenticator code at sign-in, so an unattended bot needs no daily click.

The guide covers two ways to call the API. Part A is the same for both; Part B gives each step for the **Python SDK** (`pip install sahiapi`) and for **cURL** (any HTTP client).

| Step | What | Notes |
| --- | --- | --- |
| 1 | [Create an API key](#step-1-create-an-api-key) | in the dashboard |
| 2 | [Register your static IP](#step-2-register-your-static-ip-orders-only) | orders only |
| 3 | [Approve the key every trading day](#step-3-approve-the-key-every-trading-day) | Regular keys only; resets 6 AM IST |
| 4 | Sign in: [Python SDK](#step-4-python-sdk-install-the-sdk-and-sign-in) / [cURL](#step-4-curl-mint-a-token-and-sign-in) | |
| 5 | [Make your first calls](#step-5-make-your-first-calls) | LTP → funds → order |
| 6 | [Every trading day](#step-6-every-trading-day) | |

---

## Part A: In your Sahi account

Sahi web → Profile → API Dashboard

### Step 1: Create an API key

1. Open Sahi web, click your **profile avatar** (bottom left) and choose **API Dashboard**.
2. Click **Create API key**. Complete two-factor verification if asked.
3. Enter a **Name** you will recognise later, e.g. `Trading bot`.
4. Choose the **Access**: **Full access** (orders + market data) or **Market data** (data only; needs no static IP).
5. Choose the **Key type**:
   - **Regular**: you approve the key in the dashboard every trading day (Step 3).
   - **TOTP**: an authenticator code approves it at sign-in, so a scheduled bot runs without you.
6. Finish creating it:
   - **Regular**: click **Create API key**.
   - **TOTP**: click **Continue**, scan the QR code with an authenticator app (or copy the setup key, the **TOTP secret**), enter the current 6-digit code and click **Create API key**. *Finish within 10 minutes; nothing is created until a correct code is accepted. The TOTP secret is shown only during setup: store it with your other secrets.*
7. Copy the **API key** (`pk_…`) and the **API secret** (`sahi_sk_…`) somewhere safe. *The secret is shown only once.*
8. Tick **I have saved my credentials** and click **Done**.

> **Good to know:** you can hold up to 5 keys. Deleting a key stops every token minted from it immediately.

*Videos in the original guide:* **Create a key** (steps 1–8 above); **Delete a key** (trash icon → Delete).

### Step 2: Register your static IP (orders only)

1. Skip this step if you will only read market data. Placing, modifying and cancelling orders need a registered IP; reads don't.
2. On the **machine that will place orders**, find its public IP:

   ```bash
   curl https://checkip.amazonaws.com
   ```

3. In the API Dashboard, click **Add static IP**.
4. Enter it as the **Primary IP address**. *Secondary is optional: use it for a backup line, not a second bot.*
5. Click **Save IP address**, check the review screen and confirm. *The slot is now locked for 7 days.*

> **Good to know:** use a fixed IP (cloud VM or static broadband); home and mobile IPs change. One IP can belong to only one Sahi account. Orders from any other IP fail with `403 IP_NOT_ALLOWED`.

*Videos in the original guide:* **Add static IPs** (steps 3–5 above); **Delete an IP** (orders from it stop at once; the slot stays locked for 7 days).

### Step 3: Approve the key every trading day

Regular keys only. A TOTP key needs no click: the first correct code of the trading day, sent at sign-in, approves it, and **Approve** on a TOTP key returns `409`.

1. Open the **API Dashboard** after 6 AM IST. Your key now shows `Expired`. *A key created today is already approved.*
2. Click **Approve** on the key. Its status changes to `Resets 6 AM tomorrow`.
3. Sign in from your code (Step 4). *Access tokens also expire at 6 AM IST, so every program signs in once a day.*

*Video in the original guide:* **Approve a key** (Expired → Approve → Resets 6 AM tomorrow).

---

## Part B: On your machine

Python SDK `sahiapi`, or cURL (any HTTP client works the same way).

### Step 4 (Python SDK): Install the SDK and sign in

1. Install the SDK from PyPI (Python 3.9 or newer; use `pip3` if `pip` is not found):

   ```bash
   pip install sahiapi pyotp
   ```

   *A TOTP key needs `sahiapi` 0.3.0 or newer; `pyotp` lets an unattended bot calculate the code from the TOTP secret.*

2. Save this as `hello.py`, replace `pk_...` and `sahi_sk_...` with your key id and secret, and run `python3 hello.py`:

   ```python
   from sahiapi import SahiAPI

   api = SahiAPI.from_credentials(
       key_id="pk_...",
       secret="sahi_sk_...",
       # TOTP key only: the current 6-digit code, typed in or calculated:
       # totp=pyotp.TOTP("YOUR_TOTP_SECRET").now(),
   )

   print(api.get_profile())
   ```

3. You should see your profile printed. You are signed in; the token lasts until 6 AM IST, so sign in once a day.
   - `SahiKeyNotApprovedException` → approve the key (Step 3).
   - `SahiAuthenticationException` → wrong key id or secret.
   - `SahiInvalidTotpException` → wrong TOTP code; check the machine's clock.
   - Keep the secret out of shared code: load it from an environment variable or a secret store.

### Step 4 (cURL): Mint a token and sign in

1. Exchange your key for an access token (valid until 6 AM IST).

   ```bash
   curl -X POST https://apis.sahi.com/api/v1/apikeys/token \
     -H "Content-Type: application/json" \
     -d '{"key_id":"pk_your_key_id","secret":"sahi_sk_your_secret"}'
   # → {"access_token":"eyJ…","token_type":"Bearer","expires_in":65275,"expires_at":"…T06:00:00+05:30","scope":"…"}
   ```

   For a **TOTP key**, also send the current code as a string (leading zeros kept): `"totp":"042917"`. A Regular key with `totp` is rejected.

2. Copy the `access_token` value into a variable:

   ```bash
   export TOKEN=eyJ…                       # Windows PowerShell: $env:TOKEN = "eyJ..."
   ```

3. Test it. Send `Authorization: Bearer $TOKEN` on every call from now on:

   ```bash
   curl https://direct.sahi.com/v1/profile -H "Authorization: Bearer $TOKEN"
   ```

4. You should see your profile. You are signed in; mint once a day.
   - `403 Forbidden` on mint → approve the key (Step 3).
   - `401` → wrong key id or secret.
   - `401 InvalidTotp` → wrong TOTP code; check the machine's clock (the reply carries `server_time`).

### Step 5: Make your first calls

Prices are in **paise** (divide by 100); quantities are in **units**. Market data uses `instrument_id`; orders use `exchange_segment` + `symbol`. Both come from the scrip master (the Python SDK downloads it for you).

#### 1. Find your instrument

Find it in the scrip master (RELIANCE on NSE is `12027`).

Python (`hello.py`, continued):

```python
instrument_id = api.get_instruments_by_symbol("RELIANCE", SahiAPI.EXCHANGE_SEGMENT_NSE)[0]["id"]   # 12027
```

cURL:

```bash
curl -O https://assets.sahi.com/external/instruments.csv            # rebuilt daily around 6 AM IST
grep ',RELIANCE,' instruments.csv | grep ',NSE,NSE,'                 # first column is the id → 12027
```

#### 2. Get its last traded price

Python (`hello.py`, continued):

```python
quote = api.get_quotes(instrument_id)["data"][str(instrument_id)]   # keyed by the id as a string
print(quote["last_trade_price"] / 100, "INR")
```

cURL:

```bash
curl "https://direct.sahi.com/v1/marketdata/ltp?i=12027" -H "Authorization: Bearer $TOKEN"
# → {"data":{"12027":{"last_trade_price":251000,"last_trade_time":…}}}   # paise: ₹2,510.00
```

#### 3. Check your funds

Python (`hello.py`, continued):

```python
print(api.get_funds()["available"]["stocks_delivery"] / 100, "INR for delivery buys")
```

cURL:

```bash
curl https://direct.sahi.com/v1/funds -H "Authorization: Bearer $TOKEN"
# → {"available":{"stocks_delivery":10500000,"intraday_and_fno_selling":…,…},…}   # paise
```

#### 4. Place your first order

Place it during market hours (09:15–15:30 IST).

> This places a real order: a limit buy at the bottom of the day's band, sized to your delivery funds (at most 1 share), so it rests unfilled; it is cancelled if it has not filled.

Python (`hello.py`, continued):

```python
import time

price = quote["dpr_lower"]                                        # paise; bottom of the day's band
available = api.get_funds()["available"]["stocks_delivery"]      # paise
qty = min(available // price, 1)                                  # what the funds cover, at most 1 share
if qty < 1:
    raise SystemExit("not enough funds for one share")

result = api.place_order(
    exchange_segment=SahiAPI.EXCHANGE_SEGMENT_NSE,
    symbol="RELIANCE",
    txn_type=SahiAPI.TXN_TYPE_BUY,
    qty=qty,
    order_type=SahiAPI.ORDER_TYPE_LIMIT,
    product=SahiAPI.PRODUCT_DELIVERY,
    validity=SahiAPI.VALIDITY_DAY,
    price=price,
)
order_id = result["order_ids"][0]

time.sleep(1)                                                     # the order takes a moment to reach the book
status = api.get_order_detail(order_id)["status"]
print(status)                                                     # Open, or Rejected with rejection_reason

if status in (SahiAPI.ORDER_STATUS_OPEN, SahiAPI.ORDER_STATUS_OPEN_PARTIAL):
    api.cancel_order(order_id)                                    # not filled yet
```

cURL:

```bash
# a) Day's price band (paise): dpr_lower / dpr_upper in the quote
curl "https://direct.sahi.com/v1/marketdata/quotes?i=12027" -H "Authorization: Bearer $TOKEN"

# b) Limit buy, 1 share, at dpr_lower (replace the price)
curl -X POST https://direct.sahi.com/v1/orders \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"exchange_segment":"NSE","symbol":"RELIANCE","txn_type":"B","qty":1,
       "order_type":"LMT","product":"C","validity":"DAY","price":249000}'
# → {"order_ids":["2610…"]}

# c) Check it (status: Open, or Rejected + rejection_reason), then cancel it
curl https://direct.sahi.com/v1/orders/ORDER_ID -H "Authorization: Bearer $TOKEN"
curl -X DELETE https://direct.sahi.com/v1/orders/ORDER_ID -H "Authorization: Bearer $TOKEN"
```

An order id means **accepted**, not placed: check `status`. `SahiIpNotAllowedException` (Python) / `403 IP_NOT_ALLOWED` (cURL) → your IP isn't registered (Step 2).

#### 5. View your positions and orders

Python:

```python
for p in api.get_positions()["positions"]:
    print(p["instrument_id"], p["net_qty"], p["net_avg_price"] / 100, p["realised_pnl"] / 100)

for o in api.get_order_list()["orders"]:                           # today's order book
    print(o["order_id"], o["symbol"], o["status"], o["filled_qty"])
```

cURL:

```bash
curl https://direct.sahi.com/v1/positions -H "Authorization: Bearer $TOKEN"   # net_qty, net_avg_price, realised_pnl
curl https://direct.sahi.com/v1/orders    -H "Authorization: Bearer $TOKEN"   # today's order book
```

Also:

- Python: `api.get_holdings()`, `api.get_quotes()`, `api.modify_order()`, and `SahiFeed` for live ticks.
- cURL: `GET /v1/holdings`, `PUT /v1/orders/{id}` to modify, and the WebSocket streams for live ticks.

See the docs.

### Step 6: Every trading day

1. Approve a Regular key in the API Dashboard (a TOTP key approves itself with the code at sign-in).
2. Sign in once and reuse the token until 6 AM IST.
3. If orders fail with `403 IP_NOT_ALLOWED`, your public IP has changed: re-check it (Step 2).

---

Full reference: [docs.sahi.com](https://docs.sahi.com/) · Help: [developers@sahi.com](mailto:developers@sahi.com)
