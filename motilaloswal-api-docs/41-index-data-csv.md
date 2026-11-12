# INDEX DATA (CSV Format)

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Index Data

This API is used to get index data for BSE,NSE in CSV format

| Method | GET |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/getindexdatacsv?name=BSE |
| Test URL | https://openapi.motilaloswaluat.com/getindexdatacsv?name=BSE |
| Response | File Download in .csv Format |

## Symbol Parameters Define

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | String | Y | NSE,BSE |
| Response | File Download in .csv Format |  |  |

## Sample File Format

```text
exchangename,indexcode,indexname
BSE,999902,BSE100
BSE,999903,BSE 200
BSE,999904,BSE 500
BSE,999913,BSE AUTO
BSE,999912,BSE BANKEX
BSE,999907,BSE CAPGOOD
BSE,999926,BSE CARBON
BSE,999908,BSE CONSDUR
BSE,999929,BSE CPSE
```
