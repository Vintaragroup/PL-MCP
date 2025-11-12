#!/usr/bin/env python3
"""
MCP Client for Frontend MCP Server
Connects to the containerized MCP server and allows tool interaction.
"""

import asyncio
import json
import subprocess
from typing import Dict, Any, List

class MCPClient:
    def __init__(self):
        self.container_name = "frontend-mcp-server"
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Call a tool on the MCP server."""
        try:
            # Create the command to execute in the container
            cmd = [
                "docker", "exec", "-i", self.container_name,
                "python", "-c", f"""
import asyncio
import json
from src.frontend_mcp_server.main import handle_call_tool

async def main():
    result = await handle_call_tool("{tool_name}", {json.dumps(arguments)})
    print(result[0].text)

asyncio.run(main())
"""
            ]
            
            # Execute the command
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                return stdout.decode().strip()
            else:
                return f"Error: {stderr.decode()}"
                
        except Exception as e:
            return f"Client error: {str(e)}"
    
    async def list_tools(self) -> List[str]:
        """List available tools."""
        try:
            cmd = [
                "docker", "exec", "-i", self.container_name,
                "python", "-c", """
import asyncio
from src.frontend_mcp_server.main import handle_list_tools

async def main():
    tools = await handle_list_tools()
    for tool in tools:
        print(f"{tool.name}: {tool.description}")

asyncio.run(main())
"""
            ]
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                return stdout.decode().strip().split('\n')
            else:
                return [f"Error: {stderr.decode()}"]
                
        except Exception as e:
            return [f"Client error: {str(e)}"]

async def interactive_demo():
    """Interactive demo of the MCP client."""
    client = MCPClient()
    
    print("🚀 Frontend MCP Client")
    print("=" * 50)
    
    # List available tools
    print("\n📋 Available Tools:")
    tools = await client.list_tools()
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool}")
    
    print("\n" + "=" * 50)
    print("🧪 Demo: Testing Each Tool")
    print("=" * 50)
    
    # Demo React Component Generator
    print("\n🔧 1. React Component Generator")
    result = await client.call_tool("react_component_generator", {
        "component_name": "LoginForm",
        "props": [
            {"name": "onSubmit", "type": "(email: string, password: string) => void", "optional": False},
            {"name": "loading", "type": "boolean", "optional": True}
        ],
        "styling": "tailwind"
    })
    print("Generated component:")
    print("```tsx")
    print(result[:500] + "..." if len(result) > 500 else result)
    print("```")
    
    # Demo Tailwind Suggester
    print("\n🎨 2. Tailwind Class Suggester")
    result = await client.call_tool("tailwind_class_suggester", {
        "design_description": "modern card with gradient background and hover effect",
        "element_type": "card",
        "responsive": True
    })
    print("Tailwind suggestions:")
    print(result[:400] + "..." if len(result) > 400 else result)
    
    # Demo Package Analyzer
    print("\n📦 3. Package Analyzer")
    sample_package = {
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "next": "^14.0.0",
            "tailwindcss": "^3.3.0",
            "@types/react": "^18.2.0"
        },
        "devDependencies": {
            "typescript": "^5.0.0",
            "eslint": "^8.0.0"
        }
    }
    result = await client.call_tool("package_analyzer", {
        "package_json": json.dumps(sample_package),
        "analysis_type": "all"
    })
    print("Package analysis:")
    print(result[:400] + "..." if len(result) > 400 else result)
    
    # Demo React Hook Generator
    print("\n⚡ 4. React Hook Generator")
    result = await client.call_tool("react_hook_generator", {
        "hook_name": "useLocalStorage",
        "functionality": "Persist state to localStorage with automatic synchronization"
    })
    print("Generated hook:")
    print("```tsx")
    print(result[:400] + "..." if len(result) > 400 else result)
    print("```")
    
    print("\n" + "=" * 50)
    print("✅ Demo Complete! Your MCP server is working perfectly.")
    print("💡 Use this client script to integrate with other tools or IDEs.")

if __name__ == "__main__":
    asyncio.run(interactive_demo())