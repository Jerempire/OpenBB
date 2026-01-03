@echo off
REM Start OpenBB MCP Server for Claude Desktop (HTTP mode)
REM This runs in the background and Claude Desktop connects via HTTP

echo Starting OpenBB MCP Server...
echo Server will run at http://localhost:8001/mcp
echo.
echo Press Ctrl+C to stop the server
echo.

openbb-mcp --transport streamable-http --host 127.0.0.1 --port 8001 --default-categories equity,crypto,news,economy
