<!-- Part of the dev-frontend-ssr skill. Loaded on demand from SKILL.md. -->

# Framework Deep Dives

## Next.js (React)

Next.js App Router (v13+) uses React Server Components by default. Every component is a Server Component unless marked with `'use client'`.

```typescript
// app/products/page.tsx — Server Component (default)
// Runs on the server, never ships JS to the client
import { db } from '@/lib/db';

export default async function ProductsPage() {
  const products = await db.products.findMany(); // Direct DB access

  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
      <AddToCartButton /> {/* Client Component */}
    </div>
  );
}

// Revalidation (ISR)
export const revalidate = 60; // revalidate every 60 seconds
```

```typescript
// app/products/[id]/page.tsx — Dynamic route with generateStaticParams (SSG)
export async function generateStaticParams() {
  const products = await db.products.findMany({ select: { id: true } });
  return products.map((p) => ({ id: p.id }));
}

export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await db.products.findUnique({ where: { id: params.id } });
  if (!product) notFound();
  return <ProductDetail product={product} />;
}
```

### Server Actions (Next.js)
```typescript
// app/products/actions.ts
'use server';

import { revalidatePath } from 'next/cache';

export async function addToCart(productId: string) {
  await db.cart.add({ productId, userId: getCurrentUser().id });
  revalidatePath('/cart');
}

// Used in a Client Component
'use client';
import { addToCart } from './actions';

function AddToCartButton({ productId }: { productId: string }) {
  return (
    <form action={addToCart.bind(null, productId)}>
      <button type="submit">Add to Cart</button>
    </form>
  );
}
```

## Nuxt (Vue)

Nuxt 3 uses Nitro (universal server engine) and provides SSR, SSG, ISR, and hybrid rendering out of the box.

```vue
<!-- pages/products/index.vue -->
<script setup lang="ts">
// useFetch runs on server during SSR, deduplicates on client
const { data: products, pending, error } = await useFetch('/api/products', {
  transform: (response) => response.data,
});
</script>

<template>
  <div>
    <h1>Products</h1>
    <div v-if="pending">Loading...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <ProductCard v-for="product in products" :key="product.id" :product="product" />
  </div>
</template>
```

```typescript
// nuxt.config.ts — Hybrid rendering (per-route strategies)
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },                    // SSG at build time
    '/products/**': { swr: 3600 },               // ISR — revalidate hourly
    '/dashboard/**': { ssr: true },              // SSR per request
    '/admin/**': { ssr: false },                 // SPA (client-only)
    '/api/**': { cors: true, cache: { maxAge: 60 } },
  },
});
```

## Remix (React)

Remix embraces web fundamentals: loaders for data, actions for mutations, nested routes, and progressive enhancement. Forms work without JavaScript.

```typescript
// app/routes/products.tsx — Loader (server-side data fetching)
import { json, type LoaderFunctionArgs } from '@remix-run/node';
import { useLoaderData, Link } from '@remix-run/react';

export async function loader({ request }: LoaderFunctionArgs) {
  const url = new URL(request.url);
  const category = url.searchParams.get('category');
  const products = await db.products.findMany({
    where: category ? { category } : undefined,
  });
  return json({ products });
}

export default function Products() {
  const { products } = useLoaderData<typeof loader>();
  return (
    <div>
      {products.map((product) => (
        <Link key={product.id} to={`/products/${product.id}`} prefetch="intent">
          {product.name}
        </Link>
      ))}
    </div>
  );
}
```

```typescript
// app/routes/products.$id.tsx — Action (server-side mutation)
import { type ActionFunctionArgs, redirect } from '@remix-run/node';

export async function action({ request, params }: ActionFunctionArgs) {
  const formData = await request.formData();
  const intent = formData.get('intent');

  if (intent === 'add-to-cart') {
    await db.cart.add({
      productId: params.id!,
      userId: await requireUserId(request),
      quantity: Number(formData.get('quantity')),
    });
    return redirect('/cart');
  }

  throw new Response('Invalid intent', { status: 400 });
}

export default function ProductDetail() {
  const product = useLoaderData<typeof loader>();
  return (
    <Form method="post">
      <input type="hidden" name="intent" value="add-to-cart" />
      <input type="number" name="quantity" defaultValue={1} min={1} />
      <button type="submit">Add to Cart</button>
      {/* Works without JavaScript enabled */}
    </Form>
  );
}
```

## SvelteKit (Svelte)

SvelteKit uses load functions for data fetching and form actions for mutations. It supports SSR, SSG, and SPA modes per route.

```typescript
// src/routes/products/+page.server.ts — Load function (server-only)
import type { PageServerLoad, Actions } from './$types';

export const load: PageServerLoad = async ({ fetch, url }) => {
  const category = url.searchParams.get('category');
  const response = await fetch(`/api/products?category=${category}`);
  const products = await response.json();
  return { products };
};

export const actions: Actions = {
  addToCart: async ({ request, locals }) => {
    const data = await request.formData();
    const productId = data.get('productId');
    await db.cart.add({ productId, userId: locals.user.id });
    return { success: true };
  },
};
```

```svelte
<!-- src/routes/products/+page.svelte -->
<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;
</script>

<h1>Products</h1>
{#each data.products as product}
  <div>
    <h2>{product.name}</h2>
    <form method="POST" action="?/addToCart" use:enhance>
      <input type="hidden" name="productId" value={product.id} />
      <button>Add to Cart</button>
    </form>
  </div>
{/each}
```

```typescript
// Per-route rendering strategy
// src/routes/blog/+page.ts
export const prerender = true;  // SSG — generate at build time

// src/routes/dashboard/+page.ts
export const ssr = false;       // SPA — client-only rendering

// src/routes/products/+page.ts
// Default: SSR per request
```

## Astro (Islands Architecture)

Astro renders pages as static HTML by default and ships **zero JavaScript** unless you explicitly opt in with interactive islands. Components from any framework (React, Vue, Svelte, Solid) can be used as islands.

```astro
---
// src/pages/products.astro — Server-side (runs at build/request time)
import Layout from '../layouts/Layout.astro';
import ProductCard from '../components/ProductCard.astro'; // Static, no JS
import SearchBar from '../components/SearchBar.tsx';       // React island
import CartWidget from '../components/CartWidget.vue';     // Vue island

const products = await fetch('https://api.example.com/products').then(r => r.json());
---

<Layout title="Products">
  <!-- This React component hydrates on the client (interactive island) -->
  <SearchBar client:load />

  <!-- Static HTML, no JavaScript shipped -->
  <div class="product-grid">
    {products.map((product) => (
      <ProductCard product={product} />
    ))}
  </div>

  <!-- Vue component hydrates only when visible in viewport -->
  <CartWidget client:visible />
</Layout>
```

### Astro Client Directives
| Directive | Hydration Strategy |
|-----------|-------------------|
| `client:load` | Hydrate immediately on page load |
| `client:idle` | Hydrate when browser is idle (requestIdleCallback) |
| `client:visible` | Hydrate when component enters viewport (IntersectionObserver) |
| `client:media="(min-width: 768px)"` | Hydrate when media query matches |
| `client:only="react"` | Client-render only, skip SSR entirely |
| *(no directive)* | No hydration — renders as static HTML with zero JS |
