"""
CONSOLIDATE COMPLETION DOCS
Review and consolidate completion documentation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE TRUTH:
CONSOLIDATE REDUNDANT COMPLETION DOCS
KEEP ESSENTIAL INFORMATION
ARCHIVE THE REST
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    JAN_ROOT, JAN_OUTPUT, get_output_path,
    datetime, json, logging, List, Dict,
    setup_logging, save_json, standard_main
)

logger = setup_logging(__name__)

def consolidate_completion_docs(root_dir: Path = None):
    """Analyze completion docs and suggest consolidation"""
    root = root_dir or JAN_ROOT
    completion_docs = list(root.glob("*_COMPLETE.md"))
    
    # Group by category
    categories: Dict[str, List[Path]] = {}
    
    for doc in completion_docs:
        name = doc.stem.replace("_COMPLETE", "").lower()
        
        # Categorize
        category = "other"
        if "integration" in name:
            category = "integration"
        elif "system" in name or "protocol" in name:
            category = "system"
        elif "deployment" in name or "strategy" in name:
            category = "deployment"
        elif "audit" in name or "review" in name:
            category = "audit"
        elif "complete" in name or "final" in name:
            category = "final"
        
        if category not in categories:
            categories[category] = []
        categories[category].append(doc)
    
    # Generate report
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_docs': len(completion_docs),
        'categories': {}
    }
    
    for category, docs in categories.items():
        report['categories'][category] = {
            'count': len(docs),
            'files': [str(d) for d in sorted(docs, key=lambda p: p.stat().st_mtime, reverse=True)]
        }
    
    # Save report
    report_file = get_output_path("completion_docs_analysis.json")
    save_json(report, report_file)
    
    # Print summary
    print("="*80)
    print("COMPLETION DOCS CONSOLIDATION ANALYSIS")
    print("="*80)
    print(f"\nTotal Completion Docs: {len(completion_docs)}")
    print(f"\nBy Category:")
    for category, data in report['categories'].items():
        print(f"  {category}: {data['count']} docs")
        if data['count'] > 5:
            print(f"    -> Consider consolidating")
    
    print(f"\nReport saved to: {report_file}")
    print("="*80)

def main():
    """Main function"""
    consolidate_completion_docs()

if __name__ == "__main__":
    standard_main(main, script_name="consolidate_completion_docs.py")
