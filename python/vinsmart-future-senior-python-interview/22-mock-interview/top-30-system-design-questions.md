# Top 30 System Design Questions

Không học thuộc component list. Với mỗi đề, dành 5 phút clarify/estimate, 10 phút V1, 10 phút bottleneck/evolution và 10 phút failure/security/observability/trade-off.


## 1. Design AI Chatbot Platform

- **Requirements to clarify:** tenant, private docs, citations, streaming, quality SLO.
- **Main challenge:** ACL-aware RAG and probabilistic quality.
- **Likely bottleneck:** LLM quota/TTFT and vector recall.
- **Architecture direction:** PG metadata + object/vector derived index + orchestrator.
- **Follow-up interviewer may ask:** *How do you survive provider outage and prompt injection?*

## 2. Design Intelligent Document Processing

- **Requirements to clarify:** file types/size, OCR accuracy, review, retention.
- **Main challenge:** versioned multi-stage workflow.
- **Likely bottleneck:** large file/GPU/OCR queue age.
- **Architecture direction:** pre-signed upload + object truth + idempotent stage queue.
- **Follow-up interviewer may ask:** *How do you retry one failed page without duplicating the job?*

## 3. Design Video Analytics Platform

- **Requirements to clarify:** camera count/bitrate, alert latency, retention.
- **Main challenge:** continuous ingest and GPU backpressure.
- **Likely bottleneck:** network/GPU/partition skew/storage.
- **Architecture direction:** edge segment + Kafka by camera + GPU pools + event store.
- **Follow-up interviewer may ask:** *When do you sample/drop frames, and how is evidence preserved?*

## 4. Design Vehicle Inspection Platform

- **Requirements to clarify:** station/offline mode, media, AI + human decision.
- **Main challenge:** evidence immutability and auditable workflow.
- **Likely bottleneck:** upload bandwidth/AI queue/human review.
- **Architecture direction:** PG workflow + object evidence + outbox + review.
- **Follow-up interviewer may ask:** *How do you handle model disagreement or station reconnect?*

## 5. Design Vehicle Warranty System

- **Requirements to clarify:** eligibility, claim, settlement, policy versions.
- **Main challenge:** money invariant and temporal rules.
- **Likely bottleneck:** 500M history/query/enterprise integration.
- **Architecture direction:** PG claim truth + versioned rules + ledger + outbox.
- **Follow-up interviewer may ask:** *How do you prevent duplicate claims and reconcile payment?*

## 6. Design Manufacturing Production Planning

- **Requirements to clarify:** plants/lines/BOM/demand/solver latency.
- **Main challenge:** consistent immutable planning snapshot.
- **Likely bottleneck:** solver compute/stale inputs/hot plant.
- **Architecture direction:** lake snapshot + workflow + solver + versioned plan publish.
- **Follow-up interviewer may ask:** *What happens if ERP changes while solving?*

## 7. Design Real-time Chat

- **Requirements to clarify:** DM/group, ordering, presence, offline sync.
- **Main challenge:** ordering scope and multi-device fan-out.
- **Likely bottleneck:** hot group/connections/fan-out.
- **Architecture direction:** WebSocket gateway + partitioned log + broker + history.
- **Follow-up interviewer may ask:** *How do clients resume without missing or duplicating messages?*

## 8. Design Notification System

- **Requirements to clarify:** channels, priority, preference, campaign.
- **Main challenge:** fan-out with provider quota/compliance.
- **Likely bottleneck:** provider throttling/large campaign.
- **Architecture direction:** intent DB + outbox + channel queues + receipt ledger.
- **Follow-up interviewer may ask:** *How do transactional alerts bypass marketing backlog?*

## 9. Design Distributed File Processing

- **Requirements to clarify:** file size/stages/progress/replay.
- **Main challenge:** resumable upload and stage idempotency.
- **Likely bottleneck:** bandwidth/transform workers/orphan artifact.
- **Architecture direction:** object bytes + job DB + stage queues + checksums.
- **Follow-up interviewer may ask:** *How do you detect and clean partial artifacts?*

## 10. Design Task Processing Platform

- **Requirements to clarify:** runtime/resource class/priority/cancel.
- **Main challenge:** lease, fairness, at-least-once state.
- **Likely bottleneck:** long task/starvation/noisy tenant.
- **Architecture direction:** task DB + outbox + scheduler + resource queues + result store.
- **Follow-up interviewer may ask:** *What does cancel mean during an external side effect?*

## 11. Design API Rate Limiter

- **Requirements to clarify:** identity/scope/burst/global accuracy.
- **Main challenge:** distributed counters and fail-open/closed.
- **Likely bottleneck:** hot identity/Redis outage/clock.
- **Architecture direction:** gateway token bucket + local shield + Redis atomic update.
- **Follow-up interviewer may ask:** *How do login and catalog use different failure policy?*

## 12. Design URL Shortener

- **Requirements to clarify:** read/write ratio, custom alias, expiry.
- **Main challenge:** unique ID and hot redirects.
- **Likely bottleneck:** cache miss/abuse/hot key.
- **Architecture direction:** ID service + PG/KV truth + CDN/cache.
- **Follow-up interviewer may ask:** *How do you prevent enumeration and malicious links?*

## 13. Design Search Autocomplete

- **Requirements to clarify:** language/prefix/freshness/personalization.
- **Main challenge:** low-latency ranking and index refresh.
- **Likely bottleneck:** hot prefix/index memory.
- **Architecture direction:** offline trie/index build + online cache/ranker.
- **Follow-up interviewer may ask:** *How do you publish a new index atomically?*

## 14. Design Metrics Monitoring Platform

- **Requirements to clarify:** cardinality, scrape/push, retention, query.
- **Main challenge:** high-volume time-series ingest.
- **Likely bottleneck:** cardinality/storage/query fan-out.
- **Architecture direction:** ingest shards + WAL + TSDB + downsampling.
- **Follow-up interviewer may ask:** *How do you prevent one tenant from exploding cardinality?*

## 15. Design Distributed Log Service

- **Requirements to clarify:** ordering/durability/retention/consumer.
- **Main challenge:** partition leadership and replication.
- **Likely bottleneck:** hot partition/disk/network.
- **Architecture direction:** partitioned append log + replicas + consumer offsets.
- **Follow-up interviewer may ask:** *What acknowledgement level meets the durability SLO?*

## 16. Design Payment Processing

- **Requirements to clarify:** authorize/capture/refund/currency/ledger.
- **Main challenge:** idempotent money movement and audit.
- **Likely bottleneck:** provider timeout/ledger contention.
- **Architecture direction:** API + double-entry ledger + outbox + provider adapter.
- **Follow-up interviewer may ask:** *What if provider succeeds but your response times out?*

## 17. Design Inventory Reservation

- **Requirements to clarify:** stock unit/warehouse/expiry/oversell.
- **Main challenge:** concurrent reservation invariant.
- **Likely bottleneck:** hot SKU/lock contention.
- **Architecture direction:** atomic DB counter/reservation + expiry events.
- **Follow-up interviewer may ask:** *How do you release expired reservations exactly enough?*

## 18. Design Order Management

- **Requirements to clarify:** cart/order/payment/shipment/cancel.
- **Main challenge:** cross-domain Saga and user-visible state.
- **Likely bottleneck:** payment/inventory partial failure.
- **Architecture direction:** order state machine + outbox + orchestrated Saga.
- **Follow-up interviewer may ask:** *Which step is irreversible and how do you compensate?*

## 19. Design Audit Logging

- **Requirements to clarify:** events/tamper/retention/search/privacy.
- **Main challenge:** immutable complete evidence.
- **Likely bottleneck:** write volume/index/retention.
- **Architecture direction:** append log + immutable object archive + search projection.
- **Follow-up interviewer may ask:** *How do you prove logs were not altered?*

## 20. Design Feature Flag Service

- **Requirements to clarify:** targeting/consistency/SDK/offline.
- **Main challenge:** safe low-latency evaluation.
- **Likely bottleneck:** config fan-out/stale SDK/cache.
- **Architecture direction:** versioned config truth + streaming distribution + local evaluation.
- **Follow-up interviewer may ask:** *How do you prevent a flag service outage from taking down apps?*

## 21. Design Configuration Service

- **Requirements to clarify:** secret/non-secret, version, rollout, scope.
- **Main challenge:** consistent versioned distribution.
- **Likely bottleneck:** watch fan-out/bad config.
- **Architecture direction:** config DB + signed version + watch/cache + rollback.
- **Follow-up interviewer may ask:** *How do you canary a configuration, not just code?*

## 22. Design Webhook Delivery

- **Requirements to clarify:** endpoint, signing, retry, ordering.
- **Main challenge:** untrusted slow consumers.
- **Likely bottleneck:** retry backlog/one bad tenant.
- **Architecture direction:** event DB + tenant queues + signed sender + attempt ledger.
- **Follow-up interviewer may ask:** *How do consumers dedupe and verify authenticity?*

## 23. Design IoT Telemetry Platform

- **Requirements to clarify:** device count/frequency/commands/offline.
- **Main challenge:** device identity and high-volume ingest.
- **Likely bottleneck:** connection/partition/storage.
- **Architecture direction:** MQTT gateway + stream + time-series/lake + command service.
- **Follow-up interviewer may ask:** *How do you handle out-of-order device timestamps?*

## 24. Design Fraud Detection Pipeline

- **Requirements to clarify:** online decision/feature freshness/review.
- **Main challenge:** low latency with explainable evidence.
- **Likely bottleneck:** feature store/model quota/false positive.
- **Architecture direction:** event stream + online features + model + case workflow.
- **Follow-up interviewer may ask:** *How do you fall back when the model service is unavailable?*

## 25. Design Report Generation

- **Requirements to clarify:** template/data size/schedule/download.
- **Main challenge:** consistent snapshot and long-running work.
- **Likely bottleneck:** DB impact/render CPU/storage.
- **Architecture direction:** job DB + query snapshot + worker + object artifact.
- **Follow-up interviewer may ask:** *How do you avoid reports overloading the primary DB?*

## 26. Design Data Export / GDPR Deletion

- **Requirements to clarify:** scope/format/deadline/derived copies.
- **Main challenge:** complete lineage across systems.
- **Likely bottleneck:** large scan/downstream deletion.
- **Architecture direction:** request workflow + inventory + per-store workers + audit.
- **Follow-up interviewer may ask:** *How do you verify vector/cache/backup handling?*

## 27. Design Distributed Scheduler

- **Requirements to clarify:** cron/one-off/timezone/misfire.
- **Main challenge:** single logical firing under failover.
- **Likely bottleneck:** clock/leader/hot schedule.
- **Architecture direction:** schedule DB + lease/leader + due-time index + task queue.
- **Follow-up interviewer may ask:** *What does exactly-once schedule execution mean?*

## 28. Design Multi-tenant SaaS Backend

- **Requirements to clarify:** isolation/customization/quota/region.
- **Main challenge:** tenant boundary and noisy-neighbor control.
- **Likely bottleneck:** hot tenant/pool/storage.
- **Architecture direction:** tenant context + shared/cell data plane + quota + audit.
- **Follow-up interviewer may ask:** *When do you move from shared schema to cell/database isolation?*

## 29. Design Content Moderation Pipeline

- **Requirements to clarify:** modalities/latency/appeal/policy version.
- **Main challenge:** policy/model/human consistency.
- **Likely bottleneck:** burst/GPU/review queue.
- **Architecture direction:** upload + scan/model queue + decision state + review.
- **Follow-up interviewer may ask:** *How do you re-evaluate old content after policy changes?*

## 30. Design Experimentation Platform

- **Requirements to clarify:** assignment/metrics/guardrail/exposure.
- **Main challenge:** stable bucketing and unbiased events.
- **Likely bottleneck:** event quality/late data/cardinality.
- **Architecture direction:** config truth + local assignment + exposure log + analytics.
- **Follow-up interviewer may ask:** *How do you prevent sample-ratio mismatch and peeking bias?*


## Universal closing questions

- Which component is the source of truth, and which data is derived?
- What is the first bottleneck at 10× traffic, and which metric proves it?
- What fails during a timeout after commit, and how is it reconciled?
- What would you deliberately avoid at 100 RPS?
- How do you test restore, failover, duplicate delivery, and graceful degradation?
