"""
React development tools for the MCP server.
"""

import json
import re
from typing import Any, Dict, List

from mcp.types import Tool, TextContent


def get_tools() -> List[Tool]:
    """Get all React-related tools."""
    return [
        Tool(
            name="react_component_analysis",
            description="Analyze React components for best practices, performance issues, and potential improvements",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_code": {
                        "type": "string",
                        "description": "The React component code to analyze"
                    },
                    "analysis_type": {
                        "type": "string",
                        "enum": ["performance", "accessibility", "best_practices", "all"],
                        "description": "Type of analysis to perform",
                        "default": "all"
                    }
                },
                "required": ["component_code"]
            }
        ),
        Tool(
            name="react_hook_generator",
            description="Generate custom React hooks based on requirements",
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
                    },
                    "dependencies": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "React hooks or external dependencies to use"
                    }
                },
                "required": ["hook_name", "functionality"]
            }
        ),
        Tool(
            name="react_component_generator",
            description="Generate React components with TypeScript, props interface, and styling",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_name": {
                        "type": "string",
                        "description": "Name of the React component"
                    },
                    "component_type": {
                        "type": "string",
                        "enum": ["functional", "class"],
                        "description": "Type of component to generate",
                        "default": "functional"
                    },
                    "props": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "type": {"type": "string"},
                                "optional": {"type": "boolean", "default": False},
                                "description": {"type": "string"}
                            },
                            "required": ["name", "type"]
                        },
                        "description": "Component props definition"
                    },
                    "styling": {
                        "type": "string",
                        "enum": ["css-modules", "styled-components", "tailwind", "none"],
                        "description": "Styling approach",
                        "default": "tailwind"
                    },
                    "functionality": {
                        "type": "string",
                        "description": "Description of component functionality"
                    }
                },
                "required": ["component_name"]
            }
        ),
        Tool(
            name="react_performance_optimizer",
            description="Suggest performance optimizations for React components",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_code": {
                        "type": "string",
                        "description": "React component code to optimize"
                    },
                    "optimization_focus": {
                        "type": "string",
                        "enum": ["rendering", "memory", "bundle_size", "all"],
                        "description": "Focus area for optimization",
                        "default": "all"
                    }
                },
                "required": ["component_code"]
            }
        ),
        Tool(
            name="react_testing_generator",
            description="Generate unit tests for React components using Jest and React Testing Library",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_code": {
                        "type": "string",
                        "description": "React component code to test"
                    },
                    "test_type": {
                        "type": "string",
                        "enum": ["unit", "integration", "snapshot"],
                        "description": "Type of tests to generate",
                        "default": "unit"
                    },
                    "coverage_level": {
                        "type": "string",
                        "enum": ["basic", "comprehensive"],
                        "description": "Level of test coverage",
                        "default": "comprehensive"
                    }
                },
                "required": ["component_code"]
            }
        )
    ]


async def handle_call(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle React tool calls."""
    
    if name == "react_component_analysis":
        return await analyze_component(arguments)
    elif name == "react_hook_generator":
        return await generate_hook(arguments)
    elif name == "react_component_generator":
        return await generate_component(arguments)
    elif name == "react_performance_optimizer":
        return await optimize_performance(arguments)
    elif name == "react_testing_generator":
        return await generate_tests(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown React tool: {name}")]


async def analyze_component(args: Dict[str, Any]) -> List[TextContent]:
    """Analyze React component for best practices and issues."""
    component_code = args.get("component_code", "")
    analysis_type = args.get("analysis_type", "all")
    
    issues = []
    suggestions = []
    
    # Performance analysis
    if analysis_type in ["performance", "all"]:
        if "useEffect" in component_code and "[]" not in component_code:
            issues.append("⚠️ useEffect without dependency array may cause infinite re-renders")
        
        if re.search(r'onClick=\{.*=>\s*.*\}', component_code):
            issues.append("⚠️ Inline arrow functions in onClick can cause unnecessary re-renders")
            suggestions.append("Consider using useCallback or defining functions outside render")
        
        if "console.log" in component_code:
            issues.append("⚠️ Console.log statements found - remove in production")
    
    # Accessibility analysis
    if analysis_type in ["accessibility", "all"]:
        if re.search(r'<img(?![^>]*alt=)', component_code):
            issues.append("♿ Images missing alt attributes for accessibility")
        
        if re.search(r'<button(?![^>]*aria-)', component_code) and "onClick" in component_code:
            suggestions.append("Consider adding aria-label or aria-describedby to buttons")
    
    # Best practices analysis
    if analysis_type in ["best_practices", "all"]:
        if "any" in component_code:
            issues.append("🔧 Avoid using 'any' type - use specific types for better type safety")
        
        if not re.search(r'interface\s+\w+Props', component_code) and "props" in component_code:
            suggestions.append("Define a Props interface for better type safety")
        
        if "useState" in component_code and not "React.useState" in component_code and "import" not in component_code:
            suggestions.append("Consider importing React hooks explicitly or using React.useState")
    
    analysis_result = f"""
## Component Analysis Results

### Issues Found ({len(issues)})
{chr(10).join(f"- {issue}" for issue in issues) if issues else "✅ No issues found!"}

### Suggestions ({len(suggestions)})
{chr(10).join(f"- {suggestion}" for suggestion in suggestions) if suggestions else "✅ No additional suggestions!"}

### Code Quality Score
{max(0, 100 - len(issues) * 10 - len(suggestions) * 5)}/100
"""
    
    return [TextContent(type="text", text=analysis_result)]


async def generate_hook(args: Dict[str, Any]) -> List[TextContent]:
    """Generate a custom React hook."""
    hook_name = args.get("hook_name", "")
    functionality = args.get("functionality", "")
    dependencies = args.get("dependencies", [])
    
    # Ensure hook name starts with 'use'
    if not hook_name.startswith("use"):
        hook_name = f"use{hook_name.capitalize()}"
    
    # Generate basic hook structure
    imports = ["import { useState, useEffect, useCallback } from 'react';"]
    
    # Add specific imports based on dependencies
    if "axios" in dependencies:
        imports.append("import axios from 'axios';")
    if "debounce" in dependencies:
        imports.append("import { debounce } from 'lodash';")
    
    hook_code = f"""
{chr(10).join(imports)}

/**
 * Custom hook: {hook_name}
 * {functionality}
 */
export const {hook_name} = () => {{
  const [state, setState] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {{
    // TODO: Implement {functionality.lower()}
    // Initialize hook logic here
  }}, []);

  const execute = useCallback(async () => {{
    try {{
      setLoading(true);
      setError(null);
      
      // TODO: Implement main functionality
      // {functionality}
      
      setLoading(false);
    }} catch (err) {{
      setError(err);
      setLoading(false);
    }}
  }}, []);

  return {{
    state,
    loading,
    error,
    execute,
  }};
}};

// Usage example:
// const {{ state, loading, error, execute }} = {hook_name}();
"""
    
    return [TextContent(type="text", text=hook_code.strip())]


async def generate_component(args: Dict[str, Any]) -> List[TextContent]:
    """Generate a React component with TypeScript."""
    component_name = args.get("component_name", "MyComponent")
    component_type = args.get("component_type", "functional")
    props = args.get("props", [])
    styling = args.get("styling", "tailwind")
    functionality = args.get("functionality", "")
    
    # Generate props interface
    props_interface = ""
    if props:
        props_interface = f"""
interface {component_name}Props {{
{chr(10).join(f"  {prop['name']}{'' if not prop.get('optional', False) else '?'}: {prop['type']}; // {prop.get('description', '')}" for prop in props)}
}}
"""
    
    # Generate styling imports
    style_imports = ""
    if styling == "styled-components":
        style_imports = "import styled from 'styled-components';"
    elif styling == "css-modules":
        style_imports = f"import styles from './{component_name}.module.css';"
    
    # Generate component
    if component_type == "functional":
        component_code = f"""
import React from 'react';
{style_imports}
{props_interface}
/**
 * {component_name} Component
 * {functionality}
 */
export const {component_name}: React.FC<{component_name}Props> = ({{
{chr(10).join(f"  {prop['name']}," for prop in props)}
}}) => {{
  return (
    <div className="{"p-4" if styling == "tailwind" else ""}">
      <h2 className="{"text-xl font-bold" if styling == "tailwind" else ""}">{component_name}</h2>
      {chr(10).join(f"      <p>{{{prop['name']}}}</p>" for prop in props if prop['type'] in ['string', 'number'])}
      {{/* TODO: Implement {functionality} */}}
    </div>
  );
}};

export default {component_name};
"""
    else:  # class component
        component_code = f"""
import React, {{ Component }} from 'react';
{style_imports}
{props_interface}
interface {component_name}State {{
  // Define component state here
}}

/**
 * {component_name} Component
 * {functionality}
 */
export class {component_name} extends Component<{component_name}Props, {component_name}State> {{
  constructor(props: {component_name}Props) {{
    super(props);
    this.state = {{
      // Initialize state
    }};
  }}

  render() {{
    return (
      <div className="{"p-4" if styling == "tailwind" else ""}">
        <h2 className="{"text-xl font-bold" if styling == "tailwind" else ""}">{component_name}</h2>
        {chr(10).join(f"        <p>{{this.props.{prop['name']}}}</p>" for prop in props if prop['type'] in ['string', 'number'])}
        {{/* TODO: Implement {functionality} */}}
      </div>
    );
  }}
}}

export default {component_name};
"""
    
    return [TextContent(type="text", text=component_code.strip())]


async def optimize_performance(args: Dict[str, Any]) -> List[TextContent]:
    """Suggest performance optimizations."""
    component_code = args.get("component_code", "")
    focus = args.get("optimization_focus", "all")
    
    optimizations = []
    
    # Rendering optimizations
    if focus in ["rendering", "all"]:
        if "useEffect" in component_code:
            optimizations.append({
                "category": "Rendering",
                "issue": "UseEffect optimization",
                "suggestion": "Ensure useEffect has proper dependency arrays to prevent unnecessary re-renders",
                "code": """
// ❌ Bad
useEffect(() => {
  fetchData();
}); // Missing dependency array

// ✅ Good
useEffect(() => {
  fetchData();
}, [dependency1, dependency2]);
"""
            })
        
        if re.search(r'onClick=\{.*=>\s*.*\}', component_code):
            optimizations.append({
                "category": "Rendering",
                "issue": "Inline functions causing re-renders",
                "suggestion": "Use useCallback to memoize event handlers",
                "code": """
// ❌ Bad
<button onClick={() => handleClick(id)}>Click</button>

// ✅ Good
const handleClick = useCallback((id) => {
  // handle click logic
}, [dependency]);

<button onClick={() => handleClick(id)}>Click</button>
"""
            })
    
    # Memory optimizations
    if focus in ["memory", "all"]:
        if "useState" in component_code:
            optimizations.append({
                "category": "Memory",
                "issue": "State management",
                "suggestion": "Consider using useMemo for expensive calculations",
                "code": """
// ❌ Expensive calculation on every render
const expensiveValue = calculateExpensiveValue(data);

// ✅ Memoized calculation
const expensiveValue = useMemo(() => 
  calculateExpensiveValue(data), [data]
);
"""
            })
    
    # Bundle size optimizations
    if focus in ["bundle_size", "all"]:
        optimizations.append({
            "category": "Bundle Size",
            "issue": "Import optimization",
            "suggestion": "Use tree shaking with named imports",
            "code": """
// ❌ Imports entire library
import * as lodash from 'lodash';

// ✅ Tree-shakable import
import { debounce, throttle } from 'lodash';
"""
        })
    
    result = "# React Performance Optimization Suggestions\n\n"
    
    for opt in optimizations:
        result += f"""
## {opt['category']}: {opt['issue']}

**Suggestion:** {opt['suggestion']}

```typescript
{opt['code']}
```

---
"""
    
    if not optimizations:
        result += "✅ No obvious performance issues detected in the provided code!"
    
    return [TextContent(type="text", text=result)]


async def generate_tests(args: Dict[str, Any]) -> List[TextContent]:
    """Generate tests for React components."""
    component_code = args.get("component_code", "")
    test_type = args.get("test_type", "unit")
    coverage_level = args.get("coverage_level", "comprehensive")
    
    # Extract component name from code
    component_name = "Component"
    name_match = re.search(r'(?:export\s+(?:const|function)\s+|class\s+)(\w+)', component_code)
    if name_match:
        component_name = name_match.group(1)
    
    test_code = f"""
import React from 'react';
import {{ render, screen, fireEvent, waitFor }} from '@testing-library/react';
import {{ jest }} from '@jest/globals';
import {component_name} from './{component_name}';

describe('{component_name}', () => {{
  // Basic rendering test
  test('renders without crashing', () => {{
    render(<{component_name} />);
    expect(screen.getByRole('main') || screen.getByText(/{component_name}/i)).toBeInTheDocument();
  }});

  // Props testing
  test('renders with props correctly', () => {{
    const testProps = {{
      // Add test props based on component interface
    }};
    
    render(<{component_name} {{...testProps}} />);
    // Add assertions based on expected rendering
  }});
"""
    
    if coverage_level == "comprehensive":
        test_code += f"""
  // Event handling tests
  test('handles user interactions', async () => {{
    const mockHandler = jest.fn();
    
    render(<{component_name} onClick={{mockHandler}} />);
    
    const clickableElement = screen.getByRole('button') || screen.getByText(/click/i);
    fireEvent.click(clickableElement);
    
    expect(mockHandler).toHaveBeenCalledTimes(1);
  }});

  // Async behavior tests
  test('handles async operations', async () => {{
    render(<{component_name} />);
    
    // Wait for async operations to complete
    await waitFor(() => {{
      expect(screen.queryByText(/loading/i)).not.toBeInTheDocument();
    }});
  }});

  // Error boundary tests
  test('handles errors gracefully', () => {{
    const consoleError = jest.spyOn(console, 'error').mockImplementation(() => {{}});
    
    // Test error scenarios
    
    consoleError.mockRestore();
  }});
"""
    
    if test_type in ["integration", "snapshot"]:
        test_code += f"""
  // Snapshot test
  test('matches snapshot', () => {{
    const {{ container }} = render(<{component_name} />);
    expect(container.firstChild).toMatchSnapshot();
  }});
"""
    
    test_code += """
});

// Test utilities and helpers
const renderWithProviders = (component: React.ReactElement) => {
  // Add providers (Router, Theme, etc.) if needed
  return render(component);
};
"""
    
    return [TextContent(type="text", text=test_code)]