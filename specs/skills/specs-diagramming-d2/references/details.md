<!-- Part of the specs-diagramming-d2 skill. Loaded on demand from SKILL.md. -->

# D2 — Declarative Diagramming — details

## Basic Syntax

### Shapes

Shapes are declared simply by naming them. D2 auto-creates shapes on first reference.

```d2
# Simple shapes
server
database
client

# Shape with label
server: Application Server

# Shape with explicit type
db: PostgreSQL {
  shape: cylinder
}

# Multiple shapes on one line are not supported; declare each separately
```

### Connections

Connections link shapes with arrows and optional labels.

```d2
client -> server: HTTP Request
server -> db: SQL Query
server -> client: HTTP Response

# Connection styles
a -> b: solid arrow
a -- b: line (no arrow)
a <-> b: bidirectional
a <- b: reverse arrow
```

### Labels and Tooltips

```d2
server: Application Server {
  tooltip: "Runs on port 8080"
}

server -> db: Reads data {
  style.stroke: green
}
```

## Shape Types

D2 supports a variety of built-in shapes.

| Shape | Keyword | Description |
|-------|---------|-------------|
| Rectangle | `shape: rectangle` | Default shape |
| Square | `shape: square` | Equal-sided rectangle |
| Circle | `shape: circle` | Round shape |
| Oval | `shape: oval` | Ellipse |
| Diamond | `shape: diamond` | Decision / condition |
| Cylinder | `shape: cylinder` | Database |
| Queue | `shape: queue` | Message queue |
| Package | `shape: package` | Namespace / module |
| Page | `shape: page` | Document |
| Parallelogram | `shape: parallelogram` | Input/output |
| Hexagon | `shape: hexagon` | Prepare / process |
| Cloud | `shape: cloud` | Cloud / external service |
| Person | `shape: person` | Human actor |
| Class | `shape: class` | UML class box |
| SQL Table | `shape: sql_table` | Database table |
| Image | `shape: image` | Raster or SVG image |
| Text | `shape: text` | Plain text label |
| Code | `shape: code` | Code block |

## Styles

### Shape Styles

```d2
server: Application Server {
  style: {
    fill: "#4C566A"
    stroke: "#D8DEE9"
    font-color: "#ECEFF4"
    border-radius: 8
    shadow: true
    opacity: 1.0
    stroke-width: 2
    stroke-dash: 0
  }
}
```

### Connection Styles

```d2
a -> b: Request {
  style: {
    stroke: "#88C0D0"
    stroke-width: 2
    stroke-dash: 5
    font-color: "#88C0D0"
    animated: true
  }
}
```

### Available Style Properties

| Property | Applies To | Description |
|----------|-----------|-------------|
| `fill` | Shapes | Background color |
| `stroke` | Shapes, connections | Border / line color |
| `stroke-width` | Shapes, connections | Border / line thickness |
| `stroke-dash` | Shapes, connections | Dash pattern (0 = solid) |
| `font-color` | Shapes, connections | Text color |
| `font-size` | Shapes, connections | Text size |
| `border-radius` | Shapes | Corner rounding |
| `shadow` | Shapes | Drop shadow |
| `opacity` | Shapes | Transparency (0.0 - 1.0) |
| `bold` | Shapes, connections | Bold text |
| `italic` | Shapes, connections | Italic text |
| `underline` | Shapes, connections | Underlined text |
| `animated` | Connections | Animated dashes |

## Layout Engines

D2 supports multiple layout engines, each with different strengths.

| Engine | Description | Best For |
|--------|-------------|----------|
| `dagre` | Default. Fast, hierarchical layout. | Most diagrams. Free and open source. |
| `ELK` | Eclipse Layout Kernel. More advanced algorithms. | Complex diagrams with many connections. Free and open source. |
| `TALA` | Terrastruct's proprietary engine. Best quality. | Presentation-quality diagrams. Requires license. |

### Specifying Layout Engine

```bash
# Via CLI flag
d2 --layout dagre input.d2 output.svg
d2 --layout elk input.d2 output.svg
d2 --layout tala input.d2 output.svg
```

Or in the D2 file:

```d2
direction: right
```

### Direction

```d2
direction: right  # left-to-right (default: down/top-to-bottom)
```

Available directions: `up`, `down`, `left`, `right`

## CLI Commands

```bash
# Install D2
curl -fsSL https://d2lang.com/install.sh | sh

# Or via Homebrew
brew install d2

# Compile D2 to SVG (default)
d2 input.d2 output.svg

# Compile to PNG
d2 --format png input.d2 output.png

# Compile to PDF
d2 --format pdf input.d2 output.pdf

# Watch mode (auto-recompile on changes)
d2 --watch input.d2 output.svg

# Specify layout engine
d2 --layout elk input.d2 output.svg

# Specify theme
d2 --theme 200 input.d2 output.svg

# Dark theme
d2 --dark-theme 200 input.d2 output.svg

# List available themes
d2 --help  # themes are numbered; see docs for full list

# Render a specific layer or scenario
d2 --target "layers.detailed" input.d2 output.svg

# Sketch mode (hand-drawn look)
d2 --sketch input.d2 output.svg

# Pad output
d2 --pad 50 input.d2 output.svg
```

## Complete Example

```d2
direction: right

title: E-Commerce Architecture {
  near: top-center
  shape: text
  style.font-size: 24
  style.bold: true
}

classes: {
  service: {
    style: {
      fill: "#5E81AC"
      font-color: "#ECEFF4"
      border-radius: 8
    }
  }
  datastore: {
    shape: cylinder
    style: {
      fill: "#A3BE8C"
      font-color: "#2E3440"
    }
  }
  external: {
    style: {
      fill: "#BF616A"
      font-color: "#ECEFF4"
      stroke-dash: 5
    }
  }
  client: {
    style: {
      fill: "#88C0D0"
      font-color: "#2E3440"
      border-radius: 12
    }
  }
}

customer: Customer {
  shape: person
}

frontend: Frontend {
  class: client
  web: Web App (Next.js)
  mobile: Mobile App (React Native)
}

backend: Backend Services {
  api: API Gateway {
    class: service
  }
  catalog: Catalog Service {
    class: service
  }
  orders: Order Service {
    class: service
  }
  auth: Auth Service {
    class: service
  }
}

data: Data Layer {
  catalog_db: Catalog DB {
    class: datastore
  }
  order_db: Order DB {
    class: datastore
  }
  cache: Redis Cache {
    class: datastore
  }
  queue: Message Queue {
    shape: queue
    style.fill: "#D08770"
  }
}

external: External Services {
  stripe: Stripe {
    class: external
  }
  sendgrid: SendGrid {
    class: external
  }
}

customer -> frontend.web: HTTPS
customer -> frontend.mobile: HTTPS

frontend.web -> backend.api: REST/GraphQL
frontend.mobile -> backend.api: REST/GraphQL

backend.api -> backend.auth: Verify token
backend.api -> backend.catalog: Product queries
backend.api -> backend.orders: Order management

backend.catalog -> data.catalog_db
backend.catalog -> data.cache
backend.orders -> data.order_db
backend.orders -> data.queue: Publish events

data.queue -> external.sendgrid: Order confirmation emails
backend.orders -> external.stripe: Process payment
```
