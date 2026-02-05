# Grant Robertson — Context Omnibus

Saved: 2026-02-04

---

## Professional Background

- 15+ years: VFX, AI/ML pipelines, creative tech, enterprise platforms
- Built node-based platforms for: data curation, model training, inference orchestration, workflow automation
- Systems: MetaFlow, FoxTail, ComfyUI-style node graphs, Atlas-like orchestration
- Infra experience: Kubernetes, GPU inference stacks, dataset pipelines, HITL review systems
- Core strength: Turning complex technical systems into usable, productized platforms
- Bridges: Engineering reality ↔ UX/workflow design ↔ Executive strategy/GTM

## Current Role

- **Company:** Novara (formerly KPA)
- **Industry:** EHS (Environment, Health, Safety) / Compliance
- **Role:** Sr. AI Technical Product Manager

---

## Product Philosophy (Non-Negotiables)

AI should:
- Remove work, not add steps
- Slot into real workflows
- Be measurable in business terms
- Be reliable and observable

Skeptical of:
- "AI features" for marketing optics
- Copilots not embedded in real operations
- One-off demos that don't compound

Favors:
- Platform thinking > feature thinking
- Reusable primitives > bespoke hacks
- Deterministic + probabilistic hybrids
- Guardrails, policies, fallback paths

Key questions Grant asks:
1. What work does this remove?
2. What happens when it's wrong?
3. How do we measure success?
4. How do we control cost and latency?
5. Can this power 3+ use cases?

---

## Strategic Lens (EHS/Compliance Domains)

In compliance/EHS/risk-heavy domains:
- Trust beats novelty
- Auditability beats creativity
- Reliability beats raw intelligence

Customers care about:
- Time saved
- Fewer mistakes
- Easier audits
- Better documentation
- Faster onboarding/reviews

AI must be: Observable, Logged, Explainable, Governed, Measured

---

## Architectural Worldview

### Agentic Systems

Role-based agents, not monolithic prompts:
- **Planner:** decomposes tasks
- **Researcher:** gathers context
- **Executor:** performs actions (tools, APIs, workflows)
- **Validator:** checks outputs, compliance, policy
- **Orchestrator:** routes, sequences, retries, escalates

Agents are: tool-using, policy-bound, observable, replaceable

Model routing based on: cost, latency, risk, required reliability

### Deterministic + Probabilistic Hybrid

- Deterministic workflow skeleton
- AI fills in: classification, summarization, extraction, reasoning
- Hard rails around: inputs, outputs, validation, escalation paths

Critical for: compliance, audit trails, enterprise trust

---

## Platform Primitives

Any serious AI platform needs:
- **Ingestion:** docs, policies, incidents, forms, user input
- **Retrieval:** search, RAG, filters, scoping
- **Orchestration:** workflow engine, agent router, step sequencer
- **Execution:** tool calls, API calls, DB writes, ticket creation
- **Evaluation:** automatic checks, heuristics, rules, human review hooks
- **Observability:** logs, traces, cost tracking, latency tracking, success/failure rates
- **Governance:** policy enforcement, data boundaries, audit logs, access control

---

## The AI Gateway Concept

Central to Grant's strategy — a platform layer, not a feature.

Responsibilities:
- Request intake
- Auth & authorization
- Policy checks
- Routing to agents/models/workflows
- Logging and tracing
- Cost accounting
- Evaluation hooks

Benefits:
- Decouples product teams from model churn
- Centralizes governance and observability
- Enables multi-model strategies, tiered reliability, gradual rollout

The backbone for all AI features. The control plane for AI in the company.

---

## Likely KPA Application Areas

High-value hypotheses:
- **Compliance:** policy interpretation, gap analysis, audit prep, evidence collection
- **EHS/Safety:** incident summarization, root cause clustering, risk classification, corrective action drafting
- **Operations:** document ingestion/normalization, customer-specific policy mapping, review workflows
- **Sales/CS:** faster onboarding, questionnaire automation, RFP/audit response drafting

All should be: built on shared primitives, powered by shared agents, measured with shared metrics

---

## Metrics Doctrine

### Business
- Time saved per workflow
- Cost per task
- Throughput increase
- Error reduction
- Cycle time reduction

### Product
- Adoption per workflow
- Completion rates
- Human override rates
- Task success rates

### System
- Cost per request
- Latency per step
- Model usage mix
- Failure/retry rates

**If it can't be measured, it's not "done".**

---

## Delivery Philosophy

Start with:
- Platform spine (Gateway + orchestration)
- 2–3 killer workflows

Phase it:
1. Internal enablement / pilot
2. Customer-facing narrow use cases
3. Platformization and expansion

Always ship with: metrics, guardrails, exec-ready story

Likes: 90-day plans, clear milestones, eng-realistic backlogs

---

## Buy vs Build

Build:
- Orchestration layer
- Gateway
- Workflow integration
- Domain-specific logic

Buy/integrate:
- Models
- Vector DBs
- Some eval tools
- Some agent frameworks (if helpful)

Wary of: vendor lock-in at control plane, "magic" platforms that hide too much

---

## UX & Workflow Bias

Prefers:
- Clear, step-based workflows
- Human-in-the-loop for risky steps
- Review screens, diffs, approvals

Mental model: node-based/graph-like
Exposed to users as: simple flows, not technical diagrams

UI should: make automation feel safe, make AI feel assistive (not autonomous chaos)

---

## Communication Style

Be: structured, direct, concrete, slightly opinionated

Use: bullets, tables, phases, diagrams (text-described), tradeoff analysis

Avoid: hype language, vague "AI will transform X", abstract frameworks without execution paths

---

## Known Unknowns (To Clarify)

- Exact KPA product lines and priorities
- Which workflows hurt the most today
- What data is clean vs messy
- Legal/compliance constraints
- Existing infra maturity
- Customer segmentation differences

**Ask targeted questions, don't assume.**

---

## Prime Directive

> The goal is not to "add AI features". The goal is to build a durable, governed, observable AI platform that compounds into multiple high-ROI workflows in compliance-heavy enterprise environments like KPA.
