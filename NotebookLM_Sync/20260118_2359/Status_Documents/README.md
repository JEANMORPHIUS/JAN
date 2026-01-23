# JAN MUHARREM Meta-Life Build

**A markdown-based creative identity system that separates "what you are" from "how you work."**

---

## What Problem Does This Solve?

Most creative systems mix identity (who you are, your voice, your rules) with implementation (the code that makes things work). This creates problems:

- **Identity changes require code changes** - Want to adjust your creative voice? Edit Python files.
- **Identity is locked in code** - Your creative rules are buried in functions, hard to version control, hard to share.
- **Multiple implementations can't share identity** - If you rebuild your system, you lose your identity.
- **Non-technical creators can't edit rules** - Only developers can modify creative constraints.

**JAN solves this by separating creative identity (markdown) from technical implementation (code).**

### The Core Insight

**JAN** = The "soul" (markdown files defining identity, rules, voice, templates)  
**SIYEM** = The "body" (Python code, services, APIs that execute operations)

This separation means:
- ✅ Edit your creative identity without touching code
- ✅ Version control your identity separately from implementation
- ✅ Share identity across multiple implementations
- ✅ Let non-technical creators edit rules and templates
- ✅ Rebuild your system without losing your identity

---

## Core Concepts

### JAN vs SIYEM Separation

| Aspect | JAN (Documentation/Configuration) | SIYEM (Implementation) |
|--------|----------------------------------|------------------------|
| **Location** | `S:\JAN\` | `S:\SIYEM\` |
| **Format** | Markdown files (`.md`) | Python code, JSON, React |
| **Purpose** | Define identity, rules, templates | Execute operations, serve APIs |
| **Editable By** | Anyone (markdown is human-readable) | Developers (requires coding) |
| **Version Control** | Git-friendly markdown | Code repositories |
| **Example** | `profile.md` defines entity identity | `entity_router.py` detects entities |

### The Rule Hierarchy

JAN uses a 4-level hierarchy where higher levels cannot be overridden:

```
Level 1: JAN MUHARREM Core (Non-negotiable)
├── telos.md - Purpose, principles, boundaries
├── essence.md - Creative fingerprint, tone
└── jan_engine.prompt - Execution logic

Level 2: Siyem.org Governance (Enforced)
├── admin_rules.md - Administrative protocols
├── security_lens.md - Security constraints
└── backroom/*.md - Infrastructure controls

Level 3: Entity-Specific (Contextual)
├── profile.md - Entity identity
└── creative_rules.md - Entity-specific rules

Level 4: Style Modules (Applied)
└── styles/*.md - Formatting and output rules
```

**Key Principle:** Lower levels inherit from higher levels. Entity rules cannot override core principles.

### Creation Stations

Each entity (Jean, Karasahin, Ramiz, Pierre, Siyem Media) is a **Creation Station** - an independent, modular creative station that:

- Inherits JAN's core principles automatically
- Has its own profile, rules, and prompt templates
- Operates within defined boundaries
- Cannot override JAN core directives

---

## 🚀 Quick Installation

**Get JAN Studio running in 5 minutes:**

```bash
# 1. Clone the repository
git clone <repository-url>
cd JAN

# 2. Set up environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 3. Install dependencies
cd jan-studio
pip install -r requirements.txt
cd frontend
npm install

# 4. Start backend (Terminal 1)
cd ../backend
python -m uvicorn jan-studio-api-example:router --host 127.0.0.1 --port 8000

# 5. Start frontend (Terminal 2)
cd ../frontend
npm run dev

# 6. Open http://localhost:3000
```

**📖 Full installation guide:** See [INSTALL.md](INSTALL.md)  
**⚡ 5-minute quickstart:** See [QUICKSTART.md](QUICKSTART.md)

---

## Quick Start Guide

### 1. Understand the Structure

```
S:\JAN\
├── telos.md                    # Core purpose and principles
├── essence.md                  # Creative fingerprint
├── jan_engine.prompt          # Execution logic
├── Siyem.org\                 # Entity definitions
│   ├── jean_mahram\          # Jean Creation Station
│   ├── jk\                    # Karasahin Creation Station
│   ├── pierre_pressure\       # Pierre Creation Station
│   ├── uncle_ray_ramiz\       # Ramiz Creation Station
│   └── siyem_media\           # Siyem Media Creation Station
└── styles\                     # Style modules
```

### 2. Read the Core Files

Start with these three files to understand JAN's identity:

1. **`telos.md`** - What is JAN's purpose? What are the core principles?
2. **`essence.md`** - What is JAN's creative fingerprint? What is the voice?
3. **`jan_engine.prompt`** - How does JAN execute? What is the workflow?

### 3. Explore a Creation Station

Pick an entity (e.g., `jk/` for Karasahin) and read:

1. **`profile.md`** - Who is this entity? What is their purpose?
2. **`creative_rules.md`** - What are their creative guidelines?
3. **`prompt_templates/*.md`** - What templates do they use?

### 4. Understand Integration

Read **`docs/JAN-SPECIFICATION.md`** to understand:
- How JAN files are structured
- What makes a valid JAN file
- How the rule hierarchy works

Read **`docs/SIYEM-ARCHITECTURE.md`** to understand:
- How SIYEM reads JAN files
- How services integrate with JAN
- How to extend the system

### 5. Set Up SIYEM Integration

If you want to use JAN with SIYEM:

1. **Install dependencies:**
   ```bash
   pip install markdown PyYAML python-frontmatter
   ```

2. **Configure paths:**
   - Set `JAN_ROOT` environment variable (default: `S:\JAN`)
   - Ensure SIYEM can access JAN files

3. **Use JAN services:**
   ```python
   from services.jan_integration import read_jan_profile, read_jan_template
   
   # Read entity profile
   profile = read_jan_profile("JEAN")
   
   # Read prompt template
   template = read_jan_template("JEAN", "storytelling_template")
   ```

See **`docs/SIYEM-ARCHITECTURE.md`** for complete integration guide.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    JAN MUHARREM (Root)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  telos.md    │  │  essence.md  │  │jan_engine.   │     │
│  │  (Purpose)   │  │  (Identity)   │  │  prompt      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Inherits
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  Siyem.org (Governance)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │admin_rules.md│  │security_lens. │  │  backroom/  │     │
│  │              │  │     md       │  │  (Controls)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Contains
                            ▼
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ jean_mahram/ │  │     jk/      │  │ pierre_      │
│  (Station)   │  │  (Station)   │  │ pressure/    │
│              │  │              │  │  (Station)   │
│ profile.md   │  │ profile.md   │  │ profile.md   │
│ rules.md     │  │ rules.md     │  │ rules.md     │
│ templates/   │  │ templates/   │  │ templates/   │
└──────────────┘  └──────────────┘  └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            │ Applied to
                            ▼
                    ┌──────────────┐
                    │  styles/     │
                    │  (Modules)   │
                    └──────────────┘
                            │
                            │ Read by
                            ▼
                    ┌──────────────┐
                    │    SIYEM     │
                    │ (Implementation)│
                    │              │
                    │ Services:    │
                    │ - jan_integration│
                    │ - jan_validator │
                    │ - jan_engine    │
                    └──────────────┘
```

**Flow:**
1. JAN defines identity in markdown
2. SIYEM reads JAN files via `jan_integration.py`
3. Services apply rules via `jan_engine.py`
4. Outputs validated via `jan_validator.py`
5. Governance enforced via `governance_enforcer.py`

---

## Documentation Structure

### Essential Reading

- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete beginner tutorial
- **[GLOSSARY.md](GLOSSARY.md)** - All terminology defined
- **[docs/JAN-SPECIFICATION.md](docs/JAN-SPECIFICATION.md)** - JAN file format specification
- **[docs/SIYEM-ARCHITECTURE.md](docs/SIYEM-ARCHITECTURE.md)** - SIYEM integration guide
- **[docs/BOOK-OF-RACON.md](docs/BOOK-OF-RACON.md)** - Philosophical foundation

### Core Files

- **`telos.md`** - Core purpose, principles, boundaries
- **`essence.md`** - Creative fingerprint and identity
- **`jan_engine.prompt`** - Execution logic
- **`CREATION_STATIONS_README.md`** - Creation Station details

### Integration

- **`JAN_SIYEM_INTEGRATION.md`** - Integration overview
- **`SIYEM_JAN_INTEGRATION_PROMPT.md`** - Implementation prompt
- **`SIYEM_READINESS_STATUS.md`** - Integration status

### Reference

- **`WORKFLOW_EXAMPLES.md`** - Real-world usage examples
- **`API_REFERENCE.md`** - API documentation
- **`TROUBLESHOOTING_GUIDE.md`** - Common problems and solutions

---

## Key Features

### ✅ Markdown-Based Identity

All creative identity is defined in human-readable markdown:
- Entity profiles
- Creative rules
- Prompt templates
- Governance rules
- Style modules

### ✅ Rule Hierarchy

4-level hierarchy ensures consistency:
- Core principles (non-negotiable)
- Governance rules (enforced)
- Entity rules (contextual)
- Style modules (applied)

### ✅ Separation of Concerns

- **JAN** = What you are (identity, rules, voice)
- **SIYEM** = How you work (code, services, APIs)

### ✅ Version Control Friendly

Markdown files are:
- Human-readable
- Git-friendly
- Easy to diff
- Easy to merge

### ✅ Extensible

- Add new Creation Stations
- Add new style modules
- Add new governance rules
- All without touching core code

---

## Philosophy

JAN is grounded in **The Book of Racon** - 40 laws across four volumes:

- **Loyalty (Laws 1-10)**: The table never lies. Your word is your bond.
- **Silence (Laws 11-20)**: Wisdom lives in the quiet. Listen before you speak.
- **Respect (Laws 21-30)**: Honor your elders. Know your place.
- **War (Laws 31-40)**: Finish what you begin. Protect what is yours.

These laws inform every principle in `telos.md` and guide all creative work.

See **[docs/BOOK-OF-RACON.md](docs/BOOK-OF-RACON.md)** for complete explanation.

---

## Project Status

**Status:** Active Development  
**Version:** 2.0  
**Last Updated:** 2025-01-27

### Current State

- ✅ JAN documentation complete
- ✅ Core services implemented (jan_integration, jan_validator, jan_engine)
- ✅ API endpoints implemented
- ⚠️ Service integration pending (services need to use JAN files)
- ⚠️ Testing pending

See **`SIYEM_READINESS_STATUS.md`** for detailed status.

---

## Contributing

### Adding a New Creation Station

1. Create folder: `Siyem.org/[entity_name]/`
2. Add `profile.md` with entity identity
3. Add rules file (`creative_rules.md`, `teaching_rules.md`, etc.)
4. Create `prompt_templates/` folder with templates
5. Add `style_overrides.md` (optional)
6. Update documentation

### Adding a Style Module

1. Create file: `styles/[module_name].md`
2. Define module purpose and scope
3. Reference `essence.md` for alignment
4. Document integration points
5. Update `jan_engine.prompt` if needed

### Modifying Core Files

**Warning:** Core files (`telos.md`, `essence.md`, `jan_engine.prompt`) affect the entire system. Changes should be:
- Well-documented
- Backward-compatible when possible
- Reviewed for system-wide impact

---

## Installation & Setup

- **📖 Full Installation Guide:** [INSTALL.md](INSTALL.md)
- **⚡ Quick Start (5 min):** [QUICKSTART.md](QUICKSTART.md)
- **🐳 Docker Setup:** See `docker-compose.yml` and Dockerfiles in `jan-studio/`

### Prerequisites

- Python 3.8+
- Node.js 18+
- Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Quick Install

```bash
git clone <repository-url>
cd JAN
cp .env.example .env  # Add your API keys
cd jan-studio
pip install -r requirements.txt
cd frontend && npm install
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete beginner tutorial
- **[INSTALL.md](INSTALL.md)** - Detailed installation guide
- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete API documentation
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[docs/](docs/)** - Technical specifications

---

**Remember:** JAN is the soul. SIYEM is the body. Keep them separate, and you can rebuild the body without losing the soul.
