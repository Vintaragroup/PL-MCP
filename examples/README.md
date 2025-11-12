# Frontend MCP Server Examples

This directory contains practical examples of using the Frontend MCP Server tools.

## React Component Examples

### Example 1: Analyzing a React Component

```typescript
// sample-component.tsx
import React, { useEffect, useState } from 'react';

interface UserCardProps {
  userId: number;
  showDetails?: boolean;
}

const UserCard: React.FC<UserCardProps> = ({ userId, showDetails = false }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser(userId);
  }, []); // Missing userId dependency

  const fetchUser = async (id: number) => {
    try {
      const response = await fetch(`/api/users/${id}`);
      const userData = await response.json();
      setUser(userData);
      setLoading(false);
    } catch (error) {
      console.error('Failed to fetch user:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="p-4 border rounded" onClick={() => console.log('Card clicked')}>
      <h3>{user?.name}</h3>
      {showDetails && (
        <div>
          <p>{user?.email}</p>
          <p>{user?.phone}</p>
        </div>
      )}
    </div>
  );
};

export default UserCard;
```

**Using react_component_analysis:**
- Missing dependency in useEffect
- Inline arrow function causing re-renders
- Console.log in production code
- Missing error state handling

### Example 2: Generated Optimized Component

```typescript
// optimized-user-card.tsx
import React, { useEffect, useState, useCallback } from 'react';

interface UserCardProps {
  userId: number;
  showDetails?: boolean;
  onCardClick?: (userId: number) => void;
}

interface User {
  id: number;
  name: string;
  email: string;
  phone: string;
}

interface UserState {
  user: User | null;
  loading: boolean;
  error: string | null;
}

const UserCard: React.FC<UserCardProps> = ({ 
  userId, 
  showDetails = false, 
  onCardClick 
}) => {
  const [state, setState] = useState<UserState>({
    user: null,
    loading: true,
    error: null
  });

  const fetchUser = useCallback(async (id: number) => {
    setState(prev => ({ ...prev, loading: true, error: null }));
    
    try {
      const response = await fetch(`/api/users/${id}`);
      
      if (!response.ok) {
        throw new Error(`Failed to fetch user: ${response.status}`);
      }
      
      const userData = await response.json();
      setState({ user: userData, loading: false, error: null });
    } catch (error) {
      setState({ 
        user: null, 
        loading: false, 
        error: error instanceof Error ? error.message : 'Unknown error'
      });
    }
  }, []);

  useEffect(() => {
    fetchUser(userId);
  }, [userId, fetchUser]);

  const handleCardClick = useCallback(() => {
    onCardClick?.(userId);
  }, [onCardClick, userId]);

  if (state.loading) {
    return (
      <div className="p-4 border rounded animate-pulse" aria-label="Loading user data">
        <div className="h-4 bg-gray-200 rounded mb-2"></div>
        <div className="h-3 bg-gray-200 rounded w-3/4"></div>
      </div>
    );
  }

  if (state.error) {
    return (
      <div className="p-4 border border-red-200 rounded bg-red-50" role="alert">
        <p className="text-red-600">Error: {state.error}</p>
        <button 
          onClick={() => fetchUser(userId)}
          className="mt-2 px-3 py-1 bg-red-600 text-white rounded text-sm hover:bg-red-700"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div 
      className="p-4 border rounded cursor-pointer hover:shadow-md transition-shadow"
      onClick={handleCardClick}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          handleCardClick();
        }
      }}
      aria-label={`User card for ${state.user?.name}`}
    >
      <h3 className="text-lg font-semibold text-gray-900">
        {state.user?.name}
      </h3>
      {showDetails && state.user && (
        <div className="mt-2 space-y-1">
          <p className="text-sm text-gray-600">{state.user.email}</p>
          <p className="text-sm text-gray-600">{state.user.phone}</p>
        </div>
      )}
    </div>
  );
};

export default UserCard;
```

## Tailwind CSS Examples

### Example 1: Component Builder Usage

```typescript
// Using tailwind_component_builder
// Input: component_type: "button", style_variant: "primary", size: "md", color_scheme: "blue"

// Generated result:
<button 
  type="button" 
  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
>
  Button Text
</button>
```

### Example 2: Responsive Grid Layout

```typescript
// Using tailwind_responsive_generator
// Input: layout_type: "grid", breakpoints: ["sm", "md", "lg"], mobile_first: true

// Generated classes:
"grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"

// Complete example:
<div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
  <div className="bg-white p-4 rounded-lg shadow">Item 1</div>
  <div className="bg-white p-4 rounded-lg shadow">Item 2</div>
  <div className="bg-white p-4 rounded-lg shadow">Item 3</div>
  <div className="bg-white p-4 rounded-lg shadow">Item 4</div>
</div>
```

## React Hook Examples

### Example 1: Custom API Hook

```typescript
// Generated using react_hook_generator
// Input: hook_name: "useApiData", functionality: "Fetch and manage API data with caching"

import { useState, useEffect, useCallback } from 'react';

interface UseApiDataState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

export const useApiData = <T = any>(url: string, dependencies: any[] = []) => {
  const [state, setState] = useState<UseApiDataState<T>>({
    data: null,
    loading: false,
    error: null
  });

  const fetchData = useCallback(async () => {
    if (!url) return;

    setState(prev => ({ ...prev, loading: true, error: null }));

    try {
      const response = await fetch(url);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      setState({ data, loading: false, error: null });
    } catch (error) {
      setState({ 
        data: null, 
        loading: false, 
        error: error instanceof Error ? error.message : 'Unknown error'
      });
    }
  }, [url]);

  useEffect(() => {
    fetchData();
  }, [fetchData, ...dependencies]);

  const refetch = useCallback(() => {
    fetchData();
  }, [fetchData]);

  return {
    ...state,
    refetch
  };
};

// Usage example:
const UserProfile = ({ userId }: { userId: number }) => {
  const { data: user, loading, error, refetch } = useApiData(`/api/users/${userId}`, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>No user found</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <button onClick={refetch}>Refresh</button>
    </div>
  );
};
```

## React Native Examples

### Example 1: Platform-Specific Component

```typescript
// Generated using react_native_component_generator
// Input: component_name: "PlatformButton", platform: "both"

import React from 'react';
import { 
  View, 
  Text, 
  TouchableOpacity, 
  StyleSheet, 
  Platform 
} from 'react-native';

interface PlatformButtonProps {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export const PlatformButton: React.FC<PlatformButtonProps> = ({
  title,
  onPress,
  variant = 'primary',
  disabled = false
}) => {
  const buttonStyle = [
    styles.button,
    styles[variant],
    disabled && styles.disabled,
    Platform.OS === 'ios' ? styles.ios : styles.android
  ];

  return (
    <TouchableOpacity
      style={buttonStyle}
      onPress={onPress}
      disabled={disabled}
      activeOpacity={0.7}
    >
      <Text style={[styles.text, styles[`${variant}Text`]]}>
        {title}
      </Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: 48,
  },
  primary: {
    backgroundColor: '#007AFF',
  },
  secondary: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: '#007AFF',
  },
  disabled: {
    opacity: 0.5,
  },
  ios: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  android: {
    elevation: 2,
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
  primaryText: {
    color: '#FFFFFF',
  },
  secondaryText: {
    color: '#007AFF',
  },
});

export default PlatformButton;
```

## React Flow Examples

### Example 1: Interactive Flowchart

```typescript
// Generated using react_flow_diagram_generator
// Input: diagram_type: "workflow", nodes_count: 5

import React, { useCallback } from 'react';
import ReactFlow, {
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  ConnectionMode,
} from 'reactflow';
import 'reactflow/dist/style.css';

const initialNodes: Node[] = [
  {
    id: '1',
    type: 'input',
    data: { label: 'Start Process' },
    position: { x: 250, y: 0 },
    style: { backgroundColor: '#f0f9ff', border: '2px solid #0ea5e9' }
  },
  {
    id: '2',
    data: { label: 'Validate Input' },
    position: { x: 250, y: 100 },
    style: { backgroundColor: '#fef3c7', border: '2px solid #f59e0b' }
  },
  {
    id: '3',
    data: { label: 'Process Data' },
    position: { x: 250, y: 200 },
    style: { backgroundColor: '#f0fdf4', border: '2px solid #10b981' }
  },
  {
    id: '4',
    data: { label: 'Generate Output' },
    position: { x: 250, y: 300 },
    style: { backgroundColor: '#faf5ff', border: '2px solid #8b5cf6' }
  },
  {
    id: '5',
    type: 'output',
    data: { label: 'Complete' },
    position: { x: 250, y: 400 },
    style: { backgroundColor: '#fef2f2', border: '2px solid #ef4444' }
  },
];

const initialEdges: Edge[] = [
  { id: 'e1-2', source: '1', target: '2', animated: true },
  { id: 'e2-3', source: '2', target: '3', animated: true },
  { id: 'e3-4', source: '3', target: '4', animated: true },
  { id: 'e4-5', source: '4', target: '5', animated: true },
];

export const WorkflowFlow: React.FC = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <div style={{ width: '100%', height: '600px' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        connectionMode={ConnectionMode.Loose}
        fitView
        attributionPosition="bottom-left"
      >
        <Controls />
        <Background color="#f1f5f9" gap={16} />
      </ReactFlow>
    </div>
  );
};

export default WorkflowFlow;
```

## Package Management Examples

### Example 1: Package Analysis Results

```json
// Input package.json
{
  "name": "my-react-app",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0",
    "tailwindcss": "^3.2.0",
    "axios": "^1.3.0"
  },
  "devDependencies": {
    "typescript": "^4.9.0",
    "@types/react": "^18.0.0",
    "vite": "^4.1.0"
  }
}

// Analysis results using package_analyzer:
// - Runtime dependencies: 5
// - Development dependencies: 3
// - Frontend-specific packages detected:
//   - react (^18.2.0): React framework
//   - react-dom (^18.2.0): React DOM renderer
//   - tailwindcss (^3.2.0): Tailwind CSS framework
//   - axios (^1.3.0): HTTP client
//   - typescript (^4.9.0): TypeScript compiler
```

## Testing Examples

### Example 1: Generated Component Tests

```typescript
// Generated using react_testing_generator for UserCard component

import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { jest } from '@jest/globals';
import UserCard from './UserCard';

// Mock fetch globally
global.fetch = jest.fn();

describe('UserCard', () => {
  beforeEach(() => {
    (fetch as jest.Mock).mockClear();
  });

  test('renders loading state initially', () => {
    render(<UserCard userId={1} />);
    expect(screen.getByLabelText(/loading user data/i)).toBeInTheDocument();
  });

  test('renders user data after successful fetch', async () => {
    const mockUser = {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com',
      phone: '123-456-7890'
    };

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    });

    render(<UserCard userId={1} showDetails />);

    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });

    expect(screen.getByText('john@example.com')).toBeInTheDocument();
    expect(screen.getByText('123-456-7890')).toBeInTheDocument();
  });

  test('handles fetch error gracefully', async () => {
    (fetch as jest.Mock).mockRejectedValueOnce(new Error('Network error'));

    render(<UserCard userId={1} />);

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeInTheDocument();
    });

    expect(screen.getByText(/error: network error/i)).toBeInTheDocument();
    expect(screen.getByText('Retry')).toBeInTheDocument();
  });

  test('calls onCardClick when card is clicked', async () => {
    const mockOnCardClick = jest.fn();
    const mockUser = { id: 1, name: 'John Doe' };

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    });

    render(<UserCard userId={1} onCardClick={mockOnCardClick} />);

    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });

    fireEvent.click(screen.getByRole('button'));
    expect(mockOnCardClick).toHaveBeenCalledWith(1);
  });

  test('supports keyboard navigation', async () => {
    const mockOnCardClick = jest.fn();
    const mockUser = { id: 1, name: 'John Doe' };

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    });

    render(<UserCard userId={1} onCardClick={mockOnCardClick} />);

    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });

    const card = screen.getByRole('button');
    card.focus();
    fireEvent.keyDown(card, { key: 'Enter' });
    
    expect(mockOnCardClick).toHaveBeenCalledWith(1);
  });
});
```

These examples demonstrate the comprehensive capabilities of the Frontend MCP Server across different frontend technologies and use cases.