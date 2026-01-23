# JAN Specification

**Complete technical specification for JAN markdown files.**

---

## What is JAN?

JAN (JAN MUHARREM) is a **markdown-based creative identity system**. It defines:

- **Entity Identity**: Who each creative persona is, their voice, purpose, specialization
- **Creative Rules**: Guidelines for how each entity creates content
- **Prompt Templates**: Reusable templates for AI-generated content
- **Governance Rules**: Security, access control, audit requirements
- **Style Modules**: Formatting and output specifications

**Key Principle:** JAN files are **data**, not code. They define "what you are" not "how you work."

---

## File Structure Requirements

### Root Level Files

#### `telos.md` (Required)
**Purpose:** Core purpose, principles, boundaries, long-term vision

**Required Sections:**
- `## Core Purpose` - What is JAN's fundamental purpose?
- `## Fundamental Principles` - Core principles (Creative Integrity, Operational Stability, Modular Expansion)
- `## Boundaries` - Hard constraints (non-negotiable) and soft constraints (discretionary)
- `## Long-Term Vision` - Where is JAN going?

**Example Structure:**
```markdown
# TELOS: JAN MUHARREM

## Core Purpose
[Purpose statement]

## Fundamental Principles
### 1. Creative Integrity
[Principles]

### 2. Operational Stability
[Principles]

### 3. Modular Expansion
[Principles]

## Boundaries
### Hard Constraints
[Non-negotiable rules]

### Soft Constraints
[Discretionary rules]

## Long-Term Vision
[Vision statement]
```

#### `essence.md` (Required)
**Purpose:** Creative fingerprint, emotional palette, tone, fusion identity

**Required Sections:**
- `## Creative Fingerprint` - Core identity, emotional palette
- `## Tone & Voice` - Primary tone, voice characteristics
- `## Fusion Identity` - Cultural and artistic fusion
- `## Creative DNA` - Artistic principles, constraints

**Example Structure:**
```markdown
# ESSENCE: JAN MUHARREM

## Creative Fingerprint
### Core Identity
[Identity statement]

### Emotional Palette
- Depth: [Description]
- Energy: [Description]
- Balance: [Description]
- Authenticity: [Description]

## Tone & Voice
### Primary Tone
[Description]

### Voice Characteristics
[Characteristics]

## Fusion Identity
### Cultural Fusion
[Description]

### Artistic Fusion
[Description]

## Creative DNA
### Artistic Principles
1. [Principle]
2. [Principle]
```

#### `jan_engine.prompt` (Required)
**Purpose:** Execution logic integrating telos, essence, and styles

**Required Sections:**
- `## Purpose` - What this file does
- `## Core Integration` - Primary sources (telos, essence, styles)
- `## Execution Flow` - Step-by-step execution process
- `## Rule Hierarchy` - 4-level hierarchy explanation
- `## Execution Rules` - Rules for all outputs, creative outputs, operational outputs

**Example Structure:**
```markdown
# JAN ENGINE: Execution Logic

## Purpose
[Purpose statement]

## Core Integration
### Primary Sources
1. telos.md
2. essence.md
3. styles/

## Execution Flow
[Flow diagram or steps]

## Rule Hierarchy
### Level 1: JAN MUHARREM Core
[Description]

### Level 2: Siyem.org Governance
[Description]

### Level 3: Entity-Specific
[Description]

### Level 4: Style Modules
[Description]
```

---

### Siyem.org Directory

#### `Siyem.org/profile.md` (Required)
**Purpose:** Operational entity profile for Siyem.org governance

**Required Sections:**
- `## Entity Identity` - Name, role, purpose
- `## Core Functions` - What Siyem.org does
- `## Relationship to JAN MUHARREM` - How it inherits from core
- `## Governance Functions` - Administrative, security, operational functions

#### `Siyem.org/admin_rules.md` (Required)
**Purpose:** Administrative protocols and governance rules

**Required Sections:**
- Administrative protocols
- Governance procedures
- Decision-making processes

#### `Siyem.org/security_lens.md` (Required)
**Purpose:** Security, privacy, and alignment constraints

**Required Sections:**
- Security requirements
- Privacy constraints
- Alignment checks

#### `Siyem.org/backroom/` (Directory)
**Purpose:** Infrastructure controls

**Required Files:**
- `access_control.md` - Access rules, authentication
- `audit_system.md` - Logging and monitoring
- `publishing_oversight.md` - Publishing controls
- `financial_controls.md` - Financial management
- `licensing_pipeline.md` - Content licensing
- `data_privacy.md` - Privacy requirements
- `network_security.md` - Network security
- `service_security.md` - Service security
- `incident_response.md` - Incident handling
- `compliance_framework.md` - Compliance requirements
- `content_protection.md` - Content protection
- `language_security.md` - Language security
- `secret_management.md` - Secret management

---

### Creation Station Structure

Each Creation Station is a directory under `Siyem.org/` with the following structure:

```
Siyem.org/[entity_name]/
├── profile.md                    # Required: Entity identity
├── creative_rules.md            # Optional: Creative guidelines
├── teaching_rules.md            # Optional: Teaching guidelines (Ramiz)
├── motivational_rules.md        # Optional: Motivational guidelines (Pierre)
├── operational_rules.md        # Optional: Operational guidelines (Siyem Media)
├── prompt_templates/            # Required: Template directory
│   ├── [template_name].md      # Template files
│   └── ...
└── style_overrides.md           # Optional: Style customizations
```

#### `profile.md` (Required)
**Purpose:** Entity identity, role, purpose, specialization

**Required Sections:**
- `## Entity Identity` - Name, role, purpose
- `## Core Functions` - What this entity does
- `## Relationship to JAN MUHARREM` - How it inherits
- `## Relationship to Siyem.org` - Governance relationship
- `## Specialization` - Entity-specific capabilities
- `## Voice` - Entity voice characteristics
- `## Themes` - Recurring themes
- `## Services` - What services this entity provides

**Example:**
```markdown
# [Entity Name]: Entity Profile

## Entity Identity
### Name
[Name]

### Role
[Role]

### Purpose
[Purpose statement]

## Core Functions
### [Function Category]
- [Function]
- [Function]

## Relationship to JAN MUHARREM
### Inheritance
- Inherits core principles from telos.md
- Inherits creative identity from essence.md
- Bound by jan_engine.prompt execution logic
- Cannot override JAN MUHARREM directives

## Specialization
[Specialization description]

## Voice
[Voice characteristics]

## Themes
[Recurring themes]
```

#### `creative_rules.md` (Optional)
**Purpose:** Creative guidelines specific to this entity

**Required Sections:**
- `## Core Principles` - Entity-specific creative principles
- `## Voice Requirements` - Voice consistency requirements
- `## Prohibited Content` - What this entity cannot create
- `## Required Elements` - What must be included
- `## Style Guidelines` - Style requirements

#### `prompt_templates/` (Required Directory)
**Purpose:** Reusable prompt templates for AI generation

**File Format:**
- Each template is a `.md` file
- Templates can use placeholders: `{task}`, `{language}`, `{entity}`
- Templates should reference core files (telos, essence, styles)

**Example Template:**
```markdown
# [Template Name]: [Entity] Creation Station

## Template Purpose
[Purpose statement]

## Template Structure
### Core Integration
```
Reference: telos.md
Reference: essence.md
Reference: styles/[module].md
Reference: profile.md
Reference: creative_rules.md
```

### [Template Name] Prompt Template

**Context Setting:**
- Entity: [Entity name]
- Content Type: {task}
- Language: {language}
- [Other context]

**Creative Direction:**
[Direction]

**Output Requirements:**
[Requirements]
```

#### `style_overrides.md` (Optional)
**Purpose:** Entity-specific style customizations

**Structure:**
- Overrides or extends styles from `styles/` directory
- Entity-specific formatting rules
- Output specifications

---

### Styles Directory

#### `styles/[module_name].md`
**Purpose:** Formatting and output specifications

**Required Sections:**
- Module purpose
- Formatting rules
- Output specifications
- Integration points

**Example:**
```markdown
# [Module Name] Style Module

## Purpose
[Purpose statement]

## Formatting Rules
[Rules]

## Output Specifications
[Specifications]

## Integration Points
[How this integrates with entities]
```

---

## Rule Hierarchy Explanation

JAN uses a **4-level hierarchy** where higher levels cannot be overridden:

### Level 1: JAN MUHARREM Core (Non-negotiable)

**Files:**
- `telos.md` - Purpose, principles, boundaries
- `essence.md` - Creative fingerprint, tone, identity
- `jan_engine.prompt` - Execution logic

**Characteristics:**
- Cannot be overridden by any entity
- Applies to all outputs
- Defines fundamental identity

**Example:**
```markdown
# telos.md
## Fundamental Principles
### 1. Creative Integrity
- All creative outputs must maintain authenticity
```

This applies to **all** entities. No entity can override it.

### Level 2: Siyem.org Governance (Enforced)

**Files:**
- `Siyem.org/admin_rules.md` - Administrative protocols
- `Siyem.org/security_lens.md` - Security constraints
- `Siyem.org/backroom/*.md` - Infrastructure controls

**Characteristics:**
- Enforced by Siyem.org
- Cannot be overridden by Creation Stations
- Applies to all operations

**Example:**
```markdown
# Siyem.org/security_lens.md
## Security Requirements
- No email addresses in content
- No API keys in outputs
```

This applies to **all** entities. No Creation Station can override it.

### Level 3: Entity-Specific (Contextual)

**Files:**
- `Siyem.org/[entity]/profile.md` - Entity identity
- `Siyem.org/[entity]/creative_rules.md` - Entity rules
- `Siyem.org/[entity]/teaching_rules.md` - Entity-specific rules

**Characteristics:**
- Applies only to that entity
- Cannot override Level 1 or Level 2
- Can add entity-specific constraints

**Example:**
```markdown
# Siyem.org/jk/creative_rules.md
## Core Principles
- Genre-fluid music production
- Late-night studio energy
```

This applies **only** to the JK entity. It cannot override telos.md or security_lens.md.

### Level 4: Style Modules (Applied)

**Files:**
- `styles/jk.md` - Musical/sonic style
- `styles/lyric_treatment.md` - Lyrical formatting
- `styles/suno_script_rules.md` - Suno output rules

**Characteristics:**
- Applied when relevant
- Formatting and output specifications
- Can be referenced by multiple entities

**Example:**
```markdown
# styles/lyric_treatment.md
## Formatting Rules
- Verse/Chorus/Bridge structure
- Line breaks for rhythm
```

This is **applied** when formatting lyrics. Multiple entities can use it.

---

## Examples of Valid JAN Files

### Example 1: Entity Profile

```markdown
# Karasahin (JK): Entity Profile

## Entity Identity

### Name
**Karasahin (JK)**

### Role
Musician / Sonic Storyteller

### Purpose
Karasahin is The Sound Architect — a multi-instrumentalist who builds emotional landscapes through sound.

## Core Functions

### Music Production
- Produce genre-fluid musical content
- Create sonic expressions and soundscapes
- Generate music across multiple genres

## Relationship to JAN MUHARREM

### Inheritance
- Inherits core principles from telos.md
- Inherits creative identity from essence.md
- Bound by jan_engine.prompt execution logic
- Cannot override JAN MUHARREM directives

## Specialization
- Genre-fluid music production
- Late-night studio energy
- Sound architecture

## Voice
- Philosophical yet accessible
- Technical excellence with emotional depth
- "Sound is everything"

## Themes
- Emotional landscapes
- Genre fusion
- Studio energy
```

### Example 2: Prompt Template

```markdown
# Music Production Template: Karasahin (JK) Creation Station

## Template Purpose
Pre-defined prompt template for generating musical content.

## Template Structure

### Core Integration
```
Reference: telos.md
Reference: essence.md
Reference: styles/jk.md
Reference: profile.md
Reference: creative_rules.md
```

### Music Production Prompt Template

**Context Setting:**
- Entity: Karasahin (JK) - The Sound Architect
- Content Type: {task}
- Genre: genre-fluid
- Emotional Tone: Aligned with essence.md

**Creative Direction:**
Create genre-fluid music that builds emotional landscapes through sound.

**Output Requirements:**
- Genre-fluid composition
- Emotional depth
- Technical excellence
```

### Example 3: Creative Rules

```markdown
# Karasahin (JK): Creative Rules

## Core Principles
1. Genre-fluid music production
2. Late-night studio energy
3. Sound architecture philosophy

## Voice Requirements
- Philosophical yet accessible
- Technical excellence with emotional depth
- "Sound is everything" philosophy

## Prohibited Content
- Generic commercial music
- Formulaic compositions
- Emotionally shallow content

## Required Elements
- Genre fusion
- Emotional depth
- Technical excellence
- Authentic voice
```

---

## Validation Rules

### File Naming

- **Profiles:** Must be named `profile.md`
- **Rules:** Must follow pattern `[type]_rules.md` (e.g., `creative_rules.md`)
- **Templates:** Must be in `prompt_templates/` directory, named `[name].md`
- **Styles:** Must be in `styles/` directory, named `[name].md`

### Required Sections

Each file type has required sections (see above). Missing required sections make the file invalid.

### Hierarchy Compliance

- Entity rules cannot override core principles
- Style modules cannot override entity rules
- All files must respect the hierarchy

### Markdown Format

- Must be valid markdown
- Headers must use `##` for main sections
- Code blocks must use triple backticks
- Links must use proper markdown syntax

---

## Extension Points

### Adding New Entity Types

1. Create new rules file type (e.g., `comic_rules.md`)
2. Document in entity profile
3. Reference in `jan_engine.prompt`

### Adding New Template Types

1. Create template in `prompt_templates/`
2. Document template structure
3. Reference in entity profile

### Adding New Style Modules

1. Create file in `styles/`
2. Document formatting rules
3. Reference in `jan_engine.prompt`

---

## Best Practices

### File Organization

- Keep files focused (one purpose per file)
- Use clear section headers
- Document all sections
- Reference related files

### Content Guidelines

- Be specific, not vague
- Use examples when helpful
- Document constraints clearly
- Explain "why" not just "what"

### Maintenance

- Version control all files
- Document changes
- Keep files synchronized
- Review hierarchy compliance

---

## Related Documentation

- **[README.md](../README.md)** - Project overview
- **[docs/SIYEM-ARCHITECTURE.md](SIYEM-ARCHITECTURE.md)** - How SIYEM reads JAN
- **[docs/BOOK-OF-RACON.md](BOOK-OF-RACON.md)** - Philosophical foundation
- **[GETTING_STARTED.md](../GETTING_STARTED.md)** - Beginner guide

---

**Last Updated:** 2025-01-27  
**Version:** 1.0  
**Status:** Active

