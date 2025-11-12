# 🚀 Adding MCP Server to Existing Projects

## Method 1: Quick Project Integration (Recommended)

### For Any Existing Project:

```bash
# Navigate to your project
cd /path/to/your/project

# Run the integration script
curl -s https://raw.githubusercontent.com/your-repo/frontend-mcp/main/add-mcp-to-project.sh | bash
# OR copy the script locally:
/Users/ryanmorrow/Documents/Projects2025/MCP/PL-MCP/add-mcp-to-project.sh
```

**What this does:**
- ✅ Creates `.mcp/` directory with startup scripts
- ✅ Adds VS Code settings for Copilot optimization
- ✅ Updates `package.json` with MCP scripts
- ✅ Creates project-specific documentation

### Start Using:
```bash
# Start MCP server for this project
npm run mcp:start

# Check status
npm run mcp:status

# Stop when done
npm run mcp:stop
```

---

## Method 2: Global Installation

### Install MCP Globally:
```bash
# Install globally (one-time setup)
/Users/ryanmorrow/Documents/Projects2025/MCP/PL-MCP/install-global-mcp.sh
```

### Use in Any Project:
```bash
# Navigate to any project
cd /path/to/any/project

# Add MCP integration
mcp add

# Start server
mcp start

# Check status
mcp status
```

---

## Method 3: Manual Integration

### 1. Create MCP Configuration
```bash
# In your project root
mkdir .mcp
```

### 2. Create Startup Script
```bash
cat > .mcp/start-mcp.sh << 'EOF'
#!/bin/bash
docker network create frontend-mcp-network 2>/dev/null || true
docker stop frontend-mcp-server 2>/dev/null || true
docker run -d \
    --name frontend-mcp-server \
    --rm \
    --network frontend-mcp-network \
    frontend-mcp-server \
    python -m src.frontend_mcp_server.main
echo "✅ MCP Server started for $(basename $(pwd))"
EOF

chmod +x .mcp/start-mcp.sh
```

### 3. Update Package.json
```json
{
  "scripts": {
    "mcp:start": "./.mcp/start-mcp.sh",
    "mcp:stop": "docker stop frontend-mcp-server",
    "mcp:status": "docker ps | grep frontend-mcp-server"
  }
}
```

### 4. Configure VS Code
```json
// .vscode/settings.json
{
  "github.copilot.enable": {
    "*": true,
    "typescript": true,
    "typescriptreact": true
  },
  "github.copilot.advanced": {
    "debug.overrideEngine": "codex"
  }
}
```

---

## 🎯 Project-Specific Examples

### React/Next.js Project
```bash
# Your existing Next.js project
cd my-nextjs-app
mcp add
mcp start

# Now ask GitHub Copilot:
# "Generate a Next.js page component with Tailwind styling and TypeScript"
```

### React Flow Project  
```bash
# Your existing React Flow project
cd my-flow-app
mcp add
mcp start

# Now ask GitHub Copilot:
# "Optimize this React Flow for 5000+ nodes with performance monitoring"
```

### Component Library
```bash
# Your component library
cd my-components
mcp add  
mcp start

# Now ask GitHub Copilot:
# "Generate a reusable React component with proper TypeScript props and Tailwind variants"
```

---

## 🔧 Verification Steps

### 1. Check MCP Server is Running
```bash
mcp status
# OR
docker ps | grep frontend-mcp-server
```

### 2. Test GitHub Copilot Integration
Open GitHub Copilot Chat and ask:
```
Generate a React component with Tailwind CSS for a user profile card
```

You should get enhanced responses with:
- Proper TypeScript interfaces
- Tailwind class suggestions
- Accessibility considerations
- Performance optimization tips

### 3. Test React Flow Knowledge
Ask Copilot Chat:
```
How do I create a React Flow mind map with collapsible nodes for 1000+ items?
```

You should get:
- Specific React Flow hook usage
- Performance optimization strategies
- Layout algorithm recommendations
- Memory management tips

---

## 📁 Project Structure After Integration

```
your-project/
├── .mcp/
│   ├── start-mcp.sh        # Start MCP server
│   ├── stop-mcp.sh         # Stop MCP server  
│   └── README.md           # MCP usage guide
├── .vscode/
│   └── settings.json       # Optimized for Copilot + MCP
├── package.json            # Updated with MCP scripts
└── [your existing files]
```

---

## 💡 Enhanced GitHub Copilot Prompts

Once MCP is integrated, try these enhanced prompts:

### React Components
```
Generate a React TypeScript component for [feature] with proper props, Tailwind styling, and accessibility features
```

### React Flow
```
Create a React Flow [type] diagram with [performance requirements] and [specific features]
```

### Performance
```
Optimize this React component for [scenario] with proper memoization and state management
```

### Tailwind CSS
```
Suggest Tailwind classes for [design description] with responsive design and dark mode support
```

### Troubleshooting
```
Debug why [specific issue] and provide step-by-step troubleshooting guide
```

---

## 🚀 Success Indicators

You'll know the integration is working when:

✅ **GitHub Copilot Chat** provides more detailed, specialized responses  
✅ **Code suggestions** include React Flow specific patterns  
✅ **Tailwind recommendations** are more contextual and complete  
✅ **Performance advice** includes specific optimization strategies  
✅ **TypeScript support** is enhanced with proper interfaces  
✅ **Accessibility guidance** includes WCAG compliance patterns  

---

## 🛠️ Troubleshooting

### MCP Server Not Starting
```bash
# Check Docker image exists
docker images | grep frontend-mcp-server

# Build if missing
cd /Users/ryanmorrow/Documents/Projects2025/MCP/PL-MCP
docker build -t frontend-mcp-server .

# Check for port conflicts
docker ps -a
```

### Copilot Not Using MCP Knowledge
1. Ensure MCP server is running: `mcp status`
2. Restart VS Code
3. Be specific in your prompts (mention React Flow, Tailwind, etc.)
4. Use GitHub Copilot Chat (not just autocomplete)

### Project Scripts Not Working
```bash
# Check scripts were added
cat package.json | grep mcp

# Manual start if needed
./.mcp/start-mcp.sh
```

Start building with enhanced AI assistance! 🎯