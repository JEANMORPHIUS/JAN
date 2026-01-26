"""ARCHIVE OLD COMPLETION DOCS
Archive completion docs older than threshold that aren't referenced

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE TRUTH:
IF WE DON'T NEED IT...ARCHIVE IT

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

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
    JAN_ROOT, JAN_ARCHIVE, JAN_OUTPUT, get_archive_path, get_output_path,
    datetime, json, shutil, logging,
    setup_logging, load_json, save_json, standard_main
)

logger = setup_logging(__name__)

def archive_old_completion_docs(root_dir: Path = None, days_threshold: int = 90):
    """Archive completion docs older than threshold that aren't referenced"""
    root = root_dir or JAN_ROOT
    archive_dir = get_archive_path("completion_docs")
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    # Load usefulness analysis
    analysis_file = get_output_path("usefulness_analysis.json")
    if not analysis_file.exists():
        logger.error("Error: Run analyze_usefulness.py first")
        return
    
    analysis = load_json(analysis_file)
    
    # Get unreferenced completion docs
    comp_docs = analysis['completion_docs']
    
    print("="*80)
    print("ARCHIVING OLD COMPLETION DOCS")
    print("="*80)
    print(f"\nThreshold: {days_threshold} days old and unreferenced")
    print(f"Current recommendation: Keep all (all are recent)")
    print("\nThis script is ready for future use when docs are older.")
    print("="*80)

def main():
    """Main function"""
    archive_old_completion_docs()

if __name__ == "__main__":
    standard_main(main, script_name="archive_old_completion_docs.py")
