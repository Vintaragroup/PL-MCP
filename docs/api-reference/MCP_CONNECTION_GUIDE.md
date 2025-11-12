# 🔌 Connecting to Your Frontend MCP Server

## Quick Start Options

### Option 1: Claude Desktop (Easiest) ⭐

1. **Install Claude Desktop** (if not already installed)
2. **Copy the config file**:
   ```bash
   # macOS
   cp claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
   
   # Linux
   cp claude_desktop_config.json ~/.config/claude/claude_desktop_config.json
   ```
3. **Restart Claude Desktop**
4. **Verify connection** - You should see your MCP tools available in Claude

### Option 2: VS Code with Continue Extension

1. **Install Continue extension** in VS Code
2. **Configure Continue** to use MCP:
   ```json
   {
     "models": [...],
     "mcpServers": {
       "frontend-mcp-server": {
         "command": "docker",
         "args": ["exec", "-i", "frontend-mcp-server", "python", "-m", "frontend_mcp_server.main"]
       }
     }
   }
   ```

### Option 3: Direct Python Client (Custom Integration)

Run the included MCP client:
```bash
python3 mcp_client.py
```

This will demonstrate all the tools and show you how to integrate them into your own applications.

## 🧪 Testing Your Connection

Test the MCP server is accessible:

```bash
# Quick test - should show all 4 tools working
docker exec -it frontend-mcp-server python tests/test_server.py

# Interactive demo with the Python client
python3 mcp_client.py
```

## 🔧 GitHub Copilot Integration

**Note**: GitHub Copilot doesn't natively support MCP servers yet, but you can:

1. **Use the tools manually** via the Python client
2. **Create VS Code snippets** from generated code
3. **Integrate with Claude Desktop** for AI assistance

### Creating VS Code Snippets from MCP Output

Example workflow:
1. Use MCP client to generate React component
2. Save as VS Code snippet
3. Use with Copilot for enhanced suggestions

```bash
# Generate component and save as snippet
python3 -c "
import asyncio
from mcp_client import MCPClient

async def main():
    client = MCPClient()
    component = await client.call_tool('react_component_generator', {
        'component_name': 'ButtonTemplate',
        'styling': 'tailwind'
    })
    
    # Save to VS Code snippets
    with open('.vscode/snippets.json', 'w') as f:
        f.write(component)

asyncio.run(main())
"
```

## 🚀 Advanced Integration: Custom MCP Client

For full integration with your development workflow:

1. **Modify `mcp_client.py`** to suit your needs
2. **Create VS Code tasks** that call MCP tools
3. **Set up keyboard shortcuts** for common operations

Example VS Code task:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Generate React Component",
      "type": "shell",
      "command": "python3",
      "args": ["mcp_client.py", "--tool", "react_component_generator"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

## 🔍 Troubleshooting

- **Container not running**: `docker-compose up -d`
- **Permission issues**: Make sure Docker has proper permissions
- **Port conflicts**: The MCP server uses stdio, not HTTP ports
- **Python dependencies**: Use the containerized version to avoid local setup

## 🎯 Next Steps

1. **Try the Python client demo**: `python3 mcp_client.py`
2. **Configure Claude Desktop** for the best experience
3. **Create custom integrations** using the MCP client as a template
4. **Build VS Code extensions** that leverage your MCP tools

Your Frontend MCP Server is ready to supercharge your development workflow! 🚀