<!-- Part of the dev-frontend-ssr skill. Loaded on demand from SKILL.md. -->

# Server-Side Rendering (SSR) — details

## Streaming SSR (React 18+)

```typescript
// Next.js App Router — Streaming with Suspense
import { Suspense } from 'react';

export default function ProductPage({ params }: { params: { id: string } }) {
  return (
    <div>
      {/* Streams immediately */}
      <Header />

      {/* Streams when data resolves */}
      <Suspense fallback={<ProductSkeleton />}>
        <ProductDetail id={params.id} />
      </Suspense>

      {/* Streams independently when its data resolves */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <ProductReviews id={params.id} />
      </Suspense>

      {/* Streams immediately */}
      <Footer />
    </div>
  );
}

// Each async component resolves independently
async function ProductDetail({ id }: { id: string }) {
  const product = await db.products.findUnique({ where: { id } }); // 100ms
  return <div>{product.name} — ${product.price}</div>;
}

async function ProductReviews({ id }: { id: string }) {
  const reviews = await db.reviews.findMany({ where: { productId: id } }); // 500ms
  return <ReviewList reviews={reviews} />;
}
```

The browser receives HTML progressively:
1. Header renders immediately
2. ProductSkeleton shows while product data loads
3. ProductDetail streams in when its data resolves (100ms)
4. ReviewsSkeleton shows while reviews load
5. ProductReviews streams in when reviews resolve (500ms)
6. Footer renders immediately
