# Payments

Endpoints for inspecting fund movements on the account and for managing withdrawals (payouts) over NEFT or IMPS.

---

## Get Payins

API to retrieve the pay-in (fund deposit) transactions for the authenticated user. It returns details such as amount, payment mode, current status, bank name, transaction ID, and applicable charges. The response includes the most recent 20 transactions.

### Endpoint

**GET** `https://api.upstox.com/v2/user/payments/payin`

### Response

```json
{
    "status": "success",
    "data": [
        {
            "amount": 16995.00,
            "mode": "NEFT",
            "status": "SUCCESS",
            "currency": "INR",
            "bank_name": "AXIS BANK",
            "transaction_id": "qws_0426_9680091",
            "created_at": "2026-04-19 16:35:36"
        },
        {
            "amount": 100,
            "mode": "UPI",
            "status": "SUCCESS",
            "currency": "INR",
            "bank_name": "AXIS BANK",
            "transaction_id": "order_Sx67XZ8jTEAHiJ",
            "created_at": "2026-06-03 14:17:27"
        }
    ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | array | List of pay-in transaction records. |
| data[].amount | number | Transaction amount in rupees. |
| data[].mode | string | Payment mode. For e.g. `NET_BANKING` , `UPI` , `QR` , `NEFT` etc. |
| data[].currency | string | Currency code. Always `INR` . |
| data[].status | string | Current status of the pay-in. One of `PENDING` , `SUCCESS` , `FAILED` , `CANCELLED` . |
| data[].bank_name | string | Name of the bank associated with the transaction. |
| data[].transaction_id | string | Unique identifier for the transaction. |
| data[].created_at | string | Date and time of the transaction creation in `yyyy-MM-dd HH:mm:ss` format. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Ensure the request is authenticated.

---

## Get Payouts

API to retrieve the payout (fund withdrawal) transactions for the authenticated user. It returns details such as amount, payment mode, current status, bank name, transaction ID, and applicable charges. The response includes the most recent 20 transactions.

### Endpoint

**GET** `https://api.upstox.com/v2/user/payments/payout`

### Response

```json
{
    "status": "success",
    "data": [
        {
            "transaction_id": "qws_0426_9680091",
            "status": "COMPLETED",
            "mode": "NEFT",
            "amount": 16995.00,
            "currency": "INR",
            "eta": "2026-04-19 13:30:00",
            "created_at": "2026-04-19 13:25:56",
            "bank_name": "AXIS BANK"
        },
        {
            "transaction_id": "imps_0426_7654321",
            "status": "TRANSFER_IN_PROGRESS",
            "mode": "IMPS",
            "amount": 10000.00,
            "currency": "INR",
            "eta": "2026-04-19 12:35:00",
            "created_at": "2026-04-19 12:30:00",
            "bank_name": "ICICI BANK"
        }
    ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | array | List of payout transaction records. |
| data[].transaction_id | string | Unique identifier for the transaction. |
| data[].status | string | Current status of the payout. One of `RECEIVED` , `VALIDATING` , `APPROVED` , `TRANSFER_IN_PROGRESS` , `COMPLETED` , `REJECTED` , `REVERSED` . |
| data[].mode | string | Payment mode. One of `NEFT` or `IMPS` . |
| data[].amount | number | Transaction amount in rupees. |
| data[].currency | string | Currency code. Always `INR` . |
| data[].eta | string | Estimated completion time (YYYY-MM-DD HH:MM:SS). |
| data[].created_at | string | Transaction creation timestamp (YYYY-MM-DD HH:MM:SS). |
| data[].bank_name | string | Name of the bank associated with the transaction. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Ensure the request is authenticated.

---

## Get Payout Modes

API to retrieve the available fund withdrawal (payout) modes and eligibility criteria for the authenticated user. Returns details for NEFT (Standard) and IMPS (Instant) modes, including the minimum and maximum withdrawal limits, current eligibility status, and the amount available for withdrawal.

For IMPS-specific eligibility conditions, see [Instant Withdrawal Eligibility](https://upstox.com/developer/api-documentation/appendix/instant-withdrawal-eligibility) .

The Payout APIs are subject to a separate rate limit. For more information, please check [here](https://upstox.com/developer/api-documentation/rate-limiting#payout-apis) .

### Endpoint

**GET** `https://api.upstox.com/v2/user/payments/payout/modes`

### Response

```json
{
    "status": "success",
    "data": {
        "neft": {
            "status": "ENABLED",
            "eligible": true,
            "min_amount": 100.0,
            "max_amount": 200000000.0,
            "currency": "INR",
            "eligible_amount": 15000.0
        },
        "imps": {
            "status": "ENABLED",
            "eligible": false,
            "min_amount": 100.0,
            "max_amount": 500000.0,
            "currency": "INR",
            "eligible_amount": 0.0
        }
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | object | Map of available payout modes. |
| data.neft | object | Standard (NEFT) withdrawal mode details. |
| data.neft.status | string | Availability status of the NEFT mode, either `ENABLED` or `DISABLED` . |
| data.neft.eligible | boolean | Whether the user is eligible for NEFT withdrawal. |
| data.neft.min_amount | number | Minimum withdrawal amount across platform in INR. |
| data.neft.max_amount | number | Maximum withdrawal amount across platform in INR. |
| data.neft.currency | string | Currency code. Always `INR` . |
| data.neft.eligible_amount | number | Amount currently available for NEFT withdrawal in INR. |
| data.imps | object | Instant (IMPS) withdrawal mode details. |
| data.imps.status | string | Availability status of the IMPS mode. |
| data.imps.eligible | boolean | Whether the user is eligible for IMPS withdrawal. |
| data.imps.min_amount | number | Minimum withdrawal amount across platform in INR. |
| data.imps.max_amount | number | Maximum withdrawal amount across platform in INR. |
| data.imps.currency | string | Currency code. Always `INR` . |
| data.imps.eligible_amount | number | Amount currently available for IMPS withdrawal in INR. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Ensure the request is authenticated.

---

## Payout Request

API to place a fund withdrawal (payout) request for the authenticated user. Supports Standard (NEFT) and Instant (IMPS) withdrawal modes. The withdrawal is credited to the user's registered **primary bank account** .

- Use the [Get Payout Modes](https://upstox.com/developer/api-documentation/get-payout-modes) API to fetch the modes available and eligible withdrawal amount to your account along with the minimum and maximum withdrawal amounts for each mode before placing a request.
- **NEFT (Standard):** Free of charge.
- **IMPS (Instant):** Credited within minutes subject to eligibility.
**Fee:** ₹20 + GST ( **Basic plan** ); Free ( **Plus plan** ).
- Only one active withdrawal request is allowed at a time.
- IMPS requests cannot be edited once initiated.
- The Payout APIs are subject to a separate rate limit. For more information, please check [here](https://upstox.com/developer/api-documentation/rate-limiting#payout-apis) .

### Endpoint

**POST** `https://api.upstox.com/v2/user/payments/payout`

### Instant Withdrawal Eligibility

IMPS (Instant) withdrawals are subject to real-time eligibility checks. See [Instant Withdrawal Eligibility](https://upstox.com/developer/api-documentation/appendix/instant-withdrawal-eligibility) for the full list of criteria.

### Request Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| mode | string | Yes | Withdrawal mode. One of `NEFT` (Standard) or `IMPS` (Instant). |
| amount | number | Yes | Withdrawal amount in INR. Must satisfy the min/max bounds for the selected mode. |

### Response

```json
{
    "status": "success",
    "data": {
        "transaction_id": "ABC123XYZ-GC0173-7HIMPSABC",
        "status": "received",
        "mode": "IMPS",
        "amount": 5000.0,
        "currency": "INR",
        "eta": "2026-04-19 13:30:00",
        "created_at": "2026-04-19 13:25:56",
        "bank_name": "AXIS BANK",
        "message": "Your instant withdrawal request has been received. Funds will be credited within 5 minutes."
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | object | Payout transaction record. |
| data.transaction_id | string | Unique identifier for the payout transaction. |
| data.status | string | Current state of the payout. One of `RECEIVED` , `VALIDATING` , `APPROVED` , `TRANSFER_IN_PROGRESS` , `COMPLETED` , `REJECTED` , `REVERSED` . |
| data.mode | string | Resolved payout mode. One of `NEFT` or `IMPS` . |
| data.amount | number | Withdrawal amount in INR. |
| data.currency | string | Currency code. Always `INR` . |
| data.eta | string | Estimated completion time (YYYY-MM-DD HH:MM:SS). |
| data.created_at | string | Transaction creation timestamp (YYYY-MM-DD HH:MM:SS). |
| data.bank_name | string | Display name of the destination bank. |
| data.message | string | User-facing status message. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) .

| Error Code | Description |
| --- | --- |
| UDAPI1215 | Payout mode is required. |
| UDAPI1216 | Payout mode must be `NEFT` or `IMPS` . |
| UDAPI1217 | Payout amount is required. |
| UDAPI1218 | Payout amount must be at least 100. |
| UDAPI100072 | The Funds service is accessible from 5:30 AM to 12:00 AM IST daily. Please try again during these service hours. |
| UDAPI100500 | Your withdrawal amount cannot be greater than your available to withdraw balance. |
| UDAPI100500 | Another withdrawal request is already active. Only one pending payout is allowed at a time. |
| UDAPI100500 | User account is inactive, dormant, or not eligible for the selected mode. |
| UDAPI100500 | Primary bank account not found. |

---

## Modify Payout

API to update the amount of an existing pending fund withdrawal (payout) request. Only requests currently in `RECEIVED` status can be modified. **IMPS** requests cannot be edited once initiated.

The eligibility and withdrawal fee criteria described in [Payout Request](https://upstox.com/developer/api-documentation/payout-request) also apply to modifying a payout.

Replace `{transaction_id}` with the `transaction_id` returned by the [Payout Request](https://upstox.com/developer/api-documentation/payout-request) API.

### Endpoint

**PUT** `https://api.upstox.com/v2/user/payments/payout/{transaction_id}`

### Request Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| amount | number | Yes | Updated withdrawal amount in INR. Must satisfy the min/max bounds for the mode of the original request. |

### Response

```json
{
    "status": "success",
    "data": {
        "transaction_id": "ABC123XYZ-GC0173-7HIMPSABC",
        "status": "received",
        "mode": "NEFT",
        "amount": 10000.0,
        "currency": "INR",
        "eta": "2026-04-19 14:00:00",
        "created_at": "2026-04-19 13:25:56",
        "bank_name": "AXIS BANK",
        "message": "Your withdrawal request has been updated successfully."
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | object | Updated payout transaction record. |
| data.transaction_id | string | Unique identifier for the payout transaction. |
| data.status | string | Current state of the payout. One of `RECEIVED` , `VALIDATING` , `APPROVED` , `TRANSFER_IN_PROGRESS` , `COMPLETED` , `REJECTED` , `REVERSED` . |
| data.mode | string | Updated resolved payout mode. One of `NEFT` or `IMPS` . |
| data.amount | number | Updated withdrawal amount in INR. |
| data.currency | string | Currency code. Always `INR` . |
| data.eta | string | Updated estimated completion time (YYYY-MM-DD HH:MM:SS). |
| data.created_at | string | Original transaction creation timestamp (YYYY-MM-DD HH:MM:SS). |
| data.bank_name | string | Display name of the destination bank. |
| data.message | string | User-facing status message. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) .

| Error Code | Description |
| --- | --- |
| UDAPI1217 | Payout amount is required. |
| UDAPI1218 | Payout amount must be at least 100. |
| UDAPI100500 | Withdrawal request cannot be modified. |
| UDAPI100500 | Your withdrawal amount cannot be greater than your available to withdraw balance. |
| UDAPI100072 | The Funds service is accessible from 5:30 AM to 12:00 AM IST daily. Please try again during these service hours. |

---

## Cancel Payout

API to cancel a pending fund withdrawal (payout) request for the authenticated user. Only requests currently in `RECEIVED` status can be cancelled. Once a request moves to processing, it can no longer be cancelled. **IMPS** requests cannot be cancelled once initiated.

Replace `{transaction_id}` with the `transaction_id` returned by the [Payout Request](https://upstox.com/developer/api-documentation/payout-request) API.

### Endpoint

**DELETE** `https://api.upstox.com/v2/user/payments/payout/{transaction_id}`

### Response

```json
{
    "status": "success",
    "data": {
        "transaction_id": "ABC123XYZ-GC0173-7HIMPSABC",
        "message": "Your withdrawal request of Amount 110.10 is deleted successfully."
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | object | Cancellation confirmation record. |
| data.transaction_id | string | Unique identifier of the cancelled payout transaction. |
| data.message | string | User-facing confirmation message. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) .

| Error Code | Description |
| --- | --- |
| UDAPI100500 | Withdrawal request cannot be cancelled. The request may no longer be in received status. |
| UDAPI100500 | Transaction not found or does not belong to the authenticated user. |
