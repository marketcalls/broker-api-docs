<!-- Source: https://ant.aliceblueonline.com/productdocumentation/Authentication/ -->

# Authentication

Note

The BASE URL, Endpoint, and Payload JSON key values are case-sensitive. Please use the format which we have given in the documentation.

## Get Session

1. During user login, the Individual Trader should redirect the Aliceblue user to
 `https://ant.aliceblueonline.com/?appcode=` along with the **App Code** in the URL.
2. The user will be asked to log in with their Aliceblue credentials.
3. After successful login, the user will be redirected to the **Redirect URL** provided by the Individual Trader
 (this can be configured or updated from the Developer Portal), along with:
  - authCode – User Authorization Token
  - userId – Aliceblue User ID
4. The Individual Trader must save the `authCode` and `userId`, and use them with the `apiSecret` to create a **checksum**. This is the **SHA-256 hash** of: userId + authCode + apiSecret
5. The Individual Trader should then send this checksum to the following URL to obtain a **user session**:
 `https://a3.aliceblueonline.com/open-api/od/v1/vendor/getUserDetails`

The returned `userSession` can then be used to access all further API endpoints.

| Method | APIS |
| --- | --- |
| Post | [https://a3.aliceblueonline.com/open-api/od/v1/vendor/getUserDetails](https://a3.aliceblueonline.com/open-api/od/v1/vendor/getUserDetails) |

**Request Structure**

```
{
    "checkSum":"99e9b517d1fb6012e7b105db2333151f72cd9469746d977da4def08cabftyhj533"
}
```

**Input parameters**

| Field | Type | Description |
| --- | --- | --- |
| checksum | String | SHA-256 hash of: userId + authCode + apiSecret |

**Success Response**

```
{
    "stat": "Ok",
    "clientId": "912444",
    "userSession": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyam9lOFVScGxZU3FTcDB3RDNVemVBQkgxYkpmOE4wSDRDMGVVSWhXUVAwIn0.eyJleHAiOjE3NTc3Mjc2MjgsImlhdCI6MTc1MjU1MDQ2NCwianRpIjoiMjg1ZTI2NzgtYzYzYi00NmE3LWJjYWEtMTQ0OTExMWY2ZmRkIiwiaXNzIjoiaHR0cHM6Ly9pZGFhcy5hbGljZWJsdWVvbmxpbmUuY29tL2lkYWFzL3JlYWxtcy9BbGljZUJsdWUiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMjYzM2Y4ZGMtNzI2OS00NGExLWFjYjUtMjc2ZmExYWI0OGJjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWxpY2Uta2IiLCJzaWQiOiI0MjYzMzA0Mi03MTcxLTQ1MjEtOTMwMC04NTBlZjM0MGUyNGIiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2xvY2FsaG9zdDozMDAyIiwiaHR0cDovL2xvY2FsaG9zdDo1MDUwIiwiaHR0cDovL2xvY2FsaG9z"
}
```

| Field | TYPE | Description |
| --- | --- | --- |
| userId | String | Ok (Login Success) |
| clientId | String | Unique Client Code |
| userSession | String | User Session that can be used to access all further API endpoints |

**Error Response**

```
{
    "stat": "Not_ok",
    "emsg": "Invalid auth code"
}
```

| Field | TYPE | Description |
| --- | --- | --- |
| stat | String | Not_Ok |
| emsg | String | * User does not login. Please login<br>* Your API key Expired.Please update your API key<br>* API key not available.Please generate API key<br> * Internal server error. Please try again later. |
