# Skill Assignments by Agent

*Updated: 2026-02-07*

## Recommended Skill Mapping

Based on available skills and agent roles:

| Agent | Primary Skills | Notes |
|-------|---------------|-------|
| **Rabbit (main)** | healthcheck, github, skill-creator | Orchestrator - broad access |
| **Rabbit_Coder** | coding-agent, github | Run Codex/Claude Code, manage PRs |
| **Rabbit_Researcher** | summarize | Web search built-in; summarize long content |
| **Rabbit_Creative** | canvas, sag | UI design, TTS for storytelling |
| **Rabbit_Ops** | healthcheck | System security audits |
| **Rabbit_Security** | healthcheck | Security-focused audits |
| **Rabbit_EHS** | (none) | Domain expertise, no special tools |
| **Rabbit_Novara** | (none) | Business context, no special tools |
| **Rabbit_PO** | trello | Task/project management |

## Available Skills (60+)

Key skills by category:

**Development:**
- `coding-agent` - Run Codex, Claude Code, Pi in background
- `github` - gh CLI for PRs, issues, runs

**Security:**
- `healthcheck` - Host hardening, security audits

**Communication:**
- `discord` - Discord API integration
- `slack` - Slack integration

**Content:**
- `canvas` - HTML/design work
- `openai-image-gen` - Image generation
- `sag` - ElevenLabs TTS

**Productivity:**
- `trello` - Trello boards
- `notion` - Notion integration
- `obsidian` - Obsidian notes
- `things-mac` - Things 3 tasks (macOS)

**Research:**
- `summarize` - Summarize long content
- `weather` - Weather data

## Implementation

Skills are loaded dynamically when needed. No config changes required - agents match skills by description in their SKILL.md files.

To assign a skill explicitly, add to agent's `agentDir/SKILL.md` or reference in TOOLS.md.
