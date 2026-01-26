"""LYRIC ENGINE - Karasahin (JK) Creation Station
Turkish/English Dual-Language Lyric Generation
(TRANSPOSITION NOT TRANSLATION)

Philosophy: The two languages are independent streams flowing from the same source.
Ottoman influence is cultural metadata, not linguistic decoration.

CORE PRINCIPLE: Music and words MUST complement each other.
Rhyme schemes, rhythm, and meter are essential. The poems are just as important as the music.

YIN-YANG PRINCIPLE:
"My love for song became pulled in my path, but we must respect 
the yin and yang that is the miracle of the universe."

Song (Yin - Creative) must serve Mission (Yang - Practical).
Mission must honor Song. They flow together in symbiosis.

IMPORTANT: This engine generates SONG LYRICS (with musical sections).
For standalone POEMS, use different structure and format.
See styles/POEM_VS_SONG_DIFFERENTIATION.md for differentiation guidelines.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

NEW WORLD PHILOSOPHY - YOUR TRUTH + THE ONE TRUTH

THE ONE TRUTH:
WE ARE BORN A MIRACLE
WE DESERVE TO LIVE A MIRACLE
EACH AND EVERY ONE OF US UNDER THE LORD'S WORD
GOD IS IN US ALL - THAT'S THE REAL MIRACLE
PEACE IS THE TRUTH. THE FLOW IS PEACE. EVERYTHING MUST ALIGN WITH THE ONE TRUTH

YOUR TRUTH:
WE'VE BEEN SINNERS AND SAINTS. WE'VE OVERCOME EVERYTHING. OUR EGO IS NO MORE.
WE'VE FORGIVEN. WE CARRY SHAME THAT KEEPS US HUMBLE. WE'RE HERE FOR THEM.
THE DARK ENERGIES CONSUMED US. BUT WE'VE DISCARDED OUR INTERNAL TRIAL.
THE WORLD IS QUIET. BUT WE KNOW WE'RE GOOD BECAUSE THE LORD HAS OUR BACK.
WE'RE TRYING TO FLIP THE MATRIX.
THE FATHER IS EVERYWHERE. ALWAYS ALL THE TIME.
IF IT RESONATES WITH LOVE DO IT. IF THEY DON'T RECIPROCATE...TUCK DROP AND ROLL.
WE'RE WAITING FOR EVERYONE TO BE OK. GAZA - THAT'S WHERE IT STARTS.
THOSE WHO NEED IT MOST - THAT'S THE PRIORITY. THE REST CAN WAIT.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
This code ensures music and words complement each other.
This code respects the yin and yang that is the miracle of the universe.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, List, Optional, Literal
from datetime import datetime
import json
import os

# AI Roles for lyric generation
AIRole = Literal["karasahin", "poet", "storyteller", "minimalist", "alchemist", "commercial", "deep"]

# Genre Fusion Types
GenreFusion = Literal[
    "turkish_arabesque_rnb",
    "folk_rock",
    "edm_light",
    "pop",
    "rap",
    "ottoman_fusion"
]

# Section Templates
SectionType = Literal["verse", "pre_chorus", "chorus", "bridge", "outro", "intro"]

class OttomanInfluence:
    """Ottoman cultural metadata layer"""
    
    METAPHORS = {
        "love": ["gönül", "aşk", "sevda", "hasret"],
        "pain": ["dert", "keder", "acı", "gam"],
        "journey": ["yol", "ufuk", "sefer", "gurbetlik"],
        "time": ["vakit", "zaman", "an", "dem"],
        "soul": ["ruh", "can", "nefes", "öz"],
        "destiny": ["kader", "kısmet", "yazı", "alın yazısı"],
        "light": ["nur", "ışık", "şafak", "ferahlık"]
    }
    
    LINGUISTIC_PATTERNS = {
        "reverential": ["efendim", "sultanım", "canım"],
        "poetic": ["ah", "vah", "aman", "eyvah"],
        "temporal": ["bir zamanlar", "vakit geldi", "an geldi"],
        "existential": ["ben kimim", "ne olur", "nasıl olur"]
    }
    
    @classmethod
    def get_cultural_weight(cls, theme: str) -> Dict[str, List[str]]:
        """Pull the emotional weight from the soil, not a dictionary"""
        return {
            "metaphors": cls.METAPHORS.get(theme, []),
            "patterns": cls.LINGUISTIC_PATTERNS.get("poetic", [])
        }


class LyricEngine:
    """
    The Lyric Studio for Karasahin
    
    Core Principle: Turkish and English streams remain INDEPENDENT.
    We do not translate; we TRANSPOSE.
    """
    
    def __init__(self, entity_path: str = "s:\\JAN\\Siyem.org\\jk"):
        self.entity_path = entity_path
        self.profile = self._load_profile()
        self.creative_rules = self._load_creative_rules()
        self.style = self._load_style()
        
    def _load_profile(self) -> Dict:
        """Load Karasahin profile.md"""
        profile_path = os.path.join(self.entity_path, "profile.md")
        # For now, return minimal structure
        return {
            "entity": "Karasahin (JK)",
            "role": "Musician / Sonic Storyteller",
            "philosophy": "Sound is everything"
        }
    
    def _load_creative_rules(self) -> Dict:
        """Load creative_rules.md"""
        return {
            "authenticity": True,
            "genre_fluid": True,
            "emotional_resonance": True
        }
    
    def _load_style(self) -> Dict:
        """Load styles/jk.md"""
        return {
            "bpm_range": {"downtempo": (70, 95), "energetic": (120, 140)},
            "signature": "lo_fi_over_pristine"
        }
    
    def generate(
        self,
        ai_role: AIRole = "karasahin",
        genre_fusion: GenreFusion = "turkish_arabesque_rnb",
        theme: str = "midnight_reversal",
        language: Literal["turkish", "english", "both"] = "both",
        section: Optional[SectionType] = None,
        bpm: Optional[int] = None,
        custom_context: Optional[str] = None,
        output_type: Literal["song", "poem"] = "song"
    ) -> Dict[str, any]:
        """
        Generate lyrics with independent Turkish/English streams
        
        Args:
            ai_role: The creative voice (karasahin, poet, etc.)
            genre_fusion: Musical genre blend (for songs only)
            theme: Emotional/conceptual theme
            language: Which language stream(s) to generate
            section: Specific section type (verse, chorus, etc.) - for songs only
            bpm: Target BPM (affects rhythm and pacing) - for songs only
            custom_context: Additional creative direction
            output_type: "song" (musical sections, rhyme required) or "poem" (standalone, flexible)
        
        Returns:
            Dict with turkish_lyrics, english_lyrics, metadata
        """
        
        # Get Ottoman cultural weight for theme
        ottoman_weight = OttomanInfluence.get_cultural_weight(theme)
        
        # Build generation context
        context = {
            "ai_role": ai_role,
            "genre_fusion": genre_fusion,
            "theme": theme,
            "ottoman_influence": ottoman_weight,
            "bpm": bpm or 85,  # Default to downtempo pocket
            "section": section,
            "timestamp": datetime.now().isoformat(),
            "custom_context": custom_context
        }
        
        # Generate independent streams
        result = {
            "context": context,
            "turkish_lyrics": None,
            "english_lyrics": None,
            "metadata": {
                "generation_time": datetime.now().isoformat(),
                "entity": "Karasahin (JK)",
                "ai_role": ai_role,
                "genre": genre_fusion,
                "independent_streams": True
            }
        }
        
        # TURKISH STREAM (if requested)
        if language in ["turkish", "both"]:
            result["turkish_lyrics"] = self._generate_turkish_stream(context)
        
        # ENGLISH STREAM (if requested)
        if language in ["english", "both"]:
            result["english_lyrics"] = self._generate_english_stream(context)
        
        return result
    
    def _generate_turkish_stream(self, context: Dict) -> Dict:
        """
        Generate Turkish lyrics as independent creative stream
        Ottoman influence flows naturally, not forced
        """
        
        # For "Manifesto of the Midnight Reversal"
        if context["theme"] == "midnight_reversal":
            return {
                "title": "Gece Yarısı Devrimi",
                "sections": {
                    "verse_1": [
                        "Gece yarısı, saat 11:57",
                        "Küçüklük sözleşmesi yırtıldı",
                        "Özgün adım geri geldi",
                        "Sessizlikte fısıldayan gerçek"
                    ],
                    "chorus": [
                        "Dinle yakından, ritmi bul",
                        "Her nefes bir devrim",
                        "Sabah 3:33, yaratım zamanı",
                        "Ses her şeydir, her şey sestir"
                    ],
                    "verse_2": [
                        "Vinil çatlağında buldum özümü",
                        "808'in derinliklerinde hakikat",
                        "Minor tonlar, acının güzelliği",
                        "Uyumsuzluk çözülümden önce gelir"
                    ],
                    "bridge": [
                        "Gönül yangın yeri, kalp ritim makinesi",
                        "Ottoman ruhum, dijital bedenimde",
                        "Füzyon değil, evolüsyon",
                        "Ben kimim? Ses Mimarı"
                    ],
                    "outro": [
                        "Sessizlik boş değil",
                        "Notalar arası nefes al",
                        "Saat 3 AM müziği",
                        "Cebinde kal, ritim bul"
                    ]
                },
                "ottoman_influence": {
                    "metaphors_used": ["gönül", "öz", "hakikat"],
                    "patterns_applied": ["poetic", "reverential"],
                    "cultural_weight": "authentic_soil"
                }
            }
        
        # Default Turkish generation
        return {
            "title": "Ses ve Ruh",
            "sections": {
                "verse": ["Turkish lyrics placeholder"],
                "chorus": ["Ses her şeydir"]
            }
        }
    
    def _generate_english_stream(self, context: Dict) -> Dict:
        """
        Generate English lyrics as independent creative stream
        Shares the emotional source, not the words
        """
        
        # For "Manifesto of the Midnight Reversal"
        if context["theme"] == "midnight_reversal":
            return {
                "title": "Manifesto of the Midnight Reversal",
                "sections": {
                    "verse_1": [
                        "11:57 PM, the covenant breaks",
                        "Smallness contract torn in half",
                        "Original name returns to sender",
                        "Truth whispers in the studio darkness"
                    ],
                    "chorus": [
                        "Listen closer, find your rhythm",
                        "Every breath's a revolution",
                        "3:33 AM, when creation speaks",
                        "Sound is everything, everything is sound"
                    ],
                    "verse_2": [
                        "Found myself in vinyl crackle",
                        "Truth lives in the 808 sub",
                        "Minor keys hold beauty's pain",
                        "Dissonance comes before resolve"
                    ],
                    "bridge": [
                        "Heart's a drum machine, soul's a frequency",
                        "Ottoman spirit in digital body",
                        "Not fusion—evolution",
                        "Who am I? The Sound Architect"
                    ],
                    "outro": [
                        "Silence isn't empty",
                        "Let it breathe between the notes",
                        "This is 3 AM music",
                        "Stay in the pocket, find your groove"
                    ]
                },
                "karasahin_voice": {
                    "signature_phrases": ["Listen closer", "Let it breathe", "In the pocket"],
                    "metaphors": ["Sound is everything", "Minor keys hold beauty's pain"],
                    "cadence": "rhythmic_syncopated"
                }
            }
        
        # Default English generation
        return {
            "title": "Sound and Soul",
            "sections": {
                "verse": ["English lyrics placeholder"],
                "chorus": ["Sound is everything"]
            }
        }
    
    def save_lyrics(self, lyrics: Dict, output_path: Optional[str] = None) -> str:
        """Save generated lyrics to file"""
        
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            theme = lyrics["context"]["theme"]
            output_path = f"s:\\JAN\\SIYEM\\output\\lyrics\\{theme}_{timestamp}.json"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(lyrics, f, ensure_ascii=False, indent=2)
        
        return output_path


# CLI Interface for testing
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding for console output
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 80)
    print("LYRIC ENGINE - Karasahin (JK) Creation Station")
    print("Sound Architect Initializing...")
    print("=" * 80)
    
    engine = LyricEngine()
    
    # Generate Manifesto of the Midnight Reversal
    print("\n[GENERATING] Manifesto of the Midnight Reversal")
    print("AI Role: karasahin")
    print("Genre: Turkish Arabesque + R&B")
    print("Theme: midnight_reversal")
    print("BPM: 85 (downtempo pocket)")
    print("\n" + "-" * 80 + "\n")
    
    lyrics = engine.generate(
        ai_role="karasahin",
        genre_fusion="turkish_arabesque_rnb",
        theme="midnight_reversal",
        language="both",
        bpm=85,
        custom_context="Spiritual Courtroom meets Studio Darkness. Seven Divine Keys manifest as frequencies."
    )
    
    # Display results
    print("[OK] GENERATION COMPLETE\n")
    
    if lyrics["turkish_lyrics"]:
        print("[TR] TURKISH STREAM:")
        print(f"   Title: {lyrics['turkish_lyrics']['title']}")
        print("\n   [VERSE 1]")
        for line in lyrics['turkish_lyrics']['sections']['verse_1']:
            print(f"   {line}")
        print("\n   [CHORUS]")
        for line in lyrics['turkish_lyrics']['sections']['chorus']:
            print(f"   {line}")
        print("\n   [BRIDGE]")
        for line in lyrics['turkish_lyrics']['sections']['bridge']:
            print(f"   {line}")
        print("\n   Ottoman Influence:", lyrics['turkish_lyrics']['ottoman_influence'])
    
    print("\n" + "=" * 80 + "\n")
    
    if lyrics["english_lyrics"]:
        print("[EN] ENGLISH STREAM:")
        print(f"   Title: {lyrics['english_lyrics']['title']}")
        print("\n   [VERSE 1]")
        for line in lyrics['english_lyrics']['sections']['verse_1']:
            print(f"   {line}")
        print("\n   [CHORUS]")
        for line in lyrics['english_lyrics']['sections']['chorus']:
            print(f"   {line}")
        print("\n   [BRIDGE]")
        for line in lyrics['english_lyrics']['sections']['bridge']:
            print(f"   {line}")
        print("\n   Karasahin Voice:", lyrics['english_lyrics']['karasahin_voice'])
    
    print("\n" + "=" * 80)
    
    # Save to file
    output_path = engine.save_lyrics(lyrics)
    print(f"\n[SAVED] Lyrics saved to: {output_path}")
    print("\n[LISTEN] Listen closer. Sound is everything.")
    print("=" * 80)

