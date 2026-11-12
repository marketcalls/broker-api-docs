<!-- Source: https://vortex.rupeezy.in/docs/2.2/killswitch/ -->

# Killswitch

Killswitch lets a trader disable trading on an entire exchange segment for their own account, and enable it back again later. Once a segment is disabled, no order can be placed on it through any channel — api, web or mobile — until the segment is enabled again.

Use the below apis to see and manage killswitch:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/user/killswitch](#current-killswitch-status) | Fetch current status of all segments | 1/sec |
| `GET` | [{{base_url}}/user/killswitch/history](#killswitch-history) | Fetch killswitch action history | 1/sec |
| `POST` | [{{base_url}}/user/killswitch](#update-killswitch) | Enable or disable segments | 1/sec |

## Segments

The following values are accepted wherever a segment is expected:

| value | description |
| --- | --- |
| `NSE_EQ` | Equity cash. Covers both NSE and BSE cash — they are activated and deactivated together |
| `NSE_FO` | NSE equity derivatives |
| `BSE_FO` | BSE equity derivatives |
| `MCX_FO` | Commodity derivatives |

> [!NOTE]
>
> A segment can only be managed through killswitch if it is already activated on the account. Segments that were never activated do not appear as enabled and cannot be enabled through this api — use the segment activation flow for that.

## Current Killswitch Status

```
Endpoint: {{base_url}}/user/killswitch
```

Returns the current enabled/disabled state of every segment on the account, along with the time at which the state last changed. The state is derived from the account's activation records and the current trading configuration, so it reflects what the trader can actually trade right now.

### Killswitch Status Response

```
{
    "status": "success",
    "message": "success",
    "data": {
        "nse_enabled": true,
        "nse_action_time": "2025-06-12T11:04:32Z",
        "nse_fo_enabled": false,
        "nse_fo_action_time": "2025-09-17T09:21:07.482Z",
        "bse_enabled": false,
        "bse_action_time": "0001-01-01T00:00:00Z",
        "bse_fo_enabled": true,
        "bse_fo_action_time": "2025-06-12T11:04:32Z",
        "mcx_enabled": true,
        "mcx_action_time": "2025-06-12T11:04:32Z",
        "status": "",
        "client_code": "DEMO001"
    }
}
```

| field | description |
| --- | --- |
| `nse_enabled` | Whether equity cash (NSE and BSE) is currently enabled for trading |
| `nse_action_time` | Time at which the equity cash state last changed |
| `nse_fo_enabled` | Whether NSE equity derivatives is currently enabled |
| `nse_fo_action_time` | Time at which the NSE derivatives state last changed |
| `bse_fo_enabled` | Whether BSE equity derivatives is currently enabled |
| `bse_fo_action_time` | Time at which the BSE derivatives state last changed |
| `mcx_enabled` | Whether commodity derivatives is currently enabled |
| `mcx_action_time` | Time at which the commodity state last changed |
| `client_code` | Client code of the trader |

> [!NOTE]
>
> `bse_enabled` and `bse_action_time` are reserved for a future split of the cash segment. BSE cash is currently reported through `nse_enabled` along with NSE cash, so these two fields should not be used to drive your logic.

An action time of `0001-01-01T00:00:00Z` means no activation or killswitch action has ever been recorded for that segment.

## Killswitch History

```
Endpoint: {{base_url}}/user/killswitch/history
```

Returns every killswitch action taken on the account in the last 30 days, most recent first.

### Killswitch History Response

```
{
    "status": "success",
    "message": "success",
    "data": [
        {
            "ID": 4127,
            "CreatedAt": "2025-09-17T09:21:07.482Z",
            "UpdatedAt": "2025-09-17T09:21:07.482Z",
            "DeletedAt": null,
            "exchange": "NSE_FO",
            "action": false,
            "status": "Success",
            "is_admin_action": false,
            "client_code": "DEMO001"
        },
        {
            "ID": 4126,
            "CreatedAt": "2025-09-16T05:48:11.903Z",
            "UpdatedAt": "2025-09-16T05:48:11.903Z",
            "DeletedAt": null,
            "exchange": "MCX_FO",
            "action": true,
            "status": "Success",
            "is_admin_action": false,
            "client_code": "DEMO001"
        }
    ]
}
```

| field | description |
| --- | --- |
| `ID` | Unique id of the history entry |
| `CreatedAt` | Time at which the action was taken. This is the timestamp the [cooling period](#cooling-period) is measured from |
| `UpdatedAt` | Time at which the entry was last updated |
| `exchange` | Segment the action was taken on. See [Segments](#segments) |
| `action` | `true` if the segment was enabled, `false` if it was disabled |
| `status` | Result of the action. `Success` for a completed action |
| `is_admin_action` | `true` if the action was taken by the broker rather than by the trader |
| `client_code` | Client code of the trader |

> [!NOTE]
>
> Only the last 30 days of history are returned. There is no pagination on this endpoint.

## Update Killswitch

```
Endpoint: {{base_url}}/user/killswitch
```

Enables and/or disables segments in a single call. Both lists are optional individually, but at least one of them must be non-empty.

### Update Killswitch Object

```
{
    "enable_exchanges": ["MCX_FO"],
    "disable_exchanges": ["NSE_FO", "BSE_FO"]
}
```

| field | Required | description |
| --- | --- | --- |
| `enable_exchanges` | O | Segments to enable for trading. See [Segments](#segments) |
| `disable_exchanges` | O | Segments to disable for trading. See [Segments](#segments) |

### Update Killswitch Response

#### Success

```
{
    "status": "success",
    "message": "Modified user preferences successfully"
}
```

#### Error

```
{
    "status": "error",
    "message": "You have open positions/orders. Please sqaure off/cancel all open positions/orders to proceed further."
}
```

| field | description |
| --- | --- |
| `status` | Possible values: [`success`, `error`] |
| `message` | Description of the result, or of the error if any |

The call returns `400` when the request cannot be accepted, and `500` when the change could not be applied. Common messages are listed below.

| http status | message | meaning |
| --- | --- | --- |
| `400` | `please provide exchanges to take action on` | Both `enable_exchanges` and `disable_exchanges` were empty |
| `400` | `You have open positions/orders. Please sqaure off/cancel all open positions/orders to proceed further.` | There are open intraday positions or pending orders on a segment you are trying to disable |

## Before disabling a segment

A segment can only be disabled if there is nothing left open on it. The request is rejected if, on any segment in `disable_exchanges`:

- there is an open day position with a non-zero quantity in any product other than `DELIVERY`, or
- there is an order in a pending state — either pending at the exchange or still pending with us

Square off the positions and cancel the orders first, then retry. Use the [positions](14-positions.md#fetch-all-positions) and [orderbook](07-regular-order.md#fetching-order-book) apis to check.

> [!WARNING]
>
> Disabling a segment does not square off anything by itself and does not touch existing delivery holdings. It only stops new orders from being accepted on that segment.

## Cooling period

Once a segment is disabled, it cannot be enabled again for **8 hours** from the time of the disable action. This cooling period is the whole point of killswitch — it is what makes the decision hard to reverse in the heat of the moment.

The time the cooling period is measured from is available in two places:

- the `*_action_time` field for that segment in the [killswitch status](#current-killswitch-status) response
- the `CreatedAt` of the corresponding [history](#killswitch-history) entry

Enabling a segment has no cooling period — a segment can be disabled again immediately after it is enabled.

> [!NOTE]
>
> Use the action time to show the trader when the segment becomes eligible again, rather than letting them fire a request that will be rejected.

## Things to keep in mind

- Killswitch acts on the whole account, not on a single api application. A segment disabled through the api is also disabled on web and mobile, and a segment disabled from the web is also disabled for the api.
- The change takes effect at the order management layer. Orders placed on a disabled segment are rejected before they reach the exchange.
- Equity cash cannot be disabled separately for NSE and BSE. `NSE_EQ` disables both.
- Currency derivatives cannot be managed through killswitch.
- Actions taken by the broker appear in history with `is_admin_action` set to `true`. These count towards the cooling period in exactly the same way.
