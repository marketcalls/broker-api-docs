# Binary Decoding Guide

[Market Data Stream](08-market-data-stream.md) events arrive as binary payloads (commonly viewed as hex dumps) rather than JSON, for compact and fast transmission. This walks through converting a raw hex payload into the decimal values described in each event's packet structure.

## Number Format Primer

| Base | Digits | Example |
| --- | --- | --- |
| Binary (base-2) | 0-1 | `1011` = 11 decimal |
| Decimal (base-10) | 0-9 | `155` |
| Hexadecimal (base-16) | 0-9, A-F | `9B` = 155 decimal |

Each hex digit represents 4 bits, so one byte (8 bits) is always exactly two hex characters (e.g. `10`, `F3`).

## Step-by-Step Conversion

Given a raw hex dump of a Market Feed / Depth event:

```
00000000: 10 F3 01 00 74 00 00 00 E4 54 75 00 58 F6 01 00
00000010: EC EE 01 00 97 F3 01 00 77 F5 01 00 63 F2 01 00
...
```

1. **Strip the framing.** Drop the leading address offsets (`00000000:`, `00000010:`, ...) and any trailing ASCII interpretation column — keep only the hex byte values.
2. **Concatenate into one hex string** with no whitespace, e.g. `10F3010074000000E454750058F60100...`.
3. **Split into byte groups** per the event's packet structure (4-byte or 2-byte groups, i.e. 8 or 4 hex characters each), e.g. `10F30100`, `74000000`, `E4547500`, `58F60100`, ...
4. **Reverse each group's byte order** — values are little-endian, so a 4-byte group like `10F30100` becomes `0001F310`.
5. **Convert each reversed group to decimal.** E.g. `0001F310` → `127760`; `00000074` → `116`.
6. **Divide price fields by `priceDivisor`** (located at bytes 58-61 of the Market Feed packet). If the divisor is `100`, a raw LTP of `127760` becomes `1277.6`.
7. **Convert any timestamp fields** from Unix epoch to a human-readable format.
8. **Recover `exchange`/`instrumentId` from the topic name**, e.g. topic `nseeq/2885` → `exchange = NSEEQ`, `instrumentId = 2885`.
9. **Assemble the final record**, e.g.:

   | Field | Value |
   | --- | --- |
   | `exchange` | NSEEQ |
   | `instrumentId` | 2885 |
   | `ltp` | 1277.6 |
   | `lastTradedQuantity` | 116 |
   | `tradedVolume` | 7689444 |
   | `high` | 1286 |

Apply the same 9 steps to any of the [Market Data Stream](08-market-data-stream.md) event types — only the packet layout (field names, byte offsets, group sizes) changes.
