# JAN Persona Package Tools

**Standard format for sharing JAN personas (.janpkg)**

---

## Package Format

### Structure

A `.janpkg` file is a ZIP archive with the following structure:

```
persona-name.janpkg/
├── manifest.json          # Package metadata
├── jan/                  # JAN markdown files
│   ├── profile.md
│   ├── creative_rules.md
│   └── prompt_templates/
│       └── ...
├── examples/             # Sample outputs
│   └── ...
├── README.md             # Usage instructions
└── LICENSE               # License file
```

### manifest.json

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

---

## CLI Commands

### List Personas

```bash
jan persona list
```

Lists all installed personas.

### Pack Persona

```bash
jan persona pack <persona_name> [options]
```

**Options:**
- `-o, --output PATH` - Output .janpkg file path
- `-a, --author NAME` - Author name
- `-v, --version VERSION` - Version number (default: 1.0.0)

**Example:**
```bash
jan persona pack storyteller -o storyteller-v1.0.janpkg -a "John Doe" -v 1.0.0
```

### Install Persona

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

**Example:**
```bash
jan persona info storyteller.janpkg
```

### Validate

```bash
jan persona validate <persona_name_or_package>
```

Validates a persona directory or .janpkg file.

**Example:**
```bash
jan persona validate storyteller
jan persona validate storyteller.janpkg
```

---

## Python Tools

### pack_persona.py

```python
from pack_persona import pack_persona

# Pack a persona
output_path = pack_persona(
    persona_name="storyteller",
    output_path="storyteller.janpkg",
    author="John Doe",
    version="1.0.0"
)
```

### unpack_persona.py

```python
from unpack_persona import install_persona, list_package_info

# Install a package
persona_name = install_persona("storyteller.janpkg", overwrite=False)

# Get package info
info = list_package_info("storyteller.janpkg")
print(info["manifest"])
```

### validate_persona.py

```python
from validate_persona import validate_persona, validate_package

# Validate persona directory
is_valid, errors, warnings = validate_persona("storyteller")

# Validate package
is_valid, errors, warnings = validate_package("storyteller.janpkg")
```

---

## Package Requirements

### Required Files

- `jan/profile.md` - Persona profile
- `jan/creative_rules.md` - Creative rules

### Optional Files

- `jan/prompt_templates/*.md` - Prompt templates
- `examples/*` - Example outputs
- `README.md` - Usage instructions
- `LICENSE` - License file (defaults to CC-BY-4.0)

---

## Validation Rules

### Persona Directory

- Must exist in `JAN_ROOT/Siyem.org/`
- Must have `profile.md` with required sections:
  - `## Entity Identity`
  - `### Name`
  - `### Role`
  - `### Purpose`
- Must have `creative_rules.md` (non-empty)

### Package File

- Must be valid ZIP file
- Must contain `manifest.json` with:
  - `format_version`
  - `persona_name`
  - `version`
  - `author`
- Must contain at least one JAN markdown file
- Must contain `jan/profile.md` and `jan/creative_rules.md`

---

## Usage Examples

### Creating a Package

```bash
# Pack existing persona
jan persona pack storyteller -o storyteller-v1.0.janpkg

# Pack with metadata
jan persona pack storyteller \
  -o storyteller-v1.0.janpkg \
  -a "Jane Smith" \
  -v "1.0.0"
```

### Installing a Package

```bash
# Install package
jan persona install storyteller.janpkg

# Install with overwrite
jan persona install storyteller.janpkg --overwrite
```

### Validating

```bash
# Validate installed persona
jan persona validate storyteller

# Validate package before installing
jan persona validate storyteller.janpkg
```

### Checking Package Info

```bash
# View package details
jan persona info storyteller.janpkg
```

---

## Integration with Marketplace

Packages created with `jan persona pack` can be:

1. **Uploaded to marketplace** - Submit .janpkg files
2. **Shared directly** - Distribute .janpkg files
3. **Version controlled** - Track persona versions
4. **Validated** - Ensure completeness before sharing

---

## File Structure

```
jan-studio/tools/
├── pack_persona.py      # Create .janpkg files
├── unpack_persona.py    # Install .janpkg files
├── validate_persona.py # Validate personas/packages
├── jan_cli.py          # CLI interface
└── README.md           # This file
```

---

## Environment Variables

- `JAN_ROOT` - Root directory for JAN (default: `S:\JAN`)
- Personas are stored in `JAN_ROOT/Siyem.org/`

---

## Status

✅ **Package format defined**  
✅ **Packing tool implemented**  
✅ **Unpacking tool implemented**  
✅ **Validation tool implemented**  
✅ **CLI interface complete**

**Ready for:** Package creation and distribution

---

**Last Updated:** 2025-01-27  
**Version:** 1.0.0

