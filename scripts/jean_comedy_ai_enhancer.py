"""
JEAN MORPHIUS - COMEDY AI ENHANCER
AI-Powered Comedy Material Enhancement and Improvement System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Enhance and improve comedy material using AI (Claude/Gemini)
Generate new material based on existing patterns
Improve delivery, punchlines, bilingual flow
Continue building until we can't
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict, field

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from claude_assistant import generate_with_claude
    from gemini_assistant import generate_content
    AI_AVAILABLE = True
except ImportError:
    print("Warning: AI assistants not available. Some features may not work.")
    AI_AVAILABLE = False

try:
    from jean_comedy_material_generator import (
        ComedyMaterial, ComedyStyle, generate_comedy_collection
    )
    COMEDY_GENERATOR_AVAILABLE = True
except ImportError:
    print("Warning: Comedy generator not available.")
    COMEDY_GENERATOR_AVAILABLE = False


@dataclass
class EnhancedComedyMaterial:
    """Enhanced comedy material with AI improvements"""
    original: Dict[str, Any]
    enhanced: Dict[str, Any]
    improvements: List[str]
    ai_used: str
    enhancement_score: float


class JeanComedyAIEnhancer:
    """AI-powered comedy material enhancement system"""
    
    def __init__(self):
        self.improvements_made = []
        self.enhancement_count = 0
        
    def enhance_material(self, material: ComedyMaterial, use_claude: bool = True) -> EnhancedComedyMaterial:
        """Enhance comedy material using AI"""
        
        if not AI_AVAILABLE:
            return None
        
        # Build enhancement prompt
        prompt = self._build_enhancement_prompt(material)
        
        # Generate enhancement
        if use_claude:
            enhanced_text = generate_with_claude(
                prompt,
                context="You are enhancing comedy material for Jean Morphius, a bilingual absurdist comedian.",
                system_prompt="You are a comedy writing expert. Enhance material while maintaining authenticity and bilingual flow."
            )
            ai_used = "claude"
        else:
            enhanced_text = generate_content(
                prompt,
                context="Enhancing comedy material for bilingual absurdist comedian.",
                temperature=0.8
            )
            ai_used = "gemini"
        
        # Parse enhancement
        enhanced = self._parse_enhancement(enhanced_text, material)
        improvements = self._identify_improvements(material, enhanced)
        score = self._calculate_enhancement_score(material, enhanced)
        
        result = EnhancedComedyMaterial(
            original=asdict(material),
            enhanced=enhanced,
            improvements=improvements,
            ai_used=ai_used,
            enhancement_score=score
        )
        
        self.enhancement_count += 1
        self.improvements_made.extend(improvements)
        
        return result
    
    def _build_enhancement_prompt(self, material: ComedyMaterial) -> str:
        """Build prompt for AI enhancement"""
        
        return f"""Enhance this comedy material for Jean Morphius, a bilingual absurdist comedian.

STYLE: {material.style.value}
CATEGORY: {material.category}
SETUP: {material.setup}
OBSERVATION: {material.observation}
WORDPLAY: {material.wordplay}
PUNCHLINE: {material.punchline}
BILINGUAL DELIVERY: {material.bilingual_delivery}
DELIVERY NOTES: {material.delivery_notes}

REQUIREMENTS:
1. Maintain bilingual flow (French/English/Turkish where appropriate)
2. Enhance punchline while keeping authenticity
3. Improve observational flow
4. Strengthen bilingual code-switching
5. Keep absurdist edge
6. Maintain Jean Morphius voice

Provide enhanced version with:
- Improved setup
- Enhanced observation
- Stronger punchline
- Better bilingual flow
- Delivery improvements
"""
    
    def _parse_enhancement(self, enhanced_text: str, original: ComedyMaterial) -> Dict[str, Any]:
        """Parse AI enhancement into structured format"""
        
        # Simple parsing - extract key sections
        enhanced = {
            "setup": original.setup,
            "observation": original.observation,
            "punchline": original.punchline,
            "bilingual_delivery": original.bilingual_delivery,
            "enhanced_text": enhanced_text,
            "improvements": []
        }
        
        # Try to extract structured improvements
        if "SETUP:" in enhanced_text:
            parts = enhanced_text.split("SETUP:")
            if len(parts) > 1:
                setup_part = parts[1].split("OBSERVATION:")[0] if "OBSERVATION:" in parts[1] else parts[1]
                enhanced["setup"] = setup_part.strip()
        
        if "PUNCHLINE:" in enhanced_text:
            parts = enhanced_text.split("PUNCHLINE:")
            if len(parts) > 1:
                enhanced["punchline"] = parts[1].strip()
        
        return enhanced
    
    def _identify_improvements(self, original: ComedyMaterial, enhanced: Dict[str, Any]) -> List[str]:
        """Identify specific improvements made"""
        
        improvements = []
        
        if enhanced.get("setup") != original.setup:
            improvements.append("Enhanced setup for better hook")
        
        if enhanced.get("punchline") != original.punchline:
            improvements.append("Strengthened punchline")
        
        if "bilingual" in enhanced.get("enhanced_text", "").lower():
            improvements.append("Improved bilingual flow")
        
        if "observational" in enhanced.get("enhanced_text", "").lower():
            improvements.append("Enhanced observational elements")
        
        return improvements if improvements else ["General enhancement applied"]
    
    def _calculate_enhancement_score(self, original: ComedyMaterial, enhanced: Dict[str, Any]) -> float:
        """Calculate enhancement score (0-100)"""
        
        score = 50.0  # Base score
        
        # Check for improvements
        if enhanced.get("setup") != original.setup:
            score += 10
        
        if enhanced.get("punchline") != original.punchline:
            score += 15
        
        if len(enhanced.get("enhanced_text", "")) > len(original.setup + original.punchline):
            score += 10
        
        if "bilingual" in enhanced.get("enhanced_text", "").lower():
            score += 15
        
        return min(100.0, score)
    
    def batch_enhance(self, materials: List[ComedyMaterial], use_claude: bool = True) -> List[EnhancedComedyMaterial]:
        """Batch enhance multiple materials"""
        
        enhanced = []
        
        for material in materials:
            try:
                result = self.enhance_material(material, use_claude)
                if result:
                    enhanced.append(result)
            except Exception as e:
                print(f"Error enhancing material: {e}")
                continue
        
        return enhanced
    
    def generate_improved_collection(self, count: int = 50, enhance: bool = True) -> Dict[str, Any]:
        """Generate and enhance comedy collection"""
        
        if not COMEDY_GENERATOR_AVAILABLE:
            return {"error": "Comedy generator not available"}
        
        # Generate base collection
        materials = generate_comedy_collection(count)
        
        # Enhance if requested
        enhanced_materials = []
        if enhance and AI_AVAILABLE:
            enhanced_materials = self.batch_enhance(materials, use_claude=True)
        
        # Convert materials to dict, handling ComedyStyle enum
        materials_dict = []
        for m in materials:
            m_dict = asdict(m)
            m_dict["style"] = m.style.value  # Convert enum to string
            materials_dict.append(m_dict)
        
        # Convert enhanced materials
        enhanced_dict = []
        for e in enhanced_materials:
            e_dict = asdict(e)
            enhanced_dict.append(e_dict)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_materials": len(materials),
            "enhanced_count": len(enhanced_materials),
            "materials": materials_dict,
            "enhanced": enhanced_dict if enhanced_materials else [],
            "improvements_summary": list(set(self.improvements_made)),
            "enhancement_count": self.enhancement_count
        }
    
    def save_enhanced_collection(self, collection: Dict[str, Any], output_dir: Path):
        """Save enhanced collection to JSON"""
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"jean_comedy_enhanced_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(collection, f, indent=2, ensure_ascii=False)
        
        return output_file


if __name__ == "__main__":
    print("=== JEAN MORPHIUS - COMEDY AI ENHANCER ===")
    print("\nGenerating and enhancing comedy material...")
    
    enhancer = JeanComedyAIEnhancer()
    
    # Generate improved collection
    collection = enhancer.generate_improved_collection(count=50, enhance=True)
    
    # Save collection
    output_dir = Path(__file__).parent.parent / "data" / "jean_comedy"
    output_file = enhancer.save_enhanced_collection(collection, output_dir)
    
    print(f"\nGenerated {collection['total_materials']} materials")
    print(f"Enhanced {collection['enhanced_count']} materials")
    print(f"Total improvements: {len(collection['improvements_summary'])}")
    print(f"\nCollection saved to: {output_file}")
    print("\nComedy enhancement complete!")
