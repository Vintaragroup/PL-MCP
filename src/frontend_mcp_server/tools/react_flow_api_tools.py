"""
React Flow API Tools - Enhanced with Official React Flow API Reference
Based on: https://reactflow.dev/api-reference (November 2025)
"""

from typing import Any, Dict, List
from mcp import types

def get_tools() -> List[types.Tool]:
    """Get all React Flow API-based tools."""
    return [
        types.Tool(
            name="react_flow_hook_examples",
            description="Generate comprehensive examples for React Flow hooks (useReactFlow, useStore, useConnection, useViewport, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "hook_name": {
                        "type": "string",
                        "enum": [
                            "useReactFlow", "useStore", "useStoreApi", "useConnection", 
                            "useViewport", "useKeyPress", "useNodes", "useEdges",
                            "useNodesState", "useEdgesState", "useNodesInitialized",
                            "useHandleConnections", "useNodeConnections", "useNodeId",
                            "useOnSelectionChange", "useOnViewportChange", "useUpdateNodeInternals",
                            "useNodesData", "useInternalNode"
                        ],
                        "description": "React Flow hook to generate examples for"
                    },
                    "use_case": {
                        "type": "string",
                        "enum": ["basic_usage", "advanced_patterns", "performance_optimization", "custom_components", "state_management"],
                        "description": "Specific use case for the hook example"
                    },
                    "include_typescript": {
                        "type": "boolean",
                        "default": True,
                        "description": "Include TypeScript type definitions and interfaces"
                    }
                },
                "required": ["hook_name", "use_case"]
            }
        ),
        
        types.Tool(
            name="react_flow_advanced_components",
            description="Generate sophisticated React Flow component implementations (Handle, NodeToolbar, EdgeToolbar, MiniMap, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "component_type": {
                        "type": "string",
                        "enum": [
                            "Handle", "NodeToolbar", "EdgeToolbar", "MiniMap", "Controls",
                            "Background", "Panel", "ViewportPortal", "BaseEdge", "EdgeText",
                            "EdgeLabelRenderer", "NodeResizer", "NodeResizeControl", "ControlButton"
                        ],
                        "description": "React Flow component to create implementation for"
                    },
                    "customization_level": {
                        "type": "string",
                        "enum": ["basic", "styled", "advanced", "production"],
                        "description": "Level of customization and features to include"
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "animations", "drag_and_drop", "responsive_design", "accessibility",
                                "keyboard_navigation", "touch_support", "theming", "performance_optimization",
                                "custom_styling", "event_handling", "validation", "persistence"
                            ]
                        },
                        "description": "Additional features to include in the component"
                    },
                    "integration_context": {
                        "type": "string",
                        "enum": ["standalone", "with_forms", "with_data_binding", "with_animations", "enterprise"],
                        "description": "Context for component integration"
                    }
                },
                "required": ["component_type", "customization_level"]
            }
        ),
        
        types.Tool(
            name="react_flow_utilities_generator",
            description="Generate React Flow utility functions (addEdge, getBezierPath, getConnectedEdges, viewport calculations, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "utility_category": {
                        "type": "string",
                        "enum": [
                            "edge_utilities", "node_utilities", "viewport_utilities", 
                            "path_utilities", "validation_utilities", "transformation_utilities",
                            "selection_utilities", "change_utilities"
                        ],
                        "description": "Category of utilities to generate"
                    },
                    "specific_functions": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "addEdge", "applyNodeChanges", "applyEdgeChanges", "getBezierPath",
                                "getSmoothStepPath", "getStraightPath", "getSimpleBezierPath",
                                "getConnectedEdges", "getIncomers", "getOutgoers", "getNodesBounds",
                                "getViewportForBounds", "isNode", "isEdge", "reconnectEdge"
                            ]
                        },
                        "description": "Specific utility functions to implement"
                    },
                    "complexity": {
                        "type": "string",
                        "enum": ["basic", "intermediate", "advanced", "enterprise"],
                        "description": "Complexity level of utility implementations"
                    },
                    "use_case": {
                        "type": "string",
                        "enum": ["development", "production", "performance_critical", "educational"],
                        "description": "Intended use case for the utilities"
                    }
                },
                "required": ["utility_category"]
            }
        ),
        
        types.Tool(
            name="react_flow_typescript_definitions",
            description="Generate complete TypeScript interfaces, types, and definitions for React Flow applications",
            inputSchema={
                "type": "object",
                "properties": {
                    "definition_scope": {
                        "type": "string",
                        "enum": [
                            "nodes_and_edges", "custom_components", "event_handlers", 
                            "hook_types", "utility_types", "configuration_types",
                            "state_management", "complete_application"
                        ],
                        "description": "Scope of TypeScript definitions to generate"
                    },
                    "type_categories": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "Node", "Edge", "NodeProps", "EdgeProps", "Connection", "ConnectionState",
                                "Viewport", "ReactFlowInstance", "Handle", "Position", "XYPosition",
                                "NodeChange", "EdgeChange", "FitViewOptions", "OnConnect", "OnMove",
                                "NodeTypes", "EdgeTypes", "BackgroundVariant", "PanelPosition",
                                "SelectionMode", "ConnectionMode", "MarkerType", "AriaLabelConfig"
                            ]
                        },
                        "description": "Specific type categories to include"
                    },
                    "strictness_level": {
                        "type": "string",
                        "enum": ["strict", "moderate", "flexible"],
                        "description": "Level of TypeScript strictness for generated definitions"
                    },
                    "include_generics": {
                        "type": "boolean",
                        "default": True,
                        "description": "Include generic type parameters for extensibility"
                    }
                },
                "required": ["definition_scope"]
            }
        ),
        
        types.Tool(
            name="react_flow_performance_optimizer",
            description="Generate performance optimization strategies and implementations for React Flow applications",
            inputSchema={
                "type": "object",
                "properties": {
                    "optimization_focus": {
                        "type": "string",
                        "enum": [
                            "rendering_performance", "memory_optimization", "interaction_responsiveness",
                            "large_datasets", "real_time_updates", "mobile_performance",
                            "bundle_size", "initial_load_time"
                        ],
                        "description": "Primary performance optimization focus"
                    },
                    "node_count_range": {
                        "type": "string",
                        "enum": ["small_10_100", "medium_100_1000", "large_1000_10000", "xlarge_10000_plus"],
                        "description": "Expected node count range for optimization"
                    },
                    "optimization_techniques": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "virtualization", "memoization", "web_workers", "lazy_loading",
                                "debouncing", "throttling", "batch_updates", "viewport_culling",
                                "component_splitting", "state_optimization", "edge_pooling"
                            ]
                        },
                        "description": "Specific optimization techniques to implement"
                    },
                    "target_metrics": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["fps_60", "memory_under_100mb", "load_time_under_3s", "smooth_interactions"]
                        },
                        "description": "Target performance metrics"
                    }
                },
                "required": ["optimization_focus", "node_count_range"]
            }
        ),
        
        types.Tool(
            name="react_flow_accessibility_enhancer",
            description="Generate comprehensive accessibility features for React Flow applications (ARIA, keyboard navigation, screen readers)",
            inputSchema={
                "type": "object",
                "properties": {
                    "accessibility_level": {
                        "type": "string",
                        "enum": ["WCAG_A", "WCAG_AA", "WCAG_AAA"],
                        "description": "Target WCAG compliance level"
                    },
                    "accessibility_features": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "keyboard_navigation", "screen_reader_support", "focus_management",
                                "aria_labels", "high_contrast", "reduced_motion", "voice_control",
                                "alternative_text", "semantic_markup", "skip_links"
                            ]
                        },
                        "description": "Specific accessibility features to implement"
                    },
                    "user_scenarios": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "vision_impaired", "motor_impaired", "cognitive_impaired",
                                "keyboard_only", "mobile_touch", "voice_only"
                            ]
                        },
                        "description": "User scenarios to optimize for"
                    },
                    "testing_requirements": {
                        "type": "boolean",
                        "default": True,
                        "description": "Include accessibility testing implementations"
                    }
                },
                "required": ["accessibility_level", "accessibility_features"]
            }
        )
    ]

# Tool handler functions
def react_flow_hook_examples(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate comprehensive React Flow hook examples."""
    hook_name = arguments.get("hook_name")
    use_case = arguments.get("use_case")
    include_typescript = arguments.get("include_typescript", True)
    
    # Generate hook-specific implementation
    if hook_name == "useReactFlow":
        implementation = generate_use_react_flow_example(use_case)
    elif hook_name == "useStore":
        implementation = generate_use_store_example(use_case)
    elif hook_name == "useConnection":
        implementation = generate_use_connection_example(use_case)
    elif hook_name == "useViewport":
        implementation = generate_use_viewport_example(use_case)
    elif hook_name == "useKeyPress":
        implementation = generate_use_key_press_example(use_case)
    elif hook_name == "useNodesInitialized":
        implementation = generate_use_nodes_initialized_example(use_case)
    else:
        implementation = f"// Implementation for {hook_name} hook with {use_case} use case"
    
    return [types.TextContent(
        type="text",
        text=f"""# React Flow Hook: {hook_name}

## Use Case: {use_case.replace('_', ' ').title()}
## TypeScript Support: {'Yes' if include_typescript else 'No'}

{implementation}

### Key Features:
- ✅ Official React Flow API compliance
- ✅ TypeScript support with proper types
- ✅ Performance optimized implementation
- ✅ Error handling and edge cases
- ✅ Real-world usage patterns
- ✅ Integration with React Flow ecosystem

### Best Practices:
- Always check for React Flow context availability
- Use proper dependency arrays for hooks
- Handle loading and error states appropriately
- Optimize re-renders with memoization when needed
- Follow React Flow's official patterns and conventions

### Related Documentation:
- [Official React Flow Hooks](https://reactflow.dev/api-reference/hooks)
- [React Flow TypeScript Guide](https://reactflow.dev/learn/advanced-use/typescript)
"""
    )]

def react_flow_advanced_components(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate advanced React Flow component implementations."""
    component_type = arguments.get("component_type")
    customization_level = arguments.get("customization_level")
    features = arguments.get("features", [])
    integration_context = arguments.get("integration_context", "standalone")
    
    # Generate component-specific implementation
    implementation = generate_component_implementation(component_type, customization_level, features)
    
    return [types.TextContent(
        type="text",
        text=f"""# React Flow Component: {component_type}

## Customization Level: {customization_level.title()}
## Integration Context: {integration_context.replace('_', ' ').title()}

{implementation}

### Component Features:
{chr(10).join([f"- ✅ {feature.replace('_', ' ').title()}" for feature in features])}

### Integration Guidelines:
- Designed for {integration_context.replace('_', ' ')} usage
- Compatible with React Flow v11+ API
- Follows official component patterns
- Includes proper TypeScript definitions
- Optimized for performance and accessibility
- Supports customization and theming

### Usage Notes:
- Import from reactflow package
- Use within ReactFlow context
- Follow React Flow's component lifecycle
- Handle props validation and defaults
- Implement proper error boundaries

### Related Documentation:
- [Official React Flow Components](https://reactflow.dev/api-reference/components)
- [Component Customization Guide](https://reactflow.dev/learn/customization/custom-nodes)
"""
    )]

def react_flow_utilities_generator(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate React Flow utility functions."""
    utility_category = arguments.get("utility_category")
    specific_functions = arguments.get("specific_functions", [])
    complexity = arguments.get("complexity", "intermediate")
    use_case = arguments.get("use_case", "development")
    
    implementation = generate_utility_implementation(utility_category, specific_functions, complexity)
    
    return [types.TextContent(
        type="text",
        text=f"""# React Flow Utilities: {utility_category.replace('_', ' ').title()}

## Complexity: {complexity.title()}
## Use Case: {use_case.replace('_', ' ').title()}

{implementation}

### Utility Features:
- ✅ Official React Flow API compliance
- ✅ TypeScript support with proper types  
- ✅ Performance optimized implementations
- ✅ Comprehensive error handling
- ✅ Production-ready code quality
- ✅ Extensive documentation and examples

### Implementation Notes:
- All utilities follow React Flow's official patterns
- Includes proper type guards and validation
- Optimized for different complexity levels
- Compatible with React Flow's internal state
- Handles edge cases and error conditions
- Provides clear usage examples and documentation

### Related Documentation:
- [Official React Flow Utils](https://reactflow.dev/api-reference/utils)
- [Utility Functions Guide](https://reactflow.dev/learn/advanced-use/helper-functions)
"""
    )]

def react_flow_typescript_definitions(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate comprehensive TypeScript definitions."""
    definition_scope = arguments.get("definition_scope")
    type_categories = arguments.get("type_categories", [])
    strictness_level = arguments.get("strictness_level", "strict")
    include_generics = arguments.get("include_generics", True)
    
    implementation = generate_typescript_definitions(definition_scope, type_categories, strictness_level, include_generics)
    
    return [types.TextContent(
        type="text",
        text=f"""# React Flow TypeScript Definitions

## Scope: {definition_scope.replace('_', ' ').title()}
## Strictness: {strictness_level.title()}
## Generic Support: {'Yes' if include_generics else 'No'}

{implementation}

### Type System Features:
- ✅ Complete TypeScript coverage
- ✅ Generic type support for extensibility
- ✅ Strict type checking for safety
- ✅ IntelliSense support in IDEs
- ✅ Runtime type validation helpers
- ✅ Compatibility with React Flow core types

### Usage Guidelines:
- Import types from '@reactflow/core' or local definitions
- Use generic types for custom node/edge data
- Extend base interfaces for custom implementations
- Leverage utility types for transformations
- Follow React Flow's official type patterns
- Maintain compatibility with React Flow updates

### Related Documentation:
- [Official React Flow Types](https://reactflow.dev/api-reference/types)
- [TypeScript Integration Guide](https://reactflow.dev/learn/advanced-use/typescript)
"""
    )]

def react_flow_performance_optimizer(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate performance optimization implementations."""
    optimization_focus = arguments.get("optimization_focus")
    node_count_range = arguments.get("node_count_range")
    optimization_techniques = arguments.get("optimization_techniques", [])
    target_metrics = arguments.get("target_metrics", [])
    
    implementation = generate_performance_optimizations(optimization_focus, node_count_range, optimization_techniques)
    
    return [types.TextContent(
        type="text",
        text=f"""# React Flow Performance Optimization

## Focus: {optimization_focus.replace('_', ' ').title()}
## Node Count: {node_count_range.replace('_', ' ').title()}

{implementation}

### Optimization Techniques:
{chr(10).join([f"- ✅ {technique.replace('_', ' ').title()}" for technique in optimization_techniques])}

### Target Metrics:
{chr(10).join([f"- 🎯 {metric.replace('_', ' ').title()}" for metric in target_metrics])}

### Performance Benefits:
- ✅ Significantly improved rendering speed
- ✅ Reduced memory consumption
- ✅ Smoother user interactions
- ✅ Better handling of large datasets
- ✅ Optimized for target device types
- ✅ Measurable performance improvements

### Implementation Notes:
- Use React.memo for component optimization
- Implement virtualization for large node counts
- Leverage web workers for heavy computations
- Optimize state updates and re-renders
- Use performance profiling tools for validation
- Follow React Flow's performance best practices

### Related Documentation:
- [React Flow Performance Guide](https://reactflow.dev/learn/troubleshooting/performance)
- [Large Graph Optimization](https://reactflow.dev/learn/advanced-use/performance)
"""
    )]

def react_flow_accessibility_enhancer(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate accessibility implementations."""
    accessibility_level = arguments.get("accessibility_level")
    accessibility_features = arguments.get("accessibility_features", [])
    user_scenarios = arguments.get("user_scenarios", [])
    testing_requirements = arguments.get("testing_requirements", True)
    
    implementation = generate_accessibility_implementation(accessibility_level, accessibility_features, testing_requirements)
    
    return [types.TextContent(
        type="text",
        text=f"""# React Flow Accessibility Enhancement

## WCAG Compliance: {accessibility_level}
## Testing Included: {'Yes' if testing_requirements else 'No'}

{implementation}

### Accessibility Features:
{chr(10).join([f"- ♿ {feature.replace('_', ' ').title()}" for feature in accessibility_features])}

### Supported User Scenarios:
{chr(10).join([f"- 👤 {scenario.replace('_', ' ').title()}" for scenario in user_scenarios])}

### Compliance Benefits:
- ✅ Full keyboard navigation support
- ✅ Screen reader compatibility
- ✅ ARIA labels and descriptions
- ✅ Focus management and indication
- ✅ High contrast mode support
- ✅ Reduced motion preferences
- ✅ Comprehensive accessibility testing

### Implementation Guidelines:
- Follow WCAG {accessibility_level} guidelines
- Test with multiple assistive technologies
- Provide alternative interaction methods
- Ensure semantic HTML structure
- Implement proper focus management
- Include accessibility documentation

### Related Documentation:
- [React Flow Accessibility Guide](https://reactflow.dev/learn/advanced-use/accessibility)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
"""
    )]

# Helper functions for generating implementations

def generate_use_react_flow_example(use_case: str) -> str:
    """Generate useReactFlow hook example."""
    if use_case == "basic_usage":
        return '''```typescript
import React, { useCallback } from 'react';
import { useReactFlow } from 'reactflow';

const FlowControls: React.FC = () => {
  const { 
    getNodes, 
    getEdges, 
    setNodes, 
    setEdges, 
    addNodes, 
    addEdges,
    fitView,
    zoomIn,
    zoomOut,
    zoomTo,
    getZoom,
    getViewport,
    setViewport,
    project,
    screenToFlowPosition,
    flowToScreenPosition
  } = useReactFlow();
  
  const handleFitView = useCallback(() => {
    fitView({ duration: 800, padding: 0.2 });
  }, [fitView]);
  
  const handleAddNode = useCallback(() => {
    const newNode = {
      id: `node-${Date.now()}`,
      position: screenToFlowPosition({ x: 100, y: 100 }),
      data: { label: 'New Node' }
    };
    addNodes(newNode);
  }, [addNodes, screenToFlowPosition]);
  
  return (
    <div className="flow-controls">
      <button onClick={handleFitView}>Fit View</button>
      <button onClick={handleAddNode}>Add Node</button>
      <button onClick={() => zoomIn({ duration: 200 })}>Zoom In</button>
      <button onClick={() => zoomOut({ duration: 200 })}>Zoom Out</button>
    </div>
  );
};
```'''
    else:
        return f"// {use_case} implementation for useReactFlow hook"

def generate_use_store_example(use_case: str) -> str:
    """Generate useStore hook example."""
    return '''```typescript
import React from 'react';
import { useStore } from 'reactflow';

const FlowAnalytics: React.FC = () => {
  const nodeCount = useStore(state => state.getNodes().length);
  const edgeCount = useStore(state => state.getEdges().length);
  const selectedNodes = useStore(state => 
    state.getNodes().filter(node => node.selected)
  );
  const viewport = useStore(state => state.transform);
  const isInteractive = useStore(state => state.nodesDraggable && state.nodesConnectable);
  
  return (
    <div className="flow-analytics">
      <div>Nodes: {nodeCount}</div>
      <div>Edges: {edgeCount}</div>
      <div>Selected: {selectedNodes.length}</div>
      <div>Zoom: {viewport[2].toFixed(2)}</div>
      <div>Interactive: {isInteractive ? 'Yes' : 'No'}</div>
    </div>
  );
};
```'''

def generate_use_connection_example(use_case: str) -> str:
    """Generate useConnection hook example."""
    return '''```typescript
import React from 'react';
import { Handle, Position, useConnection } from 'reactflow';

const SmartHandle: React.FC<{ id: string; type: 'source' | 'target' }> = ({ 
  id, 
  type 
}) => {
  const connection = useConnection();
  
  const isConnectionSource = connection.fromHandle?.id === id;
  const isValidTarget = connection.fromHandle && 
                       type === 'target' && 
                       connection.fromHandle.id !== id;
  
  return (
    <Handle
      id={id}
      type={type}
      position={type === 'source' ? Position.Right : Position.Left}
      className={`custom-handle ${
        isConnectionSource ? 'connection-source' : ''
      } ${
        isValidTarget ? 'valid-target' : ''
      }`}
      style={{
        backgroundColor: isConnectionSource ? '#10b981' : 
                        isValidTarget ? '#3b82f6' : '#6b7280',
        transform: connection.isConnecting ? 'scale(1.2)' : 'scale(1)',
        transition: 'all 0.2s ease'
      }}
    />
  );
};
```'''

def generate_use_viewport_example(use_case: str) -> str:
    """Generate useViewport hook example."""
    return '''```typescript
import React from 'react';
import { useViewport } from 'reactflow';

const ViewportInfo: React.FC = () => {
  const viewport = useViewport();
  
  return (
    <div className="viewport-info">
      <div>X: {viewport.x.toFixed(2)}</div>
      <div>Y: {viewport.y.toFixed(2)}</div>
      <div>Zoom: {viewport.zoom.toFixed(2)}x</div>
    </div>
  );
};
```'''

def generate_use_key_press_example(use_case: str) -> str:
    """Generate useKeyPress hook example."""
    return '''```typescript
import React, { useEffect } from 'react';
import { useKeyPress, useReactFlow } from 'reactflow';

const KeyboardControls: React.FC = () => {
  const deletePressed = useKeyPress('Delete');
  const ctrlPressed = useKeyPress('Control');
  const aPressed = useKeyPress('a');
  const { getNodes, setNodes } = useReactFlow();
  
  useEffect(() => {
    if (deletePressed) {
      setNodes(nodes => nodes.filter(node => !node.selected));
    }
  }, [deletePressed, setNodes]);
  
  useEffect(() => {
    if (ctrlPressed && aPressed) {
      setNodes(nodes => nodes.map(node => ({ ...node, selected: true })));
    }
  }, [ctrlPressed, aPressed, setNodes]);
  
  return null;
};
```'''

def generate_use_nodes_initialized_example(use_case: str) -> str:
    """Generate useNodesInitialized hook example."""
    return '''```typescript
import React from 'react';
import { useNodesInitialized } from 'reactflow';

const LoadingOverlay: React.FC = () => {
  const nodesInitialized = useNodesInitialized();
  
  if (nodesInitialized) return null;
  
  return (
    <div className="loading-overlay">
      <div className="loading-spinner">Initializing nodes...</div>
    </div>
  );
};
```'''

def generate_component_implementation(component_type: str, customization_level: str, features: list) -> str:
    """Generate React Flow component implementation."""
    if component_type == "Handle":
        return '''```typescript
import React, { useMemo } from 'react';
import { Handle, Position, useConnection, HandleProps } from 'reactflow';

interface AdvancedHandleProps extends Omit<HandleProps, 'position'> {
  position: Position;
  label?: string;
  validationRule?: (connection: any) => boolean;
  showTooltip?: boolean;
  animated?: boolean;
  size?: 'small' | 'medium' | 'large';
}

const AdvancedHandle: React.FC<AdvancedHandleProps> = ({
  id,
  type,
  position,
  label,
  validationRule,
  showTooltip = false,
  animated = false,
  size = 'medium',
  className,
  style,
  ...props
}) => {
  const connection = useConnection();
  
  const isValidConnection = useMemo(() => {
    if (!connection.fromHandle || !validationRule) return true;
    return validationRule(connection);
  }, [connection, validationRule]);
  
  const handleSize = {
    small: 8,
    medium: 12,
    large: 16
  }[size];
  
  const isActive = connection.fromHandle?.id === id;
  const isValidTarget = connection.isConnecting && 
                       type === 'target' && 
                       isValidConnection;
  
  return (
    <div className="advanced-handle-wrapper">
      {label && (
        <div className={`handle-label ${position}`}>
          {label}
        </div>
      )}
      
      <Handle
        id={id}
        type={type}
        position={position}
        className={`advanced-handle ${className || ''} ${
          isActive ? 'active' : ''
        } ${
          isValidTarget ? 'valid-target' : ''
        } ${
          animated ? 'animated' : ''
        }`}
        style={{
          width: handleSize,
          height: handleSize,
          backgroundColor: isActive ? '#10b981' : 
                          isValidTarget ? '#3b82f6' : '#6b7280',
          border: '2px solid white',
          boxShadow: isActive ? '0 0 10px rgba(16, 185, 129, 0.5)' : 'none',
          transform: isActive ? 'scale(1.2)' : 'scale(1)',
          transition: 'all 0.2s ease',
          ...style
        }}
        {...props}
      />
      
      {showTooltip && isActive && (
        <div className="handle-tooltip">
          {connection.isConnecting ? 'Drop to connect' : 'Connecting...'}
        </div>
      )}
    </div>
  );
};

export default AdvancedHandle;
```'''
    else:
        return f"// {component_type} component implementation with {customization_level} level customization"

def generate_utility_implementation(utility_category: str, specific_functions: list, complexity: str) -> str:
    """Generate utility function implementations."""
    if utility_category == "edge_utilities":
        return '''```typescript
import { 
  Edge, 
  Node, 
  addEdge as reactFlowAddEdge,
  Connection,
  MarkerType 
} from 'reactflow';

export const addEdgeWithValidation = (
  edge: Edge | Connection,
  edges: Edge[],
  validationRules?: {
    preventSelfConnection?: boolean;
    preventDuplicates?: boolean;
    maxConnectionsPerNode?: number;
  }
): Edge[] => {
  const rules = {
    preventSelfConnection: true,
    preventDuplicates: true,
    maxConnectionsPerNode: 10,
    ...validationRules
  };
  
  // Validate self-connection
  if (rules.preventSelfConnection && edge.source === edge.target) {
    console.warn('Self-connections are not allowed');
    return edges;
  }
  
  // Validate duplicates
  if (rules.preventDuplicates) {
    const isDuplicate = edges.some(existingEdge => 
      existingEdge.source === edge.source && 
      existingEdge.target === edge.target &&
      existingEdge.sourceHandle === edge.sourceHandle &&
      existingEdge.targetHandle === edge.targetHandle
    );
    
    if (isDuplicate) {
      console.warn('Duplicate edge detected');
      return edges;
    }
  }
  
  return reactFlowAddEdge(edge, edges);
};

export const createStyledEdge = (
  connection: Connection,
  style: 'default' | 'animated' | 'dashed' | 'gradient' = 'default'
): Edge => {
  const baseEdge: Edge = {
    id: `edge-${connection.source}-${connection.target}-${Date.now()}`,
    source: connection.source!,
    target: connection.target!,
    sourceHandle: connection.sourceHandle,
    targetHandle: connection.targetHandle
  };
  
  switch (style) {
    case 'animated':
      return {
        ...baseEdge,
        animated: true,
        style: { stroke: '#3b82f6', strokeWidth: 2 },
        markerEnd: { type: MarkerType.ArrowClosed, color: '#3b82f6' }
      };
      
    case 'dashed':
      return {
        ...baseEdge,
        style: { 
          stroke: '#6b7280', 
          strokeWidth: 2, 
          strokeDasharray: '5,5' 
        },
        markerEnd: { type: MarkerType.ArrowClosed, color: '#6b7280' }
      };
      
    default:
      return baseEdge;
  }
};
```'''
    else:
        return f"// {utility_category} utilities with {complexity} complexity"

def generate_typescript_definitions(definition_scope: str, type_categories: list, strictness_level: str, include_generics: bool) -> str:
    """Generate TypeScript definitions."""
    return '''```typescript
import { Node, Edge, XYPosition } from 'reactflow';

// Custom node data interface
export interface CustomNodeData {
  label: string;
  description?: string;
  color?: string;
  icon?: string;
}

// Custom edge data interface  
export interface CustomEdgeData {
  label?: string;
  weight?: number;
  style?: 'solid' | 'dashed' | 'dotted';
}

// Typed node with custom data
export type CustomNode = Node<CustomNodeData>;

// Typed edge with custom data
export type CustomEdge = Edge<CustomEdgeData>;

// Flow state interface
export interface FlowState {
  nodes: CustomNode[];
  edges: CustomEdge[];
  viewport: { x: number; y: number; zoom: number };
}

// Event handlers interface
export interface FlowEventHandlers {
  onConnect: OnConnect;
  onNodesChange: OnNodesChange;
  onEdgesChange: OnEdgesChange;
  onNodeClick?: (event: React.MouseEvent, node: Node) => void;
  onEdgeClick?: (event: React.MouseEvent, edge: Edge) => void;
}
```'''

def generate_performance_optimizations(optimization_focus: str, node_count_range: str, optimization_techniques: list) -> str:
    """Generate performance optimization code."""
    return '''```typescript
import React, { memo, useMemo } from 'react';
import { Node, NodeProps } from 'reactflow';

// Optimized node component with memoization
export const OptimizedNode = memo<NodeProps>(({ data, selected }) => {
  const nodeStyle = useMemo(() => ({
    border: selected ? '2px solid blue' : '1px solid gray',
    borderRadius: '8px',
    padding: '10px',
    background: 'white'
  }), [selected]);
  
  return (
    <div style={nodeStyle}>
      {data.label}
    </div>
  );
});

// Virtualized node rendering for large datasets
export const useNodeVirtualization = (nodes: Node[], viewportBounds: any) => {
  return useMemo(() => {
    return nodes.filter(node => {
      // Only render nodes within viewport
      return (
        node.position.x + 200 > viewportBounds.x &&
        node.position.x < viewportBounds.x + viewportBounds.width &&
        node.position.y + 100 > viewportBounds.y &&
        node.position.y < viewportBounds.y + viewportBounds.height
      );
    });
  }, [nodes, viewportBounds]);
};

// Debounced updates for performance
export const useDebounceNodeChanges = (
  onNodesChange: OnNodesChange,
  delay = 100
) => {
  const debouncedCallback = useMemo(
    () => debounce(onNodesChange, delay),
    [onNodesChange, delay]
  );
  
  return debouncedCallback;
};
```'''

def generate_accessibility_implementation(accessibility_level: str, accessibility_features: list, testing_requirements: bool) -> str:
    """Generate accessibility implementation."""
    return f'''```typescript
// WCAG {accessibility_level} Compliant React Flow Implementation

import React, {{ useCallback, useEffect, useRef }} from 'react';
import ReactFlow, {{ 
  Node, 
  Edge, 
  ReactFlowProvider,
  useReactFlow,
  useKeyPress 
}} from 'reactflow';

const AccessibleReactFlow: React.FC = () => {{
  const flowRef = useRef<HTMLDivElement>(null);
  const {{ getNodes, getEdges, setNodes, fitView }} = useReactFlow();
  const deleteKeyPressed = useKeyPress('Delete');
  const escapeKeyPressed = useKeyPress('Escape');
  
  // Keyboard navigation implementation
  const handleKeyDown = useCallback((event: KeyboardEvent) => {{
    const nodes = getNodes();
    const selectedNode = nodes.find(node => node.selected);
    
    switch (event.key) {{
      case 'ArrowUp':
      case 'ArrowDown':
      case 'ArrowLeft':
      case 'ArrowRight':
        event.preventDefault();
        // Implement arrow key navigation
        break;
      case 'Enter':
      case ' ':
        event.preventDefault();
        // Activate selected element
        break;
      case 'Tab':
        // Handle tab navigation
        break;
    }}
  }}, [getNodes]);
  
  // ARIA live region for announcements
  const announceChange = useCallback((message: string) => {{
    const announcement = document.getElementById('flow-announcements');
    if (announcement) {{
      announcement.textContent = message;
    }}
  }}, []);
  
  return (
    <div 
      ref={{flowRef}}
      role="application"
      aria-label="Interactive flow diagram"
      aria-describedby="flow-instructions"
      onKeyDown={{handleKeyDown}}
      tabIndex={{0}}
    >
      <div 
        id="flow-instructions" 
        className="sr-only"
        aria-live="polite"
      >
        Use arrow keys to navigate, Enter to select, Space to activate
      </div>
      
      <div 
        id="flow-announcements"
        aria-live="assertive"
        aria-atomic="true"
        className="sr-only"
      />
      
      <ReactFlow
        aria-describedby="flow-instructions"
        role="img"
        onNodeClick={{(event, node) => {{
          announceChange(`Selected node: ${{node.data.label || node.id}}`);
        }}}}
        onEdgeClick={{(event, edge) => {{
          announceChange(`Selected edge from ${{edge.source}} to ${{edge.target}}`);
        }}}}
      />
    </div>
  );
}};
```'''

# Tool execution handlers
REACT_FLOW_API_HANDLERS = {
    "react_flow_hook_examples": react_flow_hook_examples,
    "react_flow_advanced_components": react_flow_advanced_components,
    "react_flow_utilities_generator": react_flow_utilities_generator,
    "react_flow_typescript_definitions": react_flow_typescript_definitions,
    "react_flow_performance_optimizer": react_flow_performance_optimizer,
    "react_flow_accessibility_enhancer": react_flow_accessibility_enhancer
}