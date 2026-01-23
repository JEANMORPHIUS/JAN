# SIYEM Architecture

**Complete technical guide to SIYEM's architecture and JAN integration.**

---

## Overview

**SIYEM** (`S:\SIYEM\`) is the **implementation layer** that executes operations defined by JAN. It consists of:

- **Services** - Python modules that perform operations
- **API Endpoints** - FastAPI routes that expose functionality
- **Frontends** - React/HTML interfaces for user interaction
- **Data Files** - JSON configuration and entity data

**Key Principle:** SIYEM reads JAN files and executes operations according to JAN's rules.

---

## Service Architecture

### Core Services

#### `services/jan_integration.py`

**Purpose:** Read and parse JAN markdown files

**Key Functions:**

```python
def read_jan_profile(entity_name: str, use_cache: bool = True) -> Dict[str, Any]
    """
    Read JAN entity profile markdown and return structured data.
    
    Args:
        entity_name: SIYEM entity name (e.g., "JEAN", "KARASAHIN")
        use_cache: Whether to use cache if available
    
    Returns:
        Dictionary with profile data
    """
```

```python
def read_jan_template(entity_name: str, template_name: str, use_cache: bool = True) -> str
    """
    Read JAN prompt template and return as string.
    
    Args:
        entity_name: SIYEM entity name
        template_name: Template name without .md extension
        use_cache: Whether to use cache if available
    
    Returns:
        Template content as string (ready for .format())
    """
```

```python
def sync_jan_to_siyem() -> Dict[str, Any]
    """
    Sync all JAN markdown files to SIYEM JSON format.
    
    Returns:
        Sync report with details
    """
```

**Entity Name Mapping:**

SIYEM uses uppercase entity names, but JAN uses lowercase folder names:

| SIYEM Entity Name | JAN Folder Name | JAN Profile Path |
|------------------|-----------------|------------------|
| `KARASAHIN` | `jk` | `S:\JAN\Siyem.org\jk\profile.md` |
| `JEAN` | `jean_mahram` | `S:\JAN\Siyem.org\jean_mahram\profile.md` |
| `RAMIZ` | `uncle_ray_ramiz` | `S:\JAN\Siyem.org\uncle_ray_ramiz\profile.md` |
| `PIERRE` | `pierre_pressure` | `S:\JAN\Siyem.org\pierre_pressure\profile.md` |
| `SIYEM` | `siyem_media` | `S:\JAN\Siyem.org\siyem_media\profile.md` |

**Caching:**

- Files are cached in memory
- Cache validity checked via file modification time
- Cache key format: `{file_type}_{entity}_{name}`
- Cache invalidated when file changes

**Error Handling:**

- Missing files return empty dict/string
- Permission errors logged
- YAML frontmatter parsing is optional (graceful fallback)

#### `services/jan_validator.py`

**Purpose:** Validate content against JAN rules

**Key Functions:**

```python
def validate_output(content: str, entity: str, output_type: str) -> Dict[str, Any]
    """
    Validate content against JAN rules.
    
    Returns:
        {
            "valid": bool,
            "violations": list,
            "warnings": list,
            "checks_performed": dict
        }
    """
```

**Validation Checks:**

1. **Telos Alignment** - Checks against `telos.md` principles
2. **Essence Consistency** - Checks against `essence.md` fingerprint
3. **Entity Rules Compliance** - Checks against entity-specific rules
4. **Security Lens** - Checks for email addresses, API keys, private data

#### `services/governance_enforcer.py`

**Purpose:** Enforce JAN governance rules

**Key Functions:**

```python
def check_permission(action: str, entity: str, user: str = "system") -> bool
    """
    Check if user has permission for action on entity.
    
    Returns:
        True if allowed, False if denied
    """
```

```python
def enforce_security_lens(action: str, content: Dict[str, Any]) -> Dict[str, Any]
    """
    Enforce security lens constraints on action and content.
    
    Returns:
        {"allowed": bool, "reason": str}
    """
```

```python
def audit_action(action: str, entity: str, user: str, details: Dict[str, Any]) -> None
    """
    Audit an action according to audit_system.md requirements.
    """
```

#### `services/jan_engine.py`

**Purpose:** Execute JAN workflow as described in `jan_engine.prompt`

**Key Functions:**

```python
def execute_jan_workflow(request: Dict[str, Any]) -> Dict[str, Any]
    """
    Execute JAN workflow:
    1. Check Entity Context
    2. Load Core Rules (telos.md + essence.md)
    3. Load Entity-Specific Rules
    4. Load Relevant Style Modules
    5. Apply Security & Governance
    6. Generate Output
    7. Validate Against Core Principles
    8. Output
    """
```

```python
def load_rule_hierarchy(entity: str, output_type: str) -> Dict[str, Any]
    """
    Load all applicable rules in hierarchy:
    - Level 1: telos.md, essence.md
    - Level 2: admin_rules.md, security_lens.md
    - Level 3: entity profile.md, entity rules.md
    - Level 4: style modules
    """
```

```python
def apply_rules_to_prompt(base_prompt: str, rules: Dict[str, Any]) -> str
    """
    Combine base prompt with JAN rules.
    Applies rule hierarchy (higher levels override lower).
    """
```

---

## How SIYEM Reads JAN

### File Reading Process

1. **Entity Name Mapping**
   - SIYEM entity name (e.g., "JEAN") → JAN folder name (e.g., "jean_mahram")
   - Mapping defined in `ENTITY_NAME_MAPPING` constant

2. **File Path Construction**
   - Profile: `{JAN_ROOT}/Siyem.org/{jan_entity_name}/profile.md`
   - Template: `{JAN_ROOT}/Siyem.org/{jan_entity_name}/prompt_templates/{template_name}.md`
   - Rules: `{JAN_ROOT}/Siyem.org/{jan_entity_name}/creative_rules.md`

3. **File Reading**
   - Check cache first (if enabled)
   - Read file from disk
   - Parse YAML frontmatter (if present)
   - Parse markdown sections
   - Cache result

4. **Error Handling**
   - Missing files return empty dict/string
   - Permission errors logged
   - Invalid markdown handled gracefully

### Markdown Parsing

**Section Parsing:**

Markdown files are parsed into sections based on headers:

```markdown
# Section 1
Content here

## Subsection 1.1
More content

## Subsection 1.2
Even more content
```

Becomes:
```python
{
    "Section 1": "Content here",
    "Subsection 1.1": "More content",
    "Subsection 1.2": "Even more content"
}
```

**YAML Frontmatter:**

Optional YAML frontmatter is parsed if present:

```markdown
---
version: 1.0
author: JAN
---

# Content
```

Becomes:
```python
{
    "version": "1.0",
    "author": "JAN",
    "Content": "..."
}
```

### Template Placeholders

Templates support placeholders:

- `{task}` - Task description
- `{language}` - Language (e.g., "English", "Turkish")
- `{entity}` - Entity name

**Example:**
```markdown
Create {task} in {language} for {entity}.
```

**Usage:**
```python
template = read_jan_template("JEAN", "storytelling_template")
prompt = template.format(
    task="a short story",
    language="English",
    entity="Jean Mahram"
)
```

---

## API Endpoints

### Admin Endpoints

#### `POST /admin/sync-jan`

**Purpose:** Sync JAN markdown files to SIYEM JSON format

**Request:**
```json
{}
```

**Response:**
```json
{
    "success": true,
    "entities_synced": ["JEAN", "KARASAHIN"],
    "templates_synced": ["JEAN/storytelling_template"],
    "entities_new": [],
    "entities_updated": ["JEAN"],
    "templates_new": [],
    "templates_updated": ["JEAN/storytelling_template"],
    "errors": [],
    "timestamp": "2025-01-27T12:00:00"
}
```

#### `GET /admin/validate-jan-siyem`

**Purpose:** Validate alignment between JAN and SIYEM

**Response:**
```json
{
    "aligned": true,
    "entities": {
        "JEAN": {
            "jan_exists": true,
            "siyem_exists": true,
            "aligned": true,
            "differences": []
        }
    },
    "templates": {
        "JEAN": {
            "jan_templates": ["storytelling_template"],
            "siyem_templates": ["storytelling_template"],
            "missing_in_siyem": [],
            "missing_in_jan": [],
            "aligned": true
        }
    },
    "errors": []
}
```

#### `GET /admin/jan-status`

**Purpose:** Get status of JAN integration

**Response:**
```json
{
    "jan_available": true,
    "jan_root": "S:\\JAN",
    "services_using_jan": [
        "prompt_builder",
        "lyric_engine",
        "entity_router"
    ],
    "entities_available": [
        {
            "jan_entity": "jean_mahram",
            "siyem_entity": "JEAN",
            "profile_exists": true
        }
    ],
    "core_files": {
        "telos": true,
        "essence": true
    }
}
```

#### `POST /content/validate`

**Purpose:** Validate content against JAN rules

**Request:**
```json
{
    "content": "Generated content here",
    "entity": "JEAN",
    "output_type": "story"
}
```

**Response:**
```json
{
    "valid": true,
    "violations": [],
    "warnings": [],
    "checks_performed": {
        "telos": true,
        "essence": true,
        "entity_rules": true,
        "security_lens": true
    }
}
```

---

## Extension Points

### Adding a New Service

1. **Create service file:**
   ```python
   # services/my_service.py
   from .jan_integration import read_jan_profile, read_jan_template
   
   def my_function(entity: str):
       profile = read_jan_profile(entity)
       template = read_jan_template(entity, "my_template")
       # Use profile and template
   ```

2. **Add API endpoint:**
   ```python
   # api/my_api.py
   from fastapi import APIRouter
   from ..services.my_service import my_function
   
   router = APIRouter()
   
   @router.post("/my-endpoint")
   async def my_endpoint(entity: str):
       result = my_function(entity)
       return result
   ```

3. **Register router:**
   ```python
   # server.py
   from api.my_api import router as my_api_router
   
   app.include_router(my_api_router)
   ```

### Modifying Existing Services

**Example: Modify `prompt_builder.py` to use JAN templates:**

```python
# services/prompt_builder.py
from .jan_integration import read_jan_template

def build_entity_prompt(entity_id, task, language, template_type=None):
    # Try JAN template first
    if template_type:
        jan_template = read_jan_template(entity_id, template_type)
        if jan_template:
            return jan_template.format(
                task=task,
                language=language,
                entity=entity_id
            )
    
    # Fallback to JSON
    # ... existing code ...
```

### Adding Governance Middleware

```python
# middleware/governance.py
from fastapi import Request
from ..services.governance_enforcer import check_permission, audit_action

async def governance_middleware(request: Request, call_next):
    # Check permissions
    action = request.method + " " + request.url.path
    entity = request.path_params.get("entity", "system")
    
    if not check_permission(action, entity):
        return JSONResponse(
            {"error": "Permission denied"},
            status_code=403
        )
    
    # Process request
    response = await call_next(request)
    
    # Audit action
    audit_action(
        action=action,
        entity=entity,
        user="system",
        details={"status": response.status_code}
    )
    
    return response
```

**Register middleware:**
```python
# server.py
from middleware.governance import governance_middleware

app.middleware("http")(governance_middleware)
```

### Adding Validation to Endpoints

```python
# api/content.py
from ..services.jan_validator import validate_output

@router.post("/generate")
async def generate_content(request: GenerateRequest):
    # Generate content
    content = generate(request)
    
    # Validate against JAN rules
    validation = validate_output(
        content,
        request.entity,
        request.output_type
    )
    
    if not validation["valid"]:
        return {
            "content": content,
            "validation": validation,
            "warnings": validation["warnings"]
        }
    
    return {"content": content}
```

---

## File Structure

```
S:\SIYEM\
├── 00_CORE\
│   └── ENTITIES\
│       └── entity_database.json      # Entity definitions (JSON)
├── 07_AUTOMATION_AI\
│   ├── services\
│   │   ├── jan_integration.py        # JAN file reading
│   │   ├── jan_validator.py          # Content validation
│   │   ├── governance_enforcer.py    # Governance enforcement
│   │   ├── jan_engine.py             # JAN workflow execution
│   │   ├── prompt_builder.py         # Prompt building (uses JAN)
│   │   ├── lyric_engine.py            # Lyric generation (uses JAN)
│   │   └── entity_router.py          # Entity routing (uses JAN)
│   ├── api\
│   │   ├── jan_admin.py              # JAN admin endpoints
│   │   └── ...
│   ├── MODELS\
│   │   └── TEXT\
│   │       └── entity_prompts.json   # AI prompts (JSON, synced from JAN)
│   └── server.py                     # FastAPI server
└── 08_WEB_DEV\
    ├── console-v2\                    # React console
    └── entity-consoles-html\          # HTML consoles
```

---

## Dependencies

### Required

```python
# requirements.txt
markdown>=3.4.0
mistune>=2.0.0
python-frontmatter>=1.0.0
PyYAML>=6.0
fastapi>=0.100.0
```

### Optional

- `markdown` - Enhanced markdown parsing
- `mistune` - Fast markdown parser
- `PyYAML` - YAML frontmatter parsing

---

## Configuration

### Environment Variables

```bash
# JAN root directory
JAN_ROOT=S:\JAN

# SIYEM root directory
SIYEM_ROOT=S:\SIYEM
```

### Path Constants

Defined in `services/jan_integration.py`:

```python
JAN_ROOT = os.getenv("JAN_ROOT", r"S:\JAN")
SIYEM_ROOT = r"S:\SIYEM"
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")
JAN_TELOS = os.path.join(JAN_ROOT, "telos.md")
JAN_ESSENCE = os.path.join(JAN_ROOT, "essence.md")
JAN_STYLES = os.path.join(JAN_ROOT, "styles")
JAN_BACKROOM = os.path.join(JAN_ROOT, "Siyem.org", "backroom")
```

---

## Best Practices

### Service Development

1. **Use JAN files, not JSON**
   - Read from JAN markdown files
   - Fallback to JSON only if JAN unavailable
   - Sync JAN to JSON for backward compatibility

2. **Respect Rule Hierarchy**
   - Core rules cannot be overridden
   - Governance rules are enforced
   - Entity rules are contextual
   - Style modules are applied

3. **Validate Outputs**
   - Always validate against JAN rules
   - Check telos, essence, entity rules
   - Enforce security lens

4. **Audit Actions**
   - Log all actions
   - Track entity usage
   - Monitor governance compliance

### API Design

1. **Use Entity Names**
   - Accept SIYEM format (e.g., "JEAN")
   - Map to JAN folder names internally
   - Return consistent entity names

2. **Error Handling**
   - Return clear error messages
   - Log errors for debugging
   - Handle missing JAN files gracefully

3. **Caching**
   - Cache JAN file reads
   - Invalidate on file changes
   - Use file modification time for validation

---

## Troubleshooting

### JAN Files Not Found

**Problem:** `read_jan_profile()` returns empty dict

**Solutions:**
1. Check `JAN_ROOT` environment variable
2. Verify file path exists
3. Check file permissions
4. Verify entity name mapping

### Cache Issues

**Problem:** Changes to JAN files not reflected

**Solutions:**
1. Disable cache: `use_cache=False`
2. Clear cache: Restart service
3. Check file modification time

### Template Placeholders Not Working

**Problem:** `{task}` not replaced in template

**Solutions:**
1. Use `.format()` method, not f-strings
2. Check placeholder names match
3. Verify template syntax

---

## Related Documentation

- **[README.md](../README.md)** - Project overview
- **[docs/JAN-SPECIFICATION.md](JAN-SPECIFICATION.md)** - JAN file format
- **[docs/BOOK-OF-RACON.md](BOOK-OF-RACON.md)** - Philosophical foundation
- **[JAN_SIYEM_INTEGRATION.md](../JAN_SIYEM_INTEGRATION.md)** - Integration guide

---

**Last Updated:** 2025-01-27  
**Version:** 1.0  
**Status:** Active

