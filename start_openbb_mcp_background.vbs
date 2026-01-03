Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "openbb-mcp --transport streamable-http --host 127.0.0.1 --port 8001 --default-categories equity,crypto,news,economy", 0, False
Set WshShell = Nothing
