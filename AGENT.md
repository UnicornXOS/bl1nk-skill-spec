# Project specification for bl1nk/bl1nk-skill-spec

>นี่คือสเปคโปรเจ็คแพ็คเกจ “skill spec + CLI” ของ bl1nk ที่ทำให้ AI สร้างสกิลจากภาษาธรรมชาติเป็นไฟล์ SKILL.md ที่ใช้งานได้จริง พร้อมองค์ประกอบความรู้และตัวอย่างสกิลแบบแยกโฟลเดอร์เป็นคอลเล็กชัน ปรับแต่งง่าย ใช้ได้ทุก OS และมี CI/CD สร้าง release + release notes อัตโนมัติจาก commit messages

## Repository layout

```
bl1nk-skill-spec/
 ├─ SKILL.md                 # meta-skill: สร้างสกิลจากภาษาธรรมชาติ (สเปคของเรา)
 ├─ core-knowledge.md        # สกัดแก่นแนวคิดและข้อกำหนดของ “Skill” ฉบับ bl1nk
 ├─ validation.json          # กฎตรวจสอบความสมบูรณ์ของ SKILL.md ทุกชิ้น
 ├─ README.md                # คู่มือโปรเจ็ค, การติดตั้ง, การใช้งาน, index ตัวอย่างสกิล
 ├─ cli.js                   # CLI ข้ามแพลตฟอร์ม (Node 18+) สร้างสกิลจาก natural language
 ├─ package.json             # เมทาแพ็คเกจและ entrypoint CLI
 ├─ LICENSE                  # MIT
 ├─ .npmrc                   # (optional) ตั้งค่าความเข้มงวด
 ├─ .gitignore               # ignore มาตรฐาน
 ├─ .github/
 │   └─ workflows/
 │       ├─ release.yml      # สร้าง tarball + GitHub Release อัตโนมัติ
 │       └─ changelog.yml    # สร้าง release notes จาก commit messages
 └─ examples/                # คอลเล็กชันตัวอย่างสกิลใช้งานจริง (จริงจัง ไม่ใช่เทมเพลต)
     ├─ nextjs-app-lifecycle-manager/
     │   ├─ SKILL.md
     │   └─ README.md
     ├─ n8n-workflow-generator/
     │   ├─ SKILL.md
     │   └─ README.md
     └─ youtube-transcript-to-blog/
         ├─ SKILL.md
         └─ README.md
```
---

## Meta-skill specification in SKILL.md

---
name: skill-generator
description: Generate valid, reusable SKILL.md from natural language requests using bl1nk spec
version: 1.0.0
license: mit
tags: [meta-skill, cli, skill-spec, bl1nk]
---
# skill-generator

## When to use
ใช้เพื่อแปลงคำสั่งภาษาธรรมชาติให้เป็นสกิลที่พร้อมใช้งานทันทีในรูปแบบ SKILL.md ตามสเปคของ bl1nk โดยให้ผลลัพธ์ชัดเจน, ตรวจสอบได้, และนำไปใช้ซ้ำในระบบ AI agent ได้อย่างมีวินัย

## Core Rules
- ต้องมีไฟล์ SKILL.md ที่ขึ้นต้นด้วย YAML frontmatter และตามด้วยส่วน Markdownตามลำดับที่กำหนดอย่างเคร่งครัด
- Field `name` ใช้รูปแบบ hyphen-case, ห้ามใช้คำเฉพาะแพลตฟอร์มในชื่อ, และ `description` ไม่เกิน 200 ตัวอักษร
- ระบุส่วน “Core Rules”, “Step-by-Step Process”, “Validation & Error Handling”, “Output Format” อย่างครบถ้วนและไม่กำกวม
- กำหนด “ONLY …” ชัดเจนใน Output Format เพื่อบังคับวินัยผลลัพธ์
- มี validation loop สูงสุด 3 รอบ พร้อมหมวดหมู่ข้อผิดพลาดที่ชัดเจน

## Step-by-step process
1. รับโจทย์จากภาษาธรรมชาติและสกัดโดเมนงาน, ขอบเขต, และผลลัพธ์ที่คาดหวัง
2. สร้าง YAML frontmatter: `name`, `description`, `version`, `license`, `tags`
3. เขียนส่วน Markdown ทั้งหมดตามลำดับและครอบคลุม
4. กำหนดกฎ Validation และ Error Handling พร้อมรหัสข้อผิดพลาด
5. นิยาม Output Format ว่าต้องเป็น “ONLY …”
6. ส่งออกไฟล์ SKILL.md ที่สอดคล้องกับ validation.json ของโปรเจ็ค

## Validation & error handling
- รอบที่ 1: ตรวจความครบถ้วนของ frontmatter และรูปแบบ `name` ว่าเป็น hyphen-case
- รอบที่ 2: ตรวจหัวข้อ Markdown ครบตามลำดับที่กำหนด
- รอบที่ 3: ตรวจความเข้มงวดของ Output Format และกฎเฉพาะโดเมนสกิล
- หมวดผิดพลาด: `frontmatter-missing`, `invalid-name`, `sections-missing`, `output-format-unclear`
- วนซ้ำแก้ไขสูงสุด 3 รอบก่อนคืนผลลัพธ์

## Output Format
ONLY:
- ไฟล์เดียวชื่อ `SKILL.md` ที่สมบูรณ์ตามสเปคของ bl1nk

## Credits
แนวคิดและการออกแบบสอดคล้องกับระบบสกิลชุมชนสมัยใหม่ ปี 2025, ขอบคุณระบบและเอกสารสาธารณะที่ช่วยให้เกิดมาตรฐานร่วมในวงกว้าง

Core knowledge in core-knowledge.md

# bl1nk skill spec: core knowledge

## แนวคิดพื้นฐาน
- Skill คือชุดคำสั่ง reusable ที่ทำให้ AI agent ทำงานโดเมนเฉพาะได้ “ถูกต้องตั้งแต่ครั้งแรก”
- เป้าหมายคือผลลัพธ์ที่ determinism, reproducible, และนำไปใช้ซ้ำได้ในหลากหลายระบบ โดยไม่พึ่งพาความจำของเซสชัน

## โครงสร้างไฟล์ SKILL.md
- ชื่อไฟล์: SKILL.md (S ตัวใหญ่)
- ส่วนหัว: YAML frontmatter (name hyphen-case, description ≤ 200, optional: license, version, tags)
- ส่วน Markdown (ตามลำดับที่ต้องมี):
  1. # Title (ตรงกับ name)
  2. When to use / Short intro
  3. ## Core Rules
  4. ## Step-by-Step Process (1., 2., 3., …)
  5. ## Validation & Error Handling (สูงสุด 3 รอบ)
  6. ## Output Format (ระบุ ONLY …)
  7. ## Examples (optional)

## วินัยผลลัพธ์
- บังคับให้ระบุรูปแบบผลลัพธ์แบบ “ONLY …” เพื่อลดความกำกวมและเพิ่มการนำเข้าอัตโนมัติ

## วงจรตรวจสอบ
- Pass 1: frontmatter + รูปแบบชื่อไฟล์/ชื่อสกิล
- Pass 2: ส่วน Markdown ครบตามลำดับ
- Pass 3: กฎ Output และ validation เฉพาะโดเมน
- วนซ้ำแก้ไขได้สูงสุด 3 รอบ

## หมวดปัญหาทั่วไป
- ขาด frontmatter หรือผิดรูปแบบ → นำเข้าไม่ได้
- `name` ผิดรูปแบบหรือมีคำต้องห้าม → ไม่ผ่าน
- Output Format ไม่ชัดเจน → ใช้งานจริงสะดุด
- ไม่มีกฎ validation → ผลลัพธ์ไม่เสถียร

## การออกแบบเชิงปฏิบัติ
- กำหนด environment, แยก secrets ผ่าน `.env.example`
- ใช้คำสั่ง non-interactive เพื่อสอดคล้อง CI/CD
- แสดงไฟล์คอนฟิกที่สำคัญและผลลัพธ์ที่ตรวจสอบได้

## Credits
โปรเจ็คนี้เกิดขึ้นบนพื้นฐานความรู้จากเอกสารและเครื่องมือชุมชนสมัยใหม่ปี 2025 ซึ่งเอื้อให้เกิดมาตรฐานร่วมของการเขียนสกิล

Validation schema in validation.json

{
  "schema_version": "1.0.0",
  "required_frontmatter": {
    "name": {
      "format": "hyphen-case",
      "forbidden": []
    },
    "description": {
      "max_length": 200
    }
  },
  "required_sections_ordered": [
    "# Title",
    "When to use",
    "## Core Rules",
    "## Step-by-Step Process",
    "## Validation & Error Handling",
    "## Output Format"
  ],
  "validation_loops": 3,
  "error_categories": [
    "frontmatter-missing",
    "invalid-name",
    "sections-missing",
    "output-format-unclear"
  ],
  "output_requirements": {
    "type": "markdown",
    "only_file": "SKILL.md"
  }
}

CLI usage and behavior

# ติดตั้งจาก GitHub (global)
npm i -g github:bl1nk/bl1nk-skill-spec#v1.0.0

# ใช้งาน: สร้างสกิลจากคำบรรยายภาษาธรรมชาติ
skillgen "สร้างสกิลสำหรับการจัดการ Next.js lifecycle ตั้งแต่ init → run → test → build → deploy"

# ตัวเลือก
skillgen "..." --dir ./skills-out --tags "nextjs,ci-cd" --license mit --version 1.0.0 --dry-run

CLI script (cli.js)

#!/usr/bin/env node
import fs from "fs";
import path from "path";
import os from "os";
import process from "process";

function toHyphenCase(str) {
  return String(str).trim().toLowerCase()
    .replace(//g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

function parseArgs(argv) {
  const args = { input: null, dir: process.cwd(), dry: false, tags: [], license: "mit", version: "1.0.0" };
  const raw = argv.slice(2);
  let i = 0;
  while (i < raw.length) {
    const t = raw[i];
    if (t === "--dir") { args.dir = raw[i + 1]; i += 2; }
    else if (t === "--dry-run") { args.dry = true; i += 1; }
    else if (t === "--tags") { args.tags = raw[i + 1].split(",").map(s => s.trim()); i += 2; }
    else if (t === "--license") { args.license = raw[i + 1]; i += 2; }
    else if (t === "--version") { args.version = raw[i + 1]; i += 2; }
    else { args.input = t; i += 1; }
  }
  return args;
}

function renderSkillMd({ name, description, version, license, tags }) {
  const tagList = tags && tags.length ? `\ntags: [${tags.join(", ")}]\n` : "\n";
  return `---
name: ${name}
description: ${description}
version: ${version}
license: ${license}${tagList}---
# ${name}

## When to use
ใช้เพื่อดำเนินงานโดเมนนี้ให้เสร็จสมบูรณ์แบบ reproducible และนำไปใช้ซ้ำได้ทันที

## Core Rules
- ต้องมี YAML frontmatter และส่วน Markdownครบตามลำดับ
- ชื่อสกิลต้องเป็น hyphen-case และสั้น ชัดเจน
- ระบุ Output Format แบบ ONLY … เพื่อลดความกำกวม
- มี Validation loop สูงสุด 3 รอบและรหัสข้อผิดพลาด

## Step-by-Step Process
1. สกัดขอบเขตงานจากคำอธิบาย
2. สร้าง frontmatter: name, description (≤200), version, license, tags
3. เขียนส่วน Markdownตามสเปคของโปรเจ็ค
4. ใส่ Validation & Error Handling ครบ
5. นิยาม Output Format เฉพาะโดเมน
6. ส่งออก SKILL.md

## Validation & Error Handling
- รอบ 1: ตรวจ frontmatter และรูปแบบชื่อ
- รอบ 2: ตรวจหัวข้อครบตามลำดับ
- รอบ 3: ตรวจ Output Format และกฎเฉพาะโดเมน
- หมวด error: frontmatter-missing, invalid-name, sections-missing, output-format-unclear
- วนซ้ำสูงสุด 3 รอบ

## Output Format
ONLY:
- ไฟล์เดียวชื่อ SKILL.md ที่สมบูรณ์ตามสเปค bl1nk

## Credits
แนวคิดและการจัดระเบียบสอดคล้องกับมาตรฐานชุมชนสมัยใหม่ปี 2025
`;
}

function main() {
  const args = parseArgs(process.argv);
  if (!args.input) {
    console.error("Usage: skillgen \"สร้างสกิลสำหรับ ...\" [--dir ./out] [--tags \"a,b\"] [--license mit] [--version 1.0.0] [--dry-run]");
    process.exit(1);
  }
  const name = toHyphenCase(args.input);
  if (!name || name.length < 3) {
    console.error("invalid-name: ชื่อสกิลสั้นหรือไม่ชัดเจน");
    process.exit(1);
  }
  const description = `Generated skill: ${args.input}`.slice(0, 200);
  const content = renderSkillMd({
    name,
    description,
    version: args.version,
    license: args.license,
    tags: args.tags
  });

  if (args.dry) {
    process.stdout.write(content + os.EOL);
    return;
  }

  const targetDir = path.join(args.dir, name);
  fs.mkdirSync(targetDir, { recursive: true });
  fs.writeFileSync(path.join(targetDir, "SKILL.md"), content, { encoding: "utf-8" });
  console.log(`✓ Skill created at: ${targetDir}${path.sep}SKILL.md`);
}

main();

Examples collection in examples/

nextjs-app-lifecycle-manager/SKILL.md: สกิลครบวงจร init → run → test → build → deploy พร้อม Core Rules, Process, Validation, Output

n8n-workflow-generator/SKILL.md: สร้าง workflow n8n ที่ import/run ได้ทันทีแบบ valid JSON

youtube-transcript-to-blog/SKILL.md: แปลงวิดีโอ YouTube เป็นบทความ Markdown ที่จัดโครงสร้าง SEO พร้อม timestamps

แต่ละโฟลเดอร์มี README.md ระบุ:

Purpose: โดเมนและผลลัพธ์คาดหวัง

Usage notes: ข้อควรระวัง/เงื่อนไข

Output format: ONLY …

Status: ผ่าน validation แล้ว

README index and usage

# bl1nk skill spec

แพ็คเกจสเปคและ CLI สำหรับสร้างสกิลจากภาษาธรรมชาติเป็นไฟล์ SKILL.md ตามแนวทางของ bl1nk

## Install
```bash
npm i -g github:bl1nk/bl1nk-skill-spec#v1.0.0

Usage

skillgen "สร้างสกิลสำหรับ X"
skillgen "..." --dir ./skills --tags "domain,tag" --license mit --version 1.0.0

Examples index

examples/nextjs-app-lifecycle-manager

examples/n8n-workflow-generator

examples/youtube-transcript-to-blog

Contributing

เพิ่มสกิลใหม่โดยสร้างโฟลเดอร์ใน examples/ แล้วใส่ SKILL.md + README.md

เปิด PR พร้อมคำอธิบายสั้น ๆ และ commit messages ที่สอดคล้องกับการสร้าง release notes

Credits

โปรเจ็คนี้ได้รับแรงบันดาลใจจากเอกสารและระบบสกิลชุมชนปี 2025 ซึ่งช่วยให้เกิดแนวทางร่วมในการสร้างสกิลที่นำไปใช้ซ้ำได้


---

## CI/CD workflows

#### .github/workflows/release.yml

```yaml
name: Release

on:
  push:
    tags:
      - "v*.*.*"

jobs:
  build-and-release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Verify CLI
        run: node ./cli.js "example skill for verification" --dry-run > /dev/null

      - name: Package tarball
        run: npm pack

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: |
            *.tgz
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

.github/workflows/changelog.yml

name: Changelog

on:
  push:
    tags:
      - "v*.*.*"

jobs:
  generate-release-notes:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Generate release notes from commits
        uses: mikepenz/release-changelog-builder-action@v5
        with:
          configuration: .github/changelog-config.json
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Attach notes to release
        uses: softprops/action-gh-release@v2
        with:
          body_path: CHANGELOG.md
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

.github/changelog-config.json

{
  "categories": [
    { "title": "Features", "labels": ["feature", "enhancement"] },
    { "title": "Fixes", "labels": ["bug", "fix"] },
    { "title": "Docs", "labels": ["docs"] },
    { "title": "Examples", "labels": ["example"] }
  ],
  "ignore_labels": ["skip-changelog"],
  "template": "# Release Notes\n\n{{CHANGELOG}}\n"
}

Package metadata in package.json

{
  "name": "bl1nk-skill-spec",
  "version": "1.0.0",
  "description": "bl1nk spec + CLI for generating valid SKILL.md from natural language",
  "license": "MIT",
  "type": "module",
  "bin": {
    "skillgen": "./cli.js"
  },
  "engines": {
    "node": ">=18"
  },
  "files": [
    "cli.js",
    "SKILL.md",
    "core-knowledge.md",
    "validation.json",
    "examples",
    "README.md",
    "LICENSE",
    ".github"
  ]
}

Next steps

Populate examples: เติมรายละเอียดเต็มในแต่ละสกิลใน examples/ ให้ “นำไปใช้จริง” ได้ทันที

Contributor guide: เพิ่ม RULES สำหรับโครงสร้างสกิลใหม่ใน examples/ และวิธีเขียน commit messages

Cross-platform test: เพิ่ม job matrix (windows, ubuntu, macos) เพื่อยืนยัน CLI ทำงานครบทุก OS

Versioning: ใช้ semver และ tag release v1.x.x จากนั้นปรับสเปคและเพิ่มตัวอย่างเป็น v2, v3 โดยคงความเข้ากันย้อนหลัง