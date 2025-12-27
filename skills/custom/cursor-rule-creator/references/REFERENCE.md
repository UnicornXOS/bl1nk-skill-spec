### YAML Frontmatter Schema
```yaml
---
description: ชื่อสั้น ≤50 ตัวอักษร (Required)
globs: []  # Specific patterns เท่านั้น (Recommended)
alwaysApply: false  # true สำหรับ core rules เท่านั้น
tags: []  # language:ts, category:security (Optional)
---
```

### Quality Checklist
| เกณฑ์ | Pass Criteria | Check Command |
|--------|---------------|---------------|
| YAML Valid | 100% files | `yq eval . *.mdc` |
| Glob Specific | No `**/*` | Manual review |
| Length | <300 lines/file | `wc -l *.mdc` |
| Instructions | Bullet points, imperative | Manual |
| Structure | H1 title + bullets | Manual |

### Glob Pattern Best Practices
```
✅ GOOD:
- "src/**/*.ts"  # Specific directory
- "*.py"         # Single extension
- "modules/**/*.php"

❌ BAD:
- "**/*"         # Too broad
- "*"            # Too broad
```

### Common Tags
```
language: [ts, js, py, php, go]
category: [core, security, performance, testing, docs]
framework: [react, vue, drupal, nextjs]
```

## 4. Bash One-liner สำหรับ Repo Audit
```bash
# Quick quality check
find .cursor/rules -name "*.mdc" | wc -l && \
echo "YAML valid:" && grep -l "^---" .cursor/rules/*.mdc | wc -l && \
echo "Avg length:" && awk '{sum+=$1} END {print sum/NR}' <(wc -l .cursor/rules/*.mdc | tail -n+2)
```

## การ Deploy Toolkit
1. `mkdir cursor-rules-toolkit && cd cursor-rules-toolkit`
2. Copy 3 ไฟล์ด้านบน
3. `chmod +x *.py`
4. `./create-rule.py "My Rule" '["src/**/*.js"]' js core`
5. `python audit-rules.py`

**Metrics Target**: Quality Score >85/100 ถือว่าพร้อม production.