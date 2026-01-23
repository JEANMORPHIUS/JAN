"""
JSON Output Format Plugin Example

Example plugin for JSON output formatting.
"""

from typing import Dict, Any, Optional
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plugins.base import OutputFormatPlugin


class JSONFormatPlugin(OutputFormatPlugin):
    """JSON output format plugin."""
    
    def name(self) -> str:
        return "json-format"
    
    def version(self) -> str:
        return "1.0.0"
    
    def author(self) -> str:
        return "JAN Team"
    
    def description(self) -> str:
        return "Format output as JSON"
    
    def format_name(self) -> str:
        return "json"
    
    def process(
        self,
        content: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Format content as JSON."""
        try:
            # Try to parse as JSON first
            parsed = json.loads(content)
            formatted = json.dumps(parsed, indent=2)
        except json.JSONDecodeError:
            # If not JSON, wrap in object
            formatted = json.dumps({
                "content": content,
                "persona": persona.get("name", "unknown"),
                "format": "text"
            }, indent=2)
        
        return {
            "formatted_content": formatted,
            "format": "json",
            "mime_type": "application/json"
        }
    
    def validate(self, content: str) -> tuple[bool, Optional[str]]:
        """Validate JSON content."""
        try:
            json.loads(content)
            return True, None
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON: {str(e)}"

