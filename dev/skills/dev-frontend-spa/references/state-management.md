<!-- Part of the dev-frontend-spa skill. Loaded on demand from SKILL.md. -->

# State Management

## State Management Landscape

| Library | Ecosystem | Philosophy |
|---------|-----------|-----------|
| **Redux Toolkit** | React | Single store, immutable, actions + reducers |
| **Zustand** | React | Minimal, hook-based, no boilerplate |
| **Jotai** | React | Atomic state, bottom-up, derived atoms |
| **Valtio** | React | Proxy-based, mutable API, reactive |
| **Pinia** | Vue | Composition API-friendly, modular stores |
| **NgRx** | Angular | RxJS-based Redux for Angular, effects |
| **Angular Signals** | Angular | Fine-grained reactivity, no RxJS needed |
| **Svelte Stores** | Svelte | Built-in writable/readable/derived stores |

## Zustand (Modern React State)
```typescript
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

interface AuthStore {
  user: User | null;
  token: string | null;
  login: (credentials: Credentials) => Promise<void>;
  logout: () => void;
}

const useAuthStore = create<AuthStore>()(
  devtools(
    persist(
      (set) => ({
        user: null,
        token: null,
        login: async (credentials) => {
          const { user, token } = await api.login(credentials);
          set({ user, token });
        },
        logout: () => set({ user: null, token: null }),
      }),
      { name: 'auth-storage' }
    )
  )
);

// Usage in component
function Profile() {
  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);
  // ...
}
```

## Pinia (Vue State)
```typescript
import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', () => {
  const items = ref<CartItem[]>([]);

  const total = computed(() =>
    items.value.reduce((sum, item) => sum + item.price * item.qty, 0)
  );

  function addItem(product: Product) {
    const existing = items.value.find((i) => i.id === product.id);
    if (existing) existing.qty++;
    else items.value.push({ ...product, qty: 1 });
  }

  function removeItem(id: string) {
    items.value = items.value.filter((i) => i.id !== id);
  }

  return { items, total, addItem, removeItem };
});
```
