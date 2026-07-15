<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: EDIS APIs -->

# EDIS APIs

Using this API, users who have not submitted POA with us can do CDSL authorisation to sell their holdings. Earlier This process was done via Mobile App/Web. This can be now done via API as well. Please note that you need to provide authorisation once in a day for selling.

The API endpoint for the same is :

```
https://apiconnect.angelone.in/rest/secure/angelbroking/edis/v1/verifyDis
```

#### The request body is :

```json
{
"isin": "INE528G01035",
"quantity": "1"
}
```

The Header parameters are same as other requests.

#### Response Structure:

For first time registration in a day:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":{
"ReqId": "8180722758077144",
"ReturnURL": "https://trade.angelbroking.com/cdslpoa/response",
"DPId": "33200",
"BOID": "1203320015222472",
"TransDtls":"fZ6jlmt9GosSO0kFdI9S9FCD+IYFvjUN94Bph46YMC1BzexE1hDuCwjSUzXVoEgV3mTP5aXnwxJDikFm1xymcjfhEgtWm7ykrpxaDXSuQF25Fg5olDgXy/Suu916VNg9XID0GHy1CT5E9WBP0gocixvOFrCPFmRMmY+7Nqbb3cNfqPZ8uHfX0un5tFnQXV3AXK0g2exwRf3EINSTHSv66/inPArtDko70vuc1pb5e0tRXa14FN2hzklop2UyrcIiDmkmzcHvjdGGomCM4PU90S28xHze5/dAlTv7ywIzrQOA4N2LW7n7M9atFExQTC2tczdwhKkVzScYmpVdRvtY+Lqo8o/OSVQ8Gd3Guz7ZRpqV5073lZ/BnPN8FtJW6shfOwgbYgqmhV2jik0uw57eQ7f+SI0pYYC8noOwKncJ3/umtVY2NVgLjdZq2yxZh7wTQKC2WYaYl/MnZLpgF9yYlBAtZ6trgLG6kcmtlbibtkimi2TecMGN3KrAETsWY07fZCc9Ks/RetFzD1qNIGWZ/4WnpWyW5XTxSxlQILCz7Qwk5f+dKcXVe5CS/7DMB7aa9KQ4t1ru1xo7jM4GmUdwcGVwUqb2pfNSEUX+I10INA0TwXkWdUAAQYO0++q6mYpN59G3IW9vV/dW0/bHh4xcsPg9ysDBZ8bLlk4C3hL6RiVrxcF2AgxjJgLSxL2YerAKkgivk22KULtEDpOpE7IcwxjuWjRxOPGfnSGbc4Ii1avte50WZFh6EKIP6E16sZgKaOh/r5CSnysEtDetvhn8siIWDQbhInAoExMpsuewIthg4QVWvx0EzQL6LqNO74Hc9/JicH+cGFtn6nHjwHgquzbCZx6W6XlzHJVV04Pd0m4kXC27RrnoraFj3KpXcfmdSr0GK3HtUKYV2QgSM8COvEEuL++oxjD4PKi40JmTv2I=",
"version": "1.1"
}
}
```

If User has already registered for the Day:

```json
{
"status": false,
"message": "You have alreday been registered with CDSL for today.",
"errorcode": "AG1000",
"data":{
"ReqId": "0390624715013748",
"ReturnURL": null,
"DPId": null,
"BOID": null,
"TransDtls":null ,
"version": "1.1"
}
}
```

If there is an error:

```json
{
"status": false,
"message": "Something went wrong. Please try again",
"errorcode": "AG2001",
"data": null
}
```

## Generate TPIN

API end point:

```
https://apiconnect.angelone.in/rest/secure/angelbroking/edis/v1/generateTPIN
```

Request type- POST

#### Request Body:

```json
{
"dpId": "...",
"ReqId": "...",
"boid": "...",
"pan": "..."
}
```

The Above operation needs to be done in an HTML page which will open a browser window with CDSL website wherein the user can verify their TPIN

Below is an example of the HTML code which can be used for this purpose:

```
<!DOCTYPE html>
<html>
<script>window.onload= function()
        {submit()};function submit(){ document.getElementById("submitbtn").click();    }
</script>
<body onload="submit()">
<form name="frmDIS" method="post"
      action="https://edis.cdslindia.com/eDIS/VerifyDIS/" style="
                                              text-align: center; margin-top: 35px; /* margin-bottom: 15px; */ ">
    <input type="hidden" name="DPId" value="33200">
    <input type="hidden" name="ReqId" value="0908782441429760">
    <input type="hidden" name="Version" value="1.1">
    <input type="hidden" name="TransDtls"
           value="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">
    <input style="display: none;" id="submitbtn" type="submit" value="Submit">
</form>
</body>
</html>
```

The value for the params ReqId, DPId and TransDtls is received in the response of verifyDis API.

#### The response for this will be:

Success

```json
{
"status": true,
"SUCCESS": "",
"errorcode": null,
"data": null
}
```

Failure

```json
{
"status": false,
"message": "Something went wrong. Please try again",
"errorcode": "AG2001",
"data": null
}
```

## Get Transaction Status API:

To check whether you have authorised a particular security for selling or not, you can use transaction status API.

API end point:

```
https://apiconnect.angelone.in/rest/secure/angelbroking/edis/v1/getTranStatus
```

Request type- POST

#### Request Body:

```json
{
"ReqId": "7650687246435520"
}
```

The value for the params ReqId, DPId and TransDtls is received in the response of verifyDis API.

#### Response Body:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":{
"TransResDtls":{
"ReqId": "1278983622820067",
"ReqType": "D",
"ResId": "1603202259241073",
"ResStatus": "0",
"ResTime": "17032022000022",
"ResError": "",
"Remarks": "",
"RecordResDtls":[
{
"TxnReqId": "7659729424908225",
"TxnId": "1603202275616752",
"Status": "0",
"Errorcode": ""
}
]
}
}
}
```

The status key in the response indicates whether the authorization has been received or not. status = 0 implies that you’re not allowed to sell that particular security, whereas status = 1 implies that the authorisation to sell has been received.
