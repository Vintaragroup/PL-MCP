"""
TypeScript tools for the MCP server.
"""

from typing import Any, Dict, List

from mcp.types import Tool, TextContent


def get_tools() -> List[Tool]:
    """Get all TypeScript-related tools."""
    return [
        Tool(
            name="typescript_interface_generator",
            description="Generate TypeScript interfaces from JSON or requirements",
            inputSchema={
                "type": "object",
                "properties": {
                    "data_source": {
                        "type": "string",
                        "description": "JSON data or description to generate interface from"
                    },
                    "interface_name": {
                        "type": "string",
                        "description": "Name for the generated interface"
                    }
                },
                "required": ["data_source", "interface_name"]
            }
        )
    ]


async def handle_call(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle TypeScript tool calls."""
    
    if name == "typescript_interface_generator":
        return await generate_interface(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown TypeScript tool: {name}")]


async def generate_interface(args: Dict[str, Any]) -> List[TextContent]:
    """Generate TypeScript interface."""
    data_source = args.get("data_source", "")
    interface_name = args.get("interface_name", "MyInterface")
    
    result = f"""
# TypeScript Interface: {interface_name}

```typescript
interface {interface_name} {{
  // Generated based on: {data_source[:50]}...
  id: string;
  name: string;
  // Add specific properties based on your data
}}
```
"""
    
    return [TextContent(type="text", text=result)]