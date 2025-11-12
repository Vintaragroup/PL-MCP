"""
React Flow tools for the MCP server - Enhanced for comprehensive flow diagram development.
"""

from typing import Any, Dict, List
from mcp import types

def get_tools() -> List[types.Tool]:
    """Get all React Flow-related tools."""
    return []  # Empty list - original tools moved to API tools

async def handle_call(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Handle React Flow tool calls."""
    return [types.TextContent(type="text", text=f"Original React Flow tool {name} has been moved to API tools")]