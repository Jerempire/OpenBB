# OpenBB MCP Auto-Start Setup (No Manual PowerShell!)

This guide sets up the OpenBB MCP server to start automatically in the background when Windows boots.

## One-Time Setup (5 minutes)

### Step 1: Copy the startup script

1. Copy `start_openbb_mcp_background.vbs` from this repository to your Windows machine
2. Save it somewhere permanent like: `C:\OpenBB\start_openbb_mcp_background.vbs`

### Step 2: Add to Windows Startup

**Option A: Using Startup Folder (Easiest)**

1. Press `Windows + R`
2. Type: `shell:startup` and press Enter
3. Right-click in the folder → New → Shortcut
4. Browse to where you saved `start_openbb_mcp_background.vbs`
5. Click Next → Finish

**Option B: Using Task Scheduler (More Control)**

1. Press `Windows + R`
2. Type: `taskschd.msc` and press Enter
3. Click "Create Basic Task"
4. Name: "OpenBB MCP Server"
5. Trigger: "When I log on"
6. Action: "Start a program"
7. Browse to `start_openbb_mcp_background.vbs`
8. Check "Open the Properties dialog"
9. In Properties:
   - Check "Run whether user is logged on or not"
   - Check "Run with highest privileges"
   - Click OK

### Step 3: Update Claude Desktop Config

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "VectorBT PRO": {
      "command": "C:\\Users\\jmj2z\\anaconda3\\envs\\vectorbtpro-clean\\python.exe",
      "args": [
        "-m",
        "vectorbtpro.mcp_server"
      ],
      "env": {
        "VBT_SETTINGS_PATH": "C:\\Users\\jmj2z\\.claude\\vbt.cfg"
      }
    },
    "openbb-mcp": {
      "url": "http://localhost:8001/mcp"
    }
  },
  "preferences": {
    "chromeExtensionEnabled": true
  }
}
```

**Key change:**
- ❌ OLD: Uses `"command"` and `"args"` (stdio transport - broken)
- ✅ NEW: Uses `"url": "http://localhost:8001/mcp"` (HTTP transport - reliable)

### Step 4: Start it now (first time only)

Double-click `start_openbb_mcp_background.vbs` to start the server now.

### Step 5: Restart Claude Desktop

Completely quit and restart Claude Desktop.

---

## How It Works

1. **At Windows Startup**: The VBS script runs invisibly in the background
2. **Server Starts**: OpenBB MCP server starts on `http://localhost:8001/mcp`
3. **Claude Connects**: Claude Desktop connects via HTTP (no stdio issues)
4. **No Windows**: Everything runs silently, no PowerShell windows

---

## Verification

### Check if Server is Running

Open PowerShell and run:
```powershell
curl http://localhost:8001/health
```

If you see a response, the server is running!

### Check in Claude Desktop

1. Open Claude Desktop
2. Look at connectors
3. You should see **openbb-mcp** listed

---

## Troubleshooting

### Server Not Starting?

Check if it's running:
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*openbb*"}
```

### Wrong Port Already in Use?

If port 8001 is taken, edit the VBS script and change `8001` to `8002` (or any other port).

Then update your Claude config to match:
```json
"url": "http://localhost:8002/mcp"
```

### Stop the Server

```powershell
Get-Process | Where-Object {$_.CommandLine -like "*openbb-mcp*"} | Stop-Process
```

Or just restart your computer.

---

## Benefits

✅ **No manual PowerShell** - Starts automatically
✅ **No visible windows** - Runs silently in background
✅ **No stdio issues** - Uses reliable HTTP transport
✅ **Survives restarts** - Auto-starts on Windows boot
✅ **Works with Claude Desktop** - Stable connection

---

## Uninstall

1. Delete the shortcut from Startup folder (run `shell:startup`)
2. OR delete the scheduled task from Task Scheduler
3. Remove `"openbb-mcp"` section from Claude Desktop config
4. Delete the VBS file

---

## Alternative: Stop It From Auto-Starting

If you want to keep it installed but not have it auto-start:

1. Go to Startup folder (`shell:startup`)
2. Delete the shortcut
3. Manually double-click the VBS file when you want to use it

---

## Files

- `start_openbb_mcp_background.vbs` - Invisible background launcher
- `start_openbb_mcp.bat` - Visible console version (for debugging)

Use the `.vbs` file for normal use (invisible).
Use the `.bat` file if you need to see output for debugging.
