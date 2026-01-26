"""Fix Instagram account handles in CSV files to use @jeanmorphius

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
    Path, setup_logging, standard_main
)

import csv
from pathlib import Path

OUTPUT_ROOT = Path("S:\\JAN\\output\\2026_social_content")

def fix_instagram_handles():
    """Update Instagram account columns to @jeanmorphius"""
    csv_files = list(OUTPUT_ROOT.glob("*JEAN*.csv"))
    
    for csv_file in csv_files:
        print(f"Fixing Instagram handles in {csv_file.name}...")
        
        rows = []
        with open(csv_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)
            
            # Find Instagram column index
            instagram_col = None
            for i, col in enumerate(header):
                if "instagram" in col.lower() and "account" in col.lower():
                    instagram_col = i
                    break
            
            for row in reader:
                if instagram_col is not None and len(row) > instagram_col:
                    # Update Instagram account to @jeanmorphius
                    if row[instagram_col] == "instagram" or row[instagram_col] == "":
                        row[instagram_col] = "@jeanmorphius"
                rows.append(row)
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        print(f"  [OK] Fixed {csv_file.name}")

def main():
    print("\n[FIXING] Instagram handles in CSV files...\n")
    fix_instagram_handles()
    print("\n[COMPLETE] All Instagram handles updated to @jeanmorphius\n")

if __name__ == "__main__":
    main()
