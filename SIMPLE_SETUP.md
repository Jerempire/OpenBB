# 🚀 OpenBB MCP - Simple Setup Guide for Your Local Machine

## What You Need
- ✅ Python 3.10 or later
- ✅ Git
- ✅ Terminal/Command Prompt

## Step-by-Step Instructions

### 1️⃣ Open Terminal on Your Computer

**Mac:** Press `Cmd + Space`, type "Terminal"
**Windows:** Press `Win + R`, type "cmd"
**Linux:** Press `Ctrl + Alt + T`

### 2️⃣ Clone Your Repository

Copy and paste this into your terminal:

```bash
cd ~
git clone https://github.com/Jerempire/OpenBB.git
cd OpenBB
```

✅ **What this does:** Downloads your configured OpenBB code to your computer

### 3️⃣ Install Everything (One Command!)

Copy and paste this entire block:

```bash
# Go to OpenBB directory
cd ~/OpenBB/openbb_platform

# Install MCP server
cd extensions/mcp_server && pip install -e .

# Install all providers
cd ../../providers/fred && pip install -e .
cd ../fmp && pip install -e .
cd ../polygon && pip install -e .
cd ../alpha_vantage && pip install -e .

# Install extensions
cd ../../extensions/economy && pip install -e .
cd ../equity && pip install -e .
cd ../news && pip install -e .

echo "✅ Installation complete!"
```

⏱️ **Wait 2-3 minutes** for installation to complete

### 4️⃣ Add Your API Keys

Copy and paste this:

```bash
# Create config directory
mkdir -p ~/.openbb_platform

# Create API keys file
cat > ~/.openbb_platform/user_settings.json << 'EOF'
{
  "credentials": {
    "fred_api_key": "4532dbd3e3fb05a0ab2587a8e0ea25ec",
    "fmp_api_key": "uiGSf4RawQoYOvee0bqQn63tVPghyflw",
    "polygon_api_key": "d9CUa475dRkblSB1T5FJrvliZpq6Pe2F",
    "alpha_vantage_api_key": "DLZ3UQJN1D7FQVDP"
  }
}
EOF

echo "✅ API keys configured!"
```

### 5️⃣ Start the Server

```bash
openbb-mcp
```

You should see:
```
╭──────────────────────────────────────────╮
│            FastMCP 2.14.2                │
│         Server: OpenBB MCP               │
│  http://127.0.0.1:8001/mcp               │
╰──────────────────────────────────────────╯
```

✅ **SUCCESS!** Your server is running!

### 6️⃣ Test It Works

**Open a NEW terminal** (keep the server running) and run:

```bash
python3 << 'EOF'
from openbb import obb

# Get unemployment rate
result = obb.economy.fred_series(symbol="UNRATE", provider="fred", start_date="2024-01-01")
print("✅ FRED Working! Unemployment data:")
print(result.to_dataframe().tail())

# Get Apple stock quote
result = obb.equity.price.quote(symbol="AAPL", provider="fmp")
print("\n✅ FMP Working! Apple quote:")
print(result.to_dataframe())
EOF
```

If you see data (not errors), **IT WORKS!** 🎉

## 🖥️ Use with Claude Desktop (Optional)

### Mac/Linux:
```bash
# Open Claude Desktop config
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Add this to the file:
```json
{
  "mcpServers": {
    "openbb": {
      "command": "openbb-mcp",
      "args": ["--transport", "stdio"]
    }
  }
}
```

### Restart Claude Desktop

Now you can chat with Claude and ask:
- "What's the current CPI?"
- "Get Apple's stock price"
- "Show me unemployment trends"

## 🎯 Quick Commands

```bash
# Start server (default port 8001)
openbb-mcp

# Start with specific categories
openbb-mcp --default-categories economy,equity

# Start on different port
openbb-mcp --port 8080

# Stop server
Press Ctrl+C
```

## ❓ Troubleshooting

### "Command not found: openbb-mcp"
```bash
pip install --upgrade pip
cd ~/OpenBB/openbb_platform/extensions/mcp_server
pip install -e .
```

### "Permission denied"
Add `sudo` before commands (Linux/Mac):
```bash
sudo pip install -e .
```

### "Python not found"
Install Python 3.10+:
- Mac: `brew install python@3.11`
- Windows: Download from python.org
- Linux: `sudo apt install python3.11`

## 📞 What You Can Query

Once running, your MCP server can fetch:

- **Economic Data:** GDP, inflation, unemployment, interest rates
- **Stock Data:** Real-time quotes, historical prices, fundamentals
- **Company Data:** Financial statements, analyst estimates, news
- **Market Data:** Indices, sectors, commodities, forex
- **And much more!**

## 🎉 You're Done!

Your OpenBB MCP server is now running on your local machine with full access to:
- ✅ FRED economic data
- ✅ FMP stock market data
- ✅ Polygon market data
- ✅ Alpha Vantage technical data

**No more 403 errors!** 🚀
