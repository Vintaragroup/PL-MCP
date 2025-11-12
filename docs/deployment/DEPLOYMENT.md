# Frontend MCP Server Deployment Scripts

## Build and Run with Docker

### Development
```bash
# Build the image
docker build -t frontend-mcp-server .

# Run the container
docker run -it --rm frontend-mcp-server
```

### Production with Docker Compose
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f frontend-mcp-server

# Stop services
docker-compose down
```

## Kubernetes Deployment

### Prerequisites
- Kubernetes cluster
- kubectl configured
- Docker image pushed to registry

### Deploy to Kubernetes
```bash
# Apply deployment
kubectl apply -f k8s/

# Check status
kubectl get pods -l app=frontend-mcp-server

# View logs
kubectl logs -l app=frontend-mcp-server
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_SERVER_NAME` | Server name identifier | `frontend-mcp-server` |
| `MCP_SERVER_VERSION` | Server version | `1.0.0` |
| `PYTHONPATH` | Python path | `/app/src` |
| `LOG_LEVEL` | Logging level | `INFO` |

## Monitoring and Health Checks

The server includes health check endpoints and proper logging:

- Health check: Built-in Python import check
- Logs: JSON structured logging
- Metrics: Basic performance metrics

## Scaling

### Horizontal Scaling
```bash
# Scale with Docker Compose
docker-compose up --scale frontend-mcp-server=3

# Scale with Kubernetes
kubectl scale deployment frontend-mcp-server --replicas=3
```

### Resource Limits
Configured in docker-compose.yml:
- Memory: 512MB limit, 256MB reservation
- CPU: 0.5 cores limit, 0.25 cores reservation