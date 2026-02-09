# Create v6 with professional styling and Vera -> Vēlo fix

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-v5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Vera -> Vēlo (with macron over e)
content = content.replace('"Vera"', '"Vēlo"')
content = content.replace("'Vera'", "'Vēlo'")
content = content.replace('Vera ', 'Vēlo ')
content = content.replace(' Vera', ' Vēlo')

# Now let's create professional print styles
old_print = '''/* Print Styles */
        @media print {
            * {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            
            body {
                background: white;
                color: #1a1a1a;
                font-size: 10pt;
                line-height: 1.4;
            }
            
            .sidebar, .back-to-top {
                display: none !important;
            }
            
            .layout {
                display: block;
            }
            
            .main {
                padding: 0.5rem 1rem;
            }
            
            header {
                background: #ffffff !important;
                border-bottom: 1px solid #ccc;
                padding: 1rem;
            }
            
            header h1 {
                font-size: 1.5rem;
                margin-bottom: 0.25rem;
            }
            
            header .subtitle {
                font-size: 1rem;
            }
            
            header .meta {
                font-size: 0.8rem;
                margin-top: 0.5rem;
            }
            
            section {
                margin-bottom: 1rem;
            }
            
            h2.section-title {
                font-size: 1.1rem;
                color: #1a1a1a;
                border-color: #2563eb;
                margin-bottom: 0.75rem;
                padding-bottom: 0.25rem;
            }
            
            h3 {
                font-size: 0.95rem;
                color: #2563eb;
                margin: 0.75rem 0 0.5rem;
            }
            
            h4 {
                font-size: 0.9rem;
            }
            
            p {
                margin-bottom: 0.5rem;
                font-size: 10pt;
            }
            
            .card, .opportunity, .context-box, .table-wrapper, .scoring-key, .tldr-box {
                break-inside: avoid;
                page-break-inside: avoid;
                border: 1px solid #ddd;
                background: #fafafa !important;
                margin-bottom: 0.5rem;
            }
            
            .opportunity {
                border: 1px solid #ddd;
                margin-bottom: 0.75rem;
            }
            
            .opportunity-header {
                padding: 0.5rem 0.75rem;
            }
            
            .opportunity-body {
                padding: 0.5rem 0.75rem;
            }
            
            .opportunity.open .opportunity-content,
            .opportunity-content {
                max-height: none !important;
            }
            
            .tldr-box {
                padding: 0.5rem 0.75rem;
                margin: 0.5rem 0;
                font-size: 9.5pt;
            }
            
            .opportunity-body dl {
                gap: 0.25rem 0.75rem;
                margin-top: 0.5rem;
            }
            
            .opportunity-body dt {
                font-size: 9pt;
            }
            
            .opportunity-body dd {
                font-size: 9.5pt;
            }
            
            .table-wrapper {
                margin: 0.5rem 0;
            }
            
            table {
                font-size: 9pt;
            }
            
            th {
                background: #2563eb !important;
                color: white !important;
                padding: 0.4rem 0.5rem;
                font-size: 9pt;
            }
            
            td {
                padding: 0.35rem 0.5rem;
                font-size: 9pt;
            }
            
            .context-box {
                padding: 0.5rem 0.75rem;
            }
            
            .context-box li {
                padding: 0.2rem 0;
                font-size: 9.5pt;
            }
            
            .badges {
                margin-top: 0.5rem;
                gap: 0.25rem;
            }
            
            .badge {
                font-size: 8pt;
                padding: 0.15rem 0.5rem;
                border: 1px solid #999;
            }
            
            .scoring-key {
                padding: 0.5rem 0.75rem;
            }
            
            .scoring-key ul {
                gap: 0.25rem;
            }
            
            .scoring-key li {
                font-size: 9pt;
            }
            
            footer {
                padding: 0.5rem;
                font-size: 8pt;
            }
        }'''

new_print = '''/* Print Styles - Professional */
        @media print {
            * {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            
            body {
                background: white;
                color: #222;
                font-size: 11pt;
                line-height: 1.5;
                font-family: 'Segoe UI', Calibri, Arial, sans-serif;
            }
            
            .sidebar, .back-to-top {
                display: none !important;
            }
            
            .layout {
                display: block;
            }
            
            .main {
                padding: 0;
                max-width: 100%;
            }
            
            /* Clean Header */
            header {
                background: #ffffff !important;
                border-bottom: 2px solid #2563eb;
                padding: 1.5rem 0 1rem;
                margin-bottom: 1rem;
            }
            
            header h1 {
                font-size: 24pt;
                font-weight: 600;
                color: #1a1a1a;
                margin-bottom: 0.25rem;
            }
            
            header .subtitle {
                font-size: 14pt;
                color: #555;
                font-weight: 400;
            }
            
            header .meta {
                font-size: 10pt;
                color: #666;
                margin-top: 0.5rem;
            }
            
            /* Sections */
            section {
                margin-bottom: 1.25rem;
                page-break-inside: avoid;
            }
            
            h2.section-title {
                font-size: 14pt;
                font-weight: 600;
                color: #1a1a1a;
                border-bottom: 1px solid #2563eb;
                margin-bottom: 0.75rem;
                padding-bottom: 0.35rem;
            }
            
            h3 {
                font-size: 12pt;
                font-weight: 600;
                color: #2563eb;
                margin: 1rem 0 0.5rem;
            }
            
            h4 {
                font-size: 11pt;
                font-weight: 600;
                color: #333;
            }
            
            p {
                margin-bottom: 0.5rem;
                color: #333;
            }
            
            /* Tables - Clean and Professional */
            .table-wrapper {
                margin: 0.75rem 0;
                border-radius: 0;
                border: none;
                box-shadow: none;
            }
            
            table {
                width: 100%;
                border-collapse: collapse;
                font-size: 10pt;
            }
            
            th {
                background: #2563eb !important;
                color: white !important;
                padding: 0.5rem 0.6rem;
                font-size: 10pt;
                font-weight: 600;
                text-align: left;
                border: 1px solid #1d4ed8;
            }
            
            td {
                padding: 0.45rem 0.6rem;
                font-size: 10pt;
                border: 1px solid #ddd;
                color: #333;
            }
            
            tr:nth-child(even) td {
                background: #f8f9fa;
            }
            
            /* Opportunities - Streamlined */
            .opportunity {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                margin-bottom: 1rem;
                page-break-inside: avoid;
                background: white !important;
            }
            
            .opportunity-header {
                padding: 0.6rem 0.8rem;
                background: #f5f5f5 !important;
                border-bottom: 1px solid #e0e0e0;
            }
            
            .opportunity-header h4 {
                font-size: 11pt;
                color: #1a1a1a;
            }
            
            .opportunity-num {
                background: #2563eb !important;
                color: white !important;
                font-size: 9pt;
                width: 22px;
                height: 22px;
            }
            
            .opportunity-toggle {
                display: none;
            }
            
            .opportunity-body {
                padding: 0.6rem 0.8rem;
            }
            
            .opportunity.open .opportunity-content,
            .opportunity-content {
                max-height: none !important;
            }
            
            /* TLDR Box */
            .tldr-box {
                background: #f0f7ff !important;
                border: 1px solid #bfdbfe;
                border-left: 3px solid #2563eb;
                padding: 0.6rem 0.8rem;
                margin: 0.5rem 0;
                font-size: 10pt;
                border-radius: 0 4px 4px 0;
            }
            
            .tldr-box strong {
                color: #1d4ed8;
            }
            
            /* Definition Lists */
            .opportunity-body dl {
                display: grid;
                grid-template-columns: 80px 1fr;
                gap: 0.3rem 0.75rem;
                margin-top: 0.5rem;
                font-size: 10pt;
            }
            
            .opportunity-body dt {
                font-weight: 600;
                color: #2563eb;
                font-size: 9pt;
            }
            
            .opportunity-body dd {
                color: #444;
                font-size: 10pt;
            }
            
            /* Context Boxes */
            .context-box {
                background: #fafafa !important;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 0.6rem 0.8rem;
                margin: 0.75rem 0;
            }
            
            .context-box p {
                font-weight: 600;
                margin-bottom: 0.4rem;
            }
            
            .context-box ul {
                margin: 0;
                padding-left: 1.2rem;
            }
            
            .context-box li {
                padding: 0.2rem 0;
                font-size: 10pt;
                color: #444;
            }
            
            .context-box li::before {
                display: none;
            }
            
            /* Badges - Inline and Clean */
            .badges {
                margin-top: 0.6rem;
                gap: 0.3rem;
            }
            
            .badge {
                font-size: 8pt;
                padding: 0.2rem 0.5rem;
                border-radius: 3px;
                font-weight: 500;
            }
            
            .badge-complexity-low, .badge-proceed { 
                background: #dcfce7 !important; 
                color: #166534 !important;
                border: 1px solid #86efac;
            }
            .badge-complexity-medium, .badge-evaluate { 
                background: #fef9c3 !important; 
                color: #854d0e !important;
                border: 1px solid #fde047;
            }
            .badge-complexity-high, .badge-defer { 
                background: #fee2e2 !important; 
                color: #991b1b !important;
                border: 1px solid #fca5a5;
            }
            .badge-impact-high { 
                background: #dbeafe !important; 
                color: #1e40af !important;
                border: 1px solid #93c5fd;
            }
            .badge-impact-medium { 
                background: #f3f4f6 !important; 
                color: #374151 !important;
                border: 1px solid #d1d5db;
            }
            
            /* Scoring Key */
            .scoring-key {
                background: #f8f9fa !important;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 0.6rem 0.8rem;
            }
            
            .scoring-key h4 {
                font-size: 10pt;
                margin-bottom: 0.4rem;
            }
            
            .scoring-key ul {
                display: flex;
                flex-wrap: wrap;
                gap: 0.5rem 1.5rem;
            }
            
            .scoring-key li {
                font-size: 9pt;
                color: #555;
            }
            
            /* Footer */
            footer {
                margin-top: 1.5rem;
                padding: 0.75rem 0;
                border-top: 1px solid #e0e0e0;
                font-size: 9pt;
                color: #666;
            }
        }'''

content = content.replace(old_print, new_print)

with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-v6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('v6 created with professional styling!')
