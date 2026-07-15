# MCP Integration

Upstox offers Model Context Protocol (MCP) integration enabling AI assistants - Claude Desktop, ChatGPT, Cursor, and VS Code with GitHub Copilot - to access trading account data directly.

## What is MCP?

Model Context Protocol (MCP) enables AI assistants to access your account-specific trading data in real-time, creating context-aware conversations about your actual investments.

**Key capabilities:**

- Account-scoped portfolio analysis
- Real-time market context integration
- Natural language API query mapping
- Personalized investment research aligned with existing holdings

## Setup Requirements

- Active, non-dormant Upstox trading account
- Node.js installation
- Compatible AI client application
- Basic Upstox API familiarity

## Installation Instructions by Platform

### Claude Desktop

Install Node.js, access Settings > Developer > Edit Config, then add the MCP server configuration pointing to `https://mcp.upstox.com/mcp`.

### ChatGPT

Enable Developer mode in Settings > Apps > Advanced settings, create a custom app with the Upstox endpoint, then select it from Chat connectors.

### Cursor

Navigate Settings > Tools > MCP, click "Add custom MCP," configure the server details, then connect.

### VS Code

Add MCP configuration to settings.json with the Upstox server URL, then use `/mcp` command in Copilot Chat.

## Capabilities

- **Portfolio Insights**: Position breakdown, P&L tracking, diversification analysis
- **Account Data**: Margins, profile information
- **Market Research**: Stock analysis, technical indicators

## Important Limitations

- **Read-Only Access**: The MCP integration provides read-only access to your account data. You cannot place orders, modify positions, or execute trades through the AI assistant.
- Daily re-authorization is required for security purposes.
