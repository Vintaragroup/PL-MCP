#!/usr/bin/env python3
"""
Simple test script to verify the MCP server tools work correctly.
"""

import asyncio
import json

async def test_tools():
    """Test all the tools by calling them directly."""
    print("Testing Frontend MCP Server Tools...")
    
    # Import the handlers directly
    from src.frontend_mcp_server.main import handle_list_tools, handle_call_tool
    
    # Test list tools
    print("\n1. Testing list_tools...")
    tools = await handle_list_tools()
    print(f"Available tools: {[tool.name for tool in tools]}")
    
    # Test React component generator
    print("\n2. Testing react_component_generator...")
    result = await handle_call_tool("react_component_generator", {
        "component_name": "TestButton",
        "props": [
            {"name": "label", "type": "string", "optional": False},
            {"name": "onClick", "type": "() => void", "optional": True}
        ],
        "styling": "tailwind"
    })
    print("Generated component (first 200 chars):")
    print(result[0].text[:200] + "...")
    
    # Test Tailwind suggester
    print("\n3. Testing tailwind_class_suggester...")
    result = await handle_call_tool("tailwind_class_suggester", {
        "design_description": "blue centered button with shadow",
        "element_type": "button",
        "responsive": True
    })
    print("Tailwind suggestions (first 200 chars):")
    print(result[0].text[:200] + "...")
    
    # Test package analyzer
    print("\n4. Testing package_analyzer...")
    package_json = {
        "dependencies": {
            "react": "^18.0.0",
            "react-dom": "^18.0.0",
            "tailwindcss": "^3.0.0"
        },
        "devDependencies": {
            "typescript": "^5.0.0"
        }
    }
    result = await handle_call_tool("package_analyzer", {
        "package_json": json.dumps(package_json),
        "analysis_type": "all"
    })
    print("Package analysis (first 200 chars):")
    print(result[0].text[:200] + "...")
    
    # Test React hook generator
    print("\n5. Testing react_hook_generator...")
    result = await handle_call_tool("react_hook_generator", {
        "hook_name": "useApiData",
        "functionality": "Fetch data from an API endpoint with loading and error states"
    })
    print("Generated hook (first 200 chars):")
    print(result[0].text[:200] + "...")
    
    print("\n✅ All tools tested successfully!")

if __name__ == "__main__":
    asyncio.run(test_tools())