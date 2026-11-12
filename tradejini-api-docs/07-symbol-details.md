# Symbol Details

Scrip master (instrument) reference data. Use these endpoints to look up the `symId` values required by the order and market-data APIs.

## Scrip Master Groups

`GET /api/mkt-data/scrips/symbol-store`

$54

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `version` | `integer (int32)` | Yes | Enter the version |

### Example Request

```bash
curl -X GET "https://example.com/api/mkt-data/scrips/symbol-store?version=0"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `no-data`, `error` |
| `d` | `object` | Example: `{"version": "20240115", "updated": "2024-01-15T04:00:00Z", "symbolStore": "https://api.tradejini.com/v2/static/symbols/20240115.json"}` |
| `d.version` | `integer (int32)` |  |
| `d.updated` | `boolean` |  |
| `d.symbolStore` | `array<object>` |  |
| `d.symbolStore[].name` | `string` |  |
| `d.symbolStore[].sortOrder` | `integer (int32)` |  |
| `d.symbolStore[].idFormat` | `string` |  |
| `d.symbolStore[].data` | `string` |  |
| `d.symbolStore[].buildVersion` | `array<string>` |  |
| `d.symbolStore[].append` | `object` |  |
| `d.symbolStore[].append.data` | `string` |  |
| `d.symbolStore[].append.buildVersion` | `array<string>` |  |

**Example**

```json
{
  "s": "ok",
  "d": {
    "version": "20240115",
    "updated": "2024-01-15T04:00:00Z"
  }
}
```

---

## Scrip Master Data

`GET /api/mkt-data/scrips/symbol-store/{scripGroup}`

- Get complete list of scrips based on the group passed in path.
- This request accepts two types of response format: text/plain and application/json.
- **text/plain:** Normal plain string in csv format, rows separated with newline and columns separated with `,` (comma).
- **application/json:** List of scripts in a json array format. But usually slower than plain text format due to its larger size.

### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scripGroup` | `string` | Yes | Enter symbol categories to download. Values: `CommodityOptions`, `FutureContracts`, `CommodityFuture`, `NSEOptions`, `CurrencyOptions`, `BSEOptions`, `CurrencyFuture`, `Securities`, `Spot`, `Index` |

### Example Request

```bash
curl -X GET "https://example.com/api/mkt-data/scrips/symbol-store/CommodityOptions"
```

### Responses

#### 200 OK

OK

Content-Type: `text/plain`

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `no-data`, `error` |
| `d` | `array<object>` |  |
| `d[].id` | `string` |  |
| `d[].isin` | `string` |  |
| `d[].dispName` | `string` |  |
| `d[].desc` | `string` |  |
| `d[].excToken` | `string` |  |
| `d[].lot` | `string` |  |
| `d[].tick` | `string` |  |
| `d[].expiry` | `string` |  |
| `d[].strike` | `string` |  |
| `d[].optType` | `string` |  |
| `d[].weekly` | `string` |  |
| `d[].asset` | `string` |  |
| `d[].instrument` | `string` |  |
| `d[].symbol` | `string` |  |
| `d[].series` | `string` |  |
| `d[].exchange` | `string` |  |
| `d[].freezeQty` | `string` |  |
| `d[].undId` | `string` |  |
| `d[].trdUnit` | `string` |  |
| `d[].lotMulti` | `string` |  |

**Example**

```json
{
  "s": "ok",
  "d": [
    {
      "id": "EQT_RELIANCE_EQ_NSE",
      "isin": "INE002A01018",
      "dispName": "RELIANCE",
      "desc": "RELIANCE INDUSTRIES LTD",
      "excToken": "2885",
      "lot": 1,
      "tick": 0.05,
      "asset": "equity",
      "instrument": "EQUITY",
      "symbol": "RELIANCE",
      "series": "EQ",
      "exchange": "NSE",
      "freezeQty": 67662
    }
  ]
}
```
