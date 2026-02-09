with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Strategic Positioning section with cleaner format
old_positioning = '''<!-- Strategic Positioning -->
            <section id="positioning">
                <h2 class="section-title">Strategic Positioning</h2>
                
                <div class="phases">
                    <div class="phase-card">
                        <h4>Where We Can Lead (Differentiation)</h4>
                        <ul>
                            <li><strong>Root Cause Clustering</strong> — No one is doing real ML pattern detection on incident data</li>
                            <li><strong>Hazard Detection</strong> — Bridge between EHS software and CV; integrated workflow</li>
                            <li><strong>Audit Prep Automation</strong> — AI-powered evidence gathering; anxiety-killer</li>
                        </ul>
                    </div>
                    
                    <div class="phase-card">
                        <h4>Where We Should Fast-Follow (Table Stakes)</h4>
                        <ul>
                            <li><strong>Document Ingestion</strong> — Foundation everyone will need; get there first</li>
                            <li><strong>Incident Summarization</strong> — Easy to replicate but builds momentum</li>
                            <li><strong>Policy Interpretation</strong> — VelocityEHS has head start but shallow</li>
                        </ul>
                    </div>
                    
                    <div class="phase-card">
                        <h4>Where We Can Wait (No Urgency)</h4>
                        <ul>
                            <li><strong>Questionnaire Automation</strong> — Dedicated vendors exist; integrate vs. build</li>
                            <li><strong>Smart Onboarding</strong> — Nice to have, not competitive</li>
                            <li><strong>Corrective Action Drafting</strong> — Natural extension later</li>
                        </ul>
                    </div>
                    
                    <div class="phase-card">
                        <h4>Key Moat Opportunities</h4>
                        <ul>
                            <li><strong>Data advantage</strong> — More incident data → better predictions → more customers</li>
                            <li><strong>Integration depth</strong> — Hazard detection → incident mgmt → CAPA</li>
                            <li><strong>Industry expertise</strong> — CV companies don't understand OSHA; we do</li>
                            <li><strong>Partnership leverage</strong> — ASSP content + customer docs = unique corpus</li>
                        </ul>
                    </div>
                </div>
            </section>'''

new_positioning = '''<!-- Strategic Positioning -->
            <section id="positioning">
                <h2 class="section-title">Strategic Positioning</h2>
                
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>Category</th>
                                <th>Opportunities</th>
                                <th>Rationale</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Lead (Differentiation)</strong></td>
                                <td>Root Cause Clustering, Hazard Detection, Audit Prep</td>
                                <td>No competitor does real ML on incidents; we bridge EHS + CV; audit anxiety is universal</td>
                            </tr>
                            <tr>
                                <td><strong>Fast-Follow (Table Stakes)</strong></td>
                                <td>Document Ingestion, Incident Summarization, Policy Interpretation</td>
                                <td>Foundation everyone needs; quick wins build momentum; VelocityEHS is shallow here</td>
                            </tr>
                            <tr>
                                <td><strong>Wait (No Urgency)</strong></td>
                                <td>Questionnaire Automation, Smart Onboarding, Corrective Action</td>
                                <td>Dedicated vendors exist; nice-to-have, not competitive differentiators</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <h3>Key Moats</h3>
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>Moat</th>
                                <th>Why It Matters</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Data Advantage</strong></td>
                                <td>More incident data → better predictions → more customers (flywheel)</td>
                            </tr>
                            <tr>
                                <td><strong>Integration Depth</strong></td>
                                <td>Hazard detection → incident management → CAPA (end-to-end)</td>
                            </tr>
                            <tr>
                                <td><strong>Industry Expertise</strong></td>
                                <td>CV companies don't understand OSHA; we do</td>
                            </tr>
                            <tr>
                                <td><strong>Partnership Leverage</strong></td>
                                <td>ASSP content + customer docs = unique corpus</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>'''

content = content.replace(old_positioning, new_positioning)

# Replace Recommended Prioritization section with cleaner format
old_prioritization = '''<!-- Prioritization -->
            <section id="prioritization">
                <h2 class="section-title">Recommended Prioritization</h2>
                
                <div class="phases">
                    <div class="phase-card">
                        <h4>Tier 1: Build Now</h4>
                        <ul>
                            <li><strong>#2 Document Ingestion</strong> — Foundation for everything</li>
                            <li><strong>#3 Incident Summarization</strong> — Quick win, builds confidence</li>
                            <li><strong>#10 Hazard Detection</strong> — Already in progress; competitive race</li>
                        </ul>
                    </div>
                    
                    <div class="phase-card">
                        <h4>Tier 2: Build Next</h4>
                        <ul>
                            <li><strong>#4 Root Cause Clustering</strong> — Strategic differentiation</li>
                            <li><strong>#1 Policy Interpretation</strong> — High value once docs are ingested</li>
                            <li><strong>#6 Audit Prep Automation</strong> — High customer demand</li>
                        </ul>
                    </div>
                    
                    <div class="phase-card">
                        <h4>Tier 3: Evaluate Later</h4>
                        <ul>
                            <li>#5 Corrective Action Drafting</li>
                            <li>#7 Customer Policy Mapping</li>
                            <li>#8 Questionnaire Automation</li>
                            <li>#9 Smart Onboarding</li>
                        </ul>
                    </div>
                </div>
            </section>'''

new_prioritization = '''<!-- Prioritization -->
            <section id="prioritization">
                <h2 class="section-title">Recommended Prioritization</h2>
                
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>Tier</th>
                                <th>Opportunity</th>
                                <th>Why This Order</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="background: #d1fae5;">
                                <td rowspan="3"><strong>Tier 1: Build Now</strong></td>
                                <td>#2 Document Ingestion</td>
                                <td>Foundation for everything else</td>
                            </tr>
                            <tr style="background: #d1fae5;">
                                <td>#3 Incident Summarization</td>
                                <td>Quick win, builds internal confidence</td>
                            </tr>
                            <tr style="background: #d1fae5;">
                                <td>#10 Hazard Detection</td>
                                <td>Already in progress; competitive race</td>
                            </tr>
                            <tr style="background: #dbeafe;">
                                <td rowspan="3"><strong>Tier 2: Build Next</strong></td>
                                <td>#4 Root Cause Clustering</td>
                                <td>Strategic differentiation — genuine moat</td>
                            </tr>
                            <tr style="background: #dbeafe;">
                                <td>#1 Policy Interpretation</td>
                                <td>High value once docs are ingested</td>
                            </tr>
                            <tr style="background: #dbeafe;">
                                <td>#6 Audit Prep Automation</td>
                                <td>High customer demand</td>
                            </tr>
                            <tr style="background: #f3f4f6;">
                                <td rowspan="4"><strong>Tier 3: Evaluate Later</strong></td>
                                <td>#5 Corrective Action Drafting</td>
                                <td>Needs historical CAPA data first</td>
                            </tr>
                            <tr style="background: #f3f4f6;">
                                <td>#7 Customer Policy Mapping</td>
                                <td>Needs solid doc foundation</td>
                            </tr>
                            <tr style="background: #f3f4f6;">
                                <td>#8 Questionnaire Automation</td>
                                <td>Consider integration vs. build</td>
                            </tr>
                            <tr style="background: #f3f4f6;">
                                <td>#9 Smart Onboarding</td>
                                <td>Nice to have, not differentiator</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>'''

content = content.replace(old_prioritization, new_prioritization)

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done - reformatted Strategic Positioning and Prioritization as clean tables!')
