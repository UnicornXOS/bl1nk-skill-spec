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