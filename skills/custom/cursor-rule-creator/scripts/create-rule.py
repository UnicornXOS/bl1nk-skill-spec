#!/usr/bin/env python3
import os
from pathlib import Path

TEMPLATE = """---
description: {description}
globs: 
  {globs}
alwaysApply: {always_apply}
tags:
  - language:{language}
  - category:{category}
---
# {title}

{body}
"""

def create_rule(name, description, globs, language="general", category="core", always_apply=False, body=""):
    rules_dir = Path(".cursor/rules")
    rules_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{name.replace(' ', '-')}.mdc".lower()
    filepath = rules_dir / filename
    
    globs_str = "
  ".join(f"- "{g}"" for g in globs)
    
    content = TEMPLATE.format(
        description=description,
        globs=globs_str,
        always_apply=str(always_apply).lower(),
        language=language,
        category=category,
        title=name.title(),
        body=body or f"- Add your instructions here
- Use bullet points
- Keep <100 chars/line"
    )
    
    filepath.write_text(content)
    print(f"✅ Created {filepath}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python create-rule.py 'React Hooks' '["src/**/*.tsx"]' ts react")
        sys.exit(1)
    
    create_rule(sys.argv[1], sys.argv[1], eval(sys.argv[2]), sys.argv[3] if len(sys.argv)>3 else "general", sys.argv[4] if len(sys.argv)>4 else "core")