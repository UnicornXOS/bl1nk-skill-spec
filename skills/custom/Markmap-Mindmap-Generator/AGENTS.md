# AGENTS

---

## 1️⃣ pyproject.toml
````artifact
id: mmg_pyproject
name: pyproject.toml
type: code.toml
content: |-
  [build-system]
  requires = ["setuptools>=45", "wheel"]
  build-backend = "setuptools.build_meta"

  [project]
  name = "mmg"
  version = "1.0.0"
  description = "Markmap Mindmap Generator - Create beautiful mindmaps from templates"
  readme = "README.md"
  requires-python = ">=3.8"
  license = {text = "MIT"}
  authors = [
      {name = "MMG Team", email = "info@mmg.dev"}
  ]
  keywords = ["mindmap", "markmap", "generator", "template"]
  classifiers = [
      "Development Status :: 4 - Beta",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3.11",
  ]

  dependencies = [
      "pyyaml>=6.0",
      "click>=8.0",
  ]

  [project.optional-dependencies]
  dev = [
      "pytest>=7.0",
      "black>=22.0",
      "flake8>=4.0",
  ]

  [project.scripts]
  mmg = "mmg.cli:main"

  [tool.setuptools]
  packages = ["mmg"]

  [tool.setuptools.package-data]
  mmg = [
      "templates/*.yaml",
      "assets/*.js",
      "assets/*.css",
  ]

  [tool.black]
  line-length = 100
  target-version = ['py38']

  [tool.pytest.ini_options]
  testpaths = ["tests"]
  python_files = "test_*.py"
````

---

## 2️⃣ mmg/cli.py
````artifact
id: mmg_cli
name: mmg/cli.py
type: code.python
content: |-
  import click
  import os
  import sys
  from pathlib import Path
  from .generator import MarkmapGenerator
  from .html_export import HTMLExporter
  from .interactive import InteractiveMode

  @click.group()
  def cli():
      """MMG - Markmap Mindmap Generator"""
      pass

  @cli.command()
  def list_templates():
      """List all available templates"""
      click.echo("\n📋 Available Templates:\n")
      templates = MarkmapGenerator.get_available_templates()
      for i, template in enumerate(templates, 1):
          click.echo(f"  {i}. {template}")
      click.echo()

  @cli.command()
  @click.option('--type', '-t', default='novel', help='Template type')
  @click.option('--output', '-o', default=None, help='Output filename')
  @click.option('--add', '-a', multiple=True, help='Add custom sections (e.g., --add "Section:Item1,Item2")')
  @click.option('--html', is_flag=True, help='Export as HTML')
  @click.option('--theme', default='default', help='Theme (default, dark, light)')
  @click.option('--code', is_flag=True, help='Include code example')
  @click.option('--table', is_flag=True, help='Include table example')
  @click.option('--image', is_flag=True, help='Include image example')
  def generate(type, output, add, html, theme, code, table, image):
      """Generate mindmap from template"""
      try:
          generator = MarkmapGenerator(type)
          
          # Add custom sections
          for section in add:
              if ':' in section:
                  title, items = section.split(':', 1)
                  items_list = [item.strip() for item in items.split(',')]
                  generator.add_section(title, items_list)
          
          # Add examples
          if code:
              generator.add_code_example()
          if table:
              generator.add_table_example()
          if image:
              generator.add_image_example()
          
          # Generate markdown
          markdown_content = generator.generate()
          
          # Determine output filename
          if not output:
              output = f"markmap-{type}.md"
          
          # Save markdown
          with open(output, 'w', encoding='utf-8') as f:
              f.write(markdown_content)
          
          click.echo(f"✅ Generated: {output}")
          
          # Export HTML if requested
          if html:
              exporter = HTMLExporter()
              html_output = output.replace('.md', '.html')
              exporter.export(markdown_content, html_output, theme)
              click.echo(f"✅ Exported: {html_output}")
      
      except Exception as e:
          click.echo(f"❌ Error: {str(e)}", err=True)
          sys.exit(1)

  @cli.command()
  def interactive():
      """Interactive mode - step by step generation"""
      mode = InteractiveMode()
      mode.run()

  def main():
      """Main entry point"""
      if len(sys.argv) == 1:
          cli(['--help'])
      else:
          cli()

  if __name__ == '__main__':
      main()
````

---

## 3️⃣ mmg/generator.py
````artifact
id: mmg_generator
name: mmg/generator.py
type: code.python
content: |-
  import yaml
  import os
  from pathlib import Path

  class MarkmapGenerator:
      def __init__(self, template_type='novel'):
          self.template_type = template_type
          self.custom_sections = []
          self.examples = {
              'code': False,
              'table': False,
              'image': False
          }
          self.template_data = self._load_template()
      
      @staticmethod
      def get_available_templates():
          """Get list of available templates"""
          template_dir = Path(__file__).parent / 'templates'
          templates = []
          if template_dir.exists():
              templates = [f.stem for f in template_dir.glob('*.yaml')]
          return sorted(templates)
      
      def _load_template(self):
          """Load template from YAML file"""
          template_path = Path(__file__).parent / 'templates' / f'{self.template_type}.yaml'
          
          if not template_path.exists():
              raise ValueError(f"Template '{self.template_type}' not found")
          
          with open(template_path, 'r', encoding='utf-8') as f:
              return yaml.safe_load(f)
      
      def add_section(self, title, items):
          """Add custom section"""
          self.custom_sections.append({
              'title': title,
              'items': items
          })
      
      def add_code_example(self):
          """Add code example"""
          self.examples['code'] = True
      
      def add_table_example(self):
          """Add table example"""
          self.examples['table'] = True
      
      def add_image_example(self):
          """Add image example"""
          self.examples['image'] = True
      
      def generate(self):
          """Generate markdown content"""
          lines = []
          
          # Header
          title = self.template_data.get('title', 'Mindmap')
          lines.append(f"# {title}\n")
          
          # Main sections
          sections = self.template_data.get('sections', [])
          for section in sections:
              lines.append(f"## {section['title']}\n")
              for item in section.get('items', []):
                  lines.append(f"- {item}")
              lines.append("")
          
          # Custom sections
          if self.custom_sections:
              lines.append("## Custom Sections\n")
              for custom in self.custom_sections:
                  lines.append(f"### {custom['title']}\n")
                  for item in custom['items']:
                      lines.append(f"- {item}")
                  lines.append("")
          
          # Code example
          if self.examples['code']:
              lines.append("## Code Example\n")
              lines.append("```python")
              lines.append("def hello_world():")
              lines.append('    print("Hello, Markmap!")')
              lines.append("```\n")
          
          # Table example
          if self.examples['table']:
              lines.append("## Table Example\n")
              lines.append("| Column 1 | Column 2 | Column 3 |")
              lines.append("|----------|----------|----------|")
              lines.append("| Data 1   | Data 2   | Data 3   |")
              lines.append("| Data 4   | Data 5   | Data 6   |\n")
          
          # Image example
          if self.examples['image']:
              lines.append("## Image Example\n")
              lines.append("![Example Image](https://via.placeholder.com/400x300)\n")
          
          return '\n'.join(lines)
````

---

## 4️⃣ mmg/html_export.py
````artifact
id: mmg_html_export
name: mmg/html_export.py
type: code.python
content: |-
  import re

  class HTMLExporter:
      MARKMAP_CDN = "https://cdn.jsdelivr.net/npm/markmap-lib@0.14.3/dist/browser/index.min.js"
      
      THEMES = {
          'default': {
              'bg': '#ffffff',
              'text': '#333333',
              'accent': '#4a90e2'
          },
          'dark': {
              'bg': '#1e1e1e',
              'text': '#e0e0e0',
              'accent': '#64b5f6'
          },
          'light': {
              'bg': '#f5f5f5',
              'text': '#222222',
              'accent': '#2196f3'
          }
      }
      
      def export(self, markdown_content, output_path, theme='default'):
          """Export markdown to HTML with embedded markmap"""
          theme_config = self.THEMES.get(theme, self.THEMES['default'])
          
          html_content = f"""<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Markmap Mindmap</title>
      <script src="{self.MARKMAP_CDN}"></script>
      <style>
          * {{
              margin: 0;
              padding: 0;
              box-sizing: border-box;
          }}
          
          body {{
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
              background-color: {theme_config['bg']};
              color: {theme_config['text']};
              padding: 20px;
          }}
          
          .container {{
              max-width: 1400px;
              margin: 0 auto;
              display: grid;
              grid-template-columns: 1fr 2fr;
              gap: 20px;
          }}
          
          .sidebar {{
              background: rgba(0, 0, 0, 0.05);
              padding: 20px;
              border-radius: 8px;
              overflow-y: auto;
              max-height: 90vh;
          }}
          
          .sidebar h2 {{
              color: {theme_config['accent']};
              margin-bottom: 15px;
              font-size: 18px;
          }}
          
          .sidebar ul {{
              list-style: none;
          }}
          
          .sidebar li {{
              padding: 8px 0;
              padding-left: 16px;
              border-left: 2px solid transparent;
              transition: all 0.3s ease;
          }}
          
          .sidebar li:hover {{
              border-left-color: {theme_config['accent']};
              padding-left: 20px;
          }}
          
          .mindmap-container {{
              background: {theme_config['bg']};
              border-radius: 8px;
              overflow: hidden;
              box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
          }}
          
          svg {{
              width: 100%;
              height: 100%;
              min-height: 600px;
          }}
          
          .markmap-node {{
              font-size: 14px;
          }}
          
          @media (max-width: 768px) {{
              .container {{
                  grid-template-columns: 1fr;
              }}
              
              .sidebar {{
                  max-height: 300px;
              }}
          }}
      </style>
  </head>
  <body>
      <div class="container">
          <div class="sidebar">
              <h2>📋 Content</h2>
              <div id="toc"></div>
          </div>
          <div class="mindmap-container">
              <svg id="markmap"></svg>
          </div>
      </div>
      
      <script>
          const markdown = `{self._escape_markdown(markdown_content)}`;
          
          // Initialize markmap
          const {{Markmap, loadCSS}} = window;
          
          loadCSS().then(() => {{
              const svg = document.getElementById('markmap');
              const markmap = new Markmap(svg, null, markdown);
              markmap.fit();
          }});
          
          // Generate table of contents
          const headings = markdown.match(/^#+\\s+.+$/gm) || [];
          const toc = document.getElementById('toc');
          headings.forEach(heading => {{
              const level = heading.match(/^#+/)[0].length;
              const text = heading.replace(/^#+\\s+/, '');
              const li = document.createElement('li');
              li.textContent = text;
              li.style.paddingLeft = (level - 1) * 16 + 'px';
              li.style.fontSize = (16 - level) + 'px';
              toc.appendChild(li);
          }});
      </script>
  </body>
  </html>
  """
          
          with open(output_path, 'w', encoding='utf-8') as f:
              f.write(html_content)
      
      @staticmethod
      def _escape_markdown(content):
          """Escape markdown for JavaScript"""
          return content.replace('\\', '\\\\').replace('`', '\\`').replace('\n', '\\n')
````

---

## 5️⃣ mmg/interactive.py
````artifact
id: mmg_interactive
name: mmg/interactive.py
type: code.python
content: |-
  import click
  from .generator import MarkmapGenerator
  from .html_export import HTMLExporter

  class InteractiveMode:
      def __init__(self):
          self.generator = None
          self.template_type = None
          self.custom_sections = []
          self.examples = {}
          self.output_file = None
      
      def run(self):
          """Run interactive mode"""
          click.clear()
          click.echo("=" * 50)
          click.echo("🎯 MMG - Interactive Mindmap Generator")
          click.echo("=" * 50 + "\n")
          
          # Step 1: Select template
          self._select_template()
          
          # Step 2: Add custom sections
          self._add_custom_sections()
          
          # Step 3: Add examples
          self._add_examples()
          
          # Step 4: Set output
          self._set_output()
          
          # Step 5: Generate
          self._generate()
      
      def _select_template(self):
          """Select template"""
          templates = MarkmapGenerator.get_available_templates()
          
          click.echo("📚 Available Templates:\n")
          for i, template in enumerate(templates, 1):
              click.echo(f"  {i}. {template}")
          
          choice = click.prompt("\n👉 Select template (number or name)", type=str)
          
          try:
              if choice.isdigit():
                  self.template_type = templates[int(choice) - 1]
              else:
                  self.template_type = choice
              
              self.generator = MarkmapGenerator(self.template_type)
              click.echo(f"\n✅ Selected: {self.template_type}\n")
          
          except (IndexError, ValueError):
              click.echo("❌ Invalid selection")
              self._select_template()
      
      def _add_custom_sections(self):
          """Add custom sections"""
          click.echo("📝 Add Custom Sections\n")
          click.echo("(Press Enter to skip)\n")
          
          while True:
              section_title = click.prompt("Section title", default="", show_default=False)
              
              if not section_title:
                  break
              
              items_input = click.prompt("Items (comma-separated)", default="", show_default=False)
              
              if items_input:
                  items = [item.strip() for item in items_input.split(',')]
                  self.generator.add_section(section_title, items)
                  click.echo(f"✅ Added: {section_title}\n")
              
              if not click.confirm("Add another section?", default=False):
                  break
          
          click.echo()
      
      def _add_examples(self):
          """Add examples"""
          click.echo("📌 Add Examples\n")
          
          if click.confirm("Include code example?", default=False):
              self.generator.add_code_example()
              click.echo("✅ Code example added\n")
          
          if click.confirm("Include table example?", default=False):
              self.generator.add_table_example()
              click.echo("✅ Table example added\n")
          
          if click.confirm("Include image example?", default=False):
              self.generator.add_image_example()
              click.echo("✅ Image example added\n")
      
      def _set_output(self):
          """Set output filename"""
          default_output = f"markmap-{self.template_type}.md"
          self.output_file = click.prompt("Output filename", default=default_output)
      
      def _generate(self):
          """Generate and export"""
          click.echo("\n⏳ Generating...\n")
          
          try:
              markdown_content = self.generator.generate()
              
              # Save markdown
              with open(self.output_file, 'w', encoding='utf-8') as f:
                  f.write(markdown_content)
              
              click.echo(f"✅ Markdown saved: {self.output_file}")
              
              # Export HTML
              if click.confirm("Export as HTML?", default=True):
                  theme = click.prompt("Select theme", type=click.Choice(['default', 'dark', 'light']), default='default')
                  
                  exporter = HTMLExporter()
                  html_file = self.output_file.replace('.md', '.html')
                  exporter.export(markdown_content, html_file, theme)
                  
                  click.echo(f"✅ HTML exported: {html_file}")
              
              click.echo("\n🎉 Done! Your mindmap is ready.\n")
          
          except Exception as e:
              click.echo(f"❌ Error: {str(e)}")
````

---

## 6️⃣ mmg/__init__.py
````artifact
id: mmg_init
name: mmg/__init__.py
type: code.python
content: |-
  """MMG - Markmap Mindmap Generator"""

  __version__ = "1.0.0"
  __author__ = "MMG Team"
  __license__ = "MIT"

  from .generator import MarkmapGenerator
  from .html_export import HTMLExporter
  from .interactive import InteractiveMode
  from .cli import cli

  __all__ = [
      'MarkmapGenerator',
      'HTMLExporter',
      'InteractiveMode',
      'cli'
  ]
````

---

## 7️⃣ YAML Templates (ทั้ง 7 ตัว)
````artifact
id: mmg_templates
name: mmg/templates/*.yaml
type: code.yaml
content: |-
  # ===== novel.yaml =====
  title: Novel Story Structure
  sections:
    - title: Act I - Setup
      items:
        - Introduce protagonist
        - Establish setting
        - Present inciting incident
    - title: Act II - Confrontation
      items:
        - Rising action
        - Complications
        - Midpoint revelation
    - title: Act III - Resolution
      items:
        - Climax
        - Falling action
        - Resolution

  ---
  # ===== system_arch.yaml =====
  title: System Architecture
  sections:
    - title: Frontend
      items:
        - UI Components
        - State Management
        - API Integration
    - title: Backend
      items:
        - REST API
        - Database
        - Authentication
    - title: Infrastructure
      items:
        - Deployment
        - Monitoring
        - Scaling

  ---
  # ===== exec_report.yaml =====
  title: Executive Report
  sections:
    - title: Executive Summary
      items:
        - Key findings
        - Recommendations
        - Impact
    - title: Business Overview
      items:
        - Market analysis
        - Competitors
        - Opportunities
    - title: Financial Summary
      items:
        - Revenue
        - Expenses
        - Profit margin

  ---
  # ===== tech_report.yaml =====
  title: Technical Report
  sections:
    - title: Introduction
      items:
        - Problem statement
        - Objectives
        - Scope
    - title: Methodology
      items:
        - Research approach
        - Tools used
        - Data collection
    - title: Results & Analysis
      items:
        - Findings
        - Performance metrics
        - Comparisons

  ---
  # ===== ai_skill.yaml =====
  title: AI Skills Map
  sections:
    - title: Machine Learning
      items:
        - Supervised Learning
        - Unsupervised Learning
        - Reinforcement Learning
    - title: Deep Learning
      items:
        - Neural Networks
        - CNNs
        - RNNs & Transformers
    - title: NLP
      items:
        - Text Processing
        - Language Models
        - Sentiment Analysis

  ---
  # ===== planning.yaml =====
  title: Project Planning
  sections:
    - title: Scope
      items:
        - Objectives
        - Deliverables
        - Constraints
    - title: Timeline
      items:
        - Phase 1
        - Phase 2
        - Phase 3
    - title: Resources
      items:
        - Team
        - Budget
        - Tools

  ---
  # ===== strategy.yaml =====
  title: Business Strategy
  sections:
    - title: Vision & Mission
      items:
        - Long-term vision
        - Mission statement
        - Core values
    - title: Strategic Goals
      items:
        - Growth targets
        - Market expansion
        - Innovation
    - title: Action Plan
      items:
        - Initiatives
        - Milestones
        - KPIs
````

---

## 8️⃣ README.md
````artifact
id: mmg_readme
name: README.md
type: markdown
content: |-
  # 🗺️ MMG - Markmap Mindmap Generator

  [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

  สร้างแผนที่ความคิด (Mindmap) ที่สวยงามจากเทมเพลตที่เตรียมไว้ด้วย Markmap

  ## ✨ Features

  - 📚 **7 Built-in Templates**: Novel, System Architecture, Executive Report, Technical Report, AI Skills, Planning, Strategy
  - 🎨 **Multiple Themes**: Default, Dark, Light
  - 📝 **Custom Sections**: เพิ่ม section ของคุณเองได้
  - 🔧 **Interactive Mode**: ตอบคำถามทีละขั้นเพื่อสร้าง mindmap
  - 📊 **Export Options**: Markdown + HTML (single file)
  - 💻 **CLI & Python API**: ใช้งานผ่าน command line หรือ Python code

  ## 📦 Installation

  ### ด้วย Auto Setup Script (แนะนำ)

  ```bash
  bash setup.sh
  ```

  ### Manual Installation

  ```bash
  # Clone repository
  git clone https://github.com/yourusername/mmg.git
  cd mmg

  # Install
  pip install .

  # Verify
  mmg --list
  ```

  ## 🚀 Quick Start

  ### 1. List Templates
  ```bash
  mmg --list
  ```

  ### 2. Generate from Template
  ```bash
  mmg --type novel
  mmg --type system_arch
  mmg --type planning
  ```

  ### 3. Add Custom Sections
  ```bash
  mmg --type system_arch --add "API:Login,Register,Logout"
  ```

  ### 4. Export as HTML
  ```bash
  mmg --type planning --html --theme dark
  ```

  ### 5. Interactive Mode
  ```bash
  mmg --interactive
  ```

  ## 📖 Usage Examples

  ### Generate Novel Template
  ```bash
  mmg --type novel --output my-story.md
  ```

  ### Generate with Examples
  ```bash
  mmg --type tech_report --code --table --image --html
  ```

  ### Multiple Custom Sections
  ```bash
  mmg --type system_arch \
    --add "Frontend:React,Vue,Angular" \
    --add "Backend:Node.js,Python,Go" \
    --html --theme dark
  ```

  ### Interactive Mode
  ```bash
  mmg --interactive
  # ตอบคำถามทีละข้อ
  # เลือก template → เพิ่ม custom sections → เลือก examples → ตั้งชื่อไฟล์
  ```

  ## 🎯 Available Templates

  | Template | Use Case |
  |----------|----------|
  | `novel` | Story structure, narrative planning |
  | `system_arch` | Software architecture, system design |
  | `exec_report` | Executive summary, business reports |
  | `tech_report` | Technical documentation, research |
  | `ai_skill` | AI/ML skills mapping, learning path |
  | `planning` | Project planning, timeline |
  | `strategy` | Business strategy, strategic planning |

  ## 🎨 Themes

  - **default**: Light theme with blue accent
  - **dark**: Dark theme with light blue accent
  - **light**: Light theme with standard blue accent

  ```bash
  mmg --type planning --html --theme dark
  ```

  ## 🛠️ CLI Options

  ```
  Usage: mmg [OPTIONS] COMMAND [ARGS]...

  Commands:
    generate      Generate mindmap from template
    list          List all available templates
    interactive   Interactive mode

  Options for generate:
    -t, --type TEXT           Template type (default: novel)
    -o, --output TEXT         Output filename
    -a, --add TEXT            Add custom section
    --html                    Export as HTML
    --theme TEXT              Theme (default/dark/light)
    --code                    Include code example
    --table                   Include table example
    --image                   Include image example
  ```

  ## 📚 Python API

  ```python
  from mmg import MarkmapGenerator, HTMLExporter

  # Create generator
  gen = MarkmapGenerator('system_arch')

  # Add custom sections
  gen.add_section('API Endpoints', ['GET /users', 'POST /users', 'DELETE /users/{id}'])

  # Add examples
  gen.add_code_example()
  gen.add_table_example()

  # Generate markdown
  markdown = gen.generate()

  # Export HTML
  exporter = HTMLExporter()
  exporter.export(markdown, 'output.html', theme='dark')
  ```

  ## 📁 Project Structure

  ```
  mmg/
  ├── pyproject.toml
  ├── README.md
  ├── setup.sh
  ├── mmg/
  │   ├── __init__.py
  │   ├── cli.py
  │   ├── generator.py
  │   ├── html_export.py
  │   ├── interactive.py
  │   ├── templates/
  │   │   ├── novel.yaml
  │   │   ├── system_arch.yaml
  │   │   ├── exec_report.yaml
  │   │   ├── tech_report.yaml
  │   │   ├── ai_skill.yaml
  │   │   ├── planning.yaml
  │   │   └── strategy.yaml
  │   └── assets/
  │       └── markmap.min.js
  └── tests/
      └── test_generator.py
  ```

  ## 🧪 Testing

  ```bash
  # Install dev dependencies
  pip install -e ".[dev]"

  # Run tests
  pytest

  # Run with coverage
  pytest --cov=mmg
  ```

  ## 🤝 Contributing

  Contributions are welcome! Please feel free to submit a Pull Request.

  1. Fork the repository
  2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
  3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
  4. Push to the branch (`git push origin feature/AmazingFeature`)
  5. Open a Pull Request

  ## 📝 License

  This project is licensed under the MIT License - see the LICENSE file for details.

  ## 🙏 Acknowledgments

  - [Markmap](https://markmap.js.org/) - Awesome mindmap library
  - [Click](https://click.palletsprojects.com/) - Python CLI framework
  - [PyYAML](https://pyyaml.org/) - YAML parser

  ## 📞 Support

  - 📧 Email: info@mmg.dev
  - 🐛 Issues: [GitHub Issues](https://github.com/yourusername/mmg/issues)
  - 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/mmg/discussions)

  ---

  **Made with ❤️ by MMG Team**
````

---

## 9️⃣ setup.sh (Auto Setup Script)
````artifact
id: mmg_setup_script
name: setup.sh
type: code.bash
content: |-
  #!/bin/bash

  # Colors for output
  RED='\033[0;31m'
  GREEN='\033[0;32m'
  YELLOW='\033[1;33m'
  BLUE='\033[0;34m'
  NC='\033[0m' # No Color

  # Banner
  echo -e "${BLUE}"
  echo "╔════════════════════════════════════════╗"
  echo "║  🗺️  MMG - Markmap Generator Setup    ║"
  echo "║  Auto Installation Script              ║"
  echo "╚════════════════════════════════════════╝"
  echo -e "${NC}\n"

  # Check Python version
  echo -e "${YELLOW}[1/6] Checking Python version...${NC}"
  if ! command -v python3 &> /dev/null; then
      echo -e "${RED}❌ Python 3 is not installed${NC}"
      echo "Please install Python 3.8 or higher from https://www.python.org/"
      exit 1
  fi

  PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
  echo -e "${GREEN}✅ Python ${PYTHON_VERSION} found${NC}\n"

  # Check pip
  echo -e "${YELLOW}[2/6] Checking pip...${NC}"
  if ! command -v pip3 &> /dev/null; then
      echo -e "${RED}❌ pip3 is not installed${NC}"
      echo "Installing pip..."
      python3 -m ensurepip --upgrade
  fi
  echo -e "${GREEN}✅ pip is ready${NC}\n"

  # Create virtual environment (optional)
  echo -e "${YELLOW}[3/6] Setting up environment...${NC}"
  if [ ! -d "venv" ]; then
      echo "Creating virtual environment..."
      python3 -m venv venv
      echo -e "${GREEN}✅ Virtual environment created${NC}"
  else
      echo -e "${GREEN}✅ Virtual environment already exists${NC}"
  fi

  # Activate virtual environment
  if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
      source venv/Scripts/activate
  else
      source venv/bin/activate
  fi
  echo -e "${GREEN}✅ Virtual environment activated${NC}\n"

  # Upgrade pip, setuptools, wheel
  echo -e "${YELLOW}[4/6] Upgrading pip and setuptools...${NC}"
  pip3 install --upgrade pip setuptools wheel
  echo -e "${GREEN}✅ Dependencies upgraded${NC}\n"

  # Install MMG
  echo -e "${YELLOW}[5/6] Installing MMG...${NC}"
  if [ -f "pyproject.toml" ]; then
      pip3 install -e .
      echo -e "${GREEN}✅ MMG installed successfully${NC}\n"
  else
      echo -e "${RED}❌ pyproject.toml not found${NC}"
      exit 1
  fi

  # Verify installation
  echo -e "${YELLOW}[6/6] Verifying installation...${NC}"
  if command -v mmg &> /dev/null; then
      echo -e "${GREEN}✅ MMG command is available${NC}\n"
      
      # Show available templates
      echo -e "${BLUE}Available templates:${NC}"
      mmg --list
      
      echo -e "\n${GREEN}═══════════════════════════════════════${NC}"
      echo -e "${GREEN}🎉 Installation completed successfully!${NC}"
      echo -e "${GREEN}═══════════════════════════════════════${NC}\n"
      
      echo -e "${BLUE}Quick start commands:${NC}"
      echo -e "  ${YELLOW}mmg --list${NC}                    # List all templates"
      echo -e "  ${YELLOW}mmg --type novel${NC}             # Generate from template"
      echo -e "  ${YELLOW}mmg --interactive${NC}            # Interactive mode"
      echo -e "  ${YELLOW}mmg --type planning --html${NC}   # Export as HTML"
      echo ""
      
      echo -e "${BLUE}Next steps:${NC}"
      echo -e "  1. Run: ${YELLOW}mmg --interactive${NC}"
      echo -e "  2. Or: ${YELLOW}mmg --type novel --html${NC}"
      echo -e "  3. Check: ${YELLOW}README.md${NC} for more examples"
      echo ""
      
  else
      echo -e "${RED}❌ Installation verification failed${NC}"
      exit 1
  fi

  # Optional: Install dev dependencies
  echo -e "${BLUE}Would you like to install development dependencies?${NC}"
  read -p "Install pytest, black, flake8? (y/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
      echo -e "${YELLOW}Installing dev dependencies...${NC}"
      pip3 install -e ".[dev]"
      echo -e "${GREEN}✅ Dev dependencies installed${NC}\n"
  fi

  echo -e "${GREEN}Setup complete! Happy mindmapping! 🗺️${NC}\n"
````

---

## 🔟 test_generator.py
````artifact
id: mmg_tests
name: tests/test_generator.py
type: code.python
content: |-
  import pytest
  from mmg.generator import MarkmapGenerator
  from mmg.html_export import HTMLExporter

  class TestMarkmapGenerator:
      
      def test_get_available_templates(self):
          """Test getting available templates"""
          templates = MarkmapGenerator.get_available_templates()
          assert isinstance(templates, list)
          assert len(templates) > 0
      
      def test_load_valid_template(self):
          """Test loading a valid template"""
          gen = MarkmapGenerator('novel')
          assert gen.template_type == 'novel'
          assert gen.template_data is not None
      
      def test_load_invalid_template(self):
          """Test loading an invalid template"""
          with pytest.raises(ValueError):
              MarkmapGenerator('nonexistent')
      
      def test_add_section(self):
          """Test adding custom section"""
          gen = MarkmapGenerator('novel')
          gen.add_section('Custom', ['Item 1', 'Item 2'])
          assert len(gen.custom_sections) == 1
          assert gen.custom_sections[0]['title'] == 'Custom'
      
      def test_add_examples(self):
          """Test adding examples"""
          gen = MarkmapGenerator('novel')
          gen.add_code_example()
          gen.add_table_example()
          gen.add_image_example()
          
          assert gen.examples['code'] == True
          assert gen.examples['table'] == True
          assert gen.examples['image'] == True
      
      def test_generate_markdown(self):
          """Test markdown generation"""
          gen = MarkmapGenerator('novel')
          gen.add_section('Test', ['Item 1'])
          markdown = gen.generate()
          
          assert isinstance(markdown, str)
          assert '# ' in markdown
          assert 'Test' in markdown
          assert 'Item 1' in markdown
      
      def test_generate_with_all_examples(self):
          """Test generation with all examples"""
          gen = MarkmapGenerator('system_arch')
          gen.add_code_example()
          gen.add_table_example()
          gen.add_image_example()
          
          markdown = gen.generate()
          assert '```python' in markdown
          assert '| Column 1 |' in markdown
          assert '![Example Image]' in markdown

  class TestHTMLExporter:
      
      def test_export_html(self, tmp_path):
          """Test HTML export"""
          exporter = HTMLExporter()
          markdown = "# Test\n## Section\n- Item"
          output_file = tmp_path / "test.html"
          
          exporter.export(str(markdown), str(output_file))
          assert output_file.exists()
      
      def test_export_with_different_themes(self, tmp_path):
          """Test export with different themes"""
          exporter = HTMLExporter()
          markdown = "# Test\n## Section\n- Item"
          
          for theme in ['default', 'dark', 'light']:
              output_file = tmp_path / f"test_{theme}.html"
              exporter.export(str(markdown), str(output_file), theme)
              assert output_file.exists()
      
      def test_escape_markdown(self):
          """Test markdown escaping"""
          content = 'Test\nwith\n`backticks`'
          escaped = HTMLExporter._escape_markdown(content)
          assert '\\n' in escaped
          assert '\\`' in escaped

  if __name__ == '__main__':
      pytest.main([__file__, '-v'])
````

---

## 📋 Summary

ผมสร้าง **10 Artifacts** ทั้งหมด:

| # | ไฟล์ | คำอธิบาย |
|---|------|---------|
| 1️⃣ | `pyproject.toml` | Package configuration |
| 2️⃣ | `mmg/cli.py` | Command-line interface |
| 3️⃣ | `mmg/generator.py` | Core generator engine |
| 4️⃣ | `mmg/html_export.py` | HTML exporter |
| 5️⃣ | `mmg/interactive.py` | Interactive mode |
| 6️⃣ | `mmg/__init__.py` | Package init |
| 7️⃣ | `mmg/templates/*.yaml` | 7 YAML templates |
| 8️⃣ | `README.md` | Documentation |
| 9️⃣ | `setup.sh` | Auto setup script ⭐ |
| 🔟 | `tests/test_generator.py` | Unit tests |

---

## 🚀 วิธีใช้งาน

### ขั้นที่ 1: Copy ไฟล์ทั้งหมด
```bash
mkdir mmg
cd mmg
# Copy ไฟล์ทั้ง 10 ตัว
```

### ขั้นที่ 2: รัน Auto Setup
```bash
bash setup.sh
```

### ขั้นที่ 3: ใช้งาน
```bash
mmg --list
mmg --type novel
mmg --interactive
```

---

**✅ Ready to use! ทั้งหมดพร้อมใช้งานแล้ว 🎉**
