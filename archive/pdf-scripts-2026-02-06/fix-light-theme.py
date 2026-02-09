import re

# Read the light theme file
with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove emojis EXCEPT 🟢 🟡 🔴
# Common emojis in the doc: 📌 📋 🏢 🔮 📈 🎯 📊 🏆 ⭐ 📝 🏭 🤝 🔄
emojis_to_remove = ['📌', '📋', '🏢', '🔮', '📈', '🎯', '📊', '🏆', '⭐', '📝', '🏭', '🤝', '🔄', '▼']
for emoji in emojis_to_remove:
    content = content.replace(emoji + ' ', '')  # emoji with space after
    content = content.replace(' ' + emoji, '')  # space before emoji
    content = content.replace(emoji, '')  # just the emoji

# Make header white instead of gradient
content = content.replace(
    '''header {
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
            padding: 3rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }''',
    '''header {
            background: #ffffff;
            padding: 3rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            border-bottom: 1px solid var(--border);
        }'''
)

# Remove the header pattern overlay since we're going white
content = content.replace(
    '''header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            opacity: 0.5;
        }''',
    '''header::before {
            display: none;
        }'''
)

# Fix header text color for white background (was white text, needs to be dark now)
content = content.replace(
    '''header h1 {
            font-size: 2.75rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            position: relative;
        }''',
    '''header h1 {
            font-size: 2.75rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: var(--text);
            position: relative;
        }'''
)

content = content.replace(
    '''header .subtitle {
            font-size: 1.25rem;
            opacity: 0.9;
            position: relative;
        }''',
    '''header .subtitle {
            font-size: 1.25rem;
            color: var(--text-muted);
            position: relative;
        }'''
)

content = content.replace(
    '''header .meta {
            margin-top: 1rem;
            font-size: 0.9rem;
            opacity: 0.75;
            position: relative;
        }''',
    '''header .meta {
            margin-top: 1rem;
            font-size: 0.9rem;
            color: var(--text-muted);
            position: relative;
        }'''
)

# Save
with open(r'C:\Users\Grant\.openclaw\workspace-private\novara-ai\ai-opportunities-exec-summary-light.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done - removed emojis and made header white!')
