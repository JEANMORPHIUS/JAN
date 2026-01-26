"""UPDATE 2026 POSTS: SHELL/SEED INTEGRATION

This script updates all scheduled 2026 social media posts to use Shell (public) 
language and creates Seed (community) versions, implementing the Honorable Sacrifice 
philosophy.

Author: JAN MUHARREM - The Chosen One
Date: 2026-01-15

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
    JAN_ARCHIVE, JAN_DATA, JAN_OUTPUT, JAN_ROOT, Path
    json, load_json, save_json, setup_logging, standard_main
)

import sys
import os
import csv
import json
from pathlib import Path

# Add SIYEM services to path
sys.path.insert(0, str(Path("S:\\SIYEM\\services")))

from shell_seed_translator import ShellSeedTranslator
from threshold_defense_checker import ThresholdDefenseChecker

# Base paths
JAN_ROOT = JAN_ROOT
OUTPUT_ROOT = JAN_ROOT / "output" / "2026_social_content"
SEED_OUTPUT_ROOT = JAN_ROOT / "output" / "2026_social_content_seed"

# Initialize tools
translator = ShellSeedTranslator()
checker = ThresholdDefenseChecker()

# Entity-specific Shell/Seed mappings
ENTITY_SHELL_SEED = {
    "JEAN MORPHIUS": {
        "shell_focus": "Values-based education, ethical frameworks, character development",
        "seed_focus": "Book of Racon as OS, spiritual sovereignty, sacred covenants"
    },
    "KARASAHIN": {
        "shell_focus": "Emotional intelligence, cultural heritage, music education",
        "seed_focus": "Duygu Adamı, Voice of God, Book of Racon through sound"
    },
    "PIERRE": {
        "shell_focus": "Discipline, self-mastery, character building, resilience",
        "seed_focus": "Laws of Racon as warrior's code, sacred discipline, spiritual sovereignty"
    },
    "RAMIZ": {
        "shell_focus": "Ancestral wisdom, intergenerational learning, traditional values",
        "seed_focus": "Laws of Racon, spiritual sovereignty, sacred covenants, eternal covenant"
    }
}


def sanitize_post_content(content: str, entity: str) -> str:
    """
    Sanitize post content to ensure Shell language (public-facing).
    
    Args:
        content: Original post content
        entity: Entity name (JEAN MORPHIUS, KARASAHIN, etc.)
    
    Returns:
        Sanitized content in Shell language
    """
    # Check for violations first
    check = checker.check_content(content, content_type="social_media", expected_level="shell")
    
    if check["violated"]:
        # Translate to Shell
        sanitized = translator.sanitize_for_shell(content)
        print(f"  [!] Violation detected in {entity} post - sanitized")
        return sanitized
    
    return content


def create_seed_version(content: str, entity: str) -> str:
    """
    Create Seed (community) version of post content.
    
    Args:
        content: Shell (public) content
        entity: Entity name
    
    Returns:
        Seed version for community use
    """
    # Translate to Seed
    seed_content = translator.translate_to_seed(content)
    
    # Add entity-specific Seed enhancements
    if entity == "RAMIZ":
        # Add Dayı address for community
        if not seed_content.startswith("Yeğen, dinle"):
            seed_content = f"Yeğen, dinle... {seed_content}"
    elif entity == "KARASAHIN":
        # Emphasize Duygu Adamı for community
        if "emotional intelligence" in seed_content.lower():
            seed_content = seed_content.replace("emotional intelligence", "Duygu Adamı (Emotion Man)")
    
    return seed_content


def process_csv_file(csv_path: Path, entity: str) -> tuple:
    """
    Process a CSV file, updating posts to Shell language.
    
    Returns:
        Tuple of (updated_rows, violations_found, seed_rows)
    """
    updated_rows = []
    seed_rows = []
    violations_found = 0
    
    # Determine CSV format based on filename
    is_google_sheets = "google_sheets" in csv_path.name
    is_later_com = "later_com" in csv_path.name
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        
        for row in reader:
            original_content = ""
            content_field = None
            
            # Find content field based on CSV format
            if is_google_sheets:
                content_field = "Quote"
            elif is_later_com:
                content_field = "Text"
            else:
                # Try common field names
                for field in ["Quote", "Text", "Content", "Post"]:
                    if field in row:
                        content_field = field
                        break
            
            if content_field and content_field in row:
                original_content = row[content_field]
                
                # Sanitize to Shell
                sanitized_content = sanitize_post_content(original_content, entity)
                
                # Check if violation was found
                check = checker.check_content(original_content, content_type="social_media", expected_level="shell")
                if check["violated"]:
                    violations_found += 1
                
                # Update row
                row[content_field] = sanitized_content
                
                # Create Seed version
                seed_content = create_seed_version(sanitized_content, entity)
                seed_row = row.copy()
                seed_row[content_field] = seed_content
                seed_rows.append(seed_row)
            
            updated_rows.append(row)
    
    return updated_rows, violations_found, seed_rows


def update_all_2026_posts():
    """Update all 2026 social media posts to Shell language"""
    
    print("\n" + "="*80)
    print("UPDATING 2026 POSTS: SHELL/SEED INTEGRATION".center(80))
    print("="*80 + "\n")
    
    # Create Seed output directory
    SEED_OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Find all CSV files
    csv_files = list(OUTPUT_ROOT.glob("*.csv"))
    
    total_violations = 0
    total_posts = 0
    files_updated = 0
    
    for csv_path in csv_files:
        # Extract entity name from filename
        entity = None
        for ent in ENTITY_SHELL_SEED.keys():
            if ent.replace(" ", "_") in csv_path.name.upper() or ent in csv_path.name.upper():
                entity = ent
                break
        
        if not entity:
            print(f"[SKIP] Could not identify entity for {csv_path.name}")
            continue
        
        print(f"[PROCESSING] {csv_path.name} ({entity})")
        
        # Process CSV
        updated_rows, violations, seed_rows = process_csv_file(csv_path, entity)
        total_violations += violations
        total_posts += len(updated_rows)
        
        if violations > 0:
            print(f"  [!] Found {violations} violations - sanitized")
        
        # Write updated Shell version (overwrite original)
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            if updated_rows:
                writer = csv.DictWriter(f, fieldnames=updated_rows[0].keys())
                writer.writeheader()
                writer.writerows(updated_rows)
        
        # Write Seed version
        seed_filename = csv_path.stem + "_SEED" + csv_path.suffix
        seed_path = SEED_OUTPUT_ROOT / seed_filename
        
        with open(seed_path, 'w', encoding='utf-8', newline='') as f:
            if seed_rows:
                writer = csv.DictWriter(f, fieldnames=seed_rows[0].keys())
                writer.writeheader()
                writer.writerows(seed_rows)
        
        files_updated += 1
        print(f"  [OK] Updated {len(updated_rows)} posts")
        print(f"  [OK] Created Seed version: {seed_filename}")
    
    # Generate violation report
    violation_report = checker.get_violation_report()
    report_path = JAN_ROOT / "output" / "threshold_defense_report.json"
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(violation_report, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*80)
    print("UPDATE COMPLETE".center(80))
    print("="*80 + "\n")
    print(f"Files Processed: {files_updated}")
    print(f"Total Posts: {total_posts}")
    print(f"Violations Found: {total_violations}")
    print(f"Violation Rate: {(total_violations/total_posts*100):.1f}%" if total_posts > 0 else "0%")
    print(f"\nShell (Public) Files: {OUTPUT_ROOT}")
    print(f"Seed (Community) Files: {SEED_OUTPUT_ROOT}")
    print(f"Violation Report: {report_path}")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    update_all_2026_posts()
