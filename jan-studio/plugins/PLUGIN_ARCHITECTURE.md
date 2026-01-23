# JAN Plugin Architecture

**Complete plugin system for extending JAN functionality.**

---

## Overview

The JAN plugin system allows developers to extend JAN Studio with:

- **AI Service Plugins** - New LLM providers
- **Output Format Plugins** - Custom output formats
- **Validation Plugins** - Custom validation rules
- **Integration Plugins** - External API integrations

---

## Plugin Interface

### Base Class: `JANPlugin`

All plugins inherit from `JANPlugin`:

```python
class JANPlugin(ABC):
    def name(self) -> str
    def version(self) -> str
    def plugin_type(self) -> PluginType
    def description(self) -> str
    def author(self) -> str
    def dependencies(self) -> List[str]
    def permissions(self) -> List[str]
    def validate_config(self) -> tuple[bool, Optional[str]]
    def initialize(self) -> bool
    def cleanup(self)
```

### Plugin Types

1. **AIServicePlugin** - AI service integration
2. **OutputFormatPlugin** - Output formatting
3. **ValidatorPlugin** - Content validation
4. **IntegrationPlugin** - External service integration

---

## Directory Structure

```
plugins/
├── base.py                    # Base plugin classes
├── loader.py                  # Plugin loader
├── manager.py                 # Plugin manager
├── README.md                  # Documentation
├── ai-services/               # AI service plugins
│   └── openai-plugin/
│       ├── plugin.json
│       └── openai_plugin.py
├── output-formats/            # Output format plugins
│   └── json-format/
│       ├── plugin.json
│       └── json_plugin.py
├── validators/                # Validator plugins
│   └── length-validator/
│       ├── plugin.json
│       └── length_validator.py
├── integrations/              # Integration plugins
│   └── suno-integration/
│       ├── plugin.json
│       └── suno_plugin.py
└── examples/                  # Example plugins
    ├── ai-services/
    ├── output-formats/
    ├── validators/
    └── integrations/
```

---

## Plugin Manifest

**File:** `plugin.json`

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "author": "Your Name",
  "description": "Plugin description",
  "type": "ai-service",
  "entry_point": "plugin_file.py",
  "dependencies": [
    "package>=1.0.0"
  ],
  "permissions": [
    "api_key",
    "file_access"
  ],
  "config": {
    "api_key": "",
    "setting": "value"
  },
  "requires": {
    "jan_version": ">=1.0.0"
  }
}
```

### Required Fields

- `name` - Unique plugin identifier
- `version` - Semantic version
- `entry_point` - Python file with plugin class
- `type` - Plugin type: `ai-service`, `output-format`, `validator`, `integration`

### Optional Fields

- `author` - Author name
- `description` - Plugin description
- `dependencies` - Required Python packages
- `permissions` - Required permissions
- `config` - Default configuration
- `requires` - Version requirements

---

## Plugin Types

### 1. AI Service Plugins

**Base Class:** `AIServicePlugin`

**Purpose:** Integrate new LLM providers

**Required Methods:**
- `generate(prompt, persona, context, options)` - Generate content
- `supports_streaming()` - Check streaming support
- `stream_generate()` - Stream content (optional)

**Example:**
```python
class MyAIPlugin(AIServicePlugin):
    def generate(self, prompt, persona, context=None, options=None):
        # Call your AI service
        return {"content": "..."}
```

### 2. Output Format Plugins

**Base Class:** `OutputFormatPlugin`

**Purpose:** Add custom output formats

**Required Methods:**
- `format_name()` - Return format identifier
- `process(content, persona, context)` - Format content
- `validate(content)` - Validate format (optional)

**Example:**
```python
class MyFormatPlugin(OutputFormatPlugin):
    def format_name(self):
        return "my-format"
    
    def process(self, content, persona, context=None):
        # Format content
        return {"formatted_content": "..."}
```

### 3. Validator Plugins

**Base Class:** `ValidatorPlugin`

**Purpose:** Custom validation rules

**Required Methods:**
- `rule_name()` - Return rule identifier
- `validate(output, rules, persona, context)` - Validate content

**Example:**
```python
class MyValidatorPlugin(ValidatorPlugin):
    def rule_name(self):
        return "my-rule"
    
    def validate(self, output, rules, persona, context=None):
        # Validate content
        return (True, [], [])
```

### 4. Integration Plugins

**Base Class:** `IntegrationPlugin`

**Purpose:** External API integrations

**Required Methods:**
- `service_name()` - Return service name
- `process(persona, prompt, context)` - Process request

**Example:**
```python
class MyIntegrationPlugin(IntegrationPlugin):
    def service_name(self):
        return "My Service"
    
    def process(self, persona, prompt, context=None):
        # Call external API
        return {"result": "..."}
```

---

## Plugin Loading

### Automatic Discovery

Plugins are automatically discovered from:
- `plugins/ai-services/`
- `plugins/output-formats/`
- `plugins/validators/`
- `plugins/integrations/`

### Loading Process

1. **Discovery** - Find all `plugin.json` files
2. **Validation** - Check manifest structure
3. **Import** - Load plugin module
4. **Instantiation** - Create plugin instance
5. **Configuration** - Apply config and validate
6. **Initialization** - Call `initialize()`

### Usage

```python
from plugins.loader import PluginLoader

loader = PluginLoader()
loader.load_all_plugins()

# Get plugin
plugin = loader.get_plugin("openai")

# Get plugins by type
ai_services = loader.get_plugins_by_type(PluginType.AI_SERVICE)
```

---

## Plugin Manager

High-level interface for using plugins:

```python
from plugins.manager import get_manager

manager = get_manager()

# Generate with AI
result = manager.generate_with_ai(
    prompt="Write a story",
    persona={"name": "storyteller"},
    ai_service="openai"
)

# Format output
formatted = manager.format_output(
    content="Some content",
    format_name="json",
    persona={"name": "storyteller"}
)

# Validate output
validation = manager.validate_output(
    output="Generated content",
    rules={"length": {"min_length": 100}},
    persona={"name": "storyteller"}
)

# Call integration
result = manager.call_integration(
    service_name="Suno AI",
    persona={"name": "music-producer"},
    prompt="Generate music"
)
```

---

## Creating a Plugin

### Step 1: Create Directory

```bash
mkdir -p plugins/ai-services/my-plugin
cd plugins/ai-services/my-plugin
```

### Step 2: Create Plugin Class

```python
# my_plugin.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plugins.base import AIServicePlugin

class MyAIPlugin(AIServicePlugin):
    def name(self) -> str:
        return "my-ai"
    
    def version(self) -> str:
        return "1.0.0"
    
    def generate(self, prompt, persona, context=None, options=None):
        # Your implementation
        return {"content": "Generated content"}
```

### Step 3: Create Manifest

```json
{
  "name": "my-ai",
  "version": "1.0.0",
  "author": "Your Name",
  "description": "My AI service plugin",
  "type": "ai-service",
  "entry_point": "my_plugin.py",
  "dependencies": [],
  "permissions": [],
  "config": {}
}
```

### Step 4: Test Plugin

```python
from plugins.loader import PluginLoader

loader = PluginLoader()
plugin = loader.load_plugin("plugins/ai-services/my-plugin")
result = plugin.generate("Test prompt", {})
```

---

## Example Plugins

See `examples/` directory:

- **OpenAI Plugin** - `examples/ai-services/openai_plugin.py`
- **JSON Format** - `examples/output-formats/json_plugin.py`
- **Length Validator** - `examples/validators/length_validator.py`
- **Suno Integration** - `examples/integrations/suno_plugin.py`

---

## Plugin Lifecycle

1. **Discovery** - Loader finds plugin.json
2. **Loading** - Import plugin module
3. **Instantiation** - Create plugin instance
4. **Configuration** - Apply and validate config
5. **Initialization** - Call `initialize()`
6. **Enable** - Plugin ready for use
7. **Usage** - Plugin methods called
8. **Cleanup** - Call `cleanup()` on unload

---

## Best Practices

1. **Error Handling** - Always handle errors gracefully
2. **Configuration** - Validate in `validate_config()`
3. **Dependencies** - List all required packages
4. **Permissions** - Request only needed permissions
5. **Versioning** - Use semantic versioning
6. **Documentation** - Document plugin behavior
7. **Testing** - Test before distribution

---

## Status

✅ **Base plugin interface**  
✅ **Plugin loader**  
✅ **Plugin manager**  
✅ **Example plugins**  
✅ **Documentation**  
✅ **Directory structure**

**Ready for:** Plugin development and distribution

---

**Last Updated:** 2025-01-27  
**Version:** 1.0.0

