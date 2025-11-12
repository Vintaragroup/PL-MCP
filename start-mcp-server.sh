#!/bin/bash

# Frontend MCP Server Startup Script
# This script starts the MCP server for use with GitHub Copilot

echo "🚀 Starting Frontend MCP Server..."
echo "📦 This server provides 16 specialized tools for React, Tailwind, and React Flow development"

# Ensure Docker network exists
docker network create frontend-mcp-network 2>/dev/null || true

# Start the MCP server in the background
docker run -d \
    --name frontend-mcp-server \
    --rm \
    --network frontend-mcp-network \
    frontend-mcp-server \
    python -m src.frontend_mcp_server.main

echo "✅ Frontend MCP Server is now running!"
echo "🔗 Available tools:"
echo "   📱 React Component Generator"
echo "   🎨 Tailwind CSS Class Suggester" 
echo "   📦 Package Analyzer"
echo "   🪝 React Hook Generator"
echo "   🌊 React Flow Tools (6 tools)"
echo "   📚 React Flow Learning Tools (6 tools)"
echo ""
echo "💡 The server is now ready to assist GitHub Copilot with frontend development!"
echo "🔧 Use Copilot Chat to ask questions about React, Tailwind, or React Flow"
echo ""
echo "To stop the server: docker stop frontend-mcp-server"