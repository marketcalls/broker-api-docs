# Integration Flow

How a partner application is onboarded and how the pieces of the XStream API fit together.

> Source: https://xstream.5paisa.com/dev-docs/docFundamentals/integration-flow

Integration of Xstream APIs start with the user authentication system which helps the users to get session tokens. These session tokens are mandatory to pass in various other APIs as it includes the part of authentication system.

Login Flow:

1. The login flow starts with accessing Xstream API account
2. Our login flow :
3. OAUTH (Web based)
4. On Successful login user is provided with RequestToken which is passed to get access token API along with encryption key to obtain access token.
5. AccessToken is generated with the help of RequestToken obtained from either TOTP or OAuth login. The access token is valid throughout the day and can be used to call all further APIs.

WARNING : Do not expose the AccessToken you obtain for a session to the public

OAuth is available for both Partners and Individual users.

For more info please check respective API page of OAUTH Login under User Authentication Section.

- [Customer Login](https://xstream.5paisa.com/dev-docs/user-authentication-system/login)
- [OAuth Login](https://xstream.5paisa.com/dev-docs/user-authentication-system/oauth-login)
