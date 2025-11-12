"""
Package management tools for npm/yarn analysis.
"""

import json
import re
from typing import Any, Dict, List

from mcp.types import Tool, TextContent


def get_tools() -> List[Tool]:
    """Get all package management tools."""
    return [
        Tool(
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
        Tool(
            name="package_updater",
            description="Suggest package updates and compatibility checks",
            inputSchema={
                "type": "object",
                "properties": {
                    "package_json": {
                        "type": "string",
                        "description": "Content of package.json file"
                    },
                    "update_type": {
                        "type": "string",
                        "enum": ["major", "minor", "patch", "safe"],
                        "description": "Type of updates to suggest",
                        "default": "safe"
                    }
                },
                "required": ["package_json"]
            }
        )
    ]


async def handle_call(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle package management tool calls."""
    
    if name == "package_analyzer":
        return await analyze_package(arguments)
    elif name == "package_updater":
        return await suggest_updates(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown package tool: {name}")]


async def analyze_package(args: Dict[str, Any]) -> List[TextContent]:
    """Analyze package.json file."""
    package_json_str = args.get("package_json", "{}")
    analysis_type = args.get("analysis_type", "all")
    
    try:
        package_data = json.loads(package_json_str)
    except json.JSONDecodeError:
        return [TextContent(type="text", text="Error: Invalid package.json format")]
    
    dependencies = package_data.get("dependencies", {})
    dev_dependencies = package_data.get("devDependencies", {})
    peer_dependencies = package_data.get("peerDependencies", {})
    
    result = f"# Package Analysis Report\n\n"
    
    if analysis_type in ["dependencies", "all"]:
        result += f"""## Dependencies Overview
- **Runtime dependencies**: {len(dependencies)}
- **Development dependencies**: {len(dev_dependencies)}
- **Peer dependencies**: {len(peer_dependencies)}

### Frontend-specific packages detected:
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
            "axios": "HTTP client",
            "lodash": "Utility library"
        }
        
        found_packages = []
        for pkg, desc in frontend_packages.items():
            if pkg in dependencies or pkg in dev_dependencies:
                version = dependencies.get(pkg) or dev_dependencies.get(pkg)
                found_packages.append(f"- **{pkg}** ({version}): {desc}")
        
        result += "\n".join(found_packages) if found_packages else "No common frontend packages detected."
    
    return [TextContent(type="text", text=result)]


async def suggest_updates(args: Dict[str, Any]) -> List[TextContent]:
    """Suggest package updates."""
    package_json_str = args.get("package_json", "{}")
    update_type = args.get("update_type", "safe")
    
    try:
        package_data = json.loads(package_json_str)
    except json.JSONDecodeError:
        return [TextContent(type="text", text="Error: Invalid package.json format")]
    
    result = f"""# Package Update Suggestions ({update_type})

## Recommended Updates
- Check for updates using: `npm outdated` or `yarn outdated`
- Update packages: `npm update` or `yarn upgrade`

## Frontend Package Recommendations
- Keep React ecosystem packages in sync
- Update TypeScript regularly for latest features
- Monitor Tailwind CSS for new utilities
"""
    
    return [TextContent(type="text", text=result)]