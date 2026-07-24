# Order and Trade Updates

The Bridge Package (IIFL's streaming client library) exposes two push-event types — order updates and trade updates — delivered by registering callback functions.

| Event Type | Setter Property | Request Param | Response Format | Description |
| --- | --- | --- | --- | --- |
| Order Updates | `on_order_updates_received` | Client Id | JSON | Real-time order status: modifications, cancellations, execution progress |
| Trade Updates | `on_trade_updates_received` | Client Id | JSON | Real-time notifications of executed trades (price, quantity, time) |

## Connecting and Subscribing (Python SDK Example)

The steps below use the `bridgePy` package for illustration; see the full SDK on IIFL's GitHub for a complete implementation in your language of choice.

1. Install the package: `pip install bridgePy`
2. Import the connector: `from bridgePy import connector as connector`
3. Create a connection object: `connection_object = connector.Connect()`
4. Register acknowledgment and error handlers **before** connecting:

   ```python
   def acknowledgment_handler(response: str):
       print(f"Acknowledgment: {response}")
   connection_object.on_acknowledge_response = acknowledgment_handler

   def error_handler(code: int, message: str):
       print(f"Error {code}: {message}")
   connection_object.on_error = error_handler
   ```

   A successful connection acknowledgment looks like:

   ```json
   { "packetType": 2, "packetName": "CONNACK", "status": 0, "message": "Success" }
   ```

5. Connect, passing `bridge.iiflcapital.com` as host, `8883` as port, and the `userSession` token obtained from [Get User Session](03-user.md#get-user-session):

   ```python
   conn_req = '{"host": "bridge.iiflcapital.com", "port": 8883, "token": <userSession>}'
   connection_object.connect_host(conn_req)
   ```

6. Subscribe to the events you need, passing your client ID:

   ```python
   req = '{"subscriptionList": ["CLIENT101"]}'
   connection_object.subscribe_order_updates(req)
   connection_object.subscribe_trade_updates(req)
   ```

7. Register handlers to receive and process events:

   ```python
   def order_updates_handler(data: bytearray, topic: str):
       print(f"Order updates data received on topic {topic}: {data}")
   connection_object.on_order_updates_received = order_updates_handler

   def trade_updates_handler(data: bytearray, topic: str):
       print(f"trade update data received on topic {topic}: {data}")
   connection_object.on_trade_updates_received = trade_updates_handler
   ```

8. Unsubscribe when no longer needed:

   ```python
   connection_object.unsubscribe_order_updates(req)
   connection_object.unsubscribe_trade_updates(req)
   ```

9. Disconnect when done: `connection_object.disconnect_host()`

## Order Updates

### Packet

```json
{
  "clientId": "31625881",
  "validity": "DAY",
  "orderComplexity": "REGULAR",
  "product": "NORMAL",
  "orderType": "MARKET",
  "tradingSymbol": "IDEA-EQ",
  "transactionType": "BUY",
  "instrumentId": "14366",
  "price": "1500",
  "slTriggerPrice": "1600",
  "quantity": "1",
  "disclosedQuantity": "10",
  "cancelledQuantity": "30",
  "algoId": "algo123",
  "marketProtectionPercent": "1300",
  "placedBy": "31625881",
  "averageTradedPrice": "1510",
  "filledQuantity": "50",
  "pendingQuantity": "25",
  "brokerOrderId": "240807000000068",
  "exchangeOrderId": "900000000000000001",
  "rejectionReason": "RMS:Margin Exceeds,****duct",
  "orderStatus": "rejected",
  "exchangeTimestamp": "07-Aug-2024 16:14:17",
  "exchangeUpdateTime": "07-Aug-2024 16:14:17",
  "mainLegOrderId": "240807000000068",
  "validityDate": "45511",
  "source": "API",
  "comments": "Strangle~dQcOimFMAvsXlum~SELF",
  "brokerUpdateTime": "17-Feb-2025 06:48:39"
}
```

Fields carry the same meaning as [Order Book](05-orders.md#order-book), plus:

| Field | Description |
| --- | --- |
| `validityDate` | Date the order remains valid until, based on the validity type (GTT / GTD / VTD) |
| `comments` | Additional remarks (order tag, app key, app name, etc.) |
| `mainlegOrderId` | Parent order ID, if this order belongs to a Bracket Order |

## Trade Updates

### Packet

```json
{
  "tradedPrice": "1560",
  "filledQuantity": "50",
  "exchangeTradeId": "893487609000000",
  "instrumentId": "14366",
  "exchange": "NSEEQ",
  "clientId": "31625881",
  "orderComplexity": "REGULAR",
  "product": "NORMAL",
  "tradingSymbol": "IDEA-EQ",
  "fillDate": "45511",
  "fillTime": "0.676585648148148",
  "brokerOrderId": "240807000000068",
  "exchangeOrderId": "900000000000000",
  "transactionType": "BUY",
  "orderType": "MARKET",
  "placedBy": "31625881",
  "algoId": "algo123"
}
```

Fields carry the same meaning as [Trade Book](05-orders.md#trade-book), plus:

| Field | Description |
| --- | --- |
| `fillDate` | Date the order was filled |
| `fillTime` | Time the order was filled |
