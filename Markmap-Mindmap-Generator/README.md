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
