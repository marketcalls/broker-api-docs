> Source: https://docs.arrow.trade/python-sdk/authentication/

# Authentication

The PyArrow SDK provides secure OAuth-based authentication with support for manual web-based login and fully automated login with TOTP integration.

## Prerequisites

Before authenticating, ensure you have:

  * Valid Arrow user credentials
  * Registered redirect URL in the [Developer Apps](https://app.arrow.trade) section
  * Your `appID` and `appSecret` from the Trading API section
  * Static IP registered (mandatory per [SEBI Circular](https://www.sebi.gov.in/legal/circulars/feb-2025/safer-participation-of-retail-investors-in-algorithmic-trading_91614.html))

## Authentication Methods

### Method 1: Web-based Login (Manual)

This method redirects users to Arrow's login page for authentication.

```python
from pyarrow_client import ArrowClient

# Initialize the client
client = ArrowClient(app_id="your_app_id")

# Step 1: Get the login URL
login_url = client.login_url()
print(f"Please visit: {login_url}")

# Step 2: User completes login and gets redirected to your callback URL
# Extract the request_token from the callback URL query parameters

# Step 3: Exchange request token for access token
client.login(
    request_token="token_from_callback_url",
    api_secret="your_app_secret"  # also accepts app_secret=
)

# Verify authentication
print(f"Access Token: {client.get_token()}")
```

Token exchange endpoint

The SDK posts to `https://api.arrow.trade/auth/app/authenticate-token` and sends both `checkSum` and `checksum` in the JSON body. Trading REST calls use `https://edge.arrow.trade` via `root_url`.

Callback URL

After successful login, Arrow redirects to your registered URL with:

  * `request-token`: Temporary authentication token
  * `checksum`: SHA256 hash for verification

### Method 2: Automated Login (TOTP)

For fully automated systems, use the `auto_login` method with TOTP.

Parameter | Required | Description
---|---|---
`user_id` | ✓ | Arrow user ID
`password` | ✓ | Account password
`api_secret` or `app_secret` | ✓ | Application secret from Developer Apps (either keyword accepted)
`totp_secret` | ✓ | Base32 TOTP secret

```python
from pyarrow_client import ArrowClient

client = ArrowClient(app_id="your_app_id")

# Automated login with all credentials
client.auto_login(
    user_id="your_user_id",
    password="your_password",
    api_secret="your_app_secret",  # alias: app_secret=
    totp_secret="your_totp_secret"  # Base32 TOTP secret
)

# Client is now authenticated
print(f"Logged in successfully!")
print(f"Token: {client.get_token()}")
```

TOTP Secret

The `totp_secret` is the base32 encoded secret used to generate time-based one-time passwords. You can go to the [profile page](https://app.arrow.trade/profile) and copy the TOTP secret if enabled. If not enabled, log out of the current session and click on forgot password and complete the flow.

## Session Management

### Get Current Token

```python
# Retrieve the current access token
token = client.get_token()
# Equivalent: token = client.token
print(f"Current token: {token}")
```

### Set Token Manually

If you have a valid token from a previous session:

```python
# Set an existing token
client.set_token("your_existing_access_token")
```

### Invalidate Session

Clear the current session and token:

```python
# Logout and clear session
client.invalidate_session()
print("Session invalidated")
```

## Token Lifecycle

Aspect | Details
---|---
**Validity** | 24 hours from generation
**Refresh** | New login required after expiration
**Storage** | Store securely; never expose in client-side code

Token Expiration

Access tokens expire after 24 hours due to regulatory compliance. Implement proper token refresh mechanisms in your application.

## Authentication Response

Successful authentication returns user details:

```python
response = client.login(
    request_token="your_request_token",
    app_secret="your_app_secret"
)

print(response)
# {
#     "name": "ABHISHEK JAIN",
#     "token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9...",
#     "userID": "AJ0001"
# }
```

Field | Type | Description
---|---|---
`name` | string | User's full name
`token` | string | JWT access token
`userID` | string | Unique user identifier

## User Information

After authentication, retrieve user details:

```python
# Get user profile
user = client.get_user_details()
print(f"User: {user}")

# Get trading limits and margins
limits = client.get_user_limits()
print(f"Available margin: {limits}")
```

## Error Handling

Handle authentication errors gracefully:

```python
from pyarrow_client import ArrowClient

client = ArrowClient(app_id="your_app_id")

try:
    client.auto_login(
        user_id="your_user_id",
        password="your_password",
        app_secret="your_app_secret",
        totp_secret="your_totp_secret"
    )
    print("Login successful!")

except Exception as e:
    print(f"Authentication failed: {e}")
```

### Common Errors

Error | Cause | Solution
---|---|---
Invalid checksum | Incorrect SHA256 generation | Verify `appID:appSecret:request-token` format
Token expired | Request token timeout | Restart authentication flow
Invalid credentials | Wrong user ID or password | Verify credentials
Invalid TOTP | Incorrect or expired OTP | Check TOTP secret and system time sync

## Security Best Practices

Security Notice

  * **Never** expose `appSecret` in client-side code
  * **Never** commit credentials to version control
  * **Always** use environment variables for sensitive data
  * **Always** use HTTPS for all API communications

### Environment Variables Example

```python
import os
from pyarrow_client import ArrowClient

client = ArrowClient(app_id=os.environ["ARROW_APP_ID"])

client.auto_login(
    user_id=os.environ["ARROW_USER_ID"],
    password=os.environ["ARROW_PASSWORD"],
    app_secret=os.environ["ARROW_app_secret"],
    totp_secret=os.environ["ARROW_TOTP_SECRET"]
)
```

## Complete Example

```python
import os
from pyarrow_client import ArrowClient

def initialize_arrow_client():
    """Initialize and authenticate Arrow client."""

    # Initialize client
    client = ArrowClient(app_id=os.environ["ARROW_APP_ID"])

    # Automated login
    try:
        client.auto_login(
            user_id=os.environ["ARROW_USER_ID"],
            password=os.environ["ARROW_PASSWORD"],
            app_secret=os.environ["ARROW_app_secret"],
            totp_secret=os.environ["ARROW_TOTP_SECRET"]
        )
        print("✓ Authentication successful")

        # Verify by fetching user details
        user = client.get_user_details()
        print(f"✓ Logged in as: {user.get('name', 'Unknown')}")

        return client

    except Exception as e:
        print(f"✗ Authentication failed: {e}")
        return None

# Usage
if __name__ == "__main__":
    client = initialize_arrow_client()
    if client:
        # Your trading logic here
        pass
```
