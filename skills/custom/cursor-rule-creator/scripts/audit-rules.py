#!/usr/bin/env python3
import os
import yaml
import glob
from pathlib import Path
import re

def audit_rules(rules_dir=".cursor/rules"):
    metrics = {
        'total_files': 0, 'valid_yaml': 0, 'avg_length': 0,
        'specific_globs': 0, 'has_tags': 0, 'quality_score': 0
    }
    
    mdc_files = glob.glob(f"{rules_dir}/**/*.mdc", recursive=True)
    metrics['total_files'] = len(mdc_files)
    
    lengths = []
    for file_path in mdc_files:
        metrics['total_files'] += 1
        content = Path(file_path).read_text()
        length = len(content.splitlines())
        lengths.append(length)
        
        # Check YAML frontmatter
        if content.startswith('---') and '---' in content[3:]:
            try:
                yaml_part = content[3:content.find('---', 3)].strip()
                data = yaml.safe_load(yaml_part)
                metrics['valid_yaml'] += 1
                
                # Glob specificity check
                if data.get('globs') and not any(g == '**/*' for g in data['globs']):
                    metrics['specific_globs'] += 1
                
                # Tags check
                if data.get('tags'):
                    metrics['has_tags'] += 1
                    
            except yaml.YAMLError:
                pass
    
    metrics['avg_length'] = sum(lengths) / len(lengths) if lengths else 0
    metrics['quality_score'] = (
        (metrics['valid_yaml']/metrics['total_files'])*30 +
        (metrics['specific_globs']/metrics['total_files'])*30 +
        (1 if metrics['avg_length'] < 300 else 0)*20 +
        (metrics['has_tags']/metrics['total_files'])*20
    )
    
    print(f"📊 Quality Report for {rules_dir}")
    print(f"Total .mdc files: {metrics['total_files']}")
    print(f"Valid YAML: {metrics['valid_yaml']} ({metrics['valid_yaml']/metrics['total_files']*100:.1f}%)")
    print(f"Avg length: {metrics['avg_length']:.1f} lines")
    print(f"Quality Score: {metrics['quality_score']:.1f}/100")
    return metrics

if __name__ == "__main__":
    audit_rules()