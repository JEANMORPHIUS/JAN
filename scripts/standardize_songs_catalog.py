"""
STANDARDIZE SONGS CATALOG
Ensure uniformity across all songs: lyrics format, Suno prompts, and style

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import re


# Standard lyric section markers
STANDARD_SECTIONS = [
    "[INTRO]", "[VERSE 1]", "[VERSE 2]", "[VERSE 3]", "[VERSE 4]",
    "[PRE-CHORUS]", "[CHORUS]", "[POST-CHORUS]",
    "[BRIDGE]", "[BREAKDOWN]", "[BUILD]", "[DROP]",
    "[OUTRO]", "[INSTRUMENTAL]", "[HOOK]", "[INTERLUDE]"
]

# Standard section markers (Turkish)
STANDARD_SECTIONS_TR = [
    "[GİRİŞ]", "[KITA 1]", "[KITA 2]", "[KITA 3]", "[KITA 4]",
    "[NAKARAT ÖNCESİ]", "[NAKARAT]", "[NAKARAT SONRASI]",
    "[KÖPRÜ]", "[BREAKDOWN]", "[BUILD]", "[DROP]",
    "[ÇIKIŞ]", "[ENSTRÜMANTAL]", "[HOOK]", "[ARALIK]"
]


def standardize_lyrics_format(lyrics: str, language: str = "english") -> str:
    """
    Standardize lyrics format:
    - Ensure proper section markers
    - Add rhyme notation where missing
    - Ensure consistent formatting
    """
    if not lyrics or lyrics.startswith("[") and "to be generated" in lyrics:
        return lyrics  # Skip placeholder lyrics
    
    lines = lyrics.split('\n')
    standardized = []
    current_section = None
    
    for line in lines:
        line = line.strip()
        if not line:
            standardized.append("")
            continue
        
        # Check if line is a section marker
        section_match = re.match(r'^\[([^\]]+)\]', line)
        if section_match:
            section_name = section_match.group(1).upper()
            # Standardize section name
            if language == "turkish":
                # Map Turkish sections
                section_map = {
                    "KITA 1": "[VERSE 1]",
                    "KITA 2": "[VERSE 2]",
                    "KITA 3": "[VERSE 3]",
                    "KITA 4": "[VERSE 4]",
                    "NAKARAT": "[CHORUS]",
                    "NAKARAT ÖNCESİ": "[PRE-CHORUS]",
                    "NAKARAT SONRASI": "[POST-CHORUS]",
                    "KÖPRÜ": "[BRIDGE]",
                    "GİRİŞ": "[INTRO]",
                    "ÇIKIŞ": "[OUTRO]",
                    "ENSTRÜMANTAL": "[INSTRUMENTAL]"
                }
                if section_name in section_map:
                    current_section = section_map[section_name]
                else:
                    current_section = f"[{section_name}]"
            else:
                # Standardize English sections
                if "VERSE" in section_name:
                    verse_num = re.search(r'\d+', section_name)
                    if verse_num:
                        current_section = f"[VERSE {verse_num.group()}]"
                    else:
                        current_section = "[VERSE 1]"
                elif "CHORUS" in section_name:
                    current_section = "[CHORUS]"
                elif "BRIDGE" in section_name:
                    current_section = "[BRIDGE]"
                elif "INTRO" in section_name:
                    current_section = "[INTRO]"
                elif "OUTRO" in section_name:
                    current_section = "[OUTRO]"
                elif "PRE-CHORUS" in section_name or "PRECHORUS" in section_name:
                    current_section = "[PRE-CHORUS]"
                elif "POST-CHORUS" in section_name or "POSTCHORUS" in section_name:
                    current_section = "[POST-CHORUS]"
                elif "INSTRUMENTAL" in section_name:
                    current_section = "[INSTRUMENTAL]"
                else:
                    current_section = f"[{section_name}]"
            
            standardized.append(current_section)
        elif line.startswith("(") and line.endswith(")"):
            # Direction/instruction line - keep as is
            standardized.append(line)
        else:
            # Lyric line - ensure it's properly formatted
            # Remove any existing rhyme notation if inconsistent
            clean_line = re.sub(r'\s*\([A-Z]\)\s*$', '', line)
            standardized.append(clean_line)
    
    return '\n'.join(standardized)


def generate_suno_prompt(song: Dict) -> str:
    """
    Generate standardized Suno prompt using CODED framework
    """
    title = song.get('title', '')
    genre = song.get('genre', '')
    notes = song.get('notes', '')
    lyrics = song.get('lyrics_original', '')
    language = song.get('language', 'english')
    
    # Extract BPM from notes
    bpm_match = re.search(r'(\d+)\s*BPM', notes, re.IGNORECASE)
    bpm = bpm_match.group(1) if bpm_match else "85"
    
    # Extract key from notes
    key_match = re.search(r'Key:\s*([A-G]\s*(?:major|minor|maj|min))', notes, re.IGNORECASE)
    key = key_match.group(1) if key_match else "D minor"
    
    # Extract instrumentation from notes
    instruments = []
    if "acoustic guitar" in notes.lower():
        instruments.append("acoustic guitar")
    if "bağlama" in notes.lower() or "baglama" in notes.lower():
        instruments.append("bağlama")
    if "piano" in notes.lower():
        instruments.append("piano")
    if "bass" in notes.lower():
        instruments.append("bass guitar")
    if "drums" in notes.lower() or "drum" in notes.lower():
        instruments.append("drums")
    if "strings" in notes.lower():
        instruments.append("strings")
    if "brass" in notes.lower():
        instruments.append("brass")
    if "choir" in notes.lower():
        instruments.append("choir")
    if "davul" in notes.lower():
        instruments.append("davul")
    if "oud" in notes.lower():
        instruments.append("oud")
    if "ney" in notes.lower():
        instruments.append("Ney flute")
    if "rhodes" in notes.lower():
        instruments.append("Rhodes piano")
    if "synth" in notes.lower():
        instruments.append("synth pad")
    
    if not instruments:
        instruments = ["acoustic guitar", "piano", "bass", "drums"]
    
    # Extract vocal style
    vocal_style = "male vocals"
    if "baritone" in notes.lower():
        vocal_style = "male baritone vocals"
    elif "mid-range" in notes.lower():
        vocal_style = "male mid-range vocals"
    elif "deep" in notes.lower():
        vocal_style = "deep male vocals"
    elif "mellow" in notes.lower():
        vocal_style = "mellow male vocals"
    
    # Extract mood
    mood_parts = []
    if "melancholic" in notes.lower():
        mood_parts.append("melancholic")
    if "defiant" in notes.lower():
        mood_parts.append("defiant")
    if "introspective" in notes.lower():
        mood_parts.append("introspective")
    if "weary" in notes.lower():
        mood_parts.append("weary")
    if "proud" in notes.lower():
        mood_parts.append("proud")
    if "mournful" in notes.lower():
        mood_parts.append("mournful")
    if "hopeful" in notes.lower():
        mood_parts.append("hopeful")
    
    mood = ", ".join(mood_parts) if mood_parts else "emotional"
    
    # Build CODED framework
    context = f"Karasahin (JK) studio, {mood} atmosphere, authentic emotional expression"
    objectives = "Create music that serves The Table through truth-telling and emotional authenticity"
    details = f"Instruments: {', '.join(instruments)}. Vocals: {vocal_style}. Mood: {mood}. Production: crisp, clear, authentic"
    examples = "Style: lo-fi soul over pristine digital, warmth over perfection, space over clutter, emotional truth over production polish"
    direction = "Avoid over-produced pop sheen, sterile digital sound, generic arrangements. Maintain authentic emotional core."
    
    # Build prompt
    prompt_parts = [
        f"Genre: {genre}",
        f"BPM: {bpm}",
        f"Key: {key}",
        "",
        "=== CODED FRAMEWORK ===",
        "",
        f"[CONTEXT] {context}",
        "",
        f"[OBJECTIVES] {objectives}",
        "",
        f"[DETAILS] {details}",
        "",
        f"[EXAMPLES] {examples}",
        "",
        f"[DIRECTION] {direction}",
        "",
        "=== STRUCTURE ===",
        ""
    ]
    
    # Add lyrics structure if available
    if lyrics and not lyrics.startswith("[") or "to be generated" not in lyrics:
        # Extract structure from lyrics
        sections = re.findall(r'\[([^\]]+)\]', lyrics)
        if sections:
            prompt_parts.append("Lyrics structure:")
            for section in sections[:10]:  # Limit to first 10 sections
                prompt_parts.append(f"- {section}")
            prompt_parts.append("")
    
    return "\n".join(prompt_parts)


def standardize_song_style(song: Dict) -> Dict:
    """
    Standardize song style and metadata
    """
    standardized = song.copy()
    
    # Ensure consistent genre format
    genre = standardized.get('genre', '')
    if genre:
        # Normalize genre capitalization
        genre_parts = [g.strip().capitalize() for g in genre.split(',')]
        standardized['genre'] = ', '.join(genre_parts)
    
    # Standardize notes format
    notes = standardized.get('notes', '')
    if notes:
        # Ensure consistent formatting
        notes = re.sub(r'\s+', ' ', notes)  # Normalize whitespace
        standardized['notes'] = notes.strip()
    
    # Ensure alignment indicators are lowercase
    if 'alignment_indicators' in standardized:
        standardized['alignment_indicators'] = [
            ind.lower() if isinstance(ind, str) else ind
            for ind in standardized['alignment_indicators']
        ]
    
    # Ensure themes are lowercase
    if 'themes' in standardized:
        standardized['themes'] = [
            theme.lower() if isinstance(theme, str) else theme
            for theme in standardized['themes']
        ]
    
    return standardized


def standardize_all_songs():
    """
    Standardize all songs in the catalog
    """
    catalog_path = Path(__file__).parent.parent / 'data' / 'frequential_songs' / 'frequential_songs_catalog.json'
    
    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog = json.load(f)
    
    standardized_count = 0
    suno_prompts_generated = 0
    
    for song_id, song in catalog.get('songs', {}).items():
        # Standardize lyrics format
        if song.get('lyrics_original'):
            original_lyrics = song['lyrics_original']
            language = song.get('language', 'english')
            standardized_lyrics = standardize_lyrics_format(original_lyrics, language)
            
            if standardized_lyrics != original_lyrics:
                song['lyrics_original'] = standardized_lyrics
                standardized_count += 1
        
        # Generate Suno prompt if not exists
        if 'suno_prompt' not in song or not song.get('suno_prompt'):
            suno_prompt = generate_suno_prompt(song)
            song['suno_prompt'] = suno_prompt
            suno_prompts_generated += 1
        
        # Standardize style
        standardized_song = standardize_song_style(song)
        catalog['songs'][song_id] = standardized_song
    
    # Update timestamp
    catalog['catalog_timestamp'] = datetime.now().isoformat()
    catalog['last_standardized'] = datetime.now().isoformat()
    
    # Save standardized catalog
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Standardization complete!")
    print(f"   Songs with standardized lyrics: {standardized_count}")
    print(f"   Suno prompts generated: {suno_prompts_generated}")
    print(f"   Total songs processed: {len(catalog.get('songs', {}))}")
    
    return catalog


if __name__ == "__main__":
    standardize_all_songs()
