# Getting Started — Web Dashboard

The self-service portal at <https://tradeapi.samco.in/app/login> where you create OAuth apps, generate credentials, and register static IPs.

## Dashboard User Manual

The **Samco Trade API Web Dashboard** is the recommended self-service portal for managing your Trade API access. Use it to create OAuth apps, generate API credentials, and register static IPs — all protected by OTP.

> **INFO** — Dashboard URL
>
> **[`https://tradeapi.samco.in/app/login`](https://tradeapi.samco.in/app/login)**

---

### Getting Started

#### What you need

- A **Samco trading account** (client code + password)
- Access to your **registered mobile number** and **email** for OTP

#### Logging in

1. Open [https://tradeapi.samco.in/app/login](https://tradeapi.samco.in/app/login) in your browser.
2. Enter your **Samco User ID** (e.g. `AB1234`) and **password**.
3. Click **Sign In**.
4. You will land on the **API Keys** page.

![Dashboard login screen](https://docs-tradeapi.samco.in/assets/dashboard/login.png)

After a successful sign-in you arrive on the API Keys landing page:

![API Keys landing page](https://docs-tradeapi.samco.in/assets/dashboard/landing-api-keys.png)

Once you are signed in, the two main sections of the dashboard are covered in separate pages:

- **[API Keys](#api-keys)** — create OAuth apps, view credentials, regenerate them, and deactivate apps you no longer need (deactivation revokes all active sessions; you can reactivate later).
- **[Static IPs](#static-ips)** — register and manage the IP addresses allowed to call the order related apis.

---

### Signing Out

Click your account name in the bottom-left corner of the sidebar and click the **Logout** button (exit icon). You will be redirected to the login page.

![Sidebar account menu with Logout](https://docs-tradeapi.samco.in/assets/dashboard/sidebar-logout.png)

---

### Troubleshooting

#### OTP not received

- Check your registered mobile number and email inbox (including spam/junk folder).
- OTPs expire after a few minutes — request a new one if needed.
- Contact [apisupport@samco.in](mailto:apisupport@samco.in) if issues persist.

#### Login fails with "Invalid credentials"

- Double-check your **User ID** (e.g. `AB1234`) and **password**.
- The same credentials work on SAMCO Mobile App, SAMCO Web, and Stockbasket.
- Use the SAMCO account password reset flow if you've forgotten your password.

#### IP rejected after registration

- Verify the IP is a public IPv4 address (not a private range like `192.168.x.x` or `10.x.x.x`).
- Confirm the IP is not already registered to another client.
- Check that the 7-day IP-change cooldown has not been hit. Per SEBI A.6, you can change your IP **once every 7 days** from your last change, **across all your apps**, including deactivated ones — deleting and recreating an app does not reset this. Reusing an IP that is already registered to another of your apps does not count against the cooldown.

#### API calls failing with `403 — The IP is not the registered static IP`

- This means the source IP our server saw is **not** one of your registered `PRIMARY` / `SECONDARY` IPs.
- Check the **Your IP** value in the dashboard footer — this is the IP our server sees you from right now.
- From a backend host, call [`GET /ip/whoami`](05-ip-diagnostics.md#who-am-i) using the host's session token. If `matches: false`, the response's `srcIp` is the value that needs to match a registered IP — update via the **Static IPs** page (subject to the 7-day cooldown).
- Common causes: corporate proxy / VPN changed your source IP, the call came from a different backend pod than the one you registered, or your ISP rotated your dynamic IP.

#### API Key / Secret not working

- Confirm the app is in **Active** status.
- Regenerating Key or Secret invalidates all prior credentials — make sure your integration is using the latest values.

---

### Support

| Channel | Details |
| --- | --- |
| **Ticket** | [samco.in/support/ticket](https://www.samco.in/support/ticket) |
| **Forum** | [forum.samco.in/tag/trade_api](https://forum.samco.in/tag/trade_api) |
| **Email** | [apisupport@samco.in](mailto:apisupport@samco.in) |

---

## API Keys

The **API Keys** section lists all your OAuth apps. Each app has its own API Key and API Secret, which are used to authenticate your trading application with the Samco Trade APIs.

### Creating an OAuth App

1. On the **API Keys** page, click **Create New App**.

   ![Create New App button on API Keys page](https://docs-tradeapi.samco.in/assets/dashboard/create-new-app-button.png)
2. Fill in the form:

| Field | Description |
| --- | --- |
| **App Name** | A descriptive label (3–100 characters), e.g. `My Trading App`. Must be **unique across your apps** — comparison is case-insensitive and ignores surrounding whitespace. Deactivated apps still hold their name. |
| **Redirect URL** | The HTTPS URL users are redirected to after OAuth login. `https://tradeapi.samco.in/app/callback` is allowed for testing. |
| **Scope** | Displayed as `all` and **not editable** — granular scopes are not yet supported. Every app you create today is issued the full `all` scope. |

3. Click **Create App**. An OTP will be sent to your registered mobile and email.

   ![Create App button on Create App form](https://docs-tradeapi.samco.in/assets/dashboard/create-app-create-button.png)
4. Enter the OTP and click **Verify OTP**.

   ![Enter OTP and click Verify OTP](https://docs-tradeapi.samco.in/assets/dashboard/create-app-otp-submit.png)
5. On success, the **API Secret** is displayed **once** — copy and store it securely. The **API Key** is delivered to your registered email. The modal title includes the **app name** so you can confirm which app the credentials belong to when you create multiple apps in a row.

   ![API Secret shown once with app name in title](https://docs-tradeapi.samco.in/assets/dashboard/create-app-secret-shown.png)

> **DANGER** — Save your API Secret now
>
> The API Secret is shown **only once**. If you lose it, you must regenerate it, which invalidates all active sessions for that app.

> **INFO** — App limit
>
> You can have up to **5 OAuth apps**. **Deactivate** keeps the app on file when you don't need it temporarily; the slot is not freed because app deletion is not currently exposed in the dashboard.

### Viewing App Details

The **Registered Apps** table on the **API Keys** page has the following columns:

| Column | Description |
| --- | --- |
| **App Name** | The label you gave the app at creation time. |
| **Redirect URL** | The HTTPS callback configured for the OAuth flow. |
| **Status** | `Active` (green) or `Deactivated` (red). |
| **Last Updated** | Timestamp of the most recent change (falls back to created time if untouched). |
| **Actions** | Per-row icon buttons — see below. |

![Registered Apps table with action buttons](https://docs-tradeapi.samco.in/assets/dashboard/app-row-actions.png)

Each row exposes four action buttons, left to right. The icons below are the exact glyphs rendered by the dashboard:

| Icon | Tooltip | Action | Notes |
| --- | --- | --- | --- |
|  | **Edit app details** | Edit | Update App Name / Redirect URL. OTP required. |
|  | **Deactivate app** / **Activate app** | Toggle status | When Active, deactivates the app and revokes all active sessions + deregisters static IPs. When Deactivated, re-enables the app. |
|  | **Regenerate API key** | Regenerate Key | Issues a new key, emailed to your registered address. Revokes active sessions. |
|  | **Regenerate API secret** | Regenerate Secret | Issues a new secret, shown **once** in a modal. Revokes active sessions. |

> **INFO** — Delete is not supported
>
> The dashboard does not currently support deleting an app. Use **Deactivate** to revoke an app you no longer want — its slot is retained but the credentials stop working.

### Regenerating Credentials

| Icon | Action | Effect | Delivery |
| --- | --- | --- | --- |
|  | **Regenerate API Key** | All active sessions for this app are revoked; a new key is issued. | Emailed to your registered address. |
|  | **Regenerate API Secret** | All active sessions for this app are revoked; a new secret is issued. | Shown **once** in the dashboard — copy immediately. |

Both actions require OTP confirmation.

![Regenerate API Key confirmation](https://docs-tradeapi.samco.in/assets/dashboard/regenerate-key-confirm.png)

When you regenerate the secret, the new value is displayed once in a modal whose title includes the app name — copy it before closing:

![Regenerated API Secret modal](https://docs-tradeapi.samco.in/assets/dashboard/regenerated-secret-shown.png)

### Editing an App

Click the **Edit** icon on an app row to update:

- App Name
- Redirect URL

Scope is fixed at creation time and cannot be changed here. Credentials (API Key / API Secret) are not changed by editing — use the row's **Regenerate** actions for those. OTP confirmation is required.

![Edit App Details form](https://docs-tradeapi.samco.in/assets/dashboard/edit-app-form.png)

### Deactivating an App

Click the **Deactivate** icon on an app row and confirm with OTP to temporarily disable the app without removing it. You can re-enable it later by clicking the same icon (tooltip changes to **Activate app**).

![Deactivate App confirmation](https://docs-tradeapi.samco.in/assets/dashboard/deactivate-confirm.png)

On deactivation:

- All active sessions and tokens for this app are immediately revoked.
- The app's API Key and Secret stop working.
- Static IPs registered to this app are deregistered.
- The app row stays in your dashboard with status **Deactivated** — switch it back to **Active** any time.
- The slot **still counts** toward your 5-app limit. App deletion is not currently exposed in the dashboard.

### Source IP in the footer

The dashboard footer shows the **source IP our server sees you connecting from** (labelled **Your IP**). Use this to confirm which IP to register for your apps — it is the value SAMCO validates against, which can differ from what a "what is my IP" website shows due to NAT or VPN. See [Static IPs](#static-ips) for the IP management UI.

---

## Static IPs

The **Static IPs** section lets you **whitelist** the IP addresses that are allowed to make requests to the Samco Trade APIs on behalf of your OAuth app. Any request from an IP that is not on your whitelist is rejected.

This is a regulatory requirement: SEBI circular **SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/0000013** (4 Feb 2025) and the NSE implementation standards in circular **NSE/INVG/67858** (5 May 2025) require brokers to permit API access **only** through a unique API key paired with a static IP whitelisted by the broker, so that every algo order can be traced back to the algo provider and the end client. Both circulars are available on the SEBI and NSE archives (search by the circular reference number).

![Static IPs list](https://docs-tradeapi.samco.in/assets/dashboard/static-ips-list.png)

Each OAuth app can have:

- One **Primary** IP address (required)
- One **Secondary** IP address (optional backup)

### Registering a Static IP

1. On the **Static IPs** page, click **Add IP**.
2. Fill in the form:

| Field | Description |
| --- | --- |
| **App** | The OAuth app this IP belongs to. |
| **IP Type** | `PRIMARY` or `SECONDARY`. |
| **IP Address** | A valid public IPv4 address (e.g. `203.0.113.42`). |

3. Click **Save**. Enter the OTP when prompted.
4. The IP is registered and shows a **Last updated** timestamp.

![Add IP form](https://docs-tradeapi.samco.in/assets/dashboard/add-ip-form.png)

> **TIP** — Use the IP shown in the dashboard footer
>
> Every dashboard page shows a small chip in the **bottom-right corner** of the screen:
>
> > **Your IP:** `203.0.113.42`
>
> This is the IP **our server** sees you from — the exact value that will be validated when you call the Trade APIs from this machine. Hover the chip for a reminder: *"This is the IP our server sees you from. Register this IP under Static IPs if you plan to call the Trade APIs from this machine."*
>
> Prefer this over any third-party IP-lookup site, which can show a different address when you are behind NAT, a corporate proxy, or CGNAT.
>
> For programmatic verification from each backend host (multi-pod deployments, fallback hosts), call [`GET /ip/whoami`](05-ip-diagnostics.md#who-am-i) from that host.

![Dashboard footer chip showing "Your IP: 203.0.113.42" in the bottom-right corner](https://docs-tradeapi.samco.in/assets/dashboard/footer-your-ip.png)

### Updating an IP

1. Click the **Edit** icon on an IP row.
2. Enter the new IP address.
3. Confirm with OTP.

The new IP takes effect immediately; the old IP stops working.

![Edit IP dialog](https://docs-tradeapi.samco.in/assets/dashboard/edit-ip.png)

> **WARNING** — You can change an IP only once every 7 days
>
> Per SEBI rules (Section A.6), you can change your IP **once every 7 days** from your last change — not per OAuth app, but across your entire SAMCO account. So if you change at 2:30 PM on Monday, you can change again at 2:30 PM next Monday.
>
> While you are in the 7-day window, the **Edit** button is disabled. Hover over it to see the exact date and time when your next change becomes available.
>
> Deactivating an OAuth app and creating a new one does **not** reset this clock — the 7-day count is per account, and the history is kept on file across all of your apps.
>
> **Re-using an IP that is already whitelisted on your account is free.** Mapping an already-whitelisted IP (e.g. `203.0.113.42`) to another of your OAuth apps is treated as re-use of an existing approved IP — it does **not** count as a new IP change, and the 7-day clock is not affected.

### Removing an IP

Click the **Delete** icon on an IP row and confirm with OTP. The IP slot is cleared and the address becomes available again — either for you to register on a different app, or for another client to claim.

![Delete IP confirmation](https://docs-tradeapi.samco.in/assets/dashboard/delete-ip-confirm.png)

> **WARNING** — Deleting counts as an IP change
>
> Deleting an IP counts the same as changing one (SEBI Section A.6). After deleting, you cannot register a *different* IP for any of your apps until 7 days have elapsed from the delete. Re-registering the **same** IP (yours or one already mapped to another of your apps) is still allowed.

You can also clear all IPs for an app at once by **Deactivating** the OAuth app (API Keys → Deactivate) — every IP attached to that app is released as part of the deactivation.

### SEBI / NSE Compliance Reference

These rules implement SEBI circular **SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/0000013** (4 Feb 2025) and the NSE implementation standards in circular **NSE/INVG/67858** (5 May 2025), Annexure Section A.

> **WARNING** — Compliance requirements
>
> - **Whitelist-only order access** — order-placement / order-modification API requests are accepted only from IPs you have whitelisted here. Open APIs are not permitted for order flow (SEBI Section I(d), NSE Section I(e)).
> - **7-day cooldown** — you can change an IP only once every 7 days from your last change. This applies across all your apps, including deactivated ones (NSE Section A.6 — *"not more than once a calendar week"*; SAMCO enforces this as a strict 7-day rolling window).
> - **Unique mapping** — a static IP can be mapped to **only one client at a time** (NSE Section A.7). If the IP is already whitelisted to another SAMCO client, your request is rejected.
> - **Reuse within your account is allowed** — the same whitelisted IP can be mapped to multiple of your own apps without counting as a new IP change.
> - **Primary** and **Secondary** must each be valid **public IPv4** addresses, and the two must be different addresses for the same app.
> - **Daily 8:00 AM logout** — all API sessions are forcibly logged out every day at **8:00 AM IST**, before the start of the next trading day (NSE Section A.8). You must reauthenticate via OAuth each trading day.
