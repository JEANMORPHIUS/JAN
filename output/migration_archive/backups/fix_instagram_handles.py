"""
Fix Instagram account handles in CSV files to use @JEANMORPHIUS
"""

import csv
from pathlib import Path

OUTPUT_ROOT = Path("S:\\JAN\\output\\2026_social_content")

def fix_instagram_handles():
    """Update Instagram account columns to @JEANMORPHIUS"""
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
                    # Update Instagram account to @JEANMORPHIUS
                    if row[instagram_col] == "instagram" or row[instagram_col] == "":
                        row[instagram_col] = "@JEANMORPHIUS"
                rows.append(row)
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        print(f"  [OK] Fixed {csv_file.name}")

def main():
    print("\n[FIXING] Instagram handles in CSV files...\n")
    fix_instagram_handles()
    print("\n[COMPLETE] All Instagram handles updated to @JEANMORPHIUS\n")

if __name__ == "__main__":
    main()
