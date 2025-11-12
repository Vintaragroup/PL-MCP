# PL-MCP Quick Start Guide

Get started with PL-MCP in 5 minutes!

## 🚀 Installation (Choose One)

### Option 1: Docker (Easiest)
```bash
git clone https://github.com/Vintaragroup/PL-MCP.git
cd PL-MCP
docker build -t frontend-mcp-server .
docker run -d --name frontend-mcp -p 8000:8000 frontend-mcp-server
```

### Option 2: Local Python
```bash
git clone https://github.com/Vintaragroup/PL-MCP.git
cd PL-MCP
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/frontend_mcp_server/main.py
```

### Option 3: Add to Existing Project
```bash
cd /path/to/your/project
curl -O https://raw.githubusercontent.com/Vintaragroup/PL-MCP/main/add-mcp-to-project.sh
chmod +x add-mcp-to-project.sh
./add-mcp-to-project.sh
```

---

## 💡 Common Tasks

### Generate a React Component
```bash
python3 simple_mcp_client.py react_component \
  --name "UserCard" \
  --props "name:string,age:number,email:string" \
  --styling "tailwind"
```

### Get Tailwind CSS Classes
```bash
python3 simple_mcp_client.py tailwind_suggest \
  --description "Blue gradient button with hover effect" \
  --type "button"
```

### Create a Custom Hook
```bash
python3 simple_mcp_client.py react_hook \
  --name "useAuth" \
  --functionality "Manage user authentication state and JWT tokens"
```

### Generate React Flow Diagram
```bash
python3 simple_mcp_client.py react_flow_layouting_expert \
  --query "hierarchical_layouts" \
  --description "Create an organizational chart with 3 departments"
```

### Optimize Large React Flow Graph
```bash
python3 simple_mcp_client.py react_flow_performance_mastery \
  --nodes "large_1000_10000" \
  --focus "rendering_performance"
```

---

## 🔧 GitHub Copilot Integration

### Step 1: Configure VS Code

Create `.vscode/settings.json`:
```json
{
  "github.copilot.enable": true,
  "modelContext.mcp": {
    "enabled": true,
    "servers": {
      "frontend-mcp": {
        "command": "python3",
        "args": ["${workspaceFolder}/src/frontend_mcp_server/main.py"],
        "env": { "PYTHONUNBUFFERED": "1" }
      }
    }
  }
}
```

### Step 2: Use with Copilot Chat

Open Copilot Chat and ask:
- "Generate a React Flow diagram for a multi-step checkout process"
- "Create an accessible modal component with Tailwind CSS"
- "Optimize my React component for 500+ nodes"
- "What's the best layout algorithm for a mindmap?"

---

## 📚 Example Prompts

### For Component Development
```
"Create a reusable Card component with TypeScript and Tailwind CSS that supports dark mode"
```

### For React Flow
```
"Generate a workflow diagram with a decision node that branches into 3 paths. Use Dagre layout."
```

### For Performance
```
"I have a React Flow diagram with 5000 nodes. How can I optimize it for smooth 60fps rendering?"
```

### For Accessibility
```
"Make my React Flow component fully keyboard navigable and screen reader compatible (WCAG AA)"
```

---

## 🔍 Available Commands

### List All Tools
```bash
python3 simple_mcp_client.py list_tools
```

### React Flow Tools
- `react_flow_layouting_expert` - Layout advice
- `react_flow_performance_mastery` - Performance optimization
- `react_flow_troubleshooting_expert` - Debugging help
- `react_flow_accessibility_expert` - Accessibility guidance
- `react_flow_devtools_mastery` - Browser debugging

### Component Tools
- `react_component` - Generate components
- `react_hook` - Generate hooks
- `tailwind_suggest` - Get CSS classes
- `package_analyzer` - Analyze package.json

### Connection Tools
- `generate_connection_aware_node` - Smart node positioning
- `codex_positioning_prompts` - Codex integration
- `dagre_configuration_optimizer` - Layout optimization
- `whiteboard_layout_optimizer` - Whiteboard mode

---

## 📊 Use Cases

### Use Case 1: Build a Workflow Application
```
1. Generate diagram: react_flow_diagram_generator
2. Optimize layout: dagre_configuration_optimizer
3. Add performance: react_flow_performance_mastery
4. Make accessible: react_flow_accessibility_enhancer
```

### Use Case 2: Create Component Library
```
1. Generate components: react_component_generator
2. Add styling: tailwind_class_suggester
3. Build hooks: react_hook_generator
4. Add types: react_flow_typescript_definitions
```

### Use Case 3: Optimize Existing App
```
1. Identify bottleneck: react_flow_devtools_mastery
2. Get strategy: react_flow_performance_mastery
3. Implement: react_flow_utilities_generator
4. Test: Performance metrics
```

---

## 🐛 Troubleshooting

### Docker not starting?
```bash
# Check logs
docker logs frontend-mcp

# Rebuild image
docker build --no-cache -t frontend-mcp-server .
```

### Python dependencies missing?
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Can't connect to MCP server?
```bash
# Test server directly
python3 src/frontend_mcp_server/main.py

# Test with client
python3 simple_mcp_client.py list_tools
```

---

## 📖 Full Documentation

- **[README.md](./README.md)** - Complete overview and installation
- **[FEATURES.md](./FEATURES.md)** - Detailed tool documentation
- **[INTEGRATION-GUIDE.md](./INTEGRATION-GUIDE.md)** - Deep integration guide
- **[README-COPILOT-INTEGRATION.md](./README-COPILOT-INTEGRATION.md)** - Copilot setup
- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Production deployment

---

## 🤝 Getting Help

1. **Check Examples:** See `/examples/` directory
2. **Read Docs:** Full documentation in repository
3. **GitHub Issues:** Report bugs or ask questions
4. **Discussions:** Join community discussions

---

## ⚡ Performance Tips

- **Large Graphs (1000+ nodes):** Use virtualization with `react_flow_performance_mastery`
- **Complex Layouts:** Use ELK.js instead of Dagre with `react_flow_elk_layout_generator`
- **Real-time Updates:** Use batch updates and debouncing from `react_flow_utilities_generator`
- **Mobile:** Use viewport culling and responsive design from `whiteboard_layout_optimizer`

---

## 🎯 Next Steps

1. ✅ Install PL-MCP
2. ✅ Run your first command: `python3 simple_mcp_client.py list_tools`
3. ✅ Generate a component or diagram
4. ✅ Integrate with GitHub Copilot
5. ✅ Join the community and share your creations!

---

**Questions?** Check the [documentation](./README.md) or open an issue on GitHub.

**Happy Building! 🚀**
