# Rate Limits

## Order API Rate Limit

Applies to order-related endpoints ([Place](03-orders.md#place-order) / [Modify](03-orders.md#modify-order) / [Cancel](03-orders.md#cancel-order) / [Exit SNO](03-orders.md#exit-sno-order) Order, and similar).

| Time Frame | Rate Limit |
| --- | --- |
| Per Second | 10 |
| Per Minute | 40 |

> Accounts registered for **more than 10 orders per second** (see [Introduction](01-introduction.md#more-than-10-orders-per-second)) are provisioned with a higher limit.

## API Rate Limit

Applies to all other (non-order) API endpoints.

| Time Frame | Rate Limit |
| --- | --- |
| Per Second | 40 |
| Per Minute | 200 |

## The published limits are a ceiling, not a guarantee (observed)

> **Not in the official documentation.** Recorded from live behaviour.

The tables above are what a fully-provisioned account is allowed. Individual
accounts can be provisioned **lower** — and on a live account observed
2026-09-01 the real non-order ceiling was **10/sec and 120/min**, not the
published 40/200. Those are exactly the figures TradeSmart publishes for its
general budget on the same Noren backend, which suggests 10/120 is the platform
default and the 40/200 table above describes the higher tier from
[Introduction](01-introduction.md#more-than-10-orders-per-second).

The only place the real figure appears is the rejection text itself:

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid Input : Order Recieved 11 in a current second exceeds Limit 10 for user"
}
```

Note that this is reported against a **non-order** endpoint too, despite the
message saying "Order Recieved" — the wording is generic, so it cannot be used
to tell which of the two budgets was breached. Read the `Limit N` value and the
window it names ("current second" / "current minute") instead. The broker's
spelling of "Recieved" is reproduced verbatim; match it case-insensitively on
`exceeds Limit` rather than on the whole sentence.

A client that only retries with backoff will keep re-offering a request rate the
account was never provisioned for. Parse the ceiling out of `emsg` and lower the
local cap for the session. OpenAlgo does this in
`broker/flattrade/api/rate_limit.py::note_rate_limit_rejection`; the cap can
also be pinned up front with `FLATTRADE_MAX_PER_SECOND` /
`FLATTRADE_MAX_PER_MINUTE` (and `FLATTRADE_ORDER_MAX_PER_SECOND` /
`FLATTRADE_ORDER_MAX_PER_MINUTE` for the order budget).

OpenAlgo therefore defaults to 9/sec and 110/min for data (margin applied), not
to the published figures — starting at the published cap meant discovering the
real one by being rejected, once per process restart.

