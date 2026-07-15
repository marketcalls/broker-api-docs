> Source: https://docs.arrow.trade/rest-api/authentication/

# Authentication

Authentication forms the cornerstone of the Arrow Developer API Suite, ensuring secure access to all platform services. This guide provides comprehensive instructions for generating authentication tokens and establishing secure API connections.

## Prerequisites

Before proceeding with authentication, Please make sure you have

  * Valid Arrow user credentials
  * Registered your redirect URL in the developer apps section (click on the profile icon and then click on the Trading API's on the dropdown menu) of the main [Trading App](https://app.arrow.trade)
  * Filled in the Form with the required data (static IP is now mandatory as per the latest [SEBI Circular](https://www.sebi.gov.in/legal/circulars/feb-2025/safer-participation-of-retail-investors-in-algorithmic-trading_91614.html))
  * You have your application credentials: `appID` and `appSecret` handy (Clicking on the +Create New button in the Trading API Section)

## Authentication Flow

The Arrow API employs a secure authentication process combining OAuth-style redirects with SHA256 cryptographic verification.

### Step 1: Initiate Login Session

Navigate to the Arrow authentication endpoint with your application ID:

```
https://app.arrow.trade/app/login?appID=<YOUR_APP_ID>
```

### Step 2: Complete User Authentication

  1. Enter your **User ID** , **Password** , and **TOTP** (Time-based One-Time Password)
  2. Upon successful authentication, you'll be redirected to your registered redirect URL
  3. Extract the following parameters from the redirect URL query string:
  4. `request-token`: Temporary authentication token
  5. `checksum`: SHA256 hash of `request-token:appID` for verification

### Step 3: Generate Access Token

Create a secure checksum by generating the SHA256 hash of the concatenated string:

```
appID:appSecret:request-token
```

Security Notice

Ensure proper concatenation with colons (`:`) as delimiters. Incorrect formatting will result in authentication failure.

### Step 4: Token Exchange

Submit a POST request to exchange your request token for a permanent access token:

Token exchange host

The canonical endpoint is `https://edge.arrow.trade/auth/app/authenticate-token`. The Python SDK also accepts responses from `https://api.arrow.trade/auth/app/authenticate-token` and sends both `checkSum` and `checksum` fields for compatibility.

**Sample Request**

```json
curl --location 'https://edge.arrow.trade/auth/app/authenticate-token' \
--header 'Content-Type: application/json' \
--data '{
    "checkSum": "<SHA256_OF_appID:appSecret:request-token>",
    "token": "<YOUR_REQUEST_TOKEN>",
    "appID": "<YOUR_APP_ID>"
}'
```

### Successful Response

Upon successful authentication, you'll receive:

```json
{
    "data": {
        "name": "ABHISHEK JAIN",
        "token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBSjAmdakajehrk23432k4h32kl4n32l4kl4324zZDc3YzQ4YyIsImV4cCI6MTc2OTc5Nzc5OSwiaWF0IjoxNzY5NzUzMDA4fQ.hQvnAFJEF1MOt4jygdEFVDyqVPPVqlsX3nvWvEveHI8oHNdrnv1C6fBG12UhMnXfuUc3-6hd77UESaiVrJ3dDw",
        "userID": "AJ0001"
    },
    "status": "success"
}
```

## Using Your Access Token

Include both your `token` and `appID` in all subsequent API requests. The token serves as your authentication credential for accessing Arrow trading services.

## Token Management

### Token Expiration

Access tokens have a limited lifespan (24hrs) due to regulatory compliance. Monitor token expiration and implement proper renewal mechanisms in your application.

### Refresh Token Support

For applications requiring extended session management or automatic token renewal capabilities, please contact our development team at [support@arrow.trade](mailto:support@arrow.trade) to discuss refresh token implementation.

## Security Best Practices

Security Recommendations

  * Store your `appSecret` securely and never expose it in client-side code
  * Implement proper error handling for authentication failures
  * Use HTTPS for all authentication requests
  * Regularly rotate your application credentials
  * Monitor for unusual authentication patterns

## Troubleshooting

Error | Cause | Solution
---|---|---
Invalid checksum | Incorrect SHA256 generation | Verify concatenation format: `appID:appSecret:request-token`
Token expired | Request token timeout | Restart authentication flow
Invalid redirect | Unregistered redirect URL | Update redirect URL in Developer Portal
