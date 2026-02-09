with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The ASSP content to add to Policy Interpretation (simplified for inline use)
assp_content = '''<h4 style="color: var(--accent-light); margin: 1.5rem 0 1rem;">ASSP Partnership Strategy</h4>
                            <p style="margin-bottom: 1rem;">The American Society of Safety Professionals (ASSP) offers a safety-focused digital knowledge base with regulatory content, best practices, and training materials. A partnership could accelerate our compliance content depth.</p>
                            
                            <p style="margin-bottom: 0.5rem;"><strong>Two-Phase Approach:</strong></p>
                            <ul style="margin-bottom: 1rem; padding-left: 1.5rem;">
                                <li><strong>Phase 1: Embed via SSO</strong> — Integrate ASSP content through SSO/API (1-2 quarters). Immediate access to authoritative content.</li>
                                <li><strong>Phase 2: Custom RAG</strong> — Build RAG pipeline over ASSP content + customer docs (2-3 quarters after Phase 1). "Ask anything" experience.</li>
                            </ul>
                            
                            '''

# Remove the entire ASSP section
assp_section_start = '''<!-- ASSP Partnership -->
            <section id="assp">
                <h2 class="section-title">ASSP Partnership Strategy</h2>
                
                <h3>Context</h3>
                <p>The American Society of Safety Professionals (ASSP) offers a safety-focused digital knowledge base with regulatory content, best practices, and training materials. A partnership could accelerate our compliance content depth.</p>
                
                <h3>Two-Phase Approach</h3>
                <div class="phases">
                    <div class="phase-card">
                        <h4>Phase 1: Embed via SSO (Quick to Market)</h4>
                        <ul>
                            <li><strong>What:</strong> Integrate ASSP content through SSO/API</li>
                            <li><strong>Timeline:</strong> 1-2 quarters</li>
                            <li><strong>Value:</strong> Immediate access to authoritative content; "Powered by ASSP"</li>
                            <li><strong>Dependency:</strong> ASSP contract terms, their API/architecture</li>
                        </ul>
                    </div>
                    
                    <div class="phase-card">
                        <h4>Phase 2: Custom RAG + Consolidated Chat</h4>
                        <ul>
                            <li><strong>What:</strong> Build RAG pipeline over ASSP content + customer docs</li>
                            <li><strong>Timeline:</strong> 2-3 quarters after Phase 1</li>
                            <li><strong>Value:</strong> "Ask anything" experience blending regulatory + customer-specific</li>
                            <li><strong>Dependency:</strong> Document Ingestion capability</li>
                        </ul>
                    </div>
                </div>
                
                
            </section>'''

content = content.replace(assp_section_start, '')

# Also remove the ASSP nav link from sidebar
content = content.replace('<li><a href="#assp">ASSP Partnership</a></li>', '')

# Insert ASSP content before the "How ASSP Fits" table we already moved
insert_before = '''<h4 style="color: var(--accent-light); margin: 1.5rem 0 1rem;">How ASSP Fits with Prioritized Opportunities</h4>'''

content = content.replace(insert_before, assp_content + insert_before)

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done - moved full ASSP section into Policy Interpretation Engine!')
