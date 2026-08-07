# Login

> Source: https://firstock.in/api/docs/login/

> This document provides developers with an in-depth guide to using the Login API for the Firstock trading platform

## Overview

The **Login API** allows an authorized user to authenticate with Firstock by providing their credentials and other required fields. Upon successful login, the API returns a user token or session key that must be used in subsequent requests.

**Key benefits:**

1. **Secure Authentication** using hashed passwords and TOTP (if applicable).
2. **Session Management** through a token-based system.
3. **Access Control** to various trading and market data endpoints.

## Endpoint & Method

`POST` `/login`

**URL**:

```
https://api.firstock.in/V1/login
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Login API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account. | AB1234 |
| password | string | Yes | Hashed password for secure authentication. | 56b9fced7d672de2...d55b77f476ee |
| TOTP | string | Yes (if TOTP is enabled) | One-time password or 2FA code. | 123456 |
| vendorCode | string | Yes | Unique partner/vendor code provided by Firstock. | AB1234_API |
| apiKey | string | Yes | Your Firstock-issued API key. | 34ffc4587242fa66a03ba8ce6801f3c9 |

**Request**

```json
{
  "userId": "{{userId}}",
  "password": "{{password}}",  #Convert to SHA256
  "TOTP": "{{TOTP}}",
  "vendorCode": "{{vendorCode}}",
  "apiKey": "{{apiKey}}"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/login' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "password": "{{password}}",   #Convert to SHA256
    "TOTP": "{{TOTP}}",
    "vendorCode": "{{vendorCode}}",
    "apiKey": "{{apiKey}}"
}'
```

**Python**

```python
from firstock import firstock
login = firstock.login(
    userId="{{userID}}",
    password="{{Password}}",
    TOTP="{{TOTP}}",
    vendorCode="{{vendorCode}}",
    apiKey="{{apiKey}}",
  )

print(login)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.login(
  {
    userId: "{{userId}}",
    password: "Password@123",
    TOTP: "1234",
    vendorCode: "AA123_API",
    apiKey: "NVDewefds2343q2334",
  },
  (err, result) => {
    console.log("Error, ", err);
    console.log("Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

loginRequest := Firstock.LoginRequest{
		UserId:     "{{userID}}",
		Password:   "{{password}}",
		TOTP:       "{{totp}}",
		VendorCode: "{{vendorCode}}",
		APIKey:     "{{apiKey}}",
	}
login, err := Firstock.Login(loginRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", login)
```

## Password encryption

Please find the link below for password conversion

[SHA 256 conversion](https://emn178.github.io/online-tools/sha256.html?ref=wikiconnect.thefirstock.com)

## Response Structure

**Success Response**

If the credentials and API key are valid, you will receive a 200 OK status with a JSON response containing the following fields:

1. **status:** Indicates a successful request (e.g., *"success"*).
2. **message:** Provides a short description of the outcome (e.g., *"Login successful"*).
3. **data:** An object containing user-specific information and the session token (susertoken, jKey, or similar).

**Important:** Save the susertoken (or jKey) securely. You must include this token in subsequent requests to authorized endpoints.

**Failure Response**

If any required fields are missing or invalid, you will receive a 400 or 401 status code with a structure like:

1. **status:** Typically *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **name:** Brief error label or name (e.g., *"MISSING_FIELD"*, *"INVALID_CREDENTIALS"*).

**error:** An object detailing the specific field error.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Login successful",
    "data": {
    "actid": "AB1234",
    "userName": "DEMO",
    "susertoken": "b6339fa5006155c2ae3611892cd80e0b8ae6cbe0dee0",
    "email": "example@gmail.com"
      }
  }
```

**400**

```json
{
    "status": "failed",
    "code": "400",
    "name": "MISSING_FIELD",
    "error": {
    "field": "vendorCode",
    "message": "vendorCode cannot be empty"
    }
  }
```

## Usage & Best Practices

1. **Secure Storage of Tokens**

  - Immediately store the session token (*susertoken*, *jKey*) in a safe manner. Consider using environment variables or encrypted storage if you’re building a client-side application.
2. **API Rate Limits**

  - Check your account or developer plan for any rate limits on authentication requests. Excessive login attempts could lead to temporary blocking or throttling.
3. **Session Lifespan**

  - Some tokens may expire after a certain period of inactivity. Make sure to handle token refresh scenarios or re-login if requests start failing due to session expiration.
4. **Error Handling**

  - When the response status is *"failed"*, inspect the *error.field* and *error.message* to identify the missing or invalid parameter. Prompt the user or your application to rectify the issue.
5. **Two-Factor Authentication (TOTP)**

  - If your account requires *TOTP*, ensure you generate the correct code at the time of login. If *TOTP* is disabled, this field may not apply.
6. **Vendor Code & API Key Management**

  - Do not share or expose your *vendorCode* or *apiKey* publicly (e.g., in GitHub repositories). Rotate them periodically for enhanced security.

**Conclusion**

The **Login API** is your first step toward accessing the full suite of Firstock trading and market data services. By following the guidelines and best practices in this document, you can ensure a smooth, secure authentication experience. If you encounter issues beyond what’s covered here, consult the official support channels or documentation for additional troubleshooting tips.
