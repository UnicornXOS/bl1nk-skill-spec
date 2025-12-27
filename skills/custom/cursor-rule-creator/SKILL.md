# Cursor Rule Creator Skill

Cursor rules ในโฟลเดอร์ `.cursor/rules` (ไฟล์ `.mdc`) ช่วยกำหนดพฤติกรรม AI ใน Cursor IDE ให้ตรงตาม coding standards และ workflows ของโปรเจกต์ โดยใช้ YAML frontmatter + Markdown instructions.

## Prerequisites
- ติดตั้ง Cursor IDE ล่าสุด
- เข้าใจ glob patterns (e.g. `src/**/*.ts`)
- Repo references: ivangrynenko/cursorrules, sparesparrow/cursor-rules

## Step 1: Repo Selection Criteria
เลือก repo คุณภาพสูงด้วยเมตริกเชิงเทคนิคเพื่อศึกษาตัวอย่าง:

| เมตริก | เกณฑ์ขั้นต่ำ | คำสั่งตรวจสอบ |
|--------|---------------|---------------|
| Stars/Forks | 100+/20+ | GitHub UI |
| .mdc Files | ≥20 | `find .cursor/rules -name "*.mdc" | wc -l` |
| YAML Coverage | >95% | Manual scan |
| Last Commit | <6 เดือน | `git log -1` |
| Rule Length Avg | <300 lines/file | `awk '{sum+=$1} END {print sum/NR}' <(grep -c '^' *.mdc)`

## Step 2: Rule File Structure
ทุกไฟล์ `.mdc` ต้องมีโครงสร้างนี้:

```
---
description: ชื่อสั้นๆ ของ rule (≤50 ตัวอักษร)
globs: 
  - "src/**/*.ts" 
  - "*.py"
alwaysApply: false
---
# Optional: Title

- Instruction 1: ใช้ imperative voice สั้นๆ (<80 ตัวอักษร)
- Instruction 2: Specific, actionable
- NEVER: หลีกเลี่ยงคำสั่งนี้เสมอ
```

**YAML Validation Checklist**:
- description: Required, descriptive
- globs: Specific patterns (no `**/*`)
- alwaysApply: false เว้นแต่ core rules

## Step 3: Writing Principles
จากวิเคราะห์ 20-30 rules ดีๆ พบ patterns หลัก:

### Core Principles
- **Specificity**: Glob patterns แคบ, e.g. `modules/**/*.php` ไม่ใช่ `*.php`
- **Clarity**: Bullet points imperative: "Use snake_case for variables"
- **Brevity**: <300 lines/file, <100 chars/line
- **Categorization**: Folder structure `.cursor/rules/{core,security,react}`

### Quality Metrics Checklist
```
✅ YAML frontmatter ครบ 100%
✅ Instructions เป็น bullet points >90%
✅ Glob specificity score >80% (no broad patterns)
✅ No overlapping globs ระหว่าง rules
✅ Tags: language:ts, category:security
```

## Step 4: Example Rules
```
# .cursor/rules/react-hooks.mdc
---
description: React Hooks best practices
globs: ["src/**/*.tsx", "components/**/*.ts"]
alwaysApply: false
---
- Always use functional components with hooks
- Prefer useCallback for event handlers
- Never call hooks inside loops/conditions
- Use ESLint react-hooks/exhaustive-deps
```

```
# .cursor/rules/git-commit.mdc
---
description: Conventional Commits
globs: ["**/*.md", "*.ts"]
alwaysApply: true
---
- Use conventional commits: feat:, fix:, chore:
- Max 72 chars subject line
- Body: explain WHY, not WHAT
```

## Step 5: Validation & Deployment
1. **Local Test**: Clone repo → `cp -r .cursor/rules ./myproject/` → Cursor Chat ในไฟล์ target
2. **Metrics Audit**:
   ```bash
   # Count rules
   find .cursor/rules -name "*.mdc" | wc -l
   
   # Validate YAML
   yq eval . *.mdc
   
   # Length check
   for f in .cursor/rules/*.mdc; do echo "$f: $(wc -l < $f)"; done
   ```
3. **Install**: Git submodule หรือ copy + `.cursorignore` (exclude node_modules)
4. **Performance**: Rules >500 lines ลบหรือ split

## Advanced Patterns
- **Security**: OWASP Top 10 rules (SQL injection, XSS)
- **Framework**: Language-specific (React, Drupal, Python)
- **Automation**: Installer scripts ใน repo

**Skill Mastery**: สร้าง rule set 20+ ไฟล์ผ่าน metrics >90% แล้ว deploy ใน production project.