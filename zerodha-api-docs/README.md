# Zerodha Kite Connect API Documentation in Markdown

Complete Zerodha Kite Connect v3 API documentation converted to Markdown format for use as context with AI tools like Claude Code, Cursor, GitHub Copilot, and other LLM-powered development assistants.

## What's Included

- **20 Markdown files** covering the entire Kite Connect v3 API
- All REST API endpoints with methods, parameters, request/response formats
- WebSocket binary protocol documentation with byte-level packet structure
- Error types, rate limits, authentication flows
- Quick reference table of all endpoints

## File Structure

| File | Section |
|------|---------|
| `00-overview.md` | Introduction and getting started |
| `01-sdks.md` | Client libraries (Python, Go, Java, PHP, Node.js, .NET) |
| `02-response-structure.md` | JSON response formats |
| `03-exceptions.md` | Error types, HTTP codes, rate limits |
| `04-user.md` | Authentication, profile, margins, logout |
| `05-orders.md` | Place, modify, cancel, retrieve orders and trades |
| `06-gtt.md` | Good Till Triggered orders |
| `07-alerts.md` | Price alerts and notifications |
| `08-portfolio.md` | Holdings, positions, conversions |
| `09-market-quotes.md` | Instruments, quotes, OHLC, LTP |
| `10-websocket.md` | Real-time streaming with binary protocol |
| `11-historical.md` | Historical candle data |
| `12-postbacks.md` | WebHooks for order updates |
| `13-mutual-funds.md` | SIPs and MF orders |
| `14-margins.md` | Margin and charges calculation |
| `15-basket.md` | Offsite order execution |
| `16-publisher.md` | Publisher JS plugin |
| `17-apps.md` | Mobile and desktop app integration |
| `18-changelog.md` | Version history |
| `19-api-reference.md` | Complete endpoints quick reference |

## Usage with AI Tools

### Claude Code
Add to your `CLAUDE.md`:
```
Reference the Kite Connect docs in ./zerodha-kite-docs/ for API integration context.
```

### Cursor
Add the `zerodha-kite-docs/` directory to your project and reference in `.cursorrules`.

## Source

Documentation sourced from [Kite Connect v3](https://kite.trade/docs/connect/v3/).

## License

MIT
