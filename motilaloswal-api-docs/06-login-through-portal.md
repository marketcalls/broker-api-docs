# Login through Portal

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

This Login Flow shall be used to redirect users to third party vendor portal. To implement this flow, Third party vendor/user needs to call given login page URL along with their APP Key (provided by MOFSL) and where MOFSL user will have to enter their Trading Login ID / Password to authenticate.

Live login endpoint

`https://invest.motilaloswal.com/OpenAPI/Login.aspx?apikey={apikey}`

UAT login endpoint

`https://uattrade.motilaloswaluat.com/OpenAPI/Login.aspx?apikey={apikey}`

Ex . If your API Key = abc then URL will be

`https://uattrade.motilaloswaluat.com/OpenAPI/Login.aspx?apikey=abc`

After successful login, user gets redirected to the URL specified under My Apps Dashboard with authtoken as query parameter.

```text
Ex. Assume redirection url is : https://google.com
Redirected to below URL with authtoken

    https://www.google.com/?authtoken=d3bcc86824264c689bf18052bb724fa5_M

 in response is Authorization Token used in header of each API.
```
