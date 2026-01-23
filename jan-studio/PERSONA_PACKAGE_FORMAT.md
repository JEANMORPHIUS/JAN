# JAN Persona Package Format (.janpkg)

**Standard format for sharing and distributing JAN personas.**

---

## Package Format

### File Extension
`.janpkg` - A ZIP archive containing persona files and metadata

### Structure

```
persona-name.janpkg (ZIP)
├── manifest.json              # Package metadata
├── jan/                       # JAN markdown files
│   ├── profile.md
│   ├── creative_rules.md
│   └── prompt_templates/
│       └── *.md
├── examples/                  # Sample outputs
│   └── *.txt, *.md, etc.
├── README.md                  # Usage instructions
└── LICENSE                    # License file
```

---

## Manifest Format

**File:** `manifest.json`

```json
{
  "format_version": "1.0",
  "persona_name": "storyteller",
  "version": "1.0.0",
  "author": "Your Name",
  "description": "A creative writing persona...",
  "created_at": "2025-01-27T12:00:00",
  "jan_files": [
    "profile.md",
    "creative_rules.md",
    "prompt_templates/story_template.md"
  ],
  "examples": [
    "short_story_example.txt"
  ],
  "license": "CC-BY-4.0",
  "requires": {
    "jan_version": ">=1.0.0"
  }
}
```

### Required Fields

- `format_version` - Package format version (currently "1.0")
- `persona_name` - Name of the persona
- `version` - Semantic version (e.g., "1.0.0")
- `author` - Author name

### Optional Fields

- `description` - Persona description
- `created_at` - ISO timestamp
- `jan_files` - List of JAN file paths
- `examples` - List of example file paths
- `license` - License identifier (default: "CC-BY-4.0")
- `requires` - Version requirements
- `tags` - Array of tags
- `homepage` - Homepage URL
- `repository` - Repository URL

---

## Tools

### 1. pack_persona.py

**Purpose:** Create .janpkg file from persona directory

**Usage:**
```python
from pack_persona import pack_persona

output_path = pack_persona(
    persona_name="storyteller",
    output_path="storyteller.janpkg",
    author="John Doe",
    version="1.0.0"
)
```

**CLI:**
```bash
python pack_persona.py storyteller -o storyteller.janpkg -a "John Doe" -v 1.0.0
```

### 2. unpack_persona.py

**Purpose:** Install .janpkg file into JAN directory

**Usage:**
```python
from unpack_persona import install_persona, list_package_info

# Install
persona_name = install_persona("storyteller.janpkg", overwrite=False)

# Get info
info = list_package_info("storyteller.janpkg")
```

**CLI:**
```bash
python unpack_persona.py install storyteller.janpkg
python unpack_persona.py info storyteller.janpkg
```

### 3. validate_persona.py

**Purpose:** Validate persona directory or .janpkg file

**Usage:**
```python
from validate_persona import validate_persona, validate_package

# Validate directory
is_valid, errors, warnings = validate_persona("storyteller")

# Validate package
is_valid, errors, warnings = validate_package("storyteller.janpkg")
```

**CLI:**
```bash
python validate_persona.py storyteller
python validate_persona.py storyteller.janpkg
```

### 4. jan_cli.py

**Purpose:** Unified CLI interface

**Commands:**
- `jan persona list` - List installed personas
- `jan persona pack <name>` - Pack persona
- `jan persona install <package>` - Install package
- `jan persona info <package>` - Show package info
- `jan persona validate <target>` - Validate persona/package

---

## CLI Commands

### List Personas

```bash
jan persona list
```

Lists all installed personas with their roles.

### Pack Persona

```bash
jan persona pack <persona_name> [options]
```

**Options:**
- `-o, --output PATH` - Output .janpkg file path
- `-a, --author NAME` - Author name
- `-v, --version VERSION` - Version number

**Example:**
```bash
jan persona pack storyteller -o storyteller-v1.0.janpkg -a "Jane Smith" -v 1.0.0
```

### Install Package

```bash
jan persona install <package.janpkg> [--overwrite]
```

**Example:**
```bash
jan persona install storyteller.janpkg
jan persona install storyteller.janpkg --overwrite
```

### Package Info

```bash
jan persona info <package.janpkg>
```

Shows package information without installing.

### Validate

```bash
jan persona validate <persona_name_or_package>
```

Validates a persona directory or .janpkg file.

---

## Validation Rules

### Required Files

- `jan/profile.md` - Must contain:
  - `## Entity Identity`
  - `### Name`
  - `### Role`
  - `### Purpose`
- `jan/creative_rules.md` - Must be non-empty

### Package Validation

- Valid ZIP file
- Contains `manifest.json` with required fields
- Contains at least one JAN markdown file
- Contains `jan/profile.md` and `jan/creative_rules.md`

---

## Integration

### With JAN Studio

1. **Create persona** in JAN Studio
2. **Validate** with `jan persona validate <name>`
3. **Pack** with `jan persona pack <name>`
4. **Share** .janpkg file

### With Marketplace

1. **Pack persona** into .janpkg
2. **Submit** to marketplace (uploads .janpkg)
3. **Download** from marketplace (gets .janpkg)
4. **Install** with `jan persona install`

---

## File Structure

```
jan-studio/tools/
├── pack_persona.py          # Create .janpkg files
├── unpack_persona.py        # Install .janpkg files
├── validate_persona.py      # Validate personas/packages
├── jan_cli.py              # CLI interface
├── setup_cli.py            # Setup CLI command
├── example_manifest.json    # Example manifest
├── README.md               # Detailed documentation
└── QUICK_REFERENCE.md       # Quick reference
```

---

## Workflow Examples

### Creating a Package

```bash
# 1. Create/edit persona in JAN Studio
# 2. Validate
jan persona validate storyteller

# 3. Pack
jan persona pack storyteller \
  -o storyteller-v1.0.janpkg \
  -a "Your Name" \
  -v 1.0.0

# 4. Verify package
jan persona info storyteller-v1.0.janpkg
```

### Installing a Package

```bash
# 1. Download .janpkg file
# 2. Check info
jan persona info storyteller.janpkg

# 3. Validate
jan persona validate storyteller.janpkg

# 4. Install
jan persona install storyteller.janpkg

# 5. Verify installation
jan persona list
```

### Sharing Workflow

```bash
# Author workflow
jan persona pack my-persona -o my-persona.janpkg
# Share my-persona.janpkg

# User workflow
jan persona install my-persona.janpkg
# Use in JAN Studio
```

---

## Status

✅ **Package format defined**  
✅ **Packing tool implemented**  
✅ **Unpacking tool implemented**  
✅ **Validation tool implemented**  
✅ **CLI interface complete**  
✅ **Documentation complete**

**Ready for:** Package creation and distribution

---

**Last Updated:** 2025-01-27  
**Format Version:** 1.0

