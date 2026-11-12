# Get Profile

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Authentication/Profile

This API allows to fetch the complete information of the user who is logged in

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/login/v5/getprofile |
| Test URL | https://openapi.motilaloswaluat.com/rest/login/v5/getprofile |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| Clientcode | String(15) | N | Its mandatory in case of Dealer |

## Sample Request (Body)

```json
{
“clientcode":"AA017” //in case of dealer else not required
}
```

## Sample Response

```json
{
“status": "SUCCESS",
"message": "Profile Data",
"errorcode": "",
"data": {
"clientcode": "AA017",
"name": "Amit Kumar",
"exchanges": ["NSE","BSE","NSEFO","NSECD","NSEEX","MCX","BSECD"],
"products": ["Normal","Delivery"],
"usertype":"Investorclient"
}
}
```

## Response JSON

| Field | Type | Description |
| --- | --- | --- |
| Clientcode | String(20) | Client ID |
| Name | String(30) | Name of Client or user |
| Exchanges | String(50) | Name of the Exchanges - LIST |
| Products | String(50) | Name of products - LIST |
| Usertype | String(20) | User Type - Dealer Or Investor Client |
