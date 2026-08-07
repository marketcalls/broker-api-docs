# Introduction

> Source: <https://zebumyntapi.web.app/Base/>

Base URL

The BASE URL is the common url used as prefix for all API call.

Base URL - https://go.mynt.in
![Image title](https://zebumyntapi.web.app/assets/newlogo.svg)

```mermaid
graph LR
  A[Mynt] --> B{LogIn};
  B -->|Yes| C[Profile...];
  C --> D[API KEY GENERATE];
  D --> |Yes| E[API key Months Select];
  E --> |Yes| F[API KEY]
  B --> |No| G[LogIn to Zebull]
```

Get API KEY

- Login to MYNT WEB application.
- Navigate to Profile → ClientId.
- Users can generate "API key" via the API Key button.
- Then Select the generate "API key" → month and click the Generate API Key button.
- Finally the MYNT API key is generate.

### Login

![Image title](https://zebumyntapi.web.app/assets/login.png)

1. Enter Client code --> User ID
2. Enter Password
3. DOB/PAN/OTP/TOTP

### Profile

- Click on the the  Profile → Client code button in right top in nav bar.

![Image title](https://zebumyntapi.web.app/assets/profile.png)

### API KEY GENERATE

*Click the API key button next to the logout put for generate.

![Image title](https://zebumyntapi.web.app/assets/select.png)

- Select the API key Months
   ![Image title](https://zebumyntapi.web.app/assets/months.png)
- Generate the API Key

![Image title](https://zebumyntapi.web.app/assets/generatekey.png)

### API KEY

![Image title](https://zebumyntapi.web.app/assets/apikey.png)

MYNT Connect is a collection of REST-like HTTP APIs that offer many of the capabilities needed to create a full-featured stock market trading and investment platform. You can manage user portfolios, broadcast real-time market data using WebSockets, execute orders in real-time (for stocks, commodities, mutual funds), and more.
