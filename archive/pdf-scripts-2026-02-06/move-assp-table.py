with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The ASSP table to move
assp_table = '''<h4 style="color: var(--accent-light); margin: 1.5rem 0 1rem;">How ASSP Fits with Prioritized Opportunities</h4>
                            <div class="table-wrapper" style="margin-top: 0;">
                                <table>
                                    <thead>
                                        <tr><th>Opportunity</th><th>ASSP Relevance</th></tr>
                                    </thead>
                                    <tbody>
                                        <tr><td>Policy Interpretation</td><td>ASSP content becomes authoritative source for regulatory answers</td></tr>
                                        <tr><td>Document Ingestion</td><td>ASSP content is high-value input to the corpus</td></tr>
                                        <tr><td>Audit Prep</td><td>ASSP guidance on evidence requirements, common findings</td></tr>
                                        <tr><td>Customer Policy Mapping</td><td>Map ASSP best practices to customer-specific SOPs</td></tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            '''

# Remove the old ASSP Fits section from the ASSP Partnership area
old_assp_section = '''<h3>How ASSP Fits with Prioritized Opportunities</h3>
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>Opportunity</th>
                                <th>ASSP Relevance</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Policy Interpretation</strong></td>
                                <td>ASSP content becomes authoritative source for regulatory answers</td>
                            </tr>
                            <tr>
                                <td><strong>Document Ingestion</strong></td>
                                <td>ASSP content is high-value input to the corpus</td>
                            </tr>
                            <tr>
                                <td><strong>Audit Prep</strong></td>
                                <td>ASSP guidance on evidence requirements, common findings</td>
                            </tr>
                            <tr>
                                <td><strong>Customer Policy Mapping</strong></td>
                                <td>Map ASSP best practices to customer-specific SOPs</td>
                            </tr>
                        </tbody>
                    </table>
                </div>'''

content = content.replace(old_assp_section, '')

# Find where to insert in Policy Interpretation - after the competitive context table, before the badges
# Looking for the end of the competitive context table in opp1
insert_marker = '''<tr><td>Generic LLM tools</td><td>No access to customer documents; no regulatory accuracy</td></tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <div class="badges">'''

new_content = '''<tr><td>Generic LLM tools</td><td>No access to customer documents; no regulatory accuracy</td></tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            ''' + assp_table + '''<div class="badges">'''

content = content.replace(insert_marker, new_content)

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done - moved ASSP table into Policy Interpretation Engine!')
