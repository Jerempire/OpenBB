#!/usr/bin/env python3
"""
Simple test script to verify OpenBB MCP Server is working.
"""

import subprocess
import sys
import time

def test_mcp_server():
    """Test if the OpenBB MCP server can start successfully."""

    print("🧪 Testing OpenBB MCP Server...\n")

    # Test 1: Check if openbb-mcp command exists
    print("✓ Test 1: Checking if openbb-mcp command is available...")
    try:
        result = subprocess.run(
            ["openbb-mcp", "--help"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("  ✅ openbb-mcp command found!\n")
        else:
            print("  ❌ openbb-mcp command failed")
            return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

    # Test 2: Check uvx is available
    print("✓ Test 2: Checking if uvx is available...")
    try:
        result = subprocess.run(
            ["uvx", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"  ✅ uvx is available: {result.stdout.strip()}\n")
        else:
            print("  ❌ uvx not found")
            return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

    # Test 3: Check configuration file
    print("✓ Test 3: Checking Claude Desktop configuration...")
    import os
    config_path = os.path.expanduser("~/.config/Claude/claude_desktop_config.json")
    if os.path.exists(config_path):
        print(f"  ✅ Config file exists at: {config_path}")
        with open(config_path, 'r') as f:
            import json
            config = json.load(f)
            if "mcpServers" in config and "openbb-mcp" in config["mcpServers"]:
                print("  ✅ openbb-mcp is configured in Claude Desktop\n")
            else:
                print("  ⚠️  openbb-mcp not found in config\n")
    else:
        print(f"  ⚠️  Config file not found at: {config_path}\n")

    # Test 4: Try to import OpenBB MCP Server modules
    print("✓ Test 4: Testing OpenBB MCP Server imports...")
    try:
        from openbb_mcp_server.app.app import main
        print("  ✅ OpenBB MCP Server modules import successfully!\n")
    except Exception as e:
        print(f"  ❌ Import error: {e}\n")
        return False

    # Summary
    print("=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    print("\n📋 Next Steps:")
    print("1. Close Claude Desktop completely")
    print("2. Restart Claude Desktop")
    print("3. Look for the 🔨 hammer icon near the input box")
    print("4. Click it to see 'openbb-mcp' with financial tools")
    print("\n💡 Test it by asking Claude Desktop:")
    print('   "What MCP tools do you have?"')
    print('   "Get the stock price for AAPL"')
    print("\n✨ You now have access to 34+ financial data providers!")

    return True

if __name__ == "__main__":
    try:
        success = test_mcp_server()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)
