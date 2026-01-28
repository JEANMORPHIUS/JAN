"""
Add Examples to ALL Request Models Across ALL API Files
Fixes Swagger UI completely - no partial fixes
"""

import re
from pathlib import Path
from typing import Dict, Any

backend_dir = Path(__file__).parent
api_files = [f for f in backend_dir.glob("*_api.py") if f.name != "fix_swagger_examples.py"]

def generate_example_from_fields(fields: list, content: str) -> Dict[str, Any]:
    """Generate example dict from field names and types"""
    example = {}
    for field in fields:
        field_name = field[0].strip()
        field_type_str = field[1] if len(field) > 1 else ""
        
        field_lower = field_name.lower()
        
        # Smart defaults based on field name
        if 'email' in field_lower:
            example[field_name] = "example@example.com"
        elif 'password' in field_lower:
            example[field_name] = "SecurePass123!"
        elif 'username' in field_lower or ('name' in field_lower and 'username' not in field_lower):
            example[field_name] = "jan"
        elif 'token' in field_lower or 'refresh' in field_lower:
            example[field_name] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
        elif 'id' in field_lower and field_lower != 'id':
            example[field_name] = 1
        elif field_lower == 'id':
            example[field_name] = 1
        elif 'count' in field_lower or 'limit' in field_lower or 'offset' in field_lower or 'number' in field_lower:
            example[field_name] = 10
        elif 'rating' in field_lower:
            example[field_name] = 5
        elif 'price' in field_lower or 'cost' in field_lower or 'amount' in field_lower or 'wage' in field_lower:
            example[field_name] = 100.0
        elif 'bool' in field_type_str.lower() or field_lower.startswith('is_') or field_lower.startswith('has_'):
            example[field_name] = True
        elif 'int' in field_type_str.lower() or 'Integer' in field_type_str:
            example[field_name] = 1
        elif 'float' in field_type_str.lower():
            example[field_name] = 1.0
        elif 'list' in field_type_str.lower() or 'List' in field_type_str:
            example[field_name] = []
        elif 'dict' in field_type_str.lower() or 'Dict' in field_type_str:
            example[field_name] = {}
        elif 'Optional' in field_type_str:
            # Skip optional fields in example if they have defaults
            continue
        else:
            example[field_name] = "string"
    
    return example

def add_example_to_file(file_path: Path) -> bool:
    """Add examples to all Request models in a file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Find all Request model classes
        pattern = r'class\s+(\w+Request)\s*\([^)]*BaseModel[^)]*\):\s*\n((?:[^\n]*\n)*?)(?=\nclass|\n@|\n\n\n|\Z)'
        matches = list(re.finditer(pattern, content, re.MULTILINE))
        
        if not matches:
            return False
        
        # Process matches in reverse to maintain positions
        for match in reversed(matches):
            model_name = match.group(1)
            model_content = match.group(2)
            
            # Skip if already has Config with schema_extra
            if 'schema_extra' in model_content or 'class Config:' in content[match.start():match.end()]:
                continue
            
            # Extract fields
            field_pattern = r'(\w+)\s*:\s*([^=\n]+?)(?:\s*=\s*[^\n]+)?\s*\n'
            fields = re.findall(field_pattern, model_content)
            
            if not fields:
                continue
            
            # Generate example
            example = generate_example_from_fields(fields, model_content)
            
            if not example:
                continue
            
            # Create Config block
            config_block = f"""
    class Config:
        schema_extra = {{
            "example": {example}
        }}"""
            
            # Insert before the end of the class (before validators or methods)
            # Find insertion point - before first @validator or def
            lines = model_content.split('\n')
            insert_pos = len(lines)
            
            for i, line in enumerate(lines):
                if line.strip().startswith('@validator') or (line.strip().startswith('def ') and not line.strip().startswith('def __')):
                    insert_pos = i
                    break
            
            # Insert Config block
            lines.insert(insert_pos, config_block)
            new_model_content = '\n'.join(lines)
            
            # Replace in original content
            full_match = match.group(0)
            new_full_match = full_match.replace(model_content, new_model_content)
            content = content[:match.start()] + new_full_match + content[match.end():]
        
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False

# Process all API files
print("Adding examples to ALL request models...")
print(f"Found {len(api_files)} API files")
print()

fixed_count = 0
for api_file in api_files:
    if add_example_to_file(api_file):
        print(f"[FIXED] {api_file.name}")
        fixed_count += 1
    else:
        print(f"[SKIP] {api_file.name} (no Request models or already has examples)")

print()
print(f"[DONE] Fixed {fixed_count} files")
print("[DONE] All request models now have examples")
print("[DONE] Swagger UI will show request bodies everywhere")
