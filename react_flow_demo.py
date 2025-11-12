#!/usr/bin/env python3
"""
React Flow MCP Client - Demonstrate enhanced React Flow context
"""

import subprocess
import json

def call_react_flow_tool(tool_name: str, **kwargs):
    """Call React Flow MCP tools."""
    
    if tool_name == "react_flow_diagram":
        diagram_type = kwargs.get("type", "flowchart")
        complexity = kwargs.get("complexity", "moderate")
        cmd = f'''
import asyncio
from src.frontend_mcp_server.tools.react_flow_tools import handle_call

async def main():
    result = await handle_call("react_flow_diagram_generator", {{
        "diagram_type": "{diagram_type}",
        "complexity": "{complexity}",
        "interactive_features": ["drag_drop", "zoom_controls", "minimap"],
        "styling_theme": "modern"
    }})
    print(result[0].text)

asyncio.run(main())
'''
        
    elif tool_name == "react_flow_custom_node":
        node_type = kwargs.get("type", "decision")
        cmd = f'''
import asyncio
from src.frontend_mcp_server.tools.react_flow_tools import handle_call

async def main():
    result = await handle_call("react_flow_custom_node_generator", {{
        "node_type": "{node_type}",
        "has_inputs": True,
        "has_outputs": True,
        "data_fields": [
            {{"name": "condition", "type": "string", "required": True}},
            {{"name": "result", "type": "boolean", "required": False}}
        ],
        "styling": "tailwind"
    }})
    print(result[0].text)

asyncio.run(main())
'''
        
    elif tool_name == "react_flow_layout":
        layout_type = kwargs.get("layout", "hierarchical")
        cmd = f'''
import asyncio
from src.frontend_mcp_server.tools.react_flow_tools import handle_call

async def main():
    result = await handle_call("react_flow_layout_optimizer", {{
        "layout_type": "{layout_type}",
        "node_count": 15,
        "direction": "TB"
    }})
    print(result[0].text)

asyncio.run(main())
'''
        
    else:
        print(f"Unknown React Flow tool: {tool_name}")
        print("Available tools: react_flow_diagram, react_flow_custom_node, react_flow_layout")
        return
    
    # Execute in container
    try:
        result = subprocess.run([
            "docker", "exec", "-i", "frontend-mcp-server",
            "python", "-c", cmd
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
            
    except Exception as e:
        print(f"Error: {e}")

def demo_react_flow_context():
    """Demonstrate how MCP enhances React Flow development context."""
    
    print("🌊 React Flow MCP Context Demo")
    print("=" * 60)
    
    print("\n📋 How MCP Enhances React Flow Development:")
    print("1. Context-aware diagram generation based on use case")
    print("2. Custom node components with proper TypeScript interfaces")
    print("3. Optimal layout algorithms for different diagram types")
    print("4. Performance-optimized edge configurations")
    print("5. Theme-aware styling with accessibility considerations")
    
    print("\n🎯 Scenario: Building a Workflow Management System")
    print("-" * 60)
    
    print("\n🔧 1. Generate Workflow Diagram Structure:")
    call_react_flow_tool("react_flow_diagram", type="workflow", complexity="complex")
    
    print("\n" + "="*60)
    print("\n🧩 2. Create Custom Decision Node:")
    call_react_flow_tool("react_flow_custom_node", type="decision")
    
    print("\n" + "="*60)
    print("\n📐 3. Optimize Layout for Hierarchical Flow:")
    call_react_flow_tool("react_flow_layout", layout="hierarchical")
    
    print("\n" + "="*60)
    print("\n💡 Key Benefits for React Flow Development:")
    print("✅ Context-aware code generation based on diagram type")
    print("✅ TypeScript interfaces automatically generated")
    print("✅ Performance optimizations included")
    print("✅ Accessibility and responsive design considerations")
    print("✅ Best practices and architectural guidance")
    print("✅ Ready-to-use code with proper error handling")
    
    print("\n🚀 This is how MCP transforms React Flow development:")
    print("- No more googling for React Flow patterns")
    print("- Instant, context-aware code generation")  
    print("- Architectural guidance built into every suggestion")
    print("- Performance and accessibility considered from the start")

if __name__ == "__main__":
    demo_react_flow_context()