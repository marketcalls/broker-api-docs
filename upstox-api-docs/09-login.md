# Login

The Login section serves as a central hub for authentication-related endpoints and OAuth 2.0 integration.

## Endpoints

### 1. Authorize

Initiate the OAuth 2.0 authorization flow for Upstox API users. Redirect users to the login dialog and obtain an authorization code for token exchange.

### 2. Analytics Token

Generate read-only tokens for accessing market data, holdings, positions, and historical candle information through the Upstox API suite.

### 3. Get Token

Exchange authorization codes for access tokens, returning both the opaque token and user profile information in a single authenticated response.

### 4. Access Token Request

Webhook-based token generation where users authorize token creation and credentials are delivered automatically through designated endpoints.

### 5. Logout

Secure session termination, including access token invalidation and user session closure through dedicated API endpoints.

## Security Features

TOTP (Time-based One-Time Password) is supported as an enhanced two-factor authentication method, offering stronger security compared to standard SMS-based verification codes.
