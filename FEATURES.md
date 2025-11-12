# PL-MCP Features & Tools Documentation

## Overview

PL-MCP is a sophisticated Model Context Protocol (MCP) server featuring **21+ specialized tools** organized into 5 major categories for advanced frontend development.

## 📑 Table of Contents

1. [React Flow Tools](#react-flow-tools)
2. [React Flow API Tools](#react-flow-api-tools)
3. [React Flow Learning Tools](#react-flow-learning-tools)
4. [Connection Positioning Tools](#connection-positioning-tools)
5. [Core Frontend Tools](#core-frontend-tools)
6. [Tool Interactions](#tool-interactions)
7. [Advanced Usage Patterns](#advanced-usage-patterns)

---

## React Flow Tools

### 1. `react_flow_diagram_generator`

Generate complete React Flow diagrams with nodes, edges, and layout configurations.

**Use Cases:**
- Creating workflow diagrams
- Generating flowcharts from descriptions
- Building state machine visualizations
- Creating decision trees

**Parameters:**
```python
{
    "diagram_type": "workflow|flowchart|state_machine|decision_tree|mindmap",
    "description": "Detailed description of the diagram",
    "include_styling": true,
    "responsive": true
}
```

**Example Output:**
```typescript
// Complete React Flow component with:
// - Proper node and edge definitions
// - Layout algorithm configuration
// - Event handlers
// - Styling and animations
```

**Performance:** Handles up to 500 nodes natively

---

### 2. `react_flow_custom_node_generator`

Generate custom node components with specific functionality.

**Features:**
- Handle configuration
- Custom styling
- Data binding
- Event handlers
- TypeScript support

**Parameters:**
```python
{
    "node_type": "input|process|output|decision|custom",
    "features": ["draggable", "resizable", "deletable", "selectable"],
    "styling": "tailwind|styled-components|css-modules",
    "with_handles": true
}
```

---

### 3. `react_flow_edge_analyzer`

Analyze and optimize edge configurations for better performance.

**Analyzes:**
- Edge types (bezier, smooth, straight, step)
- Path optimization
- Performance impact
- Visual clarity

**Parameters:**
```python
{
    "edge_count": 100,
    "node_count": 50,
    "optimization_focus": "performance|visual_clarity|both"
}
```

---

### 4. `react_flow_layout_optimizer`

Optimize layout algorithms and parameters for specific use cases.

**Supported Algorithms:**
- Dagre (default)
- D3-Force
- D3-Hierarchy
- ELK.js
- Custom algorithms

**Parameters:**
```python
{
    "algorithm": "dagre|d3-force|d3-hierarchy|elk",
    "direction": "TB|BT|LR|RL",
    "node_count": "small|medium|large|xlarge",
    "optimization_goal": "performance|visual_appeal|both"
}
```

---

### 5. `react_flow_hierarchical_tree_generator`

Generate hierarchical tree structures with proper layering.

**Features:**
- Multi-level hierarchies
- Branch optimization
- Sibling alignment
- Parent-child relationships

**Parameters:**
```python
{
    "levels": 3,
    "siblings_per_node": 5,
    "node_height": 50,
    "node_width": 150,
    "level_spacing": 100
}
```

---

### 6. `react_flow_elk_layout_generator`

Generate ELK (Eclipse Layout Kernel) configurations for complex layouts.

**Capabilities:**
- Hierarchical layouts
- Orthogonal edge routing
- Cycle breaking
- Layer-based algorithms

**Parameters:**
```python
{
    "layout_algorithm": "layered|orthogonal|mrtree",
    "spacing_node": 100,
    "spacing_edge": 20,
    "direction": "UP|DOWN|LEFT|RIGHT"
}
```

---

## React Flow API Tools

### 7. `react_flow_hook_examples`

Generate examples for React Flow hooks with official API compliance.

**Available Hooks:**
- `useReactFlow` - Access flow instance
- `useStore` - Access store state
- `useConnection` - Handle connections
- `useViewport` - Manage viewport
- `useKeyPress` - Keyboard handling
- `useNodes` / `useEdges` - Access nodes/edges
- `useNodesInitialized` - Initialization tracking

**Parameters:**
```python
{
    "hook_name": "useReactFlow|useStore|useConnection|...",
    "use_case": "basic_usage|advanced_patterns|performance_optimization|custom_components|state_management",
    "include_typescript": true
}
```

**Example Output:**
```typescript
import React, { useCallback } from 'react';
import { useReactFlow } from 'reactflow';

const FlowControls: React.FC = () => {
  const { getNodes, getEdges, fitView, zoomIn, zoomOut } = useReactFlow();
  
  const handleFitView = useCallback(() => {
    fitView({ duration: 800, padding: 0.2 });
  }, [fitView]);
  
  return (
    <div className="flow-controls">
      <button onClick={handleFitView}>Fit View</button>
      <button onClick={() => zoomIn({ duration: 200 })}>Zoom In</button>
      <button onClick={() => zoomOut({ duration: 200 })}>Zoom Out</button>
    </div>
  );
};
```

---

### 8. `react_flow_advanced_components`

Generate sophisticated component implementations.

**Components:**
- `Handle` - Connection points
- `NodeToolbar` - Node controls
- `EdgeToolbar` - Edge controls
- `MiniMap` - Diagram overview
- `Controls` - Pan/zoom controls
- `Background` - Canvas background
- `Panel` - Floating panels

**Parameters:**
```python
{
    "component_type": "Handle|NodeToolbar|EdgeToolbar|MiniMap|Controls|Background|Panel|ViewportPortal",
    "customization_level": "basic|styled|advanced|production",
    "features": ["animations", "responsive_design", "accessibility", "keyboard_navigation", "touch_support"],
    "integration_context": "standalone|with_forms|with_data_binding|with_animations|enterprise"
}
```

---

### 9. `react_flow_utilities_generator`

Generate utility functions for common operations.

**Utility Categories:**
- Edge utilities (addEdge, removeEdge, updateEdge)
- Node utilities (addNodes, removeNodes, updateNodes)
- Viewport utilities (fitView, getViewport)
- Path utilities (getBezierPath, getSmoothStepPath)
- Validation utilities
- Transformation utilities

**Parameters:**
```python
{
    "utility_category": "edge_utilities|node_utilities|viewport_utilities|path_utilities|validation_utilities|transformation_utilities|selection_utilities|change_utilities",
    "specific_functions": ["addEdge", "getBezierPath", "getConnectedEdges", ...],
    "complexity": "basic|intermediate|advanced|enterprise",
    "use_case": "development|production|performance_critical|educational"
}
```

---

### 10. `react_flow_typescript_definitions`

Generate complete TypeScript interfaces and type definitions.

**Type Categories:**
- Node types
- Edge types
- Connection types
- Event handler types
- State management types
- Component prop types

**Parameters:**
```python
{
    "definition_scope": "nodes_and_edges|custom_components|event_handlers|hook_types|utility_types|configuration_types|state_management|complete_application",
    "type_categories": ["Node", "Edge", "NodeProps", "EdgeProps", "Connection", "Viewport", ...],
    "strictness_level": "strict|moderate|flexible",
    "include_generics": true
}
```

---

### 11. `react_flow_performance_optimizer`

Generate performance optimization strategies and implementations.

**Optimization Focus:**
- Rendering performance
- Memory optimization
- Interaction responsiveness
- Large dataset handling
- Real-time updates
- Mobile performance
- Bundle size reduction

**Parameters:**
```python
{
    "optimization_focus": "rendering_performance|memory_optimization|interaction_responsiveness|large_datasets|real_time_updates|mobile_performance|bundle_size|initial_load_time",
    "node_count_range": "small_10_100|medium_100_1000|large_1000_10000|xlarge_10000_plus",
    "optimization_techniques": ["virtualization", "memoization", "web_workers", "lazy_loading", "debouncing", "throttling", "batch_updates", "viewport_culling"],
    "target_metrics": ["fps_60", "memory_under_100mb", "load_time_under_3s", "smooth_interactions"]
}
```

---

### 12. `react_flow_accessibility_enhancer`

Generate accessibility features for WCAG compliance.

**Features:**
- Keyboard navigation
- Screen reader support
- Focus management
- ARIA labels
- High contrast support
- Motion preferences
- Voice control support

**Parameters:**
```python
{
    "accessibility_level": "WCAG_A|WCAG_AA|WCAG_AAA",
    "accessibility_features": ["keyboard_navigation", "screen_reader_support", "focus_management", "aria_labels", "high_contrast", "reduced_motion", "voice_control"],
    "user_scenarios": ["vision_impaired", "motor_impaired", "cognitive_impaired", "keyboard_only", "mobile_touch", "voice_only"],
    "testing_requirements": true
}
```

---

## React Flow Learning Tools

### 13. `react_flow_layouting_expert`

Expert guidance on layout algorithms and implementations.

**Topics:**
- Layout algorithm selection
- Parameter optimization
- Connection-aware positioning
- Hierarchical layouts
- Force-directed layouts
- Circular layouts

**Parameters:**
```python
{
    "query_type": "connection_aware_positioning|hierarchical_layouts|force_directed|circular_layouts|auto_layout|manual_positioning",
    "description": "Your specific use case or question"
}
```

**Response Includes:**
- Algorithm recommendations
- Parameter tuning guide
- Performance considerations
- Best practices
- Example implementations

---

### 14. `react_flow_performance_mastery`

Optimization strategies for large-scale applications.

**Covers:**
- Node virtualization
- Memoization strategies
- Web worker utilization
- Lazy loading patterns
- Viewport culling
- State optimization

**Parameters:**
```python
{
    "node_count_range": "small_1_10|medium_10_50|large_50_100|xlarge_100_plus",
    "performance_focus": "rendering|memory|interaction|all",
    "current_bottleneck": "describe your performance issue"
}
```

---

### 15. `react_flow_tutorial_generator`

Generate interactive tutorials and learning paths.

**Tutorial Types:**
- Getting started
- Intermediate patterns
- Advanced architectures
- Performance optimization
- Real-world applications

**Parameters:**
```python
{
    "skill_level": "beginner|intermediate|advanced|expert",
    "topic": "routing|layout|performance|customization|testing|deployment",
    "project_complexity": "simple|moderate|complex|enterprise"
}
```

---

### 16. `react_flow_troubleshooting_expert`

Debugging and troubleshooting guidance.

**Handles:**
- Layout issues
- Performance problems
- Connection problems
- State management issues
- Event handling
- Browser compatibility

**Parameters:**
```python
{
    "problem_category": "layout_debugging|performance_debugging|connection_issues|state_management|event_handling|browser_compatibility|rendering_issues|memory_leaks",
    "description": "Detailed description of the issue",
    "error_message": "Any error message or console output",
    "reproduction_steps": "Steps to reproduce the issue"
}
```

---

### 17. `react_flow_accessibility_expert`

Accessibility best practices and implementation.

**Topics:**
- WCAG compliance strategies
- Keyboard navigation implementation
- Screen reader optimization
- Focus management
- ARIA labeling patterns
- Testing approaches

**Parameters:**
```python
{
    "accessibility_goal": "wcag_compliance|keyboard_support|screen_reader|focus_management|color_contrast|motion_accessibility|all",
    "current_challenges": "Describe accessibility challenges",
    "target_users": "List specific user groups"
}
```

---

### 18. `react_flow_devtools_mastery`

Browser DevTools and debugging integration.

**Capabilities:**
- Performance profiling
- Memory debugging
- Network inspection
- State inspection
- Component rendering analysis
- Visual debugging overlays

**Parameters:**
```python
{
    "debugging_focus": "layout_debugging|performance_profiling|memory_analysis|state_inspection|rendering_analysis|component_hierarchy",
    "issue_description": "What you're trying to debug"
}
```

---

## Connection Positioning Tools

### 19. `generate_connection_aware_node`

Generate nodes that automatically position on the correct connection side.

**Features:**
- Automatic side detection
- Spacing calculation
- Auto-layout integration
- Whiteboard optimization

**Parameters:**
```python
{
    "connection_side": "right|left|top|bottom",
    "layout_style": "whiteboard|hierarchical|organic|tree",
    "spacing_config": {
        "horizontal": 200,
        "vertical": 150,
        "margin": 20
    },
    "auto_layout": true
}
```

---

### 20. `codex_positioning_prompts`

Generate specific prompts for Codex integration.

**Scenarios:**
- New node creation
- Workflow building
- Decision trees
- Whiteboard brainstorming
- Process flows
- Mindmaps

**Parameters:**
```python
{
    "scenario": "new_node_creation|workflow_building|decision_tree|whiteboard_brainstorming|process_flow|mindmap",
    "complexity_level": "basic|intermediate|advanced"
}
```

---

### 21. `dagre_configuration_optimizer`

Optimize Dagre layout configurations.

**Optimizes:**
- Node spacing
- Rank separation
- Direction
- Edge routing

**Parameters:**
```python
{
    "flow_direction": "TB|BT|LR|RL",
    "node_count": "small_1_10|medium_10_50|large_50_100|xlarge_100_plus",
    "connection_density": "sparse|moderate|dense"
}
```

---

### 22. `handle_positioning_guide`

Generate handle positioning configurations.

**Parameters:**
```python
{
    "node_type": "input|output|process|decision|connector|custom",
    "connection_pattern": "linear|branching|converging|bidirectional",
    "visual_style": "minimal|styled|animated|professional"
}
```

---

### 23. `whiteboard_layout_optimizer`

Whiteboard-optimized layout configurations.

**Parameters:**
```python
{
    "whiteboard_size": "compact_800x600|standard_1200x800|large_1600x1200|xlarge_2000x1500",
    "content_type": "brainstorming|process_mapping|system_design|workflow_creation",
    "collaboration_mode": false
}
```

---

## Core Frontend Tools

### 24. `react_component_generator`

Generate TypeScript React components.

**Parameters:**
```python
{
    "component_name": "MyComponent",
    "props": [
        {"name": "title", "type": "string"},
        {"name": "onClick", "type": "(data: any) => void"}
    ],
    "styling": "tailwind|css-modules|styled-components|none"
}
```

---

### 25. `tailwind_class_suggester`

Get optimized Tailwind CSS class suggestions.

**Parameters:**
```python
{
    "design_description": "blue button with rounded corners",
    "element_type": "button|card|form|navigation|layout|text|general",
    "responsive": true
}
```

---

### 26. `package_analyzer`

Analyze package.json files.

**Parameters:**
```python
{
    "package_json": "{ ... }",
    "analysis_type": "dependencies|vulnerabilities|optimization|all"
}
```

---

### 27. `react_hook_generator`

Generate custom React hooks.

**Parameters:**
```python
{
    "hook_name": "useCustomHook",
    "functionality": "Description of what the hook does"
}
```

---

## Tool Interactions

### Combined Workflows

#### Workflow 1: Complete Flow Diagram Creation
1. Use `react_flow_layouting_expert` → Determine best layout algorithm
2. Use `react_flow_diagram_generator` → Generate base structure
3. Use `react_flow_custom_node_generator` → Create custom nodes
4. Use `dagre_configuration_optimizer` → Optimize layout
5. Use `react_flow_performance_optimizer` → Optimize performance
6. Use `react_flow_accessibility_enhancer` → Add accessibility

#### Workflow 2: Large-Scale Optimization
1. Identify bottleneck with `react_flow_devtools_mastery`
2. Get optimization strategy from `react_flow_performance_mastery`
3. Generate optimized code with `react_flow_utilities_generator`
4. Implement with TypeScript types from `react_flow_typescript_definitions`
5. Test with performance metrics

#### Workflow 3: Whiteboard Layout Mastery
1. Use `whiteboard_layout_optimizer` → Configure canvas
2. Use `generate_connection_aware_node` → Create positioning logic
3. Use `dagre_configuration_optimizer` → Optimize layout
4. Use `codex_positioning_prompts` → Get Codex prompts
5. Deploy with proper TypeScript definitions

---

## Advanced Usage Patterns

### Pattern 1: Hierarchical Organization Chart

```python
# Step 1: Get layout strategy
layout_advice = react_flow_layouting_expert({
    "query_type": "hierarchical_layouts",
    "description": "Organization chart with departments and teams"
})

# Step 2: Generate hierarchical structure
hierarchy = react_flow_hierarchical_tree_generator({
    "levels": 4,
    "siblings_per_node": 5
})

# Step 3: Optimize for readability
layout = dagre_configuration_optimizer({
    "flow_direction": "TB",
    "node_count": "large_50_100"
})
```

### Pattern 2: High-Performance Large Graph

```python
# Analyze performance needs
perf_strategy = react_flow_performance_mastery({
    "node_count_range": "xlarge_10000_plus",
    "performance_focus": "rendering"
})

# Generate optimized utilities
utilities = react_flow_utilities_generator({
    "utility_category": "optimization_utilities",
    "optimization_techniques": ["virtualization", "memoization", "viewport_culling"]
})

# Implement with TypeScript
types = react_flow_typescript_definitions({
    "definition_scope": "performance_optimization"
})
```

### Pattern 3: Accessible Interactive Diagram

```python
# Plan accessibility
a11y_plan = react_flow_accessibility_expert({
    "accessibility_goal": "wcag_compliance",
    "target_users": ["vision_impaired", "keyboard_only", "motor_impaired"]
})

# Generate accessible components
components = react_flow_advanced_components({
    "customization_level": "advanced",
    "features": ["keyboard_navigation", "aria_labels", "focus_management"]
})

# Add accessibility enhancements
enhanced = react_flow_accessibility_enhancer({
    "accessibility_level": "WCAG_AA",
    "accessibility_features": ["keyboard_navigation", "screen_reader_support", "focus_management"]
})
```

---

## Performance Benchmarks

| Operation | Small (10-100) | Medium (100-1K) | Large (1K-10K) | XLarge (10K+) |
|-----------|---|---|---|---|
| Layout Time | <100ms | 100-500ms | 500ms-2s | 2s+ (needs optimization) |
| Render Time | <50ms | 50-200ms | 200-1000ms | 1s+ (virtualization required) |
| Memory | <10MB | 10-50MB | 50-200MB | 200MB+ (optimization critical) |
| Interactions | Smooth | Smooth | May stutter | Requires virtualization |

---

## Resource Links

- [Official React Flow Documentation](https://reactflow.dev)
- [MCP Specification](https://spec.modelcontextprotocol.io)
- [React Flow API Reference](https://reactflow.dev/api-reference)
- [Dagre Layout Algorithm](https://dagrejs.github.io/project/dagre)
- [ELK Layout Documentation](https://www.eclipse.org/elk)

---

**Last Updated:** November 2025  
**Tool Count:** 27  
**Status:** Production Ready
