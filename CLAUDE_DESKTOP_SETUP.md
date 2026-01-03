# Claude Desktop + OpenBB MCP Setup Guide

## Installation Complete ✅

The OpenBB MCP server has been installed successfully. Now you need to configure Claude Desktop on your local machine.

## Configuration by Operating System

### macOS
**Config file location:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**How to configure:**
1. Open Terminal
2. Create/edit the config file:
```bash
mkdir -p ~/Library/Application\ Support/Claude
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

3. Paste this configuration:
```json
{
  "mcpServers": {
    "openbb-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "openbb-mcp-server",
        "--with",
        "openbb",
        "openbb-mcp",
        "--transport",
        "stdio"
      ]
    }
  }
}
```

4. Save (Ctrl+O, Enter, Ctrl+X)
5. **Fully quit Claude Desktop** (Cmd+Q)
6. Restart Claude Desktop

---

### Windows
**Config file location:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**How to configure:**
1. Open File Explorer
2. Type in address bar: `%APPDATA%\Claude`
3. Create a new file: `claude_desktop_config.json`
4. Paste this configuration:
```json
{
  "mcpServers": {
    "openbb-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "openbb-mcp-server",
        "--with",
        "openbb",
        "openbb-mcp",
        "--transport",
        "stdio"
      ]
    }
  }
}
```

5. Save the file
6. **Fully quit Claude Desktop** (Right-click taskbar → Quit)
7. Restart Claude Desktop

---

### Linux
**Config file location:**
```
~/.config/Claude/claude_desktop_config.json
```

**How to configure:**
1. Open Terminal
2. Create/edit the config file:
```bash
mkdir -p ~/.config/Claude
nano ~/.config/Claude/claude_desktop_config.json
```

3. Paste this configuration:
```json
{
  "mcpServers": {
    "openbb-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "openbb-mcp-server",
        "--with",
        "openbb",
        "openbb-mcp",
        "--transport",
        "stdio"
      ]
    }
  }
}
```

4. Save (Ctrl+O, Enter, Ctrl+X)
5. **Fully quit Claude Desktop**
6. Restart Claude Desktop

---

## How to Verify It's Working

### 1. Look for the MCP Icon
After restarting Claude Desktop, look at the **bottom of the chat interface** near the input box:
- You should see a small **tool/plugin icon** (🔨 or similar)
- Click on it

### 2. Check for OpenBB MCP
In the tools/connectors panel, you should see:
- **openbb-mcp** server listed
- Categories like: equity, crypto, news, economy, etc.

### 3. Test It
Ask Claude in the chat:
```
What MCP tools do you have access to?
```

Or try:
```
Get the current stock price for Apple (AAPL)
```

---

## Troubleshooting

### Not seeing the connector?

**1. Check config file location**
Make sure the file is in the correct location for your OS (see above).

**2. Verify JSON syntax**
The config must be valid JSON. Use a JSON validator if needed.

**3. Check Claude Desktop version**
Make sure you have a recent version of Claude Desktop that supports MCP.

**4. Check logs**
- **macOS**: `~/Library/Logs/Claude/`
- **Windows**: `%APPDATA%\Claude\logs\`
- **Linux**: `~/.config/Claude/logs/`

**5. Install uvx**
Make sure `uvx` is installed on your system:
```bash
pip install uv
# or
pipx install uv
```

**6. Test the server manually**
Run this to test the server works:
```bash
python3 test_mcp_server.py
```

---

## Prerequisites

### Required Software

1. **Python 3.10+**
   ```bash
   python3 --version
   ```

2. **uvx** (for running the server)
   ```bash
   pip install uv
   # or
   pipx install uv
   ```

3. **OpenBB MCP Server**
   ```bash
   pip install openbb-mcp-server
   ```

---

## What You Get

Once connected, Claude Desktop will have access to:

### Financial Data Categories (34+ providers):
- 📈 **Equity** - Stock prices, fundamentals, estimates
- 💰 **Crypto** - Cryptocurrency data
- 📊 **Economy** - Economic indicators, GDP, employment
- 📰 **News** - Financial news from multiple sources
- 🏦 **Fixed Income** - Bonds, rates, treasuries
- 📉 **Derivatives** - Options and futures
- 🎯 **ETF** - ETF data and holdings
- 💱 **Currency** - Foreign exchange rates
- 🌾 **Commodity** - Commodity prices
- 📍 **Index** - Market indices
- ⚖️ **Regulators** - SEC, CFTC data
- And many more!

---

## Examples

Once connected, try asking Claude:

```
Get me the latest financial data for Tesla (TSLA)
```

```
What are the top economic indicators for the US this quarter?
```

```
Show me the latest crypto prices for Bitcoin and Ethereum
```

```
Get recent financial news about Apple
```

---

## Support

- **OpenBB Documentation**: https://docs.openbb.co
- **MCP Documentation**: https://modelcontextprotocol.io
- **Test Script**: Run `python3 test_mcp_server.py` to verify installation

---

## Notes

- The MCP server uses the `stdio` transport for Claude Desktop
- All data providers are included, but some require API keys
- API keys can be configured in `~/.openbb_platform/user_settings.json`
- The server runs locally on your machine when Claude Desktop starts
