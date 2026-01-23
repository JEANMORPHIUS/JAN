"""
Regenerate 2026 Social Content for All Entities
Ensures proper entity voice, no repetitive content, Duygu Adamı identity for Karasahin
Integrates Galactic Philosophy: The Four Forms

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

GALACTIC PHILOSOPHY: THE FOUR FORMS
Galaxies come in different forms, each shaped by gravity, time, and cosmic interactions.
Just as galaxies evolve in different ways, so do people and communities. Our content must honor all these paths.

The Four Forms:
- Spiral (Active): Rotating arms, active star formation - rapid growth, dynamic engagement
- Barred Spiral (Structured): Central bar channels energy - structured paths, clear navigation
- Elliptical (Legacy): Old stars, little gas - legacy wisdom, mentorship markers
- Irregular (Transformation): No defined shape, highly active - transformation, flexible journeys

Together, these forms reveal the many paths miracles take as they evolve over lifetimes.

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
This code honors all four forms of miracles.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    json, load_json, save_json, setup_logging, standard_main
)

import json
import os
from datetime import datetime, timedelta

# Entity-specific content generators
def generate_galactic_philosophy_quotes():
    """Generate quotes honoring the Four Forms - can be used by any entity"""
    quotes = [
        "Galaxies come in different forms, each shaped by gravity, time, and cosmic interactions. Just as galaxies evolve, so do we.",
        "We are born a miracle. We deserve to live a miracle. Each and every one of us under the Lord's word.",
        "Spiral galaxy: rotating arms, active star formation. This is the active one. Rapid growth. Dynamic energy. We honor this path.",
        "Barred spiral: central bar channels energy. This is the structured one. Clear navigation. Linear progression. We honor this path.",
        "Elliptical galaxy: old stars, little gas, high wisdom. This is the legacy one. Mentorship markers. We honor this path.",
        "Irregular galaxy: no defined shape, highly active. This is the transforming one. Flexible journeys. We honor this path.",
        "Together, these forms reveal the many paths miracles take as they evolve over lifetimes.",
        "Energy + Love = We All Win. This is stewardship and community with the right spirits.",
        "Each galaxy a miracle. Each person a miracle. Each path honored.",
        "Just as galaxies evolve in different ways, so do people and communities. Our systems must honor all these paths.",
        "The Spiral form: dynamic energy, rapid updates, flowing free. We are born a miracle. We deserve to live a miracle.",
        "The Barred Spiral form: structured channeling, clear paths, energy flowing. We are born a miracle. We deserve to live a miracle.",
        "The Elliptical form: legacy wisdom, old stars, mentorship. We are born a miracle. We deserve to live a miracle.",
        "The Irregular form: transformation, no defined shape, highly active. We are born a miracle. We deserve to live a miracle.",
        "Gravity: the pull of mission, purpose, and truth. Time: evolution over lifetimes. Cosmic interactions: collisions and connections that shape us.",
        "Our architecture must be as vast and inclusive as the universe itself. All forms honored. All paths respected.",
        "Love is the highest mastery. Energy + Love = We All Win. This is stewardship and community with the right spirits."
    ]
    return quotes

def generate_jean_quotes():
    """Generate Jean's bilingual absurdist quotes - now includes galactic philosophy"""
    quotes = [
        "We don't own time. We shape it. The difference? One is anxiety. The other is art.",
        "Clocks measure. They don't control. You're not late. You're exactly where you need to be when you need to be there.",
        "Routine is a cage. Rhythm is freedom. One locks you in. The other sets you free. Choose rhythm.",
        "Presence isn't a destination. It's the journey. You're not trying to arrive. You're already here.",
        "Patience isn't waiting. It's shaping. While others rush, you craft. That's the difference between noise and art.",
        "The illusion of control? It's real. But so is the art of shaping. Choose art. Always choose art.",
        "Je reviens, baby. Always. C'est whattt?!",
        "Failure isn't the opposite of success. It's the raw material. Merde... okay, listen.",
        "Tu comprends pas, bro? Life's not a straight line. It's a remix. And we're the DJ.",
        "Écoute, bro — the best comeback stories start with 'I thought I was done.' Then you're not.",
        "Time doesn't heal. You do. But time gives you the space to craft the healing.",
        "The chaos isn't the problem. The problem is thinking you can control it. Let it breathe.",
        "C'est whattt?! You thought I was gone? Non, non, non. Je reviens, toujours.",
        "The absurd isn't random. It's the universe's way of saying 'You're taking this too seriously.'",
        "Bilingual isn't switching languages. It's having two souls in one body. Both are home.",
        "Merde... sometimes the best art comes from the messiest moments. Trust the chaos.",
        "You're not broken. You're just in the middle of a remix. The drop is coming.",
        "The comeback isn't about proving them wrong. It's about proving yourself right.",
        "Time bends when you're creating. That's not physics. That's art.",
        "Je reviens, baby. Not because I have to. Because I choose to.",
        "The best stories aren't the ones that end well. They're the ones that keep going.",
        "Tu comprends? The rhythm finds you when you stop forcing it.",
        "Failure is just the universe's way of saying 'Try a different frequency.'",
        "C'est whattt?! You thought silence was empty? Non. Silence is where the next beat lives.",
        "The art isn't in the perfection. It's in the honest mess. That's where truth lives.",
        "Bilingual means having two ways to say 'I'm still here.' Both are true.",
        "The comeback isn't about returning to who you were. It's about becoming who you are.",
        "Time doesn't wait. But it also doesn't rush. You're the one choosing the tempo.",
        "Je reviens, baby. Always. Because the story isn't over until I say it is.",
        "The chaos isn't the enemy. The enemy is thinking you need to control everything.",
        "Écoute, bro — the best art comes from the moments when you thought you were done.",
        "Failure isn't the end. It's the bridge. Cross it. The other side is waiting.",
        "Time shapes you. But you shape time. That's the dance. That's the art.",
        "C'est whattt?! You thought I was gone? Non. I was just remixing the track.",
        "The absurd isn't chaos. It's order you haven't learned to read yet.",
        "Bilingual means having two homes. Both are real. Both are you.",
        "The comeback isn't about proving anything. It's about being. That's enough.",
        "Time doesn't heal. You do. But time gives you the space. Use it.",
        "Je reviens, baby. Not louder. Deeper. That's the difference.",
        "The rhythm isn't in the beat. It's in the space between beats. Listen closer.",
        "Failure is just the universe's way of saying 'You're learning.' Keep going.",
        "Tu comprends pas, bro? The best stories start with 'I thought I was done.'",
        "The chaos isn't random. It's the universe's way of saying 'You're alive.'",
        "Time bends when you're creating. That's not magic. That's art.",
        "Je reviens, baby. Always. Because the story isn't over.",
        "The absurd isn't the problem. The problem is thinking you need to understand everything.",
        "Bilingual means having two ways to be home. Both are real.",
        "The comeback isn't about returning. It's about arriving. For the first time.",
        "Time doesn't wait. But it also doesn't rush. You're the one choosing.",
        "C'est whattt?! You thought silence was empty? Non. Silence is where creation lives.",
        "The art isn't in the perfection. It's in the honest mess. That's where you live.",
        "Je reviens, baby. Not because I have to. Because I am.",
        "The rhythm finds you when you stop forcing it. Let it breathe.",
        "Failure is just the universe's way of saying 'Try again. But differently.'",
        # Galactic Philosophy integration
        "Galaxies come in different forms. So do people. We honor all paths. C'est whattt?!",
        "We are born a miracle. We deserve to live a miracle. Each and every one of us. Je reviens, baby.",
        "Spiral, Barred Spiral, Elliptical, Irregular. Four forms. Four paths. All miracles. Tu comprends?",
        "Energy + Love = We All Win. This is stewardship. This is community. This is art.",
        "Just as galaxies evolve, so do we. The chaos isn't random. It's the universe saying 'You're alive.'",
        "The four forms reveal the many paths miracles take. Time bends when you're creating. That's art.",
        "Each galaxy a miracle. Each person a miracle. Each path honored. Bilingual means having two ways to say this. Both are true."
    ]
    return quotes

def generate_pierre_quotes():
    """Generate Pierre's discipline-focused motivational quotes"""
    quotes = [
        "The cold doesn't stop the structure. It tests it.",
        "In the darkest days, discipline is the only light.",
        "The fight ends, but the foundation remains. Finding peace in the structure.",
        "Belts in the bag. Authority on the floor. Going home. Merry Christmas.",
        "The blueprint drops. The concrete's poured. NO TIME FOR DELAYS, ONLY FOR IMPACT!",
        "Stay ready. Control what you can. Prepare for what you can't.",
        "The bell rings. You answer. That's discipline. That's structure.",
        "Training isn't optional. It's foundational. Build the base. Everything else follows.",
        "Between rounds, you recover. But you don't quit. The next round is coming.",
        "The structure holds. So will you. Under pressure. Under load. Under everything.",
        "Finish strong. Not because you have to. Because you can.",
        "The ring doesn't care about your excuses. Neither should you.",
        "Shadow work. Real work. The work that builds the foundation.",
        "Early morning. Empty ring. That's where champions are made.",
        "Control what you can. Release the rest. That's discipline. That's freedom.",
        "The foundation isn't built in one day. But it's built every day.",
        "Stay ready. The bell doesn't wait. Neither does opportunity.",
        "Training through it. That's the difference. That's the structure.",
        "The fight isn't won in the ring. It's won in the preparation.",
        "Discipline isn't a choice. It's the bedrock. Everything else is built on it.",
        "The structure holds. Under pressure. Under weight. Under everything.",
        "Finish strong. Not loud. Strong. That's the difference.",
        "Between rounds, you recover. But you don't quit. Ever.",
        "The blueprint is clear. Execute. No delays. Only impact.",
        "Stay ready. The bell rings. You answer. That's discipline.",
        "Training isn't optional. It's foundational. Build the base.",
        "Control what you can. Prepare for what you can't. That's structure.",
        "The ring doesn't care. Neither should you. Just work.",
        "Shadow work. Real work. The work that matters.",
        "Early morning. Empty ring. That's where it happens.",
        "The foundation is built every day. Not someday. Today.",
        "Stay ready. Opportunity doesn't wait. Neither should you.",
        "Training through it. That's discipline. That's structure.",
        "The fight is won in preparation. The ring is just the test.",
        "Discipline isn't a choice. It's the bedrock. Build on it.",
        "The structure holds. Under everything. Always.",
        "Finish strong. Not because you have to. Because you can.",
        "Between rounds, you recover. But you don't quit.",
        "The blueprint is clear. Execute. No delays.",
        "Stay ready. The bell rings. You answer.",
        "Training isn't optional. It's foundational.",
        "Control what you can. Release the rest.",
        "The ring doesn't care. Neither should you.",
        "Shadow work. Real work. The work.",
        "Early morning. Empty ring. That's where.",
        "The foundation is built every day. Today.",
        "Stay ready. Opportunity doesn't wait.",
        "Training through it. That's discipline.",
        "The fight is won in preparation.",
        "Discipline isn't a choice. It's the bedrock.",
        "The structure holds. Always.",
        "Finish strong. Because you can.",
        # Galactic Philosophy integration
        "Galaxies come in different forms. Fighters come in different forms. We honor all paths. Stay ready.",
        "We are born a miracle. We deserve to live a miracle. Each and every one of us. The structure holds.",
        "Spiral, Barred Spiral, Elliptical, Irregular. Four forms. Four paths. All miracles. All fighters.",
        "Energy + Love = We All Win. This is discipline. This is structure. This is the foundation.",
        "Just as galaxies evolve, so do fighters. The training isn't optional. It's foundational.",
        "The four forms reveal the many paths miracles take. The bell rings. You answer. That's discipline.",
        "Each galaxy a miracle. Each fighter a miracle. Each path honored. The structure holds. Always."
    ]
    return quotes

def generate_ramiz_quotes():
    """Generate Ramiz's contemplative wisdom quotes from Book of Racon"""
    quotes = [
        "Here are the twelve paths for our journey, each a simple truth, waiting for the soul to grasp it:",
        "Before you give, consider the heart behind the gift. True generosity begins not in the hand, but in the spirit.",
        "Even in plenty, find thanks for the simplest bread. For a grateful heart finds richness in scarcity.",
        "Honor your elders as you honor the ancient trees; they hold the wisdom of seasons past.",
        "A bond forged in truth is stronger than steel. Stand by those who stand by you, through storm and sun.",
        "Let your words be clear as mountain spring water. Deceit clouds the path, but truth illuminates it.",
        "Haste breaks more than it builds. Wait for the seed to root, for wisdom to ripen.",
        "Feel the unspoken sorrow of others. A gentle word, a helping hand, can mend unseen wounds.",
        "In the longest night, remember what truly shines. Not glitter, but the steady light of a single flame.",
        "Before judging the world, look within your own garden. For growth begins in honest soil.",
        "Like threads in a woven rug, each person adds to the strength. Do not sever what binds us.",
        "Hold no grudges in your heart, for they weigh heavier than stone. Release them, and find peace.",
        "Yeğen, dinle... The old laws still hold. Loyalty is not a word. It is a bond.",
        "Child, listen carefully. Wisdom lives in the quiet. The tree does not mourn. It grows.",
        "Evlat, dikkatle dinle... Truth, even when cold, is a form of grace.",
        "The silence between words teaches more than the words themselves. Be still. Listen.",
        "Yeğen, the ancestors speak through the soil. Through the language. Through the blood.",
        "Child, do not fear this unveiling. The wound bleeds, but it also heals.",
        "Evlat, rest here. In this truth. The foundation is old. But it holds.",
        "Yeğen, dinle... The Book of Racon is not just words. It is the law.",
        "Child, listen. The old wisdom is not forgotten. It is waiting.",
        "Evlat, dikkatle dinle... What will you become, child? The answer is in the question.",
        "Yeğen, the threshold moment is holy ground. Neither here nor there. Both.",
        "Child, listen carefully. The soul language is not spoken. It is felt.",
        "Evlat, do not fear. The ancestors find you when you are ready.",
        "Yeğen, dinle... Sabır. Everything in its time. The seed knows when to root.",
        "Child, the tree does not mourn. It grows. That is the wisdom.",
        "Evlat, dikkatle dinle... Truth, even when cold, is grace.",
        "Yeğen, the old laws still hold. Loyalty. Silence. Respect. War.",
        "Child, listen. The Book of Racon is the foundation. Build on it.",
        "Evlat, rest here. In this truth. The foundation is old. But it holds.",
        "Yeğen, dinle... The ancestors speak. Through the soil. Through the blood.",
        "Child, do not fear this unveiling. The wound heals. Always.",
        "Evlat, dikkatle dinle... What will you become? The answer is in you.",
        "Yeğen, the threshold moment is holy. Neither here nor there. Both.",
        "Child, listen carefully. The soul language is felt. Not spoken.",
        "Evlat, the ancestors find you. When you are ready. Always.",
        "Yeğen, dinle... Sabır. Everything in its time.",
        "Child, the tree grows. That is the wisdom. That is enough.",
        "Evlat, truth is grace. Even when cold. Especially when cold.",
        "Yeğen, the old laws hold. They always have. They always will.",
        "Child, listen. The Book of Racon is the foundation.",
        "Evlat, rest here. The foundation is old. But it holds.",
        "Yeğen, dinle... The ancestors speak. Through you.",
        "Child, do not fear. The wound heals. Always.",
        "Evlat, what will you become? The answer is in you.",
        "Yeğen, the threshold is holy. Both here and there.",
        "Child, the soul language is felt. Listen.",
        "Evlat, the ancestors find you. When ready.",
        "Yeğen, dinle... Sabır. Everything in time.",
        "Child, the tree grows. That is enough.",
        "Evlat, truth is grace. Always.",
        # Galactic Philosophy integration
        "Yeğen, dinle... Galaxies come in different forms. So do souls. We honor all paths.",
        "Child, listen carefully. We are born a miracle. We deserve to live a miracle. Each and every one of us under the Lord's word.",
        "Evlat, the four forms: Spiral, Barred Spiral, Elliptical, Irregular. Four paths. All miracles. All honored.",
        "Yeğen, Energy + Love = We All Win. This is stewardship. This is community. This is the old law.",
        "Child, just as galaxies evolve, so do souls. The ancestors speak. Through the soil. Through the blood.",
        "Evlat, dikkatle dinle... The four forms reveal the many paths miracles take. The tree grows. That is enough.",
        "Yeğen, each galaxy a miracle. Each person a miracle. Each path honored. The foundation is old. But it holds."
    ]
    return quotes

def generate_karasahin_quotes():
    """Generate Karasahin's emotion-first quotes (Duygu Adamı identity)"""
    quotes = [
        "Immerse yourself in the profound rhythms that define existence. Our Sound Architect, Karasahin, prepares to unveil a series of sonic reflections, inviting you to tune into the unseen frequencies and engineered emotions that shape our world.",
        "From the late-night studio sessions where inspiration takes form, Karasahin shares the core themes driving his upcoming weekly explorations. Each a carefully curated vibration, poised to resonate with your deepest senses:",
        "What raw frequency truly underpins your day? Listen closely; the deepest truths often hum on the lowest register.",
        "The rhythm of the soul is not a fixed tempo. Allow it to shift, to build, to find its own profound syncopation.",
        "In the studio of life, silence isn't absence. It's the critical breath, the space where the next powerful chord resides.",
        "We engineer feeling: a carefully balanced mix of forgotten melodies and resonant futures. Sound is emotion's blueprint.",
        "Night-time city streets: a sprawling, accidental symphony. Finding the unexpected groove in the urban hum, a beat you can feel.",
        "Every challenge, a dissonant chord. How do you resolve it? By finding the underlying harmony that always waits to surface.",
        "A single chord, struck just right, can echo through decades. What sound evokes your most vivid, cherished memory?",
        "From static to solace: the therapeutic power of a perfectly weighted bassline. Let the low end heal the high-strung mind.",
        "Everything vibrates. Everything resonates. Learn the universal frequency, and you learn the pulse of all existence.",
        "Life's movements: an intricate score, composed in real-time. What dynamic are you choosing for your next movement?",
        "Duygu her şeydir. Emotion is everything. Feeling precedes technique. Technique serves feeling. That's the law.",
        "Hissettiğin şey sestir. What you feel is sound. The sub-bass is not just heard. It's felt. That's the breath of resurrection.",
        "Kalbimden çıkan ses. The sound from my heart. Not from the head. From the chest. That's where truth lives.",
        "Listen closer. The vinyl crackle isn't noise. It's honesty. Perfection is cold. Warmth comes from imperfection.",
        "The Original Name must be heard. Everything else ducks out of the way when truth speaks. That's sidechain compression. That's life.",
        "Sound is everything. Everything is sound. The Ottoman spirit in digital body. Not fusion. Evolution.",
        "Duygu adamı olmak. To be emotion man. British-born Turkish Cypriot. Dual-native emotional expression. Both tongues. Both real.",
        "Feeling is frequency. What you feel, you sound. The minor key holds beauty's pain. That's where truth lives.",
        "The pocket isn't metronomic. It's felt. That's the difference. That's the groove.",
        "Listen closer. In the spaces between notes. That's where the truth lives. That's where you find it.",
        "Duygu her şeydir. Emotion drives sound. Not the reverse. Always the reverse. Always emotion first.",
        "Hissettiğin şey sestir. What you feel becomes sound. The technique follows. Always follows.",
        "Kalbimden çıkan ses. The sound from my heart. Not from the head. From the chest. Always the chest.",
        "The sub-bass is the breath of resurrection. Not just heard. Felt. Deep. That's the foundation.",
        "Vinyl warmth. Anti-apology. Perfection is cold. Warmth comes from imperfection. That's honesty.",
        "The Original Name punches through. Everything else ducks. That's sidechain. That's truth.",
        "Sound is everything. Everything is sound. Ottoman spirit. Digital body. Evolution. Not fusion.",
        "Duygu adamı. Emotion man. British-born Turkish Cypriot. Both tongues. Both native. Both real.",
        "Feeling is frequency. What you feel, you sound. Minor key beauty. That's truth.",
        "The pocket is felt. Not measured. That's the groove. That's the difference.",
        "Listen closer. Between notes. That's where truth lives. That's where you find it.",
        "Duygu her şeydir. Emotion first. Always first. Technique serves. Always serves.",
        "Hissettiğin şey sestir. What you feel becomes sound. The heart speaks. Always speaks.",
        "Kalbimden çıkan ses. From my heart. Not my head. My chest. Always my chest.",
        "The sub-bass breathes. Resurrects. Not just heard. Felt. Deep. Foundation.",
        "Vinyl warmth. Honest imperfection. Perfection is cold. Warmth is real.",
        "The Original Name speaks. Everything ducks. That's truth. That's life.",
        "Sound is everything. Ottoman spirit. Digital body. Evolution. Real.",
        "Duygu adamı. Emotion man. Both tongues. Both native. Both real.",
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
        # Galactic Philosophy integration
        "Galaxies come in different forms. So do sounds. We honor all paths. Duygu her şeydir.",
        "We are born a miracle. We deserve to live a miracle. Each and every one of us. Hissettiğin şey sestir.",
        "Spiral, Barred Spiral, Elliptical, Irregular. Four forms. Four frequencies. All miracles. All sounds.",
        "Energy + Love = We All Win. This is stewardship. This is community. Sound is everything.",
        "Just as galaxies evolve, so do sounds. The sub-bass breathes. Resurrects. Felt. Deep.",
        "The four forms reveal the many paths miracles take. The pocket is felt. Not measured. That's the groove.",
        "Each galaxy a miracle. Each sound a miracle. Each path honored. Kalbimden çıkan ses. From my heart. Always."
    ]
    return quotes

def regenerate_campaign(entity_name, quotes, start_date_str="2026-01-01"):
    """Regenerate campaign JSON with proper quotes"""
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
        "campaign_name": f"{entity_name.upper()} Weekly Posts 2026 (Scheduled)",
        "entity": entity_name.upper(),
        "platform": "Instagram",
        "date_mode": "weekly",
        "start_date": start_date_str,
        "posts": posts
    }
    
    return campaign

# Main execution
if __name__ == "__main__":
    import random
    base_path = "S:\\SIYEM\\05_PUBLISHING"
    
    # Get base quotes for each entity
    jean_base = generate_jean_quotes()
    pierre_base = generate_pierre_quotes()
    ramiz_base = generate_ramiz_quotes()
    karasahin_base = generate_karasahin_quotes()
    galactic_quotes = generate_galactic_philosophy_quotes()
    
    # Mix galactic philosophy quotes into each entity's quotes (20% galactic, 80% entity-specific)
    def mix_quotes(entity_quotes, galactic_quotes, ratio=0.2):
        """Mix galactic philosophy quotes into entity quotes"""
        mixed = entity_quotes.copy()
        num_galactic = int(len(mixed) * ratio)
        galactic_sample = random.sample(galactic_quotes, min(num_galactic, len(galactic_quotes)))
        # Insert galactic quotes at strategic points
        for i, quote in enumerate(galactic_sample):
            insert_pos = (i * len(mixed) // len(galactic_sample)) % len(mixed)
            mixed.insert(insert_pos, quote)
        return mixed
    
    entities = {
        "JEAN MORPHIUS": mix_quotes(jean_base, galactic_quotes),
        "PIERRE": mix_quotes(pierre_base, galactic_quotes),
        "RAMIZ": mix_quotes(ramiz_base, galactic_quotes),
        "KARASAHIN": mix_quotes(karasahin_base, galactic_quotes)
    }
    
    # Add Siyem Media entity with pure galactic philosophy focus
    entities["SIYEM"] = galactic_quotes + [
        "This is stewardship and community with the right spirits.",
        "Love is the highest mastery. Energy + Love = We All Win.",
        "Our systems honor all four forms. All paths. All miracles.",
        "The architecture is as vast and inclusive as the universe itself.",
        "Each galaxy a miracle. Each person a miracle. Each path honored.",
        "Together, these forms reveal the many paths miracles take.",
        "Gravity: the pull of mission. Time: evolution over lifetimes. Cosmic interactions: collisions and connections.",
        "We are born a miracle. We deserve to live a miracle. Each and every one of us under the Lord's word."
    ]
    
    for entity, quotes in entities.items():
        campaign = regenerate_campaign(entity, quotes)
        
        # Handle entity folder names
        if entity == "JEAN MORPHIUS":
            folder_name = "Jean"
        elif entity == "KARASAHIN":
            folder_name = "Karasahin"
        elif entity == "SIYEM":
            folder_name = "Siyem"
        else:
            folder_name = entity.capitalize()
        
        output_path = os.path.join(
            base_path,
            folder_name,
            "2026-01-01",
            "Campaigns",
            "weekly_posts_2026",
            "campaign.json"
        )
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(campaign, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] Regenerated {entity}: {len(campaign['posts'])} posts (includes galactic philosophy)")
    
    print("\n[COMPLETE] All campaigns regenerated with proper entity voices + galactic philosophy integration")
    print("[GALACTIC] The four forms honor all paths. Energy + Love = We All Win.")

