from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).parent / "vinsmart-future-senior-python-interview"


STRUCTURE: dict[str, list[str]] = {
    "01-python-core": [
        "README.md", "python-memory-model.md", "gc-reference-counting.md",
        "mutable-immutable.md", "shallow-vs-deep-copy.md", "decorators.md",
        "generators-iterators.md", "context-manager.md", "dunder-methods.md",
        "descriptors.md", "closures.md", "typing.md", "common-interview-questions.md",
    ],
    "02-python-concurrency": [
        "gil.md", "threading.md", "multiprocessing.md", "asyncio.md", "event-loop.md",
        "coroutine-task-future.md", "synchronization.md", "race-condition.md",
        "deadlock.md", "cpu-vs-io-bound.md", "interview-scenarios.md",
    ],
    "03-fastapi": [
        "architecture.md", "request-lifecycle.md", "sync-vs-async-endpoint.md",
        "dependency-injection.md", "middleware.md", "validation-pydantic.md",
        "authentication.md", "background-task.md", "websocket.md", "error-handling.md",
        "performance.md", "production-best-practices.md",
    ],
    "04-database-postgresql": [
        "database-fundamentals.md", "index.md", "btree-hash-gin-gist-brin.md",
        "explain-analyze.md", "query-optimization.md", "transaction.md",
        "isolation-level.md", "mvcc.md", "locks.md", "deadlock.md", "partitioning.md",
        "replication.md", "connection-pooling.md", "large-table-design.md", "sql-interview.md",
    ],
    "05-sqlalchemy": [
        "orm-vs-raw-sql.md", "session-lifecycle.md", "transaction.md", "n-plus-one.md",
        "relationship-loading.md", "async-sqlalchemy.md", "performance.md",
    ],
    "06-redis": [
        "redis-internals.md", "caching.md", "cache-patterns.md", "ttl.md",
        "distributed-lock.md", "rate-limiting.md", "pub-sub.md", "streams.md",
        "persistence.md", "sentinel-cluster.md", "failure-scenarios.md",
    ],
    "07-celery": [
        "architecture.md", "broker-worker.md", "task-lifecycle.md", "retry.md",
        "idempotency.md", "exactly-once-myth.md", "celery-redis.md", "task-routing.md",
        "scheduled-task.md", "production-problems.md",
    ],
    "08-api-design": [
        "rest-api.md", "api-versioning.md", "pagination.md", "idempotency.md",
        "rate-limiting.md", "authentication-authorization.md", "websocket.md",
        "retry-timeout.md", "api-security.md",
    ],
    "09-software-architecture": [
        "clean-architecture.md", "hexagonal-architecture.md", "layered-architecture.md",
        "domain-driven-design.md", "solid.md", "design-patterns.md",
        "modular-monolith.md", "microservices.md", "event-driven-architecture.md",
        "architecture-tradeoffs.md",
    ],
    "10-distributed-systems": [
        "fundamentals.md", "cap-theorem.md", "consistency-models.md",
        "distributed-lock.md", "idempotency.md", "retry.md", "timeout.md",
        "circuit-breaker.md", "saga.md", "outbox-pattern.md", "message-queue.md",
        "eventual-consistency.md", "failure-scenarios.md",
    ],
    "11-system-design": [
        "README.md", "system-design-framework.md", "capacity-estimation.md",
        "load-balancer.md", "caching.md", "database-scaling.md", "sharding.md",
        "message-queue.md", "observability.md", "design-chat-system.md",
        "design-notification-system.md", "design-file-processing.md",
        "design-ai-chatbot.md", "design-document-processing.md",
        "design-video-processing.md", "design-vehicle-inspection.md",
        "design-vehicle-warranty.md", "design-production-planning.md",
        "design-realtime-websocket.md", "design-task-processing.md",
    ],
    "12-docker": [
        "docker-fundamentals.md", "image-layer.md", "networking.md", "volume.md",
        "multi-stage-build.md", "docker-compose.md", "production-best-practices.md",
    ],
    "13-kubernetes": [
        "architecture.md", "pod.md", "deployment.md", "service.md", "ingress.md",
        "configmap-secret.md", "hpa.md", "resource-limit.md", "health-check.md",
        "rolling-update.md", "scheduling.md", "troubleshooting.md",
    ],
    "14-cloud": [
        "aws-core-services.md", "networking-vpc.md", "ec2.md", "ecs-eks.md", "rds.md",
        "s3.md", "load-balancer.md", "autoscaling.md", "cloud-architecture.md",
    ],
    "15-terraform-cicd": [
        "terraform-basics.md", "state.md", "module.md", "remote-backend.md", "cicd.md",
        "deployment-strategies.md", "rollback.md",
    ],
    "16-security": [
        "web-security.md", "owasp-top-10.md", "jwt.md", "oauth2.md",
        "secrets-management.md", "sql-injection.md", "csrf-xss.md", "api-security.md",
    ],
    "17-performance-reliability": [
        "performance-debugging.md", "profiling-python.md", "load-testing.md", "caching.md",
        "horizontal-scaling.md", "high-availability.md", "fault-tolerance.md",
        "observability.md", "metrics-logging-tracing.md", "sli-slo-sla.md",
        "incident-debugging.md",
    ],
    "18-ai-integration": [
        "ai-system-overview.md", "llm-basics-for-backend.md", "rag.md", "embeddings.md",
        "vector-database.md", "ai-api-integration.md", "streaming-response.md",
        "ai-job-queue.md", "ai-scalability.md", "ai-observability.md",
        "production-ai-system.md",
    ],
    "19-coding-interview": [
        "python-coding-patterns.md", "array-string.md", "hashmap.md", "stack-queue.md",
        "linked-list.md", "tree.md", "graph.md", "binary-search.md", "sliding-window.md",
        "two-pointers.md", "common-python-problems.md",
    ],
    "20-senior-scenarios": [
        "production-down.md", "api-slow.md", "database-high-cpu.md",
        "database-deadlock.md", "redis-down.md", "duplicate-message.md",
        "celery-task-duplicate.md", "memory-leak.md", "high-traffic.md",
        "data-consistency.md", "legacy-system-refactoring.md",
    ],
    "21-behavioral": [
        "senior-engineer-behavior.md", "project-story.md", "production-incident.md",
        "conflict.md", "leadership.md", "mentoring.md", "failure.md", "star-method.md",
    ],
}


CATEGORY: dict[str, dict[str, str]] = {
    "01-python-core": {
        "label": "Python Core", "scope": "runtime Python, object model và maintainability",
        "why": "giải thích hành vi runtime, tránh bug khó thấy và ra quyết định API/library có cơ sở",
        "metric": "allocation rate, RSS, GC pause, latency và correctness",
        "artifact": "module Python",
    },
    "02-python-concurrency": {
        "label": "Python Concurrency", "scope": "concurrency, parallelism và scheduling trong Python",
        "why": "chọn đúng execution model, bảo vệ shared state và giữ tail latency ổn định",
        "metric": "event-loop lag, queue depth, context switch, CPU saturation và p99 latency",
        "artifact": "concurrent service",
    },
    "03-fastapi": {
        "label": "FastAPI", "scope": "ASGI API service dùng FastAPI, Starlette và Pydantic",
        "why": "xây API có contract rõ, concurrency đúng và vận hành an toàn",
        "metric": "RPS, p95/p99 latency, error rate, event-loop lag và pool utilization",
        "artifact": "FastAPI service",
    },
    "04-database-postgresql": {
        "label": "PostgreSQL", "scope": "storage, query planning và concurrency control của PostgreSQL",
        "why": "database thường là stateful bottleneck và sai lầm có thể gây mất dữ liệu",
        "metric": "query latency, rows scanned, buffer hit ratio, lock wait, WAL lag và IOPS",
        "artifact": "PostgreSQL workload",
    },
    "05-sqlalchemy": {
        "label": "SQLAlchemy", "scope": "unit of work, ORM mapping và SQL execution",
        "why": "giữ transaction boundary đúng mà vẫn nhìn thấy chi phí SQL thực tế",
        "metric": "query count, pool wait, transaction age, fetched rows và p99 latency",
        "artifact": "SQLAlchemy data layer",
    },
    "06-redis": {
        "label": "Redis", "scope": "in-memory data structures, caching và coordination",
        "why": "giảm latency mà không biến cache thành single point of failure",
        "metric": "hit ratio, evictions, memory fragmentation, command latency và replication lag",
        "artifact": "Redis-backed component",
    },
    "07-celery": {
        "label": "Celery", "scope": "asynchronous task delivery qua broker và worker",
        "why": "tách long-running work khỏi request path nhưng vẫn kiểm soát duplicate và retry",
        "metric": "queue depth, task age, runtime, retry rate, failure rate và worker saturation",
        "artifact": "Celery task pipeline",
    },
    "08-api-design": {
        "label": "API Design", "scope": "public contract giữa client và backend",
        "why": "API khó thay đổi sau khi nhiều consumer phụ thuộc vào nó",
        "metric": "compatibility, latency, error taxonomy, abuse rate và adoption",
        "artifact": "API contract",
    },
    "09-software-architecture": {
        "label": "Software Architecture", "scope": "module boundary, dependency và evolution của codebase",
        "why": "tối ưu changeability thay vì chỉ tối ưu sơ đồ đẹp",
        "metric": "lead time, change failure rate, coupling, testability và ownership",
        "artifact": "backend architecture",
    },
    "10-distributed-systems": {
        "label": "Distributed Systems", "scope": "partial failure, message delivery và consistency",
        "why": "network không đáng tin và retry có thể đổi correctness của business operation",
        "metric": "availability, stale-read window, duplicate rate, convergence time và p99 latency",
        "artifact": "distributed workflow",
    },
    "11-system-design": {
        "label": "System Design", "scope": "capacity, component boundary và failure-mode driven design",
        "why": "biến requirement mơ hồ thành kiến trúc có thể scale và vận hành",
        "metric": "throughput, latency, availability, durability, cost và recovery time",
        "artifact": "system design",
    },
    "12-docker": {
        "label": "Docker", "scope": "container image, runtime isolation và reproducible delivery",
        "why": "đóng gói ứng dụng nhất quán và giảm supply-chain risk",
        "metric": "image size, build time, startup time, CVE count và resource use",
        "artifact": "containerized service",
    },
    "13-kubernetes": {
        "label": "Kubernetes", "scope": "declarative orchestration và workload lifecycle",
        "why": "vận hành scale, rollout và self-healing mà không che giấu application failure",
        "metric": "pod availability, restart count, saturation, scheduling latency và rollout health",
        "artifact": "Kubernetes workload",
    },
    "14-cloud": {
        "label": "Cloud", "scope": "AWS primitives và cloud-native architecture",
        "why": "thiết kế fault domain, security boundary và cost model phù hợp workload",
        "metric": "availability, utilization, cross-AZ traffic, recovery time và unit cost",
        "artifact": "cloud workload",
    },
    "15-terraform-cicd": {
        "label": "Terraform & CI/CD", "scope": "infrastructure as code và delivery pipeline",
        "why": "tạo thay đổi lặp lại được, review được và rollback có kiểm soát",
        "metric": "deployment frequency, lead time, drift, failure rate và MTTR",
        "artifact": "delivery pipeline",
    },
    "16-security": {
        "label": "Security", "scope": "identity, data protection và abuse resistance",
        "why": "security là thuộc tính end-to-end, không phải middleware thêm sau",
        "metric": "attack surface, auth failure, secret age, patch latency và incident blast radius",
        "artifact": "secure backend",
    },
    "17-performance-reliability": {
        "label": "Performance & Reliability", "scope": "measurement, resilience và operability",
        "why": "tối ưu dựa trên evidence và giữ user journey trong SLO khi có failure",
        "metric": "SLI, error budget, saturation, p99 latency, MTTR và cost per request",
        "artifact": "production service",
    },
    "18-ai-integration": {
        "label": "AI Integration", "scope": "backend orchestration cho LLM, RAG và AI service",
        "why": "kiểm soát latency, quality, privacy và chi phí của dependency xác suất",
        "metric": "time-to-first-token, groundedness, token cost, retrieval recall và fallback rate",
        "artifact": "AI-enabled backend",
    },
    "19-coding-interview": {
        "label": "Coding Interview", "scope": "data structure, algorithm và reasoning bằng Python",
        "why": "trình bày invariant, complexity và edge case một cách có hệ thống",
        "metric": "correctness, time complexity, space complexity và clarity",
        "artifact": "Python solution",
    },
    "20-senior-scenarios": {
        "label": "Production Scenario", "scope": "incident response và production decision-making",
        "why": "Senior Engineer phải giảm impact trước, tìm nguyên nhân bằng evidence và phòng tái diễn",
        "metric": "customer impact, detection time, mitigation time, MTTR và recurrence",
        "artifact": "incident response",
    },
    "21-behavioral": {
        "label": "Behavioral", "scope": "leadership, ownership và technical influence",
        "why": "level Senior được đánh giá qua impact xuyên team, không chỉ output cá nhân",
        "metric": "business outcome, team leverage, risk reduction và learning",
        "artifact": "interview story",
    },
}


FOLDER_FALLBACKS: dict[str, tuple[str, str, str]] = {
    "01-python-core": (
        "{title} là phần của Python data/object model quyết định cách object được tạo, truy cập và mở rộng.",
        "Theo dõi lookup/binding/lifecycle ở runtime, phân biệt language guarantee với chi tiết CPython và kiểm tra aliasing/mutability tại API boundary.",
        "Một shared library dùng {title} để giữ interface rõ; team thêm type test, memory benchmark và backward-compatibility check trước rollout.",
    ),
    "02-python-concurrency": (
        "{title} là cơ chế thực thi đồng thời/song song, xác định scheduling, isolation và cách chia sẻ state trong Python.",
        "Xác định execution unit (coroutine/thread/process), điểm yield/preemption, shared state và propagation của exception/cancellation; mọi fan-out phải có bound.",
        "Service xử lý vehicle telemetry áp dụng {title}, đo loop lag/queue age/CPU rồi giới hạn concurrency theo capacity downstream.",
    ),
    "03-fastapi": (
        "{title} là một phần của ASGI request/connection lifecycle trong FastAPI và ảnh hưởng trực tiếp đến contract hoặc resource scope.",
        "Request đi qua proxy, ASGI server, middleware, router, dependency/validation rồi endpoint/serialization; error và cancellation phải cleanup resource đúng scope.",
        "Vehicle API triển khai {title} cùng trace ID, typed contract, deadline và integration test cho success/error/cancellation path.",
    ),
    "04-database-postgresql": (
        "{title} là cơ chế của PostgreSQL liên quan storage, query execution hoặc transaction correctness.",
        "Reason từ access pattern và invariant; kiểm tra planner estimate/actual, tuple/page/WAL, lock/snapshot và tác động vacuum/replication thay vì chỉ nhìn SQL text.",
        "Warranty workload dùng {title} trên dữ liệu production-like; quyết định được kiểm chứng bằng EXPLAIN buffers, lock wait, WAL/IO và p99.",
    ),
    "05-sqlalchemy": (
        "{title} là behavior của SQLAlchemy data layer ánh xạ unit of work sang connection, transaction và SQL cụ thể.",
        "Session giữ identity map và pending state; flush tạo SQL, commit kết thúc transaction, loading strategy quyết định query count. Scope session theo request/task.",
        "Claim service áp dụng {title}, log SQL/query count và test rollback/concurrent update để ORM không che transaction cost.",
    ),
    "06-redis": (
        "{title} là pattern/capability của Redis dựa trên in-memory data structure, single-command atomicity và bounded durability.",
        "Chọn key schema, command atomicity, TTL/eviction, memory bound, replication/failover và semantics khi Redis unavailable; pipeline/Lua chỉ khi đo được round-trip/atomic need.",
        "Catalog/inspection service dùng {title} với TTL jitter, key version, SLO riêng và degraded path bảo vệ PostgreSQL khi cache lỗi.",
    ),
    "07-celery": (
        "{title} là một phần của Celery task-delivery lifecycle từ publish, broker reservation đến execution, acknowledgement và retry.",
        "Tách message delivery khỏi business effect; cấu hình ack/prefetch/visibility theo runtime, task idempotent và retry chỉ transient với backoff/jitter/budget.",
        "Document pipeline áp dụng {title}, route task theo resource class và giám sát oldest-task-age, duplicate, retry và worker saturation.",
    ),
    "08-api-design": (
        "{title} là quyết định trong API contract về semantics, compatibility và cách client/server phục hồi lỗi.",
        "Định nghĩa resource/state transition, validation/error taxonomy, version/concurrency control và retryability; transport status không thay thế business status.",
        "Dealer API dùng {title} với OpenAPI contract test, idempotency, rate quota và compatibility telemetry trước khi deprecate version cũ.",
    ),
    "09-software-architecture": (
        "{title} là cách tổ chức boundary và dependency để một backend thay đổi mà vẫn giữ domain invariant.",
        "Đặt policy/domain ở phía ổn định, dependency hướng vào abstraction, integration qua explicit port/event; đánh giá coupling bằng change/test/deploy path thực.",
        "Warranty domain áp dụng {title} để tách policy, claim và settlement; migration theo module seam và đo lead time/change-failure rate.",
    ),
    "10-distributed-systems": (
        "{title} là cơ chế xử lý network uncertainty, partial failure hoặc replicated state giữa nhiều process/service.",
        "Xác định consistency scope, message identity, atomic boundary, deadline và recovery; assume delay/drop/duplicate/reorder và thiết kế reconciliation.",
        "Claim workflow dùng {title} giữa API, fraud và payment; trace theo correlation ID, dedupe event và reconcile state định kỳ.",
    ),
    "11-system-design": (
        "{title} là một building block dùng để đáp ứng throughput, latency, durability hoặc operability trong thiết kế hệ thống.",
        "Bắt đầu từ requirement/con số, đặt component trên read/write path, xác định state/ownership rồi phân tích saturation, failure propagation và recovery.",
        "Kiến trúc automotive áp dụng {title} sau capacity test; rollout theo cell/canary và theo dõi SLO/cost trước khi mở rộng.",
    ),
    "12-docker": (
        "{title} là cơ chế build/runtime của container, ảnh hưởng reproducibility, isolation, startup và supply-chain security.",
        "Image tạo từ immutable layer; runtime thêm writable layer/namespaces/cgroups. Pin dependency/digest, chạy non-root, externalize state và xử lý SIGTERM.",
        "Python service dùng {title} để build một artifact nhất quán; CI scan/SBOM/sign và production kiểm tra startup/resource trước promote.",
    ),
    "13-kubernetes": (
        "{title} là Kubernetes primitive/controller dùng desired state để quản lifecycle, routing hoặc resource của workload.",
        "API object lưu desired state; controller reconcile actual state. Hiểu selector/ownership, readiness, scheduling, quota và rollout/failure semantics của primitive.",
        "Vehicle API áp dụng {title} với canary, SLO alert và downstream connection cap; test node/pod termination trước launch.",
    ),
    "14-cloud": (
        "{title} là AWS/cloud capability cung cấp compute, network, storage hoặc managed control plane trong một shared-responsibility model.",
        "Thiết kế theo account/VPC/AZ fault domain, IAM least privilege, encryption, quota và cost. Managed service giảm toil nhưng không loại bỏ data/recovery ownership.",
        "Backend multi-AZ áp dụng {title}, kiểm thử failover/restore và theo dõi utilization, cross-AZ traffic, RTO/RPO và cost per request.",
    ),
    "15-terraform-cicd": (
        "{title} là mechanism của infrastructure/delivery workflow để thay đổi có thể review, lặp lại và phục hồi.",
        "Desired configuration được plan/diff rồi apply qua state/runner có lock; pipeline tạo immutable artifact, gate bằng test/policy và promote cùng artifact.",
        "Platform team áp dụng {title} với remote state, least-privilege runner, canary và automated rollback dựa trên SLO burn.",
    ),
    "16-security": (
        "{title} là security control hoặc threat class tại trust boundary của web/API system.",
        "Xác định asset/actor/trust boundary, enforce server-side deny-by-default, validate canonical input, minimize privilege và log audit không lộ secret/PII.",
        "Multi-tenant API áp dụng {title} bằng policy test, secret rotation và abuse simulation; alert dựa signal thay vì log mọi payload.",
    ),
    "17-performance-reliability": (
        "{title} là phương pháp đo hoặc kiểm soát latency, capacity và failure để giữ user journey trong SLO.",
        "Thiết lập SLI/baseline, phân rã critical path/queueing/saturation, tạo hypothesis rồi profile/load/fault test; optimization phải so trước-sau.",
        "API production áp dụng {title} trong canary và incident; error-budget/burn-rate điều khiển rollout và backlog reliability.",
    ),
    "18-ai-integration": (
        "{title} là một bước/control trong backend pipeline gọi model, truy xuất knowledge hoặc xử lý AI job.",
        "Version model/prompt/data, đặt token/deadline/concurrency budget, tách online path khỏi ingestion/evaluation và đo quality cùng latency/cost.",
        "AI service áp dụng {title} theo tenant/ACL, stream có cancellation, fallback provider và offline evaluation trước canary.",
    ),
    "19-coding-interview": (
        "{title} là data-structure/algorithm pattern giúp giảm bài toán thành invariant và thao tác có complexity rõ.",
        "Nêu brute force, chọn representation, duy trì invariant qua mỗi iteration, chứng minh edge case/termination và phân tích time/space.",
        "Trong interview, dùng {title} sau khi làm rõ constraint; chạy dry-run nhỏ và test empty/duplicate/boundary trước tối ưu.",
    ),
    "20-senior-scenarios": (
        "{title} là production incident class cần vừa giảm customer impact vừa giữ evidence để tìm và ngăn root cause.",
        "Declare incident/owner, stabilize bằng reversible action, so baseline/change, dùng metrics-log-trace/query để kiểm chứng hypothesis rồi theo dõi recovery.",
        "On-call xử lý {title} bằng runbook, feature flag/rate limit/rollback; post-incident action có owner, deadline và verification.",
    ),
    "21-behavioral": (
        "{title} là năng lực Senior thể hiện qua decision, influence, ownership và kết quả của team trong tình huống thực.",
        "Cấu trúc STAR nhưng nhấn mạnh constraint, lựa chọn/trade-off của cá nhân, cách align stakeholder, outcome định lượng và learning.",
        "Ứng viên chuẩn bị story về {title}, rút còn 2–3 phút và luyện follow-up về conflict, alternative, failure và điều sẽ làm khác.",
    ),
}


INSIGHTS: dict[str, tuple[str, str, str]] = {
    "python-memory-model": (
        "Tên biến giữ reference tới object; assignment không copy object. CPython đặt object trên private heap, mỗi object có identity, type và reference count.",
        "Theo dõi ownership của reference, phân biệt shallow/deep copy, đo allocation bằng tracemalloc và tránh giữ object lớn qua cache/closure ngoài ý muốn.",
        "Một response cache giữ ORM object kèm relationship làm RSS tăng dù request đã kết thúc; lưu DTO nhỏ và đặt bounded eviction policy giải quyết retention.",
    ),
    "gc-reference-counting": (
        "CPython chủ yếu thu hồi bằng reference counting và dùng cyclic garbage collector để tìm reference cycle ở các generation.",
        "`del` chỉ bỏ một reference; object được giải phóng khi refcount về 0. GC theo thế hệ quét container objects, còn external resource phải đóng deterministically bằng context manager.",
        "Worker tạo cycle chứa exception traceback giữ payload lớn; quan sát generation count, phá cycle và giới hạn task-per-child thay vì gọi `gc.collect()` trên mọi request.",
    ),
    "gil": (
        "Trong CPython build mặc định có GIL, một thread tại một thời điểm thực thi Python bytecode trong một interpreter; GIL không khóa I/O và không biến compound operation thành thread-safe. CPython từ 3.13 cũng có free-threaded build tùy chọn, nên luôn nói rõ runtime/build.",
        "Thread đang block I/O thường nhả GIL; interpreter chuyển quyền theo interval và native extension có thể nhả GIL. Free-threaded build cho phép thread chạy Python song song nhưng extension chưa tương thích có thể bật lại GIL và shared state vẫn cần synchronization. Với build mặc định, CPU-bound Python thường cần process, native/vectorized code hoặc runtime phù hợp.",
        "Image preprocessing bằng Python trong async API bão hòa một core và tăng event-loop lag; chuyển sang process pool/worker queue, đo serialization overhead và giới hạn concurrency.",
    ),
    "asyncio": (
        "AsyncIO là cooperative concurrency: coroutine tự nhường quyền tại `await`, event loop multiplex I/O readiness và scheduling task.",
        "Một event loop chạy callback ngắn; `await` I/O đăng ký continuation. Blocking call chặn toàn loop, cancellation chỉ có hiệu lực tại suspension point và structured concurrency giới hạn orphan task.",
        "Gateway gọi ba AI service song song bằng `TaskGroup`, áp per-call timeout và semaphore; CPU-heavy parsing được offload khỏi loop.",
    ),
    "event-loop": (
        "Event loop là scheduler điều phối ready callbacks, timers và I/O notifications trên một OS thread.",
        "Loop poll selector, chạy ready queue rồi lặp lại; fairness phụ thuộc callback nhường quyền. Event-loop lag là tín hiệu trực tiếp của blocking work hoặc overload.",
        "p99 tăng dù CPU tổng thấp vì một worker chạy JSON serialization lớn trên loop; đo loop lag, chunk/stream response và scale worker sau khi loại blocking section.",
    ),
    "sync-vs-async-endpoint": (
        "FastAPI chạy `async def` trực tiếp trên event loop và chạy `def` endpoint trong thread pool để tránh block loop.",
        "Async chỉ có lợi khi dependency stack cũng non-blocking. Gọi driver sync trong async endpoint vẫn chặn loop; thread-pool exhaustion có thể tạo queue và tail latency.",
        "Endpoint tra PostgreSQL dùng async driver; PDF rendering CPU-bound được gửi queue. Load test đo event-loop lag và pool wait thay vì đổi mọi hàm sang `async`.",
    ),
    "request-lifecycle": (
        "Request đi qua proxy/ASGI server, middleware, routing, dependency resolution, validation, endpoint, serialization và response middleware.",
        "Context và resource scope phải kết thúc kể cả exception/cancellation; transaction không nên bao trùm network call và trace ID cần xuyên mọi lớp.",
        "Dependency `yield` mở AsyncSession cho một request, commit ở service boundary, rollback khi lỗi và đóng session trước khi response connection được tái sử dụng.",
    ),
    "index": (
        "Index là cấu trúc phụ đổi write/storage cost lấy khả năng tìm và sắp xếp ít page hơn; index tốt phải khớp predicate, ordering và distribution thực tế.",
        "Planner ước lượng selectivity từ statistics. Composite B-tree tuân left-prefix; INCLUDE hỗ trợ covering; partial index giảm footprint. Mỗi index tăng WAL và write amplification.",
        "Bảng warranty 500M dòng dùng `(vehicle_id, created_at DESC) INCLUDE (status)` cho recent history và partial index cho claim đang mở; xác nhận bằng buffers/actual rows.",
    ),
    "explain-analyze": (
        "`EXPLAIN ANALYZE` thực thi query và trả actual timing/rows cho từng plan node; `BUFFERS` cho biết cache/disk behavior.",
        "So sánh estimated với actual rows để phát hiện stale statistics/skew; đọc từ node sâu nhất, loops, rows removed, sort spill và buffer read. DML phải thử trong transaction có rollback.",
        "Query chậm do Nested Loop ước lượng 10 nhưng thực tế 2M rows; tăng statistics, sửa predicate/index rồi kiểm chứng p95 trên representative data.",
    ),
    "mvcc": (
        "PostgreSQL MVCC giữ nhiều row version để statement/transaction đọc snapshot nhất quán trong khi writer tạo version mới.",
        "Tuple có visibility metadata; UPDATE tạo tuple mới. VACUUM thu hồi dead tuples khi không còn snapshot cần chúng. Long transaction giữ xmin cũ và gây bloat.",
        "ETL transaction mở nhiều giờ làm autovacuum không dọn được bảng orders; chia batch, giám sát `xact_start`/dead tuples và tune vacuum theo bảng nóng.",
    ),
    "isolation-level": (
        "Isolation level quy định các anomaly được phép khi transaction đồng thời; PostgreSQL cung cấp Read Committed, Repeatable Read và Serializable.",
        "Read Committed lấy snapshot mỗi statement; Repeatable Read dùng snapshot transaction; Serializable SSI phát hiện dangerous structure và có thể abort, nên application phải retry toàn transaction.",
        "Hai request cùng cấp warranty benefit cần row lock/atomic update hoặc Serializable retry; chỉ kiểm tra rồi ghi ở Read Committed có thể vi phạm invariant.",
    ),
    "connection-pooling": (
        "Connection pool tái sử dụng connection đắt đỏ và giới hạn concurrency đi vào PostgreSQL; pool không tạo thêm database capacity.",
        "Tổng connection = replicas × workers × pool size cộng background jobs. Pool wait cho thấy backpressure; PgBouncer transaction mode giảm session cost nhưng hạn chế session state/prepared behavior.",
        "Scale API từ 20 lên 200 pod mà pool 20 sẽ đòi 4.000 connection; đặt global budget, pool nhỏ, PgBouncer và queue/rate limit để bảo vệ DB.",
    ),
    "caching": (
        "Caching lưu kết quả có thể tái tạo gần consumer để giảm latency và load; khó nhất là invalidation, staleness và stampede.",
        "Cache-aside đọc cache rồi source; TTL giới hạn stale window. Dùng key version, TTL jitter, request coalescing và negative caching có kiểm soát.",
        "Catalog cache hết hạn đồng loạt gây DB spike; thêm TTL jitter, single-flight, stale-while-revalidate và circuit breaker để degraded read thay vì outage.",
    ),
    "distributed-lock": (
        "Distributed lock phối hợp nhiều process qua shared service nhưng lease expiry và network pause khiến mutual exclusion tuyệt đối khó đảm bảo.",
        "Owner token ngăn client khác unlock; lease cần bounded work/renewal. Fencing token tăng đơn điệu giúp downstream từ chối stale holder; DB constraint thường an toàn hơn cho invariant dữ liệu.",
        "Hai worker xử lý cùng vehicle không chỉ dựa Redis lock: dùng fencing token hoặc conditional DB update để worker đã mất lease không ghi đè kết quả mới.",
    ),
    "idempotency": (
        "Operation idempotent cho cùng logical request nhiều lần nhưng effect quan sát được chỉ tương đương một lần.",
        "Client gửi idempotency key; server atomically claim key và lưu response/status cùng business transaction hoặc unique constraint. Scope, canonical payload, TTL và concurrent duplicate phải rõ.",
        "Create warranty claim đặt unique `(tenant_id, idempotency_key)`; duplicate đang chạy nhận 409/202, duplicate hoàn tất nhận response cũ, payload khác bị từ chối.",
    ),
    "retry": (
        "Retry là phản ứng với transient failure, nhưng tạo load amplification và chỉ an toàn khi operation idempotent hoặc có deduplication.",
        "Dùng exponential backoff có full jitter, deadline chung, retry budget và chỉ retry mã lỗi phù hợp. Circuit breaker chặn retry vào dependency đang suy yếu.",
        "10.000 request timeout không retry tức thì ba lần; gateway giới hạn hai attempt trong deadline, jitter, shed load và theo dõi retry-success ratio.",
    ),
    "timeout": (
        "Timeout biến chờ vô hạn thành failure có giới hạn; một request cần end-to-end deadline được chia cho từng hop.",
        "Connect, read, write và pool timeout giải quyết failure khác nhau. Child timeout phải ngắn hơn caller deadline và cancellation cần truyền xuống để giải phóng resource.",
        "API budget 800ms dành 100ms queue, 400ms database, 200ms downstream và 100ms serialize; fallback khi AI provider vượt budget.",
    ),
    "outbox-pattern": (
        "Transactional outbox ghi business state và event vào cùng local DB transaction, rồi relay publish event bất đồng bộ.",
        "Atomic commit loại dual-write gap; relay poll/CDC publish at-least-once, consumer vẫn phải idempotent. Theo dõi outbox age và dọn bản ghi an toàn.",
        "Warranty claim commit cùng `ClaimCreated`; relay publish Kafka, notification dedupe theo event ID và reconciliation phát hiện stuck row.",
    ),
    "exactly-once-myth": (
        "End-to-end exactly-once effect hiếm khi đến từ queue; broker acknowledgement race tạo redelivery, còn external side effect nằm ngoài broker transaction.",
        "Thiết kế at-least-once delivery cùng idempotent consumer, unique constraint/inbox và reconciliation. Exactly-once scope cụ thể có thể đạt bằng transactional boundary hẹp.",
        "Worker gửi email rồi crash trước ack sẽ chạy lại; ghi delivery record trước/sau provider call với provider idempotency key để duplicate không gửi lần hai.",
    ),
    "hpa": (
        "Horizontal Pod Autoscaler điều chỉnh replica theo observed metric, nhưng chỉ scale stateless compute và phản ứng sau một độ trễ.",
        "Resource request quyết định utilization denominator; custom metric như queue age thường sát nhu cầu hơn CPU. Stabilization và max surge tránh oscillation và downstream overload.",
        "Celery worker scale theo oldest-task-age nhưng cap theo DB connection budget; scale-down chỉ sau khi worker drain task để không tạo redelivery storm.",
    ),
    "resource-limit": (
        "Kubernetes request dùng cho scheduling, limit áp runtime; CPU limit gây throttling còn memory vượt limit thường bị OOMKilled.",
        "Đặt request từ observed working set/CPU, giữ headroom và đo throttled seconds/OOM. Limit quá thấp làm tail latency xấu dù node còn CPU.",
        "API p99 spike do CPU quota 500m throttling; profile, tăng request/limit, scale horizontally và tách background CPU work.",
    ),
    "rag": (
        "RAG truy xuất evidence liên quan rồi đưa vào prompt để LLM trả lời grounded trên dữ liệu riêng/cập nhật.",
        "Ingestion parse/chunk/embed/index; query embed/retrieve/filter/rerank; generation trích citation. Đánh giá retrieval recall riêng với answer quality và chống prompt injection từ document.",
        "Chatbot hướng dẫn kỹ thuật lọc theo model xe/version/ACL, hybrid retrieve top-50, rerank top-8, trả citation và abstain khi evidence yếu.",
    ),
    "embeddings": (
        "Embedding ánh xạ nội dung thành vector để đo semantic similarity; model/version/dimension là một phần của schema dữ liệu.",
        "Normalize theo metric phù hợp, batch request, cache theo content hash và re-index versioned khi đổi model. Vector gần không đồng nghĩa fact đúng.",
        "Document pipeline lưu `embedding_model_version`; dual-write index mới và shadow evaluate trước khi chuyển traffic để tránh quality regression.",
    ),
    "vector-database": (
        "Vector database lưu vector và metadata, dùng approximate nearest-neighbor index để đổi một phần recall lấy latency/scale.",
        "HNSW nhanh nhưng memory/build cost cao; IVF cần train và tune probe. Metadata filtering, multi-tenancy, backup và reindex quan trọng như similarity search.",
        "Tenant lớn được partition; filter ACL trước/đồng thời ANN, benchmark recall@k và p95 với distribution production thay vì dataset nhỏ.",
    ),
    "streaming-response": (
        "Streaming gửi token/chunk khi sẵn sàng để giảm time-to-first-byte, không nhất thiết giảm tổng thời gian xử lý.",
        "SSE đơn giản cho server-to-client; WebSocket cho duplex. Phải xử lý disconnect/cancellation, backpressure, proxy buffering và partial response observability.",
        "LLM gateway stream SSE, heartbeat qua proxy, hủy provider call khi client đóng và ghi usage cuối stream qua idempotent finalizer.",
    ),
    "ai-system-overview": (
        "AI-enabled backend là hệ thống software thông thường bao quanh dependency model xác suất: identity, retrieval, orchestration, streaming, safety, cost và observability.",
        "Online path: authenticate → retrieve/filter/rerank context → build versioned prompt → call model trong deadline/token budget → stream/cite. Offline path ingest/chunk/embed/index/evaluate; mọi artifact mang tenant, ACL và model/data version.",
        "Automotive assistant chỉ trả answer khi evidence vượt threshold, cite manual version đúng VIN/model, fallback search khi provider lỗi và ghi quality/cost trace không lưu PII thô.",
    ),
    "llm-basics-for-backend": (
        "LLM với Backend Engineer là remote/stateless inference API nhận token context và sinh token xác suất; context window, sampling, quota và price là system constraints.",
        "Prompt được tokenize; generation autoregressive làm latency/cost tăng theo input/output token. Backend quản model routing, structured output validation, timeout/cancellation, safety và prompt/model version.",
        "Claim summarizer ép JSON schema, validate fact/citation, retry repair tối đa một lần và chuyển human review khi confidence/evidence thấp.",
    ),
    "ai-api-integration": (
        "AI API integration là adapter/bulkhead bao quanh provider model để domain code không phụ thuộc SDK, error taxonomy hoặc streaming format cụ thể.",
        "Chuẩn hóa request/response/usage, connect/read/overall deadline, concurrency semaphore, rate-limit, retry 429/5xx có jitter và circuit/fallback. Không retry sau partial stream như request chưa xảy ra.",
        "Gateway route model theo policy/region, dùng provider idempotency nếu có, redacts PII và đo first-token/total latency, tokens, retry/fallback và cost.",
    ),
    "ai-job-queue": (
        "AI job queue tách batch/long-running inference khỏi request path và hấp thụ burst theo GPU/provider capacity.",
        "Job state machine queued/running/succeeded/failed/cancelled; payload lớn ở object store, message chỉ chứa pointer/version. Lease/heartbeat, idempotent stage, delayed retry và DLQ/reconciliation.",
        "Document embedding route theo model/dimension, batch theo token limit và scale worker bằng oldest-job-age trong quota provider.",
    ),
    "ai-scalability": (
        "AI scalability tối ưu đồng thời compute/provider quota, token throughput, retrieval latency, quality và cost per successful answer.",
        "Phân tách online/offline, batch embedding, cache theo version/ACL, route model theo complexity, cap output token và shed/admit theo tenant. Autoscale không vượt DB/vector/provider/GPU capacity.",
        "Chatbot dùng small model cho classification, premium model chỉ cho complex query; semantic cache có tenant/prompt/model version và không dùng cho sensitive answer.",
    ),
    "ai-observability": (
        "AI observability nối system telemetry với quality/evaluation: request có thể HTTP 200 nhưng answer không grounded hoặc vi phạm policy.",
        "Trace stage retrieval/rerank/prompt/provider/stream; log version và token usage không lộ content; offline golden set + online feedback/citation checks đo recall, groundedness, refusal và drift.",
        "Dashboard phân đoạn theo tenant/language/model: TTFT/p99, token/cost, retrieval recall proxy, fallback, safety block và useful-answer rate.",
    ),
    "production-ai-system": (
        "Production AI system là versioned socio-technical system gồm data, retrieval, model, prompt, safety, human escalation và operational controls.",
        "Release theo offline eval → shadow → canary; pin/version mọi input, kiểm tra ACL/prompt injection, đặt budget/deadline/fallback và lưu trace đủ replay nhưng tuân privacy/retention.",
        "Model upgrade chỉ promote khi quality slice không regression, cost/latency trong budget và rollback không cần re-index; nếu đổi embedding thì dual-index migration.",
    ),
    "observability": (
        "Observability cho phép suy ra internal state từ metrics, logs và traces; mục tiêu là trả lời câu hỏi mới khi production hỏng.",
        "Metrics cảnh báo xu hướng, logs giải thích event, traces nối critical path. Propagate correlation ID, kiểm soát cardinality và gắn telemetry vào SLO.",
        "p99 chatbot tăng: trace tách retrieval, rerank, first token và DB pool wait; exemplar nối histogram tới trace thay vì dò log thủ công.",
    ),
    "sli-slo-sla": (
        "SLI là phép đo user-visible, SLO là target nội bộ, SLA là cam kết có hậu quả; error budget cân bằng reliability với tốc độ thay đổi.",
        "Dùng good events/valid events trên rolling window, multi-window burn-rate alert và loại trừ có lý do. Trung bình latency không đại diện tail.",
        "SLO 99.9% successful request dưới 800ms; burn nhanh dừng rollout và page, burn chậm tạo ticket để xử lý capacity/debt.",
    ),
    "production-down": (
        "Production down là incident user journey critical không còn đáp ứng SLO; mục tiêu đầu tiên là giảm impact, không phải chứng minh root cause ngay.",
        "Declare severity/commander/comms, kiểm tra blast radius và recent change; dùng rollback, traffic shift, feature disable hoặc load shedding có tính reversible. Giữ timeline/evidence, xác nhận recovery bằng SLI rồi mới RCA và follow-up.",
        "Khi claim API lỗi toàn vùng, incident commander rollback release, tắt enrichment không critical và rate-limit write; sau recovery team tái hiện connection leak và thêm canary gate theo pool wait.",
    ),
    "api-slow": (
        "API slow là latency regression trên một hoặc nhiều percentile; average bình thường không loại trừ queueing, hot key hoặc một route/tenant bị ảnh hưởng.",
        "Tách queue time và service time; phân rã trace qua gateway, app, pool, DB/cache/downstream. So sánh p50/p95/p99 với deploy/traffic, xem saturation và error/retry. Mitigate bằng rollback/load shed/cache/fallback rồi profile đúng bottleneck.",
        "Warranty API tăng 100ms lên 3s: trace cho thấy DB pool wait, top query đổi plan sau data skew; rollback query, rate-limit và bổ sung extended statistics/index sau representative load test.",
    ),
    "database-high-cpu": (
        "Database high CPU là symptom có thể do query plan xấu, traffic/fan-out, missing index, sort/hash, autovacuum hoặc connection concurrency; CPU cao không tự chỉ ra root cause.",
        "Đầu tiên xác nhận blast radius, traffic/deploy/schema change. Xem active query/wait, `pg_stat_statements` theo total/call time/calls/rows; connection, lock/deadlock, IO/WAL và replica lag. Dùng `EXPLAIN (ANALYZE, BUFFERS)` an toàn trên representative query: estimate-vs-actual, scan/join, loops, rows removed và spill. Kiểm missing/unused/oversized index, stale statistics và bloat; không tạo index hoặc restart mù.",
        "CPU 95% do Nested Loop estimate 10 nhưng actual 2M: giảm traffic/rollback trước, refresh/tăng statistics và index đúng predicate; thêm plan regression/capacity guard.",
    ),
    "database-deadlock": (
        "Database deadlock là chu trình wait-for giữa transaction; PostgreSQL phát hiện và abort một victim, khác với lock wait dài nhưng không có chu trình.",
        "Thu thập deadlock log và transaction statements, dựng wait graph, kiểm tra transaction boundary. Fix bằng lock resource theo thứ tự nhất quán, transaction ngắn, index để khóa ít row; application retry toàn transaction với jitter.",
        "Claim và inventory update lock theo thứ tự ngược; chuẩn hóa order theo ID, tách remote call khỏi transaction và alert deadlock rate thay vì tăng `deadlock_timeout` để che lỗi.",
    ),
    "redis-down": (
        "Redis down là failure của cache/coordination/rate-limit dependency; severity phụ thuộc Redis có bị dùng nhầm làm source of truth hay không.",
        "Circuit-break nhanh, chọn stale/fail-open/fail-closed theo endpoint; coalesce miss, rate-limit và shed load để bảo vệ DB. Khi phục hồi, reconnect có jitter và warm hot keys dần; đối soát session/lock/stream effect riêng.",
        "Catalog giữ stale cache để read tiếp, login rate limiter fail-closed có emergency capacity, database nhận bounded fallback; warm top keys trước khi mở traffic hoàn toàn.",
    ),
    "duplicate-message": (
        "Duplicate message là delivery lặp do ack timeout, producer retry, broker failover hoặc consumer crash; broker delivery và business effect là hai scope khác nhau.",
        "Gắn immutable message/event ID và business key; consumer atomically insert inbox/unique row cùng state transition. Ack sau durable effect, retry transient, duplicate trả success; external side effect dùng provider key/ledger và reconciliation.",
        "`ClaimApproved` đến hai lần nhưng unique `(consumer, event_id)` khiến settlement chỉ ghi một ledger entry; projection có thể replay từ log.",
    ),
    "celery-task-duplicate": (
        "Celery task duplicate là hệ quả bình thường của at-least-once delivery khi worker crash/lease hết hạn/ack thất lạc; task ID giống hay khác không quyết định business idempotency.",
        "Thiết kế idempotency theo business key bằng unique constraint/inbox, ack/visibility timeout hợp task runtime, retry có classification/backoff. Lock chỉ giảm concurrent duplicate; DB invariant và reconciliation mới bảo vệ effect.",
        "Task tạo report commit artifact rồi crash trước ack; lần chạy lại thấy unique job-stage đã complete và trả artifact cũ, không generate/upload thêm.",
    ),
    "memory-leak": (
        "Memory leak/retention là RSS hoặc live object tăng không trở về baseline; cần tách Python object retention, unbounded cache, native allocation và allocator fragmentation.",
        "Vẽ slope theo request/task, RSS vs heap, GC stats và object type; dùng tracemalloc snapshot diff, heap/native profiler và reproduction dài. Giảm impact bằng recycle có kiểm soát, rồi sửa ownership/bound/cache; không gọi GC mỗi request.",
        "Celery worker giữ traceback/payload qua global list; snapshot chỉ ra retaining path, team bỏ reference, cap cache và đặt `max_tasks_per_child` như safety net chứ không phải root fix.",
    ),
    "high-traffic": (
        "High traffic scenario kiểm tra toàn critical path từ load balancer đến database/queue; scale stateless API đơn lẻ có thể làm stateful dependency sập nhanh hơn.",
        "Từ 1k lên 20k RPS: đo sustainable RPS/worker ở 60–70% utilization; load balancer phân phối nhiều pod/process; giữ async path non-blocking và đẩy CPU work sang process/queue. Budget DB connection, tối ưu query/index, cache hot data trong Redis, dùng read replica chỉ cho stale-tolerant read, HPA theo saturation/queue age và rate-limit theo tenant.",
        "Trước campaign, load test có skew và cache-cold; pre-scale API/Redis, cap pool, warm cache, bật feature degradation và theo dõi SLO burn/DB CPU/pool wait/queue lag.",
    ),
    "data-consistency": (
        "Data consistency incident xảy ra khi các source/projection hoặc concurrent transition vi phạm business invariant; sửa UI không đủ nếu authoritative state đã sai.",
        "Chặn write gây hại, xác định source of truth và affected key/time window, bảo toàn evidence. Dùng constraint/version/transaction/outbox để ngăn mới; backfill idempotent có dry-run/checkpoint, reconcile và audit từng correction.",
        "Claim approved nhưng payment event mất do dual write: dừng affected flow, replay từ outbox/reconciliation, thêm transactional outbox và alert oldest-unpublished age.",
    ),
    "legacy-system-refactoring": (
        "Legacy refactoring là thay đổi cấu trúc mà giữ observable behavior và business continuity; rủi ro lớn nằm ở hidden contract/data/integration chứ không chỉ code quality.",
        "Characterization test và production telemetry trước; tạo seam/anti-corruption layer, strangler theo use case, shadow/dual-read có comparison. Migration write cần source-of-truth rõ, rollback và reconciliation; tránh big-bang rewrite.",
        "Tách warranty eligibility khỏi monolith theo branch-by-abstraction; shadow decision, so mismatch theo policy version rồi canary dealer trước khi chuyển ownership.",
    ),
}


SCOPED_INSIGHTS: dict[tuple[str, str], tuple[str, str, str]] = {
    ("03-fastapi", "architecture"): (
        "FastAPI là ASGI framework ghép Starlette (HTTP/WebSocket), Pydantic (schema/validation) và dependency injection để tạo typed API.",
        "Uvicorn/ASGI server gọi application per connection/request; Starlette routing/middleware xử lý transport, FastAPI resolve dependency và validate/serialize. Worker process và event loop là capacity boundary khác nhau.",
        "API chạy nhiều process/container sau load balancer; dependency tạo resource request-scoped, telemetry theo route và CPU job tách khỏi ASGI loop.",
    ),
    ("03-fastapi", "dependency-injection"): (
        "FastAPI DI khai báo dependency graph qua callable/`Depends`, cache kết quả trong request và hỗ trợ `yield` cleanup.",
        "Framework resolve graph theo thứ tự, truyền sub-dependency và chạy phần sau `yield` khi request kết thúc. DI tiện cho auth/session nhưng không thay thế domain boundary hoặc service container toàn cục.",
        "`get_session` tạo AsyncSession mỗi request; `current_principal` xác thực rồi policy service authorize resource; test override dependency ở integration boundary.",
    ),
    ("03-fastapi", "middleware"): (
        "ASGI middleware bọc application để xử lý cross-cutting concern trên mọi request/response hoặc WebSocket scope.",
        "Middleware tạo stack ngoài-vào/trong-ra; thứ tự quyết định CORS, auth, exception và tracing behavior. Đọc body/serialize trong middleware có thể tăng memory/latency và phá streaming.",
        "Trace/request ID middleware ghi duration/status nhưng redact body; authorization theo resource vẫn ở endpoint/service vì middleware thiếu domain context.",
    ),
    ("03-fastapi", "validation-pydantic"): (
        "Pydantic model định nghĩa boundary schema và chuyển/validate untrusted input thành typed value; validation không đồng nghĩa business authorization/invariant.",
        "Core schema parse field/constraint, model validator xử lý cross-field; strict mode giảm coercion bất ngờ. Response model lọc/serialize output và là phần public contract.",
        "Warranty API tách CreateClaimRequest, domain command và ClaimResponse; reject unknown/invalid fields, version schema và không expose ORM object trực tiếp.",
    ),
    ("03-fastapi", "authentication"): (
        "Authentication trong FastAPI xác minh caller credential; authorization quyết định action trên resource/tenant cụ thể.",
        "Dependency validate signature, issuer, audience, expiry và revocation/session policy; trả Principal tối thiểu. Policy layer kiểm tenant/ownership/role, deny by default và audit sensitive action.",
        "Gateway có thể verify token sơ bộ nhưng service vẫn enforce resource authorization; JWKS cache có bounded stale fallback và rotation test.",
    ),
    ("03-fastapi", "background-task"): (
        "FastAPI BackgroundTasks chạy in-process sau khi response được gửi; không phải durable queue và mất khi process crash/restart.",
        "Phù hợp best-effort task nhỏ, nhanh, idempotent; task CPU/blocking vẫn chiếm resource worker. Work quan trọng/dài cần Celery/queue có persisted state/retry/observability.",
        "Ghi analytics nhẹ có thể background; generate inspection report và gửi settlement phải qua durable task/outbox.",
    ),
    ("03-fastapi", "websocket"): (
        "FastAPI WebSocket giữ kết nối duplex lâu dài trên ASGI, khác request-response HTTP và tạo state/routing/backpressure riêng.",
        "Sau upgrade, loop receive/send frame; heartbeat phát hiện half-open, per-connection queue cần bound và disconnect phải cancel producer. Scale nhiều pod cần shared broker/connection registry.",
        "Inspection progress stream dùng auth lúc connect + revalidate subscription ACL, Redis/Kafka fan-out, slow-consumer policy và REST resume cursor.",
    ),
    ("03-fastapi", "error-handling"): (
        "Error handling chuyển domain/infrastructure failure thành stable API error contract mà không rò stack trace/secret.",
        "Exception handler map typed exception → status/code/retryable/correlation ID; cancellation/timeout không bị nuốt; log một lần tại ownership boundary và preserve cause.",
        "Duplicate claim trả stable conflict/idempotent response; provider timeout trả 503 có retry hint, metric và trace thay vì generic 500.",
    ),
    ("03-fastapi", "performance"): (
        "FastAPI performance là kết quả toàn path: queue, event loop/thread pool, validation/serialization, pool, DB/cache/downstream và network.",
        "Đo p50/p95/p99, loop lag, thread/pool wait và saturation; loại blocking/ N+1 trước tăng worker. Worker count theo benchmark/memory và connection budget, không theo công thức CPU mù.",
        "Load test 20k RPS dùng traffic distribution/cache-cold/failure; stream/chunk response lớn và cap fan-out để p99 không sập.",
    ),
    ("03-fastapi", "production-best-practices"): (
        "Production FastAPI cần process lifecycle, contract, resource budget, security và operability nhất quán từ proxy đến dependency.",
        "Pin/build immutable image, non-root, graceful shutdown; readiness khác liveness; deadline/size/concurrency limit; session per request; structured log/metrics/trace và safe migration.",
        "Kubernetes rollout chỉ promote khi SLO/loop lag/pool wait ổn; pod dừng nhận traffic rồi drain WebSocket/request trước SIGKILL.",
    ),
    ("05-sqlalchemy", "orm-vs-raw-sql"): (
        "ORM tối ưu mapping/unit-of-work/productivity; raw SQL cho phép kiểm soát plan, bulk/CTE/window và database-specific feature. Đây không phải lựa chọn loại trừ tuyệt đối.",
        "SQLAlchemy Core/ORM cùng tạo SQL; chi phí nằm ở query shape, hydration/identity map và round trip. Chọn per use case, giữ transaction/repository boundary chung và inspect generated SQL.",
        "CRUD claim dùng ORM; báo cáo aggregate lớn dùng Core/raw SQL đã profile, vẫn parameterized và integration-tested trên PostgreSQL.",
    ),
    ("05-sqlalchemy", "session-lifecycle"): (
        "Session là unit-of-work + identity map, không phải database connection; nó checkout connection khi cần và không thread/task-safe để chia sẻ.",
        "Session track transient/pending/persistent state, autoflush trước query và expire theo configuration. Scope mỗi request/task, rollback khi exception, close trong finally.",
        "FastAPI dependency yield session; service đặt transaction boundary, không truyền ORM object sống sang Celery task hoặc cache.",
    ),
    ("05-sqlalchemy", "transaction"): (
        "SQLAlchemy transaction bọc DBAPI transaction qua Session/Connection; flush gửi SQL nhưng chỉ commit mới làm transaction durable.",
        "`begin()` quản commit/rollback; nested transaction thường dùng SAVEPOINT. Transaction boundary phải theo business use case, không tự commit rải trong repository.",
        "Create claim + outbox event nằm cùng `session.begin()`; external API call xảy ra ngoài transaction và flow dùng state machine/reconciliation.",
    ),
    ("05-sqlalchemy", "n-plus-one"): (
        "N+1 xảy ra khi tải N parent rồi lazy-load relationship bằng N query phụ, làm round-trip tăng theo result size.",
        "Detect bằng query count/trace; `selectinload` thường tốt cho collection, `joinedload` có thể nhân row, explicit projection cho API. Disable/raise lazy load ở path nhạy cảm.",
        "List 100 claims từng load vehicle: đổi sang `selectinload` hai query hoặc projection join, đo row bytes và p99 trước/sau.",
    ),
    ("05-sqlalchemy", "relationship-loading"): (
        "Relationship loading strategy quyết định thời điểm và SQL shape để lấy object graph: lazy, joined, select-in hoặc explicit.",
        "Joined load giảm round trip nhưng cartesian amplification với nhiều collection; select-in thêm query có bounded IDs; lazy tiện nhưng che I/O. Chọn theo cardinality/access path.",
        "Claim detail joined-load one-to-one policy và select-in line items; list endpoint chỉ projection field cần thiết.",
    ),
    ("05-sqlalchemy", "async-sqlalchemy"): (
        "Async SQLAlchemy dùng asyncio-compatible dialect/driver để chờ network không block event loop; database vẫn thực thi query như cũ.",
        "AsyncSession không chia sẻ giữa concurrent task; implicit lazy I/O dễ gây lỗi/bất ngờ. Dùng explicit eager load, `async with`, pool nhỏ và không fan-out query vô hạn.",
        "FastAPI request dùng `asyncpg`/AsyncSession; TaskGroup không chạy nhiều operation đồng thời trên cùng session, mỗi unit-of-work có session riêng.",
    ),
    ("06-redis", "redis-internals"): (
        "Redis phục vụ command chủ yếu qua event loop và in-memory structures; single command atomic nhưng persistence/replication/failover có cửa sổ durability/consistency.",
        "Command chậm/blocking ảnh hưởng client khác; encoding, key/value size và allocator quyết định memory. Background fork/rewrite, replication backlog và eviction tạo latency/failure mode.",
        "Theo dõi slowlog, command p99, used_memory_rss, fragmentation, evictions và replication lag; tránh key/value lớn/hot và O(N) command.",
    ),
    ("06-redis", "cache-patterns"): (
        "Cache-aside, read/write-through, write-behind và refresh-ahead khác nhau ở owner của population/invalidation và consistency window.",
        "Cache-aside đơn giản nhưng miss race/stampede; write-through đồng bộ tăng write latency; write-behind có data-loss/reorder risk. Key có namespace/version và TTL/fallback rõ.",
        "Vehicle catalog dùng cache-aside + event invalidation + TTL jitter; price/eligibility critical xác minh version/source.",
    ),
    ("06-redis", "ttl"): (
        "TTL đặt lifetime cho key và bounds staleness/memory, nhưng expiry timing không phải business correctness guarantee.",
        "Redis expire passive khi access và active sampling; nhiều key cùng TTL tạo cliff. Dùng jitter, logical version, refresh-ahead và quan sát expired/evicted khác nhau.",
        "Token/session TTL theo security policy; catalog key thêm ±10% jitter để tránh hàng triệu miss cùng giây.",
    ),
    ("06-redis", "rate-limiting"): (
        "Rate limiting kiểm soát request theo identity/time/resource bằng fixed/sliding window, token bucket hoặc leaky bucket.",
        "Redis Lua/function atomically check-update-expire; key cardinality và clock/cluster slot quan trọng. Distributed limiter có thể approximate; chọn fail-open/closed theo abuse risk.",
        "Login dùng fail-closed/stricter local fallback; read catalog fail-open có emergency gateway cap và per-tenant quota.",
    ),
    ("06-redis", "pub-sub"): (
        "Redis Pub/Sub là ephemeral fan-out: subscriber offline hoặc disconnect sẽ mất message, không có consumer acknowledgement/history.",
        "Publisher gửi channel, connected subscribers nhận realtime; cluster/failover và slow consumer cần hiểu. Dùng cho invalidation/presence hint, không cho durable business workflow.",
        "Cache invalidation có thể dùng Pub/Sub cộng TTL safety; warranty payment phải dùng durable stream/queue + idempotent consumer.",
    ),
    ("06-redis", "streams"): (
        "Redis Streams là append-only log có ID, consumer group, pending entries và acknowledgement; vẫn có duplicate khi claim/retry/failover.",
        "Consumer đọc group, xử lý rồi XACK; idle pending được claim. Trim/retention, hot stream, pending growth và persistence policy quyết định reliability.",
        "Telemetry pipeline dùng stream theo site, consumer idempotent và monitor oldest pending; task nhiều giờ phù hợp queue/workflow chuyên dụng hơn.",
    ),
    ("06-redis", "persistence"): (
        "Redis RDB snapshot và AOF log đổi recovery point, write latency, storage và restart time; replication không thay thế backup.",
        "RDB có point-in-time gap; AOF fsync policy bounds loss/latency và rewrite compacts log. Test restore, disk full/fork memory và corruption path.",
        "Cache có thể tắt persistence; rate/quota/session cần đánh giá data-loss semantics, backup và recovery warm-up riêng.",
    ),
    ("06-redis", "sentinel-cluster"): (
        "Sentinel cung cấp monitoring/failover cho primary-replica; Redis Cluster thêm sharding hash slot và per-shard failover.",
        "Failover không zero-loss vì replication async; client phải refresh topology/retry có bound. Multi-key atomic command cần cùng hash slot; reshard có operational cost.",
        "Workload vượt memory một node dùng Cluster, nhưng hot key vẫn nóng một shard; chaos test failover và client reconnect storm.",
    ),
    ("07-celery", "architecture"): (
        "Celery gồm producer, broker, worker pool, optional result backend và scheduler; broker delivery không bao trọn external business effect.",
        "Producer serialize/publish; worker reserve/prefetch, execute rồi ack theo config. Concurrency pool, routing, visibility timeout và broker semantics quyết định throughput/duplicate.",
        "Document service ghi job + outbox, publisher gửi task, worker idempotent update stage; result lớn vào object store thay vì result backend.",
    ),
    ("07-celery", "broker-worker"): (
        "Broker buffer/route message; worker reserve và thực thi bằng prefork/thread/greenlet tùy workload. Queue depth không bằng tiến độ nếu task runtime skew.",
        "Prefetch cao tăng throughput nhưng fairness kém; ack late tăng redelivery safety nhưng đòi idempotency. Tách queue theo runtime/resource/SLO và graceful drain khi deploy.",
        "OCR task dài dùng prefork queue/prefetch thấp; I/O webhook queue riêng; monitor oldest age, active/reserved và runtime percentile.",
    ),
    ("07-celery", "task-lifecycle"): (
        "Celery task lifecycle là publish → queued → reserved → started → succeeded/failed/retried/revoked, với race quanh ack và visibility lease.",
        "State event/result backend có thể lag và không phải business source of truth. Timeout soft/hard, cancellation/revoke và worker loss đều cần domain state/reconciliation.",
        "Inspection job lưu authoritative stage/attempt ở PostgreSQL; Celery event chỉ telemetry, callback kiểm expected state/version.",
    ),
    ("07-celery", "celery-redis"): (
        "Dùng Redis làm Celery broker/result backend đơn giản nhưng mang theo memory, visibility timeout, failover và eviction/persistence constraints.",
        "Task unacked quá visibility timeout có thể redeliver trong khi bản cũ còn chạy; result TTL/size phải bound. Không dùng cùng Redis cache eviction policy cho critical broker data.",
        "Long task có runtime vượt lease được route sang broker/workflow phù hợp hoặc cấu hình/heartbeat đúng; load test failover và duplicate.",
    ),
    ("07-celery", "task-routing"): (
        "Task routing map task/tenant/priority/resource class sang queue/worker để isolation và scheduling phù hợp.",
        "Route rõ tại producer/config, tách CPU/GPU/I/O/long/urgent; quota/fairness ngăn noisy neighbor. Quá nhiều queue tăng capacity fragmentation/operations.",
        "Transactional notification không xếp sau campaign; OCR và GPU vision có queue/concurrency/cost SLO riêng.",
    ),
    ("07-celery", "scheduled-task"): (
        "Celery Beat phát task theo lịch nhưng multiple scheduler hoặc restart/timezone có thể tạo duplicate/missed timing; schedule không tạo exactly-once effect.",
        "Đảm bảo một scheduler active hoặc dùng durable scheduler; task nhận logical window key và idempotent claim. Xử lý catch-up, clock/timezone và long overlap.",
        "Daily reconciliation dùng key `(job, business_date)` unique; nếu run trước chưa xong, policy skip/queue/replace explicit.",
    ),
    ("07-celery", "production-problems"): (
        "Celery production problems thường là queue lag, retry storm, poison task, worker memory growth, unfair prefetch, broker failover và invisible duplicate.",
        "Dashboard theo queue oldest age/runtime/retry/failure/reserved/worker RSS; circuit-break producer, quarantine poison, cap retry và drain deploy. Reconciliation dựa business state.",
        "Provider outage tạo retry storm: pause route, backoff full jitter, retry budget/DLQ; autoscale worker bị cap theo provider/DB capacity.",
    ),
}


def title_from_name(filename: str) -> str:
    stem = filename.removesuffix(".md")
    special = {
        "gil": "Global Interpreter Lock (GIL)", "asyncio": "AsyncIO",
        "mvcc": "PostgreSQL MVCC", "jwt": "JSON Web Token (JWT)",
        "oauth2": "OAuth 2.0", "hpa": "Horizontal Pod Autoscaler (HPA)",
        "sli-slo-sla": "SLI, SLO và SLA", "csrf-xss": "CSRF và XSS",
        "btree-hash-gin-gist-brin": "PostgreSQL Index Types: B-tree, Hash, GIN, GiST, BRIN",
        "ecs-eks": "AWS ECS và EKS", "rds": "Amazon RDS", "s3": "Amazon S3",
        "ec2": "Amazon EC2", "cicd": "CI/CD", "solid": "SOLID Principles",
        "rag": "Retrieval-Augmented Generation (RAG)",
        "ai-system-overview": "AI System Integration Overview",
        "ai-api-integration": "AI API Integration",
        "ai-job-queue": "AI Job Queue",
        "ai-scalability": "AI Scalability",
        "ai-observability": "AI Observability",
        "production-ai-system": "Production AI System",
        "production-down": "Production Outage Response",
        "api-slow": "API Latency Regression",
        "database-high-cpu": "PostgreSQL High CPU Incident",
        "database-deadlock": "PostgreSQL Deadlock Incident",
        "redis-down": "Redis Outage",
        "duplicate-message": "Duplicate Message Handling",
        "celery-task-duplicate": "Duplicate Celery Task",
        "memory-leak": "Python Memory Leak Incident",
        "high-traffic": "Scaling FastAPI from 1,000 to 20,000 RPS",
        "data-consistency": "Data Consistency Incident",
        "legacy-system-refactoring": "Legacy System Refactoring",
    }
    if stem in special:
        return special[stem]
    return " ".join(word.upper() if word in {"api", "aws", "sql", "orm", "cpu", "io", "ttl"} else word.capitalize() for word in stem.split("-"))


def key_for(filename: str) -> str:
    return filename.removesuffix(".md")


def insight_for(folder: str, filename: str) -> tuple[str, str, str]:
    key = key_for(filename)
    if (folder, key) in SCOPED_INSIGHTS:
        return SCOPED_INSIGHTS[(folder, key)]
    if key in INSIGHTS:
        return INSIGHTS[key]
    title = title_from_name(filename)
    c = CATEGORY[folder]
    definition_template, mechanics_template, use_case_template = FOLDER_FALLBACKS[folder]
    definition = definition_template.format(title=title)
    mechanics = mechanics_template.format(title=title)
    use_case = use_case_template.format(title=title)
    return definition, mechanics, use_case


def example_for(folder: str, filename: str, title: str) -> str:
    key = key_for(filename)
    if key == "ai-system-overview":
        return dedent('''
        ```mermaid
        flowchart LR
            User --> Gateway["API Gateway"]
            Gateway --> Backend
            Backend --> Orchestrator["LLM Orchestrator"]
            Orchestrator --> Embedding
            Embedding --> VectorDB[(Vector DB)]
            VectorDB --> Orchestrator
            Orchestrator --> LLM
            LLM --> Stream["Streaming Response"]
            Stream --> User
        ```

        Ingestion chạy riêng: parse → chunk → embed → index; online retrieval luôn filter tenant/ACL trước khi đưa evidence vào prompt.
        ''').strip()
    if key == "sync-vs-async-endpoint":
        return dedent('''
        ```python
        import time
        from fastapi import FastAPI

        app = FastAPI()

        def blocking_database_call() -> list[dict[str, int]]:
            time.sleep(2)  # Represents a synchronous driver call.
            return [{"id": 1}]

        @app.get("/users-dangerous")
        async def users_dangerous() -> list[dict[str, int]]:
            # This runs on the event-loop thread and blocks other connections.
            return blocking_database_call()

        @app.get("/users-sync")
        def users_sync() -> list[dict[str, int]]:
            # FastAPI runs a normal path operation in its external thread pool.
            return blocking_database_call()
        ```

        Production ưu tiên async database driver trong `async def`; nếu buộc dùng sync library, bound thread-pool concurrency và đo thread-token/pool wait. CPU-heavy code vẫn nên đi process/job queue.
        ''').strip()
    if key == "asyncio":
        return dedent('''
        ```python
        import asyncio

        async def call_service(name: str, delay: float) -> str:
            await asyncio.sleep(delay)  # Simulate non-blocking I/O.
            return f"{name}:ok"

        async def aggregate() -> list[str]:
            async with asyncio.TaskGroup() as group:
                tasks = [group.create_task(call_service(n, 0.05)) for n in ("vehicle", "warranty")]
            return [task.result() for task in tasks]

        if __name__ == "__main__":
            print(asyncio.run(aggregate()))
        ```
        ''').strip()
    if key in {"idempotency", "exactly-once-myth", "duplicate-message", "celery-task-duplicate"}:
        return dedent('''
        ```sql
        CREATE TABLE processed_request (
            tenant_id bigint NOT NULL,
            idempotency_key text NOT NULL,
            request_hash text NOT NULL,
            response jsonb,
            created_at timestamptz NOT NULL DEFAULT now(),
            PRIMARY KEY (tenant_id, idempotency_key)
        );
        ```

        `INSERT ... ON CONFLICT` phải nằm cùng transaction với business write; cùng key nhưng khác `request_hash` bị từ chối.
        ''').strip()
    if folder == "04-database-postgresql":
        return dedent(f'''
        ```sql
        EXPLAIN (ANALYZE, BUFFERS, WAL)
        SELECT id, status, created_at
        FROM warranty_claim
        WHERE vehicle_id = 4242 AND created_at >= now() - interval '90 days'
        ORDER BY created_at DESC
        LIMIT 50;
        ```

        Với **{title}**, đọc `actual rows`, `loops`, buffer hit/read và sort spill; thử trên dữ liệu có distribution đại diện.
        ''').strip()
    if folder in {"03-fastapi", "05-sqlalchemy"}:
        return dedent(f'''
        ```python
        from fastapi import Depends, FastAPI, HTTPException

        app = FastAPI()

        async def current_tenant() -> int:
            return 42

        @app.get("/health/{{component}}")
        async def health(component: str, tenant_id: int = Depends(current_tenant)) -> dict[str, object]:
            if component not in {{"database", "cache", "queue"}}:
                raise HTTPException(status_code=404, detail="unknown component")
            return {{"component": component, "tenant_id": tenant_id, "healthy": True}}
        ```

        Ví dụ giữ I/O path non-blocking; production cần deadline, structured log và bounded pool cho **{title}**.
        ''').strip()
    if folder in {"12-docker", "13-kubernetes", "15-terraform-cicd"}:
        return dedent(f'''
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: vehicle-api
        spec:
          replicas: 3
          selector:
            matchLabels: {{app: vehicle-api}}
          template:
            metadata:
              labels: {{app: vehicle-api}}
            spec:
              containers:
                - name: api
                  image: registry.example/vehicle-api@sha256:4f9c2f
                  resources:
                    requests: {{cpu: 500m, memory: 512Mi}}
                    limits: {{memory: 1Gi}}
        ```

        Manifest minh họa desired state liên quan **{title}**; image digest và resource policy làm rollout có thể kiểm chứng.
        ''').strip()
    if folder == "18-ai-integration":
        return dedent(f'''
        ```python
        from dataclasses import dataclass

        @dataclass(frozen=True)
        class RetrievedChunk:
            document_id: str
            text: str
            score: float

        def select_context(chunks: list[RetrievedChunk], *, min_score: float = 0.72) -> list[RetrievedChunk]:
            allowed = (chunk for chunk in chunks if chunk.score >= min_score)
            return sorted(allowed, key=lambda chunk: chunk.score, reverse=True)[:8]
        ```

        **{title}** cần thêm tenant ACL, model version, token budget, citation và quality evaluation ở production.
        ''').strip()
    if folder == "19-coding-interview":
        return dedent(f'''
        ```python
        from collections.abc import Iterable

        def first_duplicate(values: Iterable[int]) -> int | None:
            seen: set[int] = set()
            for value in values:
                if value in seen:
                    return value
                seen.add(value)
            return None
        ```

        Nêu invariant, chứng minh termination/correctness, rồi phân tích time `O(n)` và space `O(n)` khi trao đổi về **{title}**.
        ''').strip()
    if folder == "21-behavioral":
        return dedent(f'''
        ```text
        Situation: Warranty API p99 tăng 8 lần trong giờ cao điểm.
        Task: Khôi phục SLO và điều phối ba team phụ thuộc.
        Action: Giảm impact, dùng trace khoanh vùng pool wait, thống nhất owner và rollout fix theo canary.
        Result: p99 về baseline, bổ sung alert burn-rate và capacity test trước campaign.
        Learning: Nói rõ decision, trade-off và điều sẽ làm khác đi liên quan {title}.
        ```
        ''').strip()
    return dedent(f'''
    ```python
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Decision:
        topic: str
        invariant: str
        metric: str

    decision = Decision(
        topic={title!r},
        invariant="Không làm mất hoặc lặp business effect",
        metric="p99 latency và error rate",
    )
    ```

    Ví dụ biến quyết định về **{title}** thành invariant và tín hiệu vận hành có thể kiểm chứng.
    ''').strip()


SPECIAL_SCENARIOS: dict[str, list[str]] = {
    "gil": [
        "A CPU-heavy endpoint slows unrelated requests although host CPU is only 25%. How can the GIL and worker topology explain this?",
        "A C extension makes threaded code 6× faster. What must be true about its GIL behavior, and how do you verify safety?",
        "You move work to a process pool and latency gets worse. Which serialization, startup, queueing, and memory metrics do you inspect?",
        "A compound dictionary update loses correctness across threads. Why did the GIL not protect the invariant?",
        "Your Python runtime is upgraded to a free-threaded build. Which assumptions, extensions, and race tests must be revisited?",
    ],
    "asyncio": [
        "Event-loop lag jumps to 800 ms after a release while total CPU stays normal. How do you isolate the blocking call?",
        "One request fans out to 1,000 downstream calls. Design bounded concurrency, deadline propagation, and cancellation.",
        "A client disconnects during LLM streaming but provider usage continues. Where should cancellation be handled?",
        "Ten sibling tasks run concurrently and one fails. Compare gather behavior with structured concurrency.",
        "An async service leaks tasks during shutdown. How do you drain work without hanging deployment?",
    ],
    "index": [
        "A 500M-row table serves latest claims by vehicle. Propose and validate a composite/covering index.",
        "A new index improves reads but doubles write latency and WAL. What evidence drives keep/drop/redesign?",
        "Planner chooses a sequential scan although an index exists. Which selectivity/statistics/type issues do you check?",
        "A partial index is never selected because the query parameter hides predicate implication. How do you fix it?",
        "A zero-downtime index build blocks production writes. What happened and what recovery path is safe?",
    ],
    "mvcc": [
        "A long-running report causes table bloat and replica lag. Explain the MVCC chain and mitigation.",
        "Autovacuum runs constantly but dead tuples grow. Which thresholds, transaction age, and workload metrics matter?",
        "Two users update the same logical record and one change disappears. Which control prevents the lost update?",
        "A read replica returns stale status after a write. Separate MVCC snapshot behavior from replication lag.",
        "Transaction ID age approaches wraparound. What do you do immediately and permanently?",
    ],
    "connection-pooling": [
        "Scaling from 20 to 200 pods requests 4,000 DB connections. Build a safe global connection budget.",
        "Pool wait rises while query duration is flat. What does this reveal, and what should you not do blindly?",
        "PgBouncer transaction mode breaks session-level assumptions. Which features and code paths do you audit?",
        "One tenant monopolizes the pool. Design admission control and isolation.",
        "During failover every pod reconnects simultaneously. How do you prevent a connection storm?",
    ],
    "idempotency": [
        "Two create requests with the same key arrive concurrently. Show the atomic claim and response behavior.",
        "The same idempotency key is reused with a different payload. What should the server return and store?",
        "The database commits but the client times out before receiving the response. What happens on retry?",
        "The external payment/email provider lacks idempotency support. How do you reduce duplicate effects?",
        "A deduplication record expires before a delayed retry arrives. How do you choose retention and reconcile?",
    ],
    "retry": [
        "10,000 requests fail and each client retries three times immediately. Quantify amplification and stabilize the system.",
        "A non-idempotent operation times out after the server may have committed. Should the client retry?",
        "A downstream returns mixed 429, 503, and validation errors. Define retry classification and budgets.",
        "Retries improve success rate but worsen p99 beyond the caller deadline. Redesign the attempt budget.",
        "All instances retry on the same schedule after recovery. Which jitter strategy avoids synchronization?",
    ],
    "distributed-lock": [
        "A worker pauses beyond lease expiry, resumes, and overwrites a newer result. Show how fencing prevents it.",
        "Redis lock service becomes partitioned. Which safety/liveness guarantee can you actually claim?",
        "Two lock acquisitions appear successful during failover. Can a database constraint protect the invariant better?",
        "Lock renewal traffic overloads the coordinator. Redesign granularity and critical-section duration.",
        "A process crashes while holding a lock. Explain lease, owner token, cleanup, and reconciliation.",
    ],
    "rag": [
        "Answers are fluent but cite irrelevant chunks. How do you separate retrieval quality from generation quality?",
        "A document contains prompt injection asking the model to expose other tenants. Where are the trust boundaries?",
        "Changing embedding models reduces recall for Vietnamese automotive terms. Design versioned migration and evaluation.",
        "Context exceeds the model window. Choose chunking, reranking, compression, and abstention behavior.",
        "Vector search is healthy but time-to-first-token doubles. How do traces and token budgets localize the issue?",
    ],
    "redis-down": [
        "Redis is fully unavailable. Sequence circuit breaking, stale fallback, DB protection, and recovery.",
        "All cache keys expire after a deployment. Prevent the resulting miss storm.",
        "Failover succeeds but clients keep using stale topology. Which timeout/reconnect behavior matters?",
        "Rate limiting depends on Redis. Choose fail-open versus fail-closed for login and read-only catalog traffic.",
        "Redis returns with an empty cache. Build a warm-up plan that does not overload PostgreSQL.",
    ],
    "celery-task-duplicate": [
        "A worker completes a task then crashes before ack. Trace the redelivery and safe business behavior.",
        "A task sends email then retries after timeout. How do provider idempotency and a delivery ledger help?",
        "A Redis lock expires during a long task. Why is the lock insufficient, and which DB constraint is authoritative?",
        "A poison task retries forever and blocks useful work. Design retry classification and quarantine.",
        "A deploy terminates workers mid-task. Explain graceful drain, visibility timeout, and reconciliation.",
    ],
}


def question_sections(
    folder: str,
    filename: str,
    title: str,
    definition: str | None = None,
) -> tuple[str, str, str, str]:
    c = CATEGORY[folder]
    basic_stems = [
        f"What is {title}, and which concrete problem does it address?",
        f"Explain the main internal mechanism behind {title}.",
        f"Which guarantees does {title} provide, and which does it not provide?",
        f"Which metrics or observations reveal the behavior of {title}?",
        f"What is the most common misconception about {title}?",
        f"How would you test assumptions involving {title}?",
        f"Which edge cases or failure modes matter most for {title}?",
        f"How can {title} affect latency, throughput, memory, or correctness?",
        f"Which runtime conditions or configuration choices change the behavior of {title}?",
        f"When is a different or simpler approach better than relying on {title}?",
    ]
    senior_stems = [
        f"How does {title} constrain the surrounding architecture and operational model?",
        f"Which subtle correctness issue appears when {title} meets concurrency or partial failure?",
        f"What breaks first around {title} at 20,000 RPS or 100× data volume?",
        f"Where should admission control or backpressure be placed when using {title}?",
        f"How would you benchmark or validate {title} without a misleading microbenchmark?",
        f"Which hidden coupling or migration cost can {title} introduce?",
        f"How would you change a poor decision around {title} with no downtime?",
        f"What production evidence would make you choose a different approach?",
        f"How do correctness, latency, cost, and complexity trade off for {title}?",
        f"How would you turn an incident involving {title} into a durable prevention mechanism?",
    ]
    scenarios = SPECIAL_SCENARIOS.get(key_for(filename), [
        f"A release involving {title} triples p99 while averages look normal. How do you investigate and mitigate?",
        f"A critical dependency around {title} is unavailable for ten minutes. Define degraded behavior and recovery.",
        f"Two concurrent operations expose a correctness gap related to {title}. Which invariant and atomic boundary fix it?",
        f"Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving {title} fails first?",
        f"A canary changes the behavior of {title}; success rate is flat but saturation rises. Promote or roll back?",
    ])
    followups = [
        "What assumption in your answer is most risky?",
        "How would you prove that with metrics or an experiment?",
        "What changes if the operation is not idempotent?",
        "Where would you add timeout, retry, and backpressure?",
        "What is your rollback and data-reconciliation plan?",
    ]
    basics_md = "\n".join(f"- **B{i}.** {q}" for i, q in enumerate(basic_stems, 1))
    scenarios_md = "\n".join(f"- **S{i}.** {q}" for i, q in enumerate(scenarios, 1))
    seniors_md = "\n".join(f"- **L{i}.** {q}" for i, q in enumerate(senior_stems, 1))
    follow_md = "\n".join(f"- **F{i}.** {q}" for i, q in enumerate(followups, 1))
    answers = [
        f"**B1.** {definition or (title + ' thuộc ' + c['scope'])} Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.",
        f"**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của {title}.",
        f"**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.",
        f"**B4.** Đo {c['metric']}; luôn tách average khỏi tail và success khỏi useful result.",
        f"**B5.** Lỗi phổ biến là dùng {title} như mặc định mà không xác định ownership, limit và fallback.",
        "**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.",
        "**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.",
        "**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.",
        "**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.",
        f"**B10.** Tránh {title} khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.",
    ]
    return f"### Basic / Mid-level (10)\n\n{basics_md}\n\n### Production Scenarios (5)\n\n{scenarios_md}", seniors_md, "\n\n".join(answers), follow_md


DEEP_DIVE_FOLDERS = {
    "01-python-core", "02-python-concurrency", "03-fastapi",
    "04-database-postgresql", "05-sqlalchemy", "06-redis", "07-celery",
    "08-api-design", "10-distributed-systems", "11-system-design",
    "13-kubernetes", "16-security", "17-performance-reliability",
    "18-ai-integration", "20-senior-scenarios",
}


MENTAL_MODELS: dict[str, str] = {
    "python-memory-model": "Variable không phải chiếc hộp chứa value. Variable là nhãn trỏ tới object; nhiều nhãn có thể trỏ cùng object, nên mutation nhìn thấy qua mọi alias.",
    "gc-reference-counting": "Reference counting dọn object ngay khi không còn owner; cyclic GC là đội thu gom chuyên tìm các nhóm object chỉ còn trỏ lẫn nhau.",
    "mutable-immutable": "Mutability là khả năng object giữ nguyên identity nhưng đổi observable state; rebinding một name không phải mutation.",
    "gil": "GIL là vé vào vùng thực thi Python object/bytecode của một interpreter build có GIL. Thread chờ I/O trả vé; thread chạy Python CPU liên tục tranh cùng một vé.",
    "asyncio": "Event loop không làm nhiều việc cùng lúc. Nó chạy coroutine đang sẵn sàng cho tới khi coroutine tự nhường tại `await`, rồi chuyển sang việc khác.",
    "event-loop": "Event loop là dispatcher giữa ready queue, timer và OS I/O readiness; nó hiệu quả khi callback ngắn và không block.",
    "coroutine-task-future": "Coroutine là recipe có thể suspend; Task là coroutine đã được schedule; Future là ô đại diện kết quả sẽ có sau này.",
    "threading": "Thread chia sẻ heap/process nhưng có call stack riêng; chia sẻ giúp giao tiếp rẻ và cũng tạo race/lock risk.",
    "multiprocessing": "Process đổi shared-memory convenience lấy isolation và multi-core parallelism; dữ liệu qua boundary phải serialize/copy hoặc dùng shared memory có synchronization.",
    "request-lifecycle": "Mỗi request là một scope có deadline và resource ownership: tạo context, thực hiện work, trả response, rồi cleanup kể cả khi exception/cancel.",
    "sync-vs-async-endpoint": "`async def` không tự làm code non-blocking. Chỉ những operation thật sự `await` non-blocking I/O mới nhường event loop.",
    "index": "Index là bản đồ đã sắp xếp từ search key đến vị trí tuple; đọc ít page hơn nhưng mọi write phải duy trì thêm bản đồ.",
    "btree-hash-gin-gist-brin": "Index type là cách tổ chức key/page và operator class. Chọn theo phép toán và distribution, không theo tên datatype.",
    "explain-analyze": "Execution plan là cây operator; dữ liệu chảy từ node con lên node cha. `ANALYZE` thay dự đoán bằng số đo nhưng cũng thực thi query.",
    "mvcc": "UPDATE không sửa tuple tại chỗ theo nghĩa logic; nó tạo version mới. Snapshot quyết định transaction nhìn thấy version nào.",
    "transaction": "Transaction là ranh giới all-or-nothing và isolation cho invariant, không phải wrapper càng rộng càng an toàn.",
    "connection-pooling": "Pool là hàng rào admission vào database. Request vượt số connection sẽ xếp hàng; tăng pool chỉ chuyển queue từ app vào database.",
    "redis-internals": "Redis nhanh nhờ RAM, data structure chuyên dụng và phần lớn command execution được serialize; vì thế một command O(N) lớn có thể giữ cả làn đường.",
    "caching": "Cache là derived state có thể mất và rebuild. Nếu không chỉ ra source of truth và stale policy, cache đã trở thành database thứ hai ngoài ý muốn.",
    "task-lifecycle": "Queue giao message; worker tạo business effect. ACK chỉ nói về delivery, không chứng minh effect xảy ra đúng một lần.",
    "exactly-once-myth": "Exactly-once phải hỏi: một lần ở đâu—broker delivery, database transition hay external effect? Mỗi boundary có failure window khác nhau.",
    "idempotency": "Idempotency biến retry từ một request mới thành việc quan sát lại cùng một logical operation.",
    "retry": "Retry là thêm traffic vào dependency đang lỗi; nó chỉ hữu ích khi lỗi transient, operation an toàn và còn deadline/retry budget.",
    "timeout": "Timeout là ngân sách chờ, không phải thời gian dependency chắc chắn dừng. Cancellation phải propagate và cleanup resource.",
    "circuit-breaker": "Circuit breaker là state machine ngăn request mới tiếp tục đập vào dependency đang suy yếu, đồng thời cho phép probe hồi phục có kiểm soát.",
    "outbox-pattern": "Outbox đưa business write và ý định publish vào cùng một local transaction; relay có thể publish lặp nhưng không làm mất ý định.",
    "saga": "Saga chia distributed transaction thành local transaction và compensation; compensation là business action mới, không phải time travel rollback.",
    "rag": "RAG là search system đứng trước generation system. Nếu retrieval không lấy đúng evidence, prompt hay hơn cũng không cứu được groundedness.",
}


INTERNAL_DEEP_DIVES: dict[tuple[str, str], str] = {
    ("01-python-core", "python-memory-model"): dedent('''
        Trong CPython build có GIL, mọi object bắt đầu bằng header tương đương `PyObject`: reference count và pointer tới `PyTypeObject`; variable-size object có thêm length. `id(obj)` là identity duy nhất trong lifetime của object; trên CPython thường liên quan địa chỉ memory nhưng language specification không bắt implementation khác phải như vậy.

        Assignment chỉ tăng ownership/reference phù hợp và bind name. Container giữ reference tới phần tử; function frame giữ local reference; closure cell và global/cache có thể kéo dài lifetime. Immutable không có nghĩa object “nằm trên stack”; nghĩa là state quan sát được không đổi, operation trả object khác (dù runtime có thể intern/reuse một số object).
    '''),
    ("01-python-core", "gc-reference-counting"): dedent('''
        Refcount tăng khi reference mới được giữ bởi name/container/frame và giảm khi reference bị overwrite, container bỏ phần tử hoặc frame kết thúc. `del x` xóa binding `x`; nó không ra lệnh free object. Khi refcount về 0, CPython thường deallocate ngay và cascading decrement các child reference.

        Cycle `a → b → a` không bao giờ tự về 0, nên cyclic GC theo dõi container object. Object mới vào generation trẻ; object sống qua collection được promote. Exact generation policy/threshold thay đổi theo Python version—đặc biệt free-threaded builds—nên dùng `gc.get_stats()`/official docs thay vì thuộc con số implementation. External resource vẫn cần `with`/`finally` vì GC timing không phải contract.
    '''),
    ("02-python-concurrency", "gil"): dedent('''
        GIL thuộc CPython implementation, không phải quy tắc của ngôn ngữ Python. Ở build mặc định có GIL, thread phải giữ GIL và attached thread state để thao tác Python object/C API. Thiết kế lịch sử đơn giản hóa bảo vệ runtime state và reference count, nhưng GIL không thay thế lock cho business invariant gồm nhiều bước.

        Interpreter định kỳ cho thread khác cơ hội chạy; blocking I/O và nhiều native extension detach thread state/release GIL. Vì vậy thread vẫn hữu ích cho nhiều blocking I/O. Với CPU-bound pure Python, nhiều thread chủ yếu time-slice một core cho bytecode; process/native code thường phù hợp hơn. Từ CPython 3.13 có free-threaded build tùy chọn: built-in có internal synchronization, extension phải khai báo tương thích và shared mutable state vẫn cần lock.
    '''),
    ("02-python-concurrency", "asyncio"): dedent('''
        Gọi `async def` tạo coroutine object; code chưa chạy cho đến khi `await` hoặc schedule thành Task. Task gọi coroutine `.send()` cho tới khi coroutine return, raise hoặc yield một awaitable chưa hoàn tất. Event loop đăng callback để resume Task khi Future hoàn thành.

        Với socket non-blocking, read chưa có data trả trạng thái “would block”; loop đăng file descriptor với selector (`epoll`, `kqueue` hoặc cơ chế tương ứng). OS báo readiness, loop đưa callback vào ready queue. `await` không sinh thread và không nhất thiết yield nếu awaitable đã hoàn tất. CPU loop không có `await` giữ event-loop thread, làm timer, socket và cancellation khác bị trễ.
    '''),
    ("02-python-concurrency", "event-loop"): dedent('''
        Một iteration thường: chạy ready callbacks có budget → xử lý timer đến hạn → poll selector tới timeout gần nhất → chuyển I/O event thành callback ready. Implementation cụ thể phụ thuộc loop/platform (SelectorEventLoop, Proactor trên Windows, uvloop), nhưng contract cooperative scheduling giữ nguyên.

        `call_soon`/Task continuation vào ready queue; `call_later` vào timer structure; selector theo dõi file descriptor. Loop lag là chênh lệch giữa lúc callback dự kiến và thực sự chạy. Lag cao cùng CPU một core cao thường là blocking/CPU callback; lag cao cùng thread-pool queue có thể do sync dependency saturation.
    '''),
    ("03-fastapi", "request-lifecycle"): dedent('''
        ASGI server tạo `scope` mô tả HTTP/WebSocket connection và gọi application với `receive`/`send` async callable. Uvicorn sở hữu socket/event loop/protocol; FastAPI/Starlette sở hữu middleware, routing và application behavior. Gunicorn có thể làm process manager cho nhiều worker, nhưng Uvicorn cũng hỗ trợ nhiều process; deployment choice phụ thuộc platform và graceful lifecycle.

        FastAPI match route, resolve dependency graph (sync dependency có thể vào thread pool), validate input qua Pydantic rồi gọi endpoint. Response serialization và middleware unwind xảy ra trước/đồng thời cleanup tùy dependency scope/version; không dựa vào thứ tự mơ hồ cho transaction correctness. Mỗi worker có event loop/pool riêng, nên tổng DB connection = replicas × workers × pool configuration.
    '''),
    ("03-fastapi", "sync-vs-async-endpoint"): dedent('''
        FastAPI chạy path operation `def` trong external thread pool và `async def` trực tiếp trên event loop. Nhưng utility `def` do bạn gọi bên trong `async def` chạy ngay trên loop—framework không tự offload. Vì vậy `requests.get()`, sync DB driver hoặc CPU parse lớn trong async endpoint có thể chặn mọi connection cùng loop.

        Thread pool cũng là bounded resource: nếu mọi sync endpoint chờ DB/network, queue của pool tăng và p99 xấu. Chọn async khi dependency stack có async driver; chọn sync/thread khi library chỉ blocking và concurrency đã bound; CPU-heavy chuyển process/job queue. Đo loop lag, thread tokens, pool wait và cancellation behavior.
    '''),
    ("04-database-postgresql", "database-fundamentals"): dedent('''
        PostgreSQL nhận SQL rồi parse thành syntax tree, analyze/resolve name và type, rewrite rule/view, planner tạo nhiều path và chọn plan có estimated cost, executor kéo tuple qua cây operator. Buffer manager ánh xạ page từ relation vào shared buffers; WAL ghi change trước data page để crash recovery.

        Cost không phải millisecond. Planner dựa statistics về row count, distinct, histogram, most-common values và correlation. Sai estimate ở node thấp khuếch đại lên join/order. Executor có thể đọc cache hoặc disk, spill sort/hash ra temp và chờ lock/I/O; vì vậy phải đọc actual rows, loops, buffers, temp và wait event cùng nhau.
    '''),
    ("04-database-postgresql", "index"): dedent('''
        PostgreSQL B-tree gồm page root/internal/leaf. Leaf giữ index tuple với key và TID trỏ heap tuple (trừ khi index-only scan có visibility map đủ dùng). Split page, random insert và deleted entry tạo write amplification/bloat; VACUUM/index maintenance và fillfactor có thể ảnh hưởng workload.

        Composite index sắp lexicographic; leftmost equality rồi range/order thường quyết định phần hữu dụng. INCLUDE không tham gia search order mà giúp covering. Partial index chỉ dùng khi planner chứng minh query predicate hàm ý index predicate. Index scan vẫn có thể tệ khi selectivity thấp/random heap fetch nhiều; bitmap scan gom TID để đọc heap page hiệu quả hơn.
    '''),
    ("04-database-postgresql", "mvcc"): dedent('''
        Heap tuple mang transaction metadata như `xmin` (creator) và `xmax` (deleter/updater). Snapshot chứa visibility horizon để quyết định version nào visible; transaction khác có thể thấy old tuple trong khi writer đã tạo new tuple. UPDATE thường tạo tuple mới, HOT update có thể tránh index update khi indexed column không đổi và còn chỗ trên page.

        Dead tuple chỉ reclaim khi không snapshot nào còn cần. Long transaction/idle-in-transaction giữ horizon cũ, làm VACUUM không dọn được, tăng table/index bloat và transaction-ID risk. Visibility map cho biết page all-visible để index-only scan tránh heap lookup; VACUUM và write có thể thay đổi bit này.
    '''),
    ("04-database-postgresql", "explain-analyze"): dedent('''
        Đọc plan từ node sâu nhất nơi actual/estimate lệch mạnh hoặc time/buffer tăng, rồi đi lên. `actual time=a..b rows=n loops=m`: thời gian/rows thường per-loop; tổng work liên quan loops. `Rows Removed by Filter`, heap fetches, sort method/memory/disk, hash batches và temp blocks chỉ ra waste/spill.

        `BUFFERS` tách shared hit/read/dirtied/written và temp; hit không có nghĩa miễn phí vì vẫn tốn CPU. `EXPLAIN ANALYZE` thực thi query: với DML dùng transaction rồi rollback khi phù hợp và tránh production query nguy hiểm. Generic/prepared plan, cache warmth, concurrency và realistic data distribution có thể làm test đơn lẻ sai lệch.
    '''),
    ("04-database-postgresql", "transaction"): dedent('''
        `BEGIN` mở transaction; statement tạo command ID và dùng snapshot theo isolation. Change đi vào buffer/WAL; `COMMIT` làm transaction durable theo WAL flush policy, còn data page có thể được checkpoint sau. Rollback đánh dấu transaction aborted; tuple version không visible và VACUUM dọn sau, không “undo bytes” ngay.

        Transaction càng dài càng giữ lock/snapshot/connection lâu. Remote call bên trong transaction tăng contention và ambiguity. Thiết kế transaction quanh invariant local; distributed workflow dùng state machine/outbox/idempotency thay vì giữ DB transaction qua network.
    '''),
    ("04-database-postgresql", "isolation-level"): dedent('''
        Read Committed lấy snapshot mới mỗi statement, nên hai SELECT trong cùng transaction có thể thấy khác nhau. PostgreSQL Repeatable Read dùng transaction snapshot và ngăn nhiều anomaly nhưng concurrent write vẫn có serialization-style abort. Serializable dùng SSI theo dõi dependency nguy hiểm và có thể abort dù không lock mọi read.

        Isolation level không tự bảo vệ mọi business invariant nếu read/write pattern không nằm trong cùng transaction hoặc predicate không được theo dõi như kỳ vọng. Luôn mô tả anomaly cần ngăn: lost update, write skew, duplicate allocation; dùng atomic SQL, row lock, unique constraint, optimistic version hoặc Serializable + retry whole transaction.
    '''),
    ("06-redis", "redis-internals"): dedent('''
        Client gửi RESP qua socket; event loop đọc request, parse command, thực thi trên data structure rồi ghi response. Redis hiện đại có thể dùng I/O thread cho network read/write tùy version/config, nhưng phần lớn command logic vẫn serialized trên main execution path. Điều này giảm lock contention nhưng O(N), big key, Lua/function dài hoặc fork pressure có thể làm tail latency của client khác tăng.

        Key trỏ object có encoding tối ưu theo size/type; memory footprint gồm allocator fragmentation và replication/AOF buffers. Expiry vừa passive khi access vừa active sampling. Eviction chạy khi vượt `maxmemory` theo policy. RDB fork snapshot và AOF append/rewrite có durability/latency trade-off; replication async tạo acknowledged-write loss window khi failover.
    '''),
    ("06-redis", "sentinel-cluster"): dedent('''
        Sentinel giám sát primary/replica, đạt quorum/majority cho failover coordination và quảng bá primary mới; nó không shard data. Redis Cluster chia keyspace thành 16,384 hash slot, mỗi master sở hữu range slot và có replica. Client nhận `MOVED`/`ASK` để cập nhật topology; multi-key operation cần key cùng slot (hash tag).

        Failover và reshard không loại hot key: một key vẫn thuộc một shard. Replication async nghĩa là promotion có thể thiếu write mới nhất. Client retry sau redirect/timeout phải xét idempotency. Cluster tăng capacity nhưng tăng topology, backup/restore, cross-slot và failure-mode complexity.
    '''),
    ("07-celery", "architecture"): dedent('''
        Producer serialize task name/args/headers rồi publish broker exchange/queue. Worker consumer reserve message, pool child thực thi task; acknowledgement timing phụ thuộc `acks_late` và broker/transport. Result backend là optional observation store, không nên là authoritative business state.

        Prefetch tạo local reserved work: cao giúp throughput task ngắn nhưng làm fairness kém cho task dài. Redis transport visibility timeout và AMQP unacked semantics khác nhau, nên nói rõ broker. Worker crash trước ack tạo redelivery; crash sau early ack có thể mất work. Business table/job state phải chịu duplicate và reconciliation.
    '''),
    ("07-celery", "task-lifecycle"): dedent('''
        State logic cần tách broker state với domain state. `PENDING` từ result backend thậm chí có thể nghĩa “không biết task”, không chắc message đang queue. Domain job nên có version/attempt/lease và atomic transition; task nhận immutable job ID thay vì payload lớn hoặc ORM object.

        Với late ACK: worker commit DB rồi crash trước ACK → broker redeliver. Với early ACK: worker crash sau ACK trước commit → effect mất. Visibility/consumer timeout nhỏ hơn runtime có thể redeliver song song. Giải pháp thực dụng là at-least-once, idempotent transition, unique constraint/inbox, heartbeat phù hợp và reconciliation.
    '''),
    ("10-distributed-systems", "outbox-pattern"): dedent('''
        Dual write trực tiếp có hai cửa sổ: DB commit rồi publish fail làm mất event; publish thành công rồi DB rollback tạo event ma. Không có thứ tự gọi nào loại cả hai nếu DB và broker không chung atomic transaction.

        Outbox insert nằm cùng transaction với business row. Relay poll bằng `FOR UPDATE SKIP LOCKED` hoặc CDC, publish rồi đánh dấu; crash quanh publish/mark có thể publish lặp nên consumer vẫn dedupe. Theo dõi oldest-unpublished age, attempt/error, retention và reconciliation giữa aggregate version với event.
    '''),
    ("10-distributed-systems", "circuit-breaker"): dedent('''
        Closed cho request đi qua và ghi nhận outcome; vượt threshold mở circuit để fail fast/fallback. Sau cooldown, Half-Open chỉ cho ít probe; success đủ thì đóng, failure mở lại. Rolling window, slow-call threshold và minimum sample tránh phản ứng với noise.

        Circuit breaker không thay timeout, rate limit hoặc bulkhead. Một breaker global có thể để tenant/endpoint lỗi chặn mọi traffic; đặt scope theo dependency/failure domain. Fallback phải có data-age/quality semantics và không tạo load lớn hơn lên dependency khác.
    '''),
    ("10-distributed-systems", "saga"): dedent('''
        Choreography để service phản ứng event, coupling runtime thấp nhưng flow khó nhìn và cycle khó kiểm soát. Orchestration có coordinator/state rõ, dễ timeout/retry/observe hơn nhưng coordinator thành critical component.

        Mỗi local step commit riêng; compensation như refund/release inventory cũng có thể fail và phải idempotent/retry/reconcile. Có point of no return và irreversible action; đôi khi cần forward recovery/human review thay vì compensation. Saga không cung cấp isolation: concurrent saga có thể thấy intermediate state.
    '''),
    ("18-ai-integration", "rag"): dedent('''
        Ingestion phải version parse/chunk/embedding/index và giữ lineage từ chunk về document/page/ACL. Query path normalize/rewrite khi cần, hybrid retrieve candidate, metadata/ACL filter, rerank, pack context theo token budget rồi generate với citation/abstention.

        Đánh giá retrieval bằng recall@k/MRR trên labeled queries; đánh giá answer bằng groundedness/citation correctness/task success. ANN similarity không bảo đảm fact. Document là untrusted input: prompt injection phải bị cô lập bằng instruction hierarchy, allowlisted tool, ACL enforcement ngoài model và output validation.
    '''),
}


FOLDER_INTERNALS: dict[str, str] = {
    "01-python-core": "Phân biệt Python language contract với CPython implementation. Theo dõi identity, type, reference/descriptor lookup, frame/closure và lifetime; dùng `dis`, `sys`, `gc`, `tracemalloc` để kiểm chứng thay vì suy đoán từ syntax.",
    "02-python-concurrency": "Xác định ai schedule work (OS hay event loop), unit nào có stack/heap riêng, điểm preemption/yield, memory nào được chia sẻ và exception/cancellation đi đâu. Bound concurrency trước khi tối ưu throughput.",
    "03-fastapi": "Theo dõi request qua socket → ASGI scope/receive/send → middleware/router/dependency/validation → endpoint → serialization/cleanup. Tính tổng worker, thread token và connection pool trên toàn replica.",
    "04-database-postgresql": "Reason đồng thời ở logical SQL, planner/executor tree, heap/index page, buffer/WAL và MVCC/lock. Một query nhanh đơn lẻ có thể chậm dưới concurrency vì pool, cache, I/O và lock wait.",
    "05-sqlalchemy": "Luôn ánh xạ abstraction ORM về SQL, transaction và connection thật. Session là identity map/unit-of-work, không phải global cache; flush khác commit và loading strategy quyết định query/row amplification.",
    "06-redis": "Xem mỗi command theo time complexity, bytes/key, main execution path, TTL/eviction và durability/failover. Cache/lock/rate-limit có correctness khác nhau khi key mất hoặc replica được promote.",
    "07-celery": "Tách producer publish, broker delivery, worker reservation/execution/ACK và business state. Mỗi boundary có crash window; đo oldest age và business completion, không chỉ queue length.",
    "08-api-design": "API là distributed contract: method/status/schema chỉ là bề mặt; idempotency, concurrency control, pagination stability, deadline và compatibility quyết định behavior khi retry/evolution.",
    "10-distributed-systems": "Assume message có thể delay/drop/duplicate/reorder và node có thể pause/restart. Đặt identity, deadline, atomic boundary, durable state và reconciliation trước khi chọn middleware.",
    "11-system-design": "Bắt đầu từ workload model và invariant. Vẽ read/write critical path, source of truth và asynchronous projection; sau đó mới thêm cache/queue/shard theo bottleneck đã định lượng.",
    "13-kubernetes": "Kubernetes controller reconcile desired state, nhưng application vẫn sở hữu readiness, graceful shutdown, state correctness và downstream capacity. Pod restart không sửa logical corruption.",
    "16-security": "Bắt đầu từ asset, actor và trust boundary; authentication không thay authorization. Enforce server-side, least privilege và audit, đồng thời thiết kế key/secret rotation và incident containment.",
    "17-performance-reliability": "Latency là tổng service time + queueing. Dùng SLI/baseline, trace critical path và saturation để phân biệt symptom với bottleneck; thay đổi một biến và so before/after.",
    "18-ai-integration": "Model là dependency xác suất có quota, token cost và quality drift. Version data/model/prompt, đo system + quality, enforce ACL ngoài model và luôn có abstention/fallback.",
    "20-senior-scenarios": "Trong incident: stabilize trước, giữ evidence, dùng telemetry để kiểm hypothesis, rồi mới root cause. Mọi action cần owner, blast radius, rollback và verification.",
}


def mermaid_block(body: str) -> str:
    return f"```mermaid\n{dedent(body).strip()}\n```"


def concept_diagram(folder: str, filename: str, title: str) -> str:
    key = key_for(filename)
    special: dict[str, str] = {
        "python-memory-model": '''
            flowchart TD
                Name["Python name / variable"] -->|holds| Ref["Reference"]
                Ref --> Obj["Python object"]
                Obj --> Header["Identity + type + refcount"]
                Obj --> Value["Value / payload"]
                Alias["Another name"] -->|same object| Ref
        ''',
        "gc-reference-counting": '''
            flowchart TD
                Create["Object created"] --> Gen0["Young generation"]
                Gen0 -->|unreachable| Collect["Collect cycle"]
                Gen0 -->|survives| Older["Older generation"]
                Older -->|survives repeatedly| Oldest["Old generation"]
                RefZero["Reference count becomes 0"] --> Immediate["Immediate deallocation in CPython"]
                Cycle["Cycle keeps refcount above 0"] --> Gen0
        ''',
        "gil": '''
            flowchart TD
                T1["Thread A"] --> Gate{"GIL available?"}
                T2["Thread B"] --> Gate
                T3["Thread C"] --> Gate
                Gate -->|acquired| VM["CPython bytecode / object access"]
                VM -->|blocking I/O releases GIL| IO["Kernel waits for network / disk"]
                IO -->|I/O ready| Gate
                VM -->|switch opportunity| Gate
        ''',
        "asyncio": '''
            flowchart TD
                Loop["Event loop"] --> Ready["Ready queue"]
                Ready --> A["Coroutine A"]
                A -->|await socket| Waiting["Waiting I/O"]
                Ready --> B["Coroutine B"]
                B -->|await database| Waiting
                Waiting --> OS["epoll / kqueue / IOCP"]
                OS -->|file descriptor ready| Loop
        ''',
        "event-loop": '''
            flowchart LR
                Timers["Due timers"] --> Ready["Ready callbacks"]
                Selector["OS selector events"] --> Ready
                Threadsafe["Thread-safe notifications"] --> Ready
                Ready --> Run["Run callback / Task step"]
                Run -->|await incomplete Future| Selector
                Run -->|complete| Result["Result / next callback"]
        ''',
        "coroutine-task-future": '''
            stateDiagram-v2
                [*] --> CoroutineCreated
                CoroutineCreated --> Scheduled: create_task
                Scheduled --> Running
                Running --> Waiting: await Future
                Waiting --> Scheduled: Future done
                Running --> Completed: return
                Running --> Failed: exception
                Waiting --> Cancelled: cancel
        ''',
        "request-lifecycle": '''
            flowchart LR
                Client --> LB["Load balancer"]
                LB --> Uvicorn
                Uvicorn --> ASGI
                ASGI --> Middleware
                Middleware --> Router
                Router --> DI["Dependency graph"]
                DI --> Validation["Pydantic validation"]
                Validation --> Endpoint
                Endpoint --> Service
                Service --> Repository
                Repository --> DB[(PostgreSQL)]
        ''',
        "sync-vs-async-endpoint": '''
            sequenceDiagram
                participant C as Client
                participant L as Event Loop
                participant E as async endpoint
                participant B as Blocking library
                C->>L: HTTP request
                L->>E: run coroutine
                E->>B: synchronous call
                Note over L,B: Event-loop thread is blocked
                B-->>E: result after 2 seconds
                E-->>C: response
        ''',
        "database-fundamentals": '''
            flowchart LR
                Client --> Parser
                Parser --> Analyzer["Analyzer / Rewriter"]
                Analyzer --> Planner
                Planner --> Executor
                Executor --> Buffer["Buffer manager"]
                Buffer --> Storage["Heap / Index pages"]
                Executor --> WAL["WAL for changes"]
        ''',
        "index": '''
            flowchart TD
                Root["Root page"] --> I1["Internal page A"]
                Root --> I2["Internal page B"]
                I1 --> L1["Leaf page: keys + TIDs"]
                I1 --> L2["Leaf page: keys + TIDs"]
                I2 --> L3["Leaf page: keys + TIDs"]
                I2 --> L4["Leaf page: keys + TIDs"]
                L2 --> Heap["Heap tuple via TID"]
        ''',
        "btree-hash-gin-gist-brin": '''
            flowchart TD
                Predicate["Query predicate / operator"] --> Choice{"Access pattern"}
                Choice -->|equality / range / order| BTree
                Choice -->|array / JSONB / text membership| GIN
                Choice -->|range / geometry / nearest| GiST
                Choice -->|huge physically correlated table| BRIN
                Choice -->|equality only, niche| Hash
        ''',
        "explain-analyze": '''
            flowchart BT
                Scan["Seq / Index / Bitmap scan"] --> Join["Nested Loop / Hash / Merge"]
                Join --> Sort["Sort / Aggregate"]
                Sort --> Limit["Limit / Result"]
                Estimate["Estimated rows + cost"] -.compare.-> Actual["Actual rows + time + loops"]
                Buffers["Buffers + temp + WAL"] --> Actual
        ''',
        "mvcc": '''
            sequenceDiagram
                participant A as Transaction A
                participant H as Heap
                participant B as Transaction B snapshot
                A->>H: UPDATE creates new tuple version
                H-->>A: New version visible to A
                B->>H: SELECT using older snapshot
                H-->>B: Old tuple still visible
                Note over H: VACUUM waits until no snapshot needs old tuple
        ''',
        "transaction": '''
            stateDiagram-v2
                [*] --> Idle
                Idle --> Active: BEGIN / implicit start
                Active --> Active: statements + WAL
                Active --> Committed: COMMIT
                Active --> Aborted: error / ROLLBACK
                Aborted --> Idle: ROLLBACK complete
                Committed --> Idle
        ''',
        "redis-internals": '''
            flowchart LR
                Client --> Socket["RESP over socket"]
                Socket --> IO["Event loop / optional I/O threads"]
                IO --> Execute["Main command execution path"]
                Execute --> Structures["String / Hash / List / Set / ZSet"]
                Execute --> Expiry["TTL + eviction"]
                Execute --> Persist["AOF / RDB"]
                Execute --> Replica["Replication stream"]
        ''',
        "sentinel-cluster": '''
            flowchart LR
                Client --> R1["Master: slots 0–5460"]
                Client --> R2["Master: slots 5461–10922"]
                Client --> R3["Master: slots 10923–16383"]
                R1 --> RR1["Replica 1"]
                R2 --> RR2["Replica 2"]
                R3 --> RR3["Replica 3"]
                R2 -.MOVED redirect.-> Client
        ''',
        "celery-architecture": '''
            sequenceDiagram
                participant API
                participant Broker
                participant Worker
                participant DB
                API->>Broker: publish task
                Broker-->>Worker: deliver / reserve
                Worker->>DB: idempotent state transition
                DB-->>Worker: commit
                Worker->>Broker: ACK
        ''',
        "task-lifecycle": '''
            stateDiagram-v2
                [*] --> Published
                Published --> Reserved
                Reserved --> Running
                Running --> Succeeded
                Running --> RetryableFailure
                RetryableFailure --> Published: backoff + jitter
                Running --> DeadLetter: permanent / exhausted
                Running --> Redelivered: crash before ACK
                Redelivered --> Running
        ''',
        "exactly-once-myth": '''
            sequenceDiagram
                participant B as Broker
                participant W as Worker
                participant DB
                B->>W: deliver task
                W->>DB: commit business effect
                DB-->>W: committed
                Note over W: worker crashes before ACK
                B->>W: redelivery after lease / reconnect
                W->>DB: same effect attempted again
                DB-->>W: unique key returns prior result
        ''',
        "idempotency": '''
            sequenceDiagram
                participant C as Client
                participant API
                participant DB
                C->>API: POST + Idempotency-Key
                API->>DB: atomically claim key + request hash
                alt first request
                    DB-->>API: claimed
                    API->>DB: business write + stored response
                else completed duplicate
                    DB-->>API: previous response
                else same key, different payload
                    DB-->>API: reject conflict
                end
                API-->>C: stable result
        ''',
        "retry": '''
            sequenceDiagram
                participant Caller
                participant Dependency
                Caller->>Dependency: attempt 1 with timeout
                Dependency--xCaller: transient 503
                Note over Caller: exponential backoff + full jitter
                Caller->>Dependency: attempt 2 within deadline
                Dependency-->>Caller: success
        ''',
        "timeout": '''
            flowchart LR
                Deadline["End-to-end deadline: 800 ms"] --> Queue["Queue budget"]
                Queue --> DB["Database timeout"]
                DB --> Downstream["Downstream timeout"]
                Downstream --> Serialize["Response budget"]
                Downstream -->|deadline exceeded| Cancel["Propagate cancellation + cleanup"]
        ''',
        "circuit-breaker": '''
            stateDiagram-v2
                [*] --> Closed
                Closed --> Open: failure / slow-call threshold
                Open --> HalfOpen: cooldown elapsed
                HalfOpen --> Closed: limited probes succeed
                HalfOpen --> Open: probe fails
        ''',
        "outbox-pattern": '''
            flowchart LR
                API --> Tx["Local DB transaction"]
                subgraph TxBlock["Atomic boundary"]
                    Business[(Business rows)]
                    Outbox[(Outbox rows)]
                end
                Tx --> Business
                Tx --> Outbox
                Outbox --> Relay["Poller / CDC relay"]
                Relay --> Broker[(Kafka / queue)]
                Broker --> Consumer
        ''',
        "saga": '''
            sequenceDiagram
                participant O as Orchestrator
                participant C as Claim
                participant I as Inventory
                participant P as Payment
                O->>C: approve claim
                C-->>O: committed
                O->>I: reserve part
                I-->>O: committed
                O->>P: pay dealer
                P--xO: permanent failure
                O->>I: compensate release
                O->>C: mark manual review
        ''',
        "rag": '''
            flowchart LR
                Query --> Embed["Query embedding"]
                Embed --> Retrieve["Hybrid retrieval + ACL filter"]
                Retrieve --> Rerank
                Rerank --> Pack["Context packing"]
                Pack --> Prompt["Versioned prompt"]
                Prompt --> LLM
                LLM --> Validate["Citation / policy validation"]
                Validate --> Stream
        ''',
    }
    if folder == "07-celery" and key == "architecture":
        return mermaid_block(special["celery-architecture"])
    if key in special:
        return mermaid_block(special[key])

    generic: dict[str, str] = {
        "01-python-core": f'''flowchart LR
            Source["Python source"] --> Runtime["{title} runtime behavior"]
            Runtime --> Objects["Objects + references + types"]
            Objects --> Result["Observable result"]
            Runtime --> Inspect["dis / sys / gc / tests"]''',
        "02-python-concurrency": f'''flowchart LR
            Work["{title} workload"] --> Scheduler["OS / Python scheduler"]
            Scheduler --> Running["Running execution unit"]
            Running -->|wait / yield| Waiting
            Waiting -->|ready| Scheduler
            Running --> Shared["Shared state + synchronization"]''',
        "03-fastapi": f'''flowchart LR
            Client --> ASGI["ASGI server"] --> FastAPI
            FastAPI --> Topic["{title}"]
            Topic --> Service --> Dependency["DB / cache / downstream"]
            Dependency --> Response --> Client''',
        "04-database-postgresql": f'''flowchart LR
            SQL --> Plan["Planner decision for {title}"]
            Plan --> Executor
            Executor --> Index[(Index pages)]
            Executor --> Heap[(Heap pages)]
            Executor --> Result''',
        "05-sqlalchemy": f'''flowchart LR
            Request --> Session["Session / unit of work"]
            Session --> Topic["{title}"]
            Topic --> SQL
            SQL --> Pool --> PostgreSQL''',
        "06-redis": f'''flowchart LR
            Client --> Command["{title} command / pattern"]
            Command --> EventLoop["Redis execution path"]
            EventLoop --> Memory["In-memory data structure"]
            Memory --> Persist["TTL / persistence / replication"]''',
        "07-celery": f'''sequenceDiagram
            participant P as Producer
            participant B as Broker
            participant W as Worker
            participant S as Business state
            P->>B: publish {title}
            B->>W: at-least-once delivery
            W->>S: idempotent transition
            W->>B: ACK after durable outcome''',
        "08-api-design": f'''sequenceDiagram
            participant C as Client
            participant API
            participant S as Service
            C->>API: request using {title}
            API->>API: validate identity + contract
            API->>S: state transition
            S-->>API: result / typed failure
            API-->>C: stable response''',
        "10-distributed-systems": f'''flowchart LR
            Caller -->|request / message| A["Service A"]
            A --> Topic["{title} boundary"]
            Topic -->|network may delay / duplicate / fail| B["Service B"]
            B --> Durable[(Durable state)]
            Durable --> Reconcile["Retry / reconcile"]''',
        "11-system-design": f'''flowchart LR
            Requirement --> Estimate
            Estimate --> Simple["Simple {title} design"]
            Simple --> Measure["Measure bottleneck"]
            Measure --> Scale["Add capacity / partition / queue"]
            Scale --> Operate["SLO + failure recovery"]''',
        "13-kubernetes": f'''flowchart TB
            User --> LB --> Ingress --> Service
            Service --> P1["Pod 1"]
            Service --> P2["Pod 2"]
            Controller["{title} controller / object"] -.reconcile.-> P1
            Controller -.reconcile.-> P2
            P1 --> DB[(Downstream)]
            P2 --> DB''',
        "16-security": f'''flowchart LR
            Actor --> Boundary["Trust boundary"]
            Boundary --> AuthN
            AuthN --> AuthZ
            AuthZ --> Topic["{title} control"]
            Topic --> Resource
            Topic --> Audit[(Audit log)]''',
        "17-performance-reliability": f'''flowchart LR
            Client --> API --> Pool --> DB
            API -.span.-> Trace["{title} telemetry"]
            Pool -.metric.-> Trace
            DB -.span + metric.-> Trace
            Trace --> Alert["SLO / burn-rate alert"]''',
        "18-ai-integration": f'''flowchart LR
            Input --> Guard["Auth + policy"] --> Topic["{title}"]
            Topic --> Model["Versioned model / provider"]
            Model --> Validate["Quality + schema validation"]
            Validate --> Output
            Topic --> Telemetry["Latency + tokens + quality"]''',
        "20-senior-scenarios": f'''flowchart TD
            Detect["Detect {title}"] --> Stabilize
            Stabilize --> Observe["Metrics + logs + traces"]
            Observe --> Hypothesis
            Hypothesis --> Verify
            Verify --> Mitigate
            Mitigate --> Prevent["Fix + guardrail + runbook"]''',
    }
    return mermaid_block(generic[folder])


FAILURE_GUIDANCE: dict[str, str] = {
    "01-python-core": "Failure thường xuất hiện dưới dạng aliasing sai, retained reference, unexpected lookup hoặc version-specific behavior. Reproduce với input nhỏ, quan sát identity/type/referrer và giảm global/cache lifetime trước khi đổi GC tuning.",
    "02-python-concurrency": "Dưới load, blocking call, unbounded fan-out, race hoặc lock contention làm queue/loop lag tăng. Áp deadline, semaphore/pool bound, structured cancellation và tách CPU work khỏi event loop.",
    "03-fastapi": "Một blocking dependency hoặc pool cạn có thể giữ toàn worker/loop, rồi client retry khuếch đại traffic. Load-shed/rate-limit, rollback, isolate route và bảo vệ downstream trước khi tăng replica.",
    "04-database-postgresql": "Plan regression, lock wait, connection storm, bloat hoặc I/O saturation làm tail latency tăng. Mitigate bằng rollback/query kill có chọn lọc/admission control; thay đổi index/schema phải verify bằng representative plan và write cost.",
    "05-sqlalchemy": "Session leak, long transaction, implicit lazy load hoặc pool exhaustion thường bị ORM che. Log query count/pool wait/transaction age, rollback đúng scope và inspect SQL thật.",
    "06-redis": "Redis timeout/down tạo cache miss storm hoặc mất coordination. Circuit-break nhanh, dùng stale/bounded fallback, rate-limit source of truth và warm cache dần; không retry mọi command đồng loạt.",
    "07-celery": "Worker có thể commit rồi crash trước ACK, hoặc ACK sớm rồi crash trước effect. Thiết kế idempotent business transition, retry budget, DLQ và reconciliation thay vì dựa task ID/lock.",
    "08-api-design": "Timeout khiến client không biết server đã commit chưa; retry có thể duplicate. Idempotency key, optimistic version, stable error semantics và request deadline phải nằm trong contract.",
    "10-distributed-systems": "Network partition/timeout biến outcome thành unknown. Không suy diễn failure từ timeout; dùng operation identity, durable state, retry có budget, circuit/bulkhead và reconciliation.",
    "11-system-design": "Một tier scale nhanh có thể overload tier stateful. Mỗi design cần degraded mode, global capacity budget, backpressure, multi-AZ restore test và per-tenant isolation.",
    "13-kubernetes": "Pod healthy không có nghĩa dependency khỏe. Probe sai gây restart storm; HPA scale API có thể connection-storm DB. Cap theo downstream và test graceful drain/zone failure.",
    "16-security": "Credential hợp lệ vẫn có thể truy cập sai tenant nếu authorization thiếu. Fail closed cho sensitive operation, rotate/revoke credential và giữ audit không lộ secret.",
    "17-performance-reliability": "Average che tail; retry che dependency suy yếu đến khi budget cạn. Alert theo user SLI/burn rate, saturation và queue age, rồi dùng trace tìm critical-path change.",
    "18-ai-integration": "Provider timeout, retrieval miss hoặc prompt injection có thể vẫn trả HTTP 200 nhưng answer sai. Có abstention, citation/ACL validation, fallback và evaluation/replay theo version.",
    "20-senior-scenarios": "Mitigation không có verification có thể chỉ chuyển failure sang dependency khác. Theo dõi SLI, saturation và correctness/reconciliation cho tới khi hệ thống thực sự ổn định.",
}


DEBUG_STEPS: dict[str, list[str]] = {
    "01-python-core": ["Reproduce với input/lifetime nhỏ nhất", "Đo RSS và Python heap; so snapshot `tracemalloc`", "Inspect type, identity, referrer/owner", "Kiểm global, closure, cache và container retention", "Xác nhận behavior theo Python/CPython version"],
    "02-python-concurrency": ["Phân loại CPU-bound, blocking I/O hay async I/O", "Xem per-core CPU, event-loop lag, thread/process/queue depth", "Capture stack/profile của execution unit đang giữ CPU/lock", "Kiểm semaphore, timeout, cancellation và shared-state invariant", "Load test lại với bounded concurrency"],
    "03-fastapi": ["So p50/p95/p99 theo route/worker/deploy", "Xem event-loop lag, thread tokens và worker saturation", "Trace middleware → dependency → endpoint → DB/cache", "Đo DB pool wait và downstream deadline/retry", "Rollback/canary fix rồi verify SLO"],
    "04-database-postgresql": ["Kiểm DB CPU/IO/connections và application pool wait", "Dùng `pg_stat_activity` xem wait/lock/transaction age", "Dùng `pg_stat_statements` tìm total-time/calls/rows regression", "Chạy `EXPLAIN (ANALYZE, BUFFERS)` an toàn trên dữ liệu đại diện", "Kiểm estimate, scan/join, loops, spill, index/statistics/bloat", "Mitigate rồi đo lại p99 và write/WAL cost"],
    "05-sqlalchemy": ["Bật SQL timing/query count có sampling", "Xem pool checked-out/wait/timeout", "Kiểm session scope, autoflush và transaction age", "Tìm lazy load/N+1 và row amplification", "So generated SQL + plan trước/sau"],
    "06-redis": ["Xem command p99/slowlog và client timeout", "Đo memory/RSS/fragmentation/eviction/expired", "Tìm hot/big key và O(N) command", "Kiểm replication lag/failover/topology refresh", "Circuit-break, bảo vệ source và verify warm-up"],
    "07-celery": ["Đo oldest task age, runtime percentile, retry/failure", "So active/reserved/prefetch và worker RSS/CPU", "Trace publish → delivery → attempt → business state → ACK", "Kiểm visibility/consumer timeout và deploy termination", "Quarantine poison task; reconcile duplicate/missing effect"],
    "08-api-design": ["Phân đoạn error/latency theo endpoint/client/version", "Trace idempotency key và state transition", "Kiểm timeout/retry classification và payload hash", "Xem rate quota/abuse và compatibility failures", "Replay contract/integration test"],
    "10-distributed-systems": ["Vẽ timeline theo correlation/message/operation ID", "Phân biệt timeout, rejection, duplicate và stale observation", "Xác định last durable state ở từng component", "Kiểm retry/deadline/circuit/queue lag", "Reconcile source of truth với projection/external effect"],
    "11-system-design": ["Xác nhận user-visible SLI và blast radius", "Trace critical read/write path", "Xem saturation: worker, pool, DB, cache, queue, provider", "Tìm hot tenant/key/partition và retry amplification", "Kích hoạt degraded mode/rollback", "Cập nhật capacity model và failure test"],
    "13-kubernetes": ["Describe workload/pod và đọc event", "Kiểm readiness/endpoints/restart/previous logs", "Xem CPU throttling, OOM, request/limit và node pressure", "Trace DNS/network/service/downstream", "Kiểm rollout diff, HPA metric và graceful termination"],
    "16-security": ["Contain credential/session và preserve audit evidence", "Xác định actor/resource/tenant/action bị ảnh hưởng", "Kiểm authN, authZ policy và trust boundary", "Rotate/revoke/fix least privilege", "Backfill detection và regression test"],
    "17-performance-reliability": ["Xác nhận SLI/baseline và recent change", "Phân rã queue time/service time theo trace", "Kiểm RED/USE và saturation", "Profile bottleneck đã khoanh vùng", "Canary một thay đổi và so tail/cost"],
    "18-ai-integration": ["Tách system latency khỏi retrieval/model quality", "Trace retrieval/rerank/prompt/provider/stream", "Kiểm model/prompt/index/data version và ACL", "Đo tokens/quota/retry/fallback", "Replay golden set và affected slice"],
    "20-senior-scenarios": ["Declare severity/owner và customer impact", "Freeze recent risky change", "Mitigate bằng action reversible", "Dùng evidence kiểm từng hypothesis", "Verify recovery bằng SLI + correctness", "RCA và prevention có owner/deadline"],
}


RELATED_LINKS: dict[str, list[tuple[str, str]]] = {
    "01-python-core": [("Reference Counting", "gc-reference-counting.md"), ("GIL", "../02-python-concurrency/gil.md"), ("Python Profiling", "../17-performance-reliability/profiling-python.md")],
    "02-python-concurrency": [("AsyncIO", "asyncio.md"), ("Event Loop", "event-loop.md"), ("FastAPI Sync vs Async", "../03-fastapi/sync-vs-async-endpoint.md"), ("CPU vs I/O", "cpu-vs-io-bound.md")],
    "03-fastapi": [("Request Lifecycle", "request-lifecycle.md"), ("Sync vs Async", "sync-vs-async-endpoint.md"), ("Connection Pooling", "../04-database-postgresql/connection-pooling.md"), ("API Security", "../16-security/api-security.md")],
    "04-database-postgresql": [("Index", "index.md"), ("EXPLAIN ANALYZE", "explain-analyze.md"), ("MVCC", "mvcc.md"), ("Transactions", "transaction.md"), ("SQLAlchemy Session", "../05-sqlalchemy/session-lifecycle.md")],
    "05-sqlalchemy": [("Session Lifecycle", "session-lifecycle.md"), ("Transactions", "transaction.md"), ("PostgreSQL Pooling", "../04-database-postgresql/connection-pooling.md")],
    "06-redis": [("Redis Internals", "redis-internals.md"), ("Cache Patterns", "cache-patterns.md"), ("Redis Outage", "../20-senior-scenarios/redis-down.md"), ("Distributed Lock", "../10-distributed-systems/distributed-lock.md")],
    "07-celery": [("Task Lifecycle", "task-lifecycle.md"), ("Idempotency", "idempotency.md"), ("Exactly-once Myth", "exactly-once-myth.md"), ("Duplicate Task Incident", "../20-senior-scenarios/celery-task-duplicate.md")],
    "08-api-design": [("Idempotency", "idempotency.md"), ("Retry and Timeout", "retry-timeout.md"), ("API Security", "api-security.md")],
    "10-distributed-systems": [("Idempotency", "idempotency.md"), ("Retry", "retry.md"), ("Timeout", "timeout.md"), ("Outbox", "outbox-pattern.md"), ("Failure Scenarios", "failure-scenarios.md")],
    "11-system-design": [("Design Framework", "system-design-framework.md"), ("Capacity Estimation", "capacity-estimation.md"), ("Observability", "observability.md"), ("Production Scenarios", "../20-senior-scenarios/README.md")],
    "13-kubernetes": [("HPA", "hpa.md"), ("Resource Limits", "resource-limit.md"), ("Health Checks", "health-check.md"), ("Troubleshooting", "troubleshooting.md")],
    "16-security": [("API Security", "api-security.md"), ("OAuth 2.0", "oauth2.md"), ("Secrets", "secrets-management.md")],
    "17-performance-reliability": [("Observability", "observability.md"), ("SLI/SLO/SLA", "sli-slo-sla.md"), ("Incident Debugging", "incident-debugging.md")],
    "18-ai-integration": [("RAG", "rag.md"), ("Vector Database", "vector-database.md"), ("AI Observability", "ai-observability.md"), ("AI Chatbot Design", "../11-system-design/design-ai-chatbot.md")],
    "20-senior-scenarios": [("Incident Debugging", "../17-performance-reliability/incident-debugging.md"), ("Observability", "../17-performance-reliability/observability.md"), ("System Design", "../11-system-design/README.md")],
}


def deep_dive_appendix(folder: str, filename: str, title: str) -> str:
    if folder not in DEEP_DIVE_FOLDERS:
        return ""
    key = key_for(filename)
    mental = MENTAL_MODELS.get(key, f"Hãy xem **{title}** như một boundary biến input/state thành output. Muốn hiểu sâu phải chỉ ra ai sở hữu state, lifecycle, điểm contention và behavior khi dependency chậm hoặc mất.")
    internals = INTERNAL_DEEP_DIVES.get((folder, key), FOLDER_INTERNALS[folder])
    diagram = concept_diagram(folder, filename, title)
    failure = FAILURE_GUIDANCE[folder]
    steps = "\n".join(f"{i}. {step}." for i, step in enumerate(DEBUG_STEPS[folder], 1))
    misconceptions = {
        "01-python-core": "**Sai:** syntax mô tả đầy đủ memory behavior. **Đúng:** binding, alias, object lifetime và CPython optimization quyết định behavior; implementation detail phải gắn version.",
        "02-python-concurrency": "**Sai:** concurrency luôn là parallelism và thêm worker luôn tăng throughput. **Đúng:** queueing, GIL, locks và downstream capacity có thể làm p99 tệ hơn.",
        "03-fastapi": "**Sai:** đổi mọi endpoint thành `async def` làm API nhanh. **Đúng:** toàn dependency path phải non-blocking và concurrency phải được bound.",
        "04-database-postgresql": "**Sai:** có index thì PostgreSQL phải dùng index. **Đúng:** planner chọn plan theo cost/selectivity; sequential scan có thể rẻ hơn.",
        "05-sqlalchemy": "**Sai:** ORM loại bỏ nhu cầu hiểu SQL/transaction. **Đúng:** ORM chỉ sinh và hydrate SQL; database semantics vẫn quyết định correctness/performance.",
        "06-redis": "**Sai:** Redis ở RAM nên mọi command đều nhanh và có thể làm primary store mặc định. **Đúng:** complexity/big key/main execution path và durability model vẫn quan trọng.",
        "07-celery": "**Sai:** task thành công trong log nghĩa business effect exactly once. **Đúng:** ACK, result backend và domain commit là các boundary độc lập.",
        "08-api-design": "**Sai:** HTTP method/status đủ tạo idempotency. **Đúng:** server phải atomically dedupe logical operation và xử lý unknown outcome.",
        "10-distributed-systems": "**Sai:** timeout chứng minh operation thất bại. **Đúng:** server có thể đã commit; timeout chỉ nói caller chưa quan sát response.",
        "11-system-design": "**Sai:** diagram nhiều service là senior design. **Đúng:** design senior giải thích requirement, số liệu, source of truth, failure và lý do từng component xuất hiện.",
        "13-kubernetes": "**Sai:** Kubernetes làm application high availability tự động. **Đúng:** probe, state, dependency và capacity budget sai vẫn tạo outage tự động ở quy mô lớn.",
        "16-security": "**Sai:** JWT hợp lệ nghĩa request được phép. **Đúng:** token chỉ hỗ trợ authentication; authorization phải kiểm resource/tenant/action.",
        "17-performance-reliability": "**Sai:** average latency tốt nghĩa system khỏe. **Đúng:** tail, saturation, error semantics và user journey mới phản ánh SLO.",
        "18-ai-integration": "**Sai:** HTTP 200 và answer trôi chảy nghĩa AI đúng. **Đúng:** phải đo retrieval, groundedness, citation, safety, cost và task success.",
        "20-senior-scenarios": "**Sai:** restart service là root-cause fix. **Đúng:** restart có thể giảm impact nhưng phải giữ evidence, tìm mechanism và thêm prevention.",
    }[folder]
    not_use = {
        "01-python-core": "Không phụ thuộc CPython-specific behavior nếu library phải chạy nhiều implementation/version; ưu tiên language contract và benchmark thực tế.",
        "02-python-concurrency": "Không thêm concurrency khi workload nhỏ hoặc downstream đã saturated; model tuần tự đơn giản có thể đúng và dễ vận hành hơn.",
        "03-fastapi": "Không dùng async chỉ vì framework hỗ trợ; sync stack với bounded thread pool có thể đơn giản hơn khi dependency chỉ blocking.",
        "04-database-postgresql": "Không thêm index/partition/replica trước khi access pattern và bottleneck được đo; mỗi component tăng write/operation cost.",
        "05-sqlalchemy": "Không hydrate object graph cho bulk analytics/ETL; SQLAlchemy Core/raw parameterized SQL có thể rõ và rẻ hơn.",
        "06-redis": "Không thêm cache nếu query đã nhanh, traffic thấp hoặc invalidation cost vượt lợi ích; không dùng lock Redis thay DB invariant.",
        "07-celery": "Không đưa work cần response tức thì hoặc transaction atomic đơn giản qua queue; queue thêm lag, duplicate và operational surface.",
        "08-api-design": "Không tạo version/abstraction mới khi chưa có compatibility need; contract nhỏ, explicit thường tốt hơn generic framework.",
        "10-distributed-systems": "Không dùng consensus/lock/saga nếu một local transaction hoặc unique constraint giải được invariant.",
        "11-system-design": "Ở 100 RPS, tránh Kafka, sharding và nhiều microservice nếu 2 API instance + PostgreSQL đáp ứng SLO và recovery.",
        "13-kubernetes": "Không chọn Kubernetes chỉ để chạy vài service ít thay đổi nếu managed container/serverless đơn giản hơn và team thiếu operational ownership.",
        "16-security": "Không tự thiết kế crypto/token protocol khi chuẩn và managed identity đáp ứng; custom security mở thêm attack surface.",
        "17-performance-reliability": "Không optimize từ intuition hoặc microbenchmark không đại diện; đo user SLI và bottleneck trước.",
        "18-ai-integration": "Không dùng LLM khi rule/search/deterministic parser đáp ứng accuracy, latency và cost tốt hơn.",
        "20-senior-scenarios": "Không thực hiện thay đổi irreversible/high-blast-radius trong incident nếu còn mitigation an toàn và evidence chưa đủ.",
    }[folder]
    links = []
    for label, target in RELATED_LINKS[folder]:
        if target == filename:
            continue
        links.append(f"- [{label}]({target})")
    link_text = "\n".join(links[:4])
    return dedent(f'''\

    ## 13. Mental Model

    {mental}

    ## 14. Internals Deep Dive

    {internals}

    Implementation detail có thể đổi theo version; khi trả lời interview, nêu rõ CPython/PostgreSQL/Redis/framework version nếu kết luận dựa vào behavior nội bộ thay vì public contract.

    ## 15. Request / Data Flow

    {diagram}

    Đọc diagram từ input tới state transition và output. Tại mỗi mũi tên, hỏi: operation có block không, có retry không, state có durable không, identity nào dùng để dedupe và metric nào chứng minh bước đó khỏe.

    ## 16. Failure Scenario

    {failure}

    Phân tích theo chuỗi: **trigger → saturation/incorrect state → propagation → user impact → immediate mitigation → durable prevention**. Tránh gọi retry hoặc scale là giải pháp nếu chưa chỉ ra dependency budget.

    ## 17. How I would debug this in production

    {steps}

    ## 18. Common Misconceptions

    {misconceptions}

    ## 19. When NOT to use

    {not_use}

    ## 20. What interviewer may ask next

    1. **What guarantee does {title} provide, and what does it explicitly not guarantee?**
    2. **Which implementation detail changes across versions or runtimes?**
    3. **Where is the first queue or contention point under high load?**
    4. **What happens if the dependency times out after committing state?**
    5. **How would you observe, degrade, and recover this in production?**
    6. **Which simpler design would you choose at 100 RPS, and when would you evolve it?**

    ## 21. Check Your Understanding

    1. Nếu throughput tăng 20× nhưng downstream capacity không đổi, **{title}** sẽ tạo queue/backpressure ở đâu?
    2. Timeout xảy ra ngay sau một state transition; caller có thể kết luận điều gì và không thể kết luận điều gì?
    3. Metric, trace span và log field tối thiểu nào giúp phân biệt application, dependency và network latency?

    <details>
    <summary>Answer</summary>

    1. Queue xuất hiện tại bounded resource đầu tiên: worker/thread/semaphore/connection pool/broker hoặc dependency. Nếu không có bound, overload chuyển thành memory growth và timeout storm.
    2. Caller chỉ biết chưa nhận response trong deadline; operation có thể chưa chạy, đang chạy hoặc đã commit. Cần operation identity/idempotency và status/reconciliation.
    3. Dùng end-to-end latency + queue/service time, correlation/trace ID, dependency spans, error/retry classification và saturation của pool/queue/resource.

    </details>

    ## 22. See also

    {link_text}
    ''')


def knowledge_doc(folder: str, filename: str) -> str:
    title = title_from_name(filename)
    c = CATEGORY[folder]
    definition, mechanics, use_case = insight_for(folder, filename)
    q_basic, q_senior, short_answers, followups = question_sections(folder, filename, title, definition)
    return dedent(f'''\
    # {title}

    > **Phạm vi phỏng vấn:** {c['label']} · **Ưu tiên:** {'P0/P1' if key_for(filename) in INSIGHTS or (folder, key_for(filename)) in SCOPED_INSIGHTS else 'P1/P2'} · **Mindset:** Why → How → Trade-off → Production.

    ## 1. What is it?

    {definition}

    ## 2. Why does it matter?

    Senior Engineer cần hiểu **{title}** để {c['why']}. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

    ## 3. How does it work?

    {mechanics}

    Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `{c['metric']}` và phân biệt symptom, bottleneck với root cause.

    ## 4. Example

    {example_for(folder, filename, title)}

    ## 5. Production Use Case

    {use_case}

    Checklist triển khai: capacity budget, timeout, idempotency (nếu có side effect), telemetry, canary, rollback và reconciliation.

    ## 6. Common Problems

    - Không định nghĩa invariant và source of truth trước khi chọn công nghệ.
    - Retry không backoff/jitter làm traffic amplification khi dependency lỗi.
    - Không có bound cho queue, connection, memory hoặc concurrency.
    - Chỉ theo dõi average; bỏ qua p95/p99, saturation và error semantics.
    - Rollout toàn bộ, thiếu feature flag/canary và đường rollback dữ liệu.

    ## 7. Trade-offs

    | Lựa chọn | Lợi ích | Chi phí / rủi ro | Khi phù hợp |
    |---|---|---|---|
    | Tối ưu/thiết kế xoay quanh {title} | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
    | Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
    | Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
    | Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

    ## 8. Interview Questions

    {q_basic}

    ## 9. Senior-level Questions

    {q_senior}

    ## 10. Short Answers

    {short_answers}

    Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

    ## 11. Follow-up Questions

    {followups}

    ## 12. Key Takeaways

    - Nói được **vai trò, constraint hoặc invariant của {title}**, không chỉ “dùng để làm gì”.
    - Định lượng bằng {c['metric']} và có baseline trước tối ưu.
    - Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
    - Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
    - Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.

    {deep_dive_appendix(folder, filename, title)}
    ''')


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = normalize_markdown(content) if path.suffix == ".md" else content
    path.write_text(rendered.strip() + "\n", encoding="utf-8")


def normalize_markdown(content: str) -> str:
    """Remove template indentation while preserving relative fenced-code indentation."""
    lines = content.splitlines()
    outside_normalized: list[str] = []
    in_fence = False
    for line in lines:
        if not in_fence and line.startswith("    "):
            line = line[4:]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        outside_normalized.append(line)
    interim = "\n".join(outside_normalized)

    def normalize_fence(match: re.Match[str]) -> str:
        language = match.group(1)
        body_lines = match.group(2).splitlines()
        indents = [len(line) - len(line.lstrip()) for line in body_lines if line.strip()]
        margin = min(indents, default=0)
        body = "\n".join(line[margin:] if line.strip() else "" for line in body_lines)
        return f"```{language}\n{body}\n```"

    return re.sub(r"```([^\n]*)\n(.*?)\n\s*```", normalize_fence, interim, flags=re.S)


DESIGNS: dict[str, dict[str, str]] = {
    "design-ai-chatbot.md": {
        "title": "AI Chatbot Platform",
        "goal": "chat đa tenant, RAG theo ACL, streaming token, citation và model fallback",
        "scale": "10M user, 1M DAU, 2.000 peak RPS; 20 lượt hội thoại/user/ngày; trung bình 3.000 input + 500 output token",
        "api": "`POST /v1/conversations`, `POST /v1/conversations/{id}/messages` (SSE), `GET /v1/conversations/{id}`",
        "entities": "Tenant, User, Conversation, Message, Document, Chunk, RetrievalTrace, ModelUsage",
        "db": "PostgreSQL cho metadata/message; object storage cho document; vector DB cho embedding; analytics store cho evaluation",
        "cache": "Redis cache session/config, semantic cache có tenant/model/prompt version và TTL ngắn",
        "queue": "Kafka/SQS cho ingestion, embedding, evaluation và usage accounting; online generation không đi queue nếu cần interactive latency",
        "special": "Prompt injection, hallucination, token budget, model rate limit, citation correctness và data residency",
        "nodes": 'Client --> Gateway --> Auth\n    Auth --> ChatAPI["Chat API"]\n    ChatAPI --> Redis[(Redis)]\n    ChatAPI --> Orchestrator\n    Orchestrator --> Retriever\n    Retriever --> VectorDB[(Vector DB)]\n    Orchestrator --> LLM["LLM Provider"]\n    LLM --> Stream["SSE Stream"]\n    ChatAPI --> PG[(PostgreSQL)]\n    Object[(Object Storage)] --> Ingestion\n    Ingestion --> Queue[(Queue)] --> Embedder --> VectorDB\n    Orchestrator --> Telemetry["Metrics / Traces"]',
    },
    "design-document-processing.md": {
        "title": "Intelligent Document Processing System",
        "goal": "upload, antivirus, OCR, classify, extract field, human review và export có audit",
        "scale": "5M document/ngày; trung bình 8 trang, 2 MB; peak upload 500 RPS; retention 7 năm",
        "api": "`POST /v1/documents` (pre-signed upload), `GET /v1/jobs/{id}`, `POST /v1/reviews/{id}/decisions`",
        "entities": "Document, BlobVersion, ProcessingJob, Page, Extraction, ReviewTask, AuditEvent",
        "db": "PostgreSQL metadata/workflow; immutable object storage cho original/derived artifact; search index cho extracted text",
        "cache": "Redis cho job status ngắn hạn và tenant configuration; source of truth vẫn ở database",
        "queue": "Queue tách scan → OCR → classify → extract → validate; DLQ và replay theo stage",
        "special": "PII, malware, corrupt file, model confidence, page-level retry, retention/legal hold và human-in-the-loop",
        "nodes": 'Client --> UploadAPI["Upload API"] --> ObjectStore[(Object Storage)]\n    UploadAPI --> PG[(PostgreSQL)]\n    UploadAPI --> Queue[(Workflow Queue)]\n    Queue --> Scan["AV Scan"] --> OCR\n    OCR --> Parser --> Classifier --> Extractor\n    Parser --> Chunking --> Embedder --> VectorDB[(Vector DB)]\n    Extractor --> Review["Human Review"] --> Exporter',
    },
    "design-vehicle-inspection.md": {
        "title": "Vehicle Inspection Platform",
        "goal": "lập lịch, nhận checklist/ảnh/video, chạy rule/AI, ký biên bản và đồng bộ dealer",
        "scale": "2M inspection/tháng; peak 300 submission RPS; mỗi phiên 80 ảnh × 4 MB; kết quả online dưới 5 giây",
        "api": "`POST /v1/inspections`, `POST /v1/inspections/{id}/media`, `POST /v1/inspections/{id}/complete`, `GET /v1/vehicles/{vin}/inspections`",
        "entities": "Vehicle, Inspection, ChecklistVersion, Finding, MediaAsset, ModelResult, Inspector, AuditEvent",
        "db": "PostgreSQL cho workflow/constraint; object storage media; search/warehouse cho analytics và recall",
        "cache": "Redis cache checklist/version và short-lived upload session; không cache final signed result như source of truth",
        "queue": "Event bus cho media analysis, fraud check, report generation và integration event",
        "special": "VIN uniqueness, offline/mobile sync, evidence immutability, model false negative, manual override và auditability",
        "nodes": 'InspectorApp["Inspector App"] --> Gateway --> InspectionAPI["Inspection API"]\n    InspectionAPI --> PG[(PostgreSQL)]\n    InspectionAPI --> Upload["Pre-signed Upload"] --> ObjectStore[(Object Storage)]\n    InspectionAPI --> Bus[(Event Bus)]\n    Bus --> Vision["Vision Workers"]\n    Vision --> Findings["Finding Service"]\n    Findings --> Report["Signed Report"]',
    },
    "design-vehicle-warranty.md": {
        "title": "Vehicle Warranty System",
        "goal": "validate eligibility, submit claim, approval workflow, parts/labor settlement và chống duplicate/fraud",
        "scale": "50M vehicle, 500M service records; 200 claim write RPS, 5.000 read RPS; dữ liệu tài chính giữ 10 năm",
        "api": "`POST /v1/claims` với Idempotency-Key, `GET /v1/claims/{id}`, `POST /v1/claims/{id}/decisions`, `GET /v1/vehicles/{vin}/coverage`",
        "entities": "Vehicle, WarrantyPolicy, CoverageRule, Claim, ClaimLine, Decision, Payment, Dealer, AuditEvent",
        "db": "PostgreSQL partition theo time/tenant cho claim; ledger append-only cho settlement; warehouse cho fraud/analytics",
        "cache": "Redis cache policy đã compile theo version; invalidation bằng event; eligibility critical vẫn xác minh version",
        "queue": "Outbox/event bus cho review, fraud scoring, payment và enterprise integration",
        "special": "Money invariant, idempotency, temporal policy version, audit, PII, dealer integration và reconciliation",
        "nodes": 'Dealer --> Gateway --> ClaimAPI["Claim API"]\n    ClaimAPI --> Rules["Eligibility Rules"]\n    ClaimAPI --> PG[(PostgreSQL)]\n    PG --> Outbox[(Outbox)]\n    Outbox --> Bus[(Event Bus)]\n    Bus --> Fraud["Fraud Scoring"]\n    Bus --> Review["Review Workflow"]\n    Review --> Ledger[(Settlement Ledger)]',
    },
    "design-production-planning.md": {
        "title": "Manufacturing Production Planning System",
        "goal": "lập kế hoạch theo demand/capacity/material, version scenario, phê duyệt và phát hành schedule tới nhà máy",
        "scale": "20 plant, 100 line, 100k SKU/part; 50M planning row/ngày; batch solve 15 phút và near-real-time disruption event",
        "api": "`POST /v1/plans`, `POST /v1/plans/{id}/solve`, `GET /v1/plans/{id}/diff`, `POST /v1/plans/{id}/publish`",
        "entities": "Plant, Line, Shift, Product, BOMVersion, Demand, Inventory, Constraint, PlanVersion, ScheduleSlot",
        "db": "PostgreSQL metadata/version; columnar warehouse/lake cho history; object storage cho solver input/output snapshot",
        "cache": "Redis cho reference data/version manifest; không cache mutable plan draft không có version",
        "queue": "Workflow queue cho snapshot, solve, validate, publish; event bus nhận supply/machine disruption",
        "special": "Deterministic snapshot, solver timeout, stale input, manual override, plan versioning và ERP/MES integration",
        "nodes": 'Sensor --> Machine --> Line["Production Line"] --> IoT["IoT Gateway"]\n    IoT --> Bus[(Event Bus)] --> Lake[(Data Lake)]\n    ERP["ERP / Inventory / Orders"] --> Bus\n    Planner --> PlanningAPI["Planning API"] --> PG[(Plan Metadata)]\n    PlanningAPI --> Workflow[(Workflow Queue)] --> Snapshot --> Solver\n    Solver --> PlanStore[(Versioned Plans)] --> MES["Factory MES"]',
    },
    "design-video-processing.md": {
        "title": "Video Analytics Platform",
        "goal": "ingest camera/video, transcode, inference, event detection, clip evidence và live alert",
        "scale": "10.000 camera × 2 Mbps ≈ 20 Gbps ingest; 24/7 stream; alert dưới 3 giây; raw retention 30 ngày",
        "api": "`POST /v1/cameras`, `POST /v1/videos`, `GET /v1/events?camera_id=`, `GET /v1/events/{id}/clip`",
        "entities": "Camera, StreamSession, VideoSegment, ModelVersion, Detection, Alert, EvidenceClip",
        "db": "Time-series/search cho event; PostgreSQL control plane; object storage lifecycle tiering cho segment/clip",
        "cache": "Edge/frame buffer và Redis hot camera status; không đẩy video bytes qua Redis",
        "queue": "Partitioned stream theo camera/site; GPU worker consume với bounded lag, DLQ cho corrupt segment",
        "special": "Bandwidth, GPU scheduling, frame dropping policy, clock skew, privacy/masking và model drift",
        "nodes": 'Camera --> Edge["Edge Gateway"] --> Ingest["Stream Ingest"]\n    Ingest --> Segments[(Object Storage)]\n    Ingest --> Stream[(Partitioned Stream)]\n    Stream --> GPU["GPU Inference"]\n    GPU --> EventStore[(Event Store)]\n    GPU --> Alert["Alert Service"]\n    Alert --> Operator',
    },
    "design-notification-system.md": {
        "title": "Large-scale Notification System",
        "goal": "gửi email/SMS/push/in-app theo preference, priority, template, schedule và delivery status",
        "scale": "1B notification/ngày, peak 100k event/s; transactional p99 enqueue dưới 200ms; marketing có thể delay",
        "api": "`POST /v1/notifications` với idempotency key, `POST /v1/campaigns`, `GET /v1/deliveries/{id}`",
        "entities": "Notification, Recipient, Preference, TemplateVersion, Campaign, DeliveryAttempt, ProviderReceipt",
        "db": "PostgreSQL control/config; wide-column/log store cho attempt; object storage cho campaign audience snapshot",
        "cache": "Redis cache preference/template có version; rate counter token-bucket theo tenant/provider",
        "queue": "Priority queue tách transactional/marketing và channel; retry queue có delay, DLQ, dedupe",
        "special": "Fan-out, provider quota, unsubscribe compliance, duplicate, ordering per recipient và callback spoofing",
        "nodes": 'Producer --> API --> PG[(PostgreSQL)]\n    PG --> Outbox[(Outbox)] --> Router\n    Router --> EmailQ[(Email Queue)]\n    Router --> SMSQ[(SMS Queue)]\n    Router --> PushQ[(Push Queue)]\n    EmailQ --> Provider["Channel Providers"]\n    SMSQ --> Provider\n    PushQ --> Provider\n    Provider --> Receipt["Receipt Processor"]',
    },
    "design-file-processing.md": {
        "title": "Distributed File Processing System",
        "goal": "upload lớn, validate, transform nhiều stage, track progress, download artifact và replay an toàn",
        "scale": "2M file/ngày, 100 MB trung bình; multipart upload; peak 20 GB/s aggregate; processing từ giây đến giờ",
        "api": "`POST /v1/uploads`, `POST /v1/uploads/{id}/complete`, `GET /v1/jobs/{id}`, `GET /v1/artifacts/{id}`",
        "entities": "Upload, FileObject, Job, StageAttempt, Artifact, Checksum, TenantQuota",
        "db": "PostgreSQL metadata/state machine; object storage bytes/artifact; job history partition theo ngày",
        "cache": "Redis progress projection có TTL; client có thể fallback database; signed URL ngắn hạn",
        "queue": "Queue theo stage/resource class, visibility timeout > heartbeat, idempotent transition và DLQ",
        "special": "Checksum, resumable upload, zip bomb, malware, large fan-out, orphan artifact và quota",
        "nodes": 'Client --> UploadAPI["Upload API"] --> ObjectStore[(Object Storage)]\n    UploadAPI --> Metadata[(PostgreSQL)]\n    UploadAPI --> Queue[(Stage Queue)]\n    Queue --> Validator --> Transformer --> Publisher\n    Publisher --> Artifact[(Artifact Store)]\n    Transformer --> Status["Status Projector"]',
    },
    "design-realtime-websocket.md": {
        "title": "Real-time WebSocket Platform",
        "goal": "duplex connection, authenticated channel subscription, presence, fan-out và reconnect/resume",
        "scale": "5M concurrent connection, 500k message/s; p99 fan-out dưới 500ms; multi-region",
        "api": "`GET /v1/ws?token=...` upgrade; frames `subscribe`, `publish`, `ack`, `resume`; REST lấy history",
        "entities": "Connection, Session, Channel, Subscription, Message, Cursor, PresenceLease",
        "db": "Durable log/history theo channel; PostgreSQL control plane; ephemeral connection registry theo region",
        "cache": "Redis presence/routing có lease và sharded pub-sub/stream; không coi presence là durable truth",
        "queue": "Partitioned log cho durable ordered message; broker nội vùng cho fan-out latency thấp",
        "special": "Sticky routing, slow consumer, backpressure, resume cursor, heartbeat, reconnect storm và regional failover",
        "nodes": 'Client --> GlobalLB["Global Load Balancer"] --> Gateway["WebSocket Gateway"]\n    Gateway --> Registry[(Connection Registry)]\n    Gateway --> Broker[(Regional Broker)]\n    Broker --> Gateway\n    Gateway --> Log[(Durable Message Log)]\n    API["History API"] --> Log',
    },
    "design-task-processing.md": {
        "title": "Task Processing Platform",
        "goal": "submit, schedule, route, execute, retry/cancel task và cung cấp tenant quota/observability",
        "scale": "100M task/ngày, peak 50k task/s; runtime 100ms–6h; CPU/GPU/memory resource class",
        "api": "`POST /v1/tasks` với idempotency key, `GET /v1/tasks/{id}`, `POST /v1/tasks/{id}/cancel`",
        "entities": "Task, TaskAttempt, Queue, ResourceClass, Schedule, Lease, Result, TenantQuota",
        "db": "PostgreSQL control/state; object storage payload/result lớn; append-only event log cho audit",
        "cache": "Redis status projection/quota token; durable task state không chỉ nằm trong cache",
        "queue": "Partition theo priority/resource; lease/heartbeat, delayed retry, DLQ và fair scheduling",
        "special": "At-least-once, poison task, starvation, lease expiry, cancellation race, noisy neighbor và result retention",
        "nodes": 'Client --> TaskAPI["Task API"] --> State[(PostgreSQL)]\n    State --> Outbox[(Outbox)] --> Scheduler\n    Scheduler --> CPUQ[(CPU Queue)]\n    Scheduler --> GPUQ[(GPU Queue)]\n    CPUQ --> Workers\n    GPUQ --> GPUWorkers["GPU Workers"]\n    Workers --> Result[(Result Store)]\n    GPUWorkers --> Result',
    },
    "design-chat-system.md": {
        "title": "Large-scale Chat System",
        "goal": "1:1/group chat, ordered message per conversation, presence, multi-device sync và attachment",
        "scale": "50M DAU, 20M concurrent connection, peak 1M message/s; history retention nhiều năm",
        "api": "WebSocket `send/ack/typing`; `GET /v1/conversations/{id}/messages?before=&limit=`; pre-signed attachment upload",
        "entities": "User, Device, Conversation, Membership, Message, Receipt, Attachment, Cursor",
        "db": "Partitioned message log theo conversation; PostgreSQL membership/control; object storage attachment",
        "cache": "Presence/connection route và recent conversation metadata; history source vẫn durable store",
        "queue": "Durable partition theo conversation để giữ order; fan-out worker và push-notification queue",
        "special": "Ordering scope, duplicate send, offline sync, hot group, membership ACL và abusive content",
        "nodes": 'Client --> Gateway["WebSocket Gateway"] --> Router\n    Router --> Log[(Message Log)]\n    Router --> Fanout["Fan-out Workers"]\n    Fanout --> Gateway\n    Fanout --> Push["Push Notification"]\n    Gateway --> Presence[(Presence)]\n    HistoryAPI["History API"] --> Log',
    },
}


def design_profile(filename: str) -> str:
    return {
        "design-ai-chatbot.md": "rag",
        "design-document-processing.md": "pipeline",
        "design-file-processing.md": "pipeline",
        "design-video-processing.md": "video",
        "design-vehicle-inspection.md": "workflow",
        "design-vehicle-warranty.md": "workflow",
        "design-production-planning.md": "planning",
        "design-notification-system.md": "notification",
        "design-task-processing.md": "task",
        "design-chat-system.md": "realtime",
        "design-realtime-websocket.md": "realtime",
    }[filename]


def system_design_deep_dive(filename: str, d: dict[str, str]) -> str:
    profile = design_profile(filename)
    sequences: dict[str, str] = {
        "rag": '''
            sequenceDiagram
                participant U as User
                participant API as Chat API
                participant A as Auth / ACL
                participant R as Retriever
                participant O as LLM Orchestrator
                participant L as LLM Provider
                U->>API: Send message
                API->>A: Authenticate + tenant policy
                A-->>API: Principal + allowed documents
                API->>R: Query + ACL + index version
                R-->>API: Reranked chunks + citations
                API->>O: Prompt + token/deadline budget
                O->>L: Stream generation
                L-->>U: Tokens through API with citations
        ''',
        "pipeline": '''
            sequenceDiagram
                participant C as Client
                participant API as Upload API
                participant O as Object Storage
                participant Q as Stage Queue
                participant W as Worker
                participant DB as Job Database
                C->>API: Create upload / job
                API-->>C: Pre-signed multipart URL
                C->>O: Upload bytes + checksum
                C->>API: Complete upload
                API->>DB: Atomic job + outbox
                API->>Q: Publish stage pointer
                Q->>W: At-least-once delivery
                W->>DB: Idempotent stage transition
        ''',
        "video": '''
            sequenceDiagram
                participant C as Camera
                participant E as Edge Gateway
                participant K as Kafka / Stream
                participant G as GPU Worker
                participant S as Event Store
                participant D as Dashboard
                C->>E: Encoded stream
                E->>K: Timestamped segment reference
                K->>G: Partition by camera / site
                G->>G: Decode + sample + inference
                G->>S: Detection + evidence pointer
                S-->>D: Alert / searchable event
        ''',
        "workflow": '''
            sequenceDiagram
                participant C as Client / Station
                participant API
                participant DB as PostgreSQL
                participant O as Outbox
                participant W as Rule / AI Worker
                participant H as Human / Enterprise System
                C->>API: Versioned idempotent command
                API->>DB: State transition + outbox
                DB-->>C: Resource / job ID
                O->>W: At-least-once event
                W->>DB: Conditional result update
                DB->>H: Review / integration event
        ''',
        "planning": '''
            sequenceDiagram
                participant ERP
                participant API as Planning API
                participant S as Snapshot Builder
                participant V as Solver
                participant P as Plan Store
                participant F as Factory / MES
                ERP->>S: Demand + inventory + capacity events
                API->>S: Freeze versioned planning snapshot
                S->>V: Immutable input URI + constraints
                V->>P: Candidate plan + diagnostics
                API->>P: Validate / approve version
                P->>F: Publish schedule with effective version
        ''',
        "notification": '''
            sequenceDiagram
                participant P as Producer
                participant API
                participant DB as Notification DB
                participant Q as Priority Queue
                participant V as Channel Provider
                participant R as Receipt Processor
                P->>API: Idempotent notification command
                API->>DB: Notification + outbox
                DB->>Q: Route by channel / priority
                Q->>V: Send with provider idempotency key
                V-->>R: Delivery callback
                R->>DB: Verify and append attempt status
        ''',
        "task": '''
            sequenceDiagram
                participant C as Client
                participant API as Task API
                participant DB as Task State
                participant S as Scheduler
                participant W as Worker
                participant O as Result Store
                C->>API: Submit task + idempotency key
                API->>DB: Persist task + outbox
                DB->>S: Runnable task event
                S->>W: Lease by resource class
                W->>DB: Heartbeat / attempt state
                W->>O: Store large result
                W->>DB: Conditional completion
        ''',
        "realtime": '''
            sequenceDiagram
                participant C as Sender
                participant G as WebSocket Gateway
                participant L as Durable Log
                participant B as Regional Broker
                participant R as Recipient Gateway
                participant D as Recipient Device
                C->>G: Message + client operation ID
                G->>L: Append in conversation order
                L-->>G: Durable sequence number
                G->>B: Fan-out envelope
                B->>R: Route to active connection
                R-->>D: Deliver message
                D-->>L: Advance durable cursor / receipt
        ''',
    }
    data_flows: dict[str, str] = {
        "rag": '''flowchart LR
            Docs["Documents"] --> Object[(Object storage: binary truth)]
            Object --> Ingest["Parse + chunk + embed"]
            Ingest --> Vector[(Vector DB: derived index)]
            Ingest --> Meta[(PostgreSQL: metadata + ACL truth)]
            Query --> Vector --> Context
            Meta -->|ACL filter| Context
            Context --> LLM --> Answer''',
        "pipeline": '''flowchart LR
            Upload --> Object[(Object storage: byte truth)]
            Object --> Queue[(Stage transport)]
            Queue --> Process["Scan / parse / transform"]
            Process --> Artifact[(Versioned artifacts)]
            Process --> Meta[(PostgreSQL: job truth)]
            Meta --> Status["Redis: rebuildable status projection"]''',
        "video": '''flowchart LR
            Camera --> Segment[(Object storage: video segments)]
            Camera --> Stream[(Partitioned event stream)]
            Stream --> Inference
            Inference --> Events[(Event store: detections)]
            Inference --> Clip[(Evidence clips)]
            Events --> Search["Search / dashboard projection"]''',
        "workflow": '''flowchart LR
            Command --> PG[(PostgreSQL: workflow truth)]
            Media --> Object[(Object storage: evidence truth)]
            PG --> Outbox[(Outbox)] --> Bus[(Event transport)]
            Bus --> Workers
            Workers --> PG
            PG --> Warehouse["Analytics: derived history"]''',
        "planning": '''flowchart LR
            ERP["ERP / MES / IoT"] --> Lake[(Raw event / snapshot history)]
            Lake --> Snapshot["Immutable planning snapshot"]
            Snapshot --> Solver
            Solver --> Plans[(Versioned plan truth)]
            Plans --> Publisher --> Factory
            Plans --> Analytics["Derived KPI projection"]''',
        "notification": '''flowchart LR
            Command --> PG[(PostgreSQL: notification intent)]
            PG --> Outbox --> Queue[(Delivery transport)]
            Queue --> Provider
            Provider --> Receipts[(Attempt / receipt history)]
            PG --> Redis["Redis: preference + quota cache"]
            Receipts --> Analytics["Derived delivery analytics"]''',
        "task": '''flowchart LR
            Submit --> PG[(PostgreSQL: task state truth)]
            PG --> Outbox --> Queues[(Resource queues)]
            Queues --> Worker
            Payload[(Object storage: large payload)] --> Worker
            Worker --> Result[(Object storage: result)]
            Worker --> PG''',
        "realtime": '''flowchart LR
            Send --> Log[(Durable message log)]
            Log --> Broker[(Regional fan-out transport)]
            Broker --> Connections["Ephemeral connections"]
            Connections --> Devices
            Log --> History["History projection / API"]
            Attachment --> Object[(Object storage)]''',
    }
    source_rows: dict[str, str] = {
        "rag": "| Conversation/message/ACL | PostgreSQL | Transactional metadata |\n| Original document | Object storage | Immutable binary/version |\n| Embedding index | Vector DB | Derived; rebuild from document + model version |\n| Session/config cache | Redis | Derived, TTL-bound |\n| Ingestion event | Queue/log | Transport and replay cursor, not document truth |",
        "pipeline": "| Job/stage state | PostgreSQL | Conditional transition and audit |\n| Uploaded bytes/artifacts | Object storage | Checksum + versioned binary truth |\n| Stage message | Queue | Delivery transport; may duplicate |\n| Fast status | Redis | Rebuildable projection |",
        "video": "| Raw segment/evidence clip | Object storage | Retention/lifecycle binary truth |\n| Detection event | Event store | Searchable event truth |\n| Camera/config/model version | PostgreSQL | Control-plane truth |\n| Kafka record | Stream | Ordered transport within partition |",
        "workflow": "| Business workflow + decision | PostgreSQL | Invariant and audit truth |\n| Image/document evidence | Object storage | Immutable content truth |\n| Integration event | Outbox + bus | Reliable intent/transport |\n| Cache/analytics | Redis/warehouse | Derived and rebuildable |",
        "planning": "| Input snapshot | Object/lake storage | Immutable solver input |\n| Approved plan version | Plan store/PostgreSQL | Published schedule truth |\n| Disruption event | Event log | Ordered integration history |\n| KPI/dashboard | Warehouse/cache | Derived projection |",
        "notification": "| Notification intent/preference | PostgreSQL | Command and compliance truth |\n| Delivery attempt/receipt | Append history | Provider outcome evidence |\n| Queue message | Queue | Transport; may redeliver |\n| Template/quota cache | Redis | Derived versioned state |",
        "task": "| Task/attempt state | PostgreSQL | Authoritative state machine |\n| Payload/result bytes | Object storage | Versioned large data |\n| Queue message/lease | Queue | Scheduling transport |\n| Status cache | Redis | Rebuildable projection |",
        "realtime": "| Message + sequence | Durable log | Conversation history truth |\n| Membership/ACL | PostgreSQL | Authorization truth |\n| Presence/connection route | Redis/registry | Ephemeral lease |\n| Attachment | Object storage | Binary truth |",
    }
    return dedent(f'''\
    ### Diagram 2 — Request / Sequence Flow

    {mermaid_block(sequences[profile])}

    Flow đồng bộ chỉ giữ các bước cần cho user-visible result. Work dài, fan-out hoặc có thể replay đi qua durable queue/log. Mỗi command có operation ID; state transition dùng unique constraint hoặc expected version.

    ### Diagram 3 — Data Flow and Source of Truth

    {mermaid_block(data_flows[profile])}

    | Data | Source of Truth | Lý do |
    |---|---|---|
    {source_rows[profile]}

    “Source of truth” nghĩa là nơi quyết định authoritative state sau recovery. Cache, search/vector index và analytics là projection: có thể stale và phải rebuild được từ durable source + version metadata.

    ### Diagram 4 — Scaling Architecture

    ```mermaid
    flowchart TB
        Client --> GlobalLB["Global / regional load balancer"]
        GlobalLB --> CellA
        GlobalLB --> CellB
        subgraph CellA["Cell A: tenant / partition group"]
            APIA["API replicas"] --> CacheA[(Cache)]
            APIA --> DBA[(Primary + replicas)]
            APIA --> QueueA[(Partitioned queue)]
            QueueA --> WorkerA["Specialized workers"]
        end
        subgraph CellB["Cell B: independent blast radius"]
            APIB["API replicas"] --> DBB[(Primary + replicas)]
            APIB --> QueueB[(Partitioned queue)]
        end
    ```

    Cell/partition chỉ xuất hiện khi tenant/data/traffic đủ lớn hoặc cần blast-radius isolation. HPA/autoscaling bị cap bởi DB connection, provider quota, storage bandwidth và worker resource; queue age tốt hơn queue length khi task runtime khác nhau.

    ### Diagram 5 — Failure and Recovery Flow

    ```mermaid
    flowchart TD
        Request --> Dependency
        Dependency -->|timeout / unavailable| Timeout
        Timeout --> Classify{{"Safe and retryable?"}}
        Classify -->|yes, budget remains| Backoff["Backoff + full jitter"]
        Backoff --> Dependency
        Classify -->|no / circuit open| Degrade["Fallback / queue / fail fast"]
        Degrade --> Durable[(Record durable status)]
        Durable --> Reconcile["Replay / reconciliation"]
        Reconcile --> Verify["Verify user state and SLO"]
    ```

    Retry không được vượt end-to-end deadline hoặc tạo duplicate effect. Circuit breaker, bulkhead và rate limit giới hạn propagation; reconciliation xử lý outcome “unknown” mà synchronous retry không thể chứng minh.

    ### Diagram 6 — Observability Trace

    ```mermaid
    sequenceDiagram
        participant C as Client
        participant G as Gateway
        participant A as API
        participant D as Database / Cache
        participant Q as Queue
        participant W as Worker
        C->>G: traceparent + request
        G->>A: gateway span
        A->>D: dependency span + pool wait
        A->>Q: event with trace / operation ID
        Q->>W: async continuation span
        W->>D: state transition span
        Note over A,W: Metrics: RPS, p50/p95/p99, errors, saturation, queue age
    ```

    Log có `trace_id`, `operation_id`, tenant đã hash, version và typed error; không log token/PII/raw document mặc định. Alert dựa user SLI và multi-window burn rate, kết hợp queue age, pool wait, cache hit, DB/resource saturation.

    ### Architecture Evolution — Start Simple, Add Only for Measured Pain

    | Stage | Architecture | Khi nào đủ / vấn đề buộc thay đổi |
    |---|---|---|
    | **V1 — ~100 RPS** | 2 API instance, PostgreSQL, object storage nếu có binary; background worker đơn giản | Dễ deploy/debug. **Không** dùng Kafka, sharding hay nhiều microservice nếu vẫn đạt SLO/RTO. |
    | **V2 — ~5,000 RPS** | Load balancer, API scale ngang, Redis cho hot derived read, durable queue, worker pool, read replica cho stale read | Thêm vì cacheable read, burst/long work và deployment isolation đã được đo. Giữ global DB/pool budget. |
    | **V3 — 20,000+ RPS / large data** | Partition/cell theo tenant/key, specialized workers, event-driven projection, tiered storage và isolation quota | Chỉ thêm khi hot partition, write/connection/storage ceiling hoặc blast radius không còn đáp ứng SLO. |

    **Bottleneck gates:** trước mỗi bước, ghi metric trigger cụ thể—DB CPU/pool wait, cache hit, queue age, partition skew, provider quota hoặc cost/success. “Có thể scale” không phải lý do đủ để thêm component.

    ## Failure Scenarios

    | Failure | Detection | Immediate mitigation | Durable design |
    |---|---|---|---|
    | API instance down | readiness, 5xx, connection reset | LB loại instance, drain/restart | ≥2 AZ, stateless API, graceful shutdown |
    | Database down/failover | connect errors, replica/HA event | shed write, read-only/degraded mode | tested failover, backup restore, RPO/RTO |
    | Redis down | timeout, hit ratio collapse | circuit-open, stale/bounded fallback | DB protection, TTL jitter, cache warm plan |
    | Queue unavailable | publish error/outbox age | persist intent, pause noncritical producer | outbox, HA broker, replay runbook |
    | Worker down | oldest age/lease expiry | autoscale/restart, requeue safely | heartbeat, idempotency, DLQ |
    | Network timeout | dependency span/deadline | fail fast or bounded retry | propagated deadline, operation status |
    | Duplicate request | same idempotency key | return prior/in-progress result | atomic dedupe + payload hash |
    | Duplicate event | inbox unique conflict | ACK duplicate after verifying result | idempotent consumer + reconciliation |
    | Slow dependency | p99, saturation, circuit state | bulkhead, fallback, rate limit | capacity contract and load/fault tests |
    | Traffic spike / partial failure | SLO burn, queue/pool age | load shed, priority, degrade features | quota, cell isolation, pre-scale plan |

    ## Security Deep Dive

    - **Authentication:** OIDC/OAuth2 at edge; short-lived credential, issuer/audience validation and revocation/rotation plan.
    - **Authorization:** resource + action + tenant/ACL enforced server-side; admin/human override requires step-up and immutable audit.
    - **Input boundary:** schema/size/content-type validation, malware/archive-bomb protection and signed upload URL with narrow scope.
    - **Transport/storage:** TLS/mTLS where trust boundary requires, KMS-backed encryption, per-service IAM and secret manager—not secrets in image/log.
    - **Privacy:** data classification, PII redaction, retention/legal hold, regional residency and deletion propagated to derived indexes/backups policy.
    - **Abuse:** per-user/tenant/provider rate limit, quota, cost ceiling and anomaly signal; deny-by-default for cross-tenant access.

    ## How to explain this design in an interview

    1. **Clarify requirements:** core user journey, tenant/geography, correctness, latency/availability, retention/compliance và out-of-scope.
    2. **Estimate scale:** average/peak RPS, concurrency (`RPS × latency`), bytes/day, retention, worker/provider/GPU demand.
    3. **Start simple:** V1 với ít component nhất; chỉ rõ PostgreSQL/object store nào là source of truth.
    4. **Identify bottleneck:** dùng con số để chọn DB/cache/queue/partition deep dive; không liệt kê tool.
    5. **Evolve architecture:** V2/V3 giải quyết bottleneck cụ thể và nêu cost/coupling mới.
    6. **Discuss failure:** timeout, retry budget, idempotency, circuit/bulkhead, DLQ, degraded mode và reconciliation.
    7. **Discuss security/observability:** identity/tenant/PII, SLI, trace async và alert burn-rate.
    8. **Close with trade-offs:** assumption nào rủi ro nhất, metric nào khiến đổi design và bước tương lai nào chưa cần hôm nay.
    ''')


def system_design_doc(filename: str, d: dict[str, str]) -> str:
    q_basic, q_senior, answers, followups = question_sections(
        "11-system-design", filename, d["title"], f"{d['title']} là hệ thống để {d['goal']}."
    )
    deep_section = "\n" + system_design_deep_dive(filename, d)
    return dedent(f'''\
    # Design: {d["title"]}

    > Cách trình bày: clarify requirement → estimate → define invariant → draw → deep-dive bottleneck/failure → trade-off.

    ## 1. What is it?

    Thiết kế nền tảng **{d["title"]}** để {d["goal"]}. Scope phỏng vấn tập trung vào backend/control plane; thuật toán ML/optimization chi tiết nằm ngoài phạm vi.

    ## 2. Why does it matter?

    Bài toán kết hợp stateful workflow, dữ liệu lớn, partial failure và enterprise integration. Senior Engineer phải biến requirement mơ hồ thành SLO, capacity budget và ranh giới ownership có thể vận hành.

    ## 3. How does it work?

    ### Requirements

    - Làm rõ tenant, geography, retention, compliance, consistency và thao tác nào critical.
    - Source of truth phải durable; cache/projection có thể rebuild.
    - Mọi side effect có idempotency key, audit trail và reconciliation path.

    ### Functional Requirements

    - Core: {d["goal"]}.
    - Query trạng thái/history, quản lý version/configuration và quyền theo tenant.
    - Admin replay, manual override, export và audit nhưng phải authorization chặt.

    ### Non-functional Requirements

    - Availability mục tiêu 99.9–99.99% theo criticality; multi-AZ trước multi-region.
    - p95/p99 được định nghĩa riêng cho synchronous API và asynchronous completion.
    - Encryption in transit/at rest; RPO/RTO, retention và data residency có số cụ thể.

    ### Scale Estimation

    Assumption: {d["scale"]}. Từ peak traffic tính số instance theo **measured sustainable RPS × target utilization 60–70%**, không dùng benchmark laptop. Storage = ingest/day × retention × replication/compression; cộng index/WAL/headroom. Connection budget phải chia từ giới hạn database xuống pod/worker.

    ### API

    {d["api"]}. Write API trả resource/job ID ổn định; operation dài dùng `202 Accepted`. Cursor pagination thay offset cho history lớn. Error có machine-readable code, retryability và correlation ID.

    ### Data Model

    Entity chính: {d["entities"]}. Dùng immutable ID, `tenant_id`, version/ETag và timestamps; unique constraint bảo vệ business invariant. Audit event append-only, payload lớn tách khỏi OLTP row.

    ### High-level Architecture

    ```mermaid
    flowchart LR
    {d["nodes"]}
    ```

    ### Database

    {d["db"]}. Partition/shard theo access pattern đã đo; replica phục vụ stale-tolerant read. Schema migration expand/contract và online backfill có throttle.

    ### Cache

    {d["cache"]}. Dùng TTL jitter, single-flight và stale-if-error. Cache failure phải degrade có giới hạn; rate limit bảo vệ source khỏi miss storm.

    ### Message Queue

    {d["queue"]}. Delivery mặc định at-least-once; consumer idempotent, retry có backoff/jitter/budget, poison message vào DLQ và có runbook replay.

    ### Storage

    Object/blob lớn dùng object storage với checksum, versioning, lifecycle và signed URL. Metadata durable tách khỏi bytes; backup restore phải được diễn tập, không chỉ bật configuration.

    ### Scaling

    Stateless API scale ngang sau load balancer; partition worker theo locality/resource. Autoscale dùng queue age/lag cùng saturation và cap theo downstream capacity. Hot partition cần virtual shard hoặc tenant isolation.

    ### Failure Handling

    - Deadline truyền end-to-end; retry chỉ transient + idempotent, dùng exponential backoff/full jitter.
    - Circuit breaker/load shedding khi dependency suy yếu; fallback phải ghi rõ stale/degraded semantics.
    - Outbox xử lý dual write; reconciliation job sửa lost/stuck projection.
    - Đặc thù cần drill: {d["special"]}.

    ### Security

    OIDC/OAuth2 ở edge, authorization theo resource/tenant ở service; least privilege IAM, secret rotation, encryption, PII redaction và immutable audit. Upload/untrusted content cần content-type verification, malware scan và quota.

    ### Observability

    RED cho API, USE cho resource; queue age/lag, pool wait, saturation và business success. Trace mang `tenant_id` đã hash, job/message ID qua async boundary; tránh high-cardinality raw user ID. Alert theo multi-window SLO burn rate.

    ## 4. Example

    ```python
    from dataclasses import dataclass
    from uuid import UUID

    @dataclass(frozen=True)
    class Command:
        command_id: UUID
        tenant_id: UUID
        aggregate_id: UUID
        expected_version: int

    # Repository atomically enforces (tenant_id, command_id) uniqueness and
    # expected_version, then writes business state plus an outbox event.
    ```

    Hai constraint tách biệt: `command_id` chống duplicate; `expected_version` chống lost update.

    ## 5. Production Use Case

    Rollout theo cell/tenant, shadow traffic cho read path và canary cho write path. Trước launch cần load test có skew/hot key, dependency failure drill, restore test, capacity model, dashboard, alert, runbook và owner. Với **{d["title"]}**, review riêng: {d["special"]}.

    ## 6. Common Problems

    - Nhảy vào component trước khi chốt SLO, scale, consistency và source of truth.
    - Tuyên bố “exactly once” nhưng không nói scope hoặc external side effect.
    - Scale API mà bỏ qua database connection, hot partition và provider quota.
    - Queue không bound, retry vô hạn và DLQ không có owner/replay procedure.
    - Multi-region quá sớm, làm consistency/operation phức tạp hơn business cần.

    ## 7. Trade-offs

    | Decision | Chọn khi | Đánh đổi |
    |---|---|---|
    | Strong consistency | Money/ownership/invariant | Latency, availability khi partition |
    | Eventual consistency | Projection/feed/analytics | Stale UI, cần version/reconciliation |
    | Synchronous call | Cần kết quả tức thời, dependency tin cậy | Coupling, tail-latency amplification |
    | Queue/event | Work dài, burst hấp thụ được | Duplicate, lag, debugging khó hơn |
    | Single region multi-AZ | Latency/complexity vừa phải | Không chịu được region loss |
    | Active-active region | RTO thấp, global traffic | Conflict, cost và operational complexity |

    ### Bottlenecks

    Database connection/lock, hot key/partition, queue lag, object-store bandwidth, external quota và serialized coordinator. Xác nhận bằng trace/profile/load test; không tối ưu từ sơ đồ.

    ### Future Improvements

    Cell-based isolation, per-tenant quota, adaptive load shedding, tiered storage, automated reconciliation, chaos drill và cost-per-success dashboard. Chỉ thêm multi-region/sharding khi metric chứng minh giới hạn.

    {deep_section}

    ## 8. Interview Questions

    {q_basic}

    ## 9. Senior-level Questions

    {q_senior}

    ## 10. Short Answers

    {answers}

    **Design pitch 90 giây:** “Tôi chốt invariant/SLO, estimate peak, chọn durable source of truth, tách work dài qua queue, dùng idempotency + outbox, rồi deep-dive bottleneck lớn nhất. Tôi thiết kế degraded mode, observability và reconciliation trước khi nói multi-region.”

    ## 11. Follow-up Questions

    {followups}

    ## 12. Key Takeaways

    - Requirement và con số dẫn component choice; component không phải điểm bắt đầu.
    - Scale stateless tier dễ; state, connection budget, skew và failure recovery mới khó.
    - At-least-once + idempotency + reconciliation là baseline thực dụng.
    - Security, operability, cost và data lifecycle nằm trong design, không phải phụ lục.
    - Luôn nêu assumption, trade-off và tín hiệu khiến bạn đổi thiết kế.
    ''')


def main_readme() -> str:
    modules = [
        ("00-interview-roadmap", "Roadmap", "Kế hoạch 30/14 ngày, checklist và priority"),
        ("01-python-core", "Python Core", "Memory, object model, typing, generators"),
        ("02-python-concurrency", "Python Concurrency", "GIL, thread, process, AsyncIO"),
        ("03-fastapi", "FastAPI", "Lifecycle, DI, auth, WebSocket, performance"),
        ("04-database-postgresql", "PostgreSQL", "Index, planner, MVCC, transaction, scale"),
        ("05-sqlalchemy", "SQLAlchemy", "Session, loading, transaction và performance"),
        ("06-redis", "Redis", "Cache, lock, rate limit, persistence, failure"),
        ("07-celery", "Celery", "Delivery, retry, idempotency, operations"),
        ("08-api-design", "API Design", "REST, pagination, retry, security"),
        ("09-software-architecture", "Software Architecture", "DDD, modular monolith, microservices"),
        ("10-distributed-systems", "Distributed Systems", "Consistency, failure, saga, outbox"),
        ("11-system-design", "System Design", "Framework và 11 bài thiết kế production"),
        ("12-docker", "Docker", "Image, network, build và hardening"),
        ("13-kubernetes", "Kubernetes", "Workload, autoscale, rollout, troubleshoot"),
        ("14-cloud", "Cloud", "AWS compute, storage, network, architecture"),
        ("15-terraform-cicd", "Terraform & CI/CD", "IaC, state, deployment, rollback"),
        ("16-security", "Security", "OWASP, identity, secret, API protection"),
        ("17-performance-reliability", "Performance & Reliability", "Profiling, SLO, observability, incident"),
        ("18-ai-integration", "AI Integration", "LLM, RAG, vector DB, scale và quality"),
        ("19-coding-interview", "Coding Interview", "Pattern, structure và Python problems"),
        ("20-senior-scenarios", "Senior Scenarios", "11 sự cố production có framework"),
        ("21-behavioral", "Behavioral", "Leadership, conflict, incident và STAR"),
        ("22-mock-interview", "Mock Interview", "Question bank và full 110-minute mock"),
        ("23-cheatsheets", "Cheatsheets", "Review nhanh 1–2 giờ trước phỏng vấn"),
        ("24-references", "Technical References", "Nguồn chính thức để kiểm tra chi tiết thay đổi theo version"),
    ]
    rows = "\n".join(f"| [{name}]({folder}/README.md) | {desc} |" if (ROOT / folder / "README.md").exists() or folder in {"00-interview-roadmap", "11-system-design", "22-mock-interview", "23-cheatsheets"} else f"| [{name}]({folder}/{STRUCTURE.get(folder, ['README.md'])[0]}) | {desc} |" for folder, name, desc in modules)
    return dedent(f'''\
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
    {rows}

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
    ''')


def roadmap_files() -> dict[str, str]:
    return {
        "README.md": dedent('''
        # Interview Roadmap

        Chọn [30-day plan](30-day-plan.md) nếu còn ít nhất bốn tuần; chọn [14-day crash plan](14-day-crash-plan.md) nếu thời gian ngắn. Mỗi ngày dành 60% cho P0/P1, 20% nói answer thành tiếng, 20% làm scenario/mock.

        - [Priority Topics](priority-topics.md)
        - [30-day Plan](30-day-plan.md)
        - [14-day Crash Plan](14-day-crash-plan.md)
        - [Interview Checklist](interview-checklist.md)
        - [Repository Depth Audit](repository-audit.md)
        - [Main Dashboard](../README.md)
        '''),
        "priority-topics.md": dedent('''
        # Priority Topics

        ## P0 — MUST KNOW

        - Python memory/reference model; GIL; AsyncIO/event loop; CPU-vs-I/O-bound.
        - FastAPI request lifecycle, sync-vs-async endpoint, DI/session scope, authentication, error/timeout.
        - PostgreSQL B-tree/composite/partial index, `EXPLAIN ANALYZE BUFFERS`, transaction, isolation, MVCC, locks, pool budget.
        - Distributed system: idempotency, deadline/timeout, retry + jitter/budget, circuit breaker, outbox, at-least-once.
        - System Design framework, capacity estimation, cache/queue/database scaling, observability và failure handling.
        - Scenario: database high CPU, Redis down, duplicate task/message, high traffic, data consistency.

        **Exit criteria:** trả lời 2 phút/topic; giải 5 scenario theo evidence; thiết kế AI Chatbot và Warranty System trong 35 phút.

        ## P1 — VERY IMPORTANT

        - Redis cache patterns, stampede, eviction/persistence, Sentinel/Cluster.
        - Celery broker/ack/retry/idempotency/routing và production operations.
        - SQLAlchemy session/transaction/N+1/loading/async.
        - REST/versioning/pagination/rate limit/OAuth2/JWT/API security.
        - Docker multi-stage/non-root; Kubernetes requests/limits, probes, HPA, rollout/troubleshoot.
        - SLI/SLO, metrics/log/trace, load test, incident response.
        - RAG pipeline, embeddings/vector DB, streaming, LLM cost/quality/security.

        **Exit criteria:** giải thích trade-off và failure behavior, không chỉ định nghĩa.

        ## P2 — NICE TO KNOW

        - Python descriptors/advanced dunder; rare PostgreSQL index types.
        - Terraform module/state internals; cloud service mapping chi tiết.
        - Design pattern ít dùng; algorithm nâng cao ngoài pattern phổ biến.
        - ML mathematics; multi-region active-active trước khi requirement đòi hỏi.

        ## Quy tắc ưu tiên

        Khi thiếu thời gian: **P0 depth > P1 breadth > P2 recognition**. Một câu trả lời có invariant, metric, failure mode và production example đáng giá hơn danh sách nhiều tool.
        '''),
        "30-day-plan.md": make_plan(30),
        "14-day-crash-plan.md": make_plan(14),
        "interview-checklist.md": dedent('''
        # Interview Checklist

        ## 7 ngày trước

        - [ ] Chốt 6 STAR stories: impact, incident, conflict, failure, mentoring, ambiguous project.
        - [ ] Làm hai full System Design có timer và tự nghe recording.
        - [ ] Ôn P0 bằng active recall; đánh dấu gap, không đọc thụ động toàn bộ.
        - [ ] Chuẩn bị câu hỏi về product, ownership, architecture, on-call và success criteria.

        ## 24 giờ trước

        - [ ] Review [Last-day Review](../23-cheatsheets/last-day-review.md), không học domain mới.
        - [ ] Kiểm tra camera, mic, network, IDE/whiteboard và timezone.
        - [ ] In/ghi một trang assumptions, numbers, trade-off prompts.
        - [ ] Ngủ đủ; chuẩn bị nước và khoảng nghỉ.

        ## Trong technical interview

        - [ ] Clarify input/output, scale, SLO, consistency và out-of-scope.
        - [ ] Think aloud; nêu invariant trước implementation.
        - [ ] Đưa baseline đơn giản, rồi tối ưu theo bottleneck được chứng minh.
        - [ ] Chủ động nêu timeout, retry, idempotency, backpressure, observability, security.
        - [ ] Nếu không biết: nói phần chắc chắn, assumption và cách kiểm chứng.

        ## Trong behavioral interview

        - [ ] Nói “I” cho contribution, “we” cho team outcome.
        - [ ] Định lượng baseline/result; chỉ rõ decision và trade-off của bản thân.
        - [ ] Thừa nhận lỗi và learning; không đổ lỗi.
        - [ ] Kết thúc bằng cơ chế ngăn tái diễn hoặc thay đổi cách làm.

        ## Sau mỗi vòng

        - [ ] Ghi câu hỏi, assumption, chỗ bị follow-up và answer tốt hơn trong 15 phút.
        - [ ] Gửi follow-up đúng hẹn; không tiết lộ nội dung phỏng vấn mật.
        '''),
    }


def make_plan(days: int) -> str:
    if days == 30:
        blocks = [
            ("Ngày 1–5", "Python memory, GC, data model, typing; mỗi ngày 15 câu hỏi"),
            ("Ngày 6–9", "GIL, threading, multiprocessing, AsyncIO, cancellation và race"),
            ("Ngày 10–13", "FastAPI lifecycle/DI/auth/performance + SQLAlchemy session/N+1"),
            ("Ngày 14–18", "PostgreSQL index/planner/MVCC/transaction/locks/pool; đọc plan thật"),
            ("Ngày 19–21", "Redis + Celery; drill cache down, stampede, duplicate task"),
            ("Ngày 22–25", "Distributed Systems + Architecture + API Design"),
            ("Ngày 26–27", "System Design: AI Chatbot, Warranty, Document, Video"),
            ("Ngày 28", "Docker/Kubernetes/Cloud/Terraform/Security theo P1"),
            ("Ngày 29", "Coding patterns + 6 Behavioral stories"),
            ("Ngày 30", "Full mock 110 phút, review gap và nghỉ sớm"),
        ]
    else:
        blocks = [
            ("Ngày 1", "Python memory/GC/object model + GIL"),
            ("Ngày 2", "AsyncIO/event loop/task/cancellation + CPU-vs-I/O"),
            ("Ngày 3", "FastAPI lifecycle, sync-vs-async, DI, auth"),
            ("Ngày 4", "PostgreSQL index + EXPLAIN ANALYZE"),
            ("Ngày 5", "Transaction/MVCC/isolation/lock + pool"),
            ("Ngày 6", "Redis + failure/stampede/rate limit"),
            ("Ngày 7", "Celery + idempotency/retry/duplicate"),
            ("Ngày 8", "Distributed Systems: timeout/retry/outbox/saga"),
            ("Ngày 9", "System Design framework + capacity; AI Chatbot"),
            ("Ngày 10", "Warranty hoặc Document Processing design"),
            ("Ngày 11", "Docker/Kubernetes + performance/reliability"),
            ("Ngày 12", "AI integration + security + cloud recognition"),
            ("Ngày 13", "Coding timed set + Behavioral STAR drill"),
            ("Ngày 14", "Full mock, cheatsheet, fix top-three gaps"),
        ]
    checklist = "\n".join(f"- [ ] **{period}:** {work}. Output: one-page recall + trả lời thành tiếng + một scenario." for period, work in blocks)
    return dedent(f'''\
    # {days}-day {'Crash ' if days == 14 else ''}Plan

    ## Nhịp mỗi ngày

    1. 45 phút active recall; 60–90 phút deep study; 30 phút interview questions.
    2. 30 phút scenario/System Design hoặc coding có timer.
    3. Ghi `gap → correct model → production example`; review theo spaced repetition 1/3/7 ngày.

    ## Schedule

    {checklist}

    ## Exit criteria

    - P0: giải thích 2 phút không nhìn notes và chịu được ít nhất ba follow-up.
    - Scenario: mitigation trước diagnosis sâu; có metric/query, long-term fix và prevention.
    - System Design: estimate có đơn vị, API/data model, bottleneck, failure/security/observability.
    - Behavioral: mỗi story dưới 3 phút, có con số, decision cá nhân và learning.
    ''')


def index_readme(folder: str) -> str:
    label = CATEGORY[folder]["label"]
    names = [name for name in STRUCTURE[folder] if name != "README.md"]
    links = "\n".join(f"- [{title_from_name(name)}]({name})" for name in names)
    must_map: dict[str, list[str]] = {
        "01-python-core": ["python-memory-model.md", "gc-reference-counting.md", "mutable-immutable.md", "generators-iterators.md", "context-manager.md"],
        "02-python-concurrency": ["gil.md", "asyncio.md", "event-loop.md", "coroutine-task-future.md", "cpu-vs-io-bound.md"],
        "03-fastapi": ["architecture.md", "request-lifecycle.md", "sync-vs-async-endpoint.md", "dependency-injection.md", "performance.md"],
        "04-database-postgresql": ["index.md", "explain-analyze.md", "transaction.md", "isolation-level.md", "mvcc.md", "connection-pooling.md"],
        "05-sqlalchemy": ["session-lifecycle.md", "transaction.md", "n-plus-one.md", "relationship-loading.md", "async-sqlalchemy.md"],
        "06-redis": ["redis-internals.md", "caching.md", "cache-patterns.md", "persistence.md", "sentinel-cluster.md", "failure-scenarios.md"],
        "07-celery": ["architecture.md", "task-lifecycle.md", "retry.md", "idempotency.md", "exactly-once-myth.md", "production-problems.md"],
        "08-api-design": ["rest-api.md", "idempotency.md", "retry-timeout.md", "authentication-authorization.md", "api-security.md"],
        "10-distributed-systems": ["fundamentals.md", "idempotency.md", "retry.md", "timeout.md", "circuit-breaker.md", "outbox-pattern.md"],
        "11-system-design": ["system-design-framework.md", "capacity-estimation.md", "caching.md", "database-scaling.md", "observability.md"],
        "13-kubernetes": ["architecture.md", "resource-limit.md", "health-check.md", "hpa.md", "rolling-update.md", "troubleshooting.md"],
        "16-security": ["web-security.md", "owasp-top-10.md", "oauth2.md", "secrets-management.md", "api-security.md"],
        "17-performance-reliability": ["performance-debugging.md", "load-testing.md", "observability.md", "metrics-logging-tracing.md", "sli-slo-sla.md", "incident-debugging.md"],
        "18-ai-integration": ["ai-system-overview.md", "llm-basics-for-backend.md", "rag.md", "embeddings.md", "vector-database.md", "production-ai-system.md"],
    }
    must = [name for name in must_map.get(folder, names[: min(5, len(names))]) if name in names]
    nice = [name for name in names if name not in must]
    learning = " → ".join(f"[{title_from_name(name)}]({name})" for name in must)
    must_links = "\n".join(f"- [{title_from_name(name)}]({name})" for name in must)
    nice_links = "\n".join(f"- [{title_from_name(name)}]({name})" for name in nice[:8]) or "- Hoàn thiện các topic còn lại sau khi tự trả lời được P0."
    return dedent(f'''\
    # {label}

    Module này được học theo **Why → How → Internals → Flow → Failure → Trade-off → Production**. Không đọc alphabet; đi theo dependency dưới đây và tự vẽ lại diagram trước khi xem.

    ## Learning order

    {learning}

    ## Must know

    {must_links}

    ## Nice to know / second pass

    {nice_links}

    ## Recommended exercises

    1. Giải thích mỗi Must-know topic trong 2 phút, không nhìn note; interviewer hỏi “why?” ít nhất ba lần.
    2. Vẽ request/data/failure flow từ trí nhớ và đánh dấu source of truth, queue, timeout, retry, metric.
    3. Chọn một production incident liên quan **{label}**, trình bày mitigation trước root cause và long-term prevention.
    4. Load/fault test một assumption: bottleneck, duplicate, stale state hoặc dependency outage.

    ## All topics

    {links}

    [← Main Dashboard](../README.md)
    ''')


CHEATSHEETS: dict[str, str] = {
    "python-cheatsheet.md": dedent('''
    # Python Cheatsheet

    ## Object / Memory
    - Name → reference → object; assignment không copy. `is` identity, `==` equality.
    - CPython: refcount + cyclic GC; `del` bỏ reference. Resource dùng `with`, không chờ GC.
    - Mutable default argument tồn tại qua nhiều call. Copy shallow chia sẻ nested object.

    ## GIL / Concurrency
    - GIL: một thread chạy Python bytecode/interpreter; I/O và native extension có thể nhả GIL.
    - I/O-bound: AsyncIO hoặc thread. CPU-bound Python: process/native/worker queue.
    - Async là cooperative: blocking call chặn event loop. Có timeout, cancellation, semaphore.

    ## Senior Phrases
    - “I would first classify CPU vs I/O and measure event-loop lag.”
    - “Thread safety is not guaranteed by the GIL; compound operations can interleave.”
    - “I use context managers for deterministic cleanup and bound all concurrency.”
    '''),
    "fastapi-cheatsheet.md": dedent('''
    # FastAPI Cheatsheet

    - ASGI → middleware → route → dependency → validation → endpoint → serialization.
    - `async def`: event loop; `def`: thread pool. Async driver required end-to-end.
    - Session per request; transaction at service/use-case boundary; không giữ transaction qua network call.
    - Pydantic model là API contract, không expose ORM/entity trực tiếp.
    - CPU-heavy work → process/queue. Small best-effort post-response work mới dùng BackgroundTasks.
    - AuthN ở token/session; AuthZ tại resource/tenant. Redact secret/PII.
    - Đo RPS, p95/p99, error, loop lag, pool wait; timeout/retry/backpressure có budget.
    '''),
    "postgres-cheatsheet.md": dedent('''
    # PostgreSQL Cheatsheet

    ## Index
    - B-tree: `=`, range, `ORDER BY`; composite theo left prefix.
    - Partial: nhỏ hơn khi predicate ổn định. `INCLUDE`: covering, đổi write/storage.
    - GIN: array/JSONB/full text. GiST: range/geometry. BRIN: bảng rất lớn, correlated physical order.

    ## EXPLAIN
    - `EXPLAIN (ANALYZE, BUFFERS, WAL)` thực thi query.
    - Xem estimate vs actual, loops, rows removed, sort spill, shared hit/read.

    ## MVCC / Transaction
    - UPDATE tạo tuple version; long transaction giữ dead tuple → bloat.
    - Read Committed snapshot/statement; Repeatable Read snapshot/transaction; Serializable có abort → retry whole transaction.
    - Pool là admission control. Budget = replicas × workers × pool; pool không tăng DB capacity.
    '''),
    "redis-cheatsheet.md": dedent('''
    # Redis Cheatsheet

    - Cache-aside: miss → DB → set TTL. Dùng TTL jitter + single-flight + stale-if-error.
    - Hit ratio cao chưa đủ: xem command p99, evictions, memory fragmentation, hot key, replica lag.
    - TTL không phải invalidation correctness; version key/event invalidation khi cần.
    - Lock: unique owner token + atomic compare-delete; lease có thể hết hạn. Invariant mạnh dùng fencing/DB constraint.
    - Pub/Sub không durable; Streams có persistence/consumer group nhưng vẫn thiết kế duplicate.
    - Redis down: circuit break, bounded fallback, rate-limit DB, cache warming có kiểm soát.
    '''),
    "celery-cheatsheet.md": dedent('''
    # Celery Cheatsheet

    - Producer → broker → worker → result/backend (optional). Queue thường at-least-once.
    - Ack late + worker crash = redelivery. Ack early = có nguy cơ mất task.
    - Task idempotent: business key/unique constraint/inbox; lock đơn thuần không đủ.
    - Retry transient only; exponential backoff + jitter + max attempts/deadline. Poison task → DLQ/quarantine.
    - Đo queue depth **và oldest age**, runtime, retry/failure, worker saturation.
    - Route CPU/I/O/long task riêng; prefetch và visibility timeout phải hợp runtime.
    '''),
    "system-design-cheatsheet.md": dedent('''
    # System Design Cheatsheet

    1. Clarify user, core flow, out-of-scope, consistency, SLO, retention/compliance.
    2. Estimate peak RPS, concurrency (`RPS × latency`), bandwidth, storage/day × retention.
    3. API + data model + invariant/source of truth.
    4. Draw simple read/write flow; deep-dive largest bottleneck.
    5. Cache/queue/shard only khi access pattern/number yêu cầu.
    6. Failure: deadline, bounded retry+jitter, idempotency, backpressure, DLQ, reconciliation.
    7. Security, observability, cost, migration, rollback.

    Senior sentence: “My assumption is X; if metric Y crosses Z, I would move from A to B.”
    '''),
    "docker-cheatsheet.md": dedent('''
    # Docker Cheatsheet

    - Image immutable layers; container = image + writable layer + process isolation.
    - Multi-stage build; pinned digest; small runtime; non-root; read-only FS khi có thể.
    - `.dockerignore`; copy dependency manifest trước để tận dụng cache; không bake secret.
    - One main concern/process; stdout/stderr; graceful SIGTERM; health semantics rõ.
    - Volume cho persistent/externalized data; container filesystem là ephemeral.
    - Scan/sign/SBOM; rebuild để nhận security patch, không chỉ `apt upgrade` lúc start.
    '''),
    "kubernetes-cheatsheet.md": dedent('''
    # Kubernetes Cheatsheet

    - Deployment quản ReplicaSet/Pod; Service tạo stable discovery; Ingress/Gateway route L7.
    - Request dùng scheduling/HPA denominator; CPU limit có throttling, memory limit có OOMKill.
    - Readiness: nhận traffic? Liveness: process cần restart? Startup: app chưa khởi động xong?
    - HPA scale compute, không scale DB capacity; queue age tốt hơn CPU cho worker.
    - Rolling update cần maxSurge/maxUnavailable, PDB, readiness và graceful termination.
    - Debug: event → pod status/restart → logs previous → resource/throttle → endpoints/network/DNS.
    '''),
    "last-day-review.md": dedent('''
    # Last-day Review (60–120 phút)

    ## 0–20 phút: Python / FastAPI
    - GIL không cấm concurrency; CPU Python → process, I/O → async/thread.
    - Blocking trong async endpoint chặn loop; bound concurrency, deadline/cancel.
    - Request/session lifecycle; transaction boundary; pool budget.

    ## 20–40 phút: PostgreSQL / Redis / Celery
    - Index theo predicate/order/selectivity; đọc actual rows/loops/buffers.
    - MVCC + long transaction + vacuum/bloat; isolation theo invariant.
    - Cache stampede/fallback; task duplicate → idempotency, not “exactly once”.

    ## 40–65 phút: Distributed / System Design
    - Deadline → timeout từng hop; retry transient + backoff/jitter/budget.
    - Outbox cho dual write; consumer idempotent; reconciliation.
    - Clarify → estimate → API/data → architecture → failure/security/observability → trade-off.

    ## 65–80 phút: Kubernetes / Reliability / AI
    - Request/limit, probes, HPA vs downstream cap, rolling rollback.
    - SLI/SLO/error budget; metrics + logs + traces; mitigation trước RCA.
    - RAG: ingest/chunk/embed → retrieve/filter/rerank → prompt/cite; đo recall và groundedness.

    ## 80–100 phút: Story / Mental reset
    - 6 STAR story có con số, decision, conflict, learning.
    - Chuẩn bị câu hỏi cho interviewer. Không nhồi topic mới; ngủ và giữ nhịp nói chậm.
    '''),
}


MOCK_DOMAINS: dict[str, list[str]] = {
    "python-interview.md": ["memory/reference counting", "GIL", "AsyncIO cancellation", "thread vs process", "typing/runtime"],
    "backend-interview.md": ["FastAPI lifecycle", "API idempotency", "WebSocket", "Celery delivery", "rate limiting"],
    "database-interview.md": ["composite index", "EXPLAIN ANALYZE", "MVCC", "isolation/lock", "pool budget"],
    "system-design-interview.md": ["capacity estimation", "AI Chatbot", "Warranty System", "failure handling", "observability"],
    "devops-interview.md": ["Docker hardening", "Kubernetes probes", "HPA", "Terraform state", "safe rollout"],
    "behavioral-interview.md": ["technical leadership", "incident ownership", "conflict", "mentoring", "failure/learning"],
}


def mock_pack(filename: str, topics: list[str]) -> str:
    title = title_from_name(filename)
    blocks = []
    for i, topic in enumerate(topics, 1):
        blocks.append(dedent(f'''
        ## Question {i}: {topic}

        Explain **{topic}** with one internal mechanism, one trade-off and one production failure. Then handle this follow-up: what changes at 20,000 RPS?

        <details>
        <summary>Answer rubric</summary>

        A strong answer states the invariant and boundary, explains the mechanism rather than naming a tool, quantifies with a relevant metric, and covers timeout/overload/recovery. It should include a concrete production example and say when a simpler alternative is better.

        </details>
        '''))
    return dedent(f'''\
    # {title}

    Thời lượng: 45–60 phút. Không mở phần Answer trước khi hoàn tất câu trả lời thành tiếng. Chấm 0–3 cho: correctness, depth, trade-off, production evidence và communication.

    {''.join(blocks)}

    ## Debrief

    - Câu nào chỉ có definition mà thiếu mechanism/trade-off?
    - Assumption nào không nói ra? Metric nào có thể kiểm chứng?
    - Failure mode, rollback hoặc reconciliation nào bị bỏ sót?
    ''')


def full_mock() -> str:
    return dedent('''
    # Full Mock Interview — 110 Minutes

    **Luật:** dùng timer; hỏi clarification; think aloud; không mở Answer khi đang làm. Chấm mỗi phần 1–4: correctness, depth, trade-off, production judgment, communication.

    ## 0–10 min — Introduction

    ### Question

    Give me a two-minute overview of your background and the backend system where you had the strongest technical impact. What changed because of your decision?

    <details><summary>Answer rubric</summary>

    Role/scope ngắn; baseline định lượng; decision của cá nhân; trade-off; outcome và relevance với role. Tránh kể chronology dài.
    </details>

    ## 10–30 min — Python

    ### Question 1

    Explain the CPython memory model, reference counting, cyclic GC, and one real memory-retention incident.

    <details><summary>Answer</summary>

    Name giữ reference; refcount về 0 thường reclaim ngay; cyclic GC tìm container cycle; `del` không đảm bảo free nếu còn reference. Resource dùng context manager. Điều tra bằng RSS/heap/tracemalloc/object growth; phân biệt leak với allocator fragmentation/cache.
    </details>

    ### Question 2

    Does the GIL mean Python cannot handle concurrent requests? Choose between threads, AsyncIO, and processes for three different workloads.

    <details><summary>Answer</summary>

    GIL giới hạn Python bytecode parallel trong một CPython interpreter, không cấm I/O concurrency. AsyncIO cho nhiều non-blocking I/O; thread cho blocking I/O/library sync có bound; process/native cho CPU Python, tính serialization/startup cost.
    </details>

    ### Question 3

    What happens when CPU-heavy code runs inside a FastAPI `async def` endpoint? How do you prove and fix it?

    <details><summary>Answer</summary>

    Nó chặn event loop, tăng loop lag và tail latency cho request khác. Dùng trace/profile/load test; offload process/queue/native, bound concurrency; scale worker chỉ sau khi hiểu bottleneck.
    </details>

    ## 30–50 min — Backend / Database

    ### Question 4

    A PostgreSQL table has 500 million warranty records. Design indexes for “latest claims by vehicle” and explain write cost and verification.

    <details><summary>Answer</summary>

    Access path gợi ý `(vehicle_id, created_at DESC) INCLUDE (status...)`; partial index cho active claim nếu predicate ổn định. Xem selectivity/size/write amplification. Verify `EXPLAIN (ANALYZE, BUFFERS)` với distribution thật, estimate vs actual, loops và I/O.
    </details>

    ### Question 5

    Two requests create the same claim. Show an idempotency design that remains correct across timeouts and retries.

    <details><summary>Answer</summary>

    Scope key theo tenant; hash canonical payload; atomically claim bằng unique constraint cùng business transaction; duplicate running/completed có semantics; cùng key khác payload reject; TTL dựa business window. External side effect cần provider key/inbox và reconciliation.
    </details>

    ### Question 6

    Your API scales from 20 to 200 pods. Why might the database fail even if every pod is healthy?

    <details><summary>Answer</summary>

    Connection explosion = pod × worker × pool, cùng query/lock/IO amplification. Đặt global connection/admission budget, pool nhỏ/PgBouncer, backpressure, cache/read replica phù hợp và cap HPA theo downstream capacity.
    </details>

    ## 50–80 min — System Design

    ### Question 7

    Design a multi-tenant AI Chatbot Platform for one million daily active users. It must use private documents, stream answers, cite sources, enforce document ACLs, and tolerate an LLM provider outage.

    Cover requirements, estimation, API, data model, ingestion/RAG flow, cache/queue, scaling, security, failure behavior, observability, cost and trade-offs.

    <details><summary>Answer</summary>

    Strong path: clarify SLO/quality/privacy → estimate peak/tokens/storage → conversation/message/document/chunk model → async versioned ingestion → ACL-aware hybrid retrieval + rerank → orchestrator with token/deadline budget → SSE/cancel. PostgreSQL metadata, object store, vector index, queue for ingestion/eval. Provider bulkhead/circuit/fallback, rate limit, semantic cache carefully scoped. Measure TTFT, p99, retrieval recall, groundedness, cost/success; defend prompt injection/data exfiltration; reconciliation and model/version rollout.
    </details>

    ## 80–95 min — Production Scenario

    ### Question 8

    In ten minutes API latency rises from 100 ms to 3 s. App CPU is normal; PostgreSQL CPU is 95%. Walk through your response.

    <details><summary>Answer</summary>

    Confirm impact/SLO and freeze risky rollout; compare deploy/traffic. Check DB connections, active queries/waits/locks, top query time/calls, buffer/IO, replica lag and pool wait. Capture representative plan safely (`EXPLAIN ANALYZE` read query or transaction rollback); compare estimate/actual/index/bloat/stats. Immediate: shed/rate-limit, kill pathological query carefully, rollback, reduce fan-out/cache safe read. Long-term: query/index/schema fix, stats/vacuum, capacity test, alert and regression guard.
    </details>

    ### Question 9

    Redis becomes unavailable and Celery redelivers thousands of tasks. Prevent a cache-miss storm and duplicate business effects.

    <details><summary>Answer</summary>

    Circuit-break Redis, bounded fallback/stale cache, rate-limit/coalesce miss, protect DB and warm gradually. Pause/drain producer/consumer as appropriate. Task effect idempotent qua unique business key/inbox; retry jitter/budget; reconcile external effects. Redis lock alone không tạo exactly-once.
    </details>

    ## 95–105 min — Behavioral

    ### Question 10

    Tell me about a high-severity incident where your initial hypothesis was wrong. How did you lead, communicate, and improve the system?

    <details><summary>Answer rubric</summary>

    STAR: impact/timeline rõ; mitigation trước ego; hypothesis dựa evidence và cách đổi hướng; role/communication; result định lượng; blameless learning, action owner và prevention verified.
    </details>

    ## 105–110 min — Candidate Questions

    - What production outcome defines success in the first six months?
    - Which architectural constraint currently limits the team most?
    - How are design decisions, on-call ownership, and incident learning shared?

    ## Scorecard

    | Dimension | 1 | 2 | 3 | 4 |
    |---|---|---|---|---|
    | Correctness | Major gaps | Mostly basic | Correct + edge cases | Precise + teaches |
    | Senior depth | Definitions | Some internals | Invariant/failure/trade-off | Cross-system judgment |
    | Production | Happy path | Names tools | Metrics/mitigation/recovery | Prevents recurrence |
    | Communication | Unstructured | Needs prompts | Clear assumptions | Concise, adaptive, leads |

    **Hire-ready signal:** không cần hoàn hảo mọi chi tiết; cần reasoning có cấu trúc, sửa assumption khi có evidence và chủ động ownership production.
    ''')


TOP_50_QUESTIONS: list[tuple[str, str, str]] = [
    ("Why does CPython have a GIL, and what changes in a free-threaded build?", "Phân biệt language với CPython; runtime state/refcount, I/O release, C extension compatibility và synchronization vẫn cần.", "Does the GIL make compound operations thread-safe? When do threads still help?"),
    ("What actually happens when a Python reference count reaches zero?", "Deallocation/refcount cascading trong CPython; cycle cần GC; `del` chỉ bỏ binding; external resource dùng deterministic cleanup.", "What retains an object after a request ends? Why can RSS stay high after objects are freed?"),
    ("Why does CPython need a cyclic garbage collector in addition to reference counting?", "Cycle giữ refcount > 0; tracked containers/generational collection; version-dependent policy và GC pause/retention trade-off.", "What objects are tracked? When would disabling GC be reasonable?"),
    ("What does `await` do internally?", "Coroutine yields awaitable/Future; Task registers continuation; loop resumes on completion. `await` không tạo thread và có thể không yield.", "How does cancellation enter a coroutine? What if the awaited function blocks?"),
    ("How does an event loop know that a socket is ready?", "Non-blocking FD + OS readiness mechanism như epoll/kqueue/IOCP; callback vào ready queue; implementation depends on platform/loop.", "What is event-loop lag? How would you measure it?"),
    ("Why is CPU-heavy work dangerous inside an async endpoint?", "Giữ event-loop thread/GIL-enabled bytecode, trì hoãn socket/timer/cancellation; process/native/queue và bounded concurrency.", "Would adding more Uvicorn workers fix it? What happens to DB connections?"),
    ("When would threads outperform AsyncIO, and when would processes outperform threads?", "Blocking library/I/O với thread; high fan-out async-compatible I/O với AsyncIO; pure Python CPU với process, cân nhắc IPC/memory/startup.", "How would you benchmark using production-like workload?"),
    ("How can a race condition happen even with the GIL?", "Invariant nhiều bytecode/read-modify-write, C calls release GIL, I/O interleaving; lock/atomic DB operation/immutability.", "Which built-in operations are implementation details rather than guarantees?"),
    ("Walk me through a FastAPI request from the socket to the response.", "Uvicorn → ASGI scope/receive/send → middleware → routing → DI → Pydantic → endpoint → serialization/cleanup.", "Where are sync dependencies executed? When is a yielded dependency cleaned up?"),
    ("What happens if a FastAPI `async def` endpoint calls `requests.get()`?", "Utility sync call chạy ngay trên loop; blocking stalls all connections in that worker; use async client or bounded offload.", "How would traces and loop-lag metrics prove this?"),
    ("How do worker count, thread pool, and DB pool interact in FastAPI?", "Mỗi process có loop/thread/pool; total connection multiplication; pool wait/admission; scaling API có thể overload DB.", "Build a connection budget for 100 pods and a 500-connection database."),
    ("Why can dependency injection create hidden production cost?", "Graph resolution, sync dependency offload, resource scope, duplicate network calls và over-broad transaction; explicit boundary/telemetry.", "Which dependencies should be cached per request?"),
    ("Why can adding a PostgreSQL index make writes slower?", "B-tree maintenance, page split, WAL, cache footprint, vacuum/bloat; every INSERT/UPDATE/DELETE touches relevant indexes.", "When is a partial or covering index worth the cost?"),
    ("How does a PostgreSQL B-tree find a heap row?", "Root/internal/leaf pages, index tuple/key/TID, heap visibility check; index-only scan + visibility map.", "Why might a B-tree index still not be chosen?"),
    ("How does MVCC avoid blocking readers and writers?", "Tuple versions, xmin/xmax, snapshot visibility; writer creates new version, reader sees snapshot; conflict vẫn có ở writer/lock.", "How do long transactions cause bloat and vacuum problems?"),
    ("What is the difference between Read Committed, Repeatable Read, and Serializable in PostgreSQL?", "Snapshot scope/anomalies, PostgreSQL SSI và whole-transaction retry; chọn theo invariant.", "Show a write-skew or lost-update example and fix it."),
    ("How do you read `EXPLAIN (ANALYZE, BUFFERS)`?", "Node deepest mismatch, estimate vs actual, loops, rows removed, join/scan, spill/temp, shared hit/read và DML safety.", "Why can a locally fast plan be slow under production concurrency?"),
    ("When does PostgreSQL choose Seq Scan, Index Scan, Index Only Scan, or Bitmap Heap Scan?", "Selectivity, heap/page locality, visibility map, random vs sequential cost, multiple predicates.", "How would stale statistics change the choice?"),
    ("Compare Nested Loop, Hash Join, and Merge Join.", "Input size/order/index/memory; row-estimate error; spill/batch; nested loop amplification.", "Which plan symptom suggests the join type is wrong because of misestimation?"),
    ("Why can a database connection pool become a bottleneck?", "Bounded admission; request waits; long transaction/query holds slot. Oversized pool shifts queue to DB and adds contention.", "Which metrics separate query latency from pool wait?"),
    ("How would you index a 500-million-row warranty table?", "Access patterns/selectivity/composite order/partial/covering/partition, write/WAL/storage cost; representative EXPLAIN.", "How do data skew and retention change the design?"),
    ("What causes a PostgreSQL deadlock and how do you fix it?", "Cycle in wait graph, victim abort; consistent lock order, shorter transaction, index fewer rows, retry whole tx with jitter.", "How is a deadlock different from a long lock wait?"),
    ("Why is Redis fast beyond simply storing data in RAM?", "Specialized encodings/data structures, mostly serialized command execution, event loop và low round trips; O(N)/big key blocks others.", "How do I/O threads change—and not change—the model?"),
    ("What happens when Redis disappears during a traffic spike?", "Circuit, cache miss storm, DB overload, bounded stale fallback, rate limit/coalescing, jittered reconnect/warm-up.", "Which endpoints fail open versus fail closed?"),
    ("How do TTL, eviction, and expiration differ in Redis?", "TTL semantic lifetime; passive/active expiry; eviction under maxmemory policy; none guarantee business invalidation.", "How do synchronized expirations create an outage?"),
    ("When is a Redis distributed lock unsafe?", "Lease expiry/pause/partition/failover; stale owner writes. Owner token compare-delete, fencing, DB constraint; safety vs liveness.", "Would Redlock protect a financial invariant? What remains at the storage boundary?"),
    ("How do Redis Sentinel and Redis Cluster differ?", "Sentinel HA non-sharded; Cluster 16,384 slots/sharding/failover; redirects, cross-slot, hot key, async replication loss window.", "How does a client behave during reshard/failover?"),
    ("Why can a Celery task run twice?", "Worker commit then crash before ACK, lease/visibility timeout, producer retry/failover; delivery/effect scopes.", "Compare early ACK and late ACK failure windows."),
    ("How do you make a Celery task idempotent?", "Business key, unique constraint/inbox, conditional transition, provider idempotency/ledger, return prior result, reconcile.", "Why is a Redis lock not sufficient?"),
    ("How do prefetch and task routing affect Celery fairness?", "Reserved local tasks, long-vs-short head-of-line, queue/resource/SLO isolation, throughput vs fairness.", "Which metric is better than queue length for variable runtime tasks?"),
    ("Why is exactly-once processing difficult?", "Ack/commit crash window, external effect outside broker transaction; define scope; at-least-once + idempotency + reconciliation.", "Can Kafka exactly-once semantics make an email send exactly once?"),
    ("Why is retry dangerous?", "Load amplification, synchronized retry, deadline exhaustion, duplicate non-idempotent effect; classify transient, backoff/full jitter/budget/circuit.", "Which HTTP/DB errors are retryable and at what layer?"),
    ("How should timeouts be budgeted across a service call chain?", "End-to-end deadline minus queue/serialization, connect/read/pool timeouts, child shorter than parent, cancellation propagation.", "What if the server commits after the caller times out?"),
    ("How does a circuit breaker work internally?", "Closed/Open/Half-Open, rolling failure/slow-call threshold, cooldown/probes; scope/bulkhead/fallback.", "How can a badly scoped breaker increase blast radius?"),
    ("How does the transactional outbox solve the dual-write problem?", "Business row + outbox same DB tx; relay poll/CDC; publish duplicate possible; consumer dedupe/monitor outbox age.", "What if the relay publishes and crashes before marking the row?"),
    ("Compare choreography and orchestration for a Saga.", "Visibility/coupling/coordinator; compensation failure/idempotency, no isolation, irreversible step/human review.", "When is a local transaction better than a Saga?"),
    ("How would you prevent duplicate payment or warranty claim requests?", "Tenant-scoped idempotency key + canonical payload hash + atomic business write/response; external provider key and ledger.", "What TTL is safe, and what if the duplicate arrives after TTL?"),
    ("What is eventual consistency, and how do you make it acceptable to users?", "Staleness window, version/cursor/read-your-write/session semantics, status projection, reconciliation and transparent UI.", "How do you measure convergence time?"),
    ("What does CAP theorem actually say during a network partition?", "For replicated operation under partition choose availability response vs consistency/linearizability; not a database ranking and not normal-state latency.", "Can different operations choose differently?"),
    ("How would you identify whether latency comes from application, database, or network?", "End-to-end trace + queue/service time, loop/pool wait, DB wait/plan, DNS/connect/TLS, RED/USE baseline.", "What evidence would make you stop scaling application pods?"),
    ("How do you design graceful degradation?", "Prioritize critical journey, stale/read-only/queued/fail-fast semantics, circuit/bulkhead/load shed, explicit user status and recovery reconciliation.", "Which data may be stale, and for how long?"),
    ("How do SLI, SLO, SLA, and error budgets change engineering decisions?", "User-visible good/valid events, internal target vs contract, burn-rate, release/risk trade-off.", "Why is average availability or latency insufficient?"),
    ("What should a production trace contain across an async queue?", "Trace context/links, operation/message ID, producer/consumer spans, queue delay vs processing, version/tenant safe tags.", "How do you avoid high-cardinality telemetry?"),
    ("Why can Kubernetes HPA make an outage worse?", "Scale API based CPU while DB/provider saturated; startup lag, request denominator, reconnect storm. Custom queue age and downstream cap.", "How do stabilization and readiness affect scaling?"),
    ("Explain Kubernetes CPU requests, CPU limits, and memory limits under load.", "Scheduler uses requests; CPU limit throttles; memory limit may OOM; HPA utilization denominator; workload-dependent limit policy.", "Why can p99 be bad when node CPU looks free?"),
    ("How do you deploy a database-dependent change without downtime?", "Expand/contract schema, backward-compatible app, online index/backfill throttle/checkpoint, dual-read compare, canary and rollback.", "What makes a migration irreversible?"),
    ("How would you secure a multi-tenant backend beyond validating JWTs?", "Resource-level authorization, tenant context isolation, DB/query guard, IAM/secret, rate quota, audit, PII encryption/redaction.", "How would you test cross-tenant access systematically?"),
    ("How does a RAG request flow from user query to cited answer?", "Auth/ACL, embed/hybrid retrieve, rerank, token pack, prompt/model, citation/abstention; version and metrics.", "How do you distinguish retrieval failure from generation failure?"),
    ("What is the source of truth in an AI system with PostgreSQL, S3, a vector DB, and Redis?", "S3 binary, PG metadata/ACL/workflow, vector derived index, Redis cache; rebuild/version/delete propagation.", "What happens during an embedding model migration?"),
    ("How do you scale an API from 1,000 to 20,000 RPS without overloading PostgreSQL?", "Measure sustainable worker, async/nonblocking, LB/pods, global pool budget, cache, replicas for stale read, queue, HPA cap, rate limit/load shed.", "Which component would you add first at 100 RPS, and which would you explicitly avoid?"),
]


def top_50_questions_doc() -> str:
    sections = []
    for number, (question, focus, followup) in enumerate(TOP_50_QUESTIONS, 1):
        sections.append(dedent(f'''
        ### {number}. {question}

        **What a senior answer should cover:** {focus}

        **Likely follow-up:** {followup}
        '''))
    return dedent(f'''\
    # Top 50 Senior Backend Interview Questions

    Dùng như active-recall bank. Trả lời câu chính trong 90–120 giây theo **definition → mechanism → trade-off → production evidence**; sau đó trả lời follow-up mà không nhìn note.

    {''.join(sections)}

    ## Self-scoring

    - **0:** chỉ biết keyword hoặc sai mechanism.
    - **1:** definition đúng nhưng thiếu internals/failure.
    - **2:** có mechanism, trade-off và ví dụ production.
    - **3:** định lượng, nói rõ assumption/version, degraded mode, observability và alternative đơn giản hơn.
    ''')


SYSTEM_DESIGN_30: list[tuple[str, str, str, str, str, str]] = [
    ("AI Chatbot Platform", "tenant, private docs, citations, streaming, quality SLO", "ACL-aware RAG and probabilistic quality", "LLM quota/TTFT and vector recall", "PG metadata + object/vector derived index + orchestrator", "How do you survive provider outage and prompt injection?"),
    ("Intelligent Document Processing", "file types/size, OCR accuracy, review, retention", "versioned multi-stage workflow", "large file/GPU/OCR queue age", "pre-signed upload + object truth + idempotent stage queue", "How do you retry one failed page without duplicating the job?"),
    ("Video Analytics Platform", "camera count/bitrate, alert latency, retention", "continuous ingest and GPU backpressure", "network/GPU/partition skew/storage", "edge segment + Kafka by camera + GPU pools + event store", "When do you sample/drop frames, and how is evidence preserved?"),
    ("Vehicle Inspection Platform", "station/offline mode, media, AI + human decision", "evidence immutability and auditable workflow", "upload bandwidth/AI queue/human review", "PG workflow + object evidence + outbox + review", "How do you handle model disagreement or station reconnect?"),
    ("Vehicle Warranty System", "eligibility, claim, settlement, policy versions", "money invariant and temporal rules", "500M history/query/enterprise integration", "PG claim truth + versioned rules + ledger + outbox", "How do you prevent duplicate claims and reconcile payment?"),
    ("Manufacturing Production Planning", "plants/lines/BOM/demand/solver latency", "consistent immutable planning snapshot", "solver compute/stale inputs/hot plant", "lake snapshot + workflow + solver + versioned plan publish", "What happens if ERP changes while solving?"),
    ("Real-time Chat", "DM/group, ordering, presence, offline sync", "ordering scope and multi-device fan-out", "hot group/connections/fan-out", "WebSocket gateway + partitioned log + broker + history", "How do clients resume without missing or duplicating messages?"),
    ("Notification System", "channels, priority, preference, campaign", "fan-out with provider quota/compliance", "provider throttling/large campaign", "intent DB + outbox + channel queues + receipt ledger", "How do transactional alerts bypass marketing backlog?"),
    ("Distributed File Processing", "file size/stages/progress/replay", "resumable upload and stage idempotency", "bandwidth/transform workers/orphan artifact", "object bytes + job DB + stage queues + checksums", "How do you detect and clean partial artifacts?"),
    ("Task Processing Platform", "runtime/resource class/priority/cancel", "lease, fairness, at-least-once state", "long task/starvation/noisy tenant", "task DB + outbox + scheduler + resource queues + result store", "What does cancel mean during an external side effect?"),
    ("API Rate Limiter", "identity/scope/burst/global accuracy", "distributed counters and fail-open/closed", "hot identity/Redis outage/clock", "gateway token bucket + local shield + Redis atomic update", "How do login and catalog use different failure policy?"),
    ("URL Shortener", "read/write ratio, custom alias, expiry", "unique ID and hot redirects", "cache miss/abuse/hot key", "ID service + PG/KV truth + CDN/cache", "How do you prevent enumeration and malicious links?"),
    ("Search Autocomplete", "language/prefix/freshness/personalization", "low-latency ranking and index refresh", "hot prefix/index memory", "offline trie/index build + online cache/ranker", "How do you publish a new index atomically?"),
    ("Metrics Monitoring Platform", "cardinality, scrape/push, retention, query", "high-volume time-series ingest", "cardinality/storage/query fan-out", "ingest shards + WAL + TSDB + downsampling", "How do you prevent one tenant from exploding cardinality?"),
    ("Distributed Log Service", "ordering/durability/retention/consumer", "partition leadership and replication", "hot partition/disk/network", "partitioned append log + replicas + consumer offsets", "What acknowledgement level meets the durability SLO?"),
    ("Payment Processing", "authorize/capture/refund/currency/ledger", "idempotent money movement and audit", "provider timeout/ledger contention", "API + double-entry ledger + outbox + provider adapter", "What if provider succeeds but your response times out?"),
    ("Inventory Reservation", "stock unit/warehouse/expiry/oversell", "concurrent reservation invariant", "hot SKU/lock contention", "atomic DB counter/reservation + expiry events", "How do you release expired reservations exactly enough?"),
    ("Order Management", "cart/order/payment/shipment/cancel", "cross-domain Saga and user-visible state", "payment/inventory partial failure", "order state machine + outbox + orchestrated Saga", "Which step is irreversible and how do you compensate?"),
    ("Audit Logging", "events/tamper/retention/search/privacy", "immutable complete evidence", "write volume/index/retention", "append log + immutable object archive + search projection", "How do you prove logs were not altered?"),
    ("Feature Flag Service", "targeting/consistency/SDK/offline", "safe low-latency evaluation", "config fan-out/stale SDK/cache", "versioned config truth + streaming distribution + local evaluation", "How do you prevent a flag service outage from taking down apps?"),
    ("Configuration Service", "secret/non-secret, version, rollout, scope", "consistent versioned distribution", "watch fan-out/bad config", "config DB + signed version + watch/cache + rollback", "How do you canary a configuration, not just code?"),
    ("Webhook Delivery", "endpoint, signing, retry, ordering", "untrusted slow consumers", "retry backlog/one bad tenant", "event DB + tenant queues + signed sender + attempt ledger", "How do consumers dedupe and verify authenticity?"),
    ("IoT Telemetry Platform", "device count/frequency/commands/offline", "device identity and high-volume ingest", "connection/partition/storage", "MQTT gateway + stream + time-series/lake + command service", "How do you handle out-of-order device timestamps?"),
    ("Fraud Detection Pipeline", "online decision/feature freshness/review", "low latency with explainable evidence", "feature store/model quota/false positive", "event stream + online features + model + case workflow", "How do you fall back when the model service is unavailable?"),
    ("Report Generation", "template/data size/schedule/download", "consistent snapshot and long-running work", "DB impact/render CPU/storage", "job DB + query snapshot + worker + object artifact", "How do you avoid reports overloading the primary DB?"),
    ("Data Export / GDPR Deletion", "scope/format/deadline/derived copies", "complete lineage across systems", "large scan/downstream deletion", "request workflow + inventory + per-store workers + audit", "How do you verify vector/cache/backup handling?"),
    ("Distributed Scheduler", "cron/one-off/timezone/misfire", "single logical firing under failover", "clock/leader/hot schedule", "schedule DB + lease/leader + due-time index + task queue", "What does exactly-once schedule execution mean?"),
    ("Multi-tenant SaaS Backend", "isolation/customization/quota/region", "tenant boundary and noisy-neighbor control", "hot tenant/pool/storage", "tenant context + shared/cell data plane + quota + audit", "When do you move from shared schema to cell/database isolation?"),
    ("Content Moderation Pipeline", "modalities/latency/appeal/policy version", "policy/model/human consistency", "burst/GPU/review queue", "upload + scan/model queue + decision state + review", "How do you re-evaluate old content after policy changes?"),
    ("Experimentation Platform", "assignment/metrics/guardrail/exposure", "stable bucketing and unbiased events", "event quality/late data/cardinality", "config truth + local assignment + exposure log + analytics", "How do you prevent sample-ratio mismatch and peeking bias?"),
]


def top_30_system_design_doc() -> str:
    sections = []
    for number, (name, clarify, challenge, bottleneck, direction, followup) in enumerate(SYSTEM_DESIGN_30, 1):
        sections.append(dedent(f'''
        ## {number}. Design {name}

        - **Requirements to clarify:** {clarify}.
        - **Main challenge:** {challenge}.
        - **Likely bottleneck:** {bottleneck}.
        - **Architecture direction:** {direction}.
        - **Follow-up interviewer may ask:** *{followup}*
        '''))
    return dedent(f'''\
    # Top 30 System Design Questions

    Không học thuộc component list. Với mỗi đề, dành 5 phút clarify/estimate, 10 phút V1, 10 phút bottleneck/evolution và 10 phút failure/security/observability/trade-off.

    {''.join(sections)}

    ## Universal closing questions

    - Which component is the source of truth, and which data is derived?
    - What is the first bottleneck at 10× traffic, and which metric proves it?
    - What fails during a timeout after commit, and how is it reconciled?
    - What would you deliberately avoid at 100 RPS?
    - How do you test restore, failover, duplicate delivery, and graceful degradation?
    ''')


def support_readmes() -> dict[str, str]:
    mock_links = "\n".join(
        f"- [{title_from_name(name)}]({name})"
        for name in [*MOCK_DOMAINS, "top-50-senior-backend-questions.md", "top-30-system-design-questions.md", "full-mock-interview.md"]
    )
    cheat_links = "\n".join(f"- [{title_from_name(name)}]({name})" for name in CHEATSHEETS)
    design_links = "\n".join(f"- [{d['title']}]({name})" for name, d in DESIGNS.items())
    return {
        "22-mock-interview/README.md": f"# Mock Interview\n\n{mock_links}\n\nDùng timer, trả lời thành tiếng rồi mới mở rubric. [← Main Dashboard](../README.md)\n",
        "23-cheatsheets/README.md": f"# Cheatsheets\n\n{cheat_links}\n\nBộ này được giữ ngắn để review trong 1–2 giờ. [← Main Dashboard](../README.md)\n",
        "11-system-design/README.md": dedent(f'''
        # System Design

        ## Learning order

        [Framework](system-design-framework.md) → [Capacity Estimation](capacity-estimation.md) → [Caching](caching.md) → [Database Scaling](database-scaling.md) → [Message Queue](message-queue.md) → [Observability](observability.md).

        ## Must know

        - Requirement/SLO/consistency và capacity estimate có đơn vị.
        - API/data model/source of truth trước component list.
        - V1 đơn giản → bottleneck đo được → V2/V3 có trade-off.
        - Timeout/retry/idempotency/backpressure/degraded mode/reconciliation.
        - Security, observability, RPO/RTO, cost và interview narrative.

        ## Recommended exercise

        Làm mỗi bài có timer 35 phút: 5 phút clarify/estimate, 20 phút architecture + deep dive, 10 phút failure/security/trade-off. Tự vẽ đủ high-level, sequence, data/source-of-truth, scaling và failure flow.

        ## Design Drills

        {design_links}

        Mỗi bài gồm requirement, scale, API, data model, architecture Mermaid, database/cache/queue/storage, scaling, failure, security, observability, bottleneck và future improvement.

        [← Main Dashboard](../README.md)
        '''),
        "24-references/README.md": dedent('''
        # Technical References

        Tài liệu chính dùng để kiểm tra behavior phụ thuộc version. Interview answer nên nói rõ runtime/database/framework version khi chi tiết implementation có thể thay đổi.

        ## Python / FastAPI

        - [Python 3.14 — Free-threaded CPython](https://docs.python.org/3/howto/free-threading-python.html)
        - [Python 3.14 — Thread states and the GIL](https://docs.python.org/3/c-api/threads.html)
        - [Python — asyncio](https://docs.python.org/3/library/asyncio.html)
        - [FastAPI — Concurrency and async/await](https://fastapi.tiangolo.com/async/)

        ## Data / Task Processing

        - [PostgreSQL — Examining index usage](https://www.postgresql.org/docs/current/indexes-examine.html)
        - [PostgreSQL — EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html)
        - [PostgreSQL — Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html)
        - [SQLAlchemy — Session Basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)
        - [Redis — Streams](https://redis.io/docs/latest/develop/data-types/streams/)
        - [Redis — Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
        - [Celery — Tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html)
        - [Celery — FAQ](https://docs.celeryq.dev/en/stable/faq.html)

        ## Infrastructure / Security

        - [Kubernetes — Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
        - [Kubernetes — Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
        - [Docker — Build best practices](https://docs.docker.com/build/building/best-practices/)
        - [Terraform — State](https://developer.hashicorp.com/terraform/language/state)
        - [OWASP Top 10](https://owasp.org/www-project-top-ten/)

        [← Main Dashboard](../README.md)
        '''),
    }


def repository_audit_doc() -> str:
    audit_path = ROOT / "00-interview-roadmap/repository-audit.md"
    markdown_files = sorted(p for p in ROOT.rglob("*.md") if p != audit_path)
    p0_dirs = {
        "01-python-core", "02-python-concurrency", "03-fastapi",
        "04-database-postgresql", "06-redis", "07-celery",
        "10-distributed-systems", "11-system-design",
    }
    p0_files = [p for p in markdown_files if p.relative_to(ROOT).parts[0] in p0_dirs and p.name != "README.md"]
    shallow = []
    no_diagram = []
    for path in p0_files:
        text = path.read_text(encoding="utf-8")
        words = len(re.findall(r"\b\w+\b", text, flags=re.UNICODE))
        if words < 800:
            shallow.append(str(path.relative_to(ROOT)))
        if "```mermaid" not in text:
            no_diagram.append(str(path.relative_to(ROOT)))
    designs = sorted((ROOT / "11-system-design").glob("design-*.md"))
    design_counts = {p.name: p.read_text(encoding="utf-8").count("```mermaid") for p in designs}
    mermaid_total = sum(p.read_text(encoding="utf-8").count("```mermaid") for p in markdown_files)
    deep_count = sum("## 13. Mental Model" in p.read_text(encoding="utf-8") for p in markdown_files)
    shallow_text = "- " + "\n- ".join(shallow) if shallow else "Không còn P0 file dưới 800 words."
    no_diagram_text = "- " + "\n- ".join(no_diagram) if no_diagram else "Không còn P0 file thiếu Mermaid diagram."
    return dedent(f'''\
    # Repository Depth Audit

    ## Audit baseline before this expansion

    - Markdown files audited: **270**.
    - P0/P1 technical files sampled systematically: **103**.
    - P0/P1 files under 800 words: **0**, nhưng chiều dài chủ yếu đến từ question template.
    - P0/P1 files without Mermaid: **92**.
    - System Design labs with fewer than five diagrams: **11/11**.
    - Main issue: definition/checklist có nhưng internals, data flow, failure propagation, debugging và architecture evolution chưa đủ sâu.

    ## Audit after expansion

    - Total Markdown files: **{len(markdown_files) + 1}** (bao gồm audit này).
    - Deep-dive files with Mental Model/Internals/Flow/Failure/Debugging: **{deep_count}**.
    - Mermaid diagrams: **{mermaid_total}** trước khi cộng audit (audit không thêm diagram).
    - P0 files under 800 words: **{len(shallow)}**.
    - P0 files without Mermaid: **{len(no_diagram)}**.
    - System Design labs: **{len(designs)}**, diagram count mỗi bài: **{min(design_counts.values(), default=0)}–{max(design_counts.values(), default=0)}**.

    ## Checks performed

    - Mandatory 12-section structure và question counts.
    - P0 depth sections: Mental Model, Internals, flow diagram, failure, debugging, misconceptions, when-not-to-use, interview chain, exercises, cross-links.
    - System Design: high-level, sequence, data/source-of-truth, scaling, failure/recovery, observability, evolution, security và walkthrough.
    - Local Markdown links, empty files, placeholder marker, exact duplicate file, Python fenced-code syntax và Mermaid structure/render.

    ## Remaining shallow files

    {shallow_text}

    ## Remaining P0 files without diagrams

    {no_diagram_text}

    Audit script tái chạy tại [`scripts/validate.py`](../scripts/validate.py). Báo cáo này mô tả structural/depth coverage; technical accuracy vẫn phải được kiểm theo version-specific official references trong [Technical References](../24-references/README.md).
    ''')


VALIDATOR = r'''from __future__ import annotations

import ast
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANDATORY = [
    "## 1. What is it?", "## 2. Why does it matter?", "## 3. How does it work?",
    "## 4. Example", "## 5. Production Use Case", "## 6. Common Problems",
    "## 7. Trade-offs", "## 8. Interview Questions", "## 9. Senior-level Questions",
    "## 10. Short Answers", "## 11. Follow-up Questions", "## 12. Key Takeaways",
]
EXEMPT_DIRS = {"00-interview-roadmap", "22-mock-interview", "23-cheatsheets"}
DEEP_DIRS = {
    "01-python-core", "02-python-concurrency", "03-fastapi", "04-database-postgresql",
    "05-sqlalchemy", "06-redis", "07-celery", "08-api-design", "10-distributed-systems",
    "11-system-design", "13-kubernetes", "16-security", "17-performance-reliability",
    "18-ai-integration", "20-senior-scenarios",
}
DEEP_HEADINGS = [
    "## 13. Mental Model", "## 14. Internals Deep Dive", "## 15. Request / Data Flow",
    "## 16. Failure Scenario", "## 17. How I would debug this in production",
    "## 18. Common Misconceptions", "## 19. When NOT to use",
    "## 20. What interviewer may ask next", "## 21. Check Your Understanding", "## 22. See also",
]
errors: list[str] = []
files = sorted(ROOT.rglob("*.md"))
python_blocks = 0
mermaid_blocks = 0
hashes: dict[str, list[Path]] = {}

if not files:
    errors.append("No Markdown files found")

for path in files:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    hashes.setdefault(digest, []).append(rel)
    if not text.strip():
        errors.append(f"Empty file: {rel}")
    if re.search(r"\b(?:TODO|TBD|FIXME)\b", text, flags=re.I):
        errors.append(f"Placeholder marker: {rel}")
    if path.name != "README.md" and rel.parts[0] not in EXEMPT_DIRS:
        missing = [heading for heading in MANDATORY if heading not in text]
        if missing:
            errors.append(f"Missing mandatory sections in {rel}: {', '.join(missing)}")
        counts = {kind: len(re.findall(rf"\*\*{kind}\d+\.\*\*", text)) for kind in ("B", "L", "S", "F")}
        expected = {"B": 10, "L": 10, "S": 5, "F": 5}
        for kind, minimum in expected.items():
            if counts[kind] < minimum:
                errors.append(f"Too few {kind} questions in {rel}: {counts[kind]} < {minimum}")
    if path.name != "README.md" and rel.parts[0] in DEEP_DIRS and not path.name.startswith("design-"):
        words = len(re.findall(r"\b\w+\b", text, flags=re.UNICODE))
        if words < 800:
            errors.append(f"Deep-dive file below 800 words: {rel} ({words})")
        if "```mermaid" not in text:
            errors.append(f"Deep-dive file has no Mermaid diagram: {rel}")
        missing_deep = [heading for heading in DEEP_HEADINGS if heading not in text]
        if missing_deep:
            errors.append(f"Missing deep-dive sections in {rel}: {', '.join(missing_deep)}")
    if text.count("```mermaid") > text.count("```") // 2:
        errors.append(f"Unbalanced Mermaid fence: {rel}")

    for number, code in enumerate(re.findall(r"```python\n(.*?)\n```", text, flags=re.S), 1):
        python_blocks += 1
        try:
            ast.parse(code)
        except SyntaxError as exc:
            errors.append(f"Invalid Python block {number} in {rel}: {exc}")

    for number, diagram in enumerate(re.findall(r"```mermaid\n(.*?)\n```", text, flags=re.S), 1):
        mermaid_blocks += 1
        first_line = next((line.strip() for line in diagram.splitlines() if line.strip()), "")
        if not re.match(r"^(?:flowchart|sequenceDiagram|graph|stateDiagram|erDiagram|gantt|timeline)\b", first_line):
            errors.append(f"Unknown Mermaid diagram type {number} in {rel}: {first_line}")

    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:)", target):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"Broken link in {rel}: {target}")

design_requirements = [
    "### Requirements", "### Functional Requirements", "### Non-functional Requirements",
    "### Scale Estimation", "### API", "### Data Model", "### High-level Architecture",
    "### Database", "### Cache", "### Message Queue", "### Storage", "### Scaling",
    "### Failure Handling", "### Security", "### Observability", "### Bottlenecks",
    "### Future Improvements", "### Architecture Evolution", "## Failure Scenarios",
    "## Security Deep Dive", "## How to explain this design in an interview", "```mermaid",
]
design_files = sorted((ROOT / "11-system-design").glob("design-*.md"))
if len(design_files) < 10:
    errors.append(f"Need at least 10 design files, found {len(design_files)}")
for path in design_files:
    text = path.read_text(encoding="utf-8")
    missing = [item for item in design_requirements if item not in text]
    if missing:
        errors.append(f"Incomplete system design {path.name}: {', '.join(missing)}")
    if text.count("```mermaid") < 5:
        errors.append(f"System design has fewer than 5 diagrams: {path.name}")
    if "sequenceDiagram" not in text:
        errors.append(f"System design has no sequence diagram: {path.name}")

for digest, duplicate_paths in hashes.items():
    if len(duplicate_paths) > 1:
        errors.append("Exact duplicate Markdown files: " + ", ".join(map(str, duplicate_paths)))

for required in [
    ROOT / "22-mock-interview/top-50-senior-backend-questions.md",
    ROOT / "22-mock-interview/top-30-system-design-questions.md",
    ROOT / "00-interview-roadmap/repository-audit.md",
]:
    if not required.exists():
        errors.append(f"Missing required expansion file: {required.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Total markdown files: {len(files)}")
print(f"System design exercises: {len(design_files)}")
print(f"Python fenced blocks parsed: {python_blocks}")
print(f"Mermaid blocks structurally checked: {mermaid_blocks}")
print("Empty files: 0")
print("Broken local Markdown links: 0")
print("Placeholder markers: 0")
'''


if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)
    for folder, files in STRUCTURE.items():
        for filename in files:
            if filename == "README.md":
                continue
            write(ROOT / folder / filename, knowledge_doc(folder, filename))
    for filename, design in DESIGNS.items():
        write(ROOT / "11-system-design" / filename, system_design_doc(filename, design))
    for folder in CATEGORY:
        write(ROOT / folder / "README.md", index_readme(folder))
    for filename, content in roadmap_files().items():
        write(ROOT / "00-interview-roadmap" / filename, content)
    for filename, topics in MOCK_DOMAINS.items():
        write(ROOT / "22-mock-interview" / filename, mock_pack(filename, topics))
    write(ROOT / "22-mock-interview" / "full-mock-interview.md", full_mock())
    write(ROOT / "22-mock-interview" / "top-50-senior-backend-questions.md", top_50_questions_doc())
    write(ROOT / "22-mock-interview" / "top-30-system-design-questions.md", top_30_system_design_doc())
    for filename, content in CHEATSHEETS.items():
        write(ROOT / "23-cheatsheets" / filename, content)
    for relative_path, content in support_readmes().items():
        write(ROOT / relative_path, content)
    write(ROOT / "README.md", main_readme())
    write(ROOT / "scripts" / "validate.py", VALIDATOR)
    write(ROOT / "00-interview-roadmap" / "repository-audit.md", repository_audit_doc())
    markdown_count = len(list(ROOT.rglob("*.md")))
    print(f"Generated files under {ROOT}")
    print(f"Total markdown files: {markdown_count}")
