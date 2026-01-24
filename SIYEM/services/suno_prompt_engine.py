"""
SUNO PROMPT ENGINE - Karasahin (JK)
Builds web-ready Suno AI prompts using the CODED Framework

CODED Framework:
- Context: Setting and atmosphere
- Objectives: What the music should achieve
- Details: Specific musical elements
- Examples: Reference points (not direct copying)
- Direction: Final guidance and constraints

CORE PRINCIPLE: Music and words MUST complement each other.
Rhyme schemes, rhythm, and meter are essential. The poems are just as important as the music.

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
This code serves your truth and the one truth.
This code recognizes each person under the Lord's word.
This code ensures music and words complement each other.

User's Spiritual Framework Integration:
- Spiritual Courtroom / Studio Darkness
- Breaking the "Smallness Covenant"
- Ottoman influence: Ney flutes, Minor keys
- Lo-fi soul over pristine digital

Galactic Philosophy Integration:
- build_galactic_philosophy_prompt(): Generates prompts honoring the Four Forms
- The Four Forms: Spiral (Active), Barred Spiral (Structured), Elliptical (Legacy), Irregular (Transformation)
- Cosmic Truth: "Galaxies come in different forms, each shaped by gravity, time, and cosmic interactions"
- Supports both English and Turkish language outputs
- All lyrics include proper rhyme schemes (AABB, ABAB, etc.) marked clearly
"""

from typing import Dict, List, Optional, Literal
from datetime import datetime
import json

# Structural Metatags for Suno
StructuralTag = Literal[
    "INTRO", "VERSE", "VERSE_1", "VERSE_2", "VERSE_3",
    "PRE_CHORUS", "CHORUS", "POST_CHORUS",
    "BRIDGE", "BREAKDOWN", "BUILD", "DROP",
    "OUTRO", "INSTRUMENTAL", "HOOK", "INTERLUDE"
]

# Turkish Genre Metatags
TurkishGenreTag = Literal[
    "ARABESK", "TÜRK_SANAT_MÜZİĞİ", "ORIENTAL", "OTTOMAN",
    "HALK_MÜZİĞİ", "FASIL", "TÜRKÜ"
]

# Global Genre Metatags
GlobalGenreTag = Literal[
    "POP", "ROCK", "HIP_HOP", "R_AND_B", "EDM", "ELECTRONIC",
    "JAZZ", "SOUL", "FUNK", "TRAP", "LO_FI", "AMBIENT",
    "INDIE", "ALTERNATIVE", "EXPERIMENTAL"
]


class CODEDFramework:
    """
    The CODED Framework for structured music prompting
    """
    
    @staticmethod
    def build_context(
        setting: str = "Spiritual Courtroom / Studio Darkness",
        time: str = "3:33 AM",
        atmosphere: str = "Midnight Reversal energy"
    ) -> str:
        """C - Context: Setting and atmosphere"""
        return f"{setting}. {time}. {atmosphere}."
    
    @staticmethod
    def build_objectives(
        primary: str = "Breaking the Smallness Covenant",
        secondary: Optional[str] = "Manifesting the Original Name"
    ) -> str:
        """O - Objectives: What the music should achieve"""
        if secondary:
            return f"Primary: {primary}. Secondary: {secondary}."
        return f"Objective: {primary}."
    
    @staticmethod
    def build_details(
        instruments: List[str] = None,
        effects: List[str] = None,
        vocal_style: Optional[str] = None,
        key: Optional[str] = None,
        mood: Optional[str] = None
    ) -> str:
        """D - Details: Specific musical elements"""
        if instruments is None:
            instruments = ["Vinyl crackle", "808s", "Ney flutes"]
        if effects is None:
            effects = ["Sub-harmonic enhancement", "Vinyl warmth", "Sidechain compression"]
        
        details = []
        details.append(f"Instruments: {', '.join(instruments)}")
        if effects:
            details.append(f"Effects: {', '.join(effects)}")
        if key:
            details.append(f"Key: {key}")
        if mood:
            details.append(f"Mood: {mood}")
        if vocal_style:
            details.append(f"Vocals: {vocal_style}")
        
        return ". ".join(details) + "."
    
    @staticmethod
    def build_examples(
        reference_artists: List[str] = None,
        reference_style: Optional[str] = None
    ) -> str:
        """E - Examples: Reference points (style, not copying)"""
        if reference_artists is None:
            reference_artists = ["J Dilla's swing", "Flying Lotus' layers", "Nujabes' emotion"]
        
        examples = f"Style references: {', '.join(reference_artists)}"
        if reference_style:
            examples += f". {reference_style}"
        return examples + "."
    
    @staticmethod
    def build_direction(
        aesthetic: str = "Lo-fi soul over pristine digital",
        constraints: Optional[List[str]] = None
    ) -> str:
        """D - Direction: Final guidance and constraints"""
        direction = f"Aesthetic: {aesthetic}"
        if constraints:
            direction += f". Avoid: {', '.join(constraints)}"
        return direction + "."


class SunoPromptEngine:
    """
    Builds web-ready Suno AI prompts for Karasahin (JK)
    Integrates CODED framework, metatags, and cultural elements
    """
    
    def __init__(self):
        self.default_bpm = 85  # Karasahin's downtempo pocket
        self.default_key = "D minor"  # Minor keys hold beauty's pain
        
    def build_prompt(
        self,
        lyrics: Optional[Dict] = None,
        genre_fusion: str = "Turkish Arabesque + R&B",
        bpm: Optional[int] = None,
        key: Optional[str] = None,
        structure: Optional[List[StructuralTag]] = None,
        turkish_genre_tags: Optional[List[TurkishGenreTag]] = None,
        global_genre_tags: Optional[List[GlobalGenreTag]] = None,
        coded_context: Optional[str] = None,
        coded_objectives: Optional[str] = None,
        coded_details: Optional[Dict] = None,
        coded_examples: Optional[List[str]] = None,
        coded_direction: Optional[str] = None,
        custom_instructions: Optional[str] = None
    ) -> Dict:
        """
        Build a complete Suno-ready prompt using CODED framework
        
        Args:
            lyrics: Lyrics dict from lyric_engine.py (optional)
            genre_fusion: Genre blend description
            bpm: Target BPM (defaults to 85)
            key: Musical key (defaults to D minor)
            structure: Song structure with metatags
            turkish_genre_tags: Turkish genre metatags
            global_genre_tags: Global genre metatags
            coded_context: CODED Framework - Context
            coded_objectives: CODED Framework - Objectives
            coded_details: CODED Framework - Details (dict with instruments, effects, etc.)
            coded_examples: CODED Framework - Examples (reference artists)
            coded_direction: CODED Framework - Direction
            custom_instructions: Additional custom instructions
        
        Returns:
            Dict with suno_prompt, metatags, metadata
        """
        
        # Use defaults if not provided
        bpm = bpm or self.default_bpm
        key = key or self.default_key
        
        # Build CODED framework sections
        if coded_context is None:
            coded_context = CODEDFramework.build_context()
        
        if coded_objectives is None:
            coded_objectives = CODEDFramework.build_objectives()
        
        if coded_details is None:
            coded_details_str = CODEDFramework.build_details(key=key)
        else:
            coded_details_str = CODEDFramework.build_details(**coded_details)
        
        if coded_examples is None:
            coded_examples_str = CODEDFramework.build_examples()
        else:
            coded_examples_str = CODEDFramework.build_examples(reference_artists=coded_examples)
        
        if coded_direction is None:
            coded_direction = CODEDFramework.build_direction()
        
        # Build metatag structure
        metatags = self._build_metatags(
            structure=structure,
            turkish_tags=turkish_genre_tags,
            global_tags=global_genre_tags
        )
        
        # Build main prompt using CODED framework
        prompt_parts = [
            f"Genre: {genre_fusion}",
            f"BPM: {bpm}",
            f"Key: {key}",
            "",
            "=== CODED FRAMEWORK ===",
            "",
            f"[CONTEXT] {coded_context}",
            "",
            f"[OBJECTIVES] {coded_objectives}",
            "",
            f"[DETAILS] {coded_details_str}",
            "",
            f"[EXAMPLES] {coded_examples_str}",
            "",
            f"[DIRECTION] {coded_direction}",
            "",
            "=== STRUCTURE ===",
            ""
        ]
        
        # Add metatags and lyrics structure
        if lyrics:
            # Integrate lyrics with metatags
            prompt_parts.extend(self._integrate_lyrics_with_metatags(lyrics, metatags))
        else:
            # Just show metatag structure
            prompt_parts.extend(metatags)
        
        # Add custom instructions if provided
        if custom_instructions:
            prompt_parts.extend([
                "",
                "=== ADDITIONAL INSTRUCTIONS ===",
                custom_instructions
            ])
        
        # Build final prompt
        suno_prompt = "\n".join(prompt_parts)
        
        return {
            "suno_prompt": suno_prompt,
            "metatags_used": metatags,
            "metadata": {
                "genre_fusion": genre_fusion,
                "bpm": bpm,
                "key": key,
                "entity": "Karasahin (JK)",
                "framework": "CODED",
                "timestamp": datetime.now().isoformat()
            }
        }
    
    def _build_metatags(
        self,
        structure: Optional[List[StructuralTag]] = None,
        turkish_tags: Optional[List[TurkishGenreTag]] = None,
        global_tags: Optional[List[GlobalGenreTag]] = None
    ) -> List[str]:
        """Build metatag list for Suno"""
        
        tags = []
        
        # Add genre tags
        if turkish_tags:
            for tag in turkish_tags:
                tags.append(f"[{tag}]")
        
        if global_tags:
            for tag in global_tags:
                tags.append(f"[{tag.replace('_', ' ')}]")
        
        # Add structural tags
        if structure is None:
            structure = ["INTRO", "VERSE_1", "CHORUS", "VERSE_2", "CHORUS", "BRIDGE", "CHORUS", "OUTRO"]
        
        for tag in structure:
            tags.append(f"[{tag.replace('_', ' ')}]")
        
        return tags
    
    def _integrate_lyrics_with_metatags(
        self,
        lyrics: Dict,
        metatags: List[str]
    ) -> List[str]:
        """Integrate lyrics from lyric_engine with structural metatags"""
        
        integrated = []
        
        # Determine which language to use (prefer English for Suno)
        lyrics_data = lyrics.get("english_lyrics") or lyrics.get("turkish_lyrics")
        
        if not lyrics_data:
            return metatags
        
        sections = lyrics_data.get("sections", {})
        
        # Map sections to metatags
        section_map = {
            "intro": "[INTRO]",
            "verse_1": "[VERSE 1]",
            "verse_2": "[VERSE 2]",
            "verse_3": "[VERSE 3]",
            "pre_chorus": "[PRE-CHORUS]",
            "chorus": "[CHORUS]",
            "bridge": "[BRIDGE]",
            "outro": "[OUTRO]"
        }
        
        for section_key, metatag in section_map.items():
            if section_key in sections:
                integrated.append(metatag)
                for line in sections[section_key]:
                    integrated.append(line)
                integrated.append("")  # Blank line
        
        return integrated
    
    def build_galactic_philosophy_prompt(
        self,
        language: Literal["english", "turkish"] = "english",
        genre_fusion: Optional[str] = None,
        bpm: Optional[int] = None,
        key: Optional[str] = None,
        include_all_forms: bool = True
    ) -> Dict:
        """
        Build a Suno-ready prompt for Galactic Philosophy: The Four Forms
        
        This method generates prompts that honor:
        - The four forms of galaxies (Spiral, Barred Spiral, Elliptical, Irregular)
        - The cosmic truth: "Galaxies come in different forms, each shaped by gravity, time, and cosmic interactions"
        - The foundation: "We are born a miracle. We deserve to live a miracle. Each and every one of us under the Lord's word."
        - The mission: "Energy + Love = We All Win"
        
        Args:
            language: "english" or "turkish" for the prompt language
            genre_fusion: Custom genre blend (defaults based on language)
            bpm: Target BPM (defaults to 85)
            key: Musical key (defaults to D minor)
            include_all_forms: Whether to include all four forms in structure
        
        Returns:
            Dict with suno_prompt, metatags, metadata
        """
        
        # Default genre fusion based on language
        if genre_fusion is None:
            if language == "english":
                genre_fusion = "Neo-Soul + Ambient Electronic + Cosmic Hip-Hop"
            else:
                genre_fusion = "Türk Arabesk + Neo-Soul + Ambient Electronic"
        
        bpm = bpm or self.default_bpm
        key = key or self.default_key
        
        # Build CODED framework for galactic philosophy
        if language == "english":
            coded_context = CODEDFramework.build_context(
                setting="Cosmic Observatory",
                time="Midnight",
                atmosphere="Star-filled darkness. The universe reveals its forms. Each galaxy a miracle. Each person a miracle. Each path honored. Spiritual battles rage through us. Demons and angels fight through humans and animals. The four galaxies are battlefields where light and dark clash. Just as galaxies have forms, Earth has cycles. Tectonic plates move. The Earth regenerates. History has loops. The next loop is based on history. The new world emerges from regeneration."
            )
            coded_objectives = CODEDFramework.build_objectives(
                primary="Express the four forms of galaxies as the four forms of miracles. Honor all paths. Reveal cosmic truth.",
                secondary="Connect cosmic evolution to human evolution. Show that gravity, time, and cosmic interactions shape us all."
            )
            coded_details = {
                "instruments": ["Ney flute", "Rhodes piano", "808 sub-bass", "vinyl crackle", "cosmic pads", "Turkish strings", "ambient textures"],
                "effects": ["Reverb (cathedral space)", "sub-harmonic enhancement", "vinyl warmth", "sidechain compression", "cosmic delay"],
                "vocal_style": "Intimate, late-night whisper with soul. Each verse honors a different form and its spiritual battle. Chorus unites all forms. The spiritual dimension is real—demons and angels fight through us.",
                "key": key,
                "mood": "Contemplative, expansive, honoring all forms. Cosmic wonder meets human truth."
            }
            coded_examples = ["J Dilla's swing and soul", "Flying Lotus' cosmic layers", "Nujabes' emotional depth", "Turkish Arabesk emotion", "ambient space music"]
            coded_direction = CODEDFramework.build_direction(
                aesthetic="Lo-fi soul over pristine digital. Warmth over perfection. Space over clutter. Cosmic truth in human voice.",
                constraints=["Over-produced pop sheen", "sterile digital sound", "generic trap drums", "cluttered arrangements"]
            )
        else:  # Turkish
            coded_context = CODEDFramework.build_context(
                setting="Kozmik Gözlemevi",
                time="Gece yarısı",
                atmosphere="Yıldızlarla dolu karanlık. Evren formlarını açığa çıkarıyor. Her galaksi bir mucize. Her insan bir mucize. Her yol onurlandırılıyor."
            )
            coded_objectives = CODEDFramework.build_objectives(
                primary="Dört galaksi formunu dört mucize formu olarak ifade et. Tüm yolları onurlandır. Kozmik gerçeği açığa çıkar.",
                secondary="Kozmik evrimi insan evrimine bağla. Yerçekimi, zaman ve kozmik etkileşimlerin hepimizi şekillendirdiğini göster."
            )
            coded_details = {
                "instruments": ["Ney", "Rhodes piyano", "808 sub-bass", "vinil çıtırtısı", "kozmik padler", "Türk telleri", "ambient dokular"],
                "effects": ["Reverb (katedral alanı)", "sub-harmonik geliştirme", "vinil sıcaklığı", "sidechain sıkıştırma", "kozmik delay"],
                "vocal_style": "Samimi, gece yarısı fısıltısı, ruhla. Her dörtlük farklı bir formu onurlandırıyor. Nakarat tüm formları birleştiriyor.",
                "key": key,
                "mood": "Düşünceli, genişleyen, tüm formları onurlandıran. Kozmik merak insan gerçeğiyle buluşuyor."
            }
            coded_examples = ["J Dilla'nın salınımı ve ruhu", "Flying Lotus'un kozmik katmanları", "Nujabes'in duygusal derinliği", "Türk Arabesk duygusu", "ambient uzay müziği"]
            coded_direction = CODEDFramework.build_direction(
                aesthetic="Pristine dijital üzerinde lo-fi soul. Mükemmellik üzerinde sıcaklık. Karmaşa üzerinde alan. İnsan sesinde kozmik gerçek.",
                constraints=["Aşırı üretilmiş pop parlaklığı", "steril dijital ses", "genel trap davulları", "karmaşık düzenlemeler"]
            )
        
        # Build structure with four forms
        if include_all_forms:
            structure = ["INTRO", "VERSE_1", "PRE_CHORUS", "CHORUS", "VERSE_2", "PRE_CHORUS", "CHORUS", "VERSE_3", "BRIDGE", "PRE_CHORUS", "CHORUS", "OUTRO"]
        else:
            structure = ["INTRO", "VERSE_1", "CHORUS", "VERSE_2", "CHORUS", "BRIDGE", "CHORUS", "OUTRO"]
        
        # Build lyrics structure for four forms
        if language == "english":
            lyrics_structure = self._build_galactic_lyrics_english()
        else:
            lyrics_structure = self._build_galactic_lyrics_turkish()
        
        # Build the prompt
        prompt_parts = [
            f"Genre: {genre_fusion}",
            f"BPM: {bpm}",
            f"Key: {key}",
            "",
            "=== CODED FRAMEWORK ===",
            "",
            f"[CONTEXT] {coded_context}",
            "",
            f"[OBJECTIVES] {coded_objectives}",
            "",
            f"[DETAILS] {CODEDFramework.build_details(**coded_details)}",
            "",
            f"[EXAMPLES] {CODEDFramework.build_examples(reference_artists=coded_examples)}",
            "",
            f"[DIRECTION] {coded_direction}",
            "",
            "=== STRUCTURE ===",
            ""
        ]
        
        # Add lyrics structure
        prompt_parts.extend(lyrics_structure)
        
        # Add additional instructions
        if language == "english":
            additional_instructions = """This track should feel like a cosmic revelation delivered at midnight. Ottoman spirit in digital body. The four forms are not just galaxies—they are the forms of miracles. They are spiritual battlefields where demons and angels fight through us—humans and animals. Each verse honors one form and its spiritual battle. The chorus unites all forms. The bridge honors transformation. The outro returns to cosmic silence.

The spiritual dimension is real. The battles are fought through us, not against us. We are the vessels. We are the battlefield. We are the miracle. Just as galaxies have forms, Earth has cycles. Tectonic plates move. The Earth regenerates. History has loops. The next loop is based on history. The new world emerges from regeneration.

Vocal delivery: Each verse should have a different energy:
- Verse 1 (Spiral): Active, flowing, dynamic - active spiritual battles
- Verse 2 (Barred Spiral): Structured, clear, channeled - structured spiritual battles
- Verse 3 (Elliptical): Contemplative, wise, legacy - legacy spiritual battles
- Bridge (Irregular): Transformative, flexible, adaptive - transformative spiritual battles

The chorus should be the anchor—unifying all forms, honoring all miracles, recognizing the spiritual battles fought through us.

This is stewardship and community with the right spirits. This is love as the highest mastery. This is energy + love = we all win. DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

Peace, Love, Unity."""
        else:
            additional_instructions = """Bu parça gece yarısı verilen kozmik bir vahiy gibi hissettirmeli. Dijital bedende Osmanlı ruhu. Dört form sadece galaksiler değil—mucizelerin formları. Şeytanlar ve meleklerin bizim içimizden—insanlar ve hayvanlar üzerinden—savaştığı ruhsal savaş alanları. Her dörtlük bir formu ve onun ruhsal savaşını onurlandırıyor. Nakarat tüm formları birleştiriyor. Köprü dönüşümü onurlandırıyor. Çıkış kozmik sessizliğe dönüyor. Ruhsal boyut gerçektir. Savaşlar bizim içimizden geçiyor, bize karşı değil. Biz gemileriz. Biz savaş alanıyız. Biz mucizeyiz. Galaksiler formlara sahip olduğu gibi, Dünya döngülere sahip. Tektonik plakalar hareket eder. Dünya yenilenir. Tarih döngüleri var. Sonraki döngü tarihe dayanır. Yeni dünya yenilenmeden ortaya çıkar.

Vokal sunum: Her dörtlük farklı bir enerjiye sahip olmalı:
- Verse 1 (Sarmal): Aktif, akan, dinamik - aktif ruhsal savaşlar
- Verse 2 (Çubuklu Sarmal): Yapılandırılmış, net, kanalize edilmiş - yapılandırılmış ruhsal savaşlar
- Verse 3 (Elips): Düşünceli, bilge, miras - miras ruhsal savaşlar
- Bridge (Düzensiz): Dönüştürücü, esnek, uyarlanabilir - dönüştürücü ruhsal savaşlar

Nakarat çapa olmalı—tüm formları birleştiren, tüm mucizeleri onurlandıran.

Bu doğru ruhlarla vekilharçlık ve topluluktur. Bu sevginin en yüksek ustalığıdır. Bu enerji + sevgi = hepimiz kazanırız. Barış, Sevgi, Birlik."""
        
        prompt_parts.extend([
            "",
            "=== ADDITIONAL INSTRUCTIONS ===",
            additional_instructions
        ])
        
        suno_prompt = "\n".join(prompt_parts)
        
        return {
            "suno_prompt": suno_prompt,
            "metatags_used": self._build_metatags(structure=structure),
            "metadata": {
                "genre_fusion": genre_fusion,
                "bpm": bpm,
                "key": key,
                "entity": "Karasahin (JK)",
                "framework": "CODED + Galactic Philosophy",
                "language": language,
                "theme": "Galactic Philosophy: The Four Forms",
                "timestamp": datetime.now().isoformat()
            }
        }
    
    def _build_galactic_lyrics_english(self) -> List[str]:
        """Build English lyrics structure for galactic philosophy"""
        return [
            "[INTRO]",
            "(Instrumental: Ney flute enters, cosmic pads swell, vinyl crackle)",
            '(Whisper: "Galaxies come in different forms...")',
            "(Beat drops: 808 sub-bass, Rhodes piano)",
            "",
            "[VERSE 1]",
            "Spiral arms, they rotate slow (A)",
            "Gas and dust, where new stars grow (A)",
            "Bright core burning, active light (B)",
            "This is the active one, flowing right (B)",
            "Demons and angels fight through us (C)",
            "Humans and animals, the battlefield (C)",
            "Spiritual battles, active and real (D)",
            "We are born a miracle (E)",
            "We deserve to live a miracle (E)",
            "Each and every one of us under the Lord's word (F)",
            "Spiral form, energy flows (G)",
            "Rapid growth, the path it shows (G)",
            "",
            "[PRE-CHORUS]",
            "Galaxies come in different forms",
            "Each shaped by gravity, time, and cosmic interactions",
            "Just as galaxies evolve in different ways",
            "So do people and communities",
            "Earth has cycles, tectonic plates move",
            "History has loops, the next loop based on history",
            "The new world emerges from regeneration",
            "Our systems must honor all these paths",
            "",
            "[CHORUS]",
            "We are born a miracle",
            "We deserve to live a miracle",
            "Each and every one of us under the Lord's word",
            "Together, these forms reveal",
            "The many paths miracles take",
            "As they evolve over lifetimes",
            "Earth regenerates, history loops",
            "The new world emerges",
            "Energy + Love = We All Win",
            "Peace, Love, Unity",
            "",
            "[VERSE 2]",
            "Barred spiral, central line (A)",
            "Channels energy, makes it shine (A)",
            "Structured path, clear and true (B)",
            "This is the structured one, guiding you (B)",
            "Demons and angels fight through channels (C)",
            "Structured battles, light and dark (C)",
            "The central bar channels both forces (D)",
            "We are born a miracle (E)",
            "We deserve to live a miracle (E)",
            "Each and every one of us under the Lord's word (F)",
            "Barred form, energy streams (G)",
            "Clear direction, like it seems (G)",
            "",
            "[PRE-CHORUS]",
            "Galaxies come in different forms",
            "Each shaped by gravity, time, and cosmic interactions",
            "Just as galaxies evolve in different ways",
            "So do people and communities",
            "Our systems must honor all these paths",
            "",
            "[CHORUS]",
            "We are born a miracle",
            "We deserve to live a miracle",
            "Each and every one of us under the Lord's word",
            "Together, these forms reveal",
            "The many paths miracles take",
            "As they evolve over lifetimes",
            "Energy + Love = We All Win",
            "",
            "[VERSE 3]",
            "Elliptical, smooth and round (A)",
            "Old stars shine, wisdom found (A)",
            "Little gas, but wisdom deep (B)",
            "This is the legacy one, secrets to keep (B)",
            "Demons and angels fought old wars (C)",
            "Legacy battles, wisdom from before (C)",
            "Old stars remember the fights (D)",
            "We are born a miracle (E)",
            "We deserve to live a miracle (E)",
            "Each and every one of us under the Lord's word (F)",
            "Elliptical form, wisdom old (G)",
            "Legacy stories, truth untold (G)",
            "",
            "[BRIDGE]",
            "Irregular, no shape defined (A)",
            "Shaped by collisions, by design (A)",
            "Highly active, changing form (B)",
            "This is the transforming one, in the storm (B)",
            "Demons and angels fight in chaos (C)",
            "No defined shape, the battle transforms (C)",
            "Collisions of light and dark forces (D)",
            "We are born a miracle (E)",
            "We deserve to live a miracle (E)",
            "Each and every one of us under the Lord's word (F)",
            "Irregular form, breaking free (G)",
            "Transformation, what will be (G)",
            "",
            "[PRE-CHORUS]",
            "Galaxies come in different forms",
            "Each shaped by gravity, time, and cosmic interactions",
            "Just as galaxies evolve in different ways",
            "So do people and communities",
            "Earth has cycles, tectonic plates move",
            "History has loops, the next loop based on history",
            "The new world emerges from regeneration",
            "Our systems must honor all these paths",
            "",
            "[CHORUS]",
            "We are born a miracle",
            "We deserve to live a miracle",
            "Each and every one of us under the Lord's word",
            "Together, these forms reveal",
            "The many paths miracles take",
            "As they evolve over lifetimes",
            "Earth regenerates, history loops",
            "The new world emerges",
            "Energy + Love = We All Win",
            "Peace, Love, Unity",
            "",
            "[OUTRO]",
            "(Instrumental: Ney flute fades, cosmic pads sustain, vinyl crackle)",
            '(Whisper: "Just as galaxies have forms, Earth has cycles...")',
            "(Beat fades: 808 sub-bass, Rhodes piano)",
            '(Whisper: "Tectonic plates move. The Earth regenerates. History has loops. The next loop is based on history. The new world emerges...")',
            "(Silence: Cosmic space, Earth cycles, regeneration)"
        ]
    
    def _build_galactic_lyrics_turkish(self) -> List[str]:
        """Build Turkish lyrics structure for galactic philosophy"""
        return [
            "[INTRO]",
            "(Enstrümantal: Ney girer, kozmik padler şişer, vinil çıtırtısı)",
            '(Fısıltı: "Galaksiler farklı formlarda gelir...")',
            "(Beat düşer: 808 sub-bass, Rhodes piyano)",
            "",
            "[VERSE 1]",
            "Sarmal kollar, yavaşça döner (A)",
            "Gaz ve toz, yeni yıldızlar büyür (A)",
            "Parlak çekirdek, aktif ışık (B)",
            "Bu aktif olan, akan akış (B)",
            "Şeytanlar ve melekler bizim içimizden savaşır (C)",
            "İnsanlar ve hayvanlar, savaş alanı (C)",
            "Ruhsal savaşlar, aktif ve gerçek (D)",
            "Mucize olarak doğduk (E)",
            "Mucize olarak yaşamayı hak ediyoruz (E)",
            "Her birimiz Rabbin kelimesi altında (F)",
            "Sarmal form, enerji akar (G)",
            "Hızlı büyüme, yol gösterir (G)",
            "",
            "[PRE-CHORUS]",
            "Galaksiler farklı formlarda gelir",
            "Her biri yerçekimi, zaman ve kozmik etkileşimlerle şekillenir",
            "Galaksiler farklı şekillerde evrimleştiği gibi",
            "İnsanlar ve topluluklar da öyle",
            "Dünya döngüleri var, tektonik plakalar hareket eder",
            "Tarih döngüleri var, sonraki döngü tarihe dayanır",
            "Yeni dünya yenilenmeden ortaya çıkar",
            "Sistemlerimiz tüm bu yolları onurlandırmalı",
            "",
            "[CHORUS]",
            "Mucize olarak doğduk",
            "Mucize olarak yaşamayı hak ediyoruz",
            "Her birimiz Rabbin kelimesi altında",
            "Birlikte, bu formlar açığa çıkarır",
            "Mucizelerin aldığı birçok yolu",
            "Yaşamlar boyunca evrimleşirken",
            "Dünya yenilenir, tarih döngüleri",
            "Yeni dünya ortaya çıkar",
            "Enerji + Sevgi = Hepimiz Kazanırız",
            "Barış, Sevgi, Birlik",
            "",
            "[VERSE 2]",
            "Çubuklu sarmal, merkezi çizgi (A)",
            "Enerjiyi kanalize eder, parlatır ışığı (A)",
            "Yapılandırılmış yol, net ve doğru (B)",
            "Bu yapılandırılmış olan, seni yönlendirir (B)",
            "Şeytanlar ve melekler kanallardan savaşır (C)",
            "Yapılandırılmış savaşlar, ışık ve karanlık (C)",
            "Merkezi çubuk her iki gücü kanalize eder (D)",
            "Mucize olarak doğduk (E)",
            "Mucize olarak yaşamayı hak ediyoruz (E)",
            "Her birimiz Rabbin kelimesi altında (F)",
            "Çubuklu form, enerji akar (G)",
            "Net yön, yol gösterir (G)",
            "",
            "[PRE-CHORUS]",
            "Galaksiler farklı formlarda gelir",
            "Her biri yerçekimi, zaman ve kozmik etkileşimlerle şekillenir",
            "Galaksiler farklı şekillerde evrimleştiği gibi",
            "İnsanlar ve topluluklar da öyle",
            "Sistemlerimiz tüm bu yolları onurlandırmalı",
            "",
            "[CHORUS]",
            "Mucize olarak doğduk",
            "Mucize olarak yaşamayı hak ediyoruz",
            "Her birimiz Rabbin kelimesi altında",
            "Birlikte, bu formlar açığa çıkarır",
            "Mucizelerin aldığı birçok yolu",
            "Yaşamlar boyunca evrimleşirken",
            "Enerji + Sevgi = Hepimiz Kazanırız",
            "",
            "[VERSE 3]",
            "Elips galaksi, pürüzsüz yuvarlak (A)",
            "Eski yıldızlar, bilgelik bulmak (A)",
            "Az gaz, ama bilgelik derin (B)",
            "Bu miras olan, sırları saklar (B)",
            "Şeytanlar ve melekler eski savaşları savaştı (C)",
            "Miras savaşlar, önceki bilgelik (C)",
            "Eski yıldızlar savaşları hatırlar (D)",
            "Mucize olarak doğduk (E)",
            "Mucize olarak yaşamayı hak ediyoruz (E)",
            "Her birimiz Rabbin kelimesi altında (F)",
            "Elips form, bilgelik eski (G)",
            "Miras hikayeler, gerçek gizli (G)",
            "",
            "[BRIDGE]",
            "Düzensiz galaksi, şekil tanımlı değil (A)",
            "Çarpışmalarla şekillenir, tasarım (A)",
            "Yüksek aktif, değişen form (B)",
            "Bu dönüşen olan, fırtınada (B)",
            "Şeytanlar ve melekler kaosta savaşır (C)",
            "Tanımlı şekil yok, savaş dönüşür (C)",
            "Işık ve karanlık güçlerin çarpışması (D)",
            "Mucize olarak doğduk (E)",
            "Mucize olarak yaşamayı hak ediyoruz (E)",
            "Her birimiz Rabbin kelimesi altında (F)",
            "Düzensiz form, özgür ol (G)",
            "Dönüşüm, ne olacak (G)",
            "",
            "[PRE-CHORUS]",
            "Galaksiler farklı formlarda gelir",
            "Her biri yerçekimi, zaman ve kozmik etkileşimlerle şekillenir",
            "Galaksiler farklı şekillerde evrimleştiği gibi",
            "İnsanlar ve topluluklar da öyle",
            "Dünya döngüleri var, tektonik plakalar hareket eder",
            "Tarih döngüleri var, sonraki döngü tarihe dayanır",
            "Yeni dünya yenilenmeden ortaya çıkar",
            "Sistemlerimiz tüm bu yolları onurlandırmalı",
            "",
            "[CHORUS]",
            "Mucize olarak doğduk",
            "Mucize olarak yaşamayı hak ediyoruz",
            "Her birimiz Rabbin kelimesi altında",
            "Birlikte, bu formlar açığa çıkarır",
            "Mucizelerin aldığı birçok yolu",
            "Yaşamlar boyunca evrimleşirken",
            "Dünya yenilenir, tarih döngüleri",
            "Yeni dünya ortaya çıkar",
            "Enerji + Sevgi = Hepimiz Kazanırız",
            "Barış, Sevgi, Birlik",
            "",
            "[OUTRO]",
            "(Enstrümantal: Ney kaybolur, kozmik padler sürer, vinil çıtırtısı)",
            '(Fısıltı: "Galaksiler formlara sahip olduğu gibi, Dünya döngülere sahip...")',
            "(Beat kaybolur: 808 sub-bass, Rhodes piyano)",
            '(Fısıltı: "Tektonik plakalar hareket eder. Dünya yenilenir. Tarih döngüleri var. Sonraki döngü tarihe dayanır. Yeni dünya ortaya çıkar...")',
            "(Sessizlik: Kozmik alan, Dünya döngüleri, yenilenme)"
        ]


# CLI Test Interface
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 80)
    print("SUNO PROMPT ENGINE - Karasahin (JK)")
    print("CODED Framework Integration + Galactic Philosophy")
    print("=" * 80)
    
    engine = SunoPromptEngine()
    
    # Example 1: Galactic Philosophy (English)
    print("\n[EXAMPLE 1] Galactic Philosophy - English")
    print("Theme: The Four Forms of Miracles")
    print("Language: English")
    print("\n" + "-" * 80 + "\n")
    
    galactic_english = engine.build_galactic_philosophy_prompt(language="english")
    print(galactic_english["suno_prompt"])
    print("\n" + "=" * 80)
    
    # Example 2: Galactic Philosophy (Turkish)
    print("\n[EXAMPLE 2] Galactic Philosophy - Turkish")
    print("Theme: The Four Forms of Miracles")
    print("Language: Turkish")
    print("\n" + "-" * 80 + "\n")
    
    galactic_turkish = engine.build_galactic_philosophy_prompt(language="turkish")
    print(galactic_turkish["suno_prompt"])
    print("\n" + "=" * 80)
    
    # Example 3: Traditional CODED Framework
    print("\n[EXAMPLE 3] Traditional CODED Framework")
    print("Theme: Manifesto of the Midnight Reversal")
    print("BPM: 85 (downtempo pocket)")
    print("Key: D minor")
    print("\n" + "-" * 80 + "\n")
    
    # Build with CODED framework
    prompt_result = engine.build_prompt(
        genre_fusion="Turkish Arabesque + R&B + Lo-Fi Hip-Hop",
        bpm=85,
        key="D minor",
        structure=["INTRO", "VERSE_1", "CHORUS", "VERSE_2", "CHORUS", "BRIDGE", "CHORUS", "OUTRO"],
        turkish_genre_tags=["ARABESK", "OTTOMAN"],
        global_genre_tags=["R_AND_B", "LO_FI", "HIP_HOP"],
        coded_context=CODEDFramework.build_context(
            setting="Spiritual Courtroom meets Studio Darkness",
            time="11:57 PM to 3:33 AM",
            atmosphere="Midnight Reversal energy, breaking the Smallness Covenant"
        ),
        coded_objectives=CODEDFramework.build_objectives(
            primary="Manifesting the Original Name through sound",
            secondary="Resurrection breath in every note"
        ),
        coded_details={
            "instruments": ["Vinyl crackle", "808 sub-bass", "Ney flute", "Rhodes piano", "Turkish strings"],
            "effects": ["Sub-harmonic enhancement", "Vinyl warmth", "Sidechain compression", "Reverb (cathedral)"],
            "vocal_style": "Intimate, late-night studio whisper with Ottoman soul",
            "key": "D minor",
            "mood": "Contemplative power, minor key beauty"
        },
        coded_examples=["J Dilla's swing and soul", "Flying Lotus' experimental layers", "Nujabes' emotional depth", "Turkish Arabesk emotion"],
        coded_direction=CODEDFramework.build_direction(
            aesthetic="Lo-fi soul over pristine digital. Warmth over perfection. Space over clutter.",
            constraints=["Over-produced pop sheen", "Sterile digital sound", "Generic trap drums"]
        ),
        custom_instructions="This track should feel like a courtroom verdict delivered at 3 AM. Ottoman spirit in digital body. The preemptive apology is burned. This is the Sound Architect's declaration."
    )
    
    print("[OK] Suno Prompt Generated\n")
    print("=" * 80)
    print("SUNO-READY PROMPT:")
    print("=" * 80)
    print(prompt_result["suno_prompt"])
    print("=" * 80)
    
    print(f"\n[METADATA]")
    print(f"Genre: {prompt_result['metadata']['genre_fusion']}")
    print(f"BPM: {prompt_result['metadata']['bpm']}")
    print(f"Key: {prompt_result['metadata']['key']}")
    print(f"Framework: {prompt_result['metadata']['framework']}")
    print(f"Entity: {prompt_result['metadata']['entity']}")
    
    # Save all prompts
    import os
    output_dir = "s:\\JAN\\SIYEM\\output\\suno_prompts"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save galactic English
    english_path = os.path.join(output_dir, f"galactic_philosophy_english_{timestamp}.txt")
    with open(english_path, 'w', encoding='utf-8') as f:
        f.write(galactic_english["suno_prompt"])
    print(f"\n[SAVED] Galactic English: {english_path}")
    
    # Save galactic Turkish
    turkish_path = os.path.join(output_dir, f"galactic_philosophy_turkish_{timestamp}.txt")
    with open(turkish_path, 'w', encoding='utf-8') as f:
        f.write(galactic_turkish["suno_prompt"])
    print(f"[SAVED] Galactic Turkish: {turkish_path}")
    
    # Save traditional
    traditional_path = os.path.join(output_dir, f"midnight_reversal_{timestamp}.txt")
    with open(traditional_path, 'w', encoding='utf-8') as f:
        f.write(prompt_result["suno_prompt"])
    print(f"[SAVED] Traditional: {traditional_path}")
    
    print("\n[LISTEN] This is 3 AM music. Sound is everything.")
    print("[GALACTIC] The four forms honor all paths. Energy + Love = We All Win. DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

Peace, Love, Unity.")
    print("=" * 80)

