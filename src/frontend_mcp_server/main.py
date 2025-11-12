#!/usr/bin/env python3
"""
Frontend MCP Server - A Model Context Protocol server for frontend development tools.
"""

import asyncio
import json
from mcp.server import Server
from mcp import types
from mcp.server.stdio import stdio_server

# Import React Flow tools
from .tools import react_flow_tools
from .tools import react_flow_api_tools
from .tools import react_flow_learning_tools
from .tools import connection_positioning_tools

app = Server("frontend-mcp-server")

@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available frontend development tools."""
    # Get React Flow tools
    react_flow_tool_list = react_flow_tools.get_tools()
    react_flow_api_tool_list = react_flow_api_tools.get_tools()
    react_flow_learning_tool_list = react_flow_learning_tools.get_tools()
    connection_positioning_tool_list = connection_positioning_tools.get_tools()
    
    return [
        types.Tool(
            name="react_component_generator",
            description="Generate React components with TypeScript and best practices",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_name": {
                        "type": "string", 
                        "description": "Name of the React component"
                    },
                    "props": {
                        "type": "array",
                        "description": "Component props definition",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "type": {"type": "string"},
                                "optional": {"type": "boolean", "default": False}
                            }
                        },
                        "default": []
                    },
                    "styling": {
                        "type": "string",
                        "enum": ["tailwind", "css-modules", "styled-components", "none"],
                        "description": "Styling approach",
                        "default": "tailwind"
                    }
                },
                "required": ["component_name"]
            }
        ),
        types.Tool(
            name="tailwind_class_suggester",
            description="Suggest Tailwind CSS classes based on design requirements",
            inputSchema={
                "type": "object",
                "properties": {
                    "design_description": {
                        "type": "string",
                        "description": "Description of the desired design/styling"
                    },
                    "element_type": {
                        "type": "string",
                        "enum": ["button", "card", "form", "navigation", "layout", "text", "general"],
                        "description": "Type of element to style"
                    },
                    "responsive": {
                        "type": "boolean",
                        "description": "Whether to include responsive variants",
                        "default": True
                    }
                },
                "required": ["design_description", "element_type"]
            }
        ),
        types.Tool(
            name="package_analyzer",
            description="Analyze package.json for dependencies, vulnerabilities, and optimization opportunities",
            inputSchema={
                "type": "object",
                "properties": {
                    "package_json": {
                        "type": "string",
                        "description": "Content of package.json file"
                    },
                    "analysis_type": {
                        "type": "string",
                        "enum": ["dependencies", "vulnerabilities", "optimization", "all"],
                        "description": "Type of analysis to perform",
                        "default": "all"
                    }
                },
                "required": ["package_json"]
            }
        ),
        types.Tool(
            name="react_hook_generator",
            description="Generate custom React hooks with TypeScript",
            inputSchema={
                "type": "object",
                "properties": {
                    "hook_name": {
                        "type": "string",
                        "description": "Name of the custom hook"
                    },
                    "functionality": {
                        "type": "string",
                        "description": "Description of what the hook should do"
                    }
                },
                "required": ["hook_name", "functionality"]
            }
        )
    ] + react_flow_tool_list + react_flow_api_tool_list + react_flow_learning_tool_list + connection_positioning_tool_list  # Add all React Flow tools

@app.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    """Handle tool execution."""
    if arguments is None:
        arguments = {}
    
    if name == "react_component_generator":
        component_name = arguments.get("component_name", "MyComponent")
        props = arguments.get("props", [])
        styling = arguments.get("styling", "tailwind")
        
        # Generate props interface
        props_interface = ""
        if props:
            props_interface = f"""
interface {component_name}Props {{
{chr(10).join(f"  {prop['name']}{'?' if prop.get('optional', False) else ''}: {prop['type']};" for prop in props)}
}}
"""
        
        # Generate component
        style_classes = 'className="p-4 rounded-lg shadow-sm"' if styling == "tailwind" else 'className="component"'
        title_classes = "text-xl font-bold mb-2" if styling == "tailwind" else "component-title"
        text_classes = "text-gray-600" if styling == "tailwind" else "component-text"
        desc_classes = "text-sm text-gray-500" if styling == "tailwind" else "component-description"
        
        prop_elements = []
        for prop in props:
            if prop['type'] in ['string', 'number']:
                prop_elements.append(f'      <p className="{text_classes}">{{{prop["name"]}}}</p>')
        
        component_code = f"""
import React from 'react';
{props_interface}
/**
 * {component_name} Component
 * Generated by Frontend MCP Server
 */
export const {component_name}: React.FC{('<' + component_name + 'Props>') if props else ''} = ({'{'}
{chr(10).join(f"  {prop['name']}," for prop in props) if props else ''}
{'}) => {' if props else '() => {'}
  return (
    <div {style_classes}>
      <h2 className="{title_classes}">{component_name}</h2>
      {chr(10).join(prop_elements)}
      <p className="{desc_classes}">Component ready for customization!</p>
    </div>
  );
{'}};'}

export default {component_name};
"""
        
        return [types.TextContent(type="text", text=component_code.strip())]
    
    elif name == "tailwind_class_suggester":
        description = arguments.get("design_description", "").lower()
        element_type = arguments.get("element_type", "general")
        responsive = arguments.get("responsive", True)
        
        suggestions = []
        
        # Analyze description for design intent
        if "center" in description or "centered" in description:
            suggestions.extend(["flex", "items-center", "justify-center"])
        
        if "shadow" in description or "elevated" in description:
            suggestions.extend(["shadow-md", "shadow-lg"])
        
        if "rounded" in description or "circle" in description:
            suggestions.extend(["rounded", "rounded-lg"])
        
        # Color suggestions
        if "blue" in description:
            suggestions.extend(["bg-blue-500", "text-blue-600", "border-blue-500"])
        elif "red" in description:
            suggestions.extend(["bg-red-500", "text-red-600", "border-red-500"])
        elif "green" in description:
            suggestions.extend(["bg-green-500", "text-green-600", "border-green-500"])
        
        # Size suggestions
        if "large" in description or "big" in description:
            suggestions.extend(["text-lg", "p-6"])
        elif "small" in description:
            suggestions.extend(["text-sm", "p-2"])
        else:
            suggestions.extend(["text-base", "p-4"])
        
        # Element-specific suggestions
        if element_type == "button":
            suggestions.extend([
                "inline-flex", "items-center", "px-4", "py-2",
                "border", "border-transparent", "font-medium",
                "rounded-md", "focus:outline-none", "focus:ring-2"
            ])
        elif element_type == "card":
            suggestions.extend([
                "bg-white", "overflow-hidden", "shadow", "rounded-lg",
                "border", "border-gray-200", "p-6"
            ])
        elif element_type == "form":
            suggestions.extend([
                "space-y-4", "p-6", "bg-white", "rounded-lg", "shadow"
            ])
        
        # Remove duplicates
        unique_suggestions = list(dict.fromkeys(suggestions))
        
        # Add responsive variants if requested
        responsive_examples = []
        if responsive and unique_suggestions:
            for suggestion in unique_suggestions[:3]:
                responsive_examples.extend([f"sm:{suggestion}", f"md:{suggestion}"])
        
        result = f"""
# Tailwind CSS Class Suggestions

**Design Description:** {description}
**Element Type:** {element_type}

## Core Classes
```css
{" ".join(unique_suggestions[:10])}
```

## Complete Class List
{chr(10).join(f"- `{cls}`" for cls in unique_suggestions)}

## Responsive Examples
{chr(10).join(f"- `{cls}`" for cls in responsive_examples[:6]) if responsive_examples else "Add responsive prefixes: sm:, md:, lg:, xl:"}

## Usage Example
```html
<{element_type} class="{" ".join(unique_suggestions[:8])}">
  Content here
</{element_type}>
```

## Alternative Combinations
- **Minimal**: {" ".join(unique_suggestions[:4])}
- **Enhanced**: {" ".join(unique_suggestions[:8])}
"""
        
        return [types.TextContent(type="text", text=result)]
    
    elif name == "package_analyzer":
        package_json_str = arguments.get("package_json", "{}")
        analysis_type = arguments.get("analysis_type", "all")
        
        try:
            package_data = json.loads(package_json_str)
            dependencies = package_data.get("dependencies", {})
            dev_dependencies = package_data.get("devDependencies", {})
            
            result = f"""
# Package Analysis Report

## Dependencies Overview
- **Runtime dependencies**: {len(dependencies)}
- **Development dependencies**: {len(dev_dependencies)}

## Frontend-Specific Packages Detected
"""
            
            frontend_packages = {
                "react": "React framework",
                "react-dom": "React DOM renderer",
                "next": "Next.js framework",
                "vue": "Vue.js framework",
                "angular": "Angular framework",
                "typescript": "TypeScript compiler",
                "tailwindcss": "Tailwind CSS framework",
                "styled-components": "CSS-in-JS library",
                "react-router": "React routing",
                "react-router-dom": "React routing for web",
                "axios": "HTTP client",
                "lodash": "Utility library",
                "@types/react": "React TypeScript definitions"
            }
            
            found_packages = []
            for pkg, desc in frontend_packages.items():
                if pkg in dependencies:
                    found_packages.append(f"- **{pkg}** ({dependencies[pkg]}): {desc} [Runtime]")
                elif pkg in dev_dependencies:
                    found_packages.append(f"- **{pkg}** ({dev_dependencies[pkg]}): {desc} [Development]")
            
            if found_packages:
                result += "\n".join(found_packages)
            else:
                result += "No common frontend packages detected."
            
            # Add recommendations
            result += f"""

## Recommendations
- Keep React ecosystem packages in sync
- Consider using TypeScript for better development experience
- Use Tailwind CSS for rapid UI development
- Add testing libraries like Jest and React Testing Library
- Consider adding ESLint and Prettier for code quality

## Package Health
- Total packages: {len(dependencies) + len(dev_dependencies)}
- Consider auditing for vulnerabilities: `npm audit` or `yarn audit`
"""
            
            return [types.TextContent(type="text", text=result)]
            
        except json.JSONDecodeError:
            return [types.TextContent(type="text", text="Error: Invalid package.json format")]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Error analyzing package.json: {str(e)}")]
    
    elif name == "react_hook_generator":
        hook_name = arguments.get("hook_name", "")
        functionality = arguments.get("functionality", "")
        
        # Ensure hook name starts with 'use'
        if hook_name and not hook_name.startswith("use"):
            hook_name = f"use{hook_name.capitalize()}"
        
        hook_code = f"""
import {{ useState, useEffect, useCallback }} from 'react';

/**
 * Custom hook: {hook_name}
 * {functionality}
 */
export const {hook_name} = () => {{
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {{
    // Initialize hook logic here
    // TODO: Implement {functionality.lower()}
  }}, []);

  const execute = useCallback(async () => {{
    try {{
      setLoading(true);
      setError(null);
      
      // TODO: Implement main functionality
      // {functionality}
      
      setLoading(false);
    }} catch (err) {{
      setError(err instanceof Error ? err.message : 'An error occurred');
      setLoading(false);
    }}
  }}, []);

  const reset = useCallback(() => {{
    setData(null);
    setError(null);
    setLoading(false);
  }}, []);

  return {{
    data,
    loading,
    error,
    execute,
    reset
  }};
}};

// Usage example:
// const {{ data, loading, error, execute, reset }} = {hook_name}();
"""
        
        return [types.TextContent(type="text", text=hook_code.strip())]
    
    # Handle React Flow tools
    elif name in ["react_flow_diagram_generator", "react_flow_custom_node_generator", 
                  "react_flow_edge_analyzer", "react_flow_layout_optimizer",
                  "react_flow_hierarchical_tree_generator", "react_flow_elk_layout_generator"]:
        return await react_flow_tools.handle_call(name, arguments)
    
    # Handle React Flow API tools
    elif name in ["react_flow_hook_examples", "react_flow_advanced_components",
                  "react_flow_utilities_generator", "react_flow_typescript_definitions", 
                  "react_flow_performance_optimizer", "react_flow_accessibility_enhancer"]:
        handler_func = react_flow_api_tools.REACT_FLOW_API_HANDLERS.get(name)
        if handler_func:
            return handler_func(arguments or {})
        else:
            return [types.TextContent(type="text", text=f"Handler not found for {name}")]
    
    # Handle React Flow Learning tools  
    elif name in ["react_flow_layouting_expert", "react_flow_performance_mastery",
                  "react_flow_tutorial_generator", "react_flow_troubleshooting_expert",
                  "react_flow_accessibility_expert", "react_flow_devtools_mastery"]:
        handler_func = react_flow_learning_tools.REACT_FLOW_LEARNING_HANDLERS.get(name)
        if handler_func:
            return handler_func(arguments or {})
        else:
            return [types.TextContent(type="text", text=f"Learning handler not found for {name}")]
    
    # Handle Connection Positioning tools
    elif name in ["generate_connection_aware_node", "codex_positioning_prompts",
                  "dagre_configuration_optimizer", "handle_positioning_guide", 
                  "whiteboard_layout_optimizer"]:
        return await connection_positioning_tools.handle_call(name, arguments or {})
    
    
    else:
        return [types.TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream, 
            write_stream, 
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())