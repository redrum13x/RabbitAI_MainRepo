# Fix encoding issues in the HTML file
import re

# Read the original dark theme file (which has correct encoding)
with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Apply light theme CSS changes to the original (properly encoded) file
light_theme_vars = '''        :root {
            --primary: #ffffff;
            --secondary: #f8fafc;
            --tertiary: #e2e8f0;
            --accent: #2563eb;
            --accent-light: #1d4ed8;
            --accent-glow: rgba(37, 99, 235, 0.15);
            --success: #059669;
            --warning: #d97706;
            --text: #1e293b;
            --text-muted: #475569;
            --border: #cbd5e1;
            --card-bg: #ffffff;
            --gradient-start: #2563eb;
            --gradient-end: #7c3aed;
        }'''

# Replace CSS variables
content = re.sub(r':root \{[^}]+\}', light_theme_vars, original)

# Fix badge colors for light theme
content = content.replace('.badge-complexity-low { background: #065f46; color: #6ee7b7; }', '.badge-complexity-low { background: #d1fae5; color: #065f46; }')
content = content.replace('.badge-complexity-medium { background: #78350f; color: #fcd34d; }', '.badge-complexity-medium { background: #fef3c7; color: #92400e; }')
content = content.replace('.badge-complexity-high { background: #7f1d1d; color: #fca5a5; }', '.badge-complexity-high { background: #fee2e2; color: #991b1b; }')
content = content.replace('.badge-impact-high { background: #1e3a5f; color: #93c5fd; }', '.badge-impact-high { background: #dbeafe; color: #1e40af; }')
content = content.replace('.badge-impact-medium { background: #3f3f46; color: #d4d4d8; }', '.badge-impact-medium { background: #e5e7eb; color: #374151; }')
content = content.replace('.badge-proceed { background: #065f46; color: #6ee7b7; }', '.badge-proceed { background: #d1fae5; color: #065f46; }')
content = content.replace('.badge-evaluate { background: #78350f; color: #fcd34d; }', '.badge-evaluate { background: #fef3c7; color: #92400e; }')
content = content.replace('.badge-defer { background: #7f1d1d; color: #fca5a5; }', '.badge-defer { background: #fee2e2; color: #991b1b; }')

# Fix table header for light theme
content = content.replace(
    '''th {
            background: linear-gradient(135deg, var(--tertiary), var(--secondary));''',
    '''th {
            background: var(--accent);'''
)
content = content.replace('border-bottom: 2px solid var(--accent);', 'border-bottom: 2px solid var(--accent-light); color: white;')

# Fix hover for light theme
content = content.replace('tr:hover td {\n            background: var(--tertiary);', 'tr:hover td {\n            background: #f1f5f9;')

# Add shadows for depth on light background
content = content.replace(
    '''/* Cards */
        .card {
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border);
            margin-bottom: 1.5rem;
            overflow: hidden;
        }''',
    '''/* Cards */
        .card {
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border);
            margin-bottom: 1.5rem;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }'''
)

# Save with proper UTF-8 encoding
with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Light theme created with proper encoding!')
