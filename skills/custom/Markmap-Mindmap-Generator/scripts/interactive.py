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