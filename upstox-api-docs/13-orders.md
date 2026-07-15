# Orders

The Orders section provides endpoints for comprehensive order management across NSE, BSE, and MCX exchanges. Place, modify, cancel, and track stock orders in real time.

## Important Notices

- If you represent a business aiming to incorporate order flow management (including placing, canceling, and modifying orders), please visit the Uplink Business.
- Customers without DDPI/POA must use a combination of CDSL TPIN and OTP to authorize securities deduction from demat accounts during delivery sale transactions.

## Order Placement & Modification Endpoints

### Place Order V3
Slicing orders with full configuration support.

### Place Multi Order
Batch orders in a single request.

### Modify Order V3
Update pending/open orders (current version).

### Modify Order
Update pending/open orders (legacy version).

## Order Cancellation Endpoints

### Cancel Order V3
Cancel single orders.

### Cancel Multi Order
Bulk cancellation of multiple orders.

### Exit All Positions
Close all positions at once.

## Order Retrieval Endpoints

### Get Order Details
Latest status by order ID.

### Get Order History
Full state transitions for an order.

### Get Order Book
Complete daily overview of all orders.

## Trade Management Endpoints

### Get Trades
Executed trades for the current day.

### Get Order Trades
Fills for specific orders.

### Get Trade History
Historical data with filtering support.
