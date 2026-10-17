<!-- Part of the specs-documentation-trd skill. Loaded on demand from SKILL.md. -->

# Technical Requirements Document (TRD) — details

## Standard TRD Structure

### 1. Title and Metadata
Document identification, ownership, and status tracking.

### 2. System Overview
High-level description of the system, its purpose, and how it fits into the broader architecture.

### 3. Architecture
System architecture including components, interactions, technology stack, and diagrams.

### 4. API Specifications
Endpoints, request/response schemas, authentication, error handling, and versioning.

### 5. Data Models
Database schema, entity relationships, data types, constraints, and migration strategy.

### 6. Security Requirements
Authentication, authorization, encryption, compliance, and threat model.

### 7. Performance Requirements
Latency, throughput, availability, and scalability targets.

### 8. Dependencies
External services, libraries, infrastructure, and team dependencies.

### 9. Technical Constraints
Technology mandates, backward compatibility, regulatory, and organizational constraints.

### 10. Deployment Plan
Environments, CI/CD pipeline, rollout strategy, and rollback procedures.

## TRD Example: Order Service

```markdown
# TRD: Order Service

| Field            | Value                     |
|------------------|---------------------------|
| Author           | Jane Engineer             |
| Status           | In Review                 |
| Created          | 2025-01-15                |
| PRD Reference    | PRD-042: Checkout Redesign|

## 1. System Overview

The Order Service manages the complete order lifecycle from creation
through fulfillment. It replaces the order module in the monolith
as part of the microservices migration (see ADR-007).

## 2. Architecture

Architecture style: Event-driven microservice (see ADR-012).

The service exposes a REST API for synchronous order operations
and publishes domain events to RabbitMQ for downstream consumers
(notification, analytics, fulfillment).

## 3. Key API Endpoints

- POST /api/v1/orders -- Create order
- GET /api/v1/orders/{id} -- Get order by ID
- GET /api/v1/orders?userId={id} -- List user orders
- PATCH /api/v1/orders/{id}/cancel -- Cancel order
- POST /api/v1/orders/{id}/refund -- Initiate refund

## 4. Data Model

Orders table with OrderItems join table. Uses PostgreSQL with
EF Core migrations. See schema definitions in Section 4.2 above.

## 5. Events Published

| Event              | Trigger               | Consumers                  |
|--------------------|-----------------------|----------------------------|
| OrderCreated       | New order placed      | Notification, Analytics    |
| OrderCancelled     | Order cancelled       | Notification, Fulfillment  |
| OrderFulfilled     | Order shipped         | Notification, Analytics    |
| PaymentProcessed   | Payment confirmed     | Order (self), Analytics    |
```
