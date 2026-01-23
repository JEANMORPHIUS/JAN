# JAN CLI Quick Reference

**Quick reference for persona package management.**

---

## Commands

### List Installed Personas

```bash
jan persona list
```

### Pack a Persona

```bash
jan persona pack <name> [-o output.janpkg] [-a author] [-v version]
```

**Examples:**
```bash
jan persona pack storyteller
jan persona pack storyteller -o storyteller-v1.0.janpkg
jan persona pack storyteller -a "John Doe" -v 1.0.0
```

### Install a Package

```bash
jan persona install <package.janpkg> [--overwrite]
```

**Examples:**
```bash
jan persona install storyteller.janpkg
jan persona install storyteller.janpkg --overwrite
```

### View Package Info

```bash
jan persona info <package.janpkg>
```

**Example:**
```bash
jan persona info storyteller.janpkg
```

### Validate Persona/Package

```bash
jan persona validate <name_or_package>
```

**Examples:**
```bash
jan persona validate storyteller
jan persona validate storyteller.janpkg
```

---

## Package Structure

```
persona-name.janpkg (ZIP)
├── manifest.json
├── jan/
│   ├── profile.md
│   ├── creative_rules.md
│   └── prompt_templates/
├── examples/
├── README.md
└── LICENSE
```

---

## Workflow Examples

### Create and Share a Persona

```bash
# 1. Create/edit persona in JAN Studio
# 2. Validate it
jan persona validate storyteller

# 3. Pack it
jan persona pack storyteller -o storyteller.janpkg -a "Your Name"

# 4. Share the .janpkg file
```

### Install a Shared Persona

```bash
# 1. Download .janpkg file
# 2. Check info
jan persona info storyteller.janpkg

# 3. Install
jan persona install storyteller.janpkg

# 4. Verify
jan persona list
```

---

## Common Issues

### "Persona directory not found"
- Check persona exists: `jan persona list`
- Verify JAN_ROOT environment variable

### "Package already exists"
- Use `--overwrite` flag: `jan persona install package.janpkg --overwrite`

### "Invalid package"
- Validate first: `jan persona validate package.janpkg`
- Check package structure

---

## Tips

- Always validate before packing
- Include examples in your packages
- Use semantic versioning (1.0.0, 1.1.0, etc.)
- Add README.md with usage instructions
- Specify license in manifest.json

