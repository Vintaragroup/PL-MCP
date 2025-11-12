"""
React Native tools for the MCP server.
"""

from typing import Any, Dict, List

from mcp.types import Tool, TextContent


def get_tools() -> List[Tool]:
    """Get all React Native-related tools."""
    return [
        Tool(
            name="react_native_component_generator",
            description="Generate React Native components with platform-specific optimizations",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_name": {
                        "type": "string",
                        "description": "Name of the React Native component"
                    },
                    "platform": {
                        "type": "string",
                        "enum": ["ios", "android", "both"],
                        "description": "Target platform",
                        "default": "both"
                    }
                },
                "required": ["component_name"]
            }
        )
    ]


async def handle_call(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle React Native tool calls."""
    
    if name == "react_native_component_generator":
        return await generate_rn_component(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown React Native tool: {name}")]


async def generate_rn_component(args: Dict[str, Any]) -> List[TextContent]:
    """Generate React Native component."""
    component_name = args.get("component_name", "MyComponent")
    platform = args.get("platform", "both")
    
    result = f"""
# React Native Component: {component_name}

```typescript
import React from 'react';
import {{ View, Text, StyleSheet }} from 'react-native';

interface {component_name}Props {{
  title?: string;
}}

export const {component_name}: React.FC<{component_name}Props> = ({{ title = 'Hello' }}) => {{
  return (
    <View style={{styles.container}}>
      <Text style={{styles.title}}>{{title}}</Text>
    </View>
  );
}};

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  }},
  title: {{
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  }},
}});

export default {component_name};
```

Platform: {platform}
"""
    
    return [TextContent(type="text", text=result)]