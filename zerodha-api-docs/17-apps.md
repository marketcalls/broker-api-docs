# Mobile and Desktop Apps

## Authentication Flow (No Server Backend)

1. Register `redirect_url` (e.g., `https://yoursite.com/kite-redirect` or `127.0.0.1` for local apps)
2. Launch webview to: `https://kite.zerodha.com/connect/login?api_key=xxx`
3. Monitor URL changes in webview
4. On redirect to your URL with `request_token` and `status`, extract both values
5. Close webview and proceed with token exchange

## Redirect Format

```
https://yoursite.com/kite-redirect?request_token=yyy&status=zzz
```

## Important Notes

- Enable cookie (and 3rd party cookie) support in your webview
- For public apps, **never embed `api_secret`** in the application - use a server backend for token exchange
