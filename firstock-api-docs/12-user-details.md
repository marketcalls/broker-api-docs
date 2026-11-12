# User Details

> Source: https://firstock.in/api/docs/user-details/

> This document provides an in-depth guide to using the User Details API for the Firstock trading platform.

## Overview

The **User Details API** allows authenticated clients to retrieve pertinent information about the currently logged-in user. This data can be used to display user profiles, identify enabled trading segments, or confirm user privileges.

**Key benefits:**

1. **Centralized Profile Data** Retrieve user name, email, and exchanges in a single request.
2. **Security**Ensures only valid session tokens can access user information.
3. **Integration Ready** Quick check for user privileges (e.g., available order types, exchange permissions).

## Endpoint & Method

`POST` `/userDetails`

**URL**:

```
https://api.firstock.in/V1/userDetails
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the User Details API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | The same user ID used during login. | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login | ce1c4471eb95... |

**Request**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/userDetails' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
userDetails = firstock.userDetails(userId="{{userId}}")
print(userDetails)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.userDetails(
  { userId: "{{userId}}" },
  (err, result) => {
    console.log("getUserDetails Error, ", err);
    console.log("getUserDetails Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

userDetails, err := Firstock.UserDetails("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", userDetails)
```

## Response Structure

**Success Response**

If the *userId*and *jKey*are valid, you will receive a **200 OK** status with a JSON response containing:

1. **status:** Typically *"success"*.
2. **data:** An object holding multiple user-related fields, such as account ID, email, enabled exchanges, and user privileges.

**Key Fields:**

1. *actid*: The user’s account ID (often the same as userId).
2. *email*: The user’s registered email address.
3. *exchange*: An array indicating which exchanges the user can access.
4. *orarr*: Supported order types (e.g., *"MKT"*, *"LMT"*, *"SL-LMT"*, *"SL-MKT"*).
5. *uprev*: Current privilege level (e.g., *"INVESTOR"*).
6. *requestTime*: Timestamp for the request processing.
7. *userName*: Full name of the user.

**Failure Response**

If your *userId*or *jKey*is missing, invalid, or expired, you may receive a **400** or **401** status code with error details:

1. **status:** Typically *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **name:** A short label describing the error (e.g., *"INVALID_JKEY"*).
4. **error:** An object detailing the specific field error.

**Response**

**200**

```json
{
    "status": "success",
    "data": {
        "actid": "AB1234",
        "email": "example@gmail.com",
        "exchange": [
          "NFO",
          "NSE",
          "BSE",
          "BFO"
          ],
          "orarr": [
          "MKT",
          "LMT",
          "SL-LMT",
          "SL-MKT"
          ],
          "requestTime": "10:40:21 23-04-2025",
          "uprev": "INVESTOR",
          "userName": "DEMOFIRSTNAME DEMOMIDDLENAME DEMOKUMAR"
      }
  }
```

**400**

```json
{
    "status": "failed",
    "code": "401",
    "name": "INVALID_JKEY",
    "error": {
      "field": "jKey",
      "message": "jKey parameter is invalid"
    }
  }
```

## Usage & Best Practices

1. **Store Session Tokens Securely**

  - Make sure you’re using the correct jKey (or susertoken) from your most recent successful login.
2. **Check Exchange & Order Types**

  - The fields exchange and orarr can be used to conditionally display or enable features in your trading app. For instance, if NFO is not listed, you can hide or restrict derivatives trading.
3. **Error Handling**

  - If status is "failed" inspect the field and message in error to debug issues (e.g., invalid token, missing user ID).
4. **Session Expiry**

  - Tokens may expire after a certain duration. If you receive repeated INVALID_JKEY errors, prompt the user to log in again.
5. **Minimal Permissions**

  - Tokens may expire after a certain duration. If you receive repeated INVALID_JKEY errors, prompt the user to log in again.

**Conclusion**

The **User Details API** is essential for any application needing real-time profile and account data for a logged-in user. By validating the correct *jKey*and *userId*, you can seamlessly fetch exchanges, order types, and user privilege levels to tailor the user’s trading experience. For further troubleshooting or more in-depth functionality, refer to Firstock’s official documentation or contact support.
