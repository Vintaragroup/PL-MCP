# PL-MCP: Frontend Development MCP Server

A comprehensive **Model Context Protocol (MCP)** server for advanced frontend development with specialized tools for React Flow, Tailwind CSS, TypeScript, and component architecture optimization.

## 🚀 Overview

PL-MCP is a sophisticated MCP server that extends your development workflow with 16+ specialized frontend development tools. It integrates seamlessly with GitHub Copilot and other AI-powered development environments to provide expert-level guidance on:

- **React Flow Diagrams** - Complex flow visualization and layouting
- **React Component Development** - Best practices and optimization
- **Tailwind CSS** - Utility class optimization and design patterns
- **TypeScript** - Type definitions and architectural patterns
- **Performance Optimization** - Large dataset handling and rendering efficiency
- **Accessibility** - WCAG compliance and inclusive design
- **Testing Strategies** - Component and integration testing approaches

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Tools Reference](#tools-reference)
- [Integration with GitHub Copilot](#integration-with-github-copilot)
- [Docker Deployment](#docker-deployment)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Tools (16+ Specialized Engines)

#### 1. **React Flow Ecosystem** (6 tools)
- Flow diagram generation and visualization
- Custom node and edge creation
- Edge analysis and relationship mapping
- Automatic layout optimization (Dagre, D3-Force, D3-Hierarchy, ELK.js)
- Hierarchical tree generation
- Advanced ELK layout configurations

#### 2. **React Flow API Tools** (6 tools)
- Hook examples and patterns (useReactFlow, useStore, useConnection, etc.)
- Advanced component implementations (Handle, NodeToolbar, MiniMap, Controls)
- Utility function generators (edge utilities, node utilities, viewport calculations)
- TypeScript definitions and type safety
- Performance optimization strategies
- Accessibility enhancement implementations

#### 3. **React Flow Learning Tools** (6 tools)
- Layout algorithm expertise with official React Flow documentation
- Performance mastery for large-scale applications
- Interactive tutorial generation
- Troubleshooting and debugging guidance
- Accessibility best practices
- Browser DevTools integration strategies

#### 4. **Connection-Aware Positioning Tools** (5 tools)
- Connection-side node placement
- Codex integration prompts
- Dagre configuration optimization
- Handle positioning guides
- Whiteboard layout optimization

#### 5. **Core Frontend Tools** (4 tools)
- React component generation with TypeScript
- Tailwind CSS class suggestions
- Package.json analysis and optimization
- Custom React hook generation

### Integration Features

✅ **GitHub Copilot Integration** - Direct MCP integration for AI-powered suggestions  
✅ **VS Code Workspace Configuration** - Pre-configured for seamless development  
✅ **Docker Containerization** - Portable, isolated server environment  
✅ **Standalone CLI** - Python client for direct tool access  
✅ **WebSocket Support** - Real-time communication with editor  

## 🏗️ Architecture

### System Components

```
PL-MCP/
├── src/frontend_mcp_server/
│   ├── main.py                           # MCP server entry point
│   ├── tools/
│   │   ├── react_flow_tools.py          # Diagram generation & visualization
│   │   ├── react_flow_api_tools.py      # Official API implementations
│   │   ├── react_flow_learning_tools.py # Learning & expertise tools
│   │   ├── connection_positioning_tools.py # Connection-aware positioning
│   │   ├── package_tools.py             # Dependency analysis
│   │   ├── react_tools.py               # Component generation
│   │   ├── tailwind_tools.py            # Style optimization
│   │   └── typescript_tools.py          # Type definitions
│   └── __init__.py
├── Dockerfile                            # Container configuration
├── docker-compose.yml                    # Multi-container orchestration
├── requirements.txt                      # Python dependencies
├── mcp_client.py                         # Async MCP client
├── simple_mcp_client.py                  # CLI client interface
└── README.md                             # This file
```

### Key Technologies

- **MCP Server** - Model Context Protocol for AI integration
- **React Flow v11+** - Flow diagram library with advanced layouts
- **Dagre** - Graph layout algorithm
- **D3-Force & D3-Hierarchy** - Advanced force-directed & hierarchical layouts
- **ELK.js** - Integrated Layout Kernel for complex graphs
- **Docker** - Containerization and deployment
- **Python 3.11+** - Server implementation
- **TypeScript** - Type-safe frontend code generation

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- Docker & Docker Compose (for containerized deployment)
- Node.js 16+ (for React Flow projects)
- Git

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/Vintaragroup/PL-MCP.git
cd PL-MCP

# Build the Docker image
docker build -t frontend-mcp-server .

# Create Docker network (optional, for service communication)
docker network create frontend-mcp-network

# Run the container
docker run -d \
  --name frontend-mcp-server \
  --network frontend-mcp-network \
  -p 8000:8000 \
  frontend-mcp-server
```

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/Vintaragroup/PL-MCP.git
cd PL-MCP

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python3 src/frontend_mcp_server/main.py
```

### Option 3: Add to Existing Project

```bash
# Copy integration script
cp add-mcp-to-project.sh /path/to/your/project/
chmod +x /path/to/your/project/add-mcp-to-project.sh

# Run integration
cd /path/to/your/project
./add-mcp-to-project.sh
```

## 🛠️ Usage

### Quick Start with CLI

```bash
# List available tools
python3 simple_mcp_client.py list_tools

# Generate a React component
python3 simple_mcp_client.py react_component \
  --name "UserCard" \
  --props "name:string,age:number,email:string"

# Suggest Tailwind classes
python3 simple_mcp_client.py tailwind_suggest \
  --description "Create a gradient button with hover effect" \
  --type "button"

# Generate a custom React hook
python3 simple_mcp_client.py react_hook \
  --name "useAuth" \
  --functionality "Manage user authentication state"

# Get React Flow layout advice
python3 simple_mcp_client.py react_flow_layouting_expert \
  --query "hierarchical_layouts" \
  --description "Create a decision tree diagram"
```

### Integration with GitHub Copilot

1. **Configure VS Code:**
   ```json
   {
     "github.copilot.enable": true,
     "github.copilot.chat.followUps": "on",
     "modelContext.mcp": {
       "enabled": true,
       "servers": [
         {
           "name": "frontend-mcp-server",
           "command": "python3",
           "args": ["/path/to/src/frontend_mcp_server/main.py"],
           "env": { "PYTHONUNBUFFERED": "1" }
         }
       ]
     }
   }
   ```

2. **Open your project and start asking Copilot:**
   - "Generate a React Flow diagram for my workflow"
   - "Create an accessible card component with Tailwind"
   - "Set up TypeScript types for my React Flow data"
   - "Optimize my component performance for 1000+ nodes"

### Standalone MCP Client

```python
import asyncio
from mcp_client import MCPClient

async def main():
    client = MCPClient()
    
    # Generate a component
    response = await client.call_tool("react_component_generator", {
        "component_name": "UserProfile",
        "props": [
            {"name": "userId", "type": "string"},
            {"name": "onUpdate", "type": "(data: UserData) => void"}
        ],
        "styling": "tailwind"
    })
    
    print(response)

asyncio.run(main())
```

## 📚 Tools Reference

### React Component Tools

#### `react_component_generator`
Generate TypeScript React components with full type safety and best practices.

**Parameters:**
- `component_name` (string) - Component name
- `props` (array) - Component props with types
- `styling` (string) - Styling approach: tailwind, css-modules, styled-components, none

**Example:**
```bash
python3 simple_mcp_client.py react_component \
  --name "SearchBar" \
  --props "onSearch:function,placeholder:string"
```

---

### React Flow Tools

#### `react_flow_layouting_expert`
Get expert guidance on React Flow layout algorithms and implementations.

**Parameters:**
- `query_type` (string) - Layout type: connection_aware_positioning, hierarchical_layouts, etc.
- `description` (string) - Your specific use case

**Example:**
```bash
python3 simple_mcp_client.py react_flow_layouting_expert \
  --query "hierarchical_layouts" \
  --description "Organizational chart with department grouping"
```

---

#### `react_flow_performance_mastery`
Optimize React Flow applications for handling large node counts.

**Parameters:**
- `node_count_range` (string) - Expected nodes: small, medium, large, xlarge
- `performance_focus` (string) - Rendering, memory, or interaction performance

**Example:**
```bash
python3 simple_mcp_client.py react_flow_performance_mastery \
  --nodes "large_1000_10000" \
  --focus "rendering_performance"
```

---

#### `generate_connection_aware_node`
Generate nodes that automatically position on the correct connection side.

**Parameters:**
- `connection_side` (string) - right, left, top, bottom
- `layout_style` (string) - whiteboard, hierarchical, organic, tree
- `auto_layout` (boolean) - Apply automatic layout

**Example:**
```bash
python3 simple_mcp_client.py connection_aware_node \
  --side "right" \
  --style "whiteboard"
```

---

### Tailwind CSS Tools

#### `tailwind_class_suggester`
Get optimized Tailwind CSS class suggestions.

**Parameters:**
- `design_description` (string) - Design requirements
- `element_type` (string) - button, card, form, navigation, etc.
- `responsive` (boolean) - Include responsive variants

**Example:**
```bash
python3 simple_mcp_client.py tailwind_suggest \
  --description "Dark mode card with shadow and hover effect" \
  --type "card"
```

---

### Package Analysis Tools

#### `package_analyzer`
Analyze package.json for dependencies, vulnerabilities, and optimization.

**Parameters:**
- `package_json` (string) - Content of package.json
- `analysis_type` (string) - dependencies, vulnerabilities, optimization, all

---

### React Hook Tools

#### `react_hook_generator`
Generate custom React hooks with TypeScript support.

**Parameters:**
- `hook_name` (string) - Hook name
- `functionality` (string) - What the hook does

**Example:**
```bash
python3 simple_mcp_client.py react_hook \
  --name "useLocalStorage" \
  --functionality "Persist state to browser localStorage"
```

---

## 🔌 Integration with GitHub Copilot

### Setup Instructions

1. **Configure MCP Server in VS Code:**

   Create or update `.vscode/settings.json`:

   ```json
   {
     "modelContext.mcp": {
       "enabled": true,
       "servers": {
         "frontend-mcp": {
           "command": "python3",
           "args": ["${workspaceFolder}/src/frontend_mcp_server/main.py"],
           "env": {
             "PYTHONUNBUFFERED": "1"
           }
         }
       }
     }
   }
   ```

2. **Use in Copilot Chat:**

   ```
   @frontend-mcp Generate a React Flow diagram for a multi-step workflow with proper layout optimization
   ```

3. **Direct Project Integration:**

   Use the provided integration script:
   ```bash
   ./add-mcp-to-project.sh
   ```

### Example Prompts for Copilot

- "Create a React Flow component that handles 500+ nodes with performance optimization"
- "Generate accessible form components with Tailwind CSS and WCAG AA compliance"
- "Set up TypeScript types for a complex Redux state management pattern"
- "Optimize my React component that's rendering 1000 nodes - what's the bottleneck?"
- "Generate a custom hook for managing infinite scroll pagination"

## 🐳 Docker Deployment

### Build and Run

```bash
# Build image
docker build -t frontend-mcp-server .

# Create network
docker network create frontend-mcp-network

# Run container
docker run -d \
  --name frontend-mcp-server \
  --network frontend-mcp-network \
  -p 8000:8000 \
  -e PYTHONUNBUFFERED=1 \
  frontend-mcp-server

# View logs
docker logs -f frontend-mcp-server
```

### Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f frontend-mcp-server

# Stop services
docker-compose down
```

### Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check status
kubectl get pods
kubectl get services
```

## ⚙️ Configuration

### Environment Variables

```bash
# Server configuration
MCP_SERVER_PORT=8000
MCP_SERVER_HOST=0.0.0.0
MCP_LOG_LEVEL=INFO

# React Flow configuration
REACT_FLOW_DEFAULT_LAYOUT=dagre
REACT_FLOW_AUTO_LAYOUT=true

# Performance tuning
MCP_MAX_WORKERS=4
MCP_CACHE_SIZE=100
```

### Project Configuration

Create `.mcp-config.json` in your project root:

```json
{
  "react_flow": {
    "default_layout": "dagre",
    "layout_direction": "LR",
    "auto_fit": true,
    "spacing": {
      "horizontal": 200,
      "vertical": 150
    }
  },
  "tailwind": {
    "color_mode": "auto",
    "breakpoints": ["sm", "md", "lg", "xl", "2xl"]
  },
  "typescript": {
    "strict_mode": true,
    "target": "ES2020"
  }
}
```

## 📖 Documentation

### Getting Started Guides

- [React Flow Integration Guide](./INTEGRATION-GUIDE.md)
- [GitHub Copilot Setup](./README-COPILOT-INTEGRATION.md)
- [VS Code Integration](./VSCODE_INTEGRATION.md)
- [Deployment Guide](./DEPLOYMENT.md)

### API Reference

- [React Flow API Tools](./src/frontend_mcp_server/tools/react_flow_api_tools.py)
- [React Flow Learning Tools](./src/frontend_mcp_server/tools/react_flow_learning_tools.py)
- [Connection Positioning Tools](./src/frontend_mcp_server/tools/connection_positioning_tools.py)

### Tutorials & Examples

- [React Flow Diagram Examples](./examples/)
- [Component Generator Examples](./demo-project/)
- [MCP Client Usage](./mcp_client.py)

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python3 -m pytest tests/

# Run specific test suite
python3 -m pytest tests/test_react_flow_tools.py

# Run with coverage
python3 -m pytest --cov=src tests/
```

### Manual Testing

```bash
# Test server connectivity
python3 test_server.py

# Test API tools
python3 test_api_tools.py

# Test learning tools
python3 test_learning_tools.py
```

## 🚀 Performance

### Optimization Strategies

- **Node Virtualization** - Handle 10,000+ nodes efficiently
- **Memoization** - Prevent unnecessary re-renders
- **Web Workers** - Offload heavy computations
- **Lazy Loading** - Load data on demand
- **Viewport Culling** - Only render visible nodes

### Benchmarks

- Small graphs (10-100 nodes): < 100ms layout time
- Medium graphs (100-1000 nodes): < 500ms layout time
- Large graphs (1000-10000 nodes): < 2s layout time with optimization
- XLarge graphs (10000+ nodes): Requires virtualization

## ♿ Accessibility

All tools follow WCAG 2.1 AA guidelines:

- **Keyboard Navigation** - Full keyboard support
- **Screen Reader Support** - Proper ARIA labels
- **High Contrast** - Works in high contrast mode
- **Motion** - Respects prefers-reduced-motion
- **Focus Management** - Clear focus indicators

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone repository
git clone https://github.com/Vintaragroup/PL-MCP.git
cd PL-MCP

# Set up development environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Make your changes
# Test thoroughly
# Submit PR
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [React Flow Documentation](https://reactflow.dev)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Tailwind CSS Documentation](https://tailwindcss.com)
- [TypeScript Documentation](https://www.typescriptlang.org)

## 👥 Support

For issues, questions, or suggestions:

1. **GitHub Issues** - [Report a bug](https://github.com/Vintaragroup/PL-MCP/issues)
2. **Discussions** - [Join the community](https://github.com/Vintaragroup/PL-MCP/discussions)
3. **Documentation** - Check the [docs](./docs/) folder

## 🎉 Acknowledgments

- React Flow team for the excellent diagram library
- Model Context Protocol for the integration framework
- GitHub Copilot for AI-powered development insights
- Community contributors and users

---

**Last Updated:** November 2025  
**Version:** 1.0.0  
**Status:** Active Development

For the latest updates, visit [github.com/Vintaragroup/PL-MCP](https://github.com/Vintaragroup/PL-MCP)