# Static IP Management

Static IPs are registered at **user level**, not per OAuth client — the same registration applies regardless of which app issued the token. Once enforcement is active, order traffic originating from an unregistered IP may be rejected.

## Operational Rules

- Static IPs can be changed only **once per calendar week**.
- A successful update **invalidates existing access tokens**; the OAuth flow must be completed again.
- `primary_ip` and `secondary_ip` must use standard IPv4 or IPv6 notation and must differ from each other.

---

## Get Static IPs

API to retrieve the **primary** and optional **secondary** static IP addresses registered for your **user account** (static IPs are managed at user level). The same registration applies regardless of which OAuth client issued your token.

When static-IP enforcement applies to order placement, requests from unregistered IPs may fail. For My Apps UI steps and platform rules, see the [My Apps guide](https://upstox.com/developer/api-documentation/appendix/my-apps-support-for-algo-trading-circular) .

Registered addresses are returned in standard **IPv4** or **IPv6** notation.

### Endpoint

**GET** `https://api.upstox.com/v2/user/ip`

### Response

```json
{
  "status": "success",
  "data": {
    "primary_ip": "122.181.101.247",
    "secondary_ip": "128.1.1.2",
    "primary_ip_updated_at": "2026-04-03 17:17:50",
    "secondary_ip_updated_at": "2026-04-03 17:17:50"
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | User-level static IP configuration for the authenticated account. |
| data.primary_ip | string | Registered primary static IP (IPv4 or IPv6, standard notation) from which API order traffic must originate once enforcement is active. |
| data.secondary_ip | string | Registered secondary static IP (IPv4 or IPv6, standard notation) for backup or failover, if configured. May be omitted or `null` if never set. |
| data.primary_ip_updated_at | string | Timestamp when the primary IP was last updated (server time). |
| data.secondary_ip_updated_at | string | Timestamp when the secondary IP was last updated, if configured. May be omitted or `null` if never set. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1179 | **You are not allowed to access this app.** - Returned when the authenticated user or token is not permitted to read static IP configuration for this account. |
| UDAPI1180 | **App is inactive.** - The OAuth client (API app) used for this token is inactive; activate it before calling this API. |
| UDAPI1181 | **Static IP configuration is not available for this application type.** - Static IP registration is not enabled for this client or account type. |

Invalid or expired access tokens and other gateway-level failures follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Check the `errors` array for `message` , `error_code` , and related fields.

---

## Update Static IPs

API to update the **primary** and optional **secondary** static IP addresses for your **user account** (user-level registration). The same IPs apply across your API usage regardless of which OAuth client issued the token.

**Platform rules** (aligned with [My Apps guide](https://upstox.com/developer/api-documentation/appendix/my-apps-support-for-algo-trading-circular) ):

- Static IPs can only be changed **once per calendar week** .
- After a successful update, the **existing access tokens are invalidated** and you need to generate a new one.
- When enforcement is active, orders may be rejected unless traffic originates from a **registered** IP.
- **primary_ip** and **secondary_ip** must use standard **IPv4** or **IPv6** address notation.

### Endpoint

**PUT** `https://api.upstox.com/v2/user/ip`

### Request Body

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| primary_ip | Required | string | Primary static IP (IPv4 or IPv6, standard notation) from which API order traffic must originate once enforcement is active. |
| secondary_ip | Optional | string | Optional secondary static IP (IPv4 or IPv6, standard notation) for backup or failover. Omit the field if you do not need a secondary IP. |

### Response

```json
{
  "status": "success",
  "data": {
    "primary_ip": "122.181.101.247",
    "secondary_ip": "128.1.1.2",
    "primary_ip_updated_at": "2026-04-03 17:17:50",
    "secondary_ip_updated_at": "2026-04-03 17:17:50",
    "access_tokens_invalidated": true
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | User-level static IP configuration for the authenticated account after the update. |
| data.primary_ip | string | Registered primary static IP (IPv4 or IPv6, standard notation). |
| data.secondary_ip | string | Registered secondary static IP, if configured (IPv4 or IPv6, standard notation). May be omitted or `null` if not set. |
| data.primary_ip_updated_at | string | Timestamp when the primary IP was last updated (server time). |
| data.secondary_ip_updated_at | string | Timestamp when the secondary IP was last updated, if configured. May be omitted or `null` if never set. |
| data.access_tokens_invalidated | boolean | When `true` , existing access tokens were invalidated; complete the OAuth flow again for a new token. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1179 | **You are not allowed to update this app.** - Returned when the authenticated user or token is not permitted to update static IPs for this account. |
| UDAPI1180 | **App is inactive.** - The OAuth client (API app) used for this token is inactive; activate it before updating static IPs. |
| UDAPI1181 | **Static IP configuration is not available for this application type.** - Static IP registration is not enabled for this client or account type. |
| UDAPI1182 | **Primary IP is required.** - The request body must include `primary_ip` . |
| UDAPI1183 | **Invalid IP.** - The supplied value is not valid IPv4 or IPv6 address notation. |
| UDAPI1184 | **Primary and secondary IP must be different.** - `primary_ip` and `secondary_ip` must not be the same. |
| UDAPI1185 | **Static IP can only be updated once per week.** - Wait until the weekly cooldown ends before changing static IPs again. |
| UDAPI1186 | **Static IP was updated by another request. Please retry.** - A concurrent update completed; submit your request again. |

Invalid or expired access tokens and other gateway-level failures follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Check the `errors` array for `message` , `error_code` , and related fields.
