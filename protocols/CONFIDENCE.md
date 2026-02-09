# Confidence Protocol

## Purpose
Sub-agents running on Sonnet should self-assess confidence. If below threshold, flag for escalation to Opus.

## Rules

### At task completion, assess confidence:
- **85%+ confident**: Deliver response normally
- **Below 85%**: Include flag at the END of response:

```
[LOW_CONFIDENCE: <brief reason>]
```

### Examples of low-confidence situations:
- Ambiguous requirements that could be interpreted multiple ways
- Domain expertise outside your specialty
- Complex multi-step reasoning where you're uncertain about steps
- Missing information that significantly affects output quality
- Tasks requiring judgment calls you're not sure about

### What happens when flagged:
1. Rabbit (orchestrator) receives the response
2. Reviews the low-confidence reason
3. May re-run the task with Opus for higher quality
4. Or may accept the response if the uncertainty is acceptable

### DO NOT flag for:
- Normal task completion where you did your best
- Stylistic uncertainty (that's subjective)
- When the task is genuinely impossible (just say so)

## Note
This is a cost-optimization protocol. Sonnet handles most tasks well. Opus is the escalation path when needed.
