# Codex Connection-Side Node Placement Configuration

## Quick Start Instructions

To configure Codex to place nodes on the correct connection side in React Flow whiteboards:

### 1. Copy this prompt to your chat/conversation with Codex:

```
When creating new nodes in React Flow, ensure that:

1. New nodes are ALWAYS placed on the side where the connection originates
2. Use these specific positioning rules:
   - Right handle connection → place new node +200px to the right
   - Left handle connection → place new node -200px to the left  
   - Bottom handle connection → place new node +150px below
   - Top handle connection → place new node -150px above

3. Apply the following layout configuration:
   - Use Dagre with 'LR' (left-to-right) direction for whiteboard flows
   - Node spacing: 200px horizontal, 150px vertical
   - Apply auto-layout after creating nodes

4. Use this connection-aware positioning function:
```typescript
const getConnectionAwarePosition = (sourceNode, connectionSide) => {
  const spacing = { horizontal: 200, vertical: 150 };
  const sideOffsets = {
    'right': { x: spacing.horizontal, y: 0 },
    'left': { x: -spacing.horizontal, y: 0 },
    'bottom': { x: 0, y: spacing.vertical },
    'top': { x: 0, y: -spacing.vertical }
  };
  const offset = sideOffsets[connectionSide] || sideOffsets['right'];
  return {
    x: sourceNode.position.x + offset.x,
    y: sourceNode.position.y + offset.y
  };
};
```

Remember: The whiteboard should ALWAYS place new nodes on the correct connection side automatically.
```

### 2. For project-specific configuration, add this to your project README or docs:

```markdown
# React Flow Node Positioning Rules

When Codex generates React Flow code:
- Always use connection-aware positioning
- Default to right-side placement for new nodes
- Apply Dagre layout with LR direction
- Maintain 200px horizontal, 150px vertical spacing
- Auto-layout after node creation
```

### 3. Test with these example prompts:

```
"Create a new workflow node connected to the right side of the current node"
"Add a decision node positioned correctly based on the connection side"
"Generate a new node that connects from the bottom handle with proper whiteboard spacing"
```

## Advanced Configuration

For more complex scenarios, use the MCP server tools:

```bash
# Get connection-aware positioning code
docker run --rm frontend-mcp-server python -c "
from frontend_mcp_server.tools.connection_positioning_tools import generate_connection_aware_node
result = generate_connection_aware_node({
    'connection_side': 'right',
    'layout_style': 'whiteboard'
})
print(result[0].text)
"
```

## Key Points for Codex

1. **Always specify connection side**: "connected to the right side"
2. **Use spacing constants**: 200px horizontal, 150px vertical  
3. **Apply auto-layout**: Use dagre with 'LR' direction
4. **Handle positioning**: Right handles → right placement, etc.
5. **Whiteboard optimization**: Prefer left-to-right flow patterns

This ensures consistent, predictable node placement that maintains clean whiteboard layouts.