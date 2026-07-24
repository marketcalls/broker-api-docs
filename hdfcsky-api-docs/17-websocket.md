# Market Data - WebSocket

> Source: https://developer.hdfcsky.com/sky-docs/docs/websocket

The WebSocket API offers the most efficient method for receiving real-time quotes across all exchanges during live market hours, optimizing speed, latency, resource usage, and bandwidth. Each quote includes key fields such as open, high, low, close, last traded price, and up to five levels of bid/offer market depth.

Users can subscribe to live quotes for up to 300 instruments on a single WebSocket connection, and each API key supports simultaneous upto three WebSocket connections without any limit.

## Websocket Endpoint

```js
'ws://uat-developer.hdfcsky.com/wsapi/v1/session'
```

## Message to subscribe and unsubscribe the scripts

```json
{
  "heart_beat" : false,
    "subscribe": [
        {
            "scripId": "BSE_1",
            "type": "LTP"
        },
        {
            "scripId": "BSE_16675",
            "type": "ALL"
        }
    ],
    "unSubscribe": [
        {
            "scripId": "CDS_3002",
            "type": "ALL"
        },
        {
            "scripId": "CDS_3003",
            "type": "ALL"
        },
        {
            "scripId": "BFO_3004",
            "type": "GREEK"
        },
        {
            "scripId": "BSE_1021",
            "type": "ALL"
        }
    ]
}
```

## HeartBeat Packet

```json
{
  "heart_beat": true
}
```

## Prefix for each Exchange and segment

| Exchange | Segment | Prefix |
|---|---|---|
| BSE | CM | BSE_**(TOKEN)** |
|  | FO | BFO_**(TOKEN)** |
|  | INDEX | BSE_INDEX_**(TOKEN)** |
| NSE | CM | NSE_**(TOKEN)** |
|  | FO | NFO_**(TOKEN)** |
|  | CD | NCD_**(TOKEN)** |
|  | INDEX | NSE_INDEX_**(TOKEN)** |
| MCX | FO | MCX_**(TOKEN)** |

## Packet Types and their meanings

Packet types let us know which fields to use/are present in the proto. Denoted by field "PacketType" in GenericDTO

| Packet Type | Fields to Use |
|---|---|
| **HEARTBEAT** | NA, only packetType field will come |
| **MARKET_STATUS** | **GenericDTO.marketStatusData** Exchange exchange = 1; MarketStatusSegment segment = 2; MarketStatus status = 3; string segmentId =4; |
| **NSE_CD_OI** **NSE_FO_OI** **BSE_FO_OI** | **GenericDTO.mbpData** |
| **NSE_CM_ALL** **NSE_CD_ALL** **NSE_FO_ALL** **BSE_CM** **BSE_FO_ALL** **MCX_PKT** | **GenericDTO.mbpData** |
| **NSE_CM_CIRC** **NSE_CD_CIRC** **NSE_FO_CIRC** | **GenericDTO.mbpData** |
| **NSE_FO_GREEK** **BSE_FO_GREEK** | **GenericDTO.greekData** |
| **NSE_INDEX** **BSE_INDEX** | **GenericDTO.indexData** |
| **ORDER** **TRADE** | **GenericDTO.order** **GenericDTO.trade** |

## Proto File to use

[download](https://developer.hdfcsky.com/sky-docs/assets/files/GenericDTO3-7527bc03756bb132bd39c0eefdae7d35.proto)
