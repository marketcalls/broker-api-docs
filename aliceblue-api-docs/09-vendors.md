# Vendors API

> Source: https://v2api.aliceblueonline.com/Vendors/

### Introduction

The vendor API is an innovative solution provided by Aliceblue APIs. Vendor APIs are usually used by technical companies to build innovative technical solutions and customised trading platforms to retail traders. Vendor API will enable vendors to create the Session for any user, who has authorized the app registered by Vendor. This way, the vendors do not have to manually get the API Key from users to generate session

### Registration as a Vendor

To register as a Vendor, Please visit [https://a3.aliceblueonline.com/](https://a3.aliceblueonline.com/)

- Login using your Aliceblue credentials.
- In the Apps sections, Create a new application.
- Fill out the mandatory details.
- Click "Save" to create a new app.
- An App Code (appCode) and API Secret (apiSecret) will be provided to the Vendor. This code is important and Confidential. DO NOT Share with anyone outside your organization.​
- The App will be activated by Aliceblue Admin team after reviewing the details given by the Vendor. The Vendor API access will be provided after necessary approval.​

### Implementation of SSO

- During User login, the Vendor should redirect the Aliceblue user to <https://ant.aliceblueonline.com/?appcode=>.along with the App Code as shown here in the url.
- User will be asked to login with their Aliceblue credentials.
- After sucessful login, the user will be redirected to the URL provided by the Vendor (Provisions to provide / update the Redirect URL is provided in the Developers Login) along with User Authorization token **(authCode)** and User ID **(userId)**.
- The Vendor will save the user authCode, UserId **(userId)** along with apiSecret to create a checkSum, which is the SHA-256 hash of **userId + authCode + apiSecret**
- Vendor should send this checkSum to the URL : <https://ant.aliceblueonline.com/rest/AliceBlueAPIService/sso/getUserDetails> to get the User Session **(userSession)**, which can be used to access all API end points.

### Postman Sample

[Download](https://v2api.aliceblueonline.com/PDF/vendor%20.json)
