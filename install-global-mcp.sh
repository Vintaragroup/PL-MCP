#!/bin/bash

# Global MCP Server Installation
# Makes the MCP server available system-wide

MCP_INSTALL_DIR="$HOME/.local/share/frontend-mcp"
BIN_DIR="$HOME/.local/bin"

echo "🌍 Installing Frontend MCP Server globally..."

# Create installation directories
mkdir -p "$MCP_INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Copy MCP server files
cp -r /Users/ryanmorrow/Documents/Projects2025/MCP/PL-MCP/* "$MCP_INSTALL_DIR/"

# Create global mcp command
cat > "$BIN_DIR/mcp" << 'EOF'
#!/bin/bash

MCP_DIR="$HOME/.local/share/frontend-mcp"

case "$1" in
    start)
        echo "🚀 Starting Frontend MCP Server..."
        cd "$MCP_DIR"
        docker network create frontend-mcp-network 2>/dev/null || true
        docker stop frontend-mcp-server 2>/dev/null || true
        docker run -d \
            --name frontend-mcp-server \
            --rm \
            --network frontend-mcp-network \
            frontend-mcp-server \
            python -m src.frontend_mcp_server.main
        
        if [ $? -eq 0 ]; then
            echo "✅ MCP Server started!"
            echo "💡 Use 'mcp status' to check server health"
        else
            echo "❌ Failed to start MCP server"
        fi
        ;;
    
    stop)
        echo "🛑 Stopping MCP Server..."
        docker stop frontend-mcp-server 2>/dev/null || true
        echo "✅ MCP Server stopped"
        ;;
    
    status)
        if docker ps | grep -q frontend-mcp-server; then
            echo "✅ MCP Server is running"
            docker ps | grep frontend-mcp-server
        else
            echo "❌ MCP Server is not running"
        fi
        ;;
    
    restart)
        echo "🔄 Restarting MCP Server..."
        $0 stop
        sleep 2
        $0 start
        ;;
        
    build)
        echo "🔨 Building MCP Server Docker image..."
        cd "$MCP_DIR"
        docker build -t frontend-mcp-server .
        ;;
    
    logs)
        echo "📋 MCP Server logs:"
        docker logs frontend-mcp-server
        ;;
        
    add)
        if [ -z "$2" ]; then
            echo "📁 Adding MCP to current directory..."
            PROJECT_DIR=$(pwd)
        else
            echo "📁 Adding MCP to $2..."
            PROJECT_DIR="$2"
        fi
        
        cd "$PROJECT_DIR"
        bash "$MCP_DIR/add-mcp-to-project.sh"
        ;;
    
    tools)
        echo "🛠️ Available MCP Tools (16 total):"
        echo ""
        echo "📱 Core Frontend Tools (4):"
        echo "   • React Component Generator"
        echo "   • Tailwind CSS Suggester" 
        echo "   • Package Analyzer"
        echo "   • React Hook Generator"
        echo ""
        echo "🌊 React Flow API Tools (6):"
        echo "   • Hook Examples"
        echo "   • Advanced Components"
        echo "   • Utilities Generator"
        echo "   • TypeScript Definitions"
        echo "   • Performance Optimizer"
        echo "   • Accessibility Enhancer"
        echo ""
        echo "📚 React Flow Learning Tools (6):"
        echo "   • Layouting Expert"
        echo "   • Performance Mastery"
        echo "   • Tutorial Generator"
        echo "   • Troubleshooting Expert"
        echo "   • Accessibility Expert"
        echo "   • DevTools Mastery"
        ;;
    
    *)
        echo "🎯 Frontend MCP Server - Global Command"
        echo ""
        echo "Usage: mcp <command>"
        echo ""
        echo "Commands:"
        echo "  start     Start the MCP server"
        echo "  stop      Stop the MCP server"
        echo "  restart   Restart the MCP server"
        echo "  status    Check if MCP server is running"
        echo "  logs      View MCP server logs"
        echo "  build     Build MCP server Docker image"
        echo "  tools     List all available tools"
        echo "  add [dir] Add MCP integration to a project"
        echo ""
        echo "Examples:"
        echo "  mcp start                 # Start server globally"
        echo "  mcp add                   # Add to current project"
        echo "  mcp add /path/to/project  # Add to specific project"
        echo "  mcp tools                 # List all 16 tools"
        ;;
esac
EOF

chmod +x "$BIN_DIR/mcp"

# Add to PATH if not already there
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo ""
    echo "📝 Add to your shell profile (~/.zshrc or ~/.bashrc):"
    echo "export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
fi

echo "🎉 Global MCP Installation Complete!"
echo ""
echo "🌍 Available commands:"
echo "  mcp start    - Start MCP server"
echo "  mcp stop     - Stop MCP server"  
echo "  mcp status   - Check server status"
echo "  mcp add      - Add MCP to current project"
echo "  mcp tools    - List all 16 available tools"
echo ""
echo "💡 Run 'mcp' for full command list"