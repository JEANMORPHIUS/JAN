"""OPTIMIZE WORKSPACE SCRIPTS
Review and optimize scripts in S:\\JAN\\scripts for performance and maintainability

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
- Review all scripts for optimization opportunities
- Remove duplicate functionality
- Consolidate similar scripts
- Improve performance and readability
- Build on what works

PEACE, LOVE, UNITY

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import os
import ast
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Any
from collections import defaultdict
import re

class ScriptOptimizer:
    """Optimize workspace scripts"""
    
    def __init__(self, scripts_dir: str = "S:\\JAN\\scripts"):
        self.scripts_dir = Path(scripts_dir)
        self.scripts: List[Dict] = []
        self.duplicates: List[Dict] = []
        self.optimizations: List[Dict] = []
        self.recommendations: List[Dict] = []
        
    def scan_scripts(self) -> List[Dict]:
        """Scan all scripts in the directory"""
        print("Scanning scripts...")
        
        script_files = []
        for ext in ['*.py', '*.ps1', '*.bat', '*.sh']:
            script_files.extend(self.scripts_dir.glob(ext))
        
        for script_file in script_files:
            try:
                stat = script_file.stat()
                script_info = {
                    'path': str(script_file),
                    'name': script_file.name,
                    'size': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'extension': script_file.suffix,
                    'content': None,
                    'imports': [],
                    'functions': [],
                    'classes': []
                }
                
                # Read content for Python files
                if script_file.suffix == '.py':
                    try:
                        with open(script_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            script_info['content'] = content
                            
                            # Parse AST for Python files
                            try:
                                tree = ast.parse(content)
                                script_info['imports'] = self._extract_imports(tree)
                                script_info['functions'] = self._extract_functions(tree)
                                script_info['classes'] = self._extract_classes(tree)
                            except SyntaxError:
                                script_info['parse_error'] = True
                    except Exception as e:
                        script_info['read_error'] = str(e)
                
                self.scripts.append(script_info)
                
            except Exception as e:
                print(f"  [!] Error scanning {script_file}: {e}")
        
        print(f"  Found {len(self.scripts)} scripts")
        return self.scripts
    
    def _extract_imports(self, tree: ast.AST) -> List[str]:
        """Extract import statements"""
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")
        return imports
    
    def _extract_functions(self, tree: ast.AST) -> List[str]:
        """Extract function names"""
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
        return functions
    
    def _extract_classes(self, tree: ast.AST) -> List[str]:
        """Extract class names"""
        classes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                classes.append(node.name)
        return classes
    
    def find_duplicate_imports(self) -> Dict[str, List[str]]:
        """Find scripts with duplicate import patterns"""
        print("\nAnalyzing imports...")
        
        import_patterns = defaultdict(list)
        
        for script in self.scripts:
            if script.get('imports'):
                # Create a signature from sorted imports
                import_sig = tuple(sorted(set(script['imports'])))
                import_patterns[import_sig].append(script['name'])
        
        duplicates = {sig: scripts for sig, scripts in import_patterns.items() if len(scripts) > 1}
        
        if duplicates:
            print(f"  Found {len(duplicates)} duplicate import patterns")
            for sig, scripts in list(duplicates.items())[:5]:
                print(f"    Pattern: {', '.join(sig[:3])}... ({len(scripts)} scripts)")
                self.recommendations.append({
                    'type': 'consolidate_imports',
                    'description': f"Consider creating shared import module for: {', '.join(sig[:5])}",
                    'scripts': scripts
                })
        else:
            print("  No significant duplicate import patterns found")
        
        return duplicates
    
    def find_similar_functions(self) -> Dict[str, List[Dict]]:
        """Find similar function names across scripts"""
        print("\nAnalyzing functions...")
        
        function_map = defaultdict(list)
        
        for script in self.scripts:
            if script.get('functions'):
                for func_name in script['functions']:
                    function_map[func_name.lower()].append({
                        'script': script['name'],
                        'function': func_name
                    })
        
        similar = {name: funcs for name, funcs in function_map.items() if len(funcs) > 1}
        
        if similar:
            print(f"  Found {len(similar)} function names used in multiple scripts")
            for name, funcs in list(similar.items())[:10]:
                print(f"    '{name}': {len(funcs)} occurrences")
                self.recommendations.append({
                    'type': 'consolidate_functions',
                    'description': f"Function '{name}' appears in {len(funcs)} scripts - consider shared utility",
                    'functions': funcs
                })
        else:
            print("  No duplicate function names found")
        
        return similar
    
    def find_unused_scripts(self) -> List[Dict]:
        """Find potentially unused scripts"""
        print("\nIdentifying potentially unused scripts...")
        
        unused = []
        
        # Check for test files that might be outdated
        test_patterns = ['test_', '_test', 'test.']
        for script in self.scripts:
            if any(pattern in script['name'].lower() for pattern in test_patterns):
                # Check modification date (older than 90 days)
                mod_date = datetime.fromisoformat(script['modified'].replace('Z', '+00:00'))
                days_old = (datetime.now() - mod_date.replace(tzinfo=None)).days
                
                if days_old > 90:
                    unused.append({
                        'script': script['name'],
                        'reason': f'Test script, {days_old} days old',
                        'days_old': days_old
                    })
        
        # Check for very small scripts (might be stubs)
        for script in self.scripts:
            if script['size'] < 100:  # Less than 100 bytes
                unused.append({
                    'script': script['name'],
                    'reason': f'Very small script ({script["size"]} bytes) - might be stub',
                    'size': script['size']
                })
        
        if unused:
            print(f"  Found {len(unused)} potentially unused scripts")
            for item in unused[:10]:
                print(f"    - {item['script']}: {item['reason']}")
        else:
            print("  No obviously unused scripts found")
        
        return unused
    
    def find_optimization_opportunities(self) -> List[Dict]:
        """Find code optimization opportunities"""
        print("\nLooking for optimization opportunities...")
        
        optimizations = []
        
        for script in self.scripts:
            if not script.get('content'):
                continue
            
            content = script['content']
            
            # Check for hardcoded paths
            hardcoded_paths = re.findall(r'["\']([A-Z]:\\.*?)["\']', content)
            if hardcoded_paths:
                unique_paths = list(set(hardcoded_paths))
                optimizations.append({
                    'script': script['name'],
                    'type': 'hardcoded_paths',
                    'description': f"Contains {len(unique_paths)} hardcoded paths - consider using Path or environment variables",
                    'paths': unique_paths[:5]
                })
            
            # Check for duplicate code blocks (simple heuristic)
            lines = content.split('\n')
            if len(lines) > 100:
                # Check for repeated long blocks
                block_size = 10
                blocks = [tuple(lines[i:i+block_size]) for i in range(len(lines) - block_size)]
                block_counts = defaultdict(int)
                for block in blocks:
                    block_counts[block] += 1
                
                repeated = {block: count for block, count in block_counts.items() if count > 2}
                if repeated:
                    optimizations.append({
                        'script': script['name'],
                        'type': 'repeated_blocks',
                        'description': f"Contains repeated code blocks - consider extracting to functions",
                        'count': len(repeated)
                    })
        
        if optimizations:
            print(f"  Found {len(optimizations)} optimization opportunities")
            for opt in optimizations[:10]:
                print(f"    - {opt['script']}: {opt['description']}")
        else:
            print("  No obvious optimization opportunities found")
        
        return optimizations
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate optimization report"""
        print("\n" + "="*80)
        print("GENERATING OPTIMIZATION REPORT")
        print("="*80)
        
        self.scan_scripts()
        duplicate_imports = self.find_duplicate_imports()
        similar_functions = self.find_similar_functions()
        unused_scripts = self.find_unused_scripts()
        optimizations = self.find_optimization_opportunities()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_scripts': len(self.scripts),
                'python_scripts': len([s for s in self.scripts if s['extension'] == '.py']),
                'powershell_scripts': len([s for s in self.scripts if s['extension'] == '.ps1']),
                'duplicate_import_patterns': len(duplicate_imports),
                'similar_functions': len(similar_functions),
                'potentially_unused': len(unused_scripts),
                'optimization_opportunities': len(optimizations)
            },
            'recommendations': self.recommendations,
            'unused_scripts': unused_scripts,
            'optimizations': optimizations,
            'scripts_by_type': {
                'python': [s['name'] for s in self.scripts if s['extension'] == '.py'],
                'powershell': [s['name'] for s in self.scripts if s['extension'] == '.ps1'],
                'batch': [s['name'] for s in self.scripts if s['extension'] == '.bat'],
                'shell': [s['name'] for s in self.scripts if s['extension'] == '.sh']
            }
        }
        
        return report
    
    def print_summary(self, report: Dict):
        """Print human-readable summary"""
        print("\n" + "="*80)
        print("OPTIMIZATION SUMMARY")
        print("="*80)
        print(f"\nTotal Scripts: {report['summary']['total_scripts']}")
        print(f"  Python: {report['summary']['python_scripts']}")
        print(f"  PowerShell: {report['summary']['powershell_scripts']}")
        print(f"\nFindings:")
        print(f"  Duplicate Import Patterns: {report['summary']['duplicate_import_patterns']}")
        print(f"  Similar Functions: {report['summary']['similar_functions']}")
        print(f"  Potentially Unused: {report['summary']['potentially_unused']}")
        print(f"  Optimization Opportunities: {report['summary']['optimization_opportunities']}")
        
        if report['recommendations']:
            print(f"\nRecommendations ({len(report['recommendations'])}):")
            for i, rec in enumerate(report['recommendations'][:10], 1):
                print(f"  {i}. {rec['description']}")
        
        if report['unused_scripts']:
            print(f"\nPotentially Unused Scripts ({len(report['unused_scripts'])}):")
            for item in report['unused_scripts'][:10]:
                print(f"  - {item['script']}: {item['reason']}")


def main():
    """Main function"""
    print("="*80)
    print("WORKSPACE SCRIPT OPTIMIZATION")
    print("="*80)
    print()
    
    optimizer = ScriptOptimizer()
    report = optimizer.generate_report()
    optimizer.print_summary(report)
    
    # Save report
    output_dir = Path("S:\\JAN\\output")
    output_dir.mkdir(exist_ok=True)
    
    report_path = output_dir / f"script_optimization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\nFull report saved to: {report_path}")
    print("\n" + "="*80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("="*80)


if __name__ == "__main__":
    main()
