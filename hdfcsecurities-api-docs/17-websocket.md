# Market Data - Websocket

> Source: https://developer.hdfcsec.com/ir-docs/docs/market_data_websocket

The WebSocket API offers the most efficient method for receiving real-time quotes across all exchanges during live market hours, optimizing speed, latency, resource usage, and bandwidth. Each quote includes key fields such as open, high, low, close, last traded price, and up to five levels of bid/offer market depth.

Users can subscribe to live quotes for up to 1500 instruments on a single WebSocket connection, and each API key supports simultaneous upto three WebSocket connections without any limit.

## Websocket Endpoint

```js
'wss://developer.hdfcsec.com/wsapi/v1/session'
```

## Message to subscribe and unsubscribe the scripts

```json
{
  "heart_beat": false,
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

Subscription `type` values seen in the official sample: `LTP`, `ALL`, `GREEK`.

## HeartBeat Packet

```json
{
  "heart_beat": true
}
```

## Prefix for each Exchange and segment

| Exchange | Segment | Prefix |
| --- | --- | --- |
| BSE | CM | BSE_**(TOKEN)** |
|  | FO | BFO_**(TOKEN)** |
|  | INDEX | BSE_INDEX_**(TOKEN)** |
| NSE | CM | NSE_**(TOKEN)** |
|  | FO | NFO_**(TOKEN)** |
|  | CD | NCD_**(TOKEN)** |
|  | INDEX | NSE_INDEX_**(TOKEN)** |
| MCX | FO | MCX_**(TOKEN)** |

> The unsubscribe sample uses a `CDS_` prefix (`CDS_3002`) while the table documents `NCD_` for the
> NSE currency segment. Both appear in the official page.

## Packet Types and their meanings

Packet types let us know which fields to use/are present in the proto. Denoted by field "PacketType" in GenericDTO

| Packet Type | Fields to Use |
| --- | --- |
| **HEARTBEAT** | NA, only packetType field will come |
| **MARKET_STATUS** | **GenericDTO.marketStatusData**<br>Exchange exchange = 1;<br>MarketStatusSegment segment = 2;<br>MarketStatus status = 3;<br>string segmentId =4; |
| **NSE_CD_OI**<br>**NSE_FO_OI**<br>**BSE_FO_OI** | **GenericDTO.mbpData** |
| **NSE_CM_ALL**<br>**NSE_CD_ALL**<br>**NSE_FO_ALL**<br>**BSE_CM**<br>**BSE_FO_ALL**<br>**MCX_PKT** | **GenericDTO.mbpData** |
| **NSE_CM_CIRC**<br>**NSE_CD_CIRC**<br>**NSE_FO_CIRC** | **GenericDTO.mbpData** |
| **NSE_FO_GREEK**<br>**BSE_FO_GREEK** | **GenericDTO.greekData** |
| **NSE_INDEX**<br>**BSE_INDEX** | **GenericDTO.indexData** |
| **ORDER**<br>**TRADE** | **GenericDTO.order**<br>**GenericDTO.trade** |

> The table references `GenericDTO.marketStatusData` and a `MarketStatusSegment` type, but the
> shipped `.proto` declares the field as `MarketStatus marketStatus = 4;` and has no
> `MarketStatusSegment` message. Decode against the `.proto`, not this table.

## Proto File to use

Original download:
<https://developer.hdfcsec.com/ir-docs/assets/files/GenericDTO3-7527bc03756bb132bd39c0eefdae7d35.proto>

A copy is checked in alongside this page as [`GenericDTO3.proto`](GenericDTO3.proto).

---

## Appendix: GenericDTO proto schema

The messages and enums below are the subset needed to decode the market data feed. The complete
schema — including the `Order`, `Trade`, `OrderConfig`, `ErrorCode` and remaining enums used by the
`ORDER` / `TRADE` packet types — is in [`GenericDTO3.proto`](GenericDTO3.proto).

### Envelope

```protobuf
syntax = "proto3";

message GenericDTOList {
  repeated GenericDTO genericDTOList = 1;
}

message GenericDTO {
  int64 instrumentId = 1;
  MBPData mbpData = 2;
  IndexData indexData = 3;
  MarketStatus marketStatus = 4;
  Order order = 5;
  Trade trade = 6;
  int64 sequenceNo = 7;
  int64 packetTimestamp = 8;
  PacketType packetType = 9;
  GreekData greekData = 10;
}
```

### Quote and depth

```protobuf
message MBPData {
  double lastTradedPrice = 1;
  int64 lastTradeTime = 2;                        // timestamp from BSE
  string netChangeIndicator = 3;
  int32 netPriceChangeFromClosingPrice = 4;
  double openPrice = 5;
  double highPrice = 6;
  double closingPrice = 7;
  double lowPrice = 8;
  int64 volumeTradedToday = 9;
  int64 lastTradeQuantity = 10;
  double averageTradePrice = 11;
  MarketDepthDTOList marketDepthDTOList = 12;
  int64 totalBuyQuantity = 13;
  int64 totalSellQuantity = 14;
  double lowerCircuitLimit = 15;
  double upperCircuitLimit = 16;
  int64 oi = 17;
}

message MarketDepthDTOList {
  repeated MarketDepthDTO marketDepthDTO = 1;
}

message MarketDepthDTO {
  int64 quantity = 1;
  double price = 2;
  int64 numberOfOrders = 3;
  bool buyFlag = 4;
}
```

### Index

```protobuf
message IndexData {
  string indexName = 1;
  double indexValue = 2;
  double highIndexValue = 3;
  double lowIndexValue = 4;
  double openingIndex = 5;
  double closingIndex = 6;
  double percentChange = 7;
  double yearlyHigh = 8;
  double yearlyLow = 9;
  int64 packetTimeStamp = 10;
}
```

### Option Greeks

```protobuf
message GreekData {
  double delta = 1;    // rate of change of option price vs underlying price
  double gamma = 2;    // rate of change of delta vs underlying price
  double vega = 3;     // sensitivity of option price to volatility
  double theta = 4;    // rate of decline in value due to time decay
  double rho = 5;      // sensitivity of option price to interest rates
  string scrip_id = 6;
  string exch = 7;
}
```

### Feed enums

```protobuf
enum PacketType {
  NSE_CM_ALL = 0;
  NSE_CD_ALL = 1;
  NSE_INDEX = 2;
  NSE_FO_ALL = 3;
  BSE_CM = 4;
  BSE_INDEX = 5;
  BSE_FO_ALL = 6;
  MCX_PKT = 7;
  ORDER = 8;
  TRADE = 9;
  NSE_CM_CIRC = 10;
  NSE_CD_CIRC = 11;
  NSE_CD_OI = 12;
  NSE_FO_CIRC = 13;
  NSE_FO_OI = 14;
  BSE_FO_OI = 15;
  HEARTBEAT = 16;
  NSE_FO_GREEK = 17;
  BSE_FO_GREEK = 18;
}

enum MarketStatus {
  PRE_OPEN_START = 0;
  PRE_OPEN_END = 1;
  OPEN = 2;
  CLOSE = 3;
  POST_CLOSE_START = 4;
  POST_CLOSE_END = 5;
  UNAVAILABLE = 6;
}

enum Exchange {
  NSE = 0;
  BSE = 1;
  MCX = 2;
  NEPSE = 3;
  DSE = 4;
  NCDEX = 5;
}

enum Segment {
  Capital = 0;
  FutOpt = 1;
  Currency = 2;
  Commodities = 3;
  SLBM = 4;
}
```

### Order and trade enums

Used by the `ORDER` / `TRADE` packets.

```protobuf
enum OrderType  { LIMIT = 0; MARKET = 1; SL = 2; SLM = 3; SPREAD = 4; }
enum OrderSide  { BUY = 0; SELL = 1; NEUTRAL = 2; }
enum OrderMode  { NEW = 0; MODIFY = 1; CANCEL = 2; SQUAREOFF = 3; }
enum Validity   { DAY = 0; IOC = 1; GTC = 2; GTD = 3; GTT = 4; FOK = 5; AON = 6; }
enum ProCli     { CLIENT = 0; PROP = 1; WAREHOUSE = 2; }

enum ProdType {
  NRML = 0;  CNC = 1;  MIS = 2;  BTST = 3;
  AMO_MIS = 4;  AMO_NRML = 5;  AMO_CNC = 6;  AMO_BTST = 7;
  BO_MIS = 8;   BO_NRML = 9;   BO_CNC = 10;  BO_BTST = 11;
  CO_MIS = 12;  CO_NRML = 13;  CO_CNC = 14;  CO_BTST = 15;
  MTF = 16;
  OCO_MIS = 17; OCO_NRML = 18; OCO_CNC = 19; OCO_BTST = 20;
}

enum ExecutionType {
  UNKNOWN_TYPE = 0; REGULAR = 1; AMO = 2; BO = 3; CO = 4;
  SPD = 5; HDG = 6; OCO = 7; NML = 8; AUCTION = 9; ICEBERG = 10;
}

enum Status {
  ACCEPTED = 0;              CONFIRMED = 1;             REJECTED = 2;
  PENDING = 3;               MODIFY_ACCEPTED = 4;       MODIFY_CONFIRMED = 5;
  MODIFY_REJECTED = 6;       MODIFY_PENDING = 7;        CANCEL_ACCEPTED = 8;
  CANCEL_CONFIRMED = 9;      CANCEL_REJECTED = 10;      CANCEL_PENDING = 11;
  PARTIAL_TRADE = 12;        SL_TRIGGER_CONFIRMED = 13; COMPLETE = 14;
  BATCH_CANCEL_CONFIRMED = 15;
  AMO_REQ_RECEIVED = 16;     AMO_REQ_CONFIRMED = 17;    AMO_REQ_MODIFIED = 18;
  AMO_CANCEL_CONFIRMED = 19; AMO_NEW_CONFIRMED = 20;    AMO_MODIFY_CONFIRMED = 21;
  BRACKET_ORDER_CONFIRMED = 22;      BRACKET_ORDER_MODIFIED = 23;
  BRACKET_ORDER_CANCELLED = 24;      BRACKET_ORDER_COMPLETE_TRADE = 25;
  ORDER_PRICE_CONFIRMATION = 26;     BRACKET_ORDER_REJECTED = 31;
  BASKET_ORDER_ACCEPTED = 32;        RRM_PENDING_AT_EXCHANGE = 33;
  RMS_VALIDATION_COMPLETED = 49;     EXCHANGE_RESPONSE_PENDING = 50;
  UNACCEPTED = 51;
}
```

> Note the enum values here are the **streaming** vocabulary and do not match the REST vocabulary:
> the proto uses `SLM`, `NRML`/`CNC`/`MIS`, while the REST order APIs use `SL-M` and
> `DELIVERY`/`OVERNIGHT`/`INTRADAY`/`MTF`.
