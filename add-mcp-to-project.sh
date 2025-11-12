#!/bin/bash

# Add MCP Server to Existing Project
# Run this script from your project root directory

PROJECT_DIR=$(pwd)
PROJECT_NAME=$(basename "$PROJECT_DIR")

echo "🚀 Adding Frontend MCP Server to project: $PROJECT_NAME"
echo "📁 Project directory: $PROJECT_DIR"

# Create MCP configuration directory
mkdir -p .mcp

# Create MCP server startup script for this project
cat > .mcp/start-mcp.sh << 'EOF'
#!/bin/bash

# Project-specific MCP server startup
echo "🚀 Starting Frontend MCP Server for $(basename $(pwd))..."

# Ensure Docker network exists
docker network create frontend-mcp-network 2>/dev/null || true

# Stop any existing MCP server
docker stop frontend-mcp-server 2>/dev/null || true

# Start fresh MCP server
docker run -d \
    --name frontend-mcp-server \
    --rm \
    --network frontend-mcp-network \
    frontend-mcp-server \
    python -m src.frontend_mcp_server.main

if [ $? -eq 0 ]; then
    echo "✅ MCP Server started successfully!"
    echo "🔗 Available tools:"
    echo "   📱 React Component Generator"
    echo "   🎨 Tailwind CSS Suggester"
    echo "   📦 Package Analyzer" 
    echo "   🪝 React Hook Generator"
    echo "   🌊 React Flow Tools (6 tools)"
    echo "   📚 React Flow Learning Tools (6 tools)"
    echo ""
    echo "💡 GitHub Copilot now has enhanced frontend expertise!"
    echo "🔧 Ask Copilot Chat questions about React, Tailwind, or React Flow"
else
    echo "❌ Failed to start MCP server"
    echo "💡 Make sure the frontend-mcp-server Docker image exists"
    echo "🛠️ Build it with: docker build -t frontend-mcp-server /path/to/mcp/project"
fi
EOF

chmod +x .mcp/start-mcp.sh

# Create MCP stop script
cat > .mcp/stop-mcp.sh << 'EOF'
#!/bin/bash
echo "🛑 Stopping Frontend MCP Server..."
docker stop frontend-mcp-server 2>/dev/null || true
echo "✅ MCP Server stopped"
EOF

chmod +x .mcp/stop-mcp.sh

# Create VS Code workspace settings that include MCP awareness
mkdir -p .vscode
cat > .vscode/settings.json << 'EOF'
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false,
    "markdown": true
  },
  "github.copilot.advanced": {},
  "files.associations": {
    "*.tsx": "typescriptreact",
    "*.ts": "typescript"
  },
  "emmet.includeLanguages": {
    "typescriptreact": "html"
  },
  "typescript.preferences.includePackageJsonAutoImports": "on",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  }
}
EOF

# Add MCP integration instructions to package.json scripts (if exists)
if [ -f package.json ]; then
    echo "📦 Found package.json - adding MCP scripts..."
    
    # Create a temp file with updated package.json
    node -e "
    const fs = require('fs');
    const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    
    if (!pkg.scripts) pkg.scripts = {};
    
    pkg.scripts['mcp:start'] = './.mcp/start-mcp.sh';
    pkg.scripts['mcp:stop'] = './.mcp/stop-mcp.sh';
    pkg.scripts['mcp:status'] = 'docker ps | grep frontend-mcp-server || echo \"MCP server not running\"';
    
    fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
    " 2>/dev/null || echo "⚠️ Could not update package.json scripts (Node.js not found)"
fi

# Create project-specific README for MCP
cat > .mcp/README.md << EOF
# MCP Integration for $PROJECT_NAME

## Quick Start

\`\`\`bash
# Start MCP server
npm run mcp:start
# OR
./.mcp/start-mcp.sh

# Check status
npm run mcp:status

# Stop server
npm run mcp:stop
\`\`\`

## Using with GitHub Copilot

Once the MCP server is running, GitHub Copilot Chat has access to 16 specialized tools:

### Enhanced Prompts You Can Use:

\`\`\`
Generate a React component for [your feature] with TypeScript and Tailwind CSS
\`\`\`

\`\`\`
How do I optimize React Flow performance for my use case?
\`\`\`

\`\`\`
Create a custom React Flow node component for [your domain]
\`\`\`

\`\`\`
Suggest Tailwind classes for [your design description]
\`\`\`

\`\`\`
Analyze my package.json for optimization opportunities
\`\`\`

### Tips for Better Results:
1. **Use Copilot Chat** (not just autocomplete)
2. **Be specific** about React Flow, Tailwind, TypeScript
3. **Mention performance** requirements if relevant
4. **Ask for explanations** of recommended patterns
5. **Reference the MCP knowledge** in your prompts

## Available Tools
- **Frontend Core** (4): React, Tailwind, Packages, Hooks
- **React Flow API** (6): Advanced React Flow capabilities  
- **React Flow Learning** (6): Tutorials and expert guidance

## Benefits
- 🧠 Enhanced GitHub Copilot responses
- 🎯 Specialized frontend knowledge
- ⚡ Performance optimization guidance
- ♿ Accessibility best practices
- 📚 Tutorial generation
- 🔧 Expert troubleshooting
EOF

# Copy MCP context for Copilot reference
cp "$MCP_DIR/mcp-context-for-copilot.md" .mcp/copilot-context.md 2>/dev/null || echo "# MCP Context available - see .mcp/README.md" > .mcp/copilot-context.md

echo ""
echo "🎉 MCP Integration Complete!"
echo ""
echo "📁 Created:"
echo "   .mcp/start-mcp.sh     - Start MCP server"
echo "   .mcp/stop-mcp.sh      - Stop MCP server"  
echo "   .mcp/README.md        - Integration guide"
echo "   .vscode/settings.json - VS Code configuration"
echo ""

if [ -f package.json ]; then
    echo "📦 Added npm scripts:"
    echo "   npm run mcp:start   - Start MCP server"
    echo "   npm run mcp:stop    - Stop MCP server"
    echo "   npm run mcp:status  - Check server status"
    echo ""
fi

echo "🚀 Next Steps:"
echo "1. Start MCP server: npm run mcp:start"
echo "2. Open VS Code: code ."
echo "3. Use GitHub Copilot Chat with enhanced frontend expertise!"
echo ""
echo "💡 The MCP server provides 16 specialized tools for React, Tailwind, and React Flow"