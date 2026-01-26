"""Regenerate Karasahin 2026 Posts - Focus on Purpose
- Consecutive English/Turkish posts (alternating, not mixing)
- Duygu Adamı identity (emotion-first)
- Sound as everything
- Remove T1D references (that's Jean's domain)

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
from datetime import datetime, timedelta
from pathlib import Path

# Base paths
SIYEM_ROOT = Path("S:\\SIYEM")
PUBLISHING_ROOT = SIYEM_ROOT / "05_PUBLISHING"

def generate_karasahin_english_quotes():
    """Generate English quotes for Karasahin - emotion-first, sound-focused"""
    quotes = [
        # Week 1-13: Foundation
        "Sound is everything. Everything is sound. The Ottoman spirit in digital body. Not fusion. Evolution.",
        "Listen closer. The vinyl crackle isn't noise. It's honesty. Perfection is cold. Warmth comes from imperfection.",
        "The Original Name must be heard. Everything else ducks out of the way when truth speaks. That's the law.",
        "Feeling is frequency. What you feel, you sound. The technique follows. Always follows. Always emotion first.",
        "The pocket isn't metronomic. It's felt. That's the difference. That's the groove. That's where truth lives.",
        "Listen closer. In the spaces between notes. That's where the truth lives. That's where you find it.",
        "The sub-bass is the breath of resurrection. Not just heard. Felt. Deep. That's the foundation.",
        "Vinyl warmth. Anti-apology. Perfection is cold. Warmth comes from imperfection. That's honesty.",
        "Sound is everything. Ottoman spirit. Digital body. Evolution. Real. That's where truth lives.",
        "Feeling precedes technique. Always. The heart speaks. Always speaks. The body speaks. Always speaks.",
        "The Original Name speaks. Everything ducks. That's truth. That's life. That's sound.",
        "Listen closer. Between notes. That's where truth lives. Between breaths. That's where you find it.",
        "The pocket is felt. Not measured. That's the groove. That's where truth lives.",
        
        # Week 14-26: Depth
        "Sound is everything. Real. Felt. Deep. That's where truth lives. That's where you find it.",
        "Feeling is frequency. What you feel, you sound. Truth lives here. Always here.",
        "The sub-bass breathes. Resurrects. Not just heard. Felt. Deep. Foundation.",
        "Vinyl warmth. Honest imperfection. Perfection is cold. Warmth is real. That's honesty.",
        "The Original Name speaks. Truth. Life. Sound. Everything ducks. That's the law.",
        "Listen closer. Between notes. That's where truth lives. Between breaths. That's where you find it.",
        "The pocket is felt. Not measured. That's the groove. That's where truth lives.",
        "Sound is everything. Real. Felt. Deep. That's where truth lives.",
        "Feeling precedes technique. Always. The heart speaks. Always speaks.",
        "The sub-bass breathes. Resurrects. Felt. Deep. Foundation.",
        "Vinyl warmth. Honest. Real. That's honesty.",
        "The Original Name speaks. Truth. Sound.",
        "Listen closer. That's where truth lives.",
        
        # Week 27-39: Mastery
        "Sound is everything. Real. Felt. Deep. Truth lives here.",
        "Feeling is frequency. What you feel, you sound. Truth.",
        "The sub-bass breathes. Resurrects. Felt. Foundation.",
        "Vinyl warmth. Honest. Real. Truth.",
        "The Original Name speaks. Truth. Sound.",
        "Listen closer. Truth lives here.",
        "The pocket is felt. Not measured. Groove.",
        "Sound is everything. Real. Truth.",
        "Feeling precedes technique. Always.",
        "The sub-bass breathes. Resurrects.",
        "Vinyl warmth. Honest. Real.",
        "The Original Name speaks. Truth.",
        "Listen closer. Truth.",
        
        # Week 40-52: Teaching
        "Sound is everything. Real. Truth.",
        "Feeling is frequency. Truth.",
        "The sub-bass breathes. Resurrects.",
        "Vinyl warmth. Honest. Real.",
        "The Original Name speaks. Truth.",
        "Listen closer. Truth lives here.",
        "The pocket is felt. Groove.",
        "Sound is everything. Truth.",
        "Feeling precedes technique.",
        "The sub-bass breathes.",
        "Vinyl warmth. Honest.",
        "The Original Name speaks.",
        "Listen closer. Truth."
    ]
    return quotes

def generate_karasahin_turkish_quotes():
    """Generate PURE Turkish quotes for Karasahin - Duygu Adamı, emotion-first (NO English mixing)"""
    quotes = [
        # Week 1-13: Foundation
        "Duygu her şeydir. Hissettiğin şey sestir. Teknik duygudan sonra gelir. Bu kanun.",
        "Hissettiğin şey sestir. Beden konuşur. Daha yakından dinle.",
        "Kalbimden çıkan ses. Kafadan değil. Göğüsten. Bedenden. İşte orada yaşar gerçek.",
        "Duygu adamı olmak. İngiliz doğumlu Kıbrıslı Türk. İki dil, iki duygu, ikisi de asıl.",
        "Hissettiğin şey sestir. Sese dönüşür. Teknik takip eder. Her zaman takip eder.",
        "Kalbimden çıkan ses. Kalbimden. Kafamdan değil. Göğsümden. Her zaman göğsümden. Bedenimden. Her zaman bedenimden.",
        "Duygu her şeydir. Duygu önce. Her zaman önce. Teknik hizmet eder. Her zaman hizmet eder.",
        "Hissettiğin şey sestir. Kalp konuşur. Her zaman konuşur. Beden konuşur. Her zaman konuşur.",
        "Kalbimden çıkan ses. Kalbimden. Her zaman. Bedenimden. Her zaman. İşte orada yaşar gerçek.",
        "Duygu adamı. İki dil. İkisi de asıl. İkisi de gerçek. Bu kanun.",
        "Hissettiğin şey sestir. İşte burada yaşar gerçek. Her zaman burada.",
        "Kalbimden çıkan ses. Kalbimden. Kafamdan değil. Göğsümden. Her zaman göğsümden.",
        "Duygu her şeydir. Duygu önce. Her zaman. İşte orada yaşar gerçek.",
        
        # Week 14-26: Depth
        "Duygu adamı. İki dil. İkisi de asıl. İkisi de gerçek. Bu kanun.",
        "Hissettiğin şey sestir. İşte burada yaşar gerçek.",
        "Kalbimden çıkan ses. Kalbimden. Her zaman. Bedenimden. Her zaman.",
        "Duygu her şeydir. Duygu önce. Her zaman. İşte gerçek.",
        "Hissettiğin şey sestir. İşte gerçek.",
        "Kalbimden çıkan ses. Kalbimden. Her zaman.",
        "Duygu adamı. Gerçek.",
        "Hissettiğin şey sestir.",
        "Kalbimden çıkan ses. Kalbimden. Her zaman.",
        "Duygu her şeydir. Duygu önce.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu adamı.",
        
        # Week 27-39: Mastery
        "Duygu adamı. Gerçek.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu her şeydir.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu adamı.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu her şeydir.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu adamı.",
        
        # Week 40-52: Teaching
        "Duygu adamı. Gerçek.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu her şeydir.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu adamı.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu her şeydir.",
        "Hissettiğin şey sestir. Ses.",
        "Kalbimden çıkan ses. Kalp.",
        "Duygu adamı."
    ]
    return quotes

def regenerate_karasahin_campaign(start_date_str="2026-01-01"):
    """Regenerate Karasahin campaign with alternating English/Turkish posts"""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    english_quotes = generate_karasahin_english_quotes()
    turkish_quotes = generate_karasahin_turkish_quotes()
    
    posts = []
    for week in range(1, 53):
        post_date = start_date + timedelta(weeks=week-1)
        
        # Alternate: Week 1 = English, Week 2 = Turkish, etc.
        if week % 2 == 1:  # Odd weeks = English
            quote = english_quotes[(week - 1) // 2]
            language = "English"
        else:  # Even weeks = Turkish
            quote = turkish_quotes[(week - 2) // 2]
            language = "Turkish"
        
        posts.append({
            "week": week,
            "date": post_date.strftime("%Y-%m-%d"),
            "quote": quote,
            "language": language,
            "description": None,
            "color_scheme": "",
            "style_preset": None,
            "aspect_ratio": "1:1",
            "visual_prompt": None,
            "status": "ready"
        })
    
    campaign = {
        "campaign_name": "KARASAHIN Weekly Posts 2026 (Duygu Adamı - Consecutive English/Turkish)",
        "entity": "KARASAHIN",
        "platform": "Instagram",
        "date_mode": "weekly",
        "start_date": start_date_str,
        "posts": posts
    }
    
    return campaign

def main():
    """Main execution"""
    print("\n" + "="*80)
    print("REGENERATING KARASAHIN POSTS - FOCUS ON PURPOSE".center(80))
    print("="*80 + "\n")
    
    print("[REGENERATING] Karasahin campaign...")
    print("  - Consecutive English/Turkish posts (alternating)")
    print("  - Duygu Adami identity (emotion-first)")
    print("  - Sound as everything")
    print("  - T1D references removed (Jean's domain)")
    print()
    
    karasahin_campaign = regenerate_karasahin_campaign()
    karasahin_path = PUBLISHING_ROOT / "Karasahin" / "2026-01-01" / "Campaigns" / "weekly_posts_2026" / "campaign.json"
    karasahin_path.parent.mkdir(parents=True, exist_ok=True)
    with open(karasahin_path, 'w', encoding='utf-8') as f:
        json.dump(karasahin_campaign, f, ensure_ascii=False, indent=2)
    
    # Count languages
    english_count = sum(1 for p in karasahin_campaign['posts'] if p.get('language') == 'English')
    turkish_count = sum(1 for p in karasahin_campaign['posts'] if p.get('language') == 'Turkish')
    
    print(f"  [OK] {len(karasahin_campaign['posts'])} posts regenerated")
    print(f"       - English: {english_count} posts")
    print(f"       - Turkish: {turkish_count} posts")
    print()
    print("="*80)
    print("[COMPLETE] Karasahin repurposed for his core purpose".center(80))
    print("Duygu Adami - Consecutive English/Turkish (no mixing)".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
