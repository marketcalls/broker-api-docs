# Responses Format

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

Responses from the API will be in JSON

## Successful Response

```json
{
"status": “SUCCESS”,
"message”: “SUCCESS”,
"errorcode":"",
"data":{}
}
```

## Failed Response

```json
{
"status”: “FAILURE",
"message”: “Login Id/Password Is Invalid",
"errorcode":"MOSL100",
"data”: “null"
}
```

The status field in the response contains the value SUCCESS/FAILURE. Message field contains actual description of the error. The errorcode field contains the error-code mentioned in Error Codes and Description section.
