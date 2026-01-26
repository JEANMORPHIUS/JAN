#!/usr/bin/env python3
"""Start Content Generation - Begin Auto-Population

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

Begins actual content generation for all scheduled posts

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
from datetime import datetime
from scripture_scheduler_2026 import generate_2026_scripture_schedule
from content_auto_populator import ContentAutoPopulator


async def generate_content(batch_size=10, max_posts=None):
    """Generate content for scheduled posts"""
    print("=" * 70)
    print("CONTENT GENERATION - BEGINNING")
    print("=" * 70)
    print()
    
    # Load or generate schedule
    schedule_path = Path(__file__).parent / 'scripture_schedule_2026_with_formats.json'
    if schedule_path.exists():
        print(f"Loading schedule from: {schedule_path}")
        with open(schedule_path, 'r', encoding='utf-8') as f:
            schedule = json.load(f)
        print(f"[OK] Loaded {schedule['summary']['total_posts']} posts")
    else:
        print("Generating new schedule...")
        schedule = generate_2026_scripture_schedule()
        with open(schedule_path, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, indent=2, ensure_ascii=False, default=str)
        print(f"[OK] Generated and saved {schedule['summary']['total_posts']} posts")
    
    print()
    
    # Initialize populator
    print("Initializing content auto-populator...")
    populator = ContentAutoPopulator(base_url="http://localhost:8000")
    print("[OK] Populator ready")
    print()
    
    # Get posts to populate
    all_posts = schedule.get('all_posts', [])
    if max_posts:
        all_posts = all_posts[:max_posts]
    
    total_posts = len(all_posts)
    print(f"Starting generation for {total_posts} posts...")
    print(f"Batch size: {batch_size}")
    print()
    
    # Process in batches
    populated_posts = []
    errors = []
    
    for i in range(0, total_posts, batch_size):
        batch = all_posts[i:i+batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (total_posts + batch_size - 1) // batch_size
        
        print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} posts)...")
        
        # Populate batch
        batch_schedule = {
            'all_posts': batch,
            'summary': schedule.get('summary', {})
        }
        
        try:
            populated_batch = await populator.populate_schedule(batch_schedule)
            batch_populated = populated_batch.get('all_posts', [])
            
            # Count successes
            success_count = sum(1 for p in batch_populated if p.get('content_populated'))
            error_count = sum(1 for p in batch_populated if p.get('content_population_error'))
            
            populated_posts.extend(batch_populated)
            
            print(f"  [OK] Batch {batch_num}: {success_count} populated, {error_count} errors")
            
            # Show sample from batch
            if batch_populated and batch_populated[0].get('content_populated'):
                sample = batch_populated[0]
                gen_content = sample.get('generated_content', {})
                if gen_content:
                    fmt = list(gen_content.keys())[0]
                    print(f"  Sample: {fmt} content generated for {sample.get('metadata', {}).get('brand', 'unknown')}")
            
        except Exception as e:
            print(f"  [ERROR] Batch {batch_num} failed: {str(e)}")
            errors.extend(batch)
        
        print()
    
    # Update schedule with populated posts
    schedule['all_posts'] = populated_posts
    schedule['content_populated'] = True
    schedule['content_populated_at'] = datetime.utcnow().isoformat()
    schedule['total_populated'] = sum(1 for p in populated_posts if p.get('content_populated'))
    schedule['total_errors'] = sum(1 for p in populated_posts if p.get('content_population_error'))
    
    # Save populated schedule
    output_path = Path(__file__).parent / 'scripture_schedule_2026_populated.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False, default=str)
    
    print("=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print()
    print(f"Total posts processed: {total_posts}")
    print(f"Successfully populated: {schedule['total_populated']}")
    print(f"Errors: {schedule['total_errors']}")
    print(f"Pending: {total_posts - schedule['total_populated'] - schedule['total_errors']}")
    print()
    print(f"Saved to: {output_path}")
    print()
    
    # Show format breakdown
    format_stats = {}
    for post in populated_posts:
        if post.get('content_populated'):
            fmt = post.get('format_notes', {}).get('primary_format', 'unknown')
            format_stats[fmt] = format_stats.get(fmt, 0) + 1
    
    if format_stats:
        print("Format breakdown (populated):")
        for fmt, count in sorted(format_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {fmt}: {count} posts")
        print()
    
    await populator.close()
    
    print("=" * 70)
    print("Next Steps:")
    print("1. Review populated content in: scripture_schedule_2026_populated.json")
    print("2. Export to calendar: POST /api/scripture-schedule/export/google")
    print("3. Check status: GET /api/content-population/status")
    print("=" * 70)
    print()
    print("Peace, Love, Unity.")


if __name__ == "__main__":
    import sys
    
    # Parse arguments
    batch_size = 10
    max_posts = None
    
    if '--batch' in sys.argv:
        idx = sys.argv.index('--batch')
        if idx + 1 < len(sys.argv):
            batch_size = int(sys.argv[idx + 1])
    
    if '--limit' in sys.argv:
        idx = sys.argv.index('--limit')
        if idx + 1 < len(sys.argv):
            max_posts = int(sys.argv[idx + 1])
    
    print(f"Starting generation with batch_size={batch_size}, max_posts={max_posts or 'all'}")
    print()
    
    asyncio.run(generate_content(batch_size=batch_size, max_posts=max_posts))
