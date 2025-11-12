"""
Connection-Aware Positioning Tools for React Flow - Codex Integration
Specialized tools for ensuring nodes are placed on the correct connection side.
"""

from typing import Any, Dict, List
from mcp import types

def get_tools() -> List[types.Tool]:
    """Get connection-aware positioning tools for Codex."""
    return [
        types.Tool(
            name="generate_connection_aware_node",
            description="Generate React Flow node placement code that positions nodes on the correct connection side",
            inputSchema={
                "type": "object",
                "properties": {
                    "connection_side": {
                        "type": "string",
                        "enum": ["right", "left", "top", "bottom"],
                        "description": "Side where the connection originates from the source node"
                    },
                    "layout_style": {
                        "type": "string",
                        "enum": ["whiteboard", "hierarchical", "organic", "tree"],
                        "description": "Overall layout style for the flow diagram"
                    },
                    "spacing_config": {
                        "type": "object",
                        "properties": {
                            "horizontal": {"type": "number", "default": 200},
                            "vertical": {"type": "number", "default": 150},
                            "margin": {"type": "number", "default": 20}
                        },
                        "description": "Spacing configuration for node placement"
                    },
                    "auto_layout": {
                        "type": "boolean", 
                        "description": "Apply automatic layout after node creation"
                    }
                },
                "required": ["connection_side", "layout_style"]
            }
        ),
        
        types.Tool(
            name="codex_positioning_prompts",
            description="Generate specific prompts for instructing Codex on connection-aware positioning",
            inputSchema={
                "type": "object",
                "properties": {
                    "scenario": {
                        "type": "string",
                        "enum": [
                            "new_node_creation", "workflow_building", "decision_tree", 
                            "whiteboard_brainstorming", "process_flow", "mindmap"
                        ],
                        "description": "Specific scenario for node positioning"
                    },
                    "complexity_level": {
                        "type": "string",
                        "enum": ["basic", "intermediate", "advanced"],
                        "description": "Complexity level for the positioning logic"
                    }
                },
                "required": ["scenario"]
            }
        ),
        
        types.Tool(
            name="dagre_configuration_optimizer",
            description="Generate optimized Dagre layout configurations for connection-aware positioning",
            inputSchema={
                "type": "object",
                "properties": {
                    "flow_direction": {
                        "type": "string",
                        "enum": ["TB", "BT", "LR", "RL"],
                        "description": "Primary flow direction (Top-Bottom, Bottom-Top, Left-Right, Right-Left)"
                    },
                    "node_count": {
                        "type": "string", 
                        "enum": ["small_1_10", "medium_10_50", "large_50_100", "xlarge_100_plus"],
                        "description": "Expected number of nodes for optimization"
                    },
                    "connection_density": {
                        "type": "string",
                        "enum": ["sparse", "moderate", "dense"],
                        "description": "Expected connection density between nodes"
                    }
                },
                "required": ["flow_direction"]
            }
        ),
        
        types.Tool(
            name="handle_positioning_guide",
            description="Generate handle positioning configurations for optimal connection-side placement",
            inputSchema={
                "type": "object",
                "properties": {
                    "node_type": {
                        "type": "string",
                        "enum": ["input", "output", "process", "decision", "connector", "custom"],
                        "description": "Type of node for handle configuration"
                    },
                    "connection_pattern": {
                        "type": "string",
                        "enum": ["linear", "branching", "converging", "bidirectional"],
                        "description": "Expected connection pattern"
                    },
                    "visual_style": {
                        "type": "string",
                        "enum": ["minimal", "styled", "animated", "professional"],
                        "description": "Visual style for handles"
                    }
                },
                "required": ["node_type", "connection_pattern"]
            }
        ),

        types.Tool(
            name="whiteboard_layout_optimizer",
            description="Generate whiteboard-optimized layout configurations for natural node placement",
            inputSchema={
                "type": "object",
                "properties": {
                    "whiteboard_size": {
                        "type": "string",
                        "enum": ["compact_800x600", "standard_1200x800", "large_1600x1200", "xlarge_2000x1500"],
                        "description": "Target whiteboard dimensions"
                    },
                    "content_type": {
                        "type": "string",
                        "enum": ["brainstorming", "process_mapping", "system_design", "workflow_creation"],
                        "description": "Type of content being created"
                    },
                    "collaboration_mode": {
                        "type": "boolean", 
                        "description": "Whether this is for collaborative editing"
                    }
                },
                "required": ["whiteboard_size", "content_type"]
            }
        )
    ]

def generate_connection_aware_node(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate connection-aware node positioning code."""
    connection_side = arguments.get("connection_side")
    layout_style = arguments.get("layout_style")
    spacing = arguments.get("spacing_config", {"horizontal": 200, "vertical": 150, "margin": 20})
    auto_layout = arguments.get("auto_layout", True)
    
    # Generate positioning algorithm
    positioning_code = f"""```typescript
// Connection-Aware Node Positioning for {connection_side.title()} Side
import dagre from 'dagre';
import {{ Node, Edge, Position }} from 'reactflow';

interface PositioningConfig {{
  horizontal: number;
  vertical: number;
  margin: number;
}}

const SPACING_CONFIG: PositioningConfig = {{
  horizontal: {spacing['horizontal']},
  vertical: {spacing['vertical']},  
  margin: {spacing['margin']}
}};

// Calculate position based on connection side
const getConnectionAwarePosition = (
  sourceNode: Node,
  connectionSide: '{connection_side}',
  customSpacing?: Partial<PositioningConfig>
): {{ x: number; y: number }} => {{
  const spacing = {{ ...SPACING_CONFIG, ...customSpacing }};
  
  const sideOffsets = {{
    'right': {{ x: spacing.horizontal, y: 0 }},
    'left': {{ x: -spacing.horizontal, y: 0 }},
    'bottom': {{ x: 0, y: spacing.vertical }},
    'top': {{ x: 0, y: -spacing.vertical }}
  }};
  
  const offset = sideOffsets[connectionSide] || sideOffsets['right'];
  
  return {{
    x: sourceNode.position.x + offset.x,
    y: sourceNode.position.y + offset.y
  }};
}};

// Generate new node with connection-aware positioning
const generateConnectedNode = (
  sourceNodeId: string,
  sourceHandleSide: '{connection_side}',
  nodeData: any,
  nodes: Node[],
  edges: Edge[]
): {{ newNode: Node; newEdge: Edge }} => {{
  const sourceNode = nodes.find(n => n.id === sourceNodeId);
  if (!sourceNode) {{
    throw new Error(`Source node ${{sourceNodeId}} not found`);
  }}
  
  // Calculate optimal position
  const position = getConnectionAwarePosition(sourceNode, sourceHandleSide);
  
  // Create new node
  const newNode: Node = {{
    id: `node-${{Date.now()}}-${{Math.random().toString(36).substr(2, 9)}}`,
    type: 'default',
    position,
    data: nodeData,
    width: 172,
    height: 36
  }};
  
  // Create connecting edge
  const newEdge: Edge = {{
    id: `edge-${{sourceNodeId}}-${{newNode.id}}`,
    source: sourceNodeId,
    sourceHandle: `source-{connection_side}`,
    target: newNode.id,
    targetHandle: 'target-{get_opposite_side(connection_side)}',
    animated: false,
    type: 'default'
  }};
  
  return {{ newNode, newEdge }};
}};

// {layout_style.title()} Layout Configuration
const get{layout_style.title()}Layout = (nodes: Node[], edges: Edge[]): {{ nodes: Node[]; edges: Edge[] }} => {{
  const g = new dagre.graphlib.Graph();
  g.setDefaultEdgeLabel(() => ({{}}));
  
  // Configure for {layout_style} layout
  g.setGraph({{
    rankdir: '{get_rankdir_for_style(layout_style)}',
    nodesep: SPACING_CONFIG.horizontal * 0.5,
    ranksep: SPACING_CONFIG.vertical,
    marginx: SPACING_CONFIG.margin,
    marginy: SPACING_CONFIG.margin
  }});

  nodes.forEach((node) => {{
    g.setNode(node.id, {{ 
      width: node.width || 172, 
      height: node.height || 36 
    }});
  }});

  edges.forEach((edge) => {{
    g.setEdge(edge.source, edge.target);
  }});

  dagre.layout(g);

  const layoutedNodes = nodes.map((node) => {{
    const nodeWithPosition = g.node(node.id);
    return {{
      ...node,
      position: {{
        x: nodeWithPosition.x - (node.width || 172) / 2,
        y: nodeWithPosition.y - (node.height || 36) / 2,
      }},
    }};
  }});

  return {{ nodes: layoutedNodes, edges }};
}};

// Usage in React Flow component
const useConnectionAwareNodeCreation = () => {{
  const [nodes, setNodes] = useNodesState([]);
  const [edges, setEdges] = useEdgesState([]);
  
  const addConnectedNode = useCallback((
    sourceNodeId: string,
    nodeData: any,
    connectionSide: '{connection_side}' = '{connection_side}'
  ) => {{
    const {{ newNode, newEdge }} = generateConnectedNode(
      sourceNodeId,
      connectionSide,
      nodeData,
      nodes,
      edges
    );
    
    const updatedNodes = [...nodes, newNode];
    const updatedEdges = [...edges, newEdge];
    
    {'// Apply automatic layout' if auto_layout else '// Manual positioning (auto-layout disabled)'}
    {f'const {{ nodes: layoutedNodes, edges: layoutedEdges }} = get{layout_style.title()}Layout(updatedNodes, updatedEdges);' if auto_layout else ''}
    {f'setNodes(layoutedNodes);' if auto_layout else 'setNodes(updatedNodes);'}
    {f'setEdges(layoutedEdges);' if auto_layout else 'setEdges(updatedEdges);'}
  }}, [nodes, edges, setNodes, setEdges]);
  
  return {{ addConnectedNode }};
}};

export {{ 
  getConnectionAwarePosition,
  generateConnectedNode,
  get{layout_style.title()}Layout,
  useConnectionAwareNodeCreation
}};
```

## Key Features:
- ✅ Automatic positioning based on connection side ({connection_side})
- ✅ Optimized for {layout_style} layout style  
- ✅ Configurable spacing: {spacing['horizontal']}px horizontal, {spacing['vertical']}px vertical
- ✅ {'Automatic layout application' if auto_layout else 'Manual positioning control'}
- ✅ TypeScript support with proper interfaces
- ✅ Error handling and validation

## Usage Example:
```typescript
// Add a node connected to the {connection_side} side
const {{ addConnectedNode }} = useConnectionAwareNodeCreation();

addConnectedNode('existing-node-id', {{
  label: 'New Connected Node',
  description: 'Placed on {connection_side} side'
}});
```"""
    
    return [types.TextContent(
        type="text",
        text=positioning_code
    )]

def codex_positioning_prompts(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate Codex-specific prompts for positioning."""
    scenario = arguments.get("scenario")
    complexity_level = arguments.get("complexity_level", "intermediate")
    
    prompts = generate_scenario_prompts(scenario, complexity_level)
    
    return [types.TextContent(
        type="text",
        text=f"""# Codex Positioning Prompts for {scenario.replace('_', ' ').title()}

## Complexity Level: {complexity_level.title()}

{prompts}

### General Codex Instructions:
When working with React Flow node positioning, always:
1. Check the source node's handle position before creating new nodes
2. Use connection-aware positioning functions
3. Apply consistent spacing based on connection side
4. Consider the overall layout pattern (whiteboard, hierarchical, etc.)
5. Test positioning with different screen sizes and zoom levels

### Debugging Prompts:
- "Show me the current node positions and their connection relationships"
- "Validate that new nodes are positioned correctly relative to their source"
- "Check if the layout algorithm is maintaining proper spacing"
- "Ensure handles are positioned for optimal connection flow"

### Best Practices for Codex:
- Always specify the connection side in positioning functions
- Use semantic variable names that indicate positioning intent
- Include spacing configurations as constants for easy adjustment
- Implement fallback positioning for edge cases
- Test with both manual and automatic layout scenarios
"""
    )]

def dagre_configuration_optimizer(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate optimized Dagre configurations."""
    flow_direction = arguments.get("flow_direction")
    node_count = arguments.get("node_count", "medium_10_50")
    connection_density = arguments.get("connection_density", "moderate")
    
    config = generate_dagre_config(flow_direction, node_count, connection_density)
    
    return [types.TextContent(
        type="text",
        text=f"""# Optimized Dagre Configuration

## Flow Direction: {flow_direction}
## Node Count: {node_count.replace('_', ' ').title()}
## Connection Density: {connection_density.title()}

{config}

### Performance Considerations:
- Node count range affects layout calculation time
- Dense connections may require larger spacing
- Consider viewport culling for large graphs
- Use React.memo for node components in large layouts

### Configuration Tuning:
- Adjust nodesep for horizontal spacing between nodes
- Modify ranksep for vertical spacing between levels  
- Use marginx/marginy for overall layout padding
- Test with different rankdir values for optimal flow
"""
    )]

def handle_positioning_guide(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate handle positioning configurations."""
    node_type = arguments.get("node_type")
    connection_pattern = arguments.get("connection_pattern") 
    visual_style = arguments.get("visual_style", "minimal")
    
    guide = generate_handle_guide(node_type, connection_pattern, visual_style)
    
    return [types.TextContent(
        type="text",
        text=f"""# Handle Positioning Guide

## Node Type: {node_type.title()}
## Connection Pattern: {connection_pattern.replace('_', ' ').title()}
## Visual Style: {visual_style.title()}

{guide}

### Handle Best Practices:
- Position handles based on expected connection flow
- Use consistent handle sizing across node types
- Implement visual feedback for connection states
- Consider accessibility for handle interaction
- Test handle positioning with different node sizes

### Integration with Positioning:
- Handles determine connection sides for new node placement
- Handle IDs should indicate their purpose and position
- Use handle validation to enforce proper connections
- Implement smart handle highlighting during connections
"""
    )]

def whiteboard_layout_optimizer(arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Generate whiteboard-optimized configurations."""
    whiteboard_size = arguments.get("whiteboard_size")
    content_type = arguments.get("content_type")
    collaboration_mode = arguments.get("collaboration_mode", False)
    
    optimizer = generate_whiteboard_config(whiteboard_size, content_type, collaboration_mode)
    
    return [types.TextContent(
        type="text",
        text=f"""# Whiteboard Layout Optimizer

## Size: {whiteboard_size.replace('_', ' ').title()}
## Content Type: {content_type.replace('_', ' ').title()}
## Collaboration: {'Enabled' if collaboration_mode else 'Disabled'}

{optimizer}

### Whiteboard Considerations:
- Larger canvas allows for more organic positioning
- Collaborative mode requires real-time position synchronization
- Consider touch device interaction for handle positioning
- Implement smart zoom-to-fit for different content types
- Use minimap for navigation on large whiteboards

### Performance Optimization:
- Implement viewport culling for large whiteboards
- Use node virtualization for 100+ nodes
- Debounce layout calculations during rapid changes
- Cache layout results for common configurations
"""
    )]

# Helper functions
def get_opposite_side(side: str) -> str:
    """Get the opposite side for target handle positioning."""
    opposites = {
        'right': 'left',
        'left': 'right', 
        'top': 'bottom',
        'bottom': 'top'
    }
    return opposites.get(side, 'left')

def get_rankdir_for_style(style: str) -> str:
    """Get optimal rankdir for layout style.""" 
    style_configs = {
        'whiteboard': 'LR',  # Left-to-right for natural flow
        'hierarchical': 'TB',  # Top-to-bottom for hierarchy
        'organic': 'TB',       # Top-to-bottom as base
        'tree': 'TB'          # Top-to-bottom for tree structure
    }
    return style_configs.get(style, 'LR')

def generate_scenario_prompts(scenario: str, complexity: str) -> str:
    """Generate scenario-specific prompts."""
    if scenario == "new_node_creation":
        return f"""### Primary Prompts:
```
"Create a new node connected to the {'{connection_side}'} side of node {'{node_id}'}"
"Generate a connected node positioned {'{spacing}'}px to the {'{direction}'} of the source"
"Add a new node that connects from the {'{handle_id}'} handle with proper spacing"
```

### Advanced Prompts ({complexity} level):
```
"Create a node with connection-aware positioning and apply dagre layout"
"Generate a new node that maintains whiteboard flow patterns"
"Position the new node optimally based on the source handle location"
```"""
    elif scenario == "workflow_building":
        return """### Workflow-Specific Prompts:
```
"Add the next step in the workflow, positioned to the right of the current step"
"Create a parallel process branch extending downward from the decision node"
"Generate a workflow node that maintains the process flow direction"
```"""
    else:
        return f"# Prompts for {scenario.replace('_', ' ').title()} scenario"

def generate_dagre_config(direction: str, node_count: str, density: str) -> str:
    """Generate optimized Dagre configuration."""
    # Determine spacing based on parameters
    spacing_map = {
        "small_1_10": {"nodesep": 50, "ranksep": 80},
        "medium_10_50": {"nodesep": 75, "ranksep": 120},
        "large_50_100": {"nodesep": 100, "ranksep": 150},
        "xlarge_100_plus": {"nodesep": 120, "ranksep": 180}
    }
    
    density_multiplier = {
        "sparse": 1.0,
        "moderate": 1.2,
        "dense": 1.5
    }
    
    base_spacing = spacing_map.get(node_count, {"nodesep": 75, "ranksep": 120})
    multiplier = density_multiplier.get(density, 1.0)
    
    return f"""```typescript
// Optimized Dagre Configuration for {direction} flow
const dagreConfig = {{
  rankdir: '{direction}',
  nodesep: {int(base_spacing['nodesep'] * multiplier)},
  ranksep: {int(base_spacing['ranksep'] * multiplier)},
  marginx: 20,
  marginy: 20,
  
  // Performance optimizations for {node_count}
  {generate_performance_config(node_count)}
}};

// Apply configuration
g.setGraph(dagreConfig);
```"""

def generate_performance_config(node_count: str) -> str:
    """Generate performance-specific configuration."""
    if "xlarge" in node_count:
        return """// Large graph optimizations
  acyclicer: 'greedy',
  ranker: 'tight-tree'"""
    else:
        return """// Standard performance settings
  acyclicer: undefined,
  ranker: 'network-simplex'"""

def generate_handle_guide(node_type: str, pattern: str, style: str) -> str:
    """Generate handle positioning guide."""
    return f"""```typescript
// {node_type.title()} Node Handle Configuration for {pattern.title()} Pattern
import {{ Handle, Position }} from 'reactflow';

const {node_type.title()}Node = ({{ data, id }}) => {{
  return (
    <div className="{node_type}-node">
      {generate_handle_jsx(node_type, pattern, style)}
      <div className="node-content">{{data.label}}</div>
    </div>
  );
}};
```"""

def generate_handle_jsx(node_type: str, pattern: str, style: str) -> str:
    """Generate JSX for handles based on configuration."""
    if pattern == "linear":
        return """
      <Handle type="target" position={Position.Left} id="input" />
      <Handle type="source" position={Position.Right} id="output" />"""
    elif pattern == "branching":
        return """
      <Handle type="target" position={Position.Left} id="input" />
      <Handle type="source" position={Position.Right} id="primary" />
      <Handle type="source" position={Position.Bottom} id="secondary" />"""
    else:
        return f"\n      {{/* Handles for {pattern} pattern */}}"

def generate_whiteboard_config(size: str, content_type: str, collaboration: bool) -> str:
    """Generate whiteboard-specific configuration."""
    dimensions = {
        "compact_800x600": {"width": 800, "height": 600},
        "standard_1200x800": {"width": 1200, "height": 800}, 
        "large_1600x1200": {"width": 1600, "height": 1200},
        "xlarge_2000x1500": {"width": 2000, "height": 1500}
    }
    
    dims = dimensions.get(size, {"width": 1200, "height": 800})
    
    return f"""```typescript
// Whiteboard Configuration for {content_type.replace('_', ' ').title()}
const whiteboardConfig = {{
  dimensions: {{
    width: {dims['width']},
    height: {dims['height']}
  }},
  
  // Content-optimized settings
  nodeSpacing: {get_content_spacing(content_type)},
  fitViewPadding: 0.1,
  
  // {'Collaboration features' if collaboration else 'Single-user mode'}
  {generate_collaboration_config(collaboration)}
  
  // Layout preferences for {content_type}
  defaultDirection: '{get_content_direction(content_type)}',
  allowFreePositioning: true,
  snapToGrid: false
}};
```"""

def get_content_spacing(content_type: str) -> int:
    """Get spacing optimized for content type.""" 
    spacing_map = {
        "brainstorming": 150,
        "process_mapping": 200,
        "system_design": 250,
        "workflow_creation": 180
    }
    return spacing_map.get(content_type, 200)

def get_content_direction(content_type: str) -> str:
    """Get optimal direction for content type."""
    direction_map = {
        "brainstorming": "LR",
        "process_mapping": "TB", 
        "system_design": "LR",
        "workflow_creation": "TB"
    }
    return direction_map.get(content_type, "LR")

def generate_collaboration_config(collaboration: bool) -> str:
    """Generate collaboration-specific configuration."""
    if collaboration:
        return """realTimeSync: true,
  cursorSharing: true,
  conflictResolution: 'last-write-wins',"""
    else:
        return """realTimeSync: false,
  localStoragePersistence: true,"""

# Tool execution handlers
CONNECTION_POSITIONING_HANDLERS = {
    "generate_connection_aware_node": generate_connection_aware_node,
    "codex_positioning_prompts": codex_positioning_prompts,
    "dagre_configuration_optimizer": dagre_configuration_optimizer,
    "handle_positioning_guide": handle_positioning_guide,
    "whiteboard_layout_optimizer": whiteboard_layout_optimizer
}

async def handle_call(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Handle connection positioning tool calls."""
    if name in CONNECTION_POSITIONING_HANDLERS:
        return CONNECTION_POSITIONING_HANDLERS[name](arguments)
    
    return [types.TextContent(
        type="text",
        text=f"Tool {name} not found in connection positioning tools"
    )]