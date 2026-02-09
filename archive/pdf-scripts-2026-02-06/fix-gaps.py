# Fix large gaps in PDF by adjusting page break behavior

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-v6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reduce section margins and allow better flow
content = content.replace(
    '''/* Sections */
            section {
                margin-bottom: 1.25rem;
                page-break-inside: avoid;
            }''',
    '''/* Sections */
            section {
                margin-bottom: 0.75rem;
            }'''
)

# Reduce header padding
content = content.replace(
    '''/* Clean Header */
            header {
                background: #ffffff !important;
                border-bottom: 2px solid #2563eb;
                padding: 1.5rem 0 1rem;
                margin-bottom: 1rem;
            }''',
    '''/* Clean Header */
            header {
                background: #ffffff !important;
                border-bottom: 2px solid #2563eb;
                padding: 1rem 0 0.75rem;
                margin-bottom: 0.5rem;
            }'''
)

# Reduce header title size
content = content.replace(
    '''header h1 {
                font-size: 24pt;
                font-weight: 600;
                color: #1a1a1a;
                margin-bottom: 0.25rem;
            }''',
    '''header h1 {
                font-size: 20pt;
                font-weight: 600;
                color: #1a1a1a;
                margin-bottom: 0.2rem;
            }'''
)

content = content.replace(
    '''header .subtitle {
                font-size: 14pt;
                color: #555;
                font-weight: 400;
            }''',
    '''header .subtitle {
                font-size: 12pt;
                color: #555;
                font-weight: 400;
            }'''
)

# Reduce opportunity margins
content = content.replace(
    '''/* Opportunities - Streamlined */
            .opportunity {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                margin-bottom: 1rem;
                page-break-inside: avoid;
                background: white !important;
            }''',
    '''/* Opportunities - Streamlined */
            .opportunity {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                margin-bottom: 0.6rem;
                background: white !important;
            }'''
)

# Reduce table margins
content = content.replace(
    '''/* Tables - Clean and Professional */
            .table-wrapper {
                margin: 0.75rem 0;
                border-radius: 0;
                border: none;
                box-shadow: none;
            }''',
    '''/* Tables - Clean and Professional */
            .table-wrapper {
                margin: 0.5rem 0;
                border-radius: 0;
                border: none;
                box-shadow: none;
            }'''
)

# Reduce h2 section title margins
content = content.replace(
    '''h2.section-title {
                font-size: 14pt;
                font-weight: 600;
                color: #1a1a1a;
                border-bottom: 1px solid #2563eb;
                margin-bottom: 0.75rem;
                padding-bottom: 0.35rem;
            }''',
    '''h2.section-title {
                font-size: 13pt;
                font-weight: 600;
                color: #1a1a1a;
                border-bottom: 1px solid #2563eb;
                margin-bottom: 0.5rem;
                padding-bottom: 0.25rem;
            }'''
)

# Reduce h3 margins
content = content.replace(
    '''h3 {
                font-size: 12pt;
                font-weight: 600;
                color: #2563eb;
                margin: 1rem 0 0.5rem;
            }''',
    '''h3 {
                font-size: 11pt;
                font-weight: 600;
                color: #2563eb;
                margin: 0.6rem 0 0.4rem;
            }'''
)

# Reduce context box margins
content = content.replace(
    '''/* Context Boxes */
            .context-box {
                background: #fafafa !important;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 0.6rem 0.8rem;
                margin: 0.75rem 0;
            }''',
    '''/* Context Boxes */
            .context-box {
                background: #fafafa !important;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 0.5rem 0.7rem;
                margin: 0.4rem 0;
            }'''
)

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-v6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed gaps - tightened spacing throughout')
