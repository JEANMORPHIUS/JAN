# JAN Plugin Architecture

**Extensible plugin system for JAN Studio.**

---

## Plugin Types

### 1. AI Service Plugins

Integrate new LLM providers (OpenAI, Anthropic, local models, etc.)

**Base Class:** `AIServicePlugin`

**Required Methods:**
- `generate(prompt, persona, context, options)` - Generate content
- `supports_streaming()` - Check streaming support
- `stream_generate()` - Stream content (optional)

### 2. Output Format Plugins

Add custom output formats (JSON, XML, HTML, etc.)

**Base Class:** `OutputFormatPlugin`

**Required Methods:**
- `format_name()` - Return format identifier
- `process(content, persona, context)` - Format content
- `validate(content)` - Validate format (optional)

### 3. Validator Plugins

Custom validation rules

**Base Class:** `ValidatorPlugin`

**Required Methods:**
- `rule_name()` - Return rule identifier
- `validate(output, rules, persona, context)` - Validate content

### 4. Integration Plugins

External API integrations (Suno, ElevenLabs, etc.)

**Base Class:** `IntegrationPlugin`

**Required Methods:**
- `service_name()` - Return service name
- `process(persona, prompt, context)` - Process request

---

## Plugin Structure

```
plugins/
├── ai-services/
│   └── my-ai-plugin/
│       ├── plugin.json
│       └── my_ai_plugin.py
├── output-formats/
│   └── my-format/
│       ├── plugin.json
│       └── my_format.py
├── validators/
│   └── my-validator/
│       ├── plugin.json
│       └── my_validator.py
└── integrations/
    └── my-integration/
        ├── plugin.json
        └── my_integration.py
```

---

## Plugin Manifest (plugin.json)

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "author": "Your Name",
  "description": "Plugin description",
  "type": "ai-service|output-format|validator|integration",
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

- `name` - Unique plugin name
- `version` - Plugin version
- `entry_point` - Python file with plugin class
- `type` - Plugin type

### Optional Fields

- `author` - Author name
- `description` - Plugin description
- `dependencies` - Required Python packages
- `permissions` - Required permissions
- `config` - Default configuration
- `requires` - JAN version requirements

---

## Creating a Plugin

### 1. Create Plugin Directory

```bash
mkdir -p plugins/ai-services/my-plugin
cd plugins/ai-services/my-plugin
```

### 2. Create Plugin Class

```python
# my_plugin.py
from plugins.base import AIServicePlugin

class MyAIPlugin(AIServicePlugin):
    def name(self) -> str:
        return "my-ai"
    
    def version(self) -> str:
        return "1.0.0"
    
    def generate(self, prompt, persona, context=None, options=None):
        # Your implementation
        return {"content": "..."}
```

### 3. Create Manifest

```json
{
  "name": "my-ai",
  "version": "1.0.0",
  "type": "ai-service",
  "entry_point": "my_plugin.py"
}
```

### 4. Load Plugin

```python
from plugins.loader import PluginLoader

loader = PluginLoader()
loader.load_all_plugins()
plugin = loader.get_plugin("my-ai")
```

---

## Using Plugins

### AI Service

```python
from plugins.manager import get_manager

manager = get_manager()
result = manager.generate_with_ai(
    prompt="Write a story",
    persona={"name": "storyteller"},
    ai_service="openai"
)
```

### Output Format

```python
formatted = manager.format_output(
    content="Some content",
    format_name="json",
    persona={"name": "storyteller"}
)
```

### Validation

```python
validation = manager.validate_output(
    output="Generated content",
    rules={"length": {"min_length": 100}},
    persona={"name": "storyteller"}
)
```

### Integration

```python
result = manager.call_integration(
    service_name="Suno AI",
    persona={"name": "music-producer"},
    prompt="Generate music"
)
```

---

## Example Plugins

See `examples/` directory for complete examples:

- `ai-services/openai_plugin.py` - OpenAI integration
- `output-formats/json_plugin.py` - JSON formatting
- `validators/length_validator.py` - Length validation
- `integrations/suno_plugin.py` - Suno AI integration

---

## Plugin Lifecycle

1. **Discovery** - Loader finds plugin.json files
2. **Loading** - Import plugin module
3. **Initialization** - Create plugin instance
4. **Configuration** - Validate and apply config
5. **Enable** - Plugin ready for use
6. **Usage** - Plugin methods called
7. **Cleanup** - Plugin resources released

---

## Best Practices

1. **Error Handling** - Always handle errors gracefully
2. **Configuration** - Validate config in `validate_config()`
3. **Dependencies** - List all required packages
4. **Permissions** - Request only needed permissions
5. **Versioning** - Use semantic versioning
6. **Documentation** - Document plugin behavior
7. **Testing** - Test plugins before distribution

---

## Status

✅ **Base plugin interface**  
✅ **Plugin loader**  
✅ **Plugin manager**  
✅ **Example plugins**  
✅ **Documentation**

**Ready for:** Plugin development and distribution

---

**Last Updated:** 2025-01-27  
**Version:** 1.0.0

