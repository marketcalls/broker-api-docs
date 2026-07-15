# GTT Orders (Good Till Triggered)

Comprehensive functionality for managing Good Till Triggered (GTT) orders - orders that are automatically executed when specified trigger conditions (price targets) are met.

## Endpoints

### Place GTT Order

**Method:** POST

Place a Good Till Triggered (GTT) order using the Upstox API. Set trigger conditions for automatic execution when price targets are met.

### Modify GTT Order

**Method:** PUT

Modify existing GTT orders. Update trigger price, quantity, or order parameters as required.

### Cancel GTT Order

**Method:** DELETE

Remove pending GTT orders by order ID and confirm the deletion instantly.

### Get GTT Order Details

**Method:** GET

Get the latest status and details of a GTT order. Retrieve trigger conditions, execution status, and order parameters by order ID.
