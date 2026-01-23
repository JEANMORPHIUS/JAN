"""
Update all campaign files from "JEAN" to "JEAN MORPHIUS" with @JEANMORPHIUS handles
Keeps jean@siyem.org unchanged
"""

import csv
import json
from pathlib import Path

OUTPUT_ROOT = Path("S:\\JAN\\output\\2026_social_content")

def update_csv_files():
    """Update all CSV files to use JEAN MORPHIUS"""
    csv_files = list(OUTPUT_ROOT.glob("JEAN_*.csv"))
    
    for csv_file in csv_files:
        print(f"Updating {csv_file.name}...")
        
        # Read CSV
        rows = []
        with open(csv_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)
            
            for row in reader:
                # Update entity name in relevant columns
                updated_row = []
                for i, cell in enumerate(row):
                    if cell == "JEAN" or cell == "Jean":
                        updated_row.append("JEAN MORPHIUS")
                    elif "instagram" in cell.lower() and "@" not in cell:
                        # Update Instagram account reference
                        updated_row.append("@JEANMORPHIUS")
                    else:
                        updated_row.append(cell)
                rows.append(updated_row)
        
        # Write updated CSV
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        print(f"  [OK] Updated {csv_file.name}")

def update_master_calendar():
    """Update master calendar CSV"""
    master_file = OUTPUT_ROOT / "MASTER_2026_CONTENT_CALENDAR.csv"
    
    if not master_file.exists():
        print("Master calendar not found")
        return
    
    print(f"Updating {master_file.name}...")
    
    rows = []
    with open(master_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)
        
        for row in reader:
            # Update entity name in Entity column (index 2)
            if len(row) > 2 and row[2] == "JEAN":
                row[2] = "JEAN MORPHIUS"
            rows.append(row)
    
    with open(master_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"  [OK] Updated {master_file.name}")

def update_visual_prompts():
    """Update visual prompts JSON"""
    prompts_file = OUTPUT_ROOT / "ALL_VISUAL_PROMPTS_2026.json"
    
    if not prompts_file.exists():
        print("Visual prompts file not found")
        return
    
    print(f"Updating {prompts_file.name}...")
    
    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update JEAN to JEAN MORPHIUS
    if "JEAN" in data:
        data["JEAN MORPHIUS"] = data.pop("JEAN")
        # Update entity field in all prompts
        for prompt in data["JEAN MORPHIUS"]:
            if prompt.get("entity") == "JEAN":
                prompt["entity"] = "JEAN MORPHIUS"
    
    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  [OK] Updated {prompts_file.name}")

def update_campaign_json():
    """Update campaign JSON file"""
    campaign_file = Path("S:\\SIYEM\\05_PUBLISHING\\Jean\\2026-01-01\\Campaigns\\weekly_posts_2026\\campaign.json")
    
    if not campaign_file.exists():
        print("Campaign JSON not found")
        return
    
    print(f"Updating {campaign_file.name}...")
    
    with open(campaign_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update campaign name and entity
    data["campaign_name"] = data["campaign_name"].replace("JEAN", "JEAN MORPHIUS")
    data["entity"] = "JEAN MORPHIUS"
    
    with open(campaign_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  [OK] Updated {campaign_file.name}")

def main():
    print("\n" + "="*80)
    print("UPDATING JEAN TO JEAN MORPHIUS".center(80))
    print("="*80 + "\n")
    
    print("[UPDATING] CSV files...")
    update_csv_files()
    
    print("\n[UPDATING] Master calendar...")
    update_master_calendar()
    
    print("\n[UPDATING] Visual prompts...")
    update_visual_prompts()
    
    print("\n[UPDATING] Campaign JSON...")
    update_campaign_json()
    
    print("\n" + "="*80)
    print("[COMPLETE] All files updated to JEAN MORPHIUS".center(80))
    print("Social handles: @JEANMORPHIUS (Instagram, TikTok)".center(80))
    print("Email unchanged: jean@siyem.org".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
