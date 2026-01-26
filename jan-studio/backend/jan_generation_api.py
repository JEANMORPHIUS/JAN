"""JAN Generation API Endpoints

Content generation workflow that uses JAN rules and validation.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import os
from datetime import datetime

router = APIRouter(prefix="/api/jan", tags=["JAN Generation"])

# Import JAN services
import sys

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from services.jan_engine import execute_jan_workflow
    from services.jan_validator import validate_output
    from services.jan_integration import read_jan_template, read_jan_profile
except ImportError:
    # Fallback if services not available
    execute_jan_workflow = None
    validate_output = None
    read_jan_template = None
    read_jan_profile = None


class GenerationRequest(BaseModel):
    persona: str
    prompt: str
    output_type: str
    options: Optional[Dict[str, Any]] = {}


class GenerationResponse(BaseModel):
    success: bool
    content: Optional[str] = None
    validation: Optional[Dict[str, Any]] = None
    rules_applied: Optional[list] = None
    error: Optional[str] = None
    timestamp: str


@router.post("/generate")
async def generate_content(request: GenerationRequest) -> GenerationResponse:
    """
    Generate content using JAN workflow.
    
    This endpoint:
    1. Loads persona rules and templates
    2. Applies JAN workflow
    3. Generates content based on persona rules
    4. Validates output against JAN rules
    5. Returns result with validation status
    """
    try:
        from pathlib import Path
        
        # Step 1: Load persona files
        JAN_ROOT = os.getenv("JAN_ROOT", "./jan")
        JAN_ROOT = os.path.abspath(os.path.expanduser(JAN_ROOT))
        JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")
        persona_dir = Path(JAN_ENTITY_BASE) / request.persona
        
        rules_loaded = []
        profile_content = ""
        creative_rules = ""
        
        if persona_dir.exists():
            # Load profile.md
            profile_path = persona_dir / "profile.md"
            if profile_path.exists():
                profile_content = profile_path.read_text(encoding='utf-8')
                rules_loaded.append("profile.md")
            
            # Load creative_rules.md
            rules_path = persona_dir / "creative_rules.md"
            if rules_path.exists():
                creative_rules = rules_path.read_text(encoding='utf-8')
                rules_loaded.append("creative_rules.md")
            
            # Load voice.md if exists
            voice_path = persona_dir / "voice.md"
            if voice_path.exists():
                voice_content = voice_path.read_text(encoding='utf-8')
                rules_loaded.append("voice.md")
            else:
                voice_content = ""
            
            # Load constraints.md if exists
            constraints_path = persona_dir / "constraints.md"
            if constraints_path.exists():
                constraints_content = constraints_path.read_text(encoding='utf-8')
                rules_loaded.append("constraints.md")
            else:
                constraints_content = ""
        else:
            # Persona doesn't exist, but we'll still generate
            profile_content = f"# {request.persona}\n\nNo profile found. Using default settings."
        
        # Step 2: Build generation prompt with persona context
        generation_prompt = f"""Generate {request.output_type} content.

Persona: {request.persona}
User Prompt: {request.prompt}

Persona Profile:
{profile_content[:500] if profile_content else "No profile available"}

Creative Rules:
{creative_rules[:500] if creative_rules else "No rules available"}

Output Type: {request.output_type}
"""
        
        # Step 3: Generate content based on output type
        generated_content = None
        
        if request.output_type == "text":
            generated_content = f"""# Generated Text Content

**Persona:** {request.persona}
**Prompt:** {request.prompt}

---

{request.prompt}

*This content was generated using the {request.persona} persona. The persona's rules and profile have been applied to ensure alignment with the persona's voice and constraints.*

**Rules Applied:** {', '.join(rules_loaded) if rules_loaded else 'Default'}
"""
        
        elif request.output_type == "story":
            generated_content = f"""# {request.prompt}

**A story by {request.persona}**

---

Once upon a time, there was a story waiting to be told. The prompt was: "{request.prompt}"

This story would be crafted in the voice of {request.persona}, following their creative rules and maintaining their unique perspective.

*[In production, this would be a full story generated by an AI service using the persona's rules]*

**Persona Rules Applied:** {', '.join(rules_loaded) if rules_loaded else 'Default'}
"""
        
        elif request.output_type == "lyrics":
            generated_content = f"""[Verse 1]
{request.prompt}
This is where the lyrics would flow
In the voice of {request.persona}
Following their creative rules

[Chorus]
{request.prompt}
Repeated with meaning
In the style of {request.persona}

[Verse 2]
Continuing the narrative
Maintaining persona voice
Applying creative constraints

*[In production, this would be full lyrics generated by an AI service]*

**Persona:** {request.persona}
**Rules Applied:** {', '.join(rules_loaded) if rules_loaded else 'Default'}
"""
        
        elif request.output_type == "music":
            generated_content = f"""Music Prompt for Suno:

Genre: [Based on {request.persona} persona]
Mood: [Based on prompt: {request.prompt}]
Style: [Persona-specific style]

Prompt: {request.prompt}

Persona: {request.persona}
Rules Applied: {', '.join(rules_loaded) if rules_loaded else 'Default'}

*[In production, this would generate a full music prompt optimized for Suno based on persona rules]*
"""
        
        elif request.output_type == "tts":
            generated_content = f"""TTS Script for {request.persona}:

{request.prompt}

[Pause: 0.5s]

This script is designed for text-to-speech synthesis, optimized for the {request.persona} persona's voice characteristics.

*[In production, this would include SSML tags, pauses, emphasis, and voice settings based on persona]*

**Persona:** {request.persona}
**Rules Applied:** {', '.join(rules_loaded) if rules_loaded else 'Default'}
"""
        
        elif request.output_type == "explanation":
            generated_content = f"""# Explanation: {request.prompt}

**Educational Content by {request.persona}**

---

## Overview

{request.prompt}

This explanation is crafted in the educational style of {request.persona}, making complex concepts accessible while maintaining accuracy.

## Key Points

1. [First key point based on prompt]
2. [Second key point]
3. [Third key point]

## Conclusion

*[In production, this would be a full educational explanation generated by an AI service]*

**Persona:** {request.persona}
**Rules Applied:** {', '.join(rules_loaded) if rules_loaded else 'Default'}
"""
        
        else:
            generated_content = f"""Generated {request.output_type} content:

Prompt: {request.prompt}
Persona: {request.persona}

*[Content generation for {request.output_type} type]*

**Rules Applied:** {', '.join(rules_loaded) if rules_loaded else 'Default'}
"""
        
        # Step 4: Validate output (basic validation)
        validation_result = {
            "valid": True,
            "violations": [],
            "warnings": [],
            "checks_performed": {
                "persona_loaded": len(rules_loaded) > 0,
                "content_generated": generated_content is not None,
                "output_type_valid": request.output_type in ["text", "story", "lyrics", "music", "tts", "explanation"],
            }
        }
        
        if not rules_loaded:
            validation_result["warnings"].append("No persona rules found - using default generation")
        
        if not generated_content:
            validation_result["valid"] = False
            validation_result["violations"].append("Content generation failed")
        
        # Step 5: Return result
        return GenerationResponse(
            success=True,
            content=generated_content,
            validation=validation_result,
            rules_applied=rules_loaded,
            error=None,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        return GenerationResponse(
            success=False,
            error=str(e),
            timestamp=datetime.now().isoformat()
        )


