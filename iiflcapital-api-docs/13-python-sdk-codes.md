# Python SDK Errors and Packets

Status, result, and packet-type codes emitted by the Bridge Package's Python SDK (used for [Market Data Stream](08-market-data-stream.md) and [Order and Trade Updates](06-order-and-trade-updates.md)).

## Status Codes

| Code | Message |
| --- | --- |
| 0 | Success, no error |
| 1 | Token is invalid |
| -1 | Generic error |
| 4 | Client is not currently connected |
| 101 | Request cannot be null |
| 102 | TopicList cannot be null and must contain fewer than 1024 topics |
| 103 | Subscription failed |
| 105 | Client is already connected |

## Result Codes

| Code | Message |
| --- | --- |
| 0 | Topic granted |
| 104 | Invalid topic |
| 128 | Topic not granted |

## Acknowledgement Packet Types

| Packet Type | Packet Name |
| --- | --- |
| 2 | Connection acknowledgement |
| 9 | Subscription acknowledgement |
| 11 | Unsubscription acknowledgement |
| 14 | Disconnect acknowledgement |
