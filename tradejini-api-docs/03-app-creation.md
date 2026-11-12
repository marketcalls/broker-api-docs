# App Creation

How to register an app on the Tradejini Developer Portal and obtain API credentials. Two app types are supported: **Individual Apps** (for your own account) and **User Based Apps** (third-party apps that trade on behalf of other Tradejini users).

## Individual Apps

To start automating your trading strategies or fetching market feeds using Tradejini's CubePlus API, individual retail traders need to register an application on the Tradejini Developer Portal. This generates the unique API credentials required to authenticate your trading sessions.

### Prerequisites

Before initiating the App Creation process, ensure you have the following:

- **Active Trading Account:** An active retail trading account with Tradejini (CubePlus).
- **Login Credentials:** Your Tradejini Client ID, trading password, and active 2FA (TOTP set up via an authenticator app or mobile OTP access).
- **Static IP Address:** In compliance with security guidelines, all individual API requests must originate from a whitelisted static IP address. Ensure you have obtained a static IP from your ISP, cloud provider (AWS/GCP/Azure), or VPS.

---

## User Based Apps

The User-Based (Individual Access) App registration page is designed for traders who intend to execute algorithmic trading strategies on their personal Tradejini trading accounts. Creating an individual user-based application generates the permanent static credentials required by the CubePlus API to establish an authenticated session, stream real-time WebSocket data, and manage order routing.

To configure your User-Based App on the Tradejini Developer Portal, provide a unique alphanumeric App Name (e.g., MyPythonBot), your official Tradejini Client Code / User ID to link your trading margins, and a Redirect URL (e.g., [http://127.0.0.1:5000/callback](http://127.0.0.1:5000/callback) or your third-party platform's callback link) where the OAuth login authorization code will be sent. Optionally, you can add a Webhook URL to receive live POST notifications for order updates and margin exceptions (leave blank if relying entirely on WebSockets), alongside a Logo URL (.png or .jpeg) to give your application a custom icon within the developer dashboard.
