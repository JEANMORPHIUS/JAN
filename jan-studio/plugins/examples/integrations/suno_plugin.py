"""Suno Integration Plugin Example

Example plugin for Suno AI music generation integration.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, Any, Optional
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plugins.base import IntegrationPlugin


class SunoPlugin(IntegrationPlugin):
    """Suno AI music generation integration."""
    
    def name(self) -> str:
        return "suno-integration"
    
    def version(self) -> str:
        return "1.0.0"
    
    def author(self) -> str:
        return "JAN Team"
    
    def description(self) -> str:
        return "Suno AI music generation integration"
    
    def service_name(self) -> str:
        return "Suno AI"
    
    def dependencies(self) -> list:
        return ["requests>=2.28.0"]
    
    def permissions(self) -> list:
        return ["api_key"]
    
    def validate_config(self) -> tuple[bool, Optional[str]]:
        """Validate Suno API key is configured."""
        api_key = self.config.get("api_key") or os.getenv("SUNO_API_KEY")
        if not api_key:
            return False, "Suno API key not configured"
        return True, None
    
    def process(
        self,
        persona: Dict[str, Any],
        prompt: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process music generation request."""
        try:
            import requests
            
            api_key = self.config.get("api_key") or os.getenv("SUNO_API_KEY")
            api_url = self.config.get("api_url", "https://api.suno.ai/v1/generate")
            
            # Build request from prompt and persona
            request_data = {
                "prompt": prompt,
                "style": persona.get("style", "general"),
                "duration": context.get("duration", 30) if context else 30
            }
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(api_url, json=request_data, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            return {
                "success": True,
                "audio_url": result.get("audio_url"),
                "song_id": result.get("song_id"),
                "metadata": result.get("metadata", {})
            }
        
        except ImportError:
            return {
                "success": False,
                "error": "requests package not installed"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

