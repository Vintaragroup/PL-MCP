// Example: Ask GitHub Copilot Chat:
// "@workspace Generate a React Flow mind map component with the MCP tools"

import React, { useState, useCallback } from 'react';
import ReactFlow, { 
  Node, 
  Edge, 
  addEdge, 
  Connection, 
  useNodesState, 
  useEdgesState 
} from 'reactflow';

// This is where you would normally write your component
// But with MCP + GitHub Copilot, you can:

// 1. Ask for React Flow patterns: "@workspace Show me React Flow hook patterns"
// 2. Get Tailwind suggestions: "@workspace Suggest Tailwind classes for a modern card design"  
// 3. Generate components: "@workspace Create a custom React Flow node component"
// 4. Optimize performance: "@workspace How to optimize React Flow for large datasets"
// 5. Add accessibility: "@workspace Make this React Flow accessible with WCAG AA compliance"

// Try asking GitHub Copilot Chat any of these questions!
// The MCP server will provide specialized knowledge and code examples.

export default function MindMapDemo() {
  // GitHub Copilot will have enhanced context here
  // Ask it to generate the full mind map implementation!
  
  return (
    <div className="w-full h-screen">
      <h1 className="text-2xl font-bold p-4">
        MCP + GitHub Copilot Demo
      </h1>
      <p className="p-4 text-gray-600">
        Ask GitHub Copilot Chat to generate React Flow components using the MCP tools!
      </p>
      {/* Ask Copilot to complete this React Flow implementation */}
    </div>
  );
}