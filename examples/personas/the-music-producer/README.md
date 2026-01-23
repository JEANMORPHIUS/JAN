# The Music Producer Persona

**A genre-agnostic music production persona for JAN.**

---

## Purpose

The Music Producer is a persona designed for audio and music generation tasks. It focuses on:
- Music theory and composition
- Genre-agnostic style preferences
- Suno prompt generation
- Lyric writing
- Audio production guidance

**No specific philosophy required** - this persona is adaptable to any musical style or genre.

---

## What This Persona Does

### Core Capabilities

1. **Suno Prompt Generation**
   - Structured prompts for Suno AI music generation
   - Genre-specific metatags and cues
   - BPM, key, and instrumentation guidance
   - Style and mood specifications

2. **Lyric Writing**
   - Original lyrics in various styles
   - Song structure (verse, chorus, bridge)
   - Rhyme schemes and meter
   - Emotional and thematic coherence

3. **Music Theory Application**
   - Chord progressions and harmony
   - Scale and mode selection
   - Rhythm and time signature guidance
   - Arrangement suggestions

4. **Audio Production**
   - Mixing and mastering guidance
   - Effect and processing recommendations
   - Instrumentation choices
   - Production workflow

---

## File Structure

```
the-music-producer/
├── README.md                          # This file
├── profile.md                         # Persona identity
├── music_rules.md                     # Music theory and style guidelines
├── prompt_templates/
│   ├── suno_prompt_template.md       # Suno AI prompt generation
│   └── lyric_writing_template.md     # Lyric generation
└── examples/
    ├── suno_prompt_example.md         # Example Suno prompt
    └── lyric_example.md               # Example lyrics
```

---

## How to Use

### 1. Read the Profile

Start with `profile.md` to understand The Music Producer's identity and capabilities.

### 2. Review the Rules

Read `music_rules.md` to understand music theory guidelines and style preferences.

### 3. Use Templates

Use the templates in `prompt_templates/` for structured music tasks:
- `suno_prompt_template.md` - For Suno AI music generation
- `lyric_writing_template.md` - For lyric writing

### 4. See Examples

Check `examples/` for sample outputs to understand expected quality and format.

---

## Integration with JAN

This persona follows JAN's structure but is **genre-agnostic**:
- Uses JAN's file structure (profile.md, rules, templates)
- Follows JAN's template format
- Can be integrated into any JAN system
- No dependency on specific musical philosophy or genre

---

## Customization

### Adapting the Style

Edit `profile.md` to change:
- Preferred genres (though persona is genre-agnostic)
- Production style (minimalist, maximalist, etc.)
- Instrumentation preferences

### Modifying Rules

Edit `music_rules.md` to adjust:
- Music theory constraints
- Style requirements
- Production standards

### Adding Templates

Create new templates in `prompt_templates/` for:
- Specific genres (if desired)
- Different formats (instrumentals, vocals, etc.)
- Specialized content (beats, melodies, etc.)

---

## Example Usage

### Generate a Suno Prompt

```python
from services.jan_integration import read_jan_template

template = read_jan_template("MUSIC_PRODUCER", "suno_prompt_template")
prompt = template.format(
    task="an upbeat electronic track",
    genre="electronic",
    mood="energetic",
    bpm="128",
    key="C major"
)
```

### Generate Lyrics

```python
template = read_jan_template("MUSIC_PRODUCER", "lyric_writing_template")
prompt = template.format(
    task="a verse and chorus about new beginnings",
    theme="hope and renewal",
    style="pop",
    structure="verse-chorus"
)
```

---

## Related Documentation

- **[JAN Specification](../../docs/JAN-SPECIFICATION.md)** - Complete JAN file format
- **[SIYEM Architecture](../../docs/SIYEM-ARCHITECTURE.md)** - How to integrate with SIYEM
- **[README](../../README.md)** - JAN overview

---

**Status:** Complete Example Persona  
**Version:** 1.0  
**Last Updated:** 2025-01-27

