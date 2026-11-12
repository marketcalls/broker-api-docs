# Fundamentals

Company fundamental data addressed by **ISIN**. Financial statements support `consolidated` and `standalone` types, and annual or quarterly periods. Monetary values are in Indian Rupees (Crore).

---

## Get Company Profile

API to retrieve the company profile for a given ISIN. The response includes a business description, sector classification, and sector market capitalisation in both INR and USD.

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/profile`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Response

```json
{
  "status": "success",
  "data": {
    "company_profile": "Reliance Industries Limited is engaged in the activities of hydrocarbon exploration and production, petroleum refining and marketing, petrochemicals, advanced materials and composites, renewables, retail and digital services.",
    "sector": "Refineries",
    "sector_market_cap_inr": {
      "value": 1942866.05,
      "unit": "crore",
      "formatted": "1,942,866.05 Cr"
    },
    "sector_market_cap_usd": {
      "value": 215.87,
      "unit": "billion",
      "formatted": "$215.87B"
    }
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data.company_profile | string | Detailed business description of the company. |
| data.sector | string | The sector to which the company belongs. |
| data.sector_market_cap_inr | object | Total market capitalisation of the sector in Indian Rupees. |
| data.sector_market_cap_inr.value | number | Numeric market cap value in Crore. |
| data.sector_market_cap_inr.unit | string | Unit of the value. Value: `crore` . |
| data.sector_market_cap_inr.formatted | string | Human-readable formatted value, e.g., `"1,942,866.05 Cr"` . |
| data.sector_market_cap_usd | object | Total market capitalisation of the sector in US Dollars. |
| data.sector_market_cap_usd.value | number | Numeric market cap value in the specified unit. |
| data.sector_market_cap_usd.unit | string | Unit of the value. Possible values: `billion` , `million` . |
| data.sector_market_cap_usd.formatted | string | Human-readable formatted value, e.g., `"$215.87B"` . |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |

---

## Get Balance Sheet

API to retrieve the historical balance sheet data for a company identified by its ISIN. The response contains total assets and total liabilities across multiple reporting periods, and can be filtered by statement type ( `consolidated` or `standalone` ). All monetary values are in Indian Rupees (Crore).

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/balance-sheet`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| type | Optional | string | Financial statement type. Allowed values: `consolidated` , `standalone` . Default: `consolidated` . |
| fs | Optional | boolean | When set to `true` , the response includes a detailed line-item breakdown in the `full_statement` field. |

### Response

```json
{
  "status": "success",
  "data": {
    "type": "consolidated",
    "time_period": "yearly",
    "units_in": "crore",
    "history": [
      { "total_asset": 1950121, "total_liability": 940495, "period": "Mar 2025" },
      { "total_asset": 1755986, "total_liability": 830198, "period": "Mar 2024" },
      { "total_asset": 1607431, "total_liability": 778550, "period": "Mar 2023" },
      { "total_asset": 1499665, "total_liability": 610681, "period": "Mar 2022" }
    ],
    "full_statement": [
      {
        "particular": "Non-Current Assets",
        "history": [
          { "period": "Mar 2025", "value": 1450851 },
          { "period": "Mar 2024", "value": 1285886 },
          { "period": "Mar 2023", "value": 1182135 },
          { "period": "Mar 2022", "value": 1152646 }
        ]
      },
      {
        "particular": "Current Assets",
        "history": [
          { "period": "Mar 2025", "value": 499270 },
          { "period": "Mar 2024", "value": 470100 },
          { "period": "Mar 2023", "value": 425296 },
          { "period": "Mar 2022", "value": 347019 }
        ]
      },
      {
        "particular": "Total Assets",
        "history": [
          { "period": "Mar 2025", "value": 1950121 },
          { "period": "Mar 2024", "value": 1755986 },
          { "period": "Mar 2023", "value": 1607431 },
          { "period": "Mar 2022", "value": 1499665 }
        ]
      },
      {
        "particular": "Current Liabilities",
        "history": [
          { "period": "Mar 2025", "value": 453737 },
          { "period": "Mar 2024", "value": 397367 },
          { "period": "Mar 2023", "value": 395743 },
          { "period": "Mar 2022", "value": 308662 }
        ]
      },
      {
        "particular": "Net Current Asset",
        "history": [
          { "period": "Mar 2025", "value": 45533 },
          { "period": "Mar 2024", "value": 72733 },
          { "period": "Mar 2023", "value": 29553 },
          { "period": "Mar 2022", "value": 38357 }
        ]
      },
      {
        "particular": "Non-Current Liabilities",
        "history": [
          { "period": "Mar 2025", "value": 486758 },
          { "period": "Mar 2024", "value": 432831 },
          { "period": "Mar 2023", "value": 382807 },
          { "period": "Mar 2022", "value": 302019 }
        ]
      },
      {
        "particular": "Equity Capital",
        "history": [
          { "period": "Mar 2025", "value": 1009626 },
          { "period": "Mar 2024", "value": 925788 },
          { "period": "Mar 2023", "value": 828881 },
          { "period": "Mar 2022", "value": 888984 }
        ]
      },
      {
        "particular": "Total Equity & Liabilities",
        "history": [
          { "period": "Mar 2025", "value": 1950121 },
          { "period": "Mar 2024", "value": 1755986 },
          { "period": "Mar 2023", "value": 1607431 },
          { "period": "Mar 2022", "value": 1499665 }
        ]
      }
    ]
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | object | Balance sheet data for the requested statement type and time period. |
| data.type | string | Financial statement type. Possible values: `consolidated` , `standalone` . |
| data.time_period | string | Reporting period. Possible values: `yearly` , `quarterly` . |
| data.units_in | string | Unit of monetary values. Value: `crore` . |
| data.history | array | Summary balance sheet records ordered by reporting period (most recent first). |
| data.history[].total_asset | number | Total assets of the company for the period (in Crore). |
| data.history[].total_liability | number | Total liabilities of the company for the period (in Crore). |
| data.history[].period | string | Reporting period label, e.g., `Mar 2025` . |
| data.full_statement | array | Detailed line-item breakdown of the balance sheet. Present only when `fs=true` is passed. Always reported on an annual basis. |
| data.full_statement[].particular | string | Label for the balance sheet line item, e.g., `Non-Current Assets` , `Current Assets` , `Total Assets` , `Current Liabilities` , `Net Current Asset` , `Non-Current Liabilities` , `Equity Capital` , `Total Equity & Liabilities` . |
| data.full_statement[].history | array | Historical values for the line item across reporting periods. |
| data.full_statement[].history[].period | string | Reporting period label, e.g., `Mar 2025` . |
| data.full_statement[].history[].value | number | Monetary value for the period (in Crore). |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |
| UDAPI1207 | **Invalid type** - Allowed values: `consolidated` , `standalone` . |

---

## Get Income Statement

API to retrieve the historical income statement (profit and loss) data for a company identified by its ISIN. The response groups income data by category (Revenue, Operating profit, Net profit), each with historical values and period-over-period percentage changes. You can filter by statement type ( `consolidated` or `standalone` ) and reporting frequency ( `yearly` or `quarterly` ). All monetary values are in Indian Rupees (Crore).

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/income-statement`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| type | Optional | string | Financial statement type. Allowed values: `consolidated` , `standalone` . Default: `consolidated` . |
| time_period | Optional | string | Reporting period. Allowed values: `yearly` , `quarterly` . Default: `yearly` . |
| fs | Optional | boolean | When set to `true` , the response includes a detailed line-item breakdown in the `full_statement` field. |

### Response

```json
{
  "status": "success",
  "data": {
    "type": "consolidated",
    "time_period": "yearly",
    "units_in": "crore",
    "income_statement": [
      {
        "category": "revenue",
        "history": [
          { "value": 1086181, "period": "Mar 2026", "change": "+10.53%" },
          { "value": 982671, "period": "Mar 2025", "change": "+7.15%" },
          { "value": 917121, "period": "Mar 2024", "change": "+3.1%" },
          { "value": 889569, "period": "Mar 2023" }
        ]
      },
      {
        "category": "operating_profit",
        "history": [
          { "value": 123162, "period": "Mar 2026", "change": "+16.17%" },
          { "value": 106017, "period": "Mar 2025", "change": "+1.61%" },
          { "value": 104340, "period": "Mar 2024", "change": "+10.95%" },
          { "value": 94046, "period": "Mar 2023" }
        ]
      },
      {
        "category": "net_profit",
        "history": [
          { "value": 95610, "period": "Mar 2026", "change": "+18.35%" },
          { "value": 80787, "period": "Mar 2025", "change": "+2.74%" },
          { "value": 78633, "period": "Mar 2024", "change": "+6.13%" },
          { "value": 74088, "period": "Mar 2023" }
        ]
      }
    ],
    "full_statement": [
      {
        "particular": "Revenue",
        "history": [
          { "period": "Mar 2025", "value": 964693 },
          { "period": "Mar 2024", "value": 901064 },
          { "period": "Mar 2023", "value": 877835 },
          { "period": "Mar 2022", "value": 695963 }
        ]
      },
      {
        "particular": "Other Income",
        "history": [
          { "period": "Mar 2025", "value": 17978 },
          { "period": "Mar 2024", "value": 16057 },
          { "period": "Mar 2023", "value": 11734 },
          { "period": "Mar 2022", "value": 14943 }
        ]
      },
      {
        "particular": "Total Revenue",
        "history": [
          { "period": "Mar 2025", "value": 982671 },
          { "period": "Mar 2024", "value": 917121 },
          { "period": "Mar 2023", "value": 889569 },
          { "period": "Mar 2022", "value": 710906 }
        ]
      },
      {
        "particular": "Total Expenses",
        "history": [
          { "period": "Mar 2025", "value": 876654 },
          { "period": "Mar 2024", "value": 812781 },
          { "period": "Mar 2023", "value": 795547 },
          { "period": "Mar 2022", "value": 631883 }
        ]
      },
      {
        "particular": "Profit Before Tax",
        "history": [
          { "period": "Mar 2025", "value": 106017 },
          { "period": "Mar 2024", "value": 104340 },
          { "period": "Mar 2023", "value": 94046 },
          { "period": "Mar 2022", "value": 82154 }
        ]
      },
      {
        "particular": "Tax",
        "history": [
          { "period": "Mar 2025", "value": 25230 },
          { "period": "Mar 2024", "value": 25707 },
          { "period": "Mar 2023", "value": 20376 },
          { "period": "Mar 2022", "value": 15970 }
        ]
      },
      {
        "particular": "Profit After Tax",
        "history": [
          { "period": "Mar 2025", "value": 80787 },
          { "period": "Mar 2024", "value": 78633 },
          { "period": "Mar 2023", "value": 73670 },
          { "period": "Mar 2022", "value": 66184 }
        ]
      },
      {
        "particular": "EPS - Basic",
        "history": [
          { "period": "Mar 2025", "value": 51.47 },
          { "period": "Mar 2024", "value": 51.45 },
          { "period": "Mar 2023", "value": 98.59 },
          { "period": "Mar 2022", "value": 92 }
        ]
      },
      {
        "particular": "EPS - Diluted",
        "history": [
          { "period": "Mar 2025", "value": 51.47 },
          { "period": "Mar 2024", "value": 51.45 },
          { "period": "Mar 2023", "value": 98.59 },
          { "period": "Mar 2022", "value": 90.86 }
        ]
      }
    ]
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | object | Income statement data for the requested statement type and time period. |
| data.type | string | Financial statement type. Possible values: `consolidated` , `standalone` . |
| data.time_period | string | Reporting period. Possible values: `yearly` , `quarterly` . |
| data.units_in | string | Unit of monetary values. Value: `crore` . |
| data.income_statement | array | Income statement categories with historical values ordered by reporting period (most recent first). |
| data.income_statement[].category | string | Income statement category. Possible values: `revenue` , `operating_profit` , `net_profit` . |
| data.income_statement[].history | array | Historical values for the income statement category. |
| data.income_statement[].history[].value | number | Value for the period (in Crore). Negative values indicate a loss. |
| data.income_statement[].history[].period | string | Reporting period label, e.g., `Mar 2026` . |
| data.income_statement[].history[].change | string | Period-over-period percentage change, e.g., `"+10.53%"` . Absent for the oldest period in the series. |
| data.full_statement | array | Detailed line-item breakdown of the income statement. Present only when `fs=true` is passed. Always reported on an annual basis, irrespective of the `time_period` filter. |
| data.full_statement[].particular | string | Label for the income statement line item, e.g., `Revenue` , `Other Income` , `Total Revenue` , `Total Expenses` , `Profit Before Tax` , `Tax` , `Profit After Tax` , `EPS - Basic` , `EPS - Diluted` . |
| data.full_statement[].history | array | Historical values for the line item across reporting periods. |
| data.full_statement[].history[].period | string | Reporting period label, e.g., `Mar 2025` . |
| data.full_statement[].history[].value | number | Monetary value for the period (in Crore). |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |
| UDAPI1207 | **Invalid type** - Allowed values: `consolidated` , `standalone` . |
| UDAPI1208 | **Invalid time period** - Allowed values: `yearly` , `quarterly` . |

---

## Get Cash Flow

API to retrieve the historical cash flow statements for a company identified by its ISIN. The response groups cash flows by category (Operating, Investing, Financing), each with historical values and period-over-period percentage changes. You can filter by statement type ( `consolidated` or `standalone` ). All monetary values are in Indian Rupees (Crore).

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/cash-flow`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| type | Optional | string | Financial statement type. Allowed values: `consolidated` , `standalone` . Default: `consolidated` . |
| fs | Optional | boolean | When set to `true` , the response includes a detailed line-item breakdown in the `full_statement` field. |

### Response

```json
{
  "status": "success",
  "data": {
    "type": "consolidated",
    "time_period": "yearly",
    "units_in": "crore",
    "cash_flow": [
      {
        "category": "operating",
        "history": [
          { "value": 178703, "period": "Mar 2025", "change": "+12.54%" },
          { "value": 158788, "period": "Mar 2024", "change": "+38.04%" },
          { "value": 115032, "period": "Mar 2023", "change": "+3.96%" },
          { "value": 110654, "period": "Mar 2022" }
        ]
      },
      {
        "category": "investing",
        "history": [
          { "value": -137535, "period": "Mar 2025", "change": "-21.09%" },
          { "value": -113581, "period": "Mar 2024", "change": "-24.49%" },
          { "value": -91235, "period": "Mar 2023", "change": "+17.14%" },
          { "value": -110103, "period": "Mar 2022" }
        ]
      },
      {
        "category": "financing",
        "history": [
          { "value": -31891, "period": "Mar 2025", "change": "-91.58%" },
          { "value": -16646, "period": "Mar 2024", "change": "-259.22%" },
          { "value": 10455, "period": "Mar 2023", "change": "-39.53%" },
          { "value": 17289, "period": "Mar 2022" }
        ]
      }
    ],
    "full_statement": [
      {
        "particular": "Profit before tax",
        "history": [
          { "period": "Mar 2025", "value": 106017 },
          { "period": "Mar 2024", "value": 104340 },
          { "period": "Mar 2023", "value": 94801 },
          { "period": "Mar 2022", "value": 84142 }
        ]
      },
      {
        "particular": "Income before WC changes",
        "history": [
          { "period": "Mar 2025", "value": 166904 },
          { "period": "Mar 2024", "value": 164383 },
          { "period": "Mar 2023", "value": 140963 },
          { "period": "Mar 2022", "value": 113726 }
        ]
      },
      {
        "particular": "Change in Assets",
        "history": [
          { "period": "Mar 2025", "value": -14703 },
          { "period": "Mar 2024", "value": -28430 },
          { "period": "Mar 2023", "value": -19034 },
          { "period": "Mar 2022", "value": -39163 }
        ]
      },
      {
        "particular": "Change in Liabilities",
        "history": [
          { "period": "Mar 2025", "value": 38427 },
          { "period": "Mar 2024", "value": 34796 },
          { "period": "Mar 2023", "value": -600 },
          { "period": "Mar 2022", "value": 39888 }
        ]
      },
      {
        "particular": "Change in WC",
        "history": [
          { "period": "Mar 2025", "value": 23724 },
          { "period": "Mar 2024", "value": 6366 },
          { "period": "Mar 2023", "value": -19634 },
          { "period": "Mar 2022", "value": 725 }
        ]
      },
      {
        "particular": "Cash flow from Operations",
        "history": [
          { "period": "Mar 2025", "value": 178703 },
          { "period": "Mar 2024", "value": 158788 },
          { "period": "Mar 2023", "value": 115032 },
          { "period": "Mar 2022", "value": 110654 }
        ]
      },
      {
        "particular": "Cash flow from Investing",
        "history": [
          { "period": "Mar 2025", "value": -137535 },
          { "period": "Mar 2024", "value": -113581 },
          { "period": "Mar 2023", "value": -91235 },
          { "period": "Mar 2022", "value": -110103 }
        ]
      },
      {
        "particular": "Cash flow from Financing",
        "history": [
          { "period": "Mar 2025", "value": -31891 },
          { "period": "Mar 2024", "value": -16646 },
          { "period": "Mar 2023", "value": 10455 },
          { "period": "Mar 2022", "value": 17289 }
        ]
      },
      {
        "particular": "Total Cash Flow",
        "history": [
          { "period": "Mar 2025", "value": 9277 },
          { "period": "Mar 2024", "value": 28561 },
          { "period": "Mar 2023", "value": 34252 },
          { "period": "Mar 2022", "value": 17840 }
        ]
      },
      {
        "particular": "Cash (Start of the year)",
        "history": [
          { "period": "Mar 2025", "value": 97225 },
          { "period": "Mar 2024", "value": 68664 },
          { "period": "Mar 2023", "value": 36178 },
          { "period": "Mar 2022", "value": 17397 }
        ]
      },
      {
        "particular": "Cash (End of the year)",
        "history": [
          { "period": "Mar 2025", "value": 106502 },
          { "period": "Mar 2024", "value": 97225 },
          { "period": "Mar 2023", "value": 68664 },
          { "period": "Mar 2022", "value": 36178 }
        ]
      }
    ]
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | object | Cash flow data for the requested statement type and time period. |
| data.type | string | Financial statement type. Possible values: `consolidated` , `standalone` . |
| data.time_period | string | Reporting period. Possible values: `yearly` , `quarterly` . |
| data.units_in | string | Unit of monetary values. Value: `crore` . |
| data.cash_flow | array | Cash flow categories with historical values ordered by reporting period (most recent first). |
| data.cash_flow[].category | string | Cash flow category. Possible values: `operating` , `investing` , `financing` . |
| data.cash_flow[].history | array | Historical values for the cash flow category. |
| data.cash_flow[].history[].value | number | Cash flow amount for the period (in Crore). Negative values indicate net outflow. |
| data.cash_flow[].history[].period | string | Reporting period label, e.g., `Mar 2025` . |
| data.cash_flow[].history[].change | string | Period-over-period percentage change, e.g., `"+12.54%"` . Absent for the oldest period in the series. |
| data.full_statement | array | Detailed line-item breakdown of the cash flow statement. Present only when `fs=true` is passed. Always reported on an annual basis. |
| data.full_statement[].particular | string | Label for the cash flow line item, e.g., `Profit before tax` , `Income before WC changes` , `Change in Assets` , `Change in Liabilities` , `Change in WC` , `Cash flow from Operations` , `Cash flow from Investing` , `Cash flow from Financing` , `Total Cash Flow` , `Cash (Start of the year)` , `Cash (End of the year)` . |
| data.full_statement[].history | array | Historical values for the line item across reporting periods. |
| data.full_statement[].history[].period | string | Reporting period label, e.g., `Mar 2025` . |
| data.full_statement[].history[].value | number | Monetary value for the period (in Crore). |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |
| UDAPI1207 | **Invalid type** - Allowed values: `consolidated` , `standalone` . |

---

## Get Key Ratios

API to retrieve the key financial ratios for a company identified by its ISIN. Each ratio includes the company's current value alongside a sector benchmark value, enabling relative valuation comparisons. Ratios returned include P/E, P/B, ROA, ROE, ROCE, and EV/EBITDA.

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/key-ratios`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Response

```json
{
  "status": "success",
  "data": [
    { "name": "P/E", "company_value": "20.15", "sector_value": "12.46" },
    { "name": "P/B", "company_value": "2.13", "sector_value": "1.53" },
    { "name": "ROA", "company_value": "4.39%", "sector_value": "7.54%" },
    { "name": "ROE", "company_value": "8.94%", "sector_value": "16.46%" },
    { "name": "ROCE", "company_value": "10.39%", "sector_value": "16.9%" },
    { "name": "EV/EBITDA", "company_value": "10.25", "sector_value": "6.94" }
  ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | array | List of key financial ratio entries. |
| data[].name | string | Name of the financial ratio. Possible values: `P/E` , `P/B` , `ROA` , `ROE` , `ROCE` , `EV/EBITDA` . |
| data[].company_value | string | Current value of the ratio for the requested company. |
| data[].sector_value | string | Sector benchmark value for the same ratio. |

**Ratio definitions:**

| Ratio | Description |
| --- | --- |
| P/E | Price-to-Earnings ratio — market price per share divided by earnings per share. |
| P/B | Price-to-Book ratio — market price per share divided by book value per share. |
| ROA | Return on Assets — net income as a percentage of total assets. |
| ROE | Return on Equity — net income as a percentage of shareholders' equity. |
| ROCE | Return on Capital Employed — EBIT as a percentage of capital employed. |
| EV/EBITDA | Enterprise Value divided by Earnings Before Interest, Taxes, Depreciation, and Amortisation. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |

---

## Get Share Holdings

API to retrieve the quarterly shareholding pattern for a company identified by its ISIN. The response breaks down the ownership structure by shareholder type — such as Promoters, FII (Foreign Institutional Investors), DII (Domestic Institutional Investors), and Public — across multiple reporting quarters, expressed as a percentage of total shares.

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/share-holdings`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Response

```json
{
  "status": "success",
  "data": [
    {
      "category": "promoters",
      "history": [
        { "period": "Mar 2026", "value": 50.0 },
        { "period": "Dec 2025", "value": 50.01 },
        { "period": "Sep 2025", "value": 50.01 },
        { "period": "Jun 2025", "value": 50.07 }
      ]
    },
    {
      "category": "fii",
      "history": [
        { "period": "Mar 2026", "value": 18.67 },
        { "period": "Dec 2025", "value": 19.09 },
        { "period": "Sep 2025", "value": 18.65 },
        { "period": "Jun 2025", "value": 19.21 }
      ]
    },
    {
      "category": "other_dii",
      "history": [
        { "period": "Mar 2026", "value": 10.77 },
        { "period": "Dec 2025", "value": 10.66 },
        { "period": "Sep 2025", "value": 10.67 },
        { "period": "Jun 2025", "value": 10.48 }
      ]
    },
    {
      "category": "mutual_funds",
      "history": [
        { "period": "Mar 2026", "value": 9.78 },
        { "period": "Dec 2025", "value": 9.52 },
        { "period": "Sep 2025", "value": 9.66 },
        { "period": "Jun 2025", "value": 9.32 }
      ]
    },
    {
      "category": "retail_and_other",
      "history": [
        { "period": "Mar 2026", "value": 10.79 },
        { "period": "Dec 2025", "value": 10.73 },
        { "period": "Sep 2025", "value": 11.01 },
        { "period": "Jun 2025", "value": 10.92 }
      ]
    }
  ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | array | List of shareholding entries, one per shareholder category. |
| data[].category | string | Shareholder category identifier. Possible values: `promoters` , `fii` , `other_dii` , `mutual_funds` , `retail_and_other` . |
| data[].history | array | Quarterly shareholding history for this category. |
| data[].history[].period | string | Reporting quarter label, e.g., `Mar 2026` . |
| data[].history[].value | number | Percentage of total shares held by this category for the period. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |

---

## Get Corporate Actions

API to retrieve the corporate actions for a company identified by its ISIN. The response contains a list of events such as dividends, bonus issues, stock splits, and rights issues, each with detailed sub-event information including announcement dates, ex-dates, record dates, and amounts.

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/corporate-actions`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Response

```json
{
  "status": "success",
  "data": [
    {
      "name": "Dividend",
      "expiry_date": "14 Aug 2025",
      "amount": 5.5,
      "ratio": null,
      "event_details": [
        { "name": "Announcement date", "value": "25 Apr 2025" },
        { "name": "Ex dividend date", "value": "14 Aug 2025" },
        { "name": "Record date", "value": "14 Aug 2025" },
        { "name": "Dividend type", "value": "Final" },
        { "name": "Amount", "value": "5.5" },
        { "name": "Dividend %", "value": "55.0" },
        { "name": "Details", "value": "Rs.5.5000 per share(55%)Final Dividend" }
      ]
    }
  ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | array | List of corporate action events. |
| data[].name | string | Type of corporate action, e.g., `Dividend` , `Bonus` , `Split` , `Rights` . |
| data[].expiry_date | string | Ex-date or effective date of the corporate action. |
| data[].amount | number | Monetary amount associated with the action (applicable for dividends). |
| data[].ratio | string | Ratio applicable for bonus or split actions (e.g., `1:1` ). `null` if not applicable. |
| data[].event_details | array | Detailed key-value pairs with full event information. |
| data[].event_details[].name | string | Label describing the event detail, e.g., `Announcement date` , `Ex dividend date` . |
| data[].event_details[].value | string | Corresponding value for the event detail. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |

---

## Get Competitors

API to retrieve the list of competitor companies for a company identified by its ISIN. The response contains an array of competitor profiles, each including the company's ISIN, a brief description, sector, and sector market capitalisation in INR and USD.

### Endpoint

**GET** `https://api.upstox.com/v2/fundamentals/{isin}/competitors`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| isin | Required | string | International Securities Identification Number (ISIN) of the company. Example: `INE002A01018` . |

### Response

```json
{
  "status": "success",
  "data": [
    {
      "instrument_key": "NSE_EQ|INE242A01010",
      "company_profile": "Indian Oil Corporation Limited is an India-based oil company. The Company's segments include Petroleum Products, Petrochemicals, Gas, and Other Business Activities. Its business interests span the entire hydrocarbon value-chain, ranging from refining, pipeline transportation and marketing to exploration and production of petrochemicals, natural gas and alternative energy.",
      "sector": "Refineries",
      "sector_market_cap_inr": {
        "value": 204334.32,
        "unit": "crore",
        "formatted": "204,334.32 Cr"
      },
      "sector_market_cap_usd": {
        "value": 22.7,
        "unit": "billion",
        "formatted": "$22.70B"
      }
    },
    {
      "instrument_key": "NSE_EQ|INE029A01011",
      "company_profile": "Bharat Petroleum Corporation Limited is an India-based company, which is engaged in the refining of crude oil and marketing of petroleum products. Its segments include Downstream Petroleum and Exploration & Production of Hydrocarbons.",
      "sector": "Refineries",
      "sector_market_cap_inr": {
        "value": 131391.64,
        "unit": "crore",
        "formatted": "131,391.64 Cr"
      },
      "sector_market_cap_usd": {
        "value": 14.6,
        "unit": "billion",
        "formatted": "$14.60B"
      }
    }
  ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` . |
| data | array | List of competitor company profiles. |
| data[].instrument_key | string | Instrument key of the competitor in the format `EXCHANGE\|ISIN` , e.g., `NSE_EQ\|INE242A01010` . |
| data[].company_profile | string | Brief description of the competitor company's business. |
| data[].sector | string | Sector to which the competitor belongs. |
| data[].sector_market_cap_inr | object | Market capitalisation of the competitor's sector in Indian Rupees. |
| data[].sector_market_cap_inr.value | number | Numeric market cap value in Crore. |
| data[].sector_market_cap_inr.unit | string | Unit of the value. Value: `crore` . |
| data[].sector_market_cap_inr.formatted | string | Human-readable formatted value, e.g., `"131,391.64 Cr"` . |
| data[].sector_market_cap_usd | object | Market capitalisation of the competitor's sector in US Dollars. |
| data[].sector_market_cap_usd.value | number | Numeric market cap value in the specified unit. |
| data[].sector_market_cap_usd.unit | string | Unit of the value. Possible values: `billion` , `million` . |
| data[].sector_market_cap_usd.formatted | string | Human-readable formatted value, e.g., `"$14.60B"` . |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1206 | **Invalid ISIN** - The provided ISIN is invalid. |
