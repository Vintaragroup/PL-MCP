#!/usr/bin/env python3
"""
Simple MCP Integration for VS Code
Usage: python3 simple_mcp_client.py <tool_name> [arguments...]
"""

import sys
import json
import subprocess

def call_mcp_tool(tool_name, **kwargs):
    """Call an MCP tool with simplified interface."""
    
    # Create the test command based on tool type
    if tool_name == "react_component":
        component_name = kwargs.get("name", "MyComponent")
        cmd = f'''
import asyncio
from src.frontend_mcp_server.main import handle_call_tool

async def main():
    result = await handle_call_tool("react_component_generator", {{
        "component_name": "{component_name}",
        "styling": "tailwind"
    }})
    print(result[0].text)

asyncio.run(main())
'''
    
    elif tool_name == "tailwind_suggest":
        description = kwargs.get("description", "blue button")
        element_type = kwargs.get("type", "button")
        cmd = f'''
import asyncio
from src.frontend_mcp_server.main import handle_call_tool

async def main():
    result = await handle_call_tool("tailwind_class_suggester", {{
        "design_description": "{description}",
        "element_type": "{element_type}",
        "responsive": True
    }})
    print(result[0].text)

asyncio.run(main())
'''
    
    elif tool_name == "react_hook":
        hook_name = kwargs.get("name", "useMyHook")
        functionality = kwargs.get("functionality", "Custom hook functionality")
        cmd = f'''
import asyncio
from src.frontend_mcp_server.main import handle_call_tool

async def main():
    result = await handle_call_tool("react_hook_generator", {{
        "hook_name": "{hook_name}",
        "functionality": "{functionality}"
    }})
    print(result[0].text)

asyncio.run(main())
'''
    
    elif tool_name == "list_tools":
        cmd = '''
import asyncio
from src.frontend_mcp_server.main import handle_list_tools

async def main():
    tools = await handle_list_tools()
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")

asyncio.run(main())
'''
    
    else:
        print(f"Unknown tool: {tool_name}")
        print("Available tools: react_component, tailwind_suggest, react_hook, list_tools")
        return
    
    # Execute in the container
    try:
        result = subprocess.run([
            "docker", "exec", "-i", "frontend-mcp-server",
            "python", "-c", cmd
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("Tool execution timed out")
    except Exception as e:
        print(f"Error executing tool: {e}")

def main():
    if len(sys.argv) < 2:
        print("Frontend MCP Tools")
        print("Usage: python3 simple_mcp_client.py <tool_name> [options]")
        print("")
        print("Examples:")
        print("  python3 simple_mcp_client.py list_tools")
        print("  python3 simple_mcp_client.py react_component --name LoginButton")
        print("  python3 simple_mcp_client.py tailwind_suggest --description 'red button with shadow' --type button")
        print("  python3 simple_mcp_client.py react_hook --name useCounter --functionality 'Counter with increment/decrement'")
        return
    
    tool_name = sys.argv[1]
    
    # Parse simple arguments
    kwargs = {}
    i = 2
    while i < len(sys.argv):
        if sys.argv[i].startswith('--'):
            key = sys.argv[i][2:]
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith('--'):
                kwargs[key] = sys.argv[i + 1]
                i += 2
            else:
                kwargs[key] = True
                i += 1
        else:
            i += 1
    
    call_mcp_tool(tool_name, **kwargs)

if __name__ == "__main__":
    main()