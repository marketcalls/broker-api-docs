# Authorization Flow

Step-by-step authentication walkthroughs for each app type. All authenticated API calls use `Authorization: Bearer <api_key>:<access_token>`.

## Individual Apps

1. Invoke `/api-gw/oauth/individual-token-v2` using `Authorization: Bearer <API_KEY>`.
2. Pass `password`, `twoFa`, and `twoFaTyp` in the request body (`twoFaTyp=totp` for authenticator app, `twoFaTyp=otp` for SMS/email).
3. On successful authorization, the API returns an `access_token`.
4. Form the authorization token as: `Bearer <API_KEY>:<access_token>`.
5. Use this token for all API requests.

![Individual App](https://developer.tradejini.com/_next/static/media/individual-apps.0y-__tas3si5d.svg)

---

## User Based Apps

1. Invoke `/api-gw/oauth/authorize` in a browser or web application.
2. Pass `client_id`, `redirect_uri`, `response_type`, `scope` and `state`.
3. User will be redirected to the **Tradejini CubePlus SSO Login** page.
4. After successful login, the user is redirected to the configured `redirect_uri` with a `code`.
5. Invoke `POST /api-gw/oauth/token` using `code`, `client_id`, `redirect_uri`, `client_secret` and `grant_type`.
6. On successful authorization, the API returns an `access_token`.
7. Form the authorization token as: `Bearer <API_KEY>:<access_token>` .
8. Use this token for all API request.

![User Based Apps](https://developer.tradejini.com/_next/static/media/user-based.0ri11673m~x34.svg)
