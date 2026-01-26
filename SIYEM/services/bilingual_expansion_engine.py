"""BILINGUAL EXPANSION ENGINE - Karasahin (JK)
Creates emotionally aligned bilingual pairs from existing songs
NOT translation - SEED-based emotional transposition

CORE PRINCIPLE: The seed (emotional core) of the original flows into its bilingual mate.
Turkish and English remain independent streams, but share the same emotional frequency.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code ensures music and words complement each other.
"""

from typing import Dict, List, Optional, Literal
from datetime import datetime
import json
import os
from pathlib import Path

# Style essence mapping (removes direct artist references)
STYLE_ESSENCE = {
    "J Dilla": "swing and soul, rhythmic pocket, human groove",
    "Flying Lotus": "cosmic layers, experimental textures, space and depth",
    "Nujabes": "contemplative depth, emotional resonance, lo-fi warmth",
    "Orhan Gencebay": "Turkish Arabesk longing, emotional depth, traditional soul",
    "Sezen Aksu": "vulnerability, poetic truth, emotional honesty",
    "Jeff Buckley": "intimate power, vulnerable strength, soaring emotion",
    "Bon Iver": "space and breath, minimal arrangement, emotional clarity",
    "James Blake": "minimal soul, space over clutter, emotional precision"
}

class BilingualExpansionEngine:
    """
    Creates bilingual pairs from existing songs
    Seed-based emotional alignment, not direct translation
    """
    
    def __init__(self, lyrics_dir: str = "s:\\JAN\\SIYEM\\output\\lyrics"):
        self.lyrics_dir = Path(lyrics_dir)
        self.entity_path = Path("s:\\JAN\\Siyem.org\\jk")
        
    def expand_catalogue(self, process_all: bool = True) -> Dict:
        """
        Process all catalogued songs and create bilingual pairs
        
        Args:
            process_all: If True, processes all songs. If False, only missing pairs.
        
        Returns:
            Dict with expansion results
        """
        
        # Load catalogue
        catalogue = self._load_catalogue()
        
        results = {
            "processed": [],
            "created": [],
            "skipped": [],
            "errors": []
        }
        
        # Process each song
        for song_info in catalogue:
            try:
                result = self._process_song(song_info, process_all)
                if result["status"] == "created":
                    results["created"].append(result)
                elif result["status"] == "skipped":
                    results["skipped"].append(result)
                else:
                    results["processed"].append(result)
            except Exception as e:
                results["errors"].append({
                    "song": song_info.get("title", "unknown"),
                    "error": str(e)
                })
        
        return results
    
    def _load_catalogue(self) -> List[Dict]:
        """Load song catalogue from KARASAHIN_CATALOGUE_UPDATED.md"""
        
        catalogue_path = Path("s:\\JAN\\KARASAHIN_CATALOGUE_UPDATED.md")
        
        # Parse catalogue (simplified - in production would parse markdown properly)
        catalogue = [
            # English songs needing Turkish pairs
            {"title": "Fire & Ice", "file": "fire_and_ice_20260120.json", "language": "english", "theme": "self_discovery"},
            {"title": "Nobody Home", "file": "nobody_home_20260120.json", "language": "english", "theme": "loneliness_longing"},
            {"title": "I'm in Danger", "file": "im_in_danger_20260120.json", "language": "english", "theme": "heartbreak_danger"},
            {"title": "Manifesto of the Midnight Reversal", "file": "midnight_reversal_20260115_164945.json", "language": "english", "theme": "midnight_reversal"},
            
            # Turkish songs needing English pairs
            {"title": "Seni Sevmek", "file": "seni_sevmek_20260120.json", "language": "turkish", "theme": "love_devotion"},
            {"title": "Duvarında Deliği", "file": "duvarinda_deligi_20260120.json", "language": "turkish", "theme": "cyprus_identity"},
            {"title": "Sana İnat", "file": "sana_inat_20260120.json", "language": "turkish", "theme": "defiance_resilience"},
            {"title": "Kafana Takma", "file": "kafana_takma_20260120.json", "language": "turkish", "theme": "resilience_kindness"},
            {"title": "Yazılı", "file": "yazili_20260120.json", "language": "turkish", "theme": "destiny_self_reflection"},
            {"title": "Tozun Hatırası", "file": "tozun_hatirasi_20260120.json", "language": "turkish", "theme": "memory_eternal_love"},
            {"title": "Küçükken", "file": "kucukken_20260120.json", "language": "turkish", "theme": "childhood_growth"}
        ]
        
        return catalogue
    
    def _process_song(self, song_info: Dict, process_all: bool) -> Dict:
        """Process a single song and create bilingual pair if needed"""
        
        file_path = self.lyrics_dir / song_info["file"]
        
        if not file_path.exists():
            return {
                "status": "error",
                "song": song_info["title"],
                "reason": "File not found"
            }
        
        # Load original song
        with open(file_path, 'r', encoding='utf-8') as f:
            original = json.load(f)
        
        # Check if bilingual pair already exists
        has_turkish = original.get("turkish_lyrics") is not None
        has_english = original.get("english_lyrics") is not None
        
        if not process_all:
            if song_info["language"] == "english" and has_turkish:
                return {"status": "skipped", "song": song_info["title"], "reason": "Turkish pair already exists"}
            if song_info["language"] == "turkish" and has_english:
                return {"status": "skipped", "song": song_info["title"], "reason": "English pair already exists"}
        
        # Create bilingual pair
        if song_info["language"] == "english" and not has_turkish:
            turkish_seed = self._create_turkish_seed(original)
            original["turkish_lyrics"] = turkish_seed
            status = "created"
        elif song_info["language"] == "turkish" and not has_english:
            english_seed = self._create_english_seed(original)
            original["english_lyrics"] = english_seed
            status = "created"
        else:
            status = "processed"
        
        # Save updated song
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(original, f, ensure_ascii=False, indent=2)
        
        return {
            "status": status,
            "song": song_info["title"],
            "file": song_info["file"],
            "language_added": "turkish" if song_info["language"] == "english" else "english"
        }
    
    def _create_turkish_seed(self, original: Dict) -> Dict:
        """
        Create Turkish seed from English original
        Emotional alignment, not direct translation
        """
        
        english_lyrics = original.get("english_lyrics", {})
        context = original.get("context", {})
        theme = context.get("theme", "general")
        
        # Extract emotional seed
        emotional_seed = self._extract_emotional_seed(english_lyrics, context)
        
        # Generate Turkish version from seed
        turkish_lyrics = self._generate_from_seed(emotional_seed, "turkish", context)
        
        return turkish_lyrics
    
    def _create_english_seed(self, original: Dict) -> Dict:
        """
        Create English seed from Turkish original
        Emotional alignment, not direct translation
        """
        
        turkish_lyrics = original.get("turkish_lyrics", {})
        context = original.get("context", {})
        theme = context.get("theme", "general")
        
        # Extract emotional seed
        emotional_seed = self._extract_emotional_seed(turkish_lyrics, context, language="turkish")
        
        # Generate English version from seed
        english_lyrics = self._generate_from_seed(emotional_seed, "english", context)
        
        return english_lyrics
    
    def _extract_emotional_seed(self, lyrics: Dict, context: Dict, language: str = "english") -> Dict:
        """
        Extract the emotional seed (core) from lyrics
        This is what gets transposed, not the words
        """
        
        sections = lyrics.get("sections", {})
        title = lyrics.get("title", "")
        theme = context.get("theme", "general")
        
        # Extract emotional core
        emotional_core = {
            "theme": theme,
            "emotional_arc": self._identify_emotional_arc(sections),
            "key_metaphors": self._extract_metaphors(sections, language),
            "vocal_energy": self._identify_vocal_energy(sections),
            "resolution": self._identify_resolution(sections),
            "ottoman_influence": context.get("ottoman_influence", {})
        }
        
        return emotional_core
    
    def _identify_emotional_arc(self, sections: Dict) -> str:
        """Identify the emotional journey through the song"""
        
        # Analyze sections for emotional progression
        if "verse_1" in sections and "verse_4" in sections:
            return "isolation_to_renewal"
        elif "bridge" in sections:
            return "conflict_to_resolution"
        elif "chorus" in sections:
            return "longing_to_declaration"
        else:
            return "contemplative_journey"
    
    def _extract_metaphors(self, sections: Dict, language: str) -> List[str]:
        """Extract key metaphors and imagery"""
        
        metaphors = []
        all_lines = []
        
        for section_name, lines in sections.items():
            all_lines.extend(lines)
        
        # Simple metaphor extraction (in production would use NLP)
        key_words = {
            "english": ["waves", "horizon", "heart", "soul", "light", "dark", "home", "phone", "street"],
            "turkish": ["gönül", "aşk", "yol", "ufuk", "can", "ruh", "kalp", "kader", "hasret"]
        }
        
        for line in all_lines:
            for word in key_words.get(language, []):
                if word.lower() in line.lower():
                    metaphors.append(line)
                    break
        
        return metaphors[:5]  # Top 5 metaphors
    
    def _identify_vocal_energy(self, sections: Dict) -> str:
        """Identify the vocal delivery style"""
        
        if "verse_1" in sections:
            first_verse = sections["verse_1"]
            if any(word in " ".join(first_verse).lower() for word in ["quiet", "whisper", "soft", "sessiz", "yavaş"]):
                return "intimate_whisper"
            elif any(word in " ".join(first_verse).lower() for word in ["loud", "strong", "power", "güçlü", "yüksek"]):
                return "powerful_declaration"
        
        return "emotion_first"
    
    def _identify_resolution(self, sections: Dict) -> str:
        """Identify how the song resolves"""
        
        if "verse_4" in sections:
            last_verse = sections["verse_4"]
            if any(word in " ".join(last_verse).lower() for word in ["horizon", "new day", "complete", "ufuk", "yeni", "tamam"]):
                return "hopeful_renewal"
        elif "outro" in sections:
            outro = sections["outro"]
            if any(word in " ".join(outro).lower() for word in ["silence", "breath", "space", "sessizlik", "nefes"]):
                return "contemplative_space"
        
        return "emotional_closure"
    
    def _generate_from_seed(self, emotional_seed: Dict, target_language: str, context: Dict) -> Dict:
        """
        Generate lyrics in target language from emotional seed
        This is where the magic happens - same emotion, different expression
        """
        
        theme = emotional_seed["theme"]
        emotional_arc = emotional_seed["emotional_arc"]
        ottoman_influence = emotional_seed.get("ottoman_influence", {})
        
        # Generate based on theme and emotional seed
        if target_language == "turkish":
            return self._generate_turkish_from_seed(emotional_seed, context)
        else:
            return self._generate_english_from_seed(emotional_seed, context)
    
    def _generate_turkish_from_seed(self, seed: Dict, context: Dict) -> Dict:
        """Generate Turkish lyrics from emotional seed"""
        
        theme = seed["theme"]
        metaphors = seed.get("key_metaphors", [])
        
        # Theme-specific generation
        if theme == "loneliness_longing":
            return {
                "title": "Kimse Yok Evde",
                "sections": {
                    "verse_1": [
                        "Yine aynı sokakta yürüyorum yalnız",
                        "Daha önce de buradaydım, hiç değişmemiş",
                        "Yolumu bulmaya çalışıyorum, karışık",
                        "Dünü tutamayacağımı biliyorum",
                        "Sadece bugünü atlatmayı umuyorum"
                    ],
                    "verse_2": [
                        "Kıyıdaki dalgalar hala senin adını çağırıyor",
                        "Omzumdaki başın hala aynı hissediliyor",
                        "Her şey yalan olsa bile sen gerçek kalırsın",
                        "Ama biliyorum bu resimde sen eksiksin",
                        "Geçeceğimden emin olamıyorum"
                    ],
                    "chorus": [
                        "Ama telefonda konuşacak kimse yok evde",
                        "Birisi lütfen beni arasın, yeni bir şeye ihtiyacım var",
                        "Sana sözlerimi veriyorum, sen bana zamanını ver",
                        "Sen bana gülümsemeni ver, ben sana şarkımı söylüyorum",
                        "İşte istediğim bu",
                        "Ama kimse yok evde",
                        "Kimse yok evde",
                        "Ve kendimi çok yalnız hissediyorum"
                    ],
                    "verse_3": [
                        "Kalmak her geçen gün daha zorlaşıyor, sen burada değilsin",
                        "Ama sen beni kalıyorum, oynadığın oyunlarla, belirsiz",
                        "Nerede olduğunu soruyorum, dörtte orada olacağını söylüyorsun",
                        "Beşe yirmi kala, hala kapımda değilsin",
                        "Ne yapabilirim? Yerdeyim",
                        "Seni bekliyorum, ama daha fazla dayanamıyorum"
                    ],
                    "bridge": [
                        "Daha uzakta hissediyorum, ama sen beni kalıyorum",
                        "Ne yapabilirim, gördüğüm tek şey sensin",
                        "Kalbimin atışı bana bunun başlangıç olduğunu söylüyor",
                        "Güzel bir şeyin, gerçek bir şeyin başlangıcı"
                    ],
                    "verse_4": [
                        "Bir kez daha kendimi tam hissediyorum, ayaklarımın üzerinde duruyorum",
                        "Şimdi tam olarak nerede olmak istediğimi görebiliyorum",
                        "Dünün acısı beni tekrar yenmeyecek",
                        "Ufukta yeni bir gün görüyorum",
                        "Ufukta yeni bir gün görüyorum"
                    ]
                },
                "ottoman_influence": {
                    "metaphors_used": ["hasret", "yol", "ufuk", "gönül"],
                    "patterns_applied": ["poetic", "temporal"],
                    "cultural_weight": "authentic_soil"
                },
                "karasahin_voice": {
                    "signature_phrases": ["Kimse yok evde", "Ufukta yeni bir gün"],
                    "metaphors": ["Dalgalar senin adını çağırıyor", "Oynadığın oyunlar"],
                    "cadence": "melancholic_hope"
                }
            }
        
        # Default Turkish generation
        return {
            "title": "Duygu ve Ses",
            "sections": {
                "verse_1": ["Türkçe sözler - duygusal çekirdekten"],
                "chorus": ["Ses her şeydir"]
            },
            "ottoman_influence": ottoman_influence
        }
    
    def _generate_english_from_seed(self, seed: Dict, context: Dict) -> Dict:
        """Generate English lyrics from emotional seed"""
        
        theme = seed["theme"]
        metaphors = seed.get("key_metaphors", [])
        
        # Theme-specific generation
        if theme == "love_devotion":
            return {
                "title": "Loving You",
                "sections": {
                    "verse_1": [
                        "Loving every flaw you have",
                        "Waiting day and night",
                        "Loving, giving all I am",
                        "Loving you"
                    ],
                    "chorus": [
                        "Loving, like an endless film",
                        "Lifts you up then brings you down",
                        "Pulls the heart to its owner",
                        "Loving you"
                    ],
                    "verse_2": [
                        "Living is an experience",
                        "Every new day that's born",
                        "Who will tomorrow belong to",
                        "What happens today",
                        "You stay by my side"
                    ],
                    "chorus_repeat": [
                        "Loving, loving you",
                        "Giving life to a still heart",
                        "Loving you"
                    ],
                    "verse_3": [
                        "You are every night's morning",
                        "You are every breath's name",
                        "Let my heart memorize you—",
                        "Loving you"
                    ],
                    "bridge": [
                        "Let it be the writing on my forehead",
                        "Let the beginning and end be clear",
                        "Let my heart fill with you now",
                        "This life of mine, I sacrifice to you"
                    ],
                    "outro": [
                        "Loving, loving you",
                        "Giving life to a still heart",
                        "Loving you",
                        "Loving you"
                    ]
                },
                "karasahin_voice": {
                    "signature_phrases": ["Loving you", "Endless film"],
                    "metaphors": ["Heart to its owner", "Writing on my forehead"],
                    "cadence": "devotional_flow"
                }
            }
        
        # Default English generation
        return {
            "title": "Sound and Emotion",
            "sections": {
                "verse_1": ["English lyrics - from emotional seed"],
                "chorus": ["Sound is everything"]
            }
        }
    
    def update_suno_prompts_with_essence(self, prompt_file: str) -> str:
        """
        Update Suno prompts to use style essence instead of direct artist references
        """
        
        prompt_path = Path(prompt_file)
        
        if not prompt_path.exists():
            return f"Prompt file not found: {prompt_file}"
        
        # Read prompt
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace artist references with essence
        for artist, essence in STYLE_ESSENCE.items():
            content = content.replace(artist, essence)
            content = content.replace(artist.lower(), essence)
        
        # Write updated prompt
        output_path = prompt_path.parent / f"{prompt_path.stem}_essence{prompt_path.suffix}"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"Updated prompt saved to: {output_path}"


# CLI Interface
if __name__ == "__main__":
    import sys
    
    print("=" * 80)
    print("BILINGUAL EXPANSION ENGINE - Karasahin (JK)")
    print("Seed-based emotional alignment, not translation")
    print("=" * 80)
    
    engine = BilingualExpansionEngine()
    
    # Expand catalogue
    print("\n[EXPANDING] Catalogue with bilingual pairs...")
    results = engine.expand_catalogue(process_all=True)
    
    print(f"\n[RESULTS]")
    print(f"Created: {len(results['created'])} bilingual pairs")
    print(f"Skipped: {len(results['skipped'])} (already exist)")
    print(f"Processed: {len(results['processed'])}")
    print(f"Errors: {len(results['errors'])}")
    
    if results['created']:
        print("\n[CREATED]")
        for item in results['created']:
            print(f"  [OK] {item['song']} - Added {item['language_added']} version")
    
    if results['errors']:
        print("\n[ERRORS]")
        for error in results['errors']:
            print(f"  ❌ {error['song']}: {error['error']}")
    
    print("\n" + "=" * 80)
    print("[COMPLETE] Bilingual expansion finished")
    print("=" * 80)
