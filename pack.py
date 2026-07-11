import json
import re

def pack():
    # Read template.html
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print("Error: template.html not found.")
        return

    # Encode as JSON string
    template_json = json.dumps(template_content, ensure_ascii=False)

    # List of files to update
    target_files = ['index.html', 'index_new.html']

    for target in target_files:
        try:
            with open(target, 'r', encoding='utf-8') as f:
                index_content = f.read()
        except FileNotFoundError:
            print(f"Warning: {target} not found. Skipping.")
            continue

        # Replace the template script content
        pattern = r'(<script type=["\']__bundler/template["\']>)(.*?)(</script>)'
        
        def replace_template(match):
            return match.group(1) + template_json + match.group(3)

        new_index_content, count = re.subn(pattern, replace_template, index_content, flags=re.DOTALL)

        if count > 0:
            with open(target, 'w', encoding='utf-8') as f:
                f.write(new_index_content)
            print(f"template.html packed into {target} successfully.")
        else:
            print(f"Error: Template script tag not found in {target}.")

if __name__ == '__main__':
    pack()
