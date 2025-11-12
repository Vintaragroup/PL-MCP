"""
Tailwind CSS tools for the MCP server.
"""

import json
import re
from typing import Any, Dict, List

from mcp.types import Tool, TextContent


# Comprehensive Tailwind CSS class mappings
TAILWIND_CLASSES = {
    "spacing": {
        "p": ["p-0", "p-1", "p-2", "p-3", "p-4", "p-5", "p-6", "p-8", "p-10", "p-12", "p-16", "p-20", "p-24"],
        "m": ["m-0", "m-1", "m-2", "m-3", "m-4", "m-5", "m-6", "m-8", "m-10", "m-12", "m-16", "m-20", "m-24"],
        "px": ["px-0", "px-1", "px-2", "px-3", "px-4", "px-5", "px-6", "px-8"],
        "py": ["py-0", "py-1", "py-2", "py-3", "py-4", "py-5", "py-6", "py-8"],
    },
    "colors": {
        "bg": ["bg-white", "bg-black", "bg-gray-100", "bg-gray-200", "bg-gray-300", "bg-blue-500", "bg-green-500", "bg-red-500"],
        "text": ["text-white", "text-black", "text-gray-600", "text-gray-800", "text-blue-600", "text-green-600", "text-red-600"],
        "border": ["border-gray-200", "border-gray-300", "border-blue-500", "border-green-500", "border-red-500"],
    },
    "layout": {
        "flex": ["flex", "flex-col", "flex-row", "flex-wrap", "flex-nowrap"],
        "grid": ["grid", "grid-cols-1", "grid-cols-2", "grid-cols-3", "grid-cols-4", "grid-cols-12"],
        "position": ["relative", "absolute", "fixed", "sticky"],
    },
    "typography": {
        "font": ["font-thin", "font-light", "font-normal", "font-medium", "font-semibold", "font-bold"],
        "text": ["text-xs", "text-sm", "text-base", "text-lg", "text-xl", "text-2xl", "text-3xl"],
        "align": ["text-left", "text-center", "text-right", "text-justify"],
    },
    "responsive": {
        "breakpoints": ["sm:", "md:", "lg:", "xl:", "2xl:"],
    }
}


def get_tools() -> List[Tool]:
    """Get all Tailwind CSS-related tools."""
    return [
        Tool(
            name="tailwind_class_suggester",
            description="Suggest appropriate Tailwind CSS classes based on design requirements",
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
        Tool(
            name="tailwind_component_builder",
            description="Build complete Tailwind CSS component markup with best practices",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_type": {
                        "type": "string",
                        "enum": ["button", "card", "modal", "form", "navigation", "hero", "grid", "table"],
                        "description": "Type of component to build"
                    },
                    "style_variant": {
                        "type": "string",
                        "enum": ["primary", "secondary", "outline", "ghost", "minimal"],
                        "description": "Style variant for the component",
                        "default": "primary"
                    },
                    "size": {
                        "type": "string",
                        "enum": ["xs", "sm", "md", "lg", "xl"],
                        "description": "Size variant",
                        "default": "md"
                    },
                    "color_scheme": {
                        "type": "string",
                        "enum": ["blue", "green", "red", "purple", "gray", "indigo"],
                        "description": "Color scheme to use",
                        "default": "blue"
                    }
                },
                "required": ["component_type"]
            }
        ),
        Tool(
            name="tailwind_responsive_generator",
            description="Generate responsive design patterns using Tailwind CSS",
            inputSchema={
                "type": "object",
                "properties": {
                    "layout_type": {
                        "type": "string",
                        "enum": ["grid", "flex", "stack", "sidebar"],
                        "description": "Type of responsive layout"
                    },
                    "breakpoints": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["sm", "md", "lg", "xl", "2xl"]
                        },
                        "description": "Breakpoints to target"
                    },
                    "mobile_first": {
                        "type": "boolean",
                        "description": "Use mobile-first approach",
                        "default": True
                    }
                },
                "required": ["layout_type"]
            }
        ),
        Tool(
            name="tailwind_optimizer",
            description="Optimize Tailwind CSS usage and suggest improvements",
            inputSchema={
                "type": "object",
                "properties": {
                    "html_content": {
                        "type": "string",
                        "description": "HTML content with Tailwind classes to optimize"
                    },
                    "optimization_type": {
                        "type": "string",
                        "enum": ["duplicate_removal", "class_ordering", "responsive_optimization", "all"],
                        "description": "Type of optimization to perform",
                        "default": "all"
                    }
                },
                "required": ["html_content"]
            }
        ),
        Tool(
            name="tailwind_color_palette",
            description="Generate comprehensive color palettes and usage patterns",
            inputSchema={
                "type": "object",
                "properties": {
                    "primary_color": {
                        "type": "string",
                        "description": "Primary color name or hex code"
                    },
                    "palette_type": {
                        "type": "string",
                        "enum": ["monochromatic", "complementary", "triadic", "analogous"],
                        "description": "Type of color palette to generate",
                        "default": "monochromatic"
                    },
                    "include_usage": {
                        "type": "boolean",
                        "description": "Include usage examples for each color",
                        "default": True
                    }
                },
                "required": ["primary_color"]
            }
        )
    ]


async def handle_call(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle Tailwind CSS tool calls."""
    
    if name == "tailwind_class_suggester":
        return await suggest_classes(arguments)
    elif name == "tailwind_component_builder":
        return await build_component(arguments)
    elif name == "tailwind_responsive_generator":
        return await generate_responsive(arguments)
    elif name == "tailwind_optimizer":
        return await optimize_tailwind(arguments)
    elif name == "tailwind_color_palette":
        return await generate_color_palette(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown Tailwind tool: {name}")]


async def suggest_classes(args: Dict[str, Any]) -> List[TextContent]:
    """Suggest Tailwind CSS classes based on design requirements."""
    description = args.get("design_description", "").lower()
    element_type = args.get("element_type", "general")
    responsive = args.get("responsive", True)
    
    suggestions = []
    
    # Analyze description for design intent
    if "center" in description or "centered" in description:
        suggestions.extend(["flex", "items-center", "justify-center"])
    
    if "shadow" in description or "elevated" in description:
        suggestions.extend(["shadow-md", "shadow-lg", "drop-shadow"])
    
    if "rounded" in description or "circle" in description:
        suggestions.extend(["rounded", "rounded-lg", "rounded-full"])
    
    if "blue" in description:
        suggestions.extend(["bg-blue-500", "text-blue-600", "border-blue-500"])
    elif "red" in description:
        suggestions.extend(["bg-red-500", "text-red-600", "border-red-500"])
    elif "green" in description:
        suggestions.extend(["bg-green-500", "text-green-600", "border-green-500"])
    
    if "large" in description or "big" in description:
        suggestions.extend(["text-lg", "text-xl", "p-6", "p-8"])
    elif "small" in description:
        suggestions.extend(["text-sm", "text-xs", "p-2", "p-3"])
    
    # Element-specific suggestions
    if element_type == "button":
        suggestions.extend([
            "inline-flex", "items-center", "px-4", "py-2",
            "border", "border-transparent", "text-sm", "font-medium",
            "rounded-md", "shadow-sm", "focus:outline-none", "focus:ring-2"
        ])
    elif element_type == "card":
        suggestions.extend([
            "bg-white", "overflow-hidden", "shadow", "rounded-lg",
            "border", "border-gray-200", "p-6"
        ])
    elif element_type == "form":
        suggestions.extend([
            "space-y-4", "p-6", "bg-white", "rounded-lg",
            "shadow", "border", "border-gray-200"
        ])
    
    # Add responsive variants if requested
    if responsive and suggestions:
        responsive_suggestions = []
        for suggestion in suggestions[:5]:  # Limit to first 5 for responsive
            responsive_suggestions.extend([
                f"sm:{suggestion}",
                f"md:{suggestion}",
                f"lg:{suggestion}"
            ])
        suggestions.extend(responsive_suggestions)
    
    # Remove duplicates and format
    unique_suggestions = list(dict.fromkeys(suggestions))
    
    result = f"""
# Tailwind CSS Class Suggestions

**Design Description:** {description}
**Element Type:** {element_type}

## Recommended Classes

### Core Classes
```css
{" ".join(unique_suggestions[:10])}
```

### Complete Class List
{chr(10).join(f"- `{cls}`" for cls in unique_suggestions)}

## Usage Example
```html
<div class="{" ".join(unique_suggestions[:8])}">
  <!-- Your {element_type} content -->
</div>
```

## Alternative Combinations
```css
/* Minimal variant */
{" ".join(unique_suggestions[:5])}

/* Enhanced variant */
{" ".join(unique_suggestions[:12])}
```
"""
    
    return [TextContent(type="text", text=result)]


async def build_component(args: Dict[str, Any]) -> List[TextContent]:
    """Build complete Tailwind CSS component markup."""
    component_type = args.get("component_type", "button")
    style_variant = args.get("style_variant", "primary")
    size = args.get("size", "md")
    color_scheme = args.get("color_scheme", "blue")
    
    components = {
        "button": {
            "primary": {
                "xs": f"inline-flex items-center px-2 py-1 border border-transparent text-xs font-medium rounded text-white bg-{color_scheme}-600 hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500",
                "sm": f"inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-{color_scheme}-600 hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500",
                "md": f"inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-{color_scheme}-600 hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500",
                "lg": f"inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-{color_scheme}-600 hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500",
                "xl": f"inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-{color_scheme}-600 hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500"
            },
            "secondary": {
                "md": f"inline-flex items-center px-4 py-2 border border-{color_scheme}-300 text-sm font-medium rounded-md text-{color_scheme}-700 bg-white hover:bg-{color_scheme}-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500"
            }
        },
        "card": {
            "primary": {
                "md": f"bg-white overflow-hidden shadow rounded-lg border border-gray-200 p-6"
            }
        },
        "modal": {
            "primary": {
                "md": "fixed inset-0 z-50 overflow-y-auto" +
                      f" bg-white rounded-lg shadow-xl transform transition-all sm:max-w-lg sm:w-full sm:mx-auto sm:my-8"
            }
        }
    }
    
    # Get the component classes
    classes = components.get(component_type, {}).get(style_variant, {}).get(size, 
                            f"p-4 bg-{color_scheme}-500 text-white rounded")
    
    # Generate component markup
    if component_type == "button":
        markup = f'''<button type="button" class="{classes}">
  Button Text
</button>'''
    elif component_type == "card":
        markup = f'''<div class="{classes}">
  <div class="px-4 py-5 sm:p-6">
    <h3 class="text-lg leading-6 font-medium text-gray-900">Card Title</h3>
    <div class="mt-2 max-w-xl text-sm text-gray-500">
      <p>Card description goes here.</p>
    </div>
    <div class="mt-5">
      <button type="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-{color_scheme}-600 hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500">
        Action
      </button>
    </div>
  </div>
</div>'''
    elif component_type == "modal":
        markup = f'''<div class="fixed inset-0 z-50 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
    <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
    <div class="{classes}">
      <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
        <div class="sm:flex sm:items-start">
          <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
              Modal Title
            </h3>
            <div class="mt-2">
              <p class="text-sm text-gray-500">
                Modal content goes here.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
        <button type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-{color_scheme}-600 text-base font-medium text-white hover:bg-{color_scheme}-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color_scheme}-500 sm:ml-3 sm:w-auto sm:text-sm">
          Confirm
        </button>
        <button type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
          Cancel
        </button>
      </div>
    </div>
  </div>
</div>'''
    else:
        markup = f'<div class="{classes}">Component content</div>'
    
    result = f"""
# {component_type.title()} Component - {style_variant.title()} ({size.upper()})

## Generated Markup
```html
{markup}
```

## Class Breakdown
```css
{classes}
```

## Variants

### Size Variants
- **xs**: Extra small
- **sm**: Small  
- **md**: Medium (default)
- **lg**: Large
- **xl**: Extra large

### Style Variants
- **primary**: Filled background
- **secondary**: Outlined style
- **outline**: Border only
- **ghost**: Minimal styling

### Usage in React
```jsx
const {component_type.title()}Component = () => {{
  return (
    {markup.replace('class=', 'className=')}
  );
}};
```
"""
    
    return [TextContent(type="text", text=result)]


async def generate_responsive(args: Dict[str, Any]) -> List[TextContent]:
    """Generate responsive design patterns."""
    layout_type = args.get("layout_type", "grid")
    breakpoints = args.get("breakpoints", ["sm", "md", "lg"])
    mobile_first = args.get("mobile_first", True)
    
    patterns = {
        "grid": {
            "mobile_first": "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4",
            "desktop_first": "grid grid-cols-4 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-1 gap-4"
        },
        "flex": {
            "mobile_first": "flex flex-col sm:flex-row items-center justify-between space-y-4 sm:space-y-0 sm:space-x-4",
            "desktop_first": "flex flex-row sm:flex-col items-center justify-between space-x-4 sm:space-x-0 sm:space-y-4"
        },
        "stack": {
            "mobile_first": "space-y-4 sm:space-y-6 md:space-y-8",
            "desktop_first": "space-y-8 md:space-y-6 sm:space-y-4"
        },
        "sidebar": {
            "mobile_first": "flex flex-col lg:flex-row min-h-screen",
            "desktop_first": "flex flex-row lg:flex-col min-h-screen"
        }
    }
    
    approach = "mobile_first" if mobile_first else "desktop_first"
    classes = patterns.get(layout_type, {}).get(approach, "")
    
    # Generate examples for each breakpoint
    examples = []
    for bp in breakpoints:
        if layout_type == "grid":
            examples.append(f"**{bp.upper()}**: {bp}:grid-cols-2 (2 columns)")
        elif layout_type == "flex":
            examples.append(f"**{bp.upper()}**: {bp}:flex-row (horizontal layout)")
    
    markup_examples = {
        "grid": f'''<div class="{classes}">
  <div class="bg-white p-4 rounded-lg shadow">Item 1</div>
  <div class="bg-white p-4 rounded-lg shadow">Item 2</div>
  <div class="bg-white p-4 rounded-lg shadow">Item 3</div>
  <div class="bg-white p-4 rounded-lg shadow">Item 4</div>
</div>''',
        "flex": f'''<div class="{classes}">
  <div class="flex-1">
    <h2 class="text-xl font-bold">Main Content</h2>
    <p>Content goes here</p>
  </div>
  <div class="w-full sm:w-auto">
    <button class="w-full sm:w-auto px-4 py-2 bg-blue-600 text-white rounded">
      Action
    </button>
  </div>
</div>''',
        "sidebar": f'''<div class="{classes}">
  <aside class="w-full lg:w-64 bg-gray-100 p-4">
    <nav>Sidebar Navigation</nav>
  </aside>
  <main class="flex-1 p-4">
    <h1 class="text-2xl font-bold mb-4">Main Content</h1>
    <p>Page content goes here</p>
  </main>
</div>'''
    }
    
    result = f"""
# Responsive {layout_type.title()} Layout

## Approach: {"Mobile-First" if mobile_first else "Desktop-First"}

## Generated Classes
```css
{classes}
```

## Breakpoint Behavior
{chr(10).join(examples)}

## Complete Example
```html
{markup_examples.get(layout_type, f'<div class="{classes}">Content</div>')}
```

## Breakpoint Reference
- **sm**: 640px and up
- **md**: 768px and up  
- **lg**: 1024px and up
- **xl**: 1280px and up
- **2xl**: 1536px and up

## Best Practices
1. Start with mobile design (mobile-first approach recommended)
2. Use logical breakpoints based on content, not device sizes
3. Test across different screen sizes
4. Consider touch targets on mobile (minimum 44px)
5. Ensure adequate spacing between interactive elements
"""
    
    return [TextContent(type="text", text=result)]


async def optimize_tailwind(args: Dict[str, Any]) -> List[TextContent]:
    """Optimize Tailwind CSS usage."""
    html_content = args.get("html_content", "")
    optimization_type = args.get("optimization_type", "all")
    
    optimizations = []
    
    # Extract all Tailwind classes
    class_pattern = r'class="([^"]*)"'
    classes_found = re.findall(class_pattern, html_content)
    all_classes = []
    
    for class_list in classes_found:
        all_classes.extend(class_list.split())
    
    # Remove duplicates
    unique_classes = list(dict.fromkeys(all_classes))
    
    if optimization_type in ["duplicate_removal", "all"]:
        duplicates = [cls for cls in unique_classes if all_classes.count(cls) > 1]
        if duplicates:
            optimizations.append({
                "type": "Duplicate Classes",
                "issue": f"Found {len(duplicates)} duplicate classes",
                "suggestion": "Consider extracting common class combinations into CSS components",
                "classes": duplicates[:10]  # Show first 10
            })
    
    if optimization_type in ["class_ordering", "all"]:
        # Suggest logical ordering
        optimizations.append({
            "type": "Class Ordering",
            "issue": "Classes could be better organized",
            "suggestion": "Follow this order: Layout → Spacing → Typography → Colors → Effects",
            "example": "flex items-center px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md shadow hover:bg-blue-700"
        })
    
    if optimization_type in ["responsive_optimization", "all"]:
        # Check for responsive classes
        responsive_classes = [cls for cls in unique_classes if any(bp in cls for bp in ["sm:", "md:", "lg:", "xl:", "2xl:"])]
        if responsive_classes:
            optimizations.append({
                "type": "Responsive Classes",
                "issue": f"Found {len(responsive_classes)} responsive classes",
                "suggestion": "Ensure mobile-first approach and logical breakpoint progression",
                "classes": responsive_classes[:5]
            })
    
    # Performance suggestions
    if len(unique_classes) > 50:
        optimizations.append({
            "type": "Performance",
            "issue": f"High number of utility classes ({len(unique_classes)})",
            "suggestion": "Consider using @apply directive for repeated patterns",
            "example": "@apply flex items-center px-4 py-2 text-white bg-blue-600 rounded;"
        })
    
    result = f"""
# Tailwind CSS Optimization Report

## Summary
- **Total classes found**: {len(all_classes)}
- **Unique classes**: {len(unique_classes)}
- **Potential optimizations**: {len(optimizations)}

## Optimizations
"""
    
    for opt in optimizations:
        result += f"""
### {opt['type']}
**Issue**: {opt['issue']}
**Suggestion**: {opt['suggestion']}

"""
        if 'classes' in opt:
            result += f"**Classes**: {', '.join(opt['classes'])}\n\n"
        if 'example' in opt:
            result += f"**Example**:\n```css\n{opt['example']}\n```\n\n"
    
    if not optimizations:
        result += "\n✅ No obvious optimizations needed! Your Tailwind usage looks good."
    
    return [TextContent(type="text", text=result)]


async def generate_color_palette(args: Dict[str, Any]) -> List[TextContent]:
    """Generate color palettes for Tailwind CSS."""
    primary_color = args.get("primary_color", "blue")
    palette_type = args.get("palette_type", "monochromatic")
    include_usage = args.get("include_usage", True)
    
    # Tailwind color scales
    color_scales = {
        "blue": ["blue-50", "blue-100", "blue-200", "blue-300", "blue-400", "blue-500", "blue-600", "blue-700", "blue-800", "blue-900"],
        "red": ["red-50", "red-100", "red-200", "red-300", "red-400", "red-500", "red-600", "red-700", "red-800", "red-900"],
        "green": ["green-50", "green-100", "green-200", "green-300", "green-400", "green-500", "green-600", "green-700", "green-800", "green-900"],
        "purple": ["purple-50", "purple-100", "purple-200", "purple-300", "purple-400", "purple-500", "purple-600", "purple-700", "purple-800", "purple-900"],
        "gray": ["gray-50", "gray-100", "gray-200", "gray-300", "gray-400", "gray-500", "gray-600", "gray-700", "gray-800", "gray-900"],
    }
    
    # Get base color scale
    base_scale = color_scales.get(primary_color.lower(), color_scales["blue"])
    
    # Generate palette based on type
    if palette_type == "monochromatic":
        palette = {
            "primary": base_scale,
            "usage": {
                "backgrounds": [base_scale[0], base_scale[1], base_scale[2]],  # Light shades
                "text": [base_scale[6], base_scale[7], base_scale[8]],  # Dark shades
                "accents": [base_scale[4], base_scale[5], base_scale[6]],  # Medium shades
            }
        }
    elif palette_type == "complementary":
        # Add complementary color
        complementary_colors = {
            "blue": "orange",
            "red": "green", 
            "green": "red",
            "purple": "yellow",
            "orange": "blue"
        }
        comp_color = complementary_colors.get(primary_color.lower(), "gray")
        comp_scale = color_scales.get(comp_color, color_scales["gray"])
        
        palette = {
            "primary": base_scale,
            "complementary": comp_scale,
            "usage": {
                "primary_bg": [base_scale[4], base_scale[5], base_scale[6]],
                "complementary_accent": [comp_scale[4], comp_scale[5], comp_scale[6]],
                "neutral": color_scales["gray"][:6]
            }
        }
    
    # Generate usage examples
    usage_examples = ""
    if include_usage:
        usage_examples = f"""
## Usage Examples

### Backgrounds
```css
/* Light backgrounds */
bg-{base_scale[0].split('-')[0]}-50  /* Very light */
bg-{base_scale[0].split('-')[0]}-100 /* Light */
bg-{base_scale[0].split('-')[0]}-200 /* Subtle */

/* Primary backgrounds */
bg-{base_scale[0].split('-')[0]}-500 /* Main */
bg-{base_scale[0].split('-')[0]}-600 /* Hover */
bg-{base_scale[0].split('-')[0]}-700 /* Active */
```

### Text Colors
```css
/* Primary text */
text-{base_scale[0].split('-')[0]}-600
text-{base_scale[0].split('-')[0]}-700
text-{base_scale[0].split('-')[0]}-800

/* Muted text */
text-gray-500
text-gray-600
text-gray-700
```

### Borders
```css
border-{base_scale[0].split('-')[0]}-200 /* Subtle */
border-{base_scale[0].split('-')[0]}-300 /* Visible */
border-{base_scale[0].split('-')[0]}-500 /* Prominent */
```

### Component Examples
```html
<!-- Primary Button -->
<button class="bg-{base_scale[0].split('-')[0]}-600 hover:bg-{base_scale[0].split('-')[0]}-700 text-white px-4 py-2 rounded">
  Primary Action
</button>

<!-- Secondary Button -->
<button class="bg-{base_scale[0].split('-')[0]}-100 hover:bg-{base_scale[0].split('-')[0]}-200 text-{base_scale[0].split('-')[0]}-700 px-4 py-2 rounded">
  Secondary Action
</button>

<!-- Card -->
<div class="bg-white border border-{base_scale[0].split('-')[0]}-200 rounded-lg p-6 shadow-sm">
  <h3 class="text-{base_scale[0].split('-')[0]}-800 text-lg font-semibold">Card Title</h3>
  <p class="text-gray-600 mt-2">Card content goes here.</p>
</div>
```
"""
    
    result = f"""
# {primary_color.title()} Color Palette - {palette_type.title()}

## Color Scale
{chr(10).join(f"- **{color}**: `{color}`" for color in base_scale)}

## Recommended Usage

### Light Theme
- **Background**: `bg-white`, `bg-{base_scale[0].split('-')[0]}-50`
- **Surface**: `bg-{base_scale[0].split('-')[0]}-100`, `bg-{base_scale[0].split('-')[0]}-200`
- **Primary**: `bg-{base_scale[0].split('-')[0]}-600`, `text-{base_scale[0].split('-')[0]}-600`
- **Text**: `text-gray-900`, `text-gray-700`, `text-gray-500`

### Dark Theme
- **Background**: `bg-gray-900`, `bg-gray-800`
- **Surface**: `bg-gray-700`, `bg-gray-600`
- **Primary**: `bg-{base_scale[0].split('-')[0]}-500`, `text-{base_scale[0].split('-')[0]}-400`
- **Text**: `text-white`, `text-gray-100`, `text-gray-300`

{usage_examples}

## Accessibility Notes
- Ensure sufficient contrast ratios (4.5:1 for normal text, 3:1 for large text)
- Test with color blindness simulators
- Use semantic color naming (primary, secondary, etc.)
- Provide alternative indicators beyond color alone
"""
    
    return [TextContent(type="text", text=result)]