"""
OpenAI AI Service Plugin Example

Example plugin for OpenAI API integration.
"""

from typing import Dict, Any, Optional
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plugins.base import AIServicePlugin, PluginType


class OpenAIPlugin(AIServicePlugin):
    """OpenAI GPT plugin for JAN."""
    
    def name(self) -> str:
        return "openai"
    
    def version(self) -> str:
        return "1.0.0"
    
    def author(self) -> str:
        return "JAN Team"
    
    def description(self) -> str:
        return "OpenAI GPT-4 and GPT-3.5 integration"
    
    def dependencies(self) -> list:
        return ["openai>=1.0.0"]
    
    def permissions(self) -> list:
        return ["api_key"]
    
    def validate_config(self) -> tuple[bool, Optional[str]]:
        """Validate OpenAI API key is configured."""
        api_key = self.config.get("api_key") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            return False, "OpenAI API key not configured"
        return True, None
    
    def generate(
        self,
        prompt: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Generate content using OpenAI API."""
        try:
            import openai
            
            api_key = self.config.get("api_key") or os.getenv("OPENAI_API_KEY")
            openai.api_key = api_key
            
            # Build messages
            messages = []
            
            # Add system message from persona
            if "profile" in persona:
                messages.append({
                    "role": "system",
                    "content": f"You are {persona.get('name', 'a creative assistant')}. {persona.get('description', '')}"
                })
            
            # Add user prompt
            messages.append({
                "role": "user",
                "content": prompt
            })
            
            # Get options
            model = options.get("model", "gpt-4") if options else "gpt-4"
            temperature = options.get("temperature", 0.7) if options else 0.7
            max_tokens = options.get("max_tokens", 2000) if options else 2000
            
            # Call API
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            content = response.choices[0].message.content
            
            return {
                "content": content,
                "model": model,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                }
            }
        
        except ImportError:
            return {
                "error": "openai package not installed",
                "content": None
            }
        except Exception as e:
            return {
                "error": str(e),
                "content": None
            }
    
    def supports_streaming(self) -> bool:
        return True
    
    def stream_generate(
        self,
        prompt: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ):
        """Stream content from OpenAI API."""
        try:
            import openai
            
            api_key = self.config.get("api_key") or os.getenv("OPENAI_API_KEY")
            openai.api_key = api_key
            
            messages = [
                {"role": "user", "content": prompt}
            ]
            
            model = options.get("model", "gpt-4") if options else "gpt-4"
            temperature = options.get("temperature", 0.7) if options else 0.7
            
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                stream=True
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        
        except Exception as e:
            yield f"Error: {str(e)}"

