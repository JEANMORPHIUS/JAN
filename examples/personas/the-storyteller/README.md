# The Storyteller Persona

**A general-purpose creative writing persona for JAN.**

---

## Purpose

The Storyteller is a persona designed for general creative writing tasks. It focuses on:
- Narrative structure and pacing
- Character development
- Descriptive language
- Story coherence
- Engaging prose

**No specific philosophy required** - this persona is genre-agnostic and adaptable to various writing styles.

---

## What This Persona Does

### Core Capabilities

1. **Short Story Generation**
   - Complete short stories with beginning, middle, end
   - Character-driven narratives
   - Setting and atmosphere creation

2. **Character Development**
   - Character bios and backstories
   - Character arcs and motivations
   - Dialogue and voice

3. **Narrative Elements**
   - Plot structure
   - Conflict and resolution
   - Pacing and tension

4. **Creative Writing**
   - Descriptive passages
   - Scene setting
   - Emotional resonance

---

## File Structure

```
the-storyteller/
├── README.md                          # This file
├── profile.md                         # Persona identity
├── creative_rules.md                  # Writing guidelines
├── prompt_templates/
│   ├── short_story_template.md       # Short story generation
│   ├── character_bio_template.md     # Character development
│   └── scene_description_template.md # Scene writing
└── examples/
    ├── short_story_example.md        # Example short story
    └── character_bio_example.md      # Example character bio
```

---

## How to Use

### 1. Read the Profile

Start with `profile.md` to understand The Storyteller's identity and capabilities.

### 2. Review the Rules

Read `creative_rules.md` to understand writing guidelines and constraints.

### 3. Use Templates

Use the templates in `prompt_templates/` for structured writing tasks:
- `short_story_template.md` - For complete short stories
- `character_bio_template.md` - For character development
- `scene_description_template.md` - For scene writing

### 4. See Examples

Check `examples/` for sample outputs to understand expected quality and style.

---

## Integration with JAN

This persona follows JAN's structure but is **philosophy-agnostic**:
- Uses JAN's file structure (profile.md, rules, templates)
- Follows JAN's template format
- Can be integrated into any JAN system
- No dependency on Book of Racon or specific philosophy

---

## Customization

### Adapting the Voice

Edit `profile.md` to change:
- Writing style (literary, commercial, experimental)
- Tone (serious, humorous, dark)
- Genre preferences

### Modifying Rules

Edit `creative_rules.md` to adjust:
- Writing constraints
- Style requirements
- Quality standards

### Adding Templates

Create new templates in `prompt_templates/` for:
- Specific genres (sci-fi, fantasy, romance)
- Different formats (flash fiction, novellas)
- Specialized content (dialogue, action scenes)

---

## Example Usage

### Generate a Short Story

```python
from services.jan_integration import read_jan_template

template = read_jan_template("STORYTELLER", "short_story_template")
prompt = template.format(
    task="a 1000-word story about a librarian who discovers a magical book",
    genre="fantasy",
    tone="whimsical"
)
```

### Generate a Character Bio

```python
template = read_jan_template("STORYTELLER", "character_bio_template")
prompt = template.format(
    task="a detailed character bio for a detective",
    character_name="Sarah Chen",
    background="former military, now private investigator"
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

