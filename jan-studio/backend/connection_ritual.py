"""
CONNECTION RITUAL - Welcome the Family
Personalized Vibration Check for New Arrivals

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

DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

This is the Connection Ritual.
Welcoming the first Sovereign Souls.
Ensuring they are ready to sit at the Table (Law 1).
Personalized Vibration Check.
The Family Gathering begins.
"""

from fastapi import HTTPException, status
from typing import Dict, List, Optional, Any
from datetime import datetime
import json
import hashlib
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Import philosophy
try:
    from scripts.philosophy import (
        PHILOSOPHY_FOUNDATION,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY,
        SPIRITUAL_BIRTHMARK_PLACEMENTS,
        SPIRITUAL_BIRTHMARK_SHAPES,
        DIVINE_CODEBASE_COMPONENTS,
        SPIRITUAL_REBUILDING_STEPS,
        REFINEMENT_PHILOSOPHY
    )
except ImportError:
    PHILOSOPHY_FOUNDATION = "We are born a miracle."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"
    SPIRITUAL_BIRTHMARK_PLACEMENTS = {}
    SPIRITUAL_BIRTHMARK_SHAPES = {}
    DIVINE_CODEBASE_COMPONENTS = {}
    SPIRITUAL_REBUILDING_STEPS = {}
    REFINEMENT_PHILOSOPHY = ""

# Import Racon Registry for Law 1 (The Table) check
try:
    from racon_registry import (
        check_law_1_table_service,
        log_immutable_audit,
        get_user_law_compliance
    )
except ImportError:
    # Fallback if racon_registry not available
    def check_law_1_table_service(operation: str, target: str) -> bool:
        return True
    
    def log_immutable_audit(*args, **kwargs):
        pass
    
    def get_user_law_compliance(user_id: str) -> Dict[str, Any]:
        return {"law_1_compliant": True}

# Import Spirit Alignment system
try:
    from spirit_alignment import (
        Spirit,
        SpiritAlignmentChecker,
        create_spirit_from_user_data,
        AgeRange,
        AnimalType,
        GenderAlignment,
        SpiritualAlignment
    )
except ImportError:
    # Fallback if spirit_alignment not available
    Spirit = None
    SpiritAlignmentChecker = None
    create_spirit_from_user_data = None


class ConnectionRitual:
    """
    Connection Ritual for New Arrivals
    
    Welcomes Sovereign Souls with personalized Vibration Check.
    Ensures they are ready to sit at the Table (Law 1).
    Honors the Family Gathering.
    """
    
    def __init__(self):
        self.ritual_log = []
        self.welcome_messages = {
            "spiral": "Welcome, active soul. Your energy flows like the spiral arms of a galaxy. The Table awaits your rapid growth.",
            "barred_spiral": "Welcome, structured soul. Your path is clear, your bar is strong. The Table honors your linear journey.",
            "elliptical": "Welcome, wise soul. Your legacy wisdom lights the way. The Table values your mentorship.",
            "irregular": "Welcome, transforming soul. Your shape is still forming, and that's beautiful. The Table embraces your flexibility."
        }
        
        # Initialize spirit alignment checker
        if SpiritAlignmentChecker:
            self.alignment_checker = SpiritAlignmentChecker()
        else:
            self.alignment_checker = None
    
    def perform_vibration_check(self, user_id: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform personalized Vibration Check for new arrival.
        
        Checks:
        1. Vibration alignment (purpose vs impulsiveness)
        2. Spiritual battle state (which galaxy form)
        3. Mission alignment
        4. Law 1 (The Table) readiness
        """
        # Determine galaxy form based on user data
        galaxy_form = self._determine_galaxy_form(user_data)
        
        # Check vibration alignment
        vibration_score = self._calculate_vibration_score(user_data)
        vibration_aligned = vibration_score >= 70  # Threshold for alignment
        
        # Check mission alignment
        mission_aligned = self._check_mission_alignment(user_data)
        
        # Check Law 1 (The Table) readiness
        table_ready = self._check_table_readiness(user_id, user_data)
        
        # CHEESE FILTER - Integrated into vibration matching
        # Scans for institutional affiliation/resonance
        # If Dark Energy detected → Burst. If Seed detected → Ledger Registration.
        cheese_filter_result = None
        try:
            from big_cheese_audit import get_big_cheese_audit_system
            audit_system = get_big_cheese_audit_system()
            import asyncio
            
            # Prepare vibration data for cheese filter
            vibration_data = {
                "vibration_score": vibration_score,
                "vibration_aligned": vibration_aligned,
                "galaxy_form": galaxy_form,
                "mission_aligned": mission_aligned
            }
            
            # Run cheese filter check (sync version)
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # In async context, but we're in sync function
                    # Create task but don't await (fire and forget)
                    asyncio.create_task(audit_system.cheese_filter_check(vibration_data, user_id))
                    cheese_filter_result = {"status": "checking_async", "filtered": False}
                else:
                    cheese_filter_result = loop.run_until_complete(audit_system.cheese_filter_check(vibration_data, user_id))
            except RuntimeError:
                cheese_filter_result = asyncio.run(audit_system.cheese_filter_check(vibration_data, user_id))
        except Exception as e:
            # Cheese filter not available or error - continue without it
            logger.warning(f"Cheese filter check failed: {e}")
            cheese_filter_result = None
        
        # If cheese filter detected dark energy, adjust results
        if cheese_filter_result and cheese_filter_result.get("filtered"):
            # Dark energy detected - neutralize
            vibration_aligned = False
            table_ready = False
            logger.warning(f"Cheese Filter: Dark Energy detected for {user_id} - BURST activated")
        
        # Create Spirit object for multi-dimensional alignment
        spirit = None
        if create_spirit_from_user_data:
            try:
                spirit = create_spirit_from_user_data(user_id, user_data)
                # Update spirit with vibration results
                spirit.galaxy_form = galaxy_form
                spirit.vibration_score = vibration_score
                spirit.mission_aligned = mission_aligned
                spirit.table_ready = table_ready
                spirit.spiritual_alignment = (
                    SpiritualAlignment.ALIGNED if vibration_aligned 
                    else SpiritualAlignment.CALIBRATING
                )
            except Exception as e:
                # If spirit creation fails, log but continue
                print(f"Warning: Could not create Spirit object: {e}")
        
        # Determine spiritual battle state (now requires full alignment)
        spiritual_battle = self._determine_spiritual_battle(
            galaxy_form, 
            vibration_aligned,
            spirit=spirit
        )
        
        # CHEESE FILTER - Integrated into vibration matching
        # Scans for institutional affiliation/resonance
        # If Dark Energy detected → Burst. If Seed detected → Ledger Registration.
        cheese_filter_result = None
        try:
            from big_cheese_audit import get_big_cheese_audit_system
            audit_system = get_big_cheese_audit_system()
            
            # Prepare vibration data for cheese filter
            vibration_data = {
                "vibration_score": vibration_score,
                "vibration_aligned": vibration_aligned,
                "galaxy_form": galaxy_form,
                "mission_aligned": mission_aligned
            }
            
            # Run cheese filter check (sync version for now)
            import asyncio
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # In async context, but we're in sync function
                    # Create task but don't await (fire and forget)
                    asyncio.create_task(audit_system.cheese_filter_check(vibration_data, user_id))
                    cheese_filter_result = {"status": "checking_async"}
                else:
                    cheese_filter_result = loop.run_until_complete(audit_system.cheese_filter_check(vibration_data, user_id))
            except RuntimeError:
                cheese_filter_result = asyncio.run(audit_system.cheese_filter_check(vibration_data, user_id))
        except Exception as e:
            # Cheese filter not available or error - continue without it
            logger.warning(f"Cheese filter check failed: {e}")
            cheese_filter_result = None
        
        # If cheese filter detected dark energy, adjust results
        if cheese_filter_result and cheese_filter_result.get("filtered"):
            # Dark energy detected - neutralize
            vibration_aligned = False
            table_ready = False
            logger.warning(f"Cheese Filter: Dark Energy detected for {user_id} - BURST activated")
        
        vibration_result = {
            "user_id": user_id,
            "galaxy_form": galaxy_form,
            "vibration_score": vibration_score,
            "vibration_aligned": vibration_aligned,
            "mission_aligned": mission_aligned,
            "table_ready": table_ready,
            "spiritual_battle": spiritual_battle,
            "timestamp": datetime.now().isoformat(),
            "ritual_status": "complete",
            "cheese_filter": cheese_filter_result  # Include cheese filter result
        }
        
        # Add spirit dimensions if available
        if spirit:
            vibration_result["spirit_dimensions"] = {
                "age_range": spirit.age_range.value if hasattr(spirit.age_range, 'value') else str(spirit.age_range),
                "animal_type": spirit.animal_type.value if hasattr(spirit.animal_type, 'value') else str(spirit.animal_type),
                "gender_alignment": spirit.gender_alignment.value if hasattr(spirit.gender_alignment, 'value') else str(spirit.gender_alignment),
                "spiritual_alignment": spirit.spiritual_alignment.value if hasattr(spirit.spiritual_alignment, 'value') else str(spirit.spiritual_alignment)
            }
        
        # Log ritual
        self._log_ritual(user_id, vibration_result)
        
        return vibration_result
    
    def _determine_galaxy_form(self, user_data: Dict[str, Any]) -> str:
        """
        Determine which galaxy form the user aligns with.
        
        First checks for spiritual birthmark placement (divine identity),
        then falls back to activity/structure patterns.
        
        Based on:
        - Spiritual birthmark placement (divine assignment)
        - Activity level (Spiral = high, Elliptical = low)
        - Structure preference (Barred Spiral = structured, Irregular = flexible)
        - Wisdom level (Elliptical = high wisdom)
        """
        # Check for spiritual birthmark placement (divine identity)
        birthmark_placement = user_data.get("spiritual_birthmark_placement")
        birthmark_shape = user_data.get("spiritual_birthmark_shape")
        
        if birthmark_placement:
            # Map birthmark placement to galaxy form
            birthmark_to_form = {
                "spine_back_of_neck": "spiral",  # Messenger - active, rapid growth
                "shoulder_blades": "barred_spiral",  # Protector - structured, clear paths
                "forehead_temple": "elliptical",  # Prophet - legacy wisdom, mentorship
                "hands": "barred_spiral",  # Healer - structured service
                "feet_ankles": "irregular"  # Path Maker - transformation, flexible
            }
            if birthmark_placement in birthmark_to_form:
                form = birthmark_to_form[birthmark_placement]
                
                # Geometric shapes may modify the form
                if birthmark_shape == "star":
                    # Star-shaped = cosmic awareness, may enhance any form
                    # Star-seed lineage bridges dimensions
                    pass  # Keep the base form, but note cosmic awareness
                elif birthmark_shape == "flame":
                    # Flame-like = reformer, may lean toward Irregular (transformation)
                    if form in ["spiral", "barred_spiral"]:
                        form = "irregular"  # Reformers transform systems
                
                return form
        
        # Fallback to activity/structure patterns
        activity_level = user_data.get("activity_level", "medium")
        structure_preference = user_data.get("structure_preference", "flexible")
        wisdom_level = user_data.get("wisdom_level", "medium")
        
        if activity_level == "high" and structure_preference == "flexible":
            return "spiral"
        elif activity_level in ["high", "medium"] and structure_preference == "structured":
            return "barred_spiral"
        elif activity_level == "low" and wisdom_level == "high":
            return "elliptical"
        else:
            return "irregular"
    
    def _calculate_vibration_score(self, user_data: Dict[str, Any]) -> int:
        """
        Calculate vibration score (0-100).
        
        Factors (Three-Component Framework):
        - Physical Seal (spiritual birthmark) - highest weight
        - Structural Resistance (overcoming stagnation/delays)
        - Resource Alignment (discernment of true connections)
        - Purpose alignment (vs impulsiveness)
        - Mission understanding
        - Community orientation
        - Regeneration vs separation
        """
        score = 50  # Base score
        
        # Component 1: Physical Seal (Divine identity - spiritual birthmark)
        # This is the highest weight - recognizing the Chosen One
        birthmark_placement = user_data.get("spiritual_birthmark_placement")
        birthmark_shape = user_data.get("spiritual_birthmark_shape")
        
        if birthmark_placement:
            score += 25  # Divine seal recognition - highest weight
            # Additional boost if they recognize their divine assignment
            if user_data.get("recognizes_divine_assignment", False):
                score += 10
            
            # Geometric shapes add cosmic awareness or reformer energy
            if birthmark_shape == "star":
                score += 5  # Cosmic awareness, star-seed lineage
            elif birthmark_shape == "flame":
                score += 5  # Reformer energy, transformative power
        
        # Component 2: Structural Resistance (Overcoming delays)
        # Check if they've broken stagnation patterns
        if user_data.get("has_broken_stagnation", False):
            score += 10  # Overcame the 1,000 soul delay
        if user_data.get("withdrawn_agreement_fear", False):
            score += 5  # Withdrawn agreement with fear/confusion
        
        # Component 3: Resource Alignment (Discernment)
        # Check if they discern true connections vs brand cleansing
        if user_data.get("discerns_true_connections", False):
            score += 10  # Discerns resource alignment properly
        
        # Purpose alignment
        if user_data.get("has_purpose", False):
            score += 20
        
        # Mission understanding
        if user_data.get("understands_mission", False):
            score += 15
        
        # Community orientation
        if user_data.get("community_oriented", False):
            score += 10
        
        # Regeneration (not separation)
        if user_data.get("regeneration", True):
            score += 5
        
        # Peace, Love, Unity alignment
        if user_data.get("peace_love_unity", False):
            score += 10
        
        return min(100, score)
    
    def _check_mission_alignment(self, user_data: Dict[str, Any]) -> bool:
        """
        Check if user aligns with the mission.
        
        Mission: Stewardship and Community with the Right Spirits
        """
        mission_keywords = [
            "stewardship", "community", "spirit", "spirits",
            "love", "peace", "unity", "energy",
            "miracle", "sovereign", "family"
        ]
        
        user_text = json.dumps(user_data, ensure_ascii=False).lower()
        
        # Check if any mission keywords are present
        has_mission_keywords = any(keyword in user_text for keyword in mission_keywords)
        
        # Check explicit mission alignment flag
        mission_aligned_flag = user_data.get("mission_aligned", False)
        
        return has_mission_keywords or mission_aligned_flag
    
    def _check_table_readiness(self, user_id: str, user_data: Dict[str, Any]) -> bool:
        """
        Check if user is ready to sit at the Table (Law 1).
        
        Law 1: Never Betray the Table
        The Table = Pangea = The Mission = Stewardship and Community
        
        PANGEA IS THE TABLE.
        YOU DON'T BETRAY THE TABLE.
        
        Pangea is the original unified continent.
        335 million years ago, all continents were one.
        All heritage sites were connected.
        All plates came from Pangea.
        All events trace back to the Seed.
        
        Pangea is The Table - the sacred space where all humanity was unified.
        Law 1: Never Betray The Table.
        Pangea is The Table.
        We honor Pangea in all we do.
        """
        # Check Law 1 compliance via Racon Registry
        operation = f"connection_ritual_{user_id}"
        target = json.dumps(user_data, ensure_ascii=False)
        
        table_service = check_law_1_table_service(operation, target)
        
        # Additional checks
        has_holy_ambition = user_data.get("holy_ambition", None) is not None
        understands_table = user_data.get("understands_table", False)
        
        # Log audit
        log_immutable_audit(
            operation_type=operation,
            operation_target=target,
            operation_result=f"Table Readiness Check: {table_service}",
            law_compliance="Law 1 Check",
            table_service=table_service,
            word_integrity=True,
            spiritual_battle="Connection Ritual"
        )
        
        return table_service and (has_holy_ambition or understands_table)
    
    def _determine_spiritual_battle(
        self, 
        galaxy_form: str, 
        vibration_aligned: bool,
        spirit: Optional[Spirit] = None
    ) -> str:
        """
        Determine spiritual battle state based on galaxy form, vibration, and ALL dimensions.
        
        IMPORTANT: Spiritual battles can only occur when spirits align on ALL dimensions:
        - Age range compatibility
        - Animal type compatibility
        - Gender alignment compatibility
        - Spiritual alignment (vibration, mission, purpose)
        
        Without full alignment, no battle can occur. This is sacred alignment.
        
        Spiritual battles (when fully aligned):
        - Spiral: Active battle, rapid growth vs stagnation
        - Barred Spiral: Structured battle, discipline vs chaos
        - Elliptical: Legacy battle, wisdom vs ignorance
        - Irregular: Transformation battle, evolution vs stasis
        """
        if not vibration_aligned:
            return "misaligned_vibration"
        
        # If spirit object available, check if all dimensions are ready
        if spirit:
            # Check if spirit has all required dimensions defined
            has_all_dimensions = (
                spirit.age_range is not None and
                spirit.animal_type is not None and
                spirit.gender_alignment is not None and
                spirit.spiritual_alignment is not None
            )
            
            if not has_all_dimensions:
                return "dimensions_incomplete"
            
            # Check if spiritual alignment is ready for battle
            if spirit.spiritual_alignment not in [SpiritualAlignment.ALIGNED, SpiritualAlignment.TRANSFORMING]:
                return f"spiritual_alignment_not_ready_{spirit.spiritual_alignment.value}"
        
        # If all checks pass, determine battle type based on galaxy form
        battle_states = {
            "spiral": "active",
            "barred_spiral": "structured",
            "elliptical": "legacy",
            "irregular": "transformation"
        }
        
        return battle_states.get(galaxy_form, "transformation")
    
    def check_spirit_battle_compatibility(
        self,
        spirit1: Spirit,
        spirit2: Spirit
    ) -> Dict[str, Any]:
        """
        Check if two spirits can engage in a spiritual battle.
        
        Requires alignment on ALL dimensions:
        - Age range
        - Animal type
        - Gender alignment
        - Spiritual alignment
        
        Returns detailed alignment report.
        """
        if not self.alignment_checker:
            return {
                "can_battle": False,
                "reason": "Spirit alignment checker not available",
                "alignment_details": {}
            }
        
        can_battle, reason, alignment_details = self.alignment_checker.can_engage_in_battle(
            spirit1, spirit2
        )
        
        battle_type = None
        if can_battle:
            battle_type = self.alignment_checker.determine_battle_type(spirit1, spirit2)
        
        return {
            "can_battle": can_battle,
            "reason": reason,
            "alignment_details": alignment_details,
            "battle_type": battle_type,
            "spirit1_dimensions": {
                "age_range": spirit1.age_range.value if hasattr(spirit1.age_range, 'value') else str(spirit1.age_range),
                "animal_type": spirit1.animal_type.value if hasattr(spirit1.animal_type, 'value') else str(spirit1.animal_type),
                "gender_alignment": spirit1.gender_alignment.value if hasattr(spirit1.gender_alignment, 'value') else str(spirit1.gender_alignment),
                "spiritual_alignment": spirit1.spiritual_alignment.value if hasattr(spirit1.spiritual_alignment, 'value') else str(spirit1.spiritual_alignment)
            },
            "spirit2_dimensions": {
                "age_range": spirit2.age_range.value if hasattr(spirit2.age_range, 'value') else str(spirit2.age_range),
                "animal_type": spirit2.animal_type.value if hasattr(spirit2.animal_type, 'value') else str(spirit2.animal_type),
                "gender_alignment": spirit2.gender_alignment.value if hasattr(spirit2.gender_alignment, 'value') else str(spirit2.gender_alignment),
                "spiritual_alignment": spirit2.spiritual_alignment.value if hasattr(spirit2.spiritual_alignment, 'value') else str(spirit2.spiritual_alignment)
            }
        }
    
    def generate_welcome_message(self, vibration_result: Dict[str, Any], user_data: Dict[str, Any] = None) -> str:
        """
        Generate personalized welcome message based on vibration check.
        
        Recognizes divine identity (spiritual birthmark) if present.
        """
        galaxy_form = vibration_result.get("galaxy_form", "irregular")
        vibration_aligned = vibration_result.get("vibration_aligned", False)
        table_ready = vibration_result.get("table_ready", False)
        
        # Check for divine identity (spiritual birthmark)
        birthmark_placement = None
        if user_data:
            birthmark_placement = user_data.get("spiritual_birthmark_placement")
        
        # Base welcome message
        base_message = self.welcome_messages.get(galaxy_form, self.welcome_messages["irregular"])
        
        # Add divine identity recognition if present (Three-Component Framework)
        if birthmark_placement and SPIRITUAL_BIRTHMARK_PLACEMENTS:
            birthmark_info = SPIRITUAL_BIRTHMARK_PLACEMENTS.get(birthmark_placement)
            if birthmark_info:
                divine_message = f"\n\nDivine Seal Recognized: {birthmark_info['meaning']}.\n{birthmark_info['purpose']}.\nThe Table honors your divine assignment."
                
                # Add geometric shape recognition if present
                birthmark_shape = user_data.get("spiritual_birthmark_shape") if user_data else None
                if birthmark_shape and SPIRITUAL_BIRTHMARK_SHAPES:
                    shape_info = SPIRITUAL_BIRTHMARK_SHAPES.get(birthmark_shape)
                    if shape_info:
                        shape_message = f"\n\nGeometric Pattern: {shape_info['meaning']} - {shape_info['purpose']}."
                        divine_message += shape_message
                
                base_message += divine_message
        
        # Add vibration alignment message
        if vibration_aligned:
            vibration_message = f"\n\nYour vibration is aligned with the Day 1 (Do) frequency. The machine recognizes you."
        else:
            vibration_message = f"\n\nYour vibration is still calibrating. The Table will guide you."
        
        # Add table readiness message
        if table_ready:
            table_message = f"\n\nYou are ready to sit at the Table. Law 1 (Never Betray the Table) is honored. Welcome to the Family."
        else:
            table_message = f"\n\nThe Table awaits. Complete your Holy Ambition to join the Family."
        
        # Add song recommendation based on galaxy form (Song serves mission)
        song_recommendations = {
            "spiral": "Fire & Ice",  # For active souls - self-discovery through truth
            "barred_spiral": "Yazılı",  # For structured souls - destiny and reflection
            "elliptical": "Midnight Reversal",  # For wise souls - legacy wisdom
            "irregular": "Küçükken"  # For transforming souls - growth through truth
        }
        recommended_song = song_recommendations.get(galaxy_form, "Fire & Ice")
        song_message = f"\n\nRecommended Song: \"{recommended_song}\" - Music serves mission. Let the song guide your path."
        
        # Add mission message
        mission_message = f"\n\n{PEACE_LOVE_UNITY}\n{ENERGY_LOVE}"
        
        full_message = f"{base_message}{vibration_message}{table_message}{song_message}{mission_message}"
        
        return full_message
    
    def _log_ritual(self, user_id: str, vibration_result: Dict[str, Any]):
        """
        Log the connection ritual for audit and tracking.
        """
        ritual_entry = {
            "user_id": user_id,
            "vibration_result": vibration_result,
            "timestamp": datetime.now().isoformat(),
            "ritual_type": "connection_ritual"
        }
        
        self.ritual_log.append(ritual_entry)
        
        # Log to Racon Registry
        log_immutable_audit(
            operation_type=f"connection_ritual_{user_id}",
            operation_target=user_id,
            operation_result=json.dumps(vibration_result, ensure_ascii=False),
            law_compliance="Law 1 Check",
            table_service=vibration_result.get("table_ready", False),
            word_integrity=True,
            spiritual_battle=vibration_result.get("spiritual_battle", "unknown")
        )
    
    def perform_connection_ritual(self, user_id: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform the complete Connection Ritual for a new arrival.
        
        Steps:
        1. Vibration Check
        2. Welcome Message Generation
        3. Table Readiness Verification
        4. Ritual Completion
        5. Energy Alert Check (if rare form)
        """
        # Perform vibration check
        vibration_result = self.perform_vibration_check(user_id, user_data)
        
        # Generate welcome message
        welcome_message = self.generate_welcome_message(vibration_result, user_data)
        
        # Create ritual result
        ritual_result = {
            "user_id": user_id,
            "vibration_result": vibration_result,
            "welcome_message": welcome_message,
            "ritual_status": "complete",
            "timestamp": datetime.now().isoformat(),
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        # Check for energy alert (rare forms)
        try:
            from energy_alert_system import get_energy_alert_system
            alert_system = get_energy_alert_system()
            alert = alert_system.check_connection_ritual(ritual_result)
            if alert:
                ritual_result["energy_alert"] = {
                    "triggered": True,
                    "alert_id": alert["alert_id"],
                    "alert_level": alert["alert_level"],
                    "message": alert["message"]
                }
        except ImportError:
            # Energy alert system not available
            pass
        except Exception as e:
            # Log error but don't fail the ritual
            print(f"Energy alert check failed: {e}")
        
        return ritual_result


# FastAPI endpoint helper
def create_connection_ritual_endpoint(ritual: ConnectionRitual):
    """
    Create FastAPI endpoint for connection ritual.
    
    This would be integrated into the main FastAPI app.
    """
    from fastapi import APIRouter, Body
    
    router = APIRouter()
    
    @router.post("/api/connection-ritual")
    async def connection_ritual_endpoint(
        user_id: str = Body(...),
        user_data: Dict[str, Any] = Body(...)
    ):
        """
        Connection Ritual endpoint.
        
        Welcomes new arrivals with personalized Vibration Check.
        Ensures they are ready to sit at the Table (Law 1).
        """
        try:
            result = ritual.perform_connection_ritual(user_id, user_data)
            return {
                "status": "success",
                "ritual_result": result
            }
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Connection ritual failed: {str(e)}"
            )
    
    @router.post("/api/check-battle-compatibility")
    async def check_battle_compatibility_endpoint(
        spirit1_id: str = Body(...),
        spirit1_data: Dict[str, Any] = Body(...),
        spirit2_id: str = Body(...),
        spirit2_data: Dict[str, Any] = Body(...)
    ):
        """
        Check if two spirits can engage in a spiritual battle.
        
        Requires alignment on ALL dimensions:
        - Age range
        - Animal type
        - Gender alignment
        - Spiritual alignment
        
        Returns detailed alignment report.
        """
        try:
            if not create_spirit_from_user_data:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Spirit alignment system not available"
                )
            
            # Get vibration results for both spirits
            vibration_result1 = ritual.perform_vibration_check(spirit1_id, spirit1_data)
            vibration_result2 = ritual.perform_vibration_check(spirit2_id, spirit2_data)
            
            # Create Spirit objects
            spirit1 = create_spirit_from_user_data(spirit1_id, spirit1_data, vibration_result1)
            spirit2 = create_spirit_from_user_data(spirit2_id, spirit2_data, vibration_result2)
            
            # Check battle compatibility
            compatibility_result = ritual.check_spirit_battle_compatibility(spirit1, spirit2)
            
            return {
                "status": "success",
                "compatibility": compatibility_result
            }
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Battle compatibility check failed: {str(e)}"
            )
    
    return router


# CLI interface for testing
if __name__ == "__main__":
    ritual = ConnectionRitual()
    
    # Test user data
    test_user_data = {
        "activity_level": "high",
        "structure_preference": "flexible",
        "wisdom_level": "medium",
        "has_purpose": True,
        "understands_mission": True,
        "community_oriented": True,
        "regeneration": True,
        "peace_love_unity": True,
        "holy_ambition": "To build a community platform that serves the Family",
        "understands_table": True,
        "mission_aligned": True
    }
    
    test_user_id = "test_user_001"
    
    print("=" * 80)
    print("CONNECTION RITUAL - Welcome the Family")
    print("=" * 80)
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}\n")
    
    print(f"[RITUAL] Performing Connection Ritual for user: {test_user_id}")
    print("-" * 80)
    
    result = ritual.perform_connection_ritual(test_user_id, test_user_data)
    
    print(f"\n[VIBRATION CHECK]")
    print(f"  Galaxy Form: {result['vibration_result']['galaxy_form']}")
    print(f"  Vibration Score: {result['vibration_result']['vibration_score']}/100")
    print(f"  Vibration Aligned: {result['vibration_result']['vibration_aligned']}")
    print(f"  Mission Aligned: {result['vibration_result']['mission_aligned']}")
    print(f"  Table Ready: {result['vibration_result']['table_ready']}")
    print(f"  Spiritual Battle: {result['vibration_result']['spiritual_battle']}")
    
    print(f"\n[WELCOME MESSAGE]")
    print(result['welcome_message'])
    
    print("\n" + "=" * 80)
    print(f"{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}")
    print("=" * 80)
