import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<script type="__bundler/template">(.*?)</script>'
match = re.search(pattern, content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    html_content = json.loads(json_str)
    with open('template.html', 'w', encoding='utf-8') as out:
        out.write(html_content)
    print("template.html unpacked successfully.")
else:
    print("Template not found.")
