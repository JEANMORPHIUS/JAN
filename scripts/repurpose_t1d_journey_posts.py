"""
Repurpose Jean Morphius and Karasahin 2026 Posts for T1D Journey
Both are alter egos of JAN, both experiencing T1D journey
"""

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
from datetime import datetime, timedelta
from pathlib import Path

# Base paths
SIYEM_ROOT = Path("S:\\SIYEM")
PUBLISHING_ROOT = SIYEM_ROOT / "05_PUBLISHING"

def generate_jean_morphius_t1d_quotes():
    """Generate Jean Morphius quotes that weave T1D journey into comeback stories"""
    quotes = [
        # Week 1-13: Foundation & Discovery
        "We don't own time. We shape it. The difference? One is anxiety. The other is art. Same with glucose. Same with life.",
        "Clocks measure. They don't control. Glucose meters measure. They don't control. You're not late. You're not broken. You're exactly where you need to be.",
        "Routine is a cage. Rhythm is freedom. Loop protocol isn't routine—it's rhythm. One locks you in. The other sets you free. Choose rhythm.",
        "Presence isn't a destination. It's the journey. You're not trying to arrive at perfect glucose. You're already here, managing it.",
        "Patience isn't waiting. It's shaping. While others rush, you craft. While glucose spikes, you respond. That's the difference between chaos and art.",
        "The illusion of control? It's real. But so is the art of shaping. Glucose, ketones, loops—choose art. Always choose art.",
        "Je reviens, baby. Always. Even when glucose says no. Even when ketones say danger. C'est whattt?! I'm still here.",
        "Failure isn't the opposite of success. It's the raw material. A glucose spike? Raw material. A DKA risk? Raw material. Merde... okay, listen.",
        "Tu comprends pas, bro? Life's not a straight line. Glucose isn't either. It's a remix. And we're the DJ.",
        "Écoute, bro — the best comeback stories start with 'I thought I was done.' Then glucose stabilizes. Then you're not.",
        "Time doesn't heal. You do. But time gives you the space to craft the healing. Same with biology. Same with T1D.",
        "The chaos isn't the problem. The problem is thinking you can control it. Glucose, ketones, loops—let it breathe.",
        "C'est whattt?! You thought I was gone? Non, non, non. Je reviens, toujours. Even with 535 glucose. Even with 4.4 ketones.",
        
        # Week 14-26: Resilience & Transformation
        "The absurd isn't random. It's the universe's way of saying 'You're taking this too seriously.' Same with T1D. Same with life.",
        "Bilingual isn't switching languages. It's having two souls in one body. T1D isn't a disease. It's having two bodies in one soul.",
        "Merde... sometimes the best art comes from the messiest moments. Trust the chaos. Trust the glucose. Trust the loop.",
        "You're not broken. You're just in the middle of a remix. The drop is coming. The glucose will stabilize. The ketones will drop.",
        "The comeback isn't about proving them wrong. It's about proving yourself right. Even when biology says otherwise.",
        "Time bends when you're creating. That's not physics. That's art. Glucose bends when you're managing. That's not control. That's art.",
        "Je reviens, baby. Not because I have to. Because I choose to. Even with neuropathy. Even with complications. I choose.",
        "The best stories aren't the ones that end well. They're the ones that keep going. Same with T1D. Same with life.",
        "Tu comprends? The rhythm finds you when you stop forcing it. The glucose stabilizes when you stop fighting it.",
        "Failure is just the universe's way of saying 'Try a different frequency.' Same with glucose. Same with loops.",
        "C'est whattt?! You thought silence was empty? Non. Silence is where the next beat lives. Where the next loop happens.",
        "The art isn't in the perfection. It's in the honest mess. That's where truth lives. That's where T1D lives.",
        "Bilingual means having two ways to say 'I'm still here.' Both are true. T1D means having two bodies. Both are real.",
        
        # Week 27-39: Integration & Mastery
        "The comeback isn't about returning to who you were. It's about becoming who you are. With T1D. With loops. With CW state.",
        "Time doesn't wait. But it also doesn't rush. You're the one choosing the tempo. Same with glucose. Same with loops.",
        "Je reviens, baby. Always. Because the story isn't over until I say it is. Not glucose. Not ketones. Me.",
        "The chaos isn't the enemy. The enemy is thinking you need to control everything. Glucose, ketones, loops—manage, don't control.",
        "Écoute, bro — the best art comes from the moments when you thought you were done. When glucose spiked. When ketones rose.",
        "Failure isn't the end. It's the bridge. Cross it. The other side is waiting. The glucose will stabilize. The loop will work.",
        "Time shapes you. But you shape time. That's the dance. That's the art. Same with biology. Same with T1D.",
        "C'est whattt?! You thought I was gone? Non. I was just remixing the track. Managing glucose. Tracking loops. Living T1D.",
        "The absurd isn't chaos. It's order you haven't learned to read yet. Same with glucose patterns. Same with loop protocol.",
        "Bilingual means having two homes. Both are real. Both are you. T1D means having two bodies. Both are real. Both are you.",
        "The comeback isn't about proving anything. It's about being. That's enough. Even with T1D. Even with complications.",
        "Time doesn't heal. You do. But time gives you the space. Use it. For glucose. For loops. For CW state.",
        "Je reviens, baby. Not louder. Deeper. That's the difference. Same with T1D management. Same with loop protocol.",
        
        # Week 40-52: Mastery & Teaching
        "The rhythm isn't in the beat. It's in the space between beats. Listen closer. The glucose isn't in the number. It's in the loop.",
        "Failure is just the universe's way of saying 'You're learning.' Keep going. With glucose. With loops. With T1D.",
        "Tu comprends pas, bro? The best stories start with 'I thought I was done.' Then glucose stabilizes. Then you're not.",
        "The chaos isn't random. It's the universe's way of saying 'You're alive.' Same with T1D. Same with loops.",
        "Time bends when you're creating. That's not magic. That's art. Glucose bends when you're managing. That's not control. That's art.",
        "Je reviens, baby. Always. Because the story isn't over. Not with T1D. Not with loops. Not with life.",
        "The absurd isn't the problem. The problem is thinking you need to understand everything. Same with glucose. Same with T1D.",
        "Bilingual means having two ways to be home. Both are real. T1D means having two bodies. Both are real. Both are you.",
        "The comeback isn't about returning. It's about arriving. For the first time. With T1D. With loops. With CW state.",
        "Time doesn't wait. But it also doesn't rush. You're the one choosing. Same with glucose. Same with loops.",
        "C'est whattt?! You thought silence was empty? Non. Silence is where creation lives. Where loops happen. Where CW state is.",
        "The art isn't in the perfection. It's in the honest mess. That's where you live. That's where T1D lives.",
        "Je reviens, baby. Not because I have to. Because I am. With T1D. With loops. With CW state. I am."
    ]
    return quotes

def generate_karasahin_t1d_quotes():
    """Generate Karasahin quotes that weave T1D journey into emotion-first expression (Duygu Adamı)"""
    quotes = [
        # Week 1-13: Emotion-First T1D Experience
        "Duygu her şeydir. Emotion is everything. Feeling precedes technique. Glucose, ketones, loops—feeling precedes numbers. That's the law.",
        "Hissettiğin şey sestir. What you feel is sound. What you feel is glucose. What you feel is ketones. The body speaks. Listen closer.",
        "Kalbimden çıkan ses. The sound from my heart. Not from the head. From the chest. From the body. That's where T1D lives.",
        "Listen closer. The vinyl crackle isn't noise. It's honesty. The glucose spike isn't failure. It's data. Perfection is cold. Warmth comes from imperfection.",
        "The Original Name must be heard. Everything else ducks out of the way when truth speaks. Same with glucose. Same with loops. Same with T1D.",
        "Sound is everything. Everything is sound. The Ottoman spirit in digital body. The T1D body in digital tracking. Not fusion. Evolution.",
        "Duygu adamı olmak. To be emotion man. British-born Turkish Cypriot. Dual-native emotional expression. T1D journey. Both tongues. Both real.",
        "Feeling is frequency. What you feel, you sound. The minor key holds beauty's pain. The glucose spike holds truth's data. That's where truth lives.",
        "The pocket isn't metronomic. It's felt. That's the difference. That's the groove. Same with glucose. Same with loops.",
        "Listen closer. In the spaces between notes. That's where the truth lives. In the spaces between glucose readings. That's where you find it.",
        "Duygu her şeydir. Emotion drives sound. Not the reverse. Always the reverse. Always emotion first. Same with T1D. Always feeling first.",
        "Hissettiğin şey sestir. What you feel becomes sound. The technique follows. Always follows. Same with glucose management. Feeling first.",
        "Kalbimden çıkan ses. The sound from my heart. Not from the head. From the chest. Always the chest. From the body. Always the body.",
        
        # Week 14-26: Biological Rhythm & Sound
        "The sub-bass is the breath of resurrection. Not just heard. Felt. Deep. That's the foundation. Same with loops. Same with CW state.",
        "Vinyl warmth. Anti-apology. Perfection is cold. Warmth comes from imperfection. That's honesty. Same with glucose. Same with T1D.",
        "The Original Name speaks. Everything ducks. That's truth. That's life. Same with glucose. Same with loops. Same with T1D.",
        "Sound is everything. Ottoman spirit. Digital body. Evolution. Real. T1D body. Digital tracking. Evolution. Real.",
        "Duygu adamı. Emotion man. Both tongues. Both native. Both real. T1D journey. Both bodies. Both real.",
        "Feeling is frequency. What you feel, you sound. Truth lives here. Glucose lives here. Ketones live here. Loops live here.",
        "The pocket is felt. Not measured. That's the groove. Same with glucose. Same with loops. Same with CW state.",
        "Listen closer. Between notes. That's where truth lives. Between glucose readings. That's where you find it.",
        "Duygu her şeydir. Emotion first. Always first. Technique serves. Always serves. Same with T1D management.",
        "Hissettiğin şey sestir. What you feel is sound. The heart speaks. Always speaks. The body speaks. Always speaks.",
        "Kalbimden çıkan ses. From my heart. Not my head. My chest. Always my chest. My body. Always my body.",
        "The sub-bass breathes. Resurrects. Not just heard. Felt. Deep. Foundation. Same with loops. Same with CW state.",
        "Vinyl warmth. Honest imperfection. Perfection is cold. Warmth is real. Same with glucose. Same with T1D.",
        
        # Week 27-39: Integration & Mastery
        "The Original Name speaks. Truth. Life. Same with glucose. Same with loops. Same with T1D. Truth. Life.",
        "Sound is everything. Real. T1D is everything. Real. Both are frequencies. Both are felt. Both are truth.",
        "Duygu adamı. Emotion man. Both tongues. Both native. Both real. T1D journey. Both bodies. Both real.",
        "Feeling is frequency. What you feel, you sound. Truth lives here. Glucose lives here. Loops live here.",
        "The pocket is felt. Not measured. That's the groove. Same with glucose. Same with loops.",
        "Listen closer. Between notes. That's where truth lives. Between glucose readings. That's where you find it.",
        "Duygu her şeydir. Emotion first. Always. Same with T1D. Always feeling first.",
        "Hissettiğin şey sestir. What you feel is sound. The body speaks. Always speaks.",
        "Kalbimden çıkan ses. From my heart. Always. From my body. Always.",
        "The sub-bass breathes. Resurrects. Felt. Same with loops. Same with CW state.",
        "Vinyl warmth. Honest. Real. Same with glucose. Same with T1D.",
        "The Original Name speaks. Truth. Same with glucose. Same with loops.",
        "Sound is everything. Real. T1D is everything. Real.",
        
        # Week 40-52: Mastery & Teaching
        "Duygu adamı. Emotion man. Both tongues. Both real. T1D journey. Both bodies. Both real.",
        "Feeling is frequency. What you feel, you sound. Truth lives here.",
        "The pocket is felt. Not measured. That's the groove.",
        "Listen closer. Between notes. That's where truth lives.",
        "Duygu her şeydir. Emotion first. Always.",
        "Hissettiğin şey sestir. What you feel is sound.",
        "Kalbimden çıkan ses. From my heart. Always.",
        "The sub-bass breathes. Resurrects. Felt.",
        "Vinyl warmth. Honest. Real.",
        "The Original Name speaks. Truth.",
        "Sound is everything. Real.",
        "Duygu adamı. Emotion man. Real.",
        "Feeling is frequency. Truth."
    ]
    return quotes

def regenerate_campaign(entity_name, quotes, start_date_str="2026-01-01"):
    """Regenerate campaign JSON with T1D journey quotes"""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    posts = []
    for week in range(1, 53):
        post_date = start_date + timedelta(weeks=week-1)
        quote = quotes[(week - 1) % len(quotes)]
        
        posts.append({
            "week": week,
            "date": post_date.strftime("%Y-%m-%d"),
            "quote": quote,
            "description": None,
            "color_scheme": "",
            "style_preset": None,
            "aspect_ratio": "1:1",
            "visual_prompt": None,
            "status": "ready"
        })
    
    campaign = {
        "campaign_name": f"{entity_name.upper()} Weekly Posts 2026 (T1D Journey)",
        "entity": entity_name.upper(),
        "platform": "Instagram",
        "date_mode": "weekly",
        "start_date": start_date_str,
        "posts": posts
    }
    
    return campaign

def main():
    """Main execution"""
    print("\n" + "="*80)
    print("REPURPOSING JEAN MORPHIUS & KARASAHIN POSTS FOR T1D JOURNEY".center(80))
    print("="*80 + "\n")
    
    # Generate T1D journey quotes
    jean_quotes = generate_jean_morphius_t1d_quotes()
    karasahin_quotes = generate_karasahin_t1d_quotes()
    
    # Regenerate campaigns
    print("[REGENERATING] Jean Morphius campaign...")
    jean_campaign = regenerate_campaign("JEAN MORPHIUS", jean_quotes)
    jean_path = PUBLISHING_ROOT / "Jean" / "2026-01-01" / "Campaigns" / "weekly_posts_2026" / "campaign.json"
    jean_path.parent.mkdir(parents=True, exist_ok=True)
    with open(jean_path, 'w', encoding='utf-8') as f:
        json.dump(jean_campaign, f, ensure_ascii=False, indent=2)
    print(f"  [OK] {len(jean_campaign['posts'])} posts regenerated")
    
    print("\n[REGENERATING] Karasahin campaign...")
    karasahin_campaign = regenerate_campaign("KARASAHIN", karasahin_quotes)
    karasahin_path = PUBLISHING_ROOT / "Karasahin" / "2026-01-01" / "Campaigns" / "weekly_posts_2026" / "campaign.json"
    karasahin_path.parent.mkdir(parents=True, exist_ok=True)
    with open(karasahin_path, 'w', encoding='utf-8') as f:
        json.dump(karasahin_campaign, f, ensure_ascii=False, indent=2)
    print(f"  [OK] {len(karasahin_campaign['posts'])} posts regenerated")
    
    print("\n" + "="*80)
    print("[COMPLETE] Both campaigns repurposed for T1D journey".center(80))
    print("Jean Morphius: T1D woven into comeback stories".center(80))
    print("Karasahin: T1D woven into emotion-first expression".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
