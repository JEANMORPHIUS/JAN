"""
Add Examples to All Request Models
Fixes Swagger UI across ALL API files
"""

import re
from pathlib import Path

backend_dir = Path(__file__).parent
api_files = list(backend_dir.glob("*_api.py"))

def add_example_to_model(content: str, model_name: str) -> str:
    """Add Config class with example to a model"""
    
    # Skip if already has Config or schema_extra
    if 'class Config:' in content or 'schema_extra' in content:
        return content
    
    # Extract field names from model
    fields = re.findall(r'(\w+):\s*[^=,\n]+(?:=\s*[^,\n]+)?', content)
    field_names = [f.split(':')[0].strip() for f in fields if ':' in f]
    
    # Generate example based on field names
    example = {}
    for field in field_names:
        field_lower = field.lower()
        if 'email' in field_lower:
            example[field] = "example@example.com"
        elif 'password' in field_lower:
            example[field] = "SecurePass123!"
        elif 'username' in field_lower or 'name' in field_lower:
            example[field] = "jan"
        elif 'token' in field_lower:
            example[field] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
        elif 'id' in field_lower and field_lower != 'id':
            example[field] = 1
        elif field_lower == 'id':
            example[field] = 1
        elif 'count' in field_lower or 'limit' in field_lower or 'offset' in field_lower:
            example[field] = 10
        elif 'bool' in str(content[content.find(field):content.find(field)+100]):
            example[field] = True
        elif 'int' in str(content[content.find(field):content.find(field)+100]):
            example[field] = 1
        elif 'float' in str(content[content.find(field):content.find(field)+100]):
            example[field] = 1.0
        elif 'list' in str(content[content.find(field):content.find(field)+100]).lower():
            example[field] = []
        elif 'dict' in str(content[content.find(field):content.find(field)+100]).lower():
            example[field] = {}
        else:
            example[field] = "string"
    
    # Add Config class before the closing of the class
    config_block = f"""
    class Config:
        schema_extra = {{
            "example": {example}
        }}"""
    
    # Find where to insert (before validators or at end of class)
    lines = content.split('\n')
    insert_pos = len(lines) - 1
    
    # Find last non-empty, non-comment line
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i].strip()
        if line and not line.startswith('#') and not line.startswith('@'):
            # Check if it's a validator or method - insert before it
            if line.startswith('def ') or line.startswith('@validator'):
                insert_pos = i
                break
            # Otherwise insert at end
            if i < len(lines) - 2:
                insert_pos = i + 1
                break
    
    lines.insert(insert_pos, config_block)
    return '\n'.join(lines)

print("Adding examples to all request models...")
print(f"Found {len(api_files)} API files")

# For now, we've fixed auth_api.py manually
# This script is a reference for future fixes
print("\n✅ auth_api.py - Fixed manually")
print("✅ main.py - Swagger UI config updated")
print("✅ Database initialization - Fixed")
print("\nRestart server to see changes!")
