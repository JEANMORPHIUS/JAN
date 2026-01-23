#!/usr/bin/env python3
"""
Run Services and Generate All Content

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

Starts backend services and generates all content for 941 posts
"""

import subprocess
import sys
import time
import asyncio
import json
from pathlib import Path
from datetime import datetime
from scripture_scheduler_2026 import generate_2026_scripture_schedule
from content_auto_populator import ContentAutoPopulator


async def generate_all_content():
    """Generate all content for all posts"""
    print("=" * 70)
    print("CONTENT GENERATION - ALL POSTS")
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
    
    # Initialize populator
    print("Initializing content auto-populator...")
    populator = ContentAutoPopulator(base_url="http://localhost:8000")
    print("[OK] Populator ready")
    print()
    
    # Get all posts
    all_posts = schedule.get('all_posts', [])
    total_posts = len(all_posts)
    
    print(f"Starting generation for ALL {total_posts} posts...")
    print("This will take some time. Processing in batches of 10...")
    print()
    
    # Process in batches
    batch_size = 10
    populated_posts = []
    total_batches = (total_posts + batch_size - 1) // batch_size
    
    start_time = datetime.now()
    
    for i in range(0, total_posts, batch_size):
        batch = all_posts[i:i+batch_size]
        batch_num = (i // batch_size) + 1
        
        print(f"Batch {batch_num}/{total_batches} ({len(batch)} posts)...", end=" ", flush=True)
        
        # Populate batch
        batch_schedule = {
            'all_posts': batch,
            'summary': schedule.get('summary', {})
        }
        
        try:
            populated_batch = await populator.populate_schedule(batch_schedule)
            batch_populated = populated_batch.get('all_posts', [])
            
            success_count = sum(1 for p in batch_populated if p.get('content_populated'))
            error_count = sum(1 for p in batch_populated if p.get('content_population_error'))
            
            populated_posts.extend(batch_populated)
            
            print(f"[OK] {success_count} populated, {error_count} errors")
            
        except Exception as e:
            print(f"[ERROR] {str(e)[:50]}")
            # Add posts with error flag
            for post in batch:
                post['content_population_error'] = str(e)
                populated_posts.append(post)
        
        # Progress update every 10 batches
        if batch_num % 10 == 0:
            elapsed = (datetime.now() - start_time).total_seconds()
            rate = batch_num / elapsed if elapsed > 0 else 0
            remaining = (total_batches - batch_num) / rate if rate > 0 else 0
            print(f"  Progress: {batch_num}/{total_batches} batches ({batch_num*100//total_batches}%)")
            print(f"  Rate: {rate:.2f} batches/sec, ETA: {remaining/60:.1f} minutes")
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
    
    print()
    print("=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print()
    print(f"Total posts processed: {total_posts}")
    print(f"Successfully populated: {schedule['total_populated']}")
    print(f"Errors: {schedule['total_errors']}")
    print(f"Pending: {total_posts - schedule['total_populated'] - schedule['total_errors']}")
    print(f"Time elapsed: {elapsed_time/60:.1f} minutes")
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
        print("Format breakdown (populated):")
        for fmt, count in sorted(format_stats.items(), key=lambda x: x[1], reverse=True):
            pct = (count / schedule['total_populated']) * 100 if schedule['total_populated'] > 0 else 0
            print(f"  - {fmt}: {count} posts ({pct:.1f}%)")
        print()
    
    await populator.close()
    
    print("=" * 70)
    print("Generation complete! Review populated content in:")
    print(f"  {output_path}")
    print("=" * 70)
    print()
    print("Peace, Love, Unity.")


def start_server():
    """Start the FastAPI server"""
    print("=" * 70)
    print("STARTING BACKEND SERVICES")
    print("=" * 70)
    print()
    print("Starting FastAPI server on http://localhost:8000...")
    print("Server will run in background...")
    print()
    
    # Start server in background
    server_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd=Path(__file__).parent,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait a bit for server to start
    print("Waiting for server to start...")
    time.sleep(5)
    
    # Check if server is running
    import requests
    try:
        response = requests.get("http://localhost:8000/docs", timeout=2)
        if response.status_code == 200:
            print("[OK] Server is running at http://localhost:8000")
            print()
            return server_process
        else:
            print("[WARNING] Server may not be fully ready")
            return server_process
    except:
        print("[WARNING] Could not verify server status, but process started")
        print("Server may need more time to start...")
        return server_process


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run services and generate all content")
    parser.add_argument("--no-server", action="store_true", help="Don't start server, assume it's running")
    parser.add_argument("--server-only", action="store_true", help="Only start server, don't generate")
    
    args = parser.parse_args()
    
    server_process = None
    
    if not args.no_server:
        server_process = start_server()
        if args.server_only:
            print("Server started. Use Ctrl+C to stop.")
            try:
                server_process.wait()
            except KeyboardInterrupt:
                print("\nStopping server...")
                server_process.terminate()
            sys.exit(0)
    
    # Wait a bit more for services to be ready
    if not args.no_server:
        print("Waiting for services to be ready...")
        time.sleep(3)
        print()
    
    # Generate all content
    try:
        asyncio.run(generate_all_content())
    except KeyboardInterrupt:
        print("\n\nGeneration interrupted by user")
        if server_process:
            print("Stopping server...")
            server_process.terminate()
    except Exception as e:
        print(f"\n[ERROR] Generation failed: {str(e)}")
        if server_process:
            print("Stopping server...")
            server_process.terminate()
        sys.exit(1)
    finally:
        if server_process:
            print("\nStopping server...")
            server_process.terminate()
