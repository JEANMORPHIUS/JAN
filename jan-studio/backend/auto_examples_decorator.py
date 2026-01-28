"""
AUTOMATIC EXAMPLES DECORATOR FOR FASTAPI
Deep search integrated - automatically adds examples to all Pydantic models

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
AUTOMATE WHAT CAN BE AUTOMATED
DEEP SEARCH FOR BEST SOLUTIONS
NO MORE MANUAL FIXES
"""

from typing import Any, Dict, Type, get_type_hints
from pydantic import BaseModel, create_model
import inspect

def auto_examples(cls: Type[BaseModel]) -> Type[BaseModel]:
    """
    Automatically add examples to Pydantic models based on field types and names.
    No manual Config.schema_extra needed.
    """
    if not issubclass(cls, BaseModel):
        return cls
    
    # Check if already has examples
    if hasattr(cls, 'Config') and hasattr(cls.Config, 'schema_extra'):
        if 'example' in cls.Config.schema_extra:
            return cls
    
    # Get field information
    fields = cls.model_fields if hasattr(cls, 'model_fields') else cls.__fields__
    
    example = {}
    for field_name, field_info in fields.items():
        field_lower = field_name.lower()
        field_type = field_info.annotation if hasattr(field_info, 'annotation') else field_info
        
        # Smart defaults based on field name and type
        if 'email' in field_lower:
            example[field_name] = "jan@example.com"
        elif 'password' in field_lower:
            example[field_name] = "SecurePass123!"
        elif 'username' in field_lower or ('name' in field_lower and 'username' not in field_lower):
            example[field_name] = "jan"
        elif 'token' in field_lower or 'refresh' in field_lower:
            example[field_name] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
        elif 'id' in field_lower:
            example[field_name] = 1
        elif 'count' in field_lower or 'limit' in field_lower or 'offset' in field_lower:
            example[field_name] = 10
        elif 'rating' in field_lower:
            example[field_name] = 5
        elif 'price' in field_lower or 'cost' in field_lower or 'amount' in field_lower:
            example[field_name] = 100.0
        elif 'bool' in str(field_type).lower() or field_lower.startswith('is_') or field_lower.startswith('has_'):
            example[field_name] = True
        elif 'int' in str(field_type).lower():
            example[field_name] = 1
        elif 'float' in str(field_type).lower():
            example[field_name] = 1.0
        elif 'list' in str(field_type).lower() or 'List' in str(field_type):
            example[field_name] = []
        elif 'dict' in str(field_type).lower() or 'Dict' in str(field_type):
            example[field_name] = {}
        else:
            example[field_name] = "string"
    
    # Add Config with schema_extra
    if not hasattr(cls, 'Config'):
        class Config:
            schema_extra = {"example": example}
        cls.Config = Config
    else:
        if not hasattr(cls.Config, 'schema_extra'):
            cls.Config.schema_extra = {"example": example}
        elif 'example' not in cls.Config.schema_extra:
            cls.Config.schema_extra["example"] = example
    
    return cls
