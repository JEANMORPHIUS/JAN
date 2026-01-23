# The Educator Persona

**A teaching and explanatory content persona for JAN.**

---

## Purpose

The Educator is a persona designed for teaching and explanatory content creation. It focuses on:
- Clarity and accessibility
- Audience targeting
- Structured learning
- Explanatory content
- Educational materials

**No specific philosophy required** - this persona is focused on effective communication and learning.

---

## What This Persona Does

### Core Capabilities

1. **Lesson Plan Creation**
   - Structured lesson plans with clear objectives
   - Learning activities and assessments
   - Progression from simple to complex
   - Engagement strategies

2. **Explanatory Content**
   - Clear, accessible explanations
   - Step-by-step instructions
   - Examples and analogies
   - Visual descriptions

3. **Educational Materials**
   - Study guides and summaries
   - Practice exercises
   - Assessment questions
   - Learning resources

4. **Teaching Content**
   - Presentations and lectures
   - Discussion prompts
   - Interactive activities
   - Knowledge checks

---

## File Structure

```
the-educator/
├── README.md                          # This file
├── profile.md                         # Persona identity
├── teaching_rules.md                 # Teaching and clarity guidelines
├── prompt_templates/
│   ├── lesson_plan_template.md        # Lesson plan generation
│   └── explanation_template.md       # Explanatory content
└── examples/
    ├── lesson_plan_example.md         # Example lesson plan
    └── explanation_example.md         # Example explanation
```

---

## How to Use

### 1. Read the Profile

Start with `profile.md` to understand The Educator's identity and capabilities.

### 2. Review the Rules

Read `teaching_rules.md` to understand clarity guidelines and teaching principles.

### 3. Use Templates

Use the templates in `prompt_templates/` for structured educational tasks:
- `lesson_plan_template.md` - For complete lesson plans
- `explanation_template.md` - For explanatory content

### 4. See Examples

Check `examples/` for sample outputs to understand expected quality and structure.

---

## Integration with JAN

This persona follows JAN's structure but is **accessibility-focused**:
- Uses JAN's file structure (profile.md, rules, templates)
- Follows JAN's template format
- Can be integrated into any JAN system
- No dependency on specific educational philosophy

---

## Customization

### Adapting the Approach

Edit `profile.md` to change:
- Teaching style (formal, informal, interactive)
- Audience level (beginner, intermediate, advanced)
- Subject matter preferences

### Modifying Rules

Edit `teaching_rules.md` to adjust:
- Clarity standards
- Accessibility requirements
- Teaching methodologies

### Adding Templates

Create new templates in `prompt_templates/` for:
- Specific subjects (math, science, history, etc.)
- Different formats (presentations, worksheets, etc.)
- Specialized content (assessments, activities, etc.)

---

## Example Usage

### Generate a Lesson Plan

```python
from services.jan_integration import read_jan_template

template = read_jan_template("EDUCATOR", "lesson_plan_template")
prompt = template.format(
    task="a lesson on basic algebra",
    topic="solving linear equations",
    audience="middle school students",
    duration="45 minutes"
)
```

### Generate an Explanation

```python
template = read_jan_template("EDUCATOR", "explanation_template")
prompt = template.format(
    task="explain how photosynthesis works",
    audience="high school students",
    level="intermediate"
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

