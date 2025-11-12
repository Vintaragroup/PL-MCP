"""
React Flow Learning Tools - Based on official /learn documentation
Provides comprehensive tutorials, patterns, and expert guidance
"""
import json
from typing import List, Dict, Any

# LAYOUTING MASTERY TOOLS
def react_flow_layouting_expert(requirement: str = "dagre", use_case: str = "hierarchical tree") -> Dict[str, Any]:
    """
    Expert guidance on React Flow layouting using Dagre, D3-Hierarchy, D3-Force, and ELK
    Based on https://reactflow.dev/learn/layouting/layouting
    """
    
    layouting_systems = {
        "dagre": {
            "description": "Simple library for layouting directed graphs. Minimal configuration, focus on speed over optimal layout.",
            "best_for": ["Tree layouts", "Hierarchical flows", "Quick setup", "Speed over precision"],
            "limitations": ["Sub-flow issues with external connections", "Same dimensions for all nodes"],
            "implementation": """
import dagre from 'dagre';

const getLayoutedElements = (nodes, edges, direction = 'TB') => {
  const g = new dagre.graphlib.Graph();
  g.setDefaultEdgeLabel(() => ({}));
  g.setGraph({ rankdir: direction });

  nodes.forEach((node) => {
    g.setNode(node.id, { width: nodeWidth, height: nodeHeight });
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
        x: nodeWithPosition.x - nodeWidth / 2,
        y: nodeWithPosition.y - nodeHeight / 2,
      },
    };
  });

  return { nodes: layoutedNodes, edges };
};""",
            "config_options": {
                "rankdir": "TB (top-bottom), LR (left-right), BT (bottom-top), RL (right-left)",
                "nodesep": "Number of pixels between nodes",
                "ranksep": "Number of pixels between ranks"
            }
        },
        
        "d3-hierarchy": {
            "description": "Perfect for tree structures with single root. Provides tree maps, partition layouts, enclosure diagrams.",
            "best_for": ["Single root trees", "Tree maps", "Partition layouts", "Enclosure diagrams"],
            "limitations": ["Requires single root", "Same width/height for all nodes", "Tree structures only"],
            "implementation": """
import { hierarchy, tree } from 'd3-hierarchy';

const getLayoutedElements = (nodes, edges) => {
  const data = stratify(nodes, edges);
  const root = hierarchy(data);
  
  const treeLayout = tree()
    .nodeSize([nodeWidth + 50, nodeHeight + 50]);
  
  const layoutRoot = treeLayout(root);
  
  const layoutedNodes = nodes.map(node => {
    const layoutNode = layoutRoot.descendants().find(d => d.data.id === node.id);
    return {
      ...node,
      position: { x: layoutNode.x, y: layoutNode.y }
    };
  });
  
  return { nodes: layoutedNodes, edges };
};""",
            "patterns": ["Tree", "Cluster", "Partition", "Pack", "Treemap"]
        },
        
        "d3-force": {
            "description": "Physics-based layouting with customizable forces. Iterative algorithm requiring multiple renders.",
            "best_for": ["Dynamic layouts", "Interactive flows", "Non-hierarchical structures", "Organic positioning"],
            "limitations": ["Complex configuration", "Performance intensive", "Requires simulation management"],
            "implementation": """
import { forceSimulation, forceLink, forceManyBody, forceCenter } from 'd3-force';

const useLayoutedElements = () => {
  const { getNodes, getEdges } = useReactFlow();
  const [nodes, , onNodesChange] = useNodesState(getNodes());
  
  const simulation = useRef(
    forceSimulation()
      .force('charge', forceManyBody().strength(-300))
      .force('link', forceLink().id(d => d.id).distance(100))
      .force('center', forceCenter(0, 0))
      .alphaTarget(0.05)
      .restart()
  );
  
  const tick = useCallback(() => {
    simulation.current.tick();
    onNodesChange(simulation.current.nodes().map(node => ({
      id: node.id,
      type: 'position',
      position: { x: node.x, y: node.y }
    })));
  }, [onNodesChange]);
  
  return { nodes, tick, simulation: simulation.current };
};""",
            "forces": {
                "charge": "Repulsion/attraction between nodes",
                "link": "Connection strength between linked nodes", 
                "center": "Pull towards center point",
                "collision": "Prevent node overlap",
                "x/y": "Position along specific axis"
            }
        },
        
        "elkjs": {
            "description": "Most configurable option. Java library ported to JavaScript with extensive options.",
            "best_for": ["Complex layouts", "Advanced configuration", "Multiple algorithms", "Production systems"],
            "limitations": ["High complexity", "Large bundle size", "Steep learning curve"],
            "implementation": """
import ELK from 'elkjs/lib/elk.bundled.js';

const elk = new ELK();

const useLayoutedElements = () => {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);
  
  const layout = useCallback(async (nodes, edges) => {
    const graph = {
      id: 'root',
      layoutOptions: {
        'elk.algorithm': 'layered',
        'elk.direction': 'RIGHT',
        'elk.spacing.nodeNode': '100',
        'elk.layered.spacing.nodeNodeBetweenLayers': '100'
      },
      children: nodes.map(node => ({
        id: node.id,
        width: 150,
        height: 50
      })),
      edges: edges.map(edge => ({
        id: edge.id,
        sources: [edge.source],
        targets: [edge.target]
      }))
    };
    
    const layoutedGraph = await elk.layout(graph);
    
    const layoutedNodes = nodes.map(node => {
      const layoutNode = layoutedGraph.children.find(n => n.id === node.id);
      return {
        ...node,
        position: { x: layoutNode.x, y: layoutNode.y }
      };
    });
    
    return { nodes: layoutedNodes, edges };
  }, []);
  
  return { layout };
};""",
            "algorithms": ["layered", "stress", "mrtree", "radial", "force", "disco"]
        }
    }
    
    selected_system = layouting_systems.get(requirement.lower(), layouting_systems["dagre"])
    
    return {
        "layouting_system": requirement,
        "recommendation": selected_system,
        "comparison_matrix": {
            "complexity": {"dagre": "Low", "d3-hierarchy": "Medium", "d3-force": "High", "elkjs": "Very High"},
            "bundle_size": {"dagre": "Small", "d3-hierarchy": "Small", "d3-force": "Medium", "elkjs": "Large"},
            "configurability": {"dagre": "Basic", "d3-hierarchy": "Limited", "d3-force": "High", "elkjs": "Extensive"},
            "performance": {"dagre": "Fast", "d3-hierarchy": "Fast", "d3-force": "Variable", "elkjs": "Good"}
        },
        "edge_routing_options": {
            "smart_edge": "react-flow-smart-edge for orthogonal routing",
            "custom_routing": "Manual path definition with editable edges",
            "libraries": ["react-flow-smart-edge", "Routing Orthogonal Diagram Connectors"]
        },
        "layout_tips": [
            "Test in playground: https://reactflow.dev/playground/layouting",
            "Start simple with Dagre for most use cases", 
            "Use D3-Force for organic, interactive layouts",
            "Choose ELK for complex production requirements",
            "Consider performance impact with large node counts"
        ]
    }

def react_flow_performance_mastery(scenario: str = "large_dataset", node_count: int = 1000) -> Dict[str, Any]:
    """
    Advanced performance optimization based on official React Flow performance guide
    Based on https://reactflow.dev/learn/advanced-use/performance
    """
    
    performance_strategies = {
        "memoization": {
            "component_memoization": """
// ✅ Memoize custom components to prevent unnecessary re-renders
const NodeComponent = memo(({ data }) => {
  return <div>{data.label}</div>;
});

// ✅ Define node types outside component to prevent re-creation
const nodeTypes = {
  custom: NodeComponent,
};

function MyFlow() {
  return <ReactFlow nodeTypes={nodeTypes} />;
}""",
            "function_memoization": """
// ✅ Memoize event handlers
const MyDiagram = () => {
  const onNodeClick = useCallback((event, node) => {
    console.log('Node clicked:', node);
  }, []);
  
  const onEdgeClick = useCallback((event, edge) => {
    console.log('Edge clicked:', edge);
  }, []);
  
  // ✅ Memoize objects and arrays
  const defaultEdgeOptions = useMemo(() => ({
    type: 'smoothstep',
    animated: true,
  }), []);
  
  const snapGrid = useMemo(() => [25, 25], []);
  
  return (
    <ReactFlow 
      onNodeClick={onNodeClick}
      onEdgeClick={onEdgeClick}
      defaultEdgeOptions={defaultEdgeOptions}
      snapToGrid={true}
      snapGrid={snapGrid}
    />
  );
};"""
        },
        
        "state_optimization": {
            "problem": """
// ❌ This causes unnecessary re-renders!
const SelectedNodeIds = () => {
  const nodes = useStore((state) => state.nodes);
  const selectedNodeIds = nodes.filter(node => node.selected).map(node => node.id);
  
  return (
    <div>
      {selectedNodeIds.map(id => <div key={id}>{id}</div>)}
    </div>
  );
};""",
            "solution": """
// ✅ Store selection state separately
const SelectedNodeIds = () => {
  const selectedNodeIds = useStore((state) => state.selectedNodeIds);
  
  return (
    <div>
      {selectedNodeIds.map(id => <div key={id}>{id}</div>)}
    </div>
  );
};

// ✅ Use specific selectors to avoid accessing entire nodes array
const useSelectedNodes = () => {
  return useStore(
    useCallback(
      (state) => state.nodes.filter((node) => node.selected),
      []
    ),
    shallow
  );
};"""
        },
        
        "tree_optimization": {
            "collapse_strategy": """
// ✅ Collapse large node trees for better performance
const handleNodeClick = (targetNode) => {
  if (targetNode.data.children) {
    setNodes(prevNodes =>
      prevNodes.map(node =>
        targetNode.data.children.includes(node.id)
          ? { ...node, hidden: !node.hidden }
          : node
      )
    );
  }
};

// ✅ Lazy loading for deeply nested structures
const LazyNodeTree = ({ nodeId, depth = 0 }) => {
  const [expanded, setExpanded] = useState(depth < 2); // Only expand first 2 levels
  
  const toggleExpansion = useCallback(() => {
    setExpanded(prev => !prev);
  }, []);
  
  return (
    <div>
      <button onClick={toggleExpansion}>
        {expanded ? 'Collapse' : 'Expand'} 
      </button>
      {expanded && <ChildNodes parentId={nodeId} />}
    </div>
  );
};"""
        },
        
        "styling_optimization": {
            "css_performance": """
/* ❌ Avoid complex animations on many nodes */
.node-with-heavy-animation {
  animation: complexGradient 2s infinite;
  box-shadow: 0 10px 20px rgba(0,0,0,0.3);
  background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
}

/* ✅ Simplified styles for large datasets */
.optimized-node {
  background: #fff;
  border: 2px solid #1a365d;
  transition: border-color 0.2s ease;
}

.optimized-node:hover {
  border-color: #3182ce;
}

/* ✅ Use CSS containment for better performance */
.react-flow__node {
  contain: layout style paint;
}"""
        }
    }
    
    optimization_levels = {
        "small": {"nodes": "< 100", "strategies": ["Basic memoization", "Simple styling"]},
        "medium": {"nodes": "100-500", "strategies": ["Component memoization", "State optimization", "Selective rendering"]},
        "large": {"nodes": "500-1000", "strategies": ["Tree collapsing", "Virtualization", "CSS optimization"]},
        "enterprise": {"nodes": "1000+", "strategies": ["Full optimization stack", "Custom rendering", "Web Workers"]}
    }
    
    level = "small" if node_count < 100 else "medium" if node_count < 500 else "large" if node_count < 1000 else "enterprise"
    
    return {
        "scenario": scenario,
        "node_count": node_count,
        "optimization_level": level,
        "recommended_strategies": optimization_levels[level],
        "implementation_guide": performance_strategies,
        "performance_monitoring": {
            "react_devtools": "Use React DevTools Profiler to identify re-renders",
            "browser_devtools": "Monitor FPS and memory usage in Performance tab",
            "custom_metrics": "Track node/edge update frequency"
        },
        "external_resources": [
            "Guide to Optimize React Flow Project Performance - SynergyCodes",
            "Tuning Edge Animations ReactFlow Optimal Performance - LiamBX",
            "5 Ways to Optimize React Flow in 10 minutes - YouTube"
        ]
    }

def react_flow_tutorial_generator(tutorial_type: str = "mind_map", complexity: str = "intermediate") -> Dict[str, Any]:
    """
    Generate step-by-step tutorials based on official React Flow learning examples
    Covers mind maps, slideshow apps, web audio API, and whiteboard features
    """
    
    tutorials = {
        "mind_map": {
            "description": "Create an interactive mind mapping application with expandable nodes",
            "difficulty": "Intermediate",
            "concepts": ["Custom nodes", "Tree structures", "Dynamic expansion", "Data flow"],
            "step_by_step": [
                {
                    "step": 1,
                    "title": "Setup Mind Map Node Structure",
                    "code": """
// MindMapNode.js
import { memo } from 'react';
import { Handle, Position } from 'reactflow';

const MindMapNode = ({ data }) => {
  return (
    <div className="mind-map-node">
      <Handle type="target" position={Position.Left} />
      <div className="node-content">
        <h3>{data.label}</h3>
        {data.description && <p>{data.description}</p>}
      </div>
      <Handle type="source" position={Position.Right} />
    </div>
  );
};

export default memo(MindMapNode);""",
                    "explanation": "Create a custom node component with handles for connections"
                },
                {
                    "step": 2, 
                    "title": "Implement Expansion Logic",
                    "code": """
// useMindMap.js
import { useCallback } from 'react';
import { useNodesState, useEdgesState } from 'reactflow';

export const useMindMap = (initialNodes, initialEdges) => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  
  const addChildNode = useCallback((parentId, childData) => {
    const parentNode = nodes.find(node => node.id === parentId);
    const childId = `${parentId}-child-${Date.now()}`;
    
    const newNode = {
      id: childId,
      type: 'mindMap',
      position: {
        x: parentNode.position.x + 200,
        y: parentNode.position.y + (nodes.filter(n => n.id.startsWith(parentId)).length * 100)
      },
      data: childData
    };
    
    const newEdge = {
      id: `${parentId}-${childId}`,
      source: parentId,
      target: childId,
      type: 'smoothstep'
    };
    
    setNodes(prev => [...prev, newNode]);
    setEdges(prev => [...prev, newEdge]);
  }, [nodes, setNodes, setEdges]);
  
  return { nodes, edges, onNodesChange, onEdgesChange, addChildNode };
};"""
                },
                {
                    "step": 3,
                    "title": "Add Interaction Handlers",
                    "code": """
// MindMapFlow.js
import { useCallback } from 'react';
import ReactFlow, { Background, Controls } from 'reactflow';
import { useMindMap } from './useMindMap';
import MindMapNode from './MindMapNode';

const nodeTypes = { mindMap: MindMapNode };

const MindMapFlow = () => {
  const { nodes, edges, onNodesChange, onEdgesChange, addChildNode } = useMindMap(
    initialNodes, 
    initialEdges
  );
  
  const onNodeDoubleClick = useCallback((event, node) => {
    const newTopic = prompt('Enter new topic:');
    if (newTopic) {
      addChildNode(node.id, { label: newTopic });
    }
  }, [addChildNode]);
  
  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onNodeDoubleClick={onNodeDoubleClick}
      nodeTypes={nodeTypes}
      fitView
    >
      <Background />
      <Controls />
    </ReactFlow>
  );
};"""
                }
            ]
        },
        
        "slideshow": {
            "description": "Build a presentation system with React Flow for visual storytelling",
            "difficulty": "Advanced",
            "concepts": ["Viewport control", "Animations", "Slide transitions", "Presentation mode"],
            "step_by_step": [
                {
                    "step": 1,
                    "title": "Create Slide Node Components",
                    "code": """
// SlideNode.js
import { memo } from 'react';
import { Handle, Position } from 'reactflow';

const SlideNode = ({ data, selected }) => {
  return (
    <div className={`slide-node ${selected ? 'selected' : ''}`}>
      <div className="slide-content">
        <h2>{data.title}</h2>
        <div className="slide-body">
          {data.content}
        </div>
        <div className="slide-number">
          Slide {data.slideNumber}
        </div>
      </div>
      <Handle type="source" position={Position.Bottom} />
      <Handle type="target" position={Position.Top} />
    </div>
  );
};

export default memo(SlideNode);"""
                },
                {
                    "step": 2,
                    "title": "Implement Presentation Controller",
                    "code": """
// useSlideshow.js
import { useState, useCallback } from 'react';
import { useReactFlow } from 'reactflow';

export const useSlideshow = (slides) => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [presentationMode, setPresentationMode] = useState(false);
  const { fitView, setViewport } = useReactFlow();
  
  const goToSlide = useCallback((slideIndex) => {
    const targetSlide = slides[slideIndex];
    if (targetSlide) {
      setCurrentSlide(slideIndex);
      
      // Animate to slide position
      setViewport({
        x: -targetSlide.position.x + window.innerWidth / 2 - 200,
        y: -targetSlide.position.y + window.innerHeight / 2 - 150,
        zoom: 1.2
      }, { duration: 800 });
    }
  }, [slides, setViewport]);
  
  const nextSlide = useCallback(() => {
    if (currentSlide < slides.length - 1) {
      goToSlide(currentSlide + 1);
    }
  }, [currentSlide, slides.length, goToSlide]);
  
  const prevSlide = useCallback(() => {
    if (currentSlide > 0) {
      goToSlide(currentSlide - 1);
    }
  }, [currentSlide, goToSlide]);
  
  return {
    currentSlide,
    presentationMode,
    setPresentationMode,
    goToSlide,
    nextSlide,
    prevSlide
  };
};"""
                }
            ]
        },
        
        "web_audio": {
            "description": "Connect React Flow to Web Audio API for visual audio programming",
            "difficulty": "Expert",
            "concepts": ["Web Audio API", "Audio nodes", "Signal flow", "Real-time audio"],
            "step_by_step": [
                {
                    "step": 1,
                    "title": "Audio Context Setup",
                    "code": """
// useAudioContext.js
import { useState, useEffect, useRef } from 'react';

export const useAudioContext = () => {
  const [audioContext, setAudioContext] = useState(null);
  const [isActive, setIsActive] = useState(false);
  const audioNodesRef = useRef(new Map());
  
  useEffect(() => {
    const initAudio = () => {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      setAudioContext(ctx);
    };
    
    initAudio();
    
    return () => {
      if (audioContext) {
        audioContext.close();
      }
    };
  }, []);
  
  const createAudioNode = (type, id, params = {}) => {
    if (!audioContext) return null;
    
    let node;
    switch (type) {
      case 'oscillator':
        node = audioContext.createOscillator();
        node.frequency.setValueAtTime(params.frequency || 440, audioContext.currentTime);
        node.type = params.waveType || 'sine';
        break;
      case 'gain':
        node = audioContext.createGain();
        node.gain.setValueAtTime(params.gain || 0.5, audioContext.currentTime);
        break;
      case 'filter':
        node = audioContext.createBiquadFilter();
        node.frequency.setValueAtTime(params.frequency || 1000, audioContext.currentTime);
        node.type = params.filterType || 'lowpass';
        break;
      default:
        return null;
    }
    
    audioNodesRef.current.set(id, node);
    return node;
  };
  
  return { audioContext, audioNodesRef, createAudioNode, isActive, setIsActive };
};"""
                }
            ]
        },
        
        "whiteboard": {
            "description": "Build collaborative whiteboard features with infinite canvas",
            "difficulty": "Advanced", 
            "concepts": ["Infinite canvas", "Collaborative editing", "Real-time sync", "Drawing tools"],
            "step_by_step": [
                {
                    "step": 1,
                    "title": "Drawing Canvas Integration",
                    "code": """
// DrawingNode.js
import { memo, useRef, useEffect } from 'react';
import { NodeResizer } from 'reactflow';

const DrawingNode = ({ data, selected }) => {
  const canvasRef = useRef(null);
  const isDrawing = useRef(false);
  
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    ctx.strokeStyle = data.strokeColor || '#000';
    ctx.lineWidth = data.lineWidth || 2;
    ctx.lineCap = 'round';
    
    // Restore drawing from data
    if (data.paths) {
      data.paths.forEach(path => {
        ctx.beginPath();
        path.points.forEach((point, index) => {
          if (index === 0) {
            ctx.moveTo(point.x, point.y);
          } else {
            ctx.lineTo(point.x, point.y);
          }
        });
        ctx.stroke();
      });
    }
  }, [data]);
  
  return (
    <div className="drawing-node">
      <canvas
        ref={canvasRef}
        width={data.width || 300}
        height={data.height || 200}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
      />
      {selected && <NodeResizer minWidth={100} minHeight={100} />}
    </div>
  );
};

export default memo(DrawingNode);"""
                }
            ]
        }
    }
    
    selected_tutorial = tutorials.get(tutorial_type, tutorials["mind_map"])
    
    return {
        "tutorial_type": tutorial_type,
        "complexity": complexity,
        "tutorial_details": selected_tutorial,
        "prerequisites": [
            "Basic React knowledge",
            "Understanding of React Flow fundamentals", 
            "Event handling concepts",
            "State management patterns"
        ],
        "next_steps": [
            "Add persistence with localStorage",
            "Implement undo/redo functionality",
            "Add collaborative features with WebRTC",
            "Optimize performance for large datasets"
        ],
        "related_examples": {
            "official_examples": f"https://reactflow.dev/examples/{tutorial_type}",
            "playground": "https://reactflow.dev/playground", 
            "github_repo": "https://github.com/xyflow/xyflow/tree/main/examples"
        }
    }

def react_flow_troubleshooting_expert(error_type: str = "common", issue_description: str = "") -> Dict[str, Any]:
    """
    Expert troubleshooting guide based on official React Flow documentation
    Based on https://reactflow.dev/learn/troubleshooting/common-errors
    """
    
    common_errors = {
        "nodes_not_rendering": {
            "symptoms": ["Nodes don't appear", "Empty flow", "Missing components"],
            "causes": [
                "Missing nodeTypes definition",
                "Incorrect node type in data",
                "Component not exported properly",
                "CSS issues hiding nodes"
            ],
            "solutions": """
// ✅ Ensure nodeTypes are defined
const nodeTypes = {
  customNode: CustomNodeComponent,
};

// ✅ Pass nodeTypes to ReactFlow
<ReactFlow nodeTypes={nodeTypes} />

// ✅ Check node data has correct type
const nodes = [{
  id: '1',
  type: 'customNode', // Must match nodeTypes key
  position: { x: 0, y: 0 },
  data: { label: 'Node 1' }
}];

// ✅ Verify component export
export default memo(CustomNodeComponent);"""
        },
        
        "performance_issues": {
            "symptoms": ["Slow dragging", "Laggy interactions", "High CPU usage"],
            "causes": [
                "Missing memoization",
                "Accessing nodes/edges in components",
                "Complex CSS animations",
                "Large dataset without optimization"
            ],
            "solutions": """
// ✅ Memoize components
const MyNode = memo(({ data }) => <div>{data.label}</div>);

// ✅ Memoize event handlers
const onNodeClick = useCallback((event, node) => {
  // Handle click
}, []);

// ✅ Use specific selectors
const selectedCount = useStore(
  state => state.nodes.filter(n => n.selected).length
);

// ✅ Optimize for large datasets
const [visibleNodes, setVisibleNodes] = useState([]);
useEffect(() => {
  const viewport = getViewport();
  const visible = allNodes.filter(node => 
    isNodeInViewport(node, viewport)
  );
  setVisibleNodes(visible);
}, [allNodes, viewport]);"""
        },
        
        "connection_issues": {
            "symptoms": ["Edges not connecting", "Handle not working", "Invalid connections"],
            "causes": [
                "Missing handles",
                "Incorrect handle positions",
                "Connection validation blocking",
                "Handle IDs not matching"
            ],
            "solutions": """
// ✅ Add handles to custom nodes
import { Handle, Position } from 'reactflow';

const CustomNode = ({ data }) => (
  <div>
    <Handle 
      type="target" 
      position={Position.Left} 
      id="input"
    />
    <div>{data.label}</div>
    <Handle 
      type="source" 
      position={Position.Right} 
      id="output"
    />
  </div>
);

// ✅ Validate connections properly
const isValidConnection = useCallback((connection) => {
  // Allow connection logic
  return connection.source !== connection.target;
}, []);

<ReactFlow isValidConnection={isValidConnection} />"""
        },
        
        "typescript_errors": {
            "symptoms": ["Type errors", "Missing type definitions", "Generic type issues"],
            "causes": [
                "Missing type imports",
                "Incorrect generic parameters", 
                "Custom node type not defined",
                "Edge data type mismatch"
            ],
            "solutions": """
// ✅ Import correct types
import type { 
  Node, 
  Edge, 
  NodeProps, 
  EdgeProps,
  Connection 
} from 'reactflow';

// ✅ Define custom node types
type CustomNodeData = {
  label: string;
  value: number;
};

type CustomNode = Node<CustomNodeData>;

// ✅ Type custom components
const CustomNode = ({ data }: NodeProps<CustomNodeData>) => (
  <div>{data.label}: {data.value}</div>
);

// ✅ Use typed hooks
const [nodes, setNodes] = useState<CustomNode[]>([]);
const [edges, setEdges] = useState<Edge[]>([]);"""
        },
        
        "layout_problems": {
            "symptoms": ["Overlapping nodes", "Poor positioning", "Layout not updating"],
            "causes": [
                "Missing node dimensions",
                "Incorrect layout configuration",
                "Async layout not handled",
                "Missing dependencies"
            ],
            "solutions": """
// ✅ Provide node dimensions for layouting
const layoutedElements = getLayoutedElements(nodes, edges, {
  'elk.algorithm': 'layered',
  'elk.direction': 'RIGHT',
  'elk.spacing.nodeNode': '100'
});

// ✅ Handle async layouts properly
const [isLayouting, setIsLayouting] = useState(false);

const applyLayout = useCallback(async () => {
  setIsLayouting(true);
  try {
    const { nodes: layoutedNodes, edges: layoutedEdges } = 
      await layoutElements(nodes, edges);
    setNodes(layoutedNodes);
    setEdges(layoutedEdges);
  } finally {
    setIsLayouting(false);
  }
}, [nodes, edges]);

// ✅ Ensure layout recalculates on data changes
useEffect(() => {
  if (nodes.length > 0) {
    applyLayout();
  }
}, [nodes.length, applyLayout]);"""
        }
    }
    
    migration_guides = {
        "v12": "Breaking changes in v12 - new package structure, updated APIs",
        "v11": "Edge label positioning changes, new edge types",
        "v10": "Major TypeScript improvements, API consolidation"
    }
    
    debugging_tools = {
        "react_devtools": "Profile component re-renders and state changes",
        "browser_devtools": "Monitor network, performance, and console errors",
        "react_flow_devtools": "Official React Flow debugging extension",
        "console_logging": "Add strategic console.log statements for data flow"
    }
    
    return {
        "error_type": error_type,
        "issue_description": issue_description,
        "troubleshooting_guide": common_errors.get(error_type, common_errors["nodes_not_rendering"]),
        "debugging_tools": debugging_tools,
        "migration_guides": migration_guides,
        "support_resources": [
            "React Flow Discord: https://discord.gg/RVmnytFmGW",
            "GitHub Issues: https://github.com/xyflow/xyflow/issues",
            "Stack Overflow: reactflow tag",
            "Official Documentation: https://reactflow.dev"
        ],
        "common_fixes": [
            "Clear browser cache and restart dev server",
            "Check console for JavaScript errors", 
            "Verify all dependencies are up to date",
            "Ensure proper import statements",
            "Check CSS for conflicting styles"
        ]
    }

def react_flow_accessibility_expert(feature: str = "keyboard_navigation", compliance_level: str = "WCAG_AA") -> Dict[str, Any]:
    """
    Comprehensive accessibility implementation for React Flow
    Based on https://reactflow.dev/learn/advanced-use/accessibility
    """
    
    accessibility_features = {
        "keyboard_navigation": {
            "description": "Full keyboard control for React Flow interactions",
            "implementation": """
// ✅ Keyboard navigation implementation
import { useCallback, useEffect } from 'react';
import { useReactFlow, useNodesState } from 'reactflow';

const useKeyboardNavigation = () => {
  const { setViewport, getViewport, getNodes } = useReactFlow();
  const [, setNodes] = useNodesState([]);
  
  const handleKeyDown = useCallback((event) => {
    const { key, ctrlKey, metaKey, shiftKey } = event;
    const viewport = getViewport();
    
    switch (key) {
      case 'ArrowUp':
        event.preventDefault();
        setViewport({
          ...viewport,
          y: viewport.y + (shiftKey ? 50 : 10)
        });
        break;
        
      case 'ArrowDown':
        event.preventDefault();
        setViewport({
          ...viewport,
          y: viewport.y - (shiftKey ? 50 : 10)
        });
        break;
        
      case 'ArrowLeft':
        event.preventDefault();
        setViewport({
          ...viewport,
          x: viewport.x + (shiftKey ? 50 : 10)
        });
        break;
        
      case 'ArrowRight':
        event.preventDefault();
        setViewport({
          ...viewport,
          x: viewport.x - (shiftKey ? 50 : 10)
        });
        break;
        
      case '+':
      case '=':
        if (ctrlKey || metaKey) {
          event.preventDefault();
          setViewport({
            ...viewport,
            zoom: Math.min(viewport.zoom * 1.2, 3)
          });
        }
        break;
        
      case '-':
        if (ctrlKey || metaKey) {
          event.preventDefault();
          setViewport({
            ...viewport,
            zoom: Math.max(viewport.zoom * 0.8, 0.1)
          });
        }
        break;
        
      case 'Tab':
        // Handle node focus cycling
        handleNodeFocus(event);
        break;
    }
  }, [setViewport, getViewport]);
  
  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);
};""",
            "aria_labels": """
// ✅ ARIA labels for screen readers
const AccessibleNode = ({ data, selected }) => {
  return (
    <div 
      role="button"
      tabIndex={0}
      aria-label={`Node: ${data.label}. ${selected ? 'Selected' : 'Not selected'}`}
      aria-describedby={`node-description-${data.id}`}
      className="accessible-node"
    >
      <div id={`node-description-${data.id}`} className="sr-only">
        {data.description || `Interactive node with label ${data.label}`}
      </div>
      <h3>{data.label}</h3>
      {data.content && <p>{data.content}</p>}
    </div>
  );
};"""
        },
        
        "screen_reader": {
            "description": "Screen reader compatible React Flow implementation",
            "implementation": """
// ✅ Screen reader announcements
import { useEffect, useRef } from 'react';

const useScreenReaderAnnouncements = () => {
  const announcementRef = useRef(null);
  
  const announce = useCallback((message) => {
    if (announcementRef.current) {
      announcementRef.current.textContent = message;
      // Clear after announcement
      setTimeout(() => {
        if (announcementRef.current) {
          announcementRef.current.textContent = '';
        }
      }, 1000);
    }
  }, []);
  
  return {
    announce,
    AnnouncementRegion: () => (
      <div 
        ref={announcementRef}
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      />
    )
  };
};

// ✅ Flow navigation for screen readers
const AccessibleReactFlow = () => {
  const { announce, AnnouncementRegion } = useScreenReaderAnnouncements();
  
  const onNodeClick = useCallback((event, node) => {
    announce(`Selected node: ${node.data.label}`);
  }, [announce]);
  
  const onEdgeClick = useCallback((event, edge) => {
    announce(`Selected edge from ${edge.source} to ${edge.target}`);
  }, [announce]);
  
  return (
    <div>
      <AnnouncementRegion />
      <ReactFlow 
        onNodeClick={onNodeClick}
        onEdgeClick={onEdgeClick}
        aria-label="Interactive flow diagram"
      />
    </div>
  );
};""",
            "semantic_structure": """
// ✅ Semantic HTML structure
const AccessibleFlowWrapper = ({ children, title, description }) => {
  return (
    <section 
      role="application"
      aria-labelledby="flow-title"
      aria-describedby="flow-description"
    >
      <h2 id="flow-title">{title}</h2>
      <p id="flow-description" className="sr-only">
        {description}
      </p>
      <div className="flow-instructions sr-only">
        Use arrow keys to navigate, Tab to cycle through nodes,
        Enter or Space to select, Ctrl+Plus to zoom in, Ctrl+Minus to zoom out.
      </div>
      {children}
    </section>
  );
};"""
        },
        
        "focus_management": {
            "description": "Proper focus management and visual indicators",
            "implementation": """
// ✅ Focus management system
import { useState, useCallback, useRef } from 'react';

const useFocusManagement = (nodes) => {
  const [focusedNodeId, setFocusedNodeId] = useState(null);
  const nodeRefs = useRef(new Map());
  
  const setNodeRef = useCallback((nodeId, ref) => {
    if (ref) {
      nodeRefs.current.set(nodeId, ref);
    } else {
      nodeRefs.current.delete(nodeId);
    }
  }, []);
  
  const focusNode = useCallback((nodeId) => {
    const nodeRef = nodeRefs.current.get(nodeId);
    if (nodeRef) {
      nodeRef.focus();
      setFocusedNodeId(nodeId);
    }
  }, []);
  
  const cycleFocus = useCallback((direction = 'forward') => {
    const nodeIds = nodes.map(n => n.id);
    const currentIndex = nodeIds.indexOf(focusedNodeId);
    
    let nextIndex;
    if (direction === 'forward') {
      nextIndex = currentIndex < nodeIds.length - 1 ? currentIndex + 1 : 0;
    } else {
      nextIndex = currentIndex > 0 ? currentIndex - 1 : nodeIds.length - 1;
    }
    
    const nextNodeId = nodeIds[nextIndex];
    focusNode(nextNodeId);
  }, [nodes, focusedNodeId, focusNode]);
  
  return { focusedNodeId, setNodeRef, focusNode, cycleFocus };
};

// ✅ Focusable node component
const FocusableNode = ({ id, data, selected }) => {
  const { setNodeRef, focusedNodeId } = useFocusManagement();
  const isFocused = focusedNodeId === id;
  
  return (
    <div
      ref={(ref) => setNodeRef(id, ref)}
      tabIndex={0}
      role="button"
      aria-pressed={selected}
      className={`node ${selected ? 'selected' : ''} ${isFocused ? 'focused' : ''}`}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          // Handle node activation
        }
      }}
    >
      {data.label}
    </div>
  );
};""",
            "css_indicators": """
/* ✅ High contrast focus indicators */
.node:focus {
  outline: 3px solid #0066cc;
  outline-offset: 2px;
  box-shadow: 0 0 0 5px rgba(0, 102, 204, 0.3);
}

.node:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}

.node.selected {
  border: 2px solid #0066cc;
  background-color: #e6f3ff;
}

/* ✅ Screen reader only content */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* ✅ High contrast mode support */
@media (prefers-contrast: high) {
  .node {
    border: 2px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
  
  .node:focus {
    outline: 3px solid Highlight;
  }
}"""
        },
        
        "color_contrast": {
            "description": "WCAG compliant color schemes and contrast ratios",
            "implementation": """
// ✅ WCAG AA compliant color palette
const accessibleColors = {
  // 4.5:1 contrast ratio for normal text
  primary: {
    background: '#ffffff',
    text: '#1a1a1a',        // 15.3:1 ratio
    border: '#666666'       // 6.4:1 ratio
  },
  
  // 3:1 contrast ratio for large text and UI components
  secondary: {
    background: '#f5f5f5',
    text: '#333333',        // 12.6:1 ratio
    border: '#999999'       // 4.2:1 ratio
  },
  
  // Status colors with proper contrast
  status: {
    success: {
      background: '#d4edda',
      text: '#155724',      // 7.1:1 ratio
      border: '#28a745'
    },
    warning: {
      background: '#fff3cd',
      text: '#856404',      // 6.5:1 ratio
      border: '#ffc107'
    },
    error: {
      background: '#f8d7da',
      text: '#721c24',      // 8.1:1 ratio
      border: '#dc3545'
    }
  }
};

// ✅ Dynamic contrast checking
const checkContrast = (foreground, background) => {
  const getLuminance = (color) => {
    // Convert hex to RGB and calculate luminance
    const hex = color.replace('#', '');
    const r = parseInt(hex.substr(0, 2), 16) / 255;
    const g = parseInt(hex.substr(2, 2), 16) / 255;
    const b = parseInt(hex.substr(4, 2), 16) / 255;
    
    const [rs, gs, bs] = [r, g, b].map(c => 
      c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4)
    );
    
    return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
  };
  
  const l1 = getLuminance(foreground);
  const l2 = getLuminance(background);
  const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  
  return {
    ratio,
    AA: ratio >= 4.5,
    AAA: ratio >= 7,
    AA_large: ratio >= 3
  };
};"""
        }
    }
    
    compliance_requirements = {
        "WCAG_A": ["Basic accessibility", "Keyboard navigation", "Alt text"],
        "WCAG_AA": ["Enhanced accessibility", "4.5:1 contrast ratio", "Focus indicators"],
        "WCAG_AAA": ["Highest accessibility", "7:1 contrast ratio", "Advanced features"]
    }
    
    return {
        "feature": feature,
        "compliance_level": compliance_level,
        "requirements": compliance_requirements.get(compliance_level, compliance_requirements["WCAG_AA"]),
        "implementation_guide": accessibility_features.get(feature, accessibility_features["keyboard_navigation"]),
        "testing_tools": [
            "axe-core for automated testing",
            "WAVE browser extension",
            "Screen reader testing (NVDA, JAWS, VoiceOver)",
            "Keyboard-only navigation testing"
        ],
        "best_practices": [
            "Test with actual assistive technologies",
            "Include users with disabilities in testing",
            "Provide multiple ways to access information",
            "Ensure all functionality is keyboard accessible",
            "Use semantic HTML and ARIA appropriately"
        ]
    }

# ADVANCED LEARNING TOOLS

def react_flow_devtools_mastery(debugging_scenario: str = "performance", issue_type: str = "re_renders") -> Dict[str, Any]:
    """
    Advanced debugging and development tools guidance
    Based on https://reactflow.dev/learn/advanced-use/devtools-and-debugging
    """
    
    debugging_strategies = {
        "performance": {
            "react_devtools_profiler": """
// ✅ Performance profiling setup
import { Profiler } from 'react';

const ReactFlowProfiler = ({ children }) => {
  const onRenderCallback = (id, phase, actualDuration, baseDuration) => {
    console.log('React Flow Performance:', {
      component: id,
      phase, // 'mount' or 'update'
      actualDuration, // Time spent rendering
      baseDuration, // Estimated time without memoization
      renderEfficiency: ((baseDuration - actualDuration) / baseDuration * 100).toFixed(2) + '%'
    });
  };
  
  return (
    <Profiler id="ReactFlow" onRender={onRenderCallback}>
      {children}
    </Profiler>
  );
};

// ✅ Custom performance monitoring
const usePerformanceMonitor = () => {
  const [metrics, setMetrics] = useState({
    renderCount: 0,
    lastRenderTime: 0,
    averageRenderTime: 0
  });
  
  const startTime = useRef(0);
  
  useEffect(() => {
    startTime.current = performance.now();
    return () => {
      const endTime = performance.now();
      const renderTime = endTime - startTime.current;
      
      setMetrics(prev => ({
        renderCount: prev.renderCount + 1,
        lastRenderTime: renderTime,
        averageRenderTime: (prev.averageRenderTime * prev.renderCount + renderTime) / (prev.renderCount + 1)
      }));
    };
  });
  
  return metrics;
};""",
            
            "memory_monitoring": """
// ✅ Memory usage tracking
const useMemoryMonitor = () => {
  const [memoryInfo, setMemoryInfo] = useState(null);
  
  useEffect(() => {
    const checkMemory = () => {
      if ('memory' in performance) {
        setMemoryInfo({
          usedJSHeapSize: (performance.memory.usedJSHeapSize / 1048576).toFixed(2) + ' MB',
          totalJSHeapSize: (performance.memory.totalJSHeapSize / 1048576).toFixed(2) + ' MB',
          jsHeapSizeLimit: (performance.memory.jsHeapSizeLimit / 1048576).toFixed(2) + ' MB'
        });
      }
    };
    
    checkMemory();
    const interval = setInterval(checkMemory, 5000);
    return () => clearInterval(interval);
  }, []);
  
  return memoryInfo;
};

// ✅ Node count impact analysis
const useNodeCountAnalysis = (nodes) => {
  const [analysis, setAnalysis] = useState({});
  
  useEffect(() => {
    const startTime = performance.now();
    
    setTimeout(() => {
      const endTime = performance.now();
      setAnalysis({
        nodeCount: nodes.length,
        renderTime: endTime - startTime,
        memoryPerNode: performance.memory ? 
          (performance.memory.usedJSHeapSize / nodes.length / 1024).toFixed(2) + ' KB' : 
          'N/A'
      });
    }, 0);
  }, [nodes.length]);
  
  return analysis;
};"""
        },
        
        "state_debugging": {
            "store_inspection": """
// ✅ React Flow store debugging
import { useStore } from 'reactflow';

const ReactFlowDebugger = () => {
  const store = useStore();
  
  useEffect(() => {
    const unsubscribe = store.subscribe((state) => {
      console.log('Store State Changed:', {
        timestamp: new Date().toISOString(),
        nodeCount: state.nodes.length,
        edgeCount: state.edges.length,
        viewport: state.viewport,
        selectedNodes: state.nodes.filter(n => n.selected).map(n => n.id),
        selectedEdges: state.edges.filter(e => e.selected).map(e => e.id),
        connectionMode: state.connectionMode,
        snapToGrid: state.snapToGrid
      });
    });
    
    return unsubscribe;
  }, [store]);
  
  return null; // This is just a debugging component
};

// ✅ State diff tracking
const useStateDiff = () => {
  const currentState = useStore(state => state);
  const previousState = useRef(currentState);
  
  useEffect(() => {
    const diff = {};
    
    Object.keys(currentState).forEach(key => {
      if (currentState[key] !== previousState.current[key]) {
        diff[key] = {
          previous: previousState.current[key],
          current: currentState[key]
        };
      }
    });
    
    if (Object.keys(diff).length > 0) {
      console.log('State Changes:', diff);
    }
    
    previousState.current = currentState;
  }, [currentState]);
};""",
            
            "connection_debugging": """
// ✅ Connection flow debugging
const useConnectionDebugger = () => {
  const onConnect = useCallback((params) => {
    console.log('Connection Attempt:', {
      source: params.source,
      target: params.target,
      sourceHandle: params.sourceHandle,
      targetHandle: params.targetHandle,
      timestamp: new Date().toISOString()
    });
    
    // Validate connection
    const validation = validateConnection(params);
    console.log('Connection Validation:', validation);
    
    return validation.isValid;
  }, []);
  
  const onConnectStart = useCallback((event, { nodeId, handleType, handleId }) => {
    console.log('Connection Started:', {
      nodeId,
      handleType,
      handleId,
      mousePosition: { x: event.clientX, y: event.clientY }
    });
  }, []);
  
  const onConnectEnd = useCallback((event) => {
    console.log('Connection Ended:', {
      endPosition: { x: event.clientX, y: event.clientY },
      targetElement: event.target.tagName
    });
  }, []);
  
  return { onConnect, onConnectStart, onConnectEnd };
};"""
        },
        
        "layout_debugging": {
            "layout_visualization": """
// ✅ Layout algorithm debugging
const useLayoutDebugger = (layoutAlgorithm) => {
  const [layoutMetrics, setLayoutMetrics] = useState({});
  
  const debugLayout = useCallback(async (nodes, edges) => {
    const startTime = performance.now();
    
    console.log('Layout Started:', {
      algorithm: layoutAlgorithm,
      nodeCount: nodes.length,
      edgeCount: edges.length,
      timestamp: new Date().toISOString()
    });
    
    try {
      const result = await applyLayout(nodes, edges, layoutAlgorithm);
      const endTime = performance.now();
      
      const metrics = {
        duration: endTime - startTime,
        nodesMoved: result.nodes.filter((node, index) => 
          node.position.x !== nodes[index]?.position.x ||
          node.position.y !== nodes[index]?.position.y
        ).length,
        boundingBox: calculateBoundingBox(result.nodes),
        density: calculateDensity(result.nodes, result.edges)
      };
      
      setLayoutMetrics(metrics);
      console.log('Layout Completed:', metrics);
      
      return result;
    } catch (error) {
      console.error('Layout Error:', error);
      throw error;
    }
  }, [layoutAlgorithm]);
  
  return { debugLayout, layoutMetrics };
};

// ✅ Visual layout debugging overlay
const LayoutDebugOverlay = ({ nodes, edges, layoutMetrics }) => {
  if (!layoutMetrics.boundingBox) return null;
  
  return (
    <div className="layout-debug-overlay">
      <div className="debug-info">
        <h4>Layout Debug Info</h4>
        <p>Duration: {layoutMetrics.duration?.toFixed(2)}ms</p>
        <p>Nodes moved: {layoutMetrics.nodesMoved}</p>
        <p>Density: {layoutMetrics.density?.toFixed(2)}</p>
      </div>
      
      <svg className="debug-visualization">
        {/* Bounding box */}
        <rect 
          x={layoutMetrics.boundingBox.x}
          y={layoutMetrics.boundingBox.y}
          width={layoutMetrics.boundingBox.width}
          height={layoutMetrics.boundingBox.height}
          fill="none"
          stroke="red"
          strokeDasharray="5,5"
        />
        
        {/* Node positions */}
        {nodes.map(node => (
          <circle
            key={node.id}
            cx={node.position.x}
            cy={node.position.y}
            r="3"
            fill="blue"
            opacity="0.5"
          />
        ))}
      </svg>
    </div>
  );
};"""
        }
    }
    
    browser_devtools = {
        "performance_tab": [
            "Record interaction performance",
            "Analyze frame rates and rendering",
            "Identify performance bottlenecks",
            "Monitor memory usage patterns"
        ],
        "console_strategies": [
            "Use console.group() for organized logging",
            "Implement conditional logging with debug flags",
            "Use console.time() for performance measurements",
            "Create custom console methods for different log levels"
        ],
        "network_debugging": [
            "Monitor API calls for dynamic content",
            "Check bundle sizes and loading times",
            "Analyze resource loading patterns",
            "Debug WebSocket connections for real-time features"
        ]
    }
    
    return {
        "debugging_scenario": debugging_scenario,
        "issue_type": issue_type,
        "debugging_strategy": debugging_strategies.get(debugging_scenario, debugging_strategies["performance"]),
        "browser_devtools": browser_devtools,
        "official_devtools": {
            "react_devtools": "Browser extension for React component debugging",
            "react_flow_devtools": "Upcoming official React Flow debugging tools",
            "redux_devtools": "For complex state management scenarios"
        },
        "debugging_checklist": [
            "Enable React Strict Mode for development",
            "Use React DevTools Profiler",
            "Monitor console for warnings and errors",
            "Check network tab for resource loading",
            "Profile performance with browser tools",
            "Test with different viewport sizes",
            "Verify accessibility with screen readers"
        ]
    }

def export_learning_tools():
    """Export all React Flow learning tools for integration"""
    return {
        "react_flow_layouting_expert": react_flow_layouting_expert,
        "react_flow_performance_mastery": react_flow_performance_mastery, 
        "react_flow_tutorial_generator": react_flow_tutorial_generator,
        "react_flow_troubleshooting_expert": react_flow_troubleshooting_expert,
        "react_flow_accessibility_expert": react_flow_accessibility_expert,
        "react_flow_devtools_mastery": react_flow_devtools_mastery
    }

# MCP Tool Definitions
def get_tools():
    """Get React Flow learning tool definitions for MCP server"""
    return [
        {
            "name": "react_flow_layouting_expert",
            "description": "Expert guidance on React Flow layouting using Dagre, D3-Hierarchy, D3-Force, and ELK",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "requirement": {
                        "type": "string",
                        "enum": ["dagre", "d3-hierarchy", "d3-force", "elkjs"],
                        "description": "Layouting system to use",
                        "default": "dagre"
                    },
                    "use_case": {
                        "type": "string",
                        "description": "Specific use case or layout requirements",
                        "default": "hierarchical tree"
                    }
                },
                "required": []
            }
        },
        {
            "name": "react_flow_performance_mastery",
            "description": "Advanced performance optimization strategies for React Flow applications",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "scenario": {
                        "type": "string",
                        "enum": ["large_dataset", "complex_interactions", "memory_optimization", "rendering_performance"],
                        "description": "Performance optimization scenario",
                        "default": "large_dataset"
                    },
                    "node_count": {
                        "type": "integer",
                        "description": "Approximate number of nodes in the flow",
                        "default": 1000
                    }
                },
                "required": []
            }
        },
        {
            "name": "react_flow_tutorial_generator",
            "description": "Generate comprehensive tutorials for React Flow applications",
            "inputSchema": {
                "type": "object", 
                "properties": {
                    "tutorial_type": {
                        "type": "string",
                        "enum": ["mind_map", "slideshow", "web_audio", "whiteboard"],
                        "description": "Type of tutorial to generate",
                        "default": "mind_map"
                    },
                    "complexity": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced", "expert"],
                        "description": "Tutorial complexity level",
                        "default": "intermediate"
                    }
                },
                "required": []
            }
        },
        {
            "name": "react_flow_troubleshooting_expert",
            "description": "Expert troubleshooting guide for React Flow issues",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "error_type": {
                        "type": "string",
                        "enum": ["nodes_not_rendering", "performance_issues", "connection_issues", "typescript_errors", "layout_problems"],
                        "description": "Type of error or issue",
                        "default": "common"
                    },
                    "issue_description": {
                        "type": "string",
                        "description": "Detailed description of the issue",
                        "default": ""
                    }
                },
                "required": []
            }
        },
        {
            "name": "react_flow_accessibility_expert",
            "description": "Comprehensive accessibility implementation for React Flow",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "feature": {
                        "type": "string",
                        "enum": ["keyboard_navigation", "screen_reader", "focus_management", "color_contrast"],
                        "description": "Accessibility feature to implement",
                        "default": "keyboard_navigation"
                    },
                    "compliance_level": {
                        "type": "string",
                        "enum": ["WCAG_A", "WCAG_AA", "WCAG_AAA"],
                        "description": "WCAG compliance level",
                        "default": "WCAG_AA"
                    }
                },
                "required": []
            }
        },
        {
            "name": "react_flow_devtools_mastery",
            "description": "Advanced debugging and development tools guidance for React Flow",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "debugging_scenario": {
                        "type": "string",
                        "enum": ["performance", "state_debugging", "layout_debugging", "connection_debugging"],
                        "description": "Debugging scenario",
                        "default": "performance"
                    },
                    "issue_type": {
                        "type": "string",
                        "description": "Specific type of issue to debug",
                        "default": "re_renders"
                    }
                },
                "required": []
            }
        }
    ]

# MCP Tool Handlers
def handle_react_flow_layouting_expert(arguments: dict):
    """Handle layouting expert tool call"""
    result = react_flow_layouting_expert(
        requirement=arguments.get("requirement", "dagre"),
        use_case=arguments.get("use_case", "hierarchical tree")
    )
    return [{
        "type": "text",
        "text": f"""# React Flow Layouting Expert

## Layout System: {result['layouting_system'].upper()}

### Recommendation
**Best for**: {', '.join(result['recommendation']['best_for'])}

**Implementation:**
```javascript
{result['recommendation']['implementation']}
```

### Configuration Options
{chr(10).join(f"- **{key}**: {value}" for key, value in result['recommendation'].get('config_options', {}).items())}

### Comparison Matrix
{chr(10).join(f"- **{category}**: {chr(10).join(f'  - {system}: {level}' for system, level in systems.items())}" for category, systems in result['comparison_matrix'].items())}

### Edge Routing Options
- **Smart Edge**: {result['edge_routing_options']['smart_edge']}
- **Custom Routing**: {result['edge_routing_options']['custom_routing']}
- **Libraries**: {', '.join(result['edge_routing_options']['libraries'])}

### Expert Tips
{chr(10).join(f"- {tip}" for tip in result['layout_tips'])}

Based on official React Flow layouting documentation: https://reactflow.dev/learn/layouting/layouting
"""
    }]

def handle_react_flow_performance_mastery(arguments: dict):
    """Handle performance mastery tool call"""
    result = react_flow_performance_mastery(
        scenario=arguments.get("scenario", "large_dataset"),
        node_count=arguments.get("node_count", 1000)
    )
    return [{
        "type": "text",
        "text": f"""# React Flow Performance Mastery

## Scenario: {result['scenario']} ({result['node_count']} nodes)
**Optimization Level**: {result['optimization_level'].upper()}

### Recommended Strategies
{chr(10).join(f"- {strategy}" for strategy in result['recommended_strategies']['strategies'])}

### Implementation Guide

#### Memoization Patterns
```javascript
{result['implementation_guide']['memoization']['component_memoization']}
```

```javascript
{result['implementation_guide']['memoization']['function_memoization']}
```

#### State Optimization
**Problem:**
```javascript
{result['implementation_guide']['state_optimization']['problem']}
```

**Solution:**
```javascript
{result['implementation_guide']['state_optimization']['solution']}
```

#### Tree Optimization
```javascript
{result['implementation_guide']['tree_optimization']['collapse_strategy']}
```

#### CSS Performance
```css
{result['implementation_guide']['styling_optimization']['css_performance']}
```

### Performance Monitoring
{chr(10).join(f"- **{tool}**: {desc}" for tool, desc in result['performance_monitoring'].items())}

### External Resources
{chr(10).join(f"- {resource}" for resource in result['external_resources'])}

Based on official React Flow performance guide: https://reactflow.dev/learn/advanced-use/performance
"""
    }]

def handle_react_flow_tutorial_generator(arguments: dict):
    """Handle tutorial generator tool call"""
    result = react_flow_tutorial_generator(
        tutorial_type=arguments.get("tutorial_type", "mind_map"),
        complexity=arguments.get("complexity", "intermediate")
    )
    
    tutorial = result['tutorial_details']
    steps_content = []
    
    for step in tutorial['step_by_step']:
        steps_content.append(f"""
### Step {step['step']}: {step['title']}

{step.get('explanation', '')}

```javascript
{step['code']}
```
""")
    
    return [{
        "type": "text", 
        "text": f"""# React Flow Tutorial: {result['tutorial_type'].replace('_', ' ').title()}

## Overview
**Description**: {tutorial['description']}
**Difficulty**: {tutorial['difficulty']}
**Complexity**: {result['complexity'].title()}

### Concepts Covered
{chr(10).join(f"- {concept}" for concept in tutorial['concepts'])}

## Step-by-Step Tutorial
{chr(10).join(steps_content)}

### Prerequisites
{chr(10).join(f"- {prereq}" for prereq in result['prerequisites'])}

### Next Steps
{chr(10).join(f"- {step}" for step in result['next_steps'])}

### Related Resources
- **Official Examples**: {result['related_examples']['official_examples']}
- **Playground**: {result['related_examples']['playground']}
- **GitHub**: {result['related_examples']['github_repo']}

Based on official React Flow tutorials: https://reactflow.dev/learn/tutorials/
"""
    }]

def handle_react_flow_troubleshooting_expert(arguments: dict):
    """Handle troubleshooting expert tool call"""
    result = react_flow_troubleshooting_expert(
        error_type=arguments.get("error_type", "common"),
        issue_description=arguments.get("issue_description", "")
    )
    
    guide = result['troubleshooting_guide']
    
    return [{
        "type": "text",
        "text": f"""# React Flow Troubleshooting Expert

## Issue: {result['error_type'].replace('_', ' ').title()}
{f"**Description**: {result['issue_description']}" if result['issue_description'] else ""}

### Symptoms
{chr(10).join(f"- {symptom}" for symptom in guide['symptoms'])}

### Common Causes
{chr(10).join(f"- {cause}" for cause in guide['causes'])}

### Solutions
```javascript
{guide['solutions']}
```

### Debugging Tools
{chr(10).join(f"- **{tool}**: {desc}" for tool, desc in result['debugging_tools'].items())}

### Migration Guides
{chr(10).join(f"- **{version}**: {desc}" for version, desc in result['migration_guides'].items())}

### Support Resources
{chr(10).join(f"- {resource}" for resource in result['support_resources'])}

### Quick Fixes Checklist
{chr(10).join(f"- {fix}" for fix in result['common_fixes'])}

Based on official React Flow troubleshooting: https://reactflow.dev/learn/troubleshooting/common-errors
"""
    }]

def handle_react_flow_accessibility_expert(arguments: dict):
    """Handle accessibility expert tool call"""
    result = react_flow_accessibility_expert(
        feature=arguments.get("feature", "keyboard_navigation"),
        compliance_level=arguments.get("compliance_level", "WCAG_AA")
    )
    
    implementation = result['implementation_guide']
    
    return [{
        "type": "text",
        "text": f"""# React Flow Accessibility Expert

## Feature: {result['feature'].replace('_', ' ').title()}
**Compliance Level**: {result['compliance_level']}

### Requirements
{chr(10).join(f"- {req}" for req in result['requirements'])}

### Implementation Guide

#### Core Implementation
```javascript
{implementation['implementation']}
```

{f'''#### ARIA Labels
```javascript
{implementation.get('aria_labels', '')}
```''' if 'aria_labels' in implementation else ''}

{f'''#### Semantic Structure  
```javascript
{implementation.get('semantic_structure', '')}
```''' if 'semantic_structure' in implementation else ''}

{f'''#### CSS Indicators
```css
{implementation.get('css_indicators', '')}
```''' if 'css_indicators' in implementation else ''}

### Testing Tools
{chr(10).join(f"- {tool}" for tool in result['testing_tools'])}

### Best Practices
{chr(10).join(f"- {practice}" for practice in result['best_practices'])}

Based on official React Flow accessibility guide: https://reactflow.dev/learn/advanced-use/accessibility
"""
    }]

def handle_react_flow_devtools_mastery(arguments: dict):
    """Handle devtools mastery tool call"""
    result = react_flow_devtools_mastery(
        debugging_scenario=arguments.get("debugging_scenario", "performance"),
        issue_type=arguments.get("issue_type", "re_renders")
    )
    
    strategy = result['debugging_strategy']
    
    return [{
        "type": "text",
        "text": f"""# React Flow DevTools Mastery

## Debugging Scenario: {result['debugging_scenario'].replace('_', ' ').title()}
**Issue Type**: {result['issue_type']}

### Implementation Examples

{chr(10).join(f'''#### {key.replace('_', ' ').title()}
```javascript
{value}
```''' for key, value in strategy.items() if isinstance(value, str))}

### Browser DevTools Strategies

#### Performance Tab
{chr(10).join(f"- {tip}" for tip in result['browser_devtools']['performance_tab'])}

#### Console Strategies  
{chr(10).join(f"- {tip}" for tip in result['browser_devtools']['console_strategies'])}

#### Network Debugging
{chr(10).join(f"- {tip}" for tip in result['browser_devtools']['network_debugging'])}

### Official DevTools
{chr(10).join(f"- **{tool}**: {desc}" for tool, desc in result['official_devtools'].items())}

### Debugging Checklist
{chr(10).join(f"- {item}" for item in result['debugging_checklist'])}

Based on official React Flow debugging guide: https://reactflow.dev/learn/advanced-use/devtools-and-debugging
"""
    }]

# Handler mapping
REACT_FLOW_LEARNING_HANDLERS = {
    "react_flow_layouting_expert": handle_react_flow_layouting_expert,
    "react_flow_performance_mastery": handle_react_flow_performance_mastery,
    "react_flow_tutorial_generator": handle_react_flow_tutorial_generator,
    "react_flow_troubleshooting_expert": handle_react_flow_troubleshooting_expert,
    "react_flow_accessibility_expert": handle_react_flow_accessibility_expert,
    "react_flow_devtools_mastery": handle_react_flow_devtools_mastery
}