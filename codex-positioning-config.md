# Codex Configuration for Connection-Side Node Placement

## Overview
Configure Codex to automatically place new nodes on the appropriate side where connections are made in React Flow whiteboards.

## Core Configuration Strategy

### 1. Connection-Aware Positioning Algorithm

```typescript
// Enhanced node positioning based on connection side
const getConnectionAwarePosition = (
  sourceNode: Node,
  sourceHandle: string,
  targetPosition?: 'left' | 'right' | 'top' | 'bottom'
) => {
  const handlePositions = {
    'source-right': { side: 'right', offset: { x: 200, y: 0 } },
    'source-left': { side: 'left', offset: { x: -200, y: 0 } },
    'source-top': { side: 'top', offset: { x: 0, y: -150 } },
    'source-bottom': { side: 'bottom', offset: { x: 0, y: 150 } }
  };
  
  const handleConfig = handlePositions[sourceHandle] || handlePositions['source-right'];
  
  return {
    x: sourceNode.position.x + handleConfig.offset.x,
    y: sourceNode.position.y + handleConfig.offset.y
  };
};

// Automatic layout with connection awareness
const getLayoutedElements = (nodes, edges, direction = 'TB') => {
  const g = new dagre.graphlib.Graph();
  g.setDefaultEdgeLabel(() => ({}));
  
  // Configure for connection-side placement
  g.setGraph({ 
    rankdir: direction,
    nodesep: 100,        // Space between nodes on same level
    ranksep: 150,        // Space between levels
    marginx: 20,         // Horizontal margin
    marginy: 20          // Vertical margin
  });

  nodes.forEach((node) => {
    g.setNode(node.id, { 
      width: node.width || 172, 
      height: node.height || 36 
    });
  });

  edges.forEach((edge) => {
    g.setEdge(edge.source, edge.target);
  });

  dagre.layout(g);

  const layoutedNodes = nodes.map((node) => {
    const nodeWithPosition = g.node(node.id);
    return {
      ...node,
      position: {
        x: nodeWithPosition.x - (node.width || 172) / 2,
        y: nodeWithPosition.y - (node.height || 36) / 2,
      },
    };
  });

  return { nodes: layoutedNodes, edges };
};
```

### 2. Codex Prompt Engineering

When instructing Codex to generate nodes, use these specific prompts:

```
When creating new nodes in React Flow:
1. Always check the source node's handle position
2. Place new nodes on the connection side (right for source-right handles, left for source-left handles)
3. Use the getConnectionAwarePosition function to calculate placement
4. Maintain consistent spacing: 200px horizontally, 150px vertically
5. For whiteboard layouts, prefer right-side placement for logical flow
6. Apply dagre layout with rankdir='LR' for left-to-right flow
```

### 3. Handle Configuration for Connection Sides

```typescript
// Define handles with explicit positioning
const ConnectionAwareNode = ({ data, id }) => {
  return (
    <div className="react-flow-node">
      <Handle
        type="target"
        position={Position.Left}
        id="target-left"
        style={{ left: -8 }}
      />
      
      <Handle
        type="source"
        position={Position.Right}
        id="source-right"
        style={{ right: -8 }}
      />
      
      <Handle
        type="source"
        position={Position.Bottom}
        id="source-bottom"
        style={{ bottom: -8 }}
      />
      
      <div>{data.label}</div>
    </div>
  );
};
```

### 4. Automatic Node Generation Workflow

```typescript
const generateConnectedNode = (
  sourceNodeId: string,
  sourceHandle: string,
  newNodeData: any
) => {
  const sourceNode = getNode(sourceNodeId);
  if (!sourceNode) return;
  
  // Calculate position based on connection side
  const newPosition = getConnectionAwarePosition(sourceNode, sourceHandle);
  
  // Create new node
  const newNode = {
    id: `node-${Date.now()}`,
    type: 'connectionAwareNode',
    position: newPosition,
    data: newNodeData
  };
  
  // Create connecting edge
  const newEdge = {
    id: `edge-${sourceNodeId}-${newNode.id}`,
    source: sourceNodeId,
    sourceHandle: sourceHandle,
    target: newNode.id,
    targetHandle: 'target-left'
  };
  
  // Add to flow
  setNodes(nodes => [...nodes, newNode]);
  setEdges(edges => [...edges, newEdge]);
  
  // Apply layout
  const { nodes: layoutedNodes, edges: layoutedEdges } = getLayoutedElements(
    [...nodes, newNode],
    [...edges, newEdge],
    'LR' // Left-to-right for whiteboard flow
  );
  
  setNodes(layoutedNodes);
  setEdges(layoutedEdges);
};
```

## Codex Integration Instructions

### VS Code Settings Configuration

Add this to your VS Code settings for Codex integration:

```json
{
  "github.copilot.enable": true,
  "github.copilot.suggestions.enabled": true,
  "github.copilot.chat.followUps": "on",
  "github.copilot.chat.useProjectTemplates": true,
  "codeium.enableConfig": {
    "reactflow": {
      "nodePositioning": "connection-aware",
      "defaultLayout": "dagre",
      "layoutDirection": "LR",
      "spacing": {
        "horizontal": 200,
        "vertical": 150
      }
    }
  }
}
```

### Project-Level Configuration

Create a `.copilot-instructions.md` file in your project root:

```markdown
# React Flow Node Positioning Rules

When generating or placing nodes in React Flow:

1. **Connection-Side Placement**: Always place new nodes on the side where the connection originates
   - Right handle → place node to the right (+200px x-axis)
   - Left handle → place node to the left (-200px x-axis)  
   - Bottom handle → place node below (+150px y-axis)
   - Top handle → place node above (-150px y-axis)

2. **Layout Algorithm**: Use Dagre with left-to-right (LR) direction for whiteboard flows

3. **Spacing Standards**:
   - Horizontal: 200px between connected nodes
   - Vertical: 150px between levels
   - Margin: 20px around entire layout

4. **Auto-Layout Trigger**: Apply layout algorithm after adding new nodes to maintain organization

5. **Handle Positioning**: Use Position.Right for source handles, Position.Left for target handles
```

## Implementation Checklist

- [ ] Install dagre: `npm install dagre @types/dagre`
- [ ] Configure connection-aware positioning function
- [ ] Set up handle-specific node placement
- [ ] Implement auto-layout on node creation
- [ ] Add project-level Codex instructions
- [ ] Test with different connection scenarios
- [ ] Optimize for whiteboard-style layouts

## Example Usage Prompts for Codex

Use these specific prompts when working with Codex:

```
"Create a new node connected to the right side of the selected node, positioned 200px to the right"

"Generate a workflow node that connects from the bottom handle, placing it 150px below with proper spacing"

"Add a decision node to the right side of the current node and apply dagre layout with LR direction"

"When I connect nodes, ensure the new node is placed on the connection side with proper whiteboard spacing"
```

This configuration ensures that Codex will consistently place nodes on the correct side where connections are made, maintaining clean whiteboard layouts.