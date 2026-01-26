#!/usr/bin/env python3
"""Complete Generation - Generate All Posts with Fallback

Uses mock generator to complete all posts, maintaining structure
for later AI service enhancement

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
from mock_content_generator import MockContentGenerator


async def complete_all_posts():
    """Complete generation for all posts using mock generator"""
    print("=" * 70)
    print("COMPLETE GENERATION - ALL POSTS")
    print("=" * 70)
    print()
    
    # Load schedule
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
    
    # Get all posts
    all_posts = schedule.get('all_posts', [])
    total_posts = len(all_posts)
    
    print(f"Generating content for ALL {total_posts} posts...")
    print("Using mock generator (ready for AI service enhancement)...")
    print()
    
    populated_posts = []
    start_time = datetime.now()
    
    for i, post in enumerate(all_posts, 1):
        if i % 50 == 0:
            print(f"Processing post {i}/{total_posts}...", end="\r", flush=True)
        
        # Initialize generated_content
        if 'generated_content' not in post:
            post['generated_content'] = {}
        
        # Get format and entity
        primary_format = post.get('format_notes', {}).get('primary_format', 'text_short')
        entity = post.get('metadata', {}).get('brand', 'edible_london')
        
        # Generate content based on format
        try:
            if primary_format == 'text_short':
                post['generated_content']['text_short'] = MockContentGenerator.generate_text_short(post, entity)
            elif primary_format == 'text_long':
                post['generated_content']['text_long'] = MockContentGenerator.generate_text_long(post, entity)
            elif primary_format == 'video':
                post['generated_content']['video'] = MockContentGenerator.generate_video(post, entity)
            elif primary_format == 'audio':
                post['generated_content']['audio'] = MockContentGenerator.generate_audio(post, entity)
            elif primary_format == 'image':
                post['generated_content']['image'] = MockContentGenerator.generate_image(post, entity)
            
            post['content_populated'] = True
            post['content_populated_at'] = datetime.utcnow().isoformat()
            
        except Exception as e:
            post['content_population_error'] = str(e)
        
        populated_posts.append(post)
    
    print(f"\n[OK] Processed all {total_posts} posts")
    print()
    
    # Update schedule
    schedule['all_posts'] = populated_posts
    schedule['content_populated'] = True
    schedule['content_populated_at'] = datetime.utcnow().isoformat()
    schedule['total_populated'] = sum(1 for p in populated_posts if p.get('content_populated'))
    schedule['total_errors'] = sum(1 for p in populated_posts if p.get('content_population_error'))
    
    # Save populated schedule
    output_path = Path(__file__).parent / 'scripture_schedule_2026_populated.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False, default=str)
    
    elapsed_time = (datetime.now() - start_time).total_seconds()
    
    print("=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print()
    print(f"Total posts processed: {total_posts}")
    print(f"Successfully populated: {schedule['total_populated']}")
    print(f"Errors: {schedule['total_errors']}")
    print(f"Time elapsed: {elapsed_time:.1f} seconds")
    print()
    print(f"Saved to: {output_path}")
    print()
    
    # Format breakdown
    format_stats = {}
    for post in populated_posts:
        if post.get('content_populated'):
            fmt = post.get('format_notes', {}).get('primary_format', 'unknown')
            format_stats[fmt] = format_stats.get(fmt, 0) + 1
    
    if format_stats:
        print("Format breakdown:")
        for fmt, count in sorted(format_stats.items(), key=lambda x: x[1], reverse=True):
            pct = (count / schedule['total_populated']) * 100 if schedule['total_populated'] > 0 else 0
            print(f"  - {fmt}: {count} posts ({pct:.1f}%)")
        print()
    
    print("=" * 70)
    print("All posts generated! Content is ready for:")
    print("1. Review and enhancement with AI services")
    print("2. Calendar export")
    print("3. Publishing")
    print("=" * 70)
    print()
    print("Peace, Love, Unity.")


if __name__ == "__main__":
    asyncio.run(complete_all_posts())
