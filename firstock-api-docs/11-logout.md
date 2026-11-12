# Logout

> Source: https://firstock.in/api/docs/logout/

> This document provides a detailed guide to using the Logout API for the Firstock trading platform

## Overview

The **Logout API** invalidates the active session token, effectively terminating the user’s authenticated session. After a successful logout, you will be required to re-authenticate via the **Login API** before accessing any restricted endpoints.

**Key benefits:**

1. **Session Security:** Ensures tokens are invalidated when a user logs out.
2. **Controlled Access:** Prevents further requests or trades from being placed once the session is terminated.
3. **Easy Integration:** A simple *POST*request that requires minimal parameters.

## Endpoint & Method

`POST` `/logout`

**URL**:

```
https://api.firstock.in/V1/logout
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Logout API request. All fields marked as Mandatory must be included.

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
curl --location 'https://api.firstock.in/V1/logout' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
logout = firstock.logout(userId="{{userId}}")
print(logout)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.logout(
 {
	userId: "{{userId}}"
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

logout, err := Firstock.Logout("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", logout)
```

## Response Structure

**Success Response**

If the session is successfully invalidated, you will receive a **200 OK** status with a JSON response containing:

1. **status:** Indicates a successful request (e.g., "*success*").
2. **message:** Provides a short description of the outcome (e.g., "*Successfully logged out*").

**Important:** After this response, the userToken used for this session becomes invalid. Any subsequent request using the same token will fail.

**Failure Response**

If any required fields are missing or invalid, or if the token is already invalid, you may receive a **400** or **401** status code with details such as:

1. **status:** Typically *"failed"*.
2. **code:** An error code (e.g., *"401"*).
3. **name:** A brief error label (e.g., *"INVALID_JKEY"*, *"INVALID_USERID"*).

**error:** An object detailing the specific field error.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Successfully logged out"
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

1. **Token Invalidation**

  - Once you call the Logout API, the provided userToken or jKey becomes invalid. You cannot reuse it for further actions without logging in again.
2. **Timely Logout**

  - Encourage users to log out after each session for improved security, especially in public or shared environments.
3. **Error Handling**

  - Verify the response status. If it is "failed", check the error.field and error.message for more details (e.g., a missing or incorrect userToken).
4. **Session Management**

  - If you handle multiple users or sessions, ensure you store and invalidate the correct token for each session.

**Conclusion**

The **Logout API** is a straightforward but critical endpoint for maintaining session security within the Firstock trading ecosystem. By ensuring you invalidate user sessions when they are no longer needed, you protect your application and user data from unauthorized access. If you experience any issues or unexpected responses, refer to Firstock’s support resources or documentation for assistance.
