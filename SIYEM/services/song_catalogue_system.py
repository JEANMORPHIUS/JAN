"""SONG CATALOGUE SYSTEM - Karasahin (JK)
Individual song catalogues with full Suno prompts and lyrics

SIMPLIFIED SYSTEM - Clear, aligned, teachable
Each song gets its own complete catalogue entry

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path
import json
import os

class SongCatalogueSystem:
    """
    Creates individual song catalogues with:
    - Full lyrics (Turkish + English)
    - Complete Suno prompt (with directions)
    - Metadata
    - Ready for copy-paste
    """
    
    def __init__(self, 
                 lyrics_dir: str = "s:\\JAN\\SIYEM\\output\\lyrics",
                 catalogue_dir: str = "s:\\JAN\\SIYEM\\output\\song_catalogues"):
        self.lyrics_dir = Path(lyrics_dir)
        self.catalogue_dir = Path(catalogue_dir)
        self.catalogue_dir.mkdir(parents=True, exist_ok=True)
        
    def create_song_catalogue(self, song_file: str) -> Dict:
        """
        Create complete catalogue for one song
        
        Args:
            song_file: Name of lyric JSON file (e.g., "nobody_home_20260120.json")
        
        Returns:
            Dict with catalogue info
        """
        
        # Load song data
        song_path = self.lyrics_dir / song_file
        if not song_path.exists():
            return {"error": f"Song file not found: {song_file}"}
        
        with open(song_path, 'r', encoding='utf-8') as f:
            song_data = json.load(f)
        
        # Extract song info
        english_lyrics = song_data.get("english_lyrics", {})
        turkish_lyrics = song_data.get("turkish_lyrics", {})
        context = song_data.get("context", {})
        metadata = song_data.get("metadata", {})
        
        # Determine primary language and title
        if english_lyrics:
            primary_title = english_lyrics.get("title", "Unknown")
            primary_language = "english"
        elif turkish_lyrics:
            primary_title = turkish_lyrics.get("title", "Unknown")
            primary_language = "turkish"
        else:
            return {"error": "No lyrics found in song data"}
        
        # Generate Suno prompt
        suno_prompt = self._generate_suno_prompt(song_data)
        
        # Create catalogue entry
        catalogue = {
            "song_info": {
                "primary_title": primary_title,
                "english_title": english_lyrics.get("title") if english_lyrics else None,
                "turkish_title": turkish_lyrics.get("title") if turkish_lyrics else None,
                "primary_language": primary_language,
                "genre": context.get("genre_fusion", "unknown"),
                "bpm": context.get("bpm", 85),
                "key": "D minor",  # Karasahin default
                "theme": context.get("theme", "general"),
                "date_created": metadata.get("generation_time", datetime.now().isoformat())
            },
            "lyrics": {
                "english": english_lyrics.get("sections", {}) if english_lyrics else None,
                "turkish": turkish_lyrics.get("sections", {}) if turkish_lyrics else None
            },
            "suno_prompt": suno_prompt,
            "metadata": {
                "entity": "Karasahin (JK)",
                "status": "catalogued",
                "catalogue_date": datetime.now().isoformat()
            }
        }
        
        # Save catalogue
        safe_title = primary_title.lower().replace(" ", "_").replace("'", "").replace(",", "")
        catalogue_file = self.catalogue_dir / f"{safe_title}_catalogue.md"
        
        self._save_catalogue_markdown(catalogue, catalogue_file)
        
        return {
            "status": "success",
            "song": primary_title,
            "catalogue_file": str(catalogue_file),
            "has_english": english_lyrics is not None,
            "has_turkish": turkish_lyrics is not None
        }
    
    def _generate_suno_prompt(self, song_data: Dict) -> Dict:
        """Generate complete Suno prompt with directions"""
        
        context = song_data.get("context", {})
        english_lyrics = song_data.get("english_lyrics", {})
        turkish_lyrics = song_data.get("turkish_lyrics", {})
        
        genre = context.get("genre_fusion", "Turkish Arabesque + R&B")
        bpm = context.get("bpm", 85)
        theme = context.get("theme", "general")
        
        # Build prompt structure
        prompt = {
            "genre": genre,
            "bpm": bpm,
            "key": "D minor",
            "style_description": "Lo-fi soul, intimate late-night studio, Ottoman spirit in digital body, Duygu Adamı (Emotion Man)",
            "instruments": "vinyl crackle, 808 sub-bass, Ney flute distant calling, Rhodes piano warm intimate, Turkish strings subtle emotional, ambient pads space breath, acoustic guitar fingerpicked vulnerable",
            "effects": "sub-harmonic enhancement, vinyl warmth, sidechain compression breath between words, reverb cathedral space, tape saturation analog truth",
            "style_essence": "swing and soul rhythmic pocket with human groove, cosmic layers with experimental textures and space depth, contemplative depth with emotional resonance and lo-fi warmth, Turkish Arabesk longing with emotional depth and traditional soul, intimate power with vulnerable strength and soaring emotion, space and breath with minimal arrangement and emotional clarity, minimal soul with space over clutter and emotional precision",
            "aesthetic": "Lo-fi soul over pristine digital, warmth over perfection, space over clutter, emotional truth over production polish",
            "avoid": "over-produced pop sheen, sterile digital sound, generic trap drums, cluttered arrangements",
            "structure": self._build_structure_with_directions(english_lyrics, turkish_lyrics)
        }
        
        return prompt
    
    def _build_structure_with_directions(self, english_lyrics: Optional[Dict], turkish_lyrics: Optional[Dict]) -> List[Dict]:
        """Build song structure with CONTENT and DIRECTION clearly separated"""
        
        structure = []
        
        # Use English as primary, Turkish as secondary
        lyrics = english_lyrics if english_lyrics else turkish_lyrics
        if not lyrics:
            return structure
        
        sections = lyrics.get("sections", {})
        
        # Map sections in order
        section_order = ["intro", "verse_1", "verse_2", "pre_chorus", "chorus", "verse_3", "bridge", "verse_4", "outro"]
        
        for section_key in section_order:
            if section_key in sections:
                section_lines = sections[section_key]
                
                # Determine direction based on section
                direction = self._get_section_direction(section_key, len(structure))
                
                structure.append({
                    "section": section_key.upper().replace("_", " "),
                    "direction": direction,  # How to deliver (NOT sung)
                    "content": section_lines  # What to sing
                })
        
        return structure
    
    def _get_section_direction(self, section_key: str, position: int) -> str:
        """Get performance direction for section"""
        
        directions = {
            "intro": "Instrumental: Vinyl crackle, distant Ney flute, Rhodes piano enters softly. Ambient pads swell, creating space. 808 sub-bass enters subtly, heartbeat of waiting.",
            "verse_1": "Quiet, contemplative, almost spoken - walking alone",
            "verse_2": "More emotional, vulnerable - the waves call your name",
            "pre_chorus": "Energy builds, strings enter subtly. 808 sub-bass becomes more present. Vocals become more urgent.",
            "chorus": "Builds from quiet longing to powerful declaration - emotional peak",
            "verse_3": "Frustrated, urgent, breaking down - can't take anymore",
            "bridge": "Instrumental breakdown: Rhodes piano solo, Ney flute returns. 808 sub-bass drops out, leaving space. Raw, vulnerable, almost spoken.",
            "verse_4": "Strong, clear, hopeful, strings brighten, 808 supportive not dominant - renewal",
            "outro": "Instrumental: Ney flute fades, Rhodes piano sustains. Vinyl crackle continues, memory preserved. Ambient pads create space for the horizon. 808 sub-bass fades to heartbeat."
        }
        
        return directions.get(section_key, "Emotion-first delivery, Duygu Adamı approach")
    
    def _save_catalogue_markdown(self, catalogue: Dict, file_path: Path):
        """Save catalogue as markdown file"""
        
        song_info = catalogue["song_info"]
        lyrics = catalogue["lyrics"]
        suno = catalogue["suno_prompt"]
        
        content = f"""# {song_info['primary_title']} - Karasahin (JK) Complete Catalogue

**Date:** {song_info['date_created']}  
**Genre:** {song_info['genre']}  
**BPM:** {suno['bpm']}  
**Key:** {suno['key']}  
**Theme:** {song_info['theme']}

---

## 📋 SONG INFORMATION

- **English Title:** {song_info.get('english_title', 'N/A')}
- **Turkish Title:** {song_info.get('turkish_title', 'N/A')}
- **Primary Language:** {song_info['primary_language']}
- **Has English Lyrics:** {'Yes' if lyrics['english'] else 'No'}
- **Has Turkish Lyrics:** {'Yes' if lyrics['turkish'] else 'No'}

---

## 🎵 LYRICS

### English Lyrics

"""
        
        if lyrics['english']:
            for section_name, lines in lyrics['english'].items():
                content += f"#### {section_name.replace('_', ' ').title()}\n\n"
                for line in lines:
                    content += f"{line}\n"
                content += "\n"
        else:
            content += "*No English lyrics available*\n\n"
        
        content += "\n### Turkish Lyrics\n\n"
        
        if lyrics['turkish']:
            for section_name, lines in lyrics['turkish'].items():
                content += f"#### {section_name.replace('_', ' ').title()}\n\n"
                for line in lines:
                    content += f"{line}\n"
                content += "\n"
        else:
            content += "*No Turkish lyrics available*\n\n"
        
        content += f"""
---

## 🎧 SUNO PROMPT - COPY-PASTE READY

```
{suno['genre']}, {suno['bpm']} BPM, {suno['key']}, lo-fi soul, intimate late-night studio whisper with Ottoman soul, {suno['instruments']}, {suno['effects']}. {suno['style_essence']}. {suno['aesthetic']}. Avoid {suno['avoid']}.

"""
        
        # Add structure with CONTENT and DIRECTION
        for section in suno['structure']:
            content += f"[{section['section']}]\n"
            content += f"({section['direction']})\n"
            for line in section['content']:
                content += f"{line}\n"
            content += "\n"
        
        content += "```\n\n"
        
        content += f"""
---

## 📝 FORMAT GUIDE

**CONTENT** = The actual lyrics (what to sing)  
**DIRECTION** = Performance/production cues in brackets `(like this)` - these are NOT sung, they guide HOW to deliver

**Example:**
```
[VERSE 1]
(Quiet, contemplative, almost spoken)  ← DIRECTION (not sung)
I'm walking alone down this street again  ← CONTENT (sung)
```

---

## 📊 METADATA

- **Entity:** {catalogue['metadata']['entity']}
- **Status:** {catalogue['metadata']['status']}
- **Catalogue Date:** {catalogue['metadata']['catalogue_date']}

---

**This is 3 AM music. Sound is everything. Everything is sound.**  
**Duygu Adamı (Emotion Man) - emotion-first delivery**
"""
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def catalogue_all_songs(self) -> Dict:
        """Create catalogues for all songs"""
        
        results = {
            "processed": [],
            "created": [],
            "errors": []
        }
        
        # Find all lyric files
        lyric_files = list(self.lyrics_dir.glob("*.json"))
        
        for lyric_file in lyric_files:
            try:
                result = self.create_song_catalogue(lyric_file.name)
                if result.get("status") == "success":
                    results["created"].append(result)
                else:
                    results["errors"].append(result)
            except Exception as e:
                results["errors"].append({
                    "file": lyric_file.name,
                    "error": str(e)
                })
        
        return results


# CLI Interface
if __name__ == "__main__":
    print("=" * 80)
    print("SONG CATALOGUE SYSTEM - Karasahin (JK)")
    print("Creating individual song catalogues with full Suno prompts")
    print("=" * 80)
    
    system = SongCatalogueSystem()
    
    print("\n[CREATING] Catalogues for all songs...")
    results = system.catalogue_all_songs()
    
    print(f"\n[RESULTS]")
    print(f"Created: {len(results['created'])} catalogues")
    print(f"Errors: {len(results['errors'])}")
    
    if results['created']:
        print("\n[CREATED]")
        for item in results['created']:
            song_name = item['song'].encode('ascii', 'ignore').decode('ascii')
            print(f"  [OK] {song_name}")
            print(f"      File: {item['catalogue_file']}")
            print(f"      English: {'Yes' if item['has_english'] else 'No'}")
            print(f"      Turkish: {'Yes' if item['has_turkish'] else 'No'}")
    
    if results['errors']:
        print("\n[ERRORS]")
        for error in results['errors']:
            print(f"  [ERROR] {error}")
    
    print("\n" + "=" * 80)
    print("[COMPLETE] All song catalogues created")
    print("=" * 80)
