# MCP Server

> Source: https://docs.delta.exchange/#mcp-server

```json
// Claude Desktop / Claude Code / Cursor / VS Code
{
  "mcpServers": {
    "delta-exchange": {
      "command": "uvx",
      "args": ["delta-exchange-mcp"],
      "env": {
        "DELTA_API_KEY": "your_api_key",
        "DELTA_API_SECRET": "your_api_secret"
      }
    }
  }
}
```

The Delta Exchange MCP server exposes this API to AI agents over the Model Context Protocol. It runs as a local stdio subprocess and turns agent tool calls into signed REST requests. An agent reads market data, checks an account and places orders without writing HTTP or signing code.

Install and run it with `uvx delta-exchange-mcp`. Its tools fall into three tiers:

| Category | API key | Permissions | What an agent can do |
| --- | --- | --- | --- |
| Market data | Not required | — | Read the product catalog, tickers, order-book depth, recent trades and OHLC candles. Pull option chains, spot indices, settlement prices, and funding-rate, mark-price and open-interest history. |
| Account data | Required | Read permission | Read open positions with size, entry and unrealized PnL. Read balances, the wallet ledger, active and past orders, own fills, leverage and account preferences. Export fills to CSV. |
| Trading | Required | Trading permission + `DELTA_MCP_MODE=trade` | Place, edit and cancel single orders, batches of up to 50 on one contract, and take-profit/stop-loss brackets. Set leverage, adjust isolated margin, close all positions. |

Every tool is a read-only `GET` by default. The trading tools register only when you set `DELTA_MCP_MODE=trade` and supply an API key with trading permissions.

Once connected, ask the agent in plain language:

- "What is my unrealized PnL on BTCUSD?"
- "Show the BTC option chain expiring this Friday."
- "Cancel my open orders on ETHUSD." (trade mode only)

For setup, the full tool reference and key permissions, see [mcp.delta.exchange/docs](https://mcp.delta.exchange/docs).
