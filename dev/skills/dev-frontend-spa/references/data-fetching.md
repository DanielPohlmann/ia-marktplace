<!-- Part of the dev-frontend-spa skill. Loaded on demand from SKILL.md. -->

# Data Fetching

## The Server State Problem
Server data is not the same as client state. Server data is:
- **Asynchronous** — fetched over the network
- **Shared** — multiple components may need the same data
- **Stale** — can be outdated the moment it arrives
- **Cacheable** — often the same data is requested repeatedly

Libraries like TanStack Query and SWR solve these problems with caching, deduplication, background refetching, and optimistic updates.

## TanStack Query (React Query)
```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function TodoList() {
  const queryClient = useQueryClient();

  const { data: todos, isLoading, error } = useQuery({
    queryKey: ['todos'],
    queryFn: () => api.getTodos(),
    staleTime: 5 * 60 * 1000,     // consider fresh for 5 min
    gcTime: 30 * 60 * 1000,       // garbage collect after 30 min
  });

  const addTodo = useMutation({
    mutationFn: (newTodo: NewTodo) => api.createTodo(newTodo),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] });
    },
    // Optimistic update
    onMutate: async (newTodo) => {
      await queryClient.cancelQueries({ queryKey: ['todos'] });
      const previous = queryClient.getQueryData(['todos']);
      queryClient.setQueryData(['todos'], (old: Todo[]) => [
        ...old,
        { ...newTodo, id: 'temp' },
      ]);
      return { previous };
    },
    onError: (_err, _newTodo, context) => {
      queryClient.setQueryData(['todos'], context?.previous);
    },
  });

  if (isLoading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  // render todos...
}
```

## SWR (Vercel)
```typescript
import useSWR from 'swr';

const fetcher = (url: string) => fetch(url).then((r) => r.json());

function Profile() {
  const { data, error, isLoading, mutate } = useSWR('/api/user', fetcher, {
    revalidateOnFocus: true,
    revalidateOnReconnect: true,
    dedupingInterval: 2000,
  });

  // mutate() to trigger revalidation
  // mutate(newData, false) for optimistic update
}
```

## Apollo Client (GraphQL)
```typescript
import { useQuery, gql } from '@apollo/client';

const GET_TODOS = gql`
  query GetTodos($status: Status) {
    todos(status: $status) {
      id
      title
      completed
    }
  }
`;

function TodoList({ status }: { status: Status }) {
  const { loading, error, data } = useQuery(GET_TODOS, {
    variables: { status },
    pollInterval: 30000, // refetch every 30s
  });
  // ...
}
```
