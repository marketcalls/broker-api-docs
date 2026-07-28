# Static IP Whitelisting for Retail Algo Trading

**Effective From: 1 April 2026**

To comply with the SEBI circular on retail algorithmic trading participation, Kotak Neo Trade APIs will require Static IP Whitelisting for order execution. This ensures orders are placed only from verified infrastructure, improving security and regulatory compliance.

From 1 April 2026, order APIs will accept requests only from whitelisted static IPs with a valid session created from the same IP.

## What This Change Means

If you are using Kotak Neo APIs to automate trading, you must:

1. Whitelist a static IP address
2. Create an API session from that IP
3. Place orders from the same environment

If requests originate from non-whitelisted IPs, or sessions created from another IP, order APIs will reject the request.

## How to Whitelist Static IP

You can configure static IP from the Kotak Neo platform.

Steps:

1. Login to Kotak Neo
2. Go to **More**
3. Open **Trade API**
4. If you have not already created one → **Create API Application**
5. Click **Add IP** and add your Primary Static IP
6. Optionally add a Secondary Static IP from the default application details page as a fallback

## Static IP Rules

| Rule | Details |
| --- | --- |
| Maximum IPs | 2 (Primary + Secondary) |
| Change Frequency | Once every 7 days |
| Session Requirement | New session required after IP change |
| Supported IP types | IPv4 and IPv6 |

## How IP Validation Works

IP validation is enforced **only on order APIs**.

**APIs With IP Validation:**

- Place Order
- Modify Order
- Cancel Order

**APIs Without IP Validation:**

- Login APIs
- Report APIs
- Portfolio APIs
- Data APIs
- Websocket streams

These APIs continue to work normally regardless of IP.

## Session Binding Logic

IP is bound to the API session. The session must be created from the same IP that is sending order requests.

**Correct Flow:**

1. Whitelist static IP
2. Run trading system on that environment
3. Create Neo API session
4. Place orders

## Error Responses

**Non-Whitelisted IP** — request originates from an IP that is not whitelisted:

```json
{
  "stCode": 100008,
  "errMsg": "unauthorized",
  "stat": "Not_Ok"
}
```

**Session IP Mismatch** — IP is whitelisted but the session was created from another IP:

```json
{
  "stCode": 1037,
  "errMsg": "session ip doesnt match with reqest ip",
  "stat": "Not_Ok"
}
```

## What Happens If IP Changes During Active Session?

Sessions do not automatically terminate if the IP changes. However:

- Order APIs will fail (return `unauthorized`)
- Other APIs will continue to work

To resume order placement: ensure the correct IP, then create a new API session.

## Recommended Setup Workflow

1. **Obtain Static IP** — from your ISP or a cloud VPS (AWS, DigitalOcean, Azure, Google Cloud).
2. **Configure Your Strategy Environment** — run your trading algorithm from the system where the static IP is configured.
3. **Verify Your Static IP** — `GET https://api.ipify.org/`. If it returns your whitelisted static IP, your environment is correct.
4. **Create API Session** — from the same environment.
5. **Place Orders** — once session and IP match, Place/Modify/Cancel should return HTTP 200 OK.

## Family Account IP Sharing

Kotak Neo allows family members to share the same static IP.

Rules:

- Up to 10 family members can be added.
- Sharing is only for static IP usage; it does not give account access.
- Existing login family relationships do **not** automatically apply here — you must add family members separately under Trade API family management.

**Permissions:**

- **Parent account** can: add family members, add static IP, change static IP.
- **Child accounts** can: create API application. Cannot: add or modify static IP.

## Order Type Guidance

### Are Market Orders Allowed?

As per the SEBI circular, market orders are **not allowed** for retail algos. Kotak Neo recommends using limit orders.

If you still send a market order, the system will automatically apply a protection limit according to the grid below:

| Security type | Price range (in ₹) | Percentage of the Last Traded Price (LTP) |
| --- | --- | --- |
| EQ and FUT | Less than 100 | 2% |
| EQ and FUT | Between 100 and 500 | 1% |
| EQ and FUT | More than 500 | 0.50% |
| OPT | Less than 1 | ₹0.1 (absolute) |
| OPT | Between 1 to 5 | 10% |
| OPT | Between 5 to 10 | 5% |
| OPT | Between 10 and 100 | 3% |
| OPT | Between 100 and 500 | 2% |
| OPT | More than 500 | 1% |

- Buy orders use a protection limit **above** the LTP; sell orders use a limit **below** the LTP.
- Same logic applies to AMO market orders.
- For options, if LTP is unavailable the order must be rejected (with a clear rejection reason).
- The client places a Market order, but in the order book a Limit order will be visible.
- For precise execution, always use limit orders.

## Algo ID Requirement

Do users need to send Algo ID in the order payload? **No.** Kotak Neo APIs automatically append the appropriate exchange-compliant Algo ID. (APIs are rate limited to 10 orders per second and intended for tech-savvy retail users.)

## Fintech Partner Users

As per the SEBI circular, your fintech partner must:

- Get empanelled with exchanges
- Host their infrastructure on broker systems

Confirm with your fintech partner: Are they exchange empanelled? Are they hosted on Kotak infrastructure?

## FAQs

- **How many IP addresses can I whitelist?** Maximum 2 (Primary + Secondary fallback).
- **How many sessions can I create?** Multiple. However, orders can only be placed from 2 sessions simultaneously (one from Primary IP, one from Secondary IP).
- **How often can I change my IP?** Once every 7 days. After changing, create a new API session.
- **Is there any delay after whitelisting IP?** No — changes apply immediately.
- **Can I use IPv6?** Yes.
- **Can multiple accounts use the same IP?** Yes — family accounts can share the same IP.
- **Can I run multiple strategies from the same IP?** Yes, if sessions are created from that environment.
- **Do websocket streams require the same IP?** No — WebSocket connections are not restricted by IP validation.

## Need Help?

Contact Kotak Neo API support: **service.securities@kotak.com**
