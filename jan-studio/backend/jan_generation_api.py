"""
JAN Generation API Endpoints

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
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import os
from datetime import datetime

router = APIRouter(prefix="/api/jan", tags=["JAN Generation"])

# Import JAN services
import sys
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
    3. Generates content (would call AI service)
    4. Validates output against JAN rules
    5. Returns result with validation status
    """
    try:
        # Step 1: Prepare JAN workflow request
        workflow_request = {
            "entity": request.persona.upper(),
            "task": request.prompt,
            "output_type": request.output_type,
            "options": request.options or {},
        }
        
        # Step 2: Execute JAN workflow
        if execute_jan_workflow:
            workflow_result = execute_jan_workflow(workflow_request)
        else:
            # Fallback if services not available
            workflow_result = {
                "success": True,
                "content": None,
                "rules_loaded": [],
            }
        
        # Step 3: Generate content (in production, this would call AI service)
        # For now, we'll return a placeholder
        generated_content = None
        
        if workflow_result.get("success"):
            # In production, this would:
            # 1. Load template from JAN
            # 2. Apply rules to prompt
            # 3. Call AI service (OpenAI, Claude, etc.)
            # 4. Return generated content
            
            # Placeholder for actual generation
            generated_content = f"[Generated {request.output_type} content would appear here]\n\nPrompt: {request.prompt}\n\nPersona: {request.persona}\n\nThis is a placeholder. In production, this would call your AI service."
        
        # Step 4: Validate output
        validation_result = None
        if generated_content and validate_output:
            validation_result = validate_output(
                content=generated_content,
                entity=request.persona.upper(),
                output_type=request.output_type
            )
        
        # Step 5: Return result
        return GenerationResponse(
            success=workflow_result.get("success", False),
            content=generated_content,
            validation=validation_result,
            rules_applied=workflow_result.get("rules_loaded", []),
            error=workflow_result.get("error"),
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        return GenerationResponse(
            success=False,
            error=str(e),
            timestamp=datetime.now().isoformat()
        )


