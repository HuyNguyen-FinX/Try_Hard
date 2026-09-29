# Senior Python Interview Preparation

## Target Role

**Senior Software Engineer (Python) — VinSmart Future**

Bộ tài liệu này tối ưu cho cách trả lời Senior: **Definition → Why → How → Trade-off → Production example**. Không học tuyến tính toàn bộ; bắt đầu từ P0, tự trả lời thành tiếng, sau đó drill scenario và System Design.

## Main Skills

Python · FastAPI · PostgreSQL · Redis · Celery · System Design · Distributed Systems · Docker · Kubernetes · AWS · Terraform · AI Integration · Security · Reliability

## Learning Roadmap

### Tier 1 — Must Know

Python internals; GIL/AsyncIO; FastAPI request lifecycle; PostgreSQL index/MVCC/transaction; System Design; idempotency/retry/timeout/outbox; production debugging.

### Tier 2 — Very Important

Redis failure behavior; Celery delivery semantics; API Design; Docker; Kubernetes; architecture trade-off; security và observability.

### Tier 3 — Contextual Advantage

AWS/Terraform/CI/CD; RAG/LLM integration; coding pattern; domain designs cho automotive/manufacturing; behavioral story refinement.

Đi theo [30-day plan](00-interview-roadmap/30-day-plan.md) hoặc [14-day crash plan](00-interview-roadmap/14-day-crash-plan.md). Trước ngày phỏng vấn dùng [Last-day Review](23-cheatsheets/last-day-review.md).

## Module Dashboard

| Module | Nội dung |
|---|---|
| [Roadmap](00-interview-roadmap/README.md) | Kế hoạch 30/14 ngày, checklist và priority |
| [Python Core](01-python-core/README.md) | Memory, object model, typing, generators |
| [Python Concurrency](02-python-concurrency/README.md) | GIL, thread, process, AsyncIO |
| [FastAPI](03-fastapi/README.md) | Lifecycle, DI, auth, WebSocket, performance |
| [PostgreSQL](04-database-postgresql/README.md) | Index, planner, MVCC, transaction, scale |
| [SQLAlchemy](05-sqlalchemy/README.md) | Session, loading, transaction và performance |
| [Redis](06-redis/README.md) | Cache, lock, rate limit, persistence, failure |
| [Celery](07-celery/README.md) | Delivery, retry, idempotency, operations |
| [API Design](08-api-design/README.md) | REST, pagination, retry, security |
| [Software Architecture](09-software-architecture/README.md) | DDD, modular monolith, microservices |
| [Distributed Systems](10-distributed-systems/README.md) | Consistency, failure, saga, outbox |
| [System Design](11-system-design/README.md) | Framework và 11 bài thiết kế production |
| [Docker](12-docker/README.md) | Image, network, build và hardening |
| [Kubernetes](13-kubernetes/README.md) | Workload, autoscale, rollout, troubleshoot |
| [Cloud](14-cloud/README.md) | AWS compute, storage, network, architecture |
| [Terraform & CI/CD](15-terraform-cicd/README.md) | IaC, state, deployment, rollback |
| [Security](16-security/README.md) | OWASP, identity, secret, API protection |
| [Performance & Reliability](17-performance-reliability/README.md) | Profiling, SLO, observability, incident |
| [AI Integration](18-ai-integration/README.md) | LLM, RAG, vector DB, scale và quality |
| [Coding Interview](19-coding-interview/README.md) | Pattern, structure và Python problems |
| [Senior Scenarios](20-senior-scenarios/README.md) | 11 sự cố production có framework |
| [Behavioral](21-behavioral/README.md) | Leadership, conflict, incident và STAR |
| [Mock Interview](22-mock-interview/README.md) | Question bank và full 110-minute mock |
| [Cheatsheets](23-cheatsheets/README.md) | Review nhanh 1–2 giờ trước phỏng vấn |
| [Technical References](24-references/README.md) | Nguồn chính thức để kiểm tra chi tiết thay đổi theo version |

## Architecture Diagrams

Các P0/P1 topic có concept/request/data/failure diagram phù hợp; 11 System Design Lab có ít nhất 6 diagram/bài: high-level, sequence, source-of-truth data flow, scaling, failure/recovery và observability trace. Bắt đầu từ [System Design Dashboard](11-system-design/README.md).

## Deep Dive Topics

- [Python memory model](01-python-core/python-memory-model.md), [GIL](02-python-concurrency/gil.md), [AsyncIO](02-python-concurrency/asyncio.md), [Event Loop](02-python-concurrency/event-loop.md).
- [FastAPI request lifecycle](03-fastapi/request-lifecycle.md) và [sync vs async endpoint](03-fastapi/sync-vs-async-endpoint.md).
- [PostgreSQL Index](04-database-postgresql/index.md), [EXPLAIN ANALYZE](04-database-postgresql/explain-analyze.md), [MVCC](04-database-postgresql/mvcc.md) và [Transactions](04-database-postgresql/transaction.md).
- [Redis Internals](06-redis/redis-internals.md), [Celery Task Lifecycle](07-celery/task-lifecycle.md), [Outbox Pattern](10-distributed-systems/outbox-pattern.md).
- [RAG](18-ai-integration/rag.md) và [Production AI System](18-ai-integration/production-ai-system.md).

## System Design Labs

Các lab dạy cách nói trong interview theo flow **clarify → estimate → V1 → bottleneck → evolution → failure → security/observability → trade-off**. Ưu tiên: [AI Chatbot](11-system-design/design-ai-chatbot.md), [Vehicle Warranty](11-system-design/design-vehicle-warranty.md), [Document Processing](11-system-design/design-document-processing.md), [Video Analytics](11-system-design/design-video-processing.md) và [Production Planning](11-system-design/design-production-planning.md).

## Production Failure Scenarios

Drill [API latency regression](20-senior-scenarios/api-slow.md), [PostgreSQL high CPU](20-senior-scenarios/database-high-cpu.md), [Redis outage](20-senior-scenarios/redis-down.md), [duplicate Celery task](20-senior-scenarios/celery-task-duplicate.md), [memory leak](20-senior-scenarios/memory-leak.md) và [scale 1k→20k RPS](20-senior-scenarios/high-traffic.md).

## Interview Question Bank

- [Top 50 Senior Backend Questions](22-mock-interview/top-50-senior-backend-questions.md)
- [Top 30 System Design Questions](22-mock-interview/top-30-system-design-questions.md)
- [Full Mock Interview — 110 minutes](22-mock-interview/full-mock-interview.md)

## Progress Tracker

- [ ] Python Core
- [ ] Python AsyncIO / GIL / concurrency
- [ ] FastAPI
- [ ] PostgreSQL + SQLAlchemy
- [ ] Redis
- [ ] Celery
- [ ] API Design
- [ ] Software Architecture
- [ ] Distributed Systems
- [ ] System Design (ít nhất 5 bài nói thành tiếng)
- [ ] Docker / Kubernetes
- [ ] Cloud / Terraform / CI/CD
- [ ] Security
- [ ] Performance / Reliability
- [ ] AI Integration
- [ ] Coding Interview
- [ ] Production Scenarios
- [ ] Behavioral stories
- [ ] Full Mock Interview

## Cách dùng mỗi topic

1. Đọc **What/Why/How**, tự vẽ lifecycle và failure path.
2. Chạy/biến đổi example; nêu assumption và invariant.
3. Trả lời 10 Basic + 10 Senior mà không nhìn notes.
4. Với 5 scenario, dùng: **stabilize → observe → hypothesize → verify → mitigate → prevent**.
5. So sánh với Short Answers; bổ sung ví dụ thật từ kinh nghiệm của bạn.

## Interview North Star

- Correctness trước optimization; số liệu trước opinion.
- Phân biệt concurrency với parallelism, availability với correctness, delivery với effect.
- Mọi dependency đều có timeout; mọi retry có budget/jitter; mọi queue có bound/DLQ/owner.
- Scale API phải đi kèm database connection budget, backpressure và degraded mode.
- “Production-ready” gồm observability, security, canary, rollback, runbook và reconciliation.
