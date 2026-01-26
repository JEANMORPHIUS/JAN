#!/usr/bin/env python3
"""Begin Auto-Population - Start Content Generation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

Generates schedule and begins auto-population process

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import asyncio
import json
from pathlib import Path
from scripture_scheduler_2026 import generate_2026_scripture_schedule
from content_auto_populator import ContentAutoPopulator


async def main():
    print("=" * 70)
    print("Content Auto-Population - Beginning Generation")
    print("=" * 70)
    print()
    
    # Step 1: Generate schedule with formats
    print("Step 1: Generating schedule with format assignments...")
    schedule = generate_2026_scripture_schedule()
    print(f"[OK] Generated {schedule['summary']['total_posts']} posts")
    print(f"   Entities: {', '.join(schedule['summary']['entities'])}")
    print()
    
    # Show format distribution
    format_counts = {}
    for post in schedule['all_posts']:
        fmt = post.get('format_notes', {}).get('primary_format', 'unknown')
        format_counts[fmt] = format_counts.get(fmt, 0) + 1
    
    print("Format distribution:")
    for fmt, count in sorted(format_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / schedule['summary']['total_posts']) * 100
        print(f"   - {fmt}: {count} posts ({pct:.1f}%)")
    print()
    
    # Step 2: Save schedule
    schedule_path = Path(__file__).parent / 'scripture_schedule_2026_with_formats.json'
    with open(schedule_path, 'w', encoding='utf-8') as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False, default=str)
    print(f"[OK] Saved schedule to: {schedule_path}")
    print()
    
    # Step 3: Begin auto-population (test with small batch first)
    print("Step 2: Beginning auto-population (testing with first 5 posts)...")
    print("   Note: This requires AI services to be running")
    print()
    
    # Initialize populator
    populator = ContentAutoPopulator(base_url="http://localhost:8000")
    
    try:
        # Test with first 5 posts
        test_schedule = {
            'all_posts': schedule['all_posts'][:5],
            'summary': schedule['summary']
        }
        
        print("Populating first 5 posts...")
        populated_schedule = await populator.populate_schedule(test_schedule)
        
        # Show results
        populated_count = populated_schedule.get('total_populated', 0)
        print(f"[OK] Populated {populated_count} posts")
        print()
        
        # Show sample generated content
        if populated_schedule['all_posts']:
            sample = populated_schedule['all_posts'][0]
            if sample.get('content_populated'):
                print("Sample generated content:")
                gen_content = sample.get('generated_content', {})
                for fmt, content in gen_content.items():
                    if isinstance(content, dict) and 'content' in content:
                        preview = content['content'][:100] + "..." if len(content['content']) > 100 else content['content']
                        print(f"   - {fmt}: {preview}")
                    elif isinstance(content, dict) and 'script' in content:
                        preview = content['script'][:100] + "..." if len(content.get('script', '')) > 100 else content.get('script', '')
                        print(f"   - {fmt} (script): {preview}")
                print()
            else:
                print("[WARNING] Sample post not populated (check AI services)")
                if sample.get('content_population_error'):
                    print(f"   Error: {sample['content_population_error']}")
                print()
        
        # Save populated schedule
        populated_path = Path(__file__).parent / 'scripture_schedule_2026_populated_sample.json'
        with open(populated_path, 'w', encoding='utf-8') as f:
            json.dump(populated_schedule, f, indent=2, ensure_ascii=False, default=str)
        print(f"[OK] Saved populated sample to: {populated_path}")
        print()
        
        print("=" * 70)
        print("Next Steps:")
        print("1. Review populated sample to verify AI services are working")
        print("2. If successful, populate full schedule:")
        print("   POST /api/content-population/populate-schedule")
        print("3. Or use the script with full schedule:")
        print("   python begin_auto_population.py --full")
        print("=" * 70)
        
    except Exception as e:
        print(f"[ERROR] Error during population: {str(e)}")
        print()
        print("This is expected if AI services are not running.")
        print("To populate content:")
        print("1. Ensure AI services are running (WRITER, ARTIST, etc.)")
        print("2. Update base_url in ContentAutoPopulator if needed")
        print("3. Retry population")
        print()
    
    finally:
        await populator.close()
    
    print()
    print("Peace, Love, Unity.")


if __name__ == "__main__":
    import sys
    
    if '--full' in sys.argv:
        # Full population (commented out for safety - uncomment when ready)
        print("[WARNING] Full population requires AI services to be running")
        print("   Uncomment the full population code when ready")
        # asyncio.run(main_full())
    else:
        asyncio.run(main())
