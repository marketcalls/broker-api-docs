# EOD (CSV Format)

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: EOD Data

This API is used to get end of day data (OHLC,Volume) for different exchanges in CSV format

| Method | GET |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/geteoddatacsv?name=NSE<br>name = exchangename in URL and you will get CSV file for that exchange |
| Test URL | https://openapi.motilaloswaluat.com/geteoddatacsv?name=NSE<br>name = exchangename in URL and you will get CSV file for that exchange |
| Response | File Download in .csv Format |

## Sample File Format

```text
exchange,scripcode,open,high,low,close,volume,date,scripfullname,scripshortname,instrumentname,expirydate,strikeprice,optiontype
NSE,4934,218.900,223.950,217.550,222.450,99235,09-02-2023,INDIA PESTICIDES LIMITED-IPL EQ,IPL,"      ",0,0.00,"  "
NSE,20030,1134.300,1134.300,1134.300,1134.300,1,09-02-2023,7.74% TAX FREE NCD-IREDA N7,IREDA,"      ",0,0.00,"  "
NSE,29605,0.000,0.000,0.000,1093.000,0,09-02-2023,BOND 6.88% PA TAX FREE S1-IRFC N5,IRFC,"      ",0,0.00,"  "
NSE,29607,0.000,0.000,0.000,1096.000,0,09-02-2023,BOND 7.04% PA TAX FREE S2-IRFC N6,IRFC,"      ",0,0.00,"  "
```
