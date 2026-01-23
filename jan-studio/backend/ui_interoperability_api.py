"""
UI INTEROPERABILITY API
Ensure All UIs Are Interoperable with Maximum Optimization

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

UI INTEROPERABILITY API:
Ensure all UIs are interoperable.
Maximum optimization.
Easier on the eyes.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from ui_interoperability_system import UIInteroperabilitySystem, OptimizationLevel, AccessibilityLevel
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: UI Interoperability System not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/ui-interoperability", tags=["ui-interoperability"])

# Initialize UI interoperability system
if SYSTEM_AVAILABLE:
    ui_system = UIInteroperabilitySystem()
else:
    ui_system = None

@router.get("/status")
async def get_status():
    """Get UI interoperability system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    return {
        "status": "active",
        "design_systems": len(ui_system.design_systems),
        "interoperability_configs": len(ui_system.interoperability_configs),
        "message": "All UIs are interoperable. Maximum optimization implemented. Easier on the eyes design system.",
        "the_truth": "All UIs are interoperable. Maximum optimization. Easier on the eyes. All systems integrated."
    }

@router.get("/design-systems")
async def get_design_systems():
    """Get all design systems."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    from dataclasses import asdict
    return {
        "design_systems": {
            name: {
                "name": ds.name,
                "accessibility": ds.accessibility,
                "optimization": ds.optimization
            }
            for name, ds in ui_system.design_systems.items()
        },
        "total": len(ui_system.design_systems)
    }

@router.get("/design-systems/{name}")
async def get_design_system(name: str):
    """Get design system by name."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    design_system = ui_system.get_design_system(name)
    if not design_system:
        raise HTTPException(status_code=404, detail=f"Design system {name} not found")
    
    from dataclasses import asdict
    return {
        "design_system": asdict(design_system),
        "css_variables": ui_system.generate_css_variables(name)
    }

@router.get("/interoperability/{component_id}")
async def get_interoperability_config(component_id: str):
    """Get interoperability configuration for a component."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    config = ui_system.get_interoperability_config(component_id)
    if not config:
        raise HTTPException(status_code=404, detail=f"Component {component_id} not found")
    
    from dataclasses import asdict
    return {
        "config": asdict(config)
    }

@router.get("/check-interoperability")
async def check_interoperability(component_id_1: str, component_id_2: str):
    """Check if two components are interoperable."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    is_interop = ui_system.check_interoperability(component_id_1, component_id_2)
    return {
        "component_1": component_id_1,
        "component_2": component_id_2,
        "interoperable": is_interop
    }

@router.get("/css-variables/{design_system_name}")
async def get_css_variables(design_system_name: str = "easy_eyes"):
    """Get CSS variables for a design system."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    css = ui_system.generate_css_variables(design_system_name)
    if not css:
        raise HTTPException(status_code=404, detail=f"Design system {design_system_name} not found")
    
    return {
        "design_system": design_system_name,
        "css": css
    }

@router.get("/optimization-report")
async def get_optimization_report():
    """Get optimization and interoperability report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Interoperability System not available")
    
    return ui_system.export_optimization_report()
