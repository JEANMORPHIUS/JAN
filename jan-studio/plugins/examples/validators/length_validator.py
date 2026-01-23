"""
Length Validator Plugin Example

Example plugin for content length validation.
"""

from typing import Dict, Any, Optional, List
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plugins.base import ValidatorPlugin


class LengthValidatorPlugin(ValidatorPlugin):
    """Content length validator plugin."""
    
    def name(self) -> str:
        return "length-validator"
    
    def version(self) -> str:
        return "1.0.0"
    
    def author(self) -> str:
        return "JAN Team"
    
    def description(self) -> str:
        return "Validates content length constraints"
    
    def rule_name(self) -> str:
        return "length"
    
    def validate(
        self,
        output: str,
        rules: Dict[str, Any],
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, List[str], List[str]]:
        """Validate content length."""
        errors = []
        warnings = []
        
        length = len(output)
        
        # Check minimum length
        min_length = rules.get("min_length", 0)
        if length < min_length:
            errors.append(f"Content too short: {length} < {min_length} characters")
        
        # Check maximum length
        max_length = rules.get("max_length")
        if max_length and length > max_length:
            errors.append(f"Content too long: {length} > {max_length} characters")
        
        # Check word count
        word_count = len(output.split())
        min_words = rules.get("min_words", 0)
        if word_count < min_words:
            warnings.append(f"Low word count: {word_count} < {min_words} words")
        
        max_words = rules.get("max_words")
        if max_words and word_count > max_words:
            warnings.append(f"High word count: {word_count} > {max_words} words")
        
        is_valid = len(errors) == 0
        
        return is_valid, errors, warnings

