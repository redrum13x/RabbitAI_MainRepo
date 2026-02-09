# Update TLDRs to be more value-focused

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Old TLDRs -> New TLDRs (more robust, ROI-focused, differentiated)

replacements = [
    # 1. Policy Interpretation
    (
        'AI that answers compliance questions using your actual policies. Saves 15-30 min per query. Build after Document Ingestion.',
        'Instant answers to "does this apply to us?" questions. Safety managers spend 2-4 hours/week hunting through policy docs — this gives them answers in seconds with source citations. Unlike generic chatbots, it knows YOUR policies. ROI: 100+ hours saved per safety manager annually.'
    ),
    # 2. Document Ingestion
    (
        'Turn uploaded PDFs and docs into searchable, structured data. Foundation for everything else. Start here.',
        'The foundation that powers everything else. Upload any safety doc — PDFs, Word, scanned paper — and it becomes searchable, tagged, and AI-ready. Without this, customers are stuck with static file folders. First-mover advantage: competitors don\'t have EHS-specific document AI.'
    ),
    # 3. Incident Summarization
    (
        'One-click executive summaries from incident reports. Low complexity, high visibility. Quick win.',
        'Turn a 3-page incident report into a 3-paragraph executive brief instantly. Safety directors get board-ready summaries without manual rewriting. Low complexity, high visibility — ship fast to build internal confidence and show customers immediate value. Demo-friendly.'
    ),
    # 4. Root Cause Clustering
    (
        'ML finds hidden patterns across incidents ("17 incidents share inadequate training — all night shift, Plant B"). Catches issues 60-90 days earlier. Major differentiator.',
        'Finds what humans miss: "17 incidents this quarter share inadequate training — all night shift, Plant B." Surfaces systemic issues 60-90 days before they become crises. No competitor does real ML pattern detection on incident data. This is predictive safety — a genuine moat.'
    ),
    # 5. Corrective Action Drafting
    (
        'AI suggests corrective actions based on what worked for similar past incidents. Cuts drafting time 50%. Build after we have CAPA history.',
        'AI suggests proven fixes: "For slip-and-fall incidents like this, these 3 actions resolved 80% of similar cases." Cuts CAPA drafting time in half. Depends on historical data — gets smarter with every incident. Value grows over time as the system learns what works.'
    ),
    # 6. Audit Prep
    (
        'Auto-gathers evidence, pre-fills responses, flags gaps before audits. "Never scramble for an audit again." High customer demand.',
        '"Never scramble for an audit again." System auto-gathers evidence, pre-fills responses, and flags gaps 2 weeks before the auditor arrives. Audit anxiety is universal — this is the aspirin. High customer demand; clear ROI in reduced prep time and fewer findings.'
    ),
    # 7. Customer Policy Mapping
    (
        'Connects generic regulations to your specific SOPs. "What\'s our procedure for X?" → Exact document and section. Build after doc foundation is solid.',
        'Bridges the gap between "what does OSHA require?" and "what\'s OUR procedure?" Returns exact SOP sections, not generic guidance. Eliminates the "I think it\'s in the blue binder" problem. Requires solid document foundation first.'
    ),
    # 8. Questionnaire Automation
    (
        'AI drafts 80% of compliance questionnaire responses from past answers. Clear ROI but not core EHS. Consider Loopio integration.',
        'Customers drown in compliance questionnaires — 200 questions, same answers every time. AI drafts 80% from past responses. Clear time savings (days → hours) but not core EHS. Consider integration with Loopio/Responsive before building.'
    ),
    # 9. Smart Onboarding
    (
        'AI-guided setup for new customers. Reduces implementation time 30-50%. Nice to have, not a differentiator.',
        'Conversational setup that asks "what industry, what size, what regulations?" and auto-configures the platform. Cuts implementation time 30-50%, improves time-to-value. Not a differentiator, but reduces churn and support load.'
    ),
    # 10. Hazard Detection
    (
        'AI analyzes photos/video to spot hazards and PPE violations. High complexity but high impact. Competitive race with Intenseye/SafetyCulture. Already in progress.',
        'AI spots hazards in photos and video: missing PPE, blocked exits, unsafe conditions. Turns every phone into a safety inspector. High complexity, high impact — and a competitive race (Intenseye has $64M, SafetyCulture is moving fast). Our edge: integrated EHS workflow, not just alerts.'
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f'Updated: {old[:50]}...')
    else:
        print(f'NOT FOUND: {old[:50]}...')

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone!')
