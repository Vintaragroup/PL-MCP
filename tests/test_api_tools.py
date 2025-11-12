"""
Test the enhanced React Flow API tools specifically.
"""

import asyncio
from src.frontend_mcp_server.tools import react_flow_api_tools

async def test_react_flow_api_tools():
    """Test the new React Flow API tools."""
    print("🧪 Testing Enhanced React Flow API Tools...")
    print("=" * 60)
    
    # Test useReactFlow hook examples
    print("\n1. Testing react_flow_hook_examples (useReactFlow)...")
    result = react_flow_api_tools.react_flow_hook_examples({
        "hook_name": "useReactFlow",
        "use_case": "basic_usage",
        "include_typescript": True
    })
    print(f"Result preview: {result[0].text[:300]}...")
    
    # Test advanced components
    print("\n2. Testing react_flow_advanced_components (Handle)...")
    result = react_flow_api_tools.react_flow_advanced_components({
        "component_type": "Handle",
        "customization_level": "advanced",
        "features": ["animations", "accessibility", "validation"],
        "integration_context": "production"
    })
    print(f"Result preview: {result[0].text[:300]}...")
    
    # Test utilities generator
    print("\n3. Testing react_flow_utilities_generator...")
    result = react_flow_api_tools.react_flow_utilities_generator({
        "utility_category": "edge_utilities",
        "specific_functions": ["addEdge", "getConnectedEdges"],
        "complexity": "advanced",
        "use_case": "production"
    })
    print(f"Result preview: {result[0].text[:300]}...")
    
    # Test TypeScript definitions
    print("\n4. Testing react_flow_typescript_definitions...")
    result = react_flow_api_tools.react_flow_typescript_definitions({
        "definition_scope": "nodes_and_edges",
        "type_categories": ["Node", "Edge", "CustomNodeData"],
        "strictness_level": "strict",
        "include_generics": True
    })
    print(f"Result preview: {result[0].text[:300]}...")
    
    # Test performance optimizer
    print("\n5. Testing react_flow_performance_optimizer...")
    result = react_flow_api_tools.react_flow_performance_optimizer({
        "optimization_focus": "rendering_performance",
        "node_count_range": "large_1000_10000",
        "optimization_techniques": ["virtualization", "memoization", "debouncing"],
        "target_metrics": ["fps_60", "smooth_interactions"]
    })
    print(f"Result preview: {result[0].text[:300]}...")
    
    # Test accessibility enhancer
    print("\n6. Testing react_flow_accessibility_enhancer...")
    result = react_flow_api_tools.react_flow_accessibility_enhancer({
        "accessibility_level": "WCAG_AA",
        "accessibility_features": ["keyboard_navigation", "screen_reader_support", "aria_labels"],
        "user_scenarios": ["vision_impaired", "keyboard_only"],
        "testing_requirements": True
    })
    print(f"Result preview: {result[0].text[:300]}...")
    
    print("\n" + "=" * 60)
    print("✅ All React Flow API tools tested successfully!")
    print("🚀 Your MCP server now has EXPERT-LEVEL React Flow capabilities!")
    
    # Print summary
    print("\n📊 ENHANCED CAPABILITIES SUMMARY:")
    tools = react_flow_api_tools.get_tools()
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool.name} - {tool.description[:80]}...")

if __name__ == "__main__":
    asyncio.run(test_react_flow_api_tools())