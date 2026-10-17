<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 7. Proxy

## Intent
Provide a surrogate or placeholder for another object to control access to it.

## Structure

```
┌──────────────────┐
│    Subject        │◀──────────────────────┐
│    (interface)    │                       │
├──────────────────┤                       │
│ + request()       │                       │ delegates to
└──────┬───────────┘                       │
       │ implements                         │
       ├──────────────────┐                │
       ▼                  ▼                │
┌────────────────┐ ┌─────────────────┐     │
│ RealSubject     │ │     Proxy        │────┘
├────────────────┤ ├─────────────────┤
│ + request()     │ │ - realSubject    │
└────────────────┘ │ + request()      │
                    └─────────────────┘
```

## Participants
- **Subject** — defines the common interface for RealSubject and Proxy
- **RealSubject** — defines the real object that the proxy represents
- **Proxy** — maintains a reference to the RealSubject; controls access to it

## Proxy Variants
| Variant | Purpose |
|---------|---------|
| **Virtual Proxy** | Lazy-loads expensive objects on first access |
| **Protection Proxy** | Controls access based on permissions |
| **Caching Proxy** | Caches results of expensive operations |
| **Logging Proxy** | Logs all operations for debugging/auditing |
| **Remote Proxy** | Represents an object in a different address space |

## When to Use
- You need lazy initialization (virtual proxy)
- You need access control (protection proxy)
- You need caching of expensive operations (caching proxy)
- You want to log or audit access to an object (logging proxy)

## TypeScript Example

```typescript
// Subject interface
interface WeatherService {
  getForecast(city: string): string;
}

// Real subject — expensive operation
class RealWeatherService implements WeatherService {
  getForecast(city: string): string {
    // Simulates an expensive API call
    console.log(`  [API] Fetching weather for ${city}...`);
    return `${city}: 72F, Sunny`;
  }
}

// Caching + Logging Proxy
class WeatherServiceProxy implements WeatherService {
  private cache = new Map<string, { data: string; expiry: number }>();
  private readonly TTL = 60_000; // 1 minute

  constructor(private service: RealWeatherService) {}

  getForecast(city: string): string {
    const cached = this.cache.get(city);
    if (cached && cached.expiry > Date.now()) {
      console.log(`  [Cache HIT] ${city}`);
      return cached.data;
    }

    console.log(`  [Cache MISS] ${city}`);
    const data = this.service.getForecast(city);
    this.cache.set(city, { data, expiry: Date.now() + this.TTL });
    return data;
  }
}

// Protection Proxy — access control layer
class AuthWeatherServiceProxy implements WeatherService {
  constructor(
    private service: WeatherService,
    private userRole: string
  ) {}

  getForecast(city: string): string {
    if (this.userRole !== "admin" && this.userRole !== "user") {
      throw new Error("Access denied: insufficient permissions");
    }
    return this.service.getForecast(city);
  }
}

// Usage — stack proxies
let service: WeatherService = new RealWeatherService();
service = new WeatherServiceProxy(service as RealWeatherService);
service = new AuthWeatherServiceProxy(service, "user");

console.log(service.getForecast("Seattle")); // Cache MISS -> API call
console.log(service.getForecast("Seattle")); // Cache HIT
```

---
