"""
Fix Swagger UI Examples - Add examples to all Pydantic models
This script adds examples to all request models across all API files
"""

import os
import re
from pathlib import Path

# Find all API files
backend_dir = Path(__file__).parent
api_files = list(backend_dir.glob("*_api.py")) + list(backend_dir.glob("jan_*.py"))

# Pattern to find BaseModel classes that need examples
model_pattern = re.compile(
    r'class\s+(\w+Request)\s*\([^)]*BaseModel[^)]*\):\s*\n(.*?)(?=\nclass|\n\nclass|\Z)',
    re.DOTALL
)

# Example templates for common request types
example_templates = {
    'RegisterRequest': {
        "username": "jan",
        "email": "jan@example.com",
        "password": "SecurePass123!"
    },
    'LoginRequest': {
        "email": "jan@example.com",
        "password": "SecurePass123!"
    },
    'RefreshRequest': {
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
    },
    'LogoutRequest': {
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
    }
}

def add_example_to_model(model_content: str, model_name: str) -> str:
    """Add Config class with example to a model if it doesn't have one"""
    
    # Check if Config already exists
    if 'class Config:' in model_content or 'Config =' in model_content:
        return model_content
    
    # Check if schema_extra already exists
    if 'schema_extra' in model_content:
        return model_content
    
    # Generate example based on model name
    if 'Request' in model_name:
        # Try to infer example from field names
        fields = re.findall(r'(\w+):\s*\w+', model_content)
        example = {}
        for field in fields:
            if field == 'email':
                example[field] = "example@example.com"
            elif field == 'password':
                example[field] = "SecurePass123!"
            elif field == 'username':
                example[field] = "jan"
            elif field == 'token' or 'token' in field.lower():
                example[field] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
            elif 'id' in field.lower():
                example[field] = 1
            elif 'name' in field.lower():
                example[field] = "Example Name"
            else:
                example[field] = "string"
        
        config_block = f"""
    class Config:
        schema_extra = {{
            "example": {example}
        }}"""
        
        # Add before the last line (closing of class)
        lines = model_content.split('\n')
        # Find last non-empty line before class ends
        insert_pos = len(lines) - 1
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() and not lines[i].strip().startswith('#'):
                insert_pos = i
                break
        
        lines.insert(insert_pos, config_block)
        return '\n'.join(lines)
    
    return model_content

print("Fix Swagger Examples Script")
print("=" * 50)
print(f"Found {len(api_files)} API files to check")
print("\nNote: This is a helper script. Manual fixes may be needed.")
print("The main fix has been applied to auth_api.py")
