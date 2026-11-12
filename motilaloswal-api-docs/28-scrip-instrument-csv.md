# Scrip/Instrument (CSV Format)

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Master Data

This Downloads exchange data in .CSV file

| Method | GET |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/getscripmastercsv?name=NSEFO<br>name = exchangename in URL and you will get CSV file for that exchange |
| Test URL | https://openapi.motilaloswaluat.com/getscripmastercsv?name=NSEFO<br>name = exchangename in URL and you will get CSV file for that exchange |
| Response | File Download in .csv Format |

Format as below

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| exchange | exchangename | scripcode | scripname | marketlot | scripshortname | issuspended |
| instrumentname | expirydate | strikeprice | optiontype | markettype | foexposurepercent | ticksize |
| scripisinno | indicesidentifier | isbanscrip | scripfullname | facevalue | calevel | maxqtyperorder |
