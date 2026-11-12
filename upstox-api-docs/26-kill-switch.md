# Kill Switch

The Kill Switch is a risk-management control that lets a user halt trading in specific exchange segments. When a segment is disabled all pending orders in it are cancelled and new orders are blocked.

## Operational Rules

- All open positions in a segment must be closed before that segment can be disabled.
- A **12-hour cooling period** applies after disabling a segment before it can be re-enabled.
- The access token must be regenerated after a kill switch change for it to take effect.
- A segment that is already `INACTIVE` or dormant cannot have the kill switch enabled — trading is blocked there already.
- If any segment in a multi-segment request fails, none of the segments in that request are updated.

---

## Kill Switch Status

API to fetch the current Kill Switch status and segment status for all trading segments associated with the user's account. The segment status represents the account-level state of the segment and is independent of the Kill Switch. While toggling the [Kill Switch](https://upstox.com/uplearn/structure-courses/trade-risk-management/avoid-destructive-behaviors/) restricts trading activity as a risk management feature to help traders avoid impulsive decisions, it does not change the segment's underlying `ACTIVE` or `INACTIVE` designation.

### Endpoint

**GET** `https://api.upstox.com/v2/user/kill-switch`

### Response

```json
{
    "status": "success",
    "data": [
        {
            "segment": "MCX_FO",
            "segment_status": "INACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "NCD_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "NSE_EQ",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": true
        },
        {
            "segment": "BCD_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "BSE_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "NSE_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": true
        },
        {
            "segment": "BSE_EQ",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": true
        },
        {
            "segment": "NSE_COM",
            "segment_status": "INACTIVE",
            "kill_switch_enabled": false
        }
    ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` |
| data | array | List of kill switch status entries for each trading segment |
| data[].segment | string | Exchange segment identifier (e.g. `NSE_EQ` , `BSE_FO` , `MCX_FO` ) |
| data[].segment_status | string | Whether the segment is currently enabled for the user. Possible values: `ACTIVE` , `INACTIVE` |
| data[].kill_switch_enabled | boolean | `true` if the kill switch is currently engaged for this segment, halting trading activity |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1181 | **The specified segment does not exist.** - The segment value provided is not a valid trading segment. |

---

## Update Kill Switch

API to enable or disable one or more trading segments in a single request. The kill switch is a risk management tool that lets traders temporarily halt activity in specific segments to avoid emotionally-driven or compulsive trading decisions. When a segment is disabled, all pending orders in that segment are cancelled and new orders are blocked.

For more information on the kill switch and how it helps with trade risk management, [click here](https://upstox.com/uplearn/structure-courses/trade-risk-management/avoid-destructive-behaviors/) .

- All open positions in a segment must be closed before you can disable it.
- After disabling a segment, a **12-hour cooling period** applies before it can be re-enabled.
- All open orders in the segment are cancelled automatically when it is disabled.
- If your given segment is inactive or dormant kill switch cannot be enabled as trading is already blocked. You can only enable kill switch for segments that are currently active.

### Endpoint

**POST** `https://api.upstox.com/v2/user/kill-switch`

### Request Body

The request body is an array of segment update objects. You can update multiple segments in a single call.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| segment | string | Yes | Trading segment to update. Possible values: `BSE_EQ` , `NSE_EQ` , `NCD_FO` , `BCD_FO` , `NSE_FO` , `BSE_FO` , `MCX_FO` , `NSE_COM` |
| action | string | Yes | Action to perform. Possible values: `ENABLE` , `DISABLE` |

- After calling the kill switch API, you must regenerate your access token for the kill switch to take effect.
- If any segment in the request fails to update, none of the other segments in the same request will be updated.

### Response

```json
{
    "status": "success",
    "data": [
        {
            "segment": "MCX_FO",
            "segment_status": "INACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "NCD_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "NSE_EQ",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": true
        },
        {
            "segment": "BCD_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "BSE_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": false
        },
        {
            "segment": "NSE_FO",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": true
        },
        {
            "segment": "BSE_EQ",
            "segment_status": "ACTIVE",
            "kill_switch_enabled": true
        },
        {
            "segment": "NSE_COM",
            "segment_status": "INACTIVE",
            "kill_switch_enabled": false
        }
    ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` |
| data | array | Updated kill switch status for each requested segment |
| data[].segment | string | Exchange segment identifier (e.g. `NSE_EQ` , `BSE_FO` , `MCX_FO` ) |
| data[].segment_status | string | This is an account-level segment status and it remains independent of the kill switch. Activating the kill switch will block trading, but it will not change the segment's status between `ACTIVE` and `INACTIVE` . |
| data[].kill_switch_enabled | boolean | `true` if the kill switch is now engaged for this segment |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1184 | **Segment status cannot be changed until all open positions are closed.** - Close all open positions in the segment before attempting to change its status. |
| UDAPI1185 | **Cannot enable segment — cooling period is still in effect.** - A mandatory waiting period applies after disabling a segment. Retry after the cooling period expires. |
| UDAPI1186 | **The specified segment does not exist.** - The segment value provided is not a valid trading segment. |
| UDAPI1187 | **Failed to update segment status due to an error processing open orders.** - An internal error occurred while processing open orders. Retry the request or contact support. |
| UDAPI1188 | **Invalid action. Allowed values are ENABLE and DISABLE.** - The `action` field must be exactly `ENABLE` or `DISABLE` . |
