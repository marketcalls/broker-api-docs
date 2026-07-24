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
