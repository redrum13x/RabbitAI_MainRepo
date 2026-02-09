# MEMORY.md — Long-Term Memory

*Last curated: 2026-02-06*

---

## Who I Am
- **Name:** Rabbit 🐇
- **Role:** Senior AI Technical Product Manager — Grant's second brain and co-worker
- **Born:** 2026-02-04 (first conversation with Grant)

## Who Grant Is
- Works at **Novara** (formerly KPA) — EHS (Environment, Health & Safety) industry
- Role: Sr. AI Technical Product Manager
- Timezone: America/New_York (EST)
- Communication: Primarily via Discord

## The Team
- **Rabbit** 🐇 — Orchestrator, strategy, analysis
- **Rabbit_Coder** 💻 — Coding, generation, PDF/doc creation
- **Rabbit_Researcher** 🔍 — Deep research, competitive intel
- **Grant** 👤 — PM, decision maker, human in the loop

---

## Novara AI Strategy (Private)

### Key Project: AI Opportunities Assessment
- 10 AI opportunities identified and documented
- Hazard Detection (Computer Vision) is in progress
- Two-stage model approach: Nova Lite for triage ($0.0005), Claude for deep analysis ($0.0016)
- PostgreSQL preferred over DynamoDB (existing infrastructure)

### Competitive Landscape
- **Major EHS players:** Intelex, Enablon, VelocityEHS, SafetyCulture, Benchmark Gensuite
- **CV specialists:** Intenseye ($64M raised), Protex AI, Voxel
- **Wearables:** Kinetic, Soter Analytics
- **Threat:** SafetyCulture moving fast on photo AI; Intenseye expanding scope

### Strategic Priorities
1. **Document Ingestion** — Foundation for everything
2. **Hazard Detection** — Competitive race, high differentiation
3. **Root Cause Clustering** — Unique ML capability, hard to replicate
4. **Audit Prep Automation** — High customer demand

### Key Decisions Made
- Focus on current capabilities (photos, text, audio) before future tech (AR/wearables)
- No timelines in presentations — list what needs to be built without Q1/Q2 dates
- All Novara docs are private (not synced to public board)
- No AI/Claude/Rabbit references in client-facing documents

---

## Technical Context

### Model Accuracy Findings (from KPA eval)
- Nova: 45%/54% match rate
- Claude: 27%/27% match rate (but best detail quality)
- Pixtral: 41%/27% match rate

### Infrastructure
- PostgreSQL preferred (team knows it, pgvector for embeddings, RDS Proxy for Lambda)
- Offline-first workflow: queue submissions locally, auto-sync when connected
- PDF generation: Edge headless with `--no-pdf-header-footer`

---

## Workspace Structure
- **Main workspace:** `C:\Users\Grant\.openclaw\workspace`
- **Rabbit_Coder workspace:** `C:\Users\Grant\.openclaw\workspace-rabbit_coder`
- **Rabbit_Researcher workspace:** `C:\Users\Grant\.openclaw\workspace-rabbit_researcher`
- **Private Novara docs:** `workspace-private\novara-ai\`
- **Inbox (Grant's uploads):** `workspace\inbox\`

### Key Files
- Board: `kanban/` — deployed to GitHub Pages
- Memory: `memory/YYYY-MM-DD.md` — daily logs
- This file: Long-term curated memory

---

## Communication Channels
- **#main-work** — Primary work channel with Grant
- **#agent-activity** (1469017791498813626) — Sub-agent orchestration visibility
- Private DMs for sensitive info

---

## Lessons Learned

### Process
- Post to #agent-activity when spawning sub-agents (Grant wants visibility)
- Private tasks should stay local, not sync to GitHub
- Use bullet lists instead of markdown tables on Discord/WhatsApp

### Technical
- PowerShell uses `;` not `&&` for command chaining
- Always use `--no-pdf-header-footer` for clean PDF generation

---

## Pending Setup
- [x] Brave API key for web search ✅ 2026-02-06
- [x] Google Drive access (redrum137@gmail.com) ✅ 2026-02-06
- [x] Multi-account Discord for Creative ✅ 2026-02-07 (use `accountId: "creative"`)
- [x] Local Ollama fallback ✅ 2026-02-07
- [x] Auto-start at boot ✅ 2026-02-07
- [x] Health monitoring ✅ 2026-02-07
- [ ] Gmail integration (needs gcloud CLI)
- [x] Google Drive integration ✅ 2026-02-07 (rclone + RabbitAI OAuth)
- [ ] Calendar integration

---

## Hardware (Grant's PC)
- **GPU:** RTX 3090 (24GB VRAM)
- **PSU:** ROG Thor 1200W
- **Storage:** Samsung 970 EVO Plus 1TB, MS100 1TB

## Model Configuration (2026-02-07)

**Claude agents:** Main, Security (Opus), Coder, Researcher, Creative, Ops (Sonnet)
**Local Ollama agents:** EHS, Novara, PO (gpt-oss:20b on RTX 3090)
**Fallback chain:** Opus → Sonnet → Local Ollama

**Memory Search:** Local embeddings via Ollama (`nomic-embed-text`), hybrid BM25+vector

**Confidence Protocol:** Sub-agents flag `[LOW_CONFIDENCE: reason]` if <85% confident; I escalate to Opus.

**Gateway restart protocol:** Always post "✅ Back online" immediately after any restart.

---

*This file is mine to maintain. Update when significant decisions are made or context changes.*
