# Participant Detail

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

This API is used to get Participant Detail for a clientcode

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getparticipantsdetail |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getparticipantsdetail |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |

## Sample Request (Body)

```json
{
"clientcode":"AA020"// in case of dealer only
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Participants DATA",
"errorcode": "",
"data": [
{
"clientcode": "PAWZ1431",
"participantid": "218450147IH",
"exchangename": "NSE",
"participanname": "RAJUL M "
},
{
"clientcode": "PAWZ1431",
"participantid": "E5986615IH",
"exchangename": "NSE",
"participanname": "JAYAN A"
}
]
}
```
