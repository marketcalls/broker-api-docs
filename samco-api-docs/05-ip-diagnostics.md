# IP Diagnostics

Confirm which public IP address Samco sees for your requests.

## Who Am I

`GET /ip/whoami`

A read-only diagnostic that reports **which source IP our server sees you calling from**, plus your currently-registered `PRIMARY` and `SECONDARY` IPs, and whether the source IP matches one of them.

> **TIP** — Use this to debug `403 — The IP is not the registered static IP`
>
> When an order-related endpoint rejects your request with HTTP 403 and `statusMessage: "The IP is not the registered static IP"`, call `/ip/whoami` from the *same host* that was rejected. The response tells you the exact IP our server sees you from — often different from what a third-party "what is my IP" lookup reports due to NAT, corporate proxies, multi-pod egress, or fallback hosts.
>
> This endpoint **does not** consume your SEBI weekly IP-update slot. It is purely informational.

### Authentication

Requires a valid session token in the `x-session-token` header (same as `/quote/getQuote`). Obtain one via [Generate Session Token](04-authentication.md#generate-session-token).

### Parameter

No request body, no query parameters, no path parameters.

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/ip/whoami' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/ip/whoami"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .GET()
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const response = await fetch('https://tradeapi.samco.in/ip/whoami', {
    method: 'GET',
    headers,
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

r = requests.get('https://tradeapi.samco.in/ip/whoami',
  headers=headers)

print(r.json())
```

### Sample Response

**200 - Matched**

```json
{
    "serverTime": "03/06/26 10:46:06",
    "msgId": "d5f083f3-1b04-4b97-9385-1e578fdfeb7a",
    "status": "Success",
    "statusMessage": "Calling from registered PRIMARY IP (203.0.113.10).",
    "srcIp": "203.0.113.10",
    "primaryIp": "203.0.113.10",
    "secondaryIp": "203.0.113.11",
    "matches": true,
    "matchedAs": "PRIMARY"
}
```

**200 - Not matched**

```json
{
    "serverTime": "03/06/26 10:46:06",
    "msgId": "d5f083f3-1b04-4b97-9385-1e578fdfeb7a",
    "status": "Success",
    "statusMessage": "Calling IP (198.51.100.7) is NOT a registered IP. Registered: PRIMARY=203.0.113.10, SECONDARY=203.0.113.11. Order endpoints will reject this host.",
    "srcIp": "198.51.100.7",
    "primaryIp": "203.0.113.10",
    "secondaryIp": "203.0.113.11",
    "matches": false,
    "matchedAs": null
}
```

**401 - Missing/invalid token**

```json
{
    "status": "Failure",
    "statusMessage": "Unauthorized - Session token is mandatory. Please provide session token in 'x-session-token' header"
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | Unique identifier for the API response message. |
| `status` | string | Always `Success` for this endpoint (any failure surfaces as a 4xx HTTP error). |
| `statusMessage` | string | Human-readable summary of the match result. |
| `srcIp` | string | The source IP **our server** sees this request coming from. |
| `primaryIp` | string \| null | The currently-registered `PRIMARY` IP for your app (or default mapping). `null` if none registered. |
| `secondaryIp` | string \| null | The currently-registered `SECONDARY` IP for your app, if any. |
| `matches` | boolean | `true` if `srcIp` equals `primaryIp` or `secondaryIp`; `false` otherwise. |
| `matchedAs` | string \| null | `"PRIMARY"`, `"SECONDARY"`, or `null` — which registered slot the source IP matched, if any. |

### When to call

- **At deploy time** — run from each backend pod / host before going live to confirm the host's source IP will pass IP validation. If `matches: false`, update your registered IP via the [Web Dashboard → Static IPs](03-dashboard.md#static-ips) page before sending order traffic.
- **On a `403 — The IP is not the registered static IP` error** — when an order endpoint rejects a request, call `/ip/whoami` from the failing host. The `srcIp` field is the exact value that needs to match your `PRIMARY` or `SECONDARY`.
- **From a new fallback host** — if you've added a new egress host (e.g. a DR site), call this once from there to confirm before routing real traffic through it.

> **WARNING** — Read-only — does not change anything
>
> This endpoint never modifies your IP allowlist and never consumes your SEBI weekly IP-update slot. To change your registered IPs, use the [Web Dashboard](03-dashboard.md#static-ips).
