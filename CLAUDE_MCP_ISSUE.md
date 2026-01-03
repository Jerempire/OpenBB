# Claude Desktop MCP Integration Issue

## Problem Summary

The OpenBB MCP server (v1.2.2) crashes during initialization when connecting to Claude Desktop, preventing the connector from appearing in the UI.

## Environment

- **OpenBB MCP Server**: v1.2.2
- **Claude Desktop**: Latest version (Windows)
- **Python**: 3.13
- **uvx**: 0.9.18
- **OS**: Windows 11

## Error Details

### Symptoms
- Server starts successfully
- Begins initialization process
- Crashes with error at `app.py:773`
- Times out after ~10 seconds
- Never completes MCP protocol handshake

### Log Evidence

```
[01/03/26 12:56:38] ERROR    Server error:                           app.py:773
2026-01-03T18:56:40.479Z [openbb-mcp] [info] Server transport closed
2026-01-03T18:56:42.986Z [openbb-mcp] [error] Server disconnected
```

### Full Error Sequence

1. ✅ Server initialization begins
2. ✅ All dependencies load (with deprecation warnings)
3. ✅ Claude Desktop sends initialize request
4. ❌ **Error occurs at app.py:773**
5. ❌ Server transport closes unexpectedly
6. ❌ Connection times out

## Configuration Tested

### Config File Location
`%APPDATA%\Claude\claude_desktop_config.json`

### Attempted Configurations

**1. Standard Configuration (Failed)**
```json
{
  "mcpServers": {
    "openbb-mcp": {
      "command": "C:\\Users\\jmj2z\\.local\\bin\\uvx.exe",
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

**2. Minimal Configuration (Failed)**
```json
{
  "mcpServers": {
    "openbb-mcp": {
      "command": "C:\\Users\\jmj2z\\.local\\bin\\uvx.exe",
      "args": [
        "--from",
        "openbb-mcp-server",
        "--with",
        "openbb",
        "openbb-mcp",
        "--transport",
        "stdio",
        "--default-categories",
        "admin",
        "--no-tool-discovery"
      ]
    }
  }
}
```

## Manual Testing

### Server Works Standalone
```powershell
PS> uvx --from openbb-mcp-server --with openbb openbb-mcp --transport stdio
# Server starts successfully and waits for input
# All deprecation warnings appear but no crashes
```

### Claude Desktop Integration Fails
- Server crashes during Claude Desktop's initialization handshake
- Error occurs after receiving initialize request from Claude Desktop
- Specific error at line 773 in app.py

## Investigation Needed

### Questions

1. **What is happening at app.py:773?**
   - Need to examine `/home/user/OpenBB/openbb_platform/extensions/mcp_server/openbb_mcp_server/app/app.py:773`
   - What code is executing when the error occurs?

2. **Is this a timeout issue?**
   - The server has ~10 seconds before timeout
   - Loading all providers may exceed this limit
   - Even with `--default-categories admin` it still times out

3. **Is this a Python 3.13 compatibility issue?**
   - Many deprecation warnings related to Pydantic validators
   - May be incompatible with Python 3.13

4. **Is this a Windows-specific issue?**
   - Path handling differences
   - Process communication issues with stdio on Windows

## Possible Root Causes

### 1. Initialization Timeout
- Claude Desktop may have a strict timeout (60 seconds based on logs)
- OpenBB loading all 34+ providers takes too long
- Even minimal config exceeds timeout

### 2. Python 3.13 Incompatibility
- Pydantic deprecation warnings suggest compatibility issues
- `@model_validator(mode='after')` on classmethods deprecated in Pydantic 2.12

### 3. Stdio Communication Issue
- Windows stdio handling differs from Unix
- Buffer flushing problems
- Process pipe communication errors

### 4. Bug in app.py:773
- Unknown error in the actual code
- Need to inspect source to determine

## Next Steps

### Immediate Actions

1. **Inspect app.py:773**
   ```bash
   # Line 773 in the MCP server app file
   cat -n /home/user/OpenBB/openbb_platform/extensions/mcp_server/openbb_mcp_server/app/app.py | sed -n '770,780p'
   ```

2. **Add Debug Logging**
   - Add stderr logging around line 773
   - Identify exact failure point

3. **Test Python Version**
   - Try with Python 3.10 or 3.11
   - Check if Python 3.13 is the issue

4. **Test on Linux/Mac**
   - Verify if this is Windows-specific
   - Test stdio transport on different OS

### Potential Fixes

**Option 1: Fix the Bug**
- Identify and fix the code at app.py:773
- Submit PR to OpenBB repository

**Option 2: Use HTTP Transport**
- Run server separately with HTTP transport
- Connect Claude Desktop via HTTP URL instead of stdio
- More stable but less integrated

**Option 3: Downgrade Dependencies**
- Use Python 3.11 instead of 3.13
- Downgrade Pydantic if needed
- Test with older dependency versions

**Option 4: Increase Timeout**
- Configure Claude Desktop with longer timeout (if possible)
- Optimize server startup time

## Workaround: HTTP Transport

If stdio continues to fail, use HTTP transport instead:

**1. Start server manually:**
```powershell
openbb-mcp --transport streamable-http --host 127.0.0.1 --port 8001
```

**2. Configure Claude Desktop:**
```json
{
  "mcpServers": {
    "openbb-mcp": {
      "url": "http://localhost:8001/mcp/"
    }
  }
}
```

This bypasses the stdio communication issues.

## Files to Investigate

1. `/home/user/OpenBB/openbb_platform/extensions/mcp_server/openbb_mcp_server/app/app.py` (line 773)
2. `/home/user/OpenBB/openbb_platform/extensions/mcp_server/openbb_mcp_server/models/settings.py`
3. `/home/user/OpenBB/openbb_platform/extensions/mcp_server/pyproject.toml`

## References

- [MCP Debugging Documentation](https://modelcontextprotocol.io/docs/tools/debugging)
- [OpenBB MCP Server README](/home/user/OpenBB/openbb_platform/extensions/mcp_server/README.md)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

## Status

**Current**: ❌ Non-functional - Server crashes on initialization

**Blocker**: Unknown error at app.py:773

**Priority**: High - Prevents Claude Desktop integration entirely
