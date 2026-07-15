# WebSocket Implementation

WebSocket streaming is an efficient way to receive market and order related communication over a long standing connection.

## Key Advantages

1. **Efficiency** - Rather than continuously polling for updates, websockets enable data to be pushed to clients as it becomes available
2. **Real-time Communication** - Critical for trading platforms where timing matters significantly
3. **Reduced Overhead** - A single persistent connection eliminates repeated connection establishment costs

## When to Use WebSockets

- Real-time data reception is necessary
- Update frequency is high, making traditional API polling impractical
- Minimizing network overhead is important

## Streaming Options Available

Upstox provides two categories of websocket streams:

1. **Market-related changes** for subscribed entities
2. **Order-related updates**

## Streamer Functions

SDK helper methods for trading platforms to connect to websocket feeds for live market data and portfolio updates.
