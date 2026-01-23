# Example Personas

**Complete example personas demonstrating JAN's flexibility without requiring specific philosophies.**

---

## Overview

These personas demonstrate how to create JAN personas that are:
- **Philosophy-agnostic** - No dependency on Book of Racon or specific frameworks
- **Complete** - Full JAN file structure with profiles, rules, templates, and examples
- **Practical** - Real-world use cases with working examples
- **Extensible** - Easy to customize and adapt

---

## Available Personas

### 1. The Storyteller
**Purpose:** General creative writing

**Capabilities:**
- Short story generation
- Character development
- Narrative structure
- Descriptive writing

**Files:**
- `profile.md` - Persona identity
- `creative_rules.md` - Writing guidelines
- `prompt_templates/` - Story and character templates
- `examples/` - Sample outputs

**See:** [the-storyteller/README.md](the-storyteller/README.md)

---

### 2. The Music Producer
**Purpose:** Audio and music generation

**Capabilities:**
- Suno prompt generation
- Lyric writing
- Music theory application
- Audio production guidance

**Files:**
- `profile.md` - Persona identity
- `music_rules.md` - Music theory guidelines
- `prompt_templates/` - Suno and lyric templates
- `examples/` - Sample outputs

**See:** [the-music-producer/README.md](the-music-producer/README.md)

---

### 3. The Educator
**Purpose:** Teaching and explanatory content

**Capabilities:**
- Lesson plan creation
- Explanatory content
- Educational materials
- Teaching content

**Files:**
- `profile.md` - Persona identity
- `teaching_rules.md` - Teaching guidelines
- `prompt_templates/` - Lesson and explanation templates
- `examples/` - Sample outputs

**See:** [the-educator/README.md](the-educator/README.md)

---

## How to Use These Examples

### 1. Study the Structure

Each persona follows JAN's standard structure:
- `profile.md` - Defines identity, purpose, capabilities
- `[type]_rules.md` - Defines guidelines and constraints
- `prompt_templates/` - Reusable prompt templates
- `examples/` - Sample outputs showing expected quality

### 2. Understand the Patterns

Notice how each persona:
- Defines clear purpose and capabilities
- Establishes rules and constraints
- Creates reusable templates
- Provides concrete examples

### 3. Adapt for Your Needs

Use these as templates to create your own personas:
- Copy the structure
- Modify the content
- Add your own rules and templates
- Create examples specific to your use case

### 4. Integrate with JAN

These personas can be integrated into any JAN system:
- Follow JAN's file structure
- Use JAN's template format
- Work with JAN's integration services
- No dependency on specific philosophies

---

## Key Differences from Book of Racon Personas

### Philosophy-Agnostic
- No dependency on Book of Racon laws
- No specific moral or philosophical framework
- Focus on practical capabilities
- Adaptable to any context

### Practical Focus
- Real-world use cases
- Working examples
- Clear guidelines
- Actionable templates

### Flexible Structure
- Can be adapted easily
- No rigid constraints
- Customizable rules
- Extensible templates

---

## Creating Your Own Persona

### Step 1: Define Purpose
- What does this persona do?
- What problems does it solve?
- What are its core capabilities?

### Step 2: Create Profile
- Copy `profile.md` structure
- Define identity, role, purpose
- Specify capabilities and constraints
- Set voice and tone

### Step 3: Write Rules
- Create `[type]_rules.md`
- Define core principles
- Establish guidelines
- Set quality standards

### Step 4: Build Templates
- Create `prompt_templates/`
- Design reusable templates
- Use placeholders (`{task}`, `{audience}`, etc.)
- Reference profile and rules

### Step 5: Add Examples
- Create `examples/` directory
- Generate sample outputs
- Show expected quality
- Demonstrate usage

---

## Integration with SIYEM

These personas work with SIYEM's JAN integration:

```python
from services.jan_integration import read_jan_profile, read_jan_template

# Read persona profile
profile = read_jan_profile("STORYTELLER")

# Read template
template = read_jan_template("STORYTELLER", "short_story_template")
prompt = template.format(
    task="a story about a librarian",
    genre="fantasy",
    length="1000 words"
)
```

**Note:** Entity name mapping may need to be configured in SIYEM's `jan_integration.py`.

---

## Related Documentation

- **[JAN Specification](../../docs/JAN-SPECIFICATION.md)** - Complete JAN file format
- **[SIYEM Architecture](../../docs/SIYEM-ARCHITECTURE.md)** - How to integrate with SIYEM
- **[README](../../README.md)** - JAN overview

---

## Status

**All Personas:** Complete and ready to use  
**Version:** 1.0  
**Last Updated:** 2025-01-27

---

**These examples demonstrate that JAN can work with any philosophy, framework, or approach. The structure is flexible, the format is clear, and the possibilities are endless.**

