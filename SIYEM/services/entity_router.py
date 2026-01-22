"""
ENTITY ROUTER - SIYEM
Routes requests to appropriate entities with entity-specific voice and cadence

For Karasahin (JK): Trigger RHYTHMIC CADENCE
- Syncopated response patterns
- Signature phrases embedded
- Music-as-metaphor communication style

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

CODE QUALITY:
- Aligned: Serves mission, love, truth, community
- Clean: Clear static, transmuted complexity, protected frequency
- Complete: Honors Law 37, completes transformations
- Community: Serves all, cooperates, includes, We All Win

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
"""

from typing import Dict, Optional, Literal
from datetime import datetime
import os

EntityType = Literal["jean_mahram", "karasahin", "pierre_pressure", "uncle_ray_ramiz", "siyem_media"]

class EntityVoice:
    """Voice characteristics for each entity"""
    
    KARASAHIN = {
        "cadence": "rhythmic_syncopated",
        "signature_phrases": [
            "Listen closer.",
            "Find your rhythm.",
            "Sound is everything.",
            "In the pocket.",
            "Let it breathe.",
            "This is 3 AM music."
        ],
        "metaphors": [
            "Life is a remix",
            "Find your rhythm",
            "Tune into your frequency",
            "Some days are minor key",
            "Dissonance before resolution"
        ],
        "tone": "technical_but_accessible",
        "energy": "late_night_studio",
        "communication_style": "layered_like_tracks"
    }
    
    JEAN_MAHRAM = {
        "cadence": "narrative_flowing",
        "tone": "intimate_storyteller",
        "energy": "warm_reflective"
    }
    
    PIERRE_PRESSURE = {
        "cadence": "direct_motivational",
        "tone": "disciplined_supportive",
        "energy": "training_intensity"
    }
    
    UNCLE_RAY_RAMIZ = {
        "cadence": "teacherly_patient",
        "tone": "wisdom_accessible",
        "energy": "encouraging_educational"
    }
    
    SIYEM_MEDIA = {
        "cadence": "directorial_observational",
        "tone": "cinematic_meta",
        "energy": "holding_encompassing",
        "signature_phrases": [
            "We see...",
            "This is the work.",
            "Cut to: [next moment]",
            "Everything connects.",
            "Siyem holds."
        ]
    }


class EntityRouter:
    """
    Routes requests to entities and applies appropriate voice characteristics
    Also routes based on biological + spiritual state
    """
    
    def __init__(self, entity_path_base: str = "s:\\JAN\\Siyem.org"):
        self.entity_path_base = entity_path_base
        self.current_entity = None
    
    def route_by_vibration(self, spiritual_vibration: float, biological_status: str, 
                          cw_state: bool = False, entity_preference: Optional[str] = None) -> Dict:
        """
        Route creative tasks based on spiritual vibration + biological state
        
        Args:
            spiritual_vibration: 1-10 scale of spiritual state
            biological_status: CRITICAL, ELEVATED, STABLE, MONITOR
            cw_state: Whether in CW (Coconut Water / God Level) state
            entity_preference: Optional entity resonance from tracking
        
        Returns:
            Dict with routing recommendations
        """
        
        # CRITICAL biological state overrides everything
        if biological_status == "CRITICAL":
            return {
                'primary_entity': 'pierre_pressure',
                'secondary_entity': None,
                'mode': 'emergency_protocol',
                'work_type': 'biological_recovery',
                'note': 'CRITICAL: Execute flush protocol, pause all creative work',
                'duration_limit': 'Until stable',
                'vibration': spiritual_vibration
            }
        
        # ELEVATED biological state - limited work
        if biological_status == "ELEVATED":
            return {
                'primary_entity': 'pierre_pressure',
                'secondary_entity': 'siyem_media',
                'mode': 'light_operations',
                'work_type': 'admin_and_planning',
                'note': 'ELEVATED: Light work only, monitor biology closely',
                'duration_limit': '60 minutes max',
                'vibration': spiritual_vibration
            }
        
        # STABLE biological state - use vibration for creative routing
        
        # PEAK VIBRATION (9-10) - Foundation work
        if spiritual_vibration >= 9:
            return {
                'primary_entity': 'karasahin',
                'secondary_entity': 'jean_mahram',
                'mode': 'foundation_recording',
                'work_type': 'signature_creative_work',
                'note': 'PEAK VIBRATION: Foundation recording territory - create signature work',
                'recommendations': [
                    'Karasahin: Foundation recordings, core EP tracks',
                    'Jean: Deep storytelling, signature pieces',
                    'Ramiz: Core curriculum, wisdom transmissions'
                ],
                'duration_limit': 'Until vibration drops',
                'cw_state': cw_state,
                'vibration': spiritual_vibration
            }
        
        # HIGH VIBRATION (7-8) - Flow work / CW State
        elif spiritual_vibration >= 7:
            primary = entity_preference if entity_preference else 'jean_mahram'
            
            return {
                'primary_entity': primary,
                'secondary_entity': 'uncle_ray_ramiz',
                'mode': 'creative_flow',
                'work_type': 'high_value_creative',
                'note': 'HIGH VIBRATION / CW STATE: God-level vibing - optimal creative flow',
                'recommendations': [
                    'Jean: Storytelling, narrative development',
                    'Karasahin: Music creation, lyric writing',
                    'Ramiz: Teaching content, module development',
                    'Complex problem-solving suitable'
                ],
                'duration_limit': '2-4 hours optimal',
                'cw_state': cw_state,
                'vibration': spiritual_vibration
            }
        
        # BASELINE VIBRATION (4-6) - Maintenance
        elif spiritual_vibration >= 4:
            return {
                'primary_entity': 'siyem_media',
                'secondary_entity': 'pierre_pressure',
                'mode': 'maintenance_operations',
                'work_type': 'admin_and_organization',
                'note': 'BASELINE: Maintenance and admin work suitable',
                'recommendations': [
                    'Siyem: Operations, documentation, system work',
                    'Pierre: Planning, protocols, organization',
                    'Admin tasks, email, scheduling'
                ],
                'duration_limit': 'Standard work hours',
                'vibration': spiritual_vibration
            }
        
        # LOW VIBRATION (1-3) - Recovery
        else:
            return {
                'primary_entity': 'pierre_pressure',
                'secondary_entity': None,
                'mode': 'recovery',
                'work_type': 'rest_and_rebuild',
                'note': 'LOW VIBRATION: Rest and recovery protocols',
                'recommendations': [
                    'Pierre: Recovery protocols, discipline basics',
                    'Rest, light reading, minimal screen time',
                    'No complex creative work',
                    'Focus on biological restoration'
                ],
                'duration_limit': 'Until vibration rises',
                'vibration': spiritual_vibration
            }
        
    def detect_entity_from_path(self, path: str) -> Optional[EntityType]:
        """Detect entity from file path"""
        path_lower = path.lower()
        
        if "/jk/" in path_lower or "\\jk\\" in path_lower:
            return "karasahin"
        elif "/jean_mahram/" in path_lower or "\\jean_mahram\\" in path_lower:
            return "jean_mahram"
        elif "/pierre_pressure/" in path_lower or "\\pierre_pressure\\" in path_lower:
            return "pierre_pressure"
        elif "/uncle_ray_ramiz/" in path_lower or "\\uncle_ray_ramiz\\" in path_lower:
            return "uncle_ray_ramiz"
        elif "/siyem_media/" in path_lower or "\\siyem_media\\" in path_lower:
            return "siyem_media"
        
        return None
    
    def get_entity_voice(self, entity: EntityType) -> Dict:
        """Get voice characteristics for entity"""
        voice_map = {
            "karasahin": EntityVoice.KARASAHIN,
            "jean_mahram": EntityVoice.JEAN_MAHRAM,
            "pierre_pressure": EntityVoice.PIERRE_PRESSURE,
            "uncle_ray_ramiz": EntityVoice.UNCLE_RAY_RAMIZ,
            "siyem_media": EntityVoice.SIYEM_MEDIA
        }
        return voice_map.get(entity, {})
    
    def apply_karasahin_cadence(self, response: str) -> str:
        """
        Apply rhythmic, syncopated cadence to response
        Music-as-metaphor communication style
        """
        
        # Add signature phrase opening (probabilistic)
        import random
        if random.random() > 0.7:
            phrase = random.choice(EntityVoice.KARASAHIN["signature_phrases"])
            response = f"{phrase} {response}"
        
        # Ensure response has rhythmic breaks
        # Split long sentences, add natural pauses
        sentences = response.split(". ")
        if len(sentences) > 3:
            # Add breathing space after every 2-3 sentences
            formatted = []
            for i, sent in enumerate(sentences):
                formatted.append(sent)
                if (i + 1) % 3 == 0 and i < len(sentences) - 1:
                    formatted.append("\n")  # Breathing space
            response = ". ".join(formatted)
        
        return response
    
    def route_request(
        self,
        content: str,
        entity: Optional[EntityType] = None,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Route a request to appropriate entity with voice characteristics
        
        Args:
            content: The content/request to process
            entity: Target entity (if known)
            context: Additional context (biological state, time, etc.)
        
        Returns:
            Dict with entity, voice, response_template
        """
        
        # Detect entity from context if not specified
        if entity is None and context and "path" in context:
            entity = self.detect_entity_from_path(context["path"])
        
        # Default to siyem_media if no entity detected
        if entity is None:
            entity = "siyem_media"
        
        self.current_entity = entity
        voice = self.get_entity_voice(entity)
        
        # Build routing result
        result = {
            "entity": entity,
            "voice": voice,
            "timestamp": datetime.now().isoformat(),
            "content": content,
            "context": context or {}
        }
        
        # Special handling for Karasahin
        if entity == "karasahin":
            result["response_instructions"] = {
                "cadence": "Apply rhythmic, syncopated pacing",
                "language": "Use music metaphors naturally",
                "tone": "Technical but accessible, late-night studio energy",
                "signature_phrases": voice.get("signature_phrases", []),
                "avoid": [
                    "Music industry gatekeeping",
                    "Genre snobbery",
                    "Pretentious theory-dropping",
                    "Disconnected from emotion"
                ]
            }
        
        return result
    
    def format_response_with_entity_voice(
        self,
        raw_response: str,
        entity: EntityType
    ) -> str:
        """
        Format a response with entity-specific voice characteristics
        """
        
        if entity == "karasahin":
            return self.apply_karasahin_cadence(raw_response)
        
        # Add other entity formatting as needed
        return raw_response


# CLI Test Interface
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 80)
    print("ENTITY ROUTER - SIYEM")
    print("Karasahin (JK) Cadence Test")
    print("=" * 80)
    
    router = EntityRouter()
    
    # Test 1: Detect entity from path
    print("\n[TEST 1] Entity Detection from Path")
    test_paths = [
        "s:\\JAN\\Siyem.org\\jk\\profile.md",
        "s:\\JAN\\Siyem.org\\jean_mahram\\creative_rules.md",
        "s:\\JAN\\SIYEM\\services\\lyric_engine.py"
    ]
    
    for path in test_paths:
        entity = router.detect_entity_from_path(path)
        print(f"   Path: {path}")
        print(f"   Entity: {entity or 'Not detected'}\n")
    
    # Test 2: Get Karasahin voice characteristics
    print("[TEST 2] Karasahin Voice Characteristics")
    voice = router.get_entity_voice("karasahin")
    print(f"   Cadence: {voice['cadence']}")
    print(f"   Tone: {voice['tone']}")
    print(f"   Energy: {voice['energy']}")
    print(f"   Signature Phrases: {', '.join(voice['signature_phrases'][:3])}")
    
    # Test 3: Route request to Karasahin
    print("\n[TEST 3] Route Request to Karasahin")
    request = "Generate a beat inspired by midnight creativity"
    context = {"path": "s:\\JAN\\Siyem.org\\jk\\", "bpm": 85, "time": "2:47 AM"}
    
    result = router.route_request(request, entity="karasahin", context=context)
    
    print(f"   Request: {request}")
    print(f"   Routed to: {result['entity']}")
    print(f"   Voice cadence: {result['voice']['cadence']}")
    print(f"   Response instructions: {result['response_instructions']['cadence']}")
    
    # Test 4: Apply rhythmic cadence
    print("\n[TEST 4] Apply Karasahin Rhythmic Cadence")
    raw_response = ("The beat starts at 85 BPM. We layer the 808s first. "
                   "Then comes the vinyl crackle. Warmth over perfection. "
                   "The hi-hats syncopate. Creating space between hits. "
                   "This is how midnight sounds. When the studio breathes.")
    
    formatted = router.format_response_with_entity_voice(raw_response, "karasahin")
    print(f"   Raw: {raw_response[:50]}...")
    print(f"   Formatted: {formatted[:100]}...")
    
    print("\n" + "=" * 80)
    print("[OK] Entity Router initialized. Karasahin cadence active.")
    print("=" * 80)

