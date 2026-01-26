"""COMPLETE AUTOMATION: Visualize and Schedule All 2026 Social Posts
Generates visuals, exports campaigns, creates scheduler files

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
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import json
import os
import csv
from datetime import datetime, timedelta
from pathlib import Path
import requests
from typing import Dict, List, Any

# Base paths
SIYEM_ROOT = Path("S:\\SIYEM")
PUBLISHING_ROOT = SIYEM_ROOT / "05_PUBLISHING"
OUTPUT_ROOT = Path("S:\\JAN\\output\\2026_social_content")

# API endpoints (adjust if SIYEM server is running)
SIYEM_API_BASE = "http://localhost:8000"  # Default SIYEM API port

# Entity configurations
ENTITIES = {
    "JEAN MORPHIUS": {
        "folder": "Jean",
        "style_preset": "Glitch Noir",
        "color_scheme": "jean_primary",
        "platform": "instagram",
        "instagram_handle": "@jeanmorphius",
        "tiktok_handle": "@jeanmorphius"
    },
    "PIERRE": {
        "folder": "Pierre",
        "style_preset": "Brutalist Fighter",
        "color_scheme": "pierre_primary",
        "platform": "instagram"
    },
    "RAMIZ": {
        "folder": "Ramiz",
        "style_preset": "Anatolian Warmth",
        "color_scheme": "ramiz_primary",
        "platform": "instagram"
    },
    "KARASAHIN": {
        "folder": "Karasahin",
        "style_preset": "Studio Midnight",
        "color_scheme": "karasahin_primary",
        "platform": "instagram"
    }
}

def load_campaign(entity: str) -> Dict[str, Any]:
    """Load campaign JSON for entity"""
    entity_config = ENTITIES[entity]
    campaign_path = PUBLISHING_ROOT / entity_config["folder"] / "2026-01-01" / "Campaigns" / "weekly_posts_2026" / "campaign.json"
    
    if not campaign_path.exists():
        raise FileNotFoundError(f"Campaign not found: {campaign_path}")
    
    with open(campaign_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_visual_prompts_for_campaign(campaign: Dict[str, Any], entity: str) -> List[Dict[str, Any]]:
    """Generate visual prompts for all posts in campaign"""
    entity_config = ENTITIES[entity]
    prompts = []
    
    for post in campaign["posts"]:
        prompt_data = {
            "week": post["week"],
            "date": post["date"],
            "quote": post["quote"],
            "entity": entity,
            "style_preset": entity_config["style_preset"],
            "color_scheme": entity_config["color_scheme"],
            "aspect_ratio": post.get("aspect_ratio", "1:1"),
            "description": post.get("description"),
            "visual_prompt": None  # Will be generated
        }
        prompts.append(prompt_data)
    
    return prompts

def export_to_later_com(campaign: Dict[str, Any], entity: str, output_dir: Path) -> str:
    """Export campaign to Later.com CSV format"""
    entity_config = ENTITIES[entity]
    filename = f"{entity}_2026_weekly_posts_later_com.csv"
    filepath = output_dir / filename
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Later.com CSV header
        writer.writerow([
            "Photo/Video",
            "Text",
            "Link",
            "First Comment",
            "Instagram First Comment",
            "Pinterest Description",
            "Time",
            "Instagram Accounts",
            "Facebook Accounts",
            "Twitter Accounts",
            "Pinterest Boards",
            "TikTok Accounts",
            "LinkedIn Accounts"
        ])
        
        for post in campaign["posts"]:
            # Parse date and set time (default to 9:00 AM)
            post_date = datetime.strptime(post["date"], "%Y-%m-%d")
            post_time = post_date.strftime("%Y-%m-%d 09:00:00")
            
            writer.writerow([
                "",  # Photo/Video (to be filled after image generation)
                post["quote"],
                "",  # Link
                "",  # First Comment
                "",  # Instagram First Comment
                "",  # Pinterest Description
                post_time,
                entity_config.get("instagram_handle", entity_config["platform"]),  # Instagram account
                "",  # Facebook
                "",  # Twitter
                "",  # Pinterest
                "",  # TikTok
                ""   # LinkedIn
            ])
    
    return str(filepath)

def export_to_metricool(campaign: Dict[str, Any], entity: str, output_dir: Path) -> str:
    """Export campaign to Metricool CSV format"""
    filename = f"{entity}_2026_weekly_posts_metricool.csv"
    filepath = output_dir / filename
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Metricool CSV header
        writer.writerow([
            "Date",
            "Time",
            "Text",
            "Image",
            "Link",
            "Instagram",
            "Facebook",
            "Twitter",
            "LinkedIn",
            "Pinterest",
            "TikTok"
        ])
        
        for post in campaign["posts"]:
            post_date = datetime.strptime(post["date"], "%Y-%m-%d")
            date_str = post_date.strftime("%Y-%m-%d")
            time_str = "09:00"
            
            writer.writerow([
                date_str,
                time_str,
                post["quote"],
                "",  # Image (to be filled after image generation)
                "",  # Link
                "Yes",  # Instagram
                "",  # Facebook
                "",  # Twitter
                "",  # LinkedIn
                "",  # Pinterest
                ""   # TikTok
            ])
    
    return str(filepath)

def export_to_publer(campaign: Dict[str, Any], entity: str, output_dir: Path) -> str:
    """Export campaign to Publer CSV format"""
    filename = f"{entity}_2026_weekly_posts_publer.csv"
    filepath = output_dir / filename
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Publer CSV header
        writer.writerow([
            "Date",
            "Time",
            "Text",
            "Image",
            "Link",
            "Instagram",
            "Facebook",
            "Twitter",
            "LinkedIn"
        ])
        
        for post in campaign["posts"]:
            post_date = datetime.strptime(post["date"], "%Y-%m-%d")
            date_str = post_date.strftime("%Y-%m-%d")
            time_str = "09:00"
            
            writer.writerow([
                date_str,
                time_str,
                post["quote"],
                "",  # Image (to be filled after image generation)
                "",  # Link
                "Yes",  # Instagram
                "",  # Facebook
                "",  # Twitter
                ""   # LinkedIn
            ])
    
    return str(filepath)

def export_to_google_sheets_format(campaign: Dict[str, Any], entity: str, output_dir: Path) -> str:
    """Export campaign to Google Sheets CSV format"""
    filename = f"{entity}_2026_weekly_posts_google_sheets.csv"
    filepath = output_dir / filename
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Google Sheets header
        writer.writerow([
            "Week",
            "Date",
            "Entity",
            "Quote",
            "Image Path",
            "Visual Prompt",
            "Status",
            "Platform",
            "Scheduled",
            "Instagram Handle",
            "TikTok Handle"
        ])
        
        for post in campaign["posts"]:
            writer.writerow([
                post["week"],
                post["date"],
                entity,
                post["quote"],
                "",  # Image Path (to be filled after image generation)
                post.get("visual_prompt", ""),
                post.get("status", "ready"),
                ENTITIES[entity]["platform"],
                "No",  # Scheduled
                ENTITIES[entity].get("instagram_handle", ""),  # Instagram Handle
                ENTITIES[entity].get("tiktok_handle", "")  # TikTok Handle
            ])
    
    return str(filepath)

def create_master_calendar(all_campaigns: Dict[str, Dict[str, Any]], output_dir: Path) -> str:
    """Create master content calendar with all entities"""
    filename = "MASTER_2026_CONTENT_CALENDAR.csv"
    filepath = output_dir / filename
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Date",
            "Week",
            "Entity",
            "Quote",
            "Image Path",
            "Platform",
            "Status"
        ])
        
        # Collect all posts from all entities
        all_posts = []
        for entity, campaign in all_campaigns.items():
            for post in campaign["posts"]:
                all_posts.append({
                    "date": post["date"],
                    "week": post["week"],
                    "entity": entity,
                    "quote": post["quote"],
                    "platform": ENTITIES[entity]["platform"],
                    "status": post.get("status", "ready")
                })
        
        # Sort by date
        all_posts.sort(key=lambda x: x["date"])
        
        # Write to CSV
        for post in all_posts:
            writer.writerow([
                post["date"],
                post["week"],
                post["entity"],
                post["quote"],
                "",  # Image Path (to be filled)
                post["platform"],
                post["status"]
            ])
    
    return str(filepath)

def create_visual_prompts_file(all_prompts: Dict[str, List[Dict[str, Any]]], output_dir: Path) -> str:
    """Create JSON file with all visual prompts for batch generation"""
    filename = "ALL_VISUAL_PROMPTS_2026.json"
    filepath = output_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(all_prompts, f, ensure_ascii=False, indent=2)
    
    return str(filepath)

def print_summary(all_campaigns: Dict[str, Dict[str, Any]], output_files: Dict[str, List[str]]):
    """Print summary of generated files"""
    print("\n" + "="*80)
    print("2026 SOCIAL CONTENT VISUALIZATION & SCHEDULING COMPLETE".center(80))
    print("="*80 + "\n")
    
    print("[CAMPAIGN SUMMARY]")
    print("-" * 80)
    total_posts = 0
    for entity, campaign in all_campaigns.items():
        post_count = len(campaign["posts"])
        total_posts += post_count
        print(f"  {entity:12} : {post_count:3} posts")
    print(f"\n  {'TOTAL':12} : {total_posts:3} posts")
    print("\n" + "-" * 80)
    
    print("\n[GENERATED FILES]")
    print("-" * 80)
    for category, files in output_files.items():
        print(f"\n  {category}:")
        for file in files:
            print(f"    [OK] {Path(file).name}")
    
    print("\n" + "="*80)
    print("NEXT STEPS:".center(80))
    print("="*80)
    print("\n1. VISUAL GENERATION:")
    print("   - Use Visual Arts Studio bulk import")
    print("   - Or call /visual/bulk-create API with ALL_VISUAL_PROMPTS_2026.json")
    print("   - Generate 208 images (52 per entity)")
    print("\n2. SCHEDULER IMPORT:")
    print("   - Later.com: Import *_later_com.csv files")
    print("   - Metricool: Import *_metricool.csv files")
    print("   - Publer: Import *_publer.csv files")
    print("\n3. MASTER CALENDAR:")
    print("   - Import MASTER_2026_CONTENT_CALENDAR.csv to Google Sheets")
    print("   - Use for tracking and monitoring")
    print("\n" + "="*80 + "\n")

def main():
    """Main execution"""
    print("\n" + "="*80)
    print("GENERATING VISUALS & SCHEDULING FOR ALL 2026 SOCIAL POSTS".center(80))
    print("="*80 + "\n")
    
    # Create output directory
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Load all campaigns
    print("[LOADING] Campaigns...")
    all_campaigns = {}
    all_prompts = {}
    
    for entity in ENTITIES.keys():
        print(f"  Loading {entity}...")
        campaign = load_campaign(entity)
        all_campaigns[entity] = campaign
        all_prompts[entity] = generate_visual_prompts_for_campaign(campaign, entity)
        print(f"    [OK] {len(campaign['posts'])} posts loaded")
    
    print("\n[EXPORTING] Scheduler files...")
    output_files = {
        "Later.com Exports": [],
        "Metricool Exports": [],
        "Publer Exports": [],
        "Google Sheets Exports": [],
        "Master Files": []
    }
    
    # Export for each entity
    for entity in ENTITIES.keys():
        campaign = all_campaigns[entity]
        print(f"  Exporting {entity}...")
        
        # Later.com
        later_file = export_to_later_com(campaign, entity, OUTPUT_ROOT)
        output_files["Later.com Exports"].append(later_file)
        print(f"    [OK] Later.com: {Path(later_file).name}")
        
        # Metricool
        metricool_file = export_to_metricool(campaign, entity, OUTPUT_ROOT)
        output_files["Metricool Exports"].append(metricool_file)
        print(f"    [OK] Metricool: {Path(metricool_file).name}")
        
        # Publer
        publer_file = export_to_publer(campaign, entity, OUTPUT_ROOT)
        output_files["Publer Exports"].append(publer_file)
        print(f"    [OK] Publer: {Path(publer_file).name}")
        
        # Google Sheets
        gsheets_file = export_to_google_sheets_format(campaign, entity, OUTPUT_ROOT)
        output_files["Google Sheets Exports"].append(gsheets_file)
        print(f"    [OK] Google Sheets: {Path(gsheets_file).name}")
    
    # Create master calendar
    print("\n[CREATING] Master calendar...")
    master_calendar = create_master_calendar(all_campaigns, OUTPUT_ROOT)
    output_files["Master Files"].append(master_calendar)
    print(f"  [OK] Master Calendar: {Path(master_calendar).name}")
    
    # Create visual prompts file
    print("\n[CREATING] Visual prompts file...")
    prompts_file = create_visual_prompts_file(all_prompts, OUTPUT_ROOT)
    output_files["Master Files"].append(prompts_file)
    print(f"  [OK] Visual Prompts: {Path(prompts_file).name}")
    
    # Print summary
    print_summary(all_campaigns, output_files)
    
    print("\n[COMPLETE] All files generated and ready for visualization & scheduling!")
    print(f"Output directory: {OUTPUT_ROOT}\n")

if __name__ == "__main__":
    main()
