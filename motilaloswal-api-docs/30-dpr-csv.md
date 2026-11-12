# DPR CSV

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: DPR Data

This API is used to get daily price range of BANKNIFTY OR NIFTY scripts in CSV format

| Method | GET |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/getdprcsv?symbol=NIFTY |
| Test URL | https://openapi.motilaloswaluat.com/getdprcsv?symbol=NIFTY |
| Request | None |
| Response | CSV File |

Symbol Parameters define

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | String | Y | It''s either NIFTY or BANKNIFTY |

## Sample File Format

```text
exchangename,exchange,scripcode,scripname,scripshortname,strikeprice,optiontype,instrumentname
,expirydate,lowercircuitprice,uppercircuitprice
NSEFO,2,52826,NIFTY 13-Oct-2022 PE 16500,NIFTY,16500.000,PE,OPTIDX,1350138600,0.050,17.400
NSEFO,2,52827,NIFTY 13-Oct-2022 CE 16550,NIFTY,16550.000,CE,OPTIDX,1350138600,0.050,1548.050
```
