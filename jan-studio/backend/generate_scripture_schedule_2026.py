#!/usr/bin/env python3
"""
Quick Start Script: Generate 2026 Scripture Schedule

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

Generates and exports scripture schedule for 2026.
Run this script to create the schedule and export to calendar.
"""

import sys
import os
import json
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from scripture_scheduler_2026 import generate_2026_scripture_schedule
from google_calendar_exporter import CalendarExportService


def main():
    print("=" * 70)
    print("Scripture Schedule Generator - 2026")
    print("All SIYEM Entities")
    print("=" * 70)
    print()
    
    # Generate schedule for all entities with optimized frequencies
    print("Generating scripture schedule for 2026 (all entities with optimized frequencies)...")
    print("\nEntity frequencies:")
    print("  - Edible London: 2 posts/week (Business - steady presence)")
    print("  - ILVEN Sea Moss: 2 posts/week (Business - consistent)")
    print("  - Jean Morphius: 4 posts/week (Spiral/Active - high frequency)")
    print("  - Karasahin (JK): 3 posts/week (Music/Emotion - regular)")
    print("  - Pierre Pressure: 3 posts/week (Barred Spiral/Structured - disciplined)")
    print("  - Uncle Ray Ramiz: 2 posts/week (Elliptical/Legacy - contemplative)")
    print("  - Siyem Media: 2 posts/week (Systems-level - moderate)")
    print()
    
    schedule = generate_2026_scripture_schedule()  # Uses optimized entity-specific frequencies
    
    print(f"[OK] Generated {schedule['summary']['total_posts']} scripture posts")
    print(f"\nPosts per entity (optimized frequencies):")
    for entity in schedule['summary']['entities']:
        count_key = f"{entity}_count"
        freq_key = f"{entity}_frequency"
        count = schedule['summary'].get(count_key, 0)
        freq = schedule['summary'].get(freq_key, 'N/A')
        entity_display = entity.replace('_', ' ').title()
        print(f"   - {entity_display}: {count} posts ({freq} posts/week)")
    print()
    
    # Save JSON
    json_path = Path(__file__).parent / 'scripture_schedule_2026.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False, default=str)
    print(f"[OK] Saved schedule to: {json_path}")
    print()
    
    # Export to iCal
    print("Exporting to iCal format...")
    service = CalendarExportService()
    
    # Export all posts
    ical_all = service.export_to_ical(
        schedule['all_posts'],
        calendar_name='Scripture Posts 2026 - All Brands',
        output_path=str(Path(__file__).parent / 'scripture_schedule_2026_all.ics')
    )
    print(f"[OK] Exported all posts to: scripture_schedule_2026_all.ics")
    
    # Export each entity separately
    for entity in schedule['summary']['entities']:
        if entity in schedule:
            entity_name = entity.replace('_', ' ').title()
            ical_content = service.export_to_ical(
                schedule[entity],
                calendar_name=f'Scripture Posts 2026 - {entity_name}',
                output_path=str(Path(__file__).parent / f'scripture_schedule_2026_{entity}.ics')
            )
            print(f"[OK] Exported {entity_name} posts to: scripture_schedule_2026_{entity}.ics")
    print()
    
    print("=" * 70)
    print("Next Steps:")
    print("1. Import the .ics files into Google Calendar:")
    print("   - Google Calendar > Settings > Import & Export")
    print("   - Select the .ics file")
    print("   - Choose which calendar to import to")
    print()
    print("2. Or use the API to export directly:")
    print("   POST /api/scripture-schedule/export/google")
    print()
    print("3. Review the schedule in scripture_schedule_2026.json")
    print("=" * 70)
    print()
    print("Peace, Love, Unity.")


if __name__ == "__main__":
    main()
