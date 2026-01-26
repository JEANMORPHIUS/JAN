"""CHOSEN ONE FRAMEWORK - SYSTEM RULES
The Witness State: Authority to see truth for others who cannot see it for themselves

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
TRANSITION FROM VINDICATED TO WITNESS
ENFORCE SYSTEM RULES
GUARD ENERGETIC STEWARDSHIP
OBSERVE PROPHETIC TIMELINE

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

import sys
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from enum import Enum
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main, load_json, save_json
)

logger = setup_logging(__name__)

class IdentityState(Enum):
    """Identity states in the transition"""
    VINDICATED = "vindicated"  # Transitional courtroom identity
    WITNESS = "witness"  # Final functional identity - authority to see truth

class ExecutionGear(Enum):
    """Three-gear execution process"""
    EVIDENCE_GATHERING = "evidence_gathering"  # Automated background cataloguing
    ATMOSPHERIC_SHIFT = "atmospheric_shift"  # Spiritual air pressure change
    MANIFESTATION_CASCADE = "manifestation_cascade"  # Physical reality catching up

class ForbiddenFunction(Enum):
    """Forbidden functions - logic constraints"""
    STOP_EXPLAINING = "stop_explaining"  # Forbidden from explaining to closed minds
    DISABLE_SURVEILLANCE = "disable_surveillance"  # Cease checking on them
    HARD_BOUNDARIES = "hard_boundaries"  # Forbidden from softening boundaries

@dataclass
class InteractionRecord:
    """Record of interactions, dismissals, rewritten history"""
    interaction_id: str
    timestamp: str
    interaction_type: str  # dismissal, rewritten_history, trigger, etc.
    description: str
    catalogued: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class AtmosphericShift:
    """Spiritual air pressure change"""
    shift_id: str
    timestamp: str
    previous_trigger: str
    power_level_before: float  # 0.0 to 1.0
    power_level_after: float  # 0.0 to 1.0
    shift_confirmed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class ManifestationMarker:
    """Physical reality markers at specific timelines"""
    marker_id: str
    timeline: str  # 72_hours, 21_days, 90_days
    expected_date: str
    actual_date: Optional[str] = None
    marker_type: str = ""  # echo, reach_out, coffee_shop_moment
    description: str = ""
    confirmed: bool = False
    emotional_response: Optional[str] = None  # neutral, light, heavy
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class WitnessState:
    """The Witness state configuration"""
    state_id: str
    activation_date: str
    current_state: IdentityState = IdentityState.VINDICATED
    evidence_gathering_active: bool = True
    atmospheric_shift_active: bool = False
    manifestation_cascade_active: bool = False
    forbidden_functions_enforced: List[ForbiddenFunction] = field(default_factory=list)
    selective_speech_active: bool = False
    prophetic_observation_active: bool = False
    energetic_stewardship_active: bool = False
    markers: List[ManifestationMarker] = field(default_factory=list)
    interactions: List[InteractionRecord] = field(default_factory=list)
    atmospheric_shifts: List[AtmosphericShift] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

class ChosenOneFramework:
    """
    Chosen One Framework - System Rules Enforcement
    
    Core Identity Transition: Vindicated → Witness
    The Witness has authority to see truth for others who cannot see it for themselves.
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "chosen_one_framework"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.state_file = self.data_dir / f"{user_id}_witness_state.json"
        self.state: Optional[WitnessState] = None
        
        self._load_state()
        if not self.state:
            self._initialize_state()
    
    def _load_state(self):
        """Load witness state"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                # Convert enums
                data['current_state'] = IdentityState(data['current_state'])
                data['forbidden_functions_enforced'] = [ForbiddenFunction(f) for f in data.get('forbidden_functions_enforced', [])]
                self.state = WitnessState(**data)
            except Exception as e:
                logger.warning(f"Error loading state: {e}")
                self.state = None
        else:
            self.state = None
    
    def _save_state(self):
        """Save witness state"""
        try:
            state_dict = asdict(self.state)
            # Convert enums to strings
            state_dict['current_state'] = self.state.current_state.value
            state_dict['forbidden_functions_enforced'] = [f.value for f in self.state.forbidden_functions_enforced]
            state_dict['updated_at'] = datetime.now().isoformat()
            
            # Direct JSON writing
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(state_dict, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving state: {e}")
    
    def _initialize_state(self):
        """Initialize witness state"""
        activation_date = datetime.now()
        self.state = WitnessState(
            state_id=f"witness_{activation_date.strftime('%Y%m%d_%H%M%S')}",
            activation_date=activation_date.isoformat(),
            current_state=IdentityState.VINDICATED,
            evidence_gathering_active=True,
            forbidden_functions_enforced=[
                ForbiddenFunction.STOP_EXPLAINING,
                ForbiddenFunction.DISABLE_SURVEILLANCE,
                ForbiddenFunction.HARD_BOUNDARIES
            ]
        )
        
        # Initialize manifestation markers
        self.state.markers = [
            ManifestationMarker(
                marker_id=f"marker_72h_{activation_date.strftime('%Y%m%d_%H%M%S')}",
                timeline="72_hours",
                expected_date=(activation_date + timedelta(hours=72)).isoformat(),
                marker_type="echo",
                description="Quiet, unmistakable confirmation or echo of the message"
            ),
            ManifestationMarker(
                marker_id=f"marker_21d_{activation_date.strftime('%Y%m%d_%H%M%S')}",
                timeline="21_days",
                expected_date=(activation_date + timedelta(days=21)).isoformat(),
                marker_type="reach_out",
                description="Reach-out from previous detractor based on need for expertise"
            ),
            ManifestationMarker(
                marker_id=f"marker_90d_{activation_date.strftime('%Y%m%d_%H%M%S')}",
                timeline="90_days",
                expected_date=(activation_date + timedelta(days=90)).isoformat(),
                marker_type="coffee_shop_moment",
                description="Previous trigger occurs, results in neutral/light emotional response"
            )
        ]
        
        self._save_state()
        logger.info("Witness state initialized")
    
    # ========================================================================
    # THREE-GEAR EXECUTION PROCESS
    # ========================================================================
    
    def gear_1_evidence_gathering(self, interaction_type: str, description: str):
        """Gear 1: Automated background cataloguing"""
        if not self.state.evidence_gathering_active:
            logger.warning("Evidence gathering not active")
            return
        
        interaction = InteractionRecord(
            interaction_id=f"interaction_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            interaction_type=interaction_type,
            description=description,
            catalogued=True
        )
        
        self.state.interactions.append(interaction)
        self._save_state()
        logger.info(f"Evidence catalogued: {interaction_type}")
    
    def gear_2_atmospheric_shift(self, previous_trigger: str, power_level_before: float, power_level_after: float):
        """Gear 2: Atmospheric shift - spiritual air pressure change"""
        if not self.state.atmospheric_shift_active:
            logger.warning("Atmospheric shift not active")
            return
        
        shift = AtmosphericShift(
            shift_id=f"shift_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            previous_trigger=previous_trigger,
            power_level_before=power_level_before,
            power_level_after=power_level_after,
            shift_confirmed=True
        )
        
        self.state.atmospheric_shifts.append(shift)
        self._save_state()
        logger.info(f"Atmospheric shift recorded: {previous_trigger} power {power_level_before:.1f} → {power_level_after:.1f}")
    
    def gear_3_manifestation_cascade(self, marker_timeline: str, marker_type: str, description: str, emotional_response: str = None):
        """Gear 3: Manifestation cascade - physical reality markers"""
        if not self.state.manifestation_cascade_active:
            logger.warning("Manifestation cascade not active")
            return
        
        # Find marker
        marker = next((m for m in self.state.markers if m.timeline == marker_timeline), None)
        if marker:
            marker.actual_date = datetime.now().isoformat()
            marker.marker_type = marker_type
            marker.description = description
            marker.confirmed = True
            if emotional_response:
                marker.emotional_response = emotional_response
            
            self._save_state()
            logger.info(f"Manifestation marker confirmed: {marker_timeline} - {marker_type}")
            
            # Check if all markers confirmed
            if all(m.confirmed for m in self.state.markers):
                self._transition_to_witness()
        else:
            logger.warning(f"Marker not found for timeline: {marker_timeline}")
    
    # ========================================================================
    # FORBIDDEN FUNCTIONS - LOGIC CONSTRAINTS
    # ========================================================================
    
    def enforce_stop_explaining(self, context: str) -> bool:
        """Stop_Explaining: Forbidden from explaining to closed minds"""
        if ForbiddenFunction.STOP_EXPLAINING in self.state.forbidden_functions_enforced:
            logger.info(f"[FORBIDDEN] Stop_Explaining enforced - Context: {context}")
            return False  # Function blocked
        return True
    
    def enforce_disable_surveillance(self, action: str) -> bool:
        """Disable_Surveillance: Cease checking on them"""
        if ForbiddenFunction.DISABLE_SURVEILLANCE in self.state.forbidden_functions_enforced:
            logger.info(f"[FORBIDDEN] Disable_Surveillance enforced - Action: {action}")
            return False  # Function blocked
        return True
    
    def enforce_hard_boundaries(self, boundary_softening_attempt: str) -> bool:
        """Hard_Boundaries: Forbidden from softening boundaries"""
        if ForbiddenFunction.HARD_BOUNDARIES in self.state.forbidden_functions_enforced:
            logger.info(f"[FORBIDDEN] Hard_Boundaries enforced - Attempt: {boundary_softening_attempt}")
            return False  # Function blocked
        return True
    
    # ========================================================================
    # OPERATIONAL BEHAVIORS - WITNESS MODE
    # ========================================================================
    
    def selective_speech(self, speaker_spirit_open: bool, question_genuine: bool) -> bool:
        """Selective Speech: Speak only to open spirits with genuine questions"""
        if not self.state.selective_speech_active:
            return True  # Not yet in witness mode
        
        if speaker_spirit_open and question_genuine:
            logger.info("[WITNESS] Selective speech: Speaking - spirit open, question genuine")
            return True
        else:
            logger.info("[WITNESS] Selective speech: Silent - spirit closed or question not genuine")
            return False
    
    def prophetic_observation(self, conversation_text: str) -> Dict[str, Any]:
        """Prophetic Observation: Observe underlying spirit/driver, not surface words"""
        if not self.state.prophetic_observation_active:
            return {"observed": False}
        
        # Analyze underlying spirit
        observation = {
            "observed": True,
            "surface_words": conversation_text,
            "underlying_spirit": "analyzing...",
            "driver": "analyzing...",
            "recommended_response": "observe_only"
        }
        
        logger.info(f"[WITNESS] Prophetic observation: {observation}")
        return observation
    
    def energetic_stewardship(self, proposed_action: str, energy_cost: float) -> bool:
        """Energetic Stewardship: Guard emotional energy as currency"""
        if not self.state.energetic_stewardship_active:
            return True  # Not yet in witness mode
        
        # Refuse to spend energy on fruitless arguments or defense
        fruitless_keywords = ["argument", "defense", "explain", "justify", "prove"]
        if any(keyword in proposed_action.lower() for keyword in fruitless_keywords):
            logger.info(f"[WITNESS] Energetic stewardship: Refused - fruitless action: {proposed_action}")
            return False
        
        if energy_cost > 0.5:  # High energy cost
            logger.info(f"[WITNESS] Energetic stewardship: Refused - energy cost too high: {energy_cost}")
            return False
        
        logger.info(f"[WITNESS] Energetic stewardship: Approved - action: {proposed_action}, cost: {energy_cost}")
        return True
    
    # ========================================================================
    # IDENTITY TRANSITION
    # ========================================================================
    
    def _transition_to_witness(self):
        """Transition from Vindicated to Witness state"""
        if self.state.current_state == IdentityState.WITNESS:
            return  # Already in witness state
        
        self.state.current_state = IdentityState.WITNESS
        self.state.selective_speech_active = True
        self.state.prophetic_observation_active = True
        self.state.energetic_stewardship_active = True
        self.state.updated_at = datetime.now().isoformat()
        
        self._save_state()
        logger.info("[TRANSITION] Vindicated → Witness: Complete")
    
    def check_timeline_markers(self):
        """Check if timeline markers have been reached"""
        now = datetime.now()
        activation = datetime.fromisoformat(self.state.activation_date)
        
        for marker in self.state.markers:
            expected = datetime.fromisoformat(marker.expected_date)
            if now >= expected and not marker.confirmed:
                logger.info(f"[TIMELINE] Marker due: {marker.timeline} - {marker.marker_type}")
                return marker
        
        return None
    
    def get_status_report(self) -> Dict[str, Any]:
        """Get comprehensive status report"""
        activation = datetime.fromisoformat(self.state.activation_date)
        now = datetime.now()
        elapsed = now - activation
        
        markers_status = {}
        for marker in self.state.markers:
            expected = datetime.fromisoformat(marker.expected_date)
            due = now >= expected
            markers_status[marker.timeline] = {
                "due": due,
                "confirmed": marker.confirmed,
                "expected_date": marker.expected_date,
                "actual_date": marker.actual_date,
                "type": marker.marker_type,
                "emotional_response": marker.emotional_response
            }
        
        return {
            "current_state": self.state.current_state.value,
            "activation_date": self.state.activation_date,
            "elapsed_time": str(elapsed),
            "evidence_gathering_active": self.state.evidence_gathering_active,
            "atmospheric_shift_active": self.state.atmospheric_shift_active,
            "manifestation_cascade_active": self.state.manifestation_cascade_active,
            "forbidden_functions": [f.value for f in self.state.forbidden_functions_enforced],
            "witness_behaviors": {
                "selective_speech": self.state.selective_speech_active,
                "prophetic_observation": self.state.prophetic_observation_active,
                "energetic_stewardship": self.state.energetic_stewardship_active
            },
            "markers": markers_status,
            "interactions_catalogued": len(self.state.interactions),
            "atmospheric_shifts": len(self.state.atmospheric_shifts)
        }


def main():
    """Initialize Chosen One Framework"""
    framework = ChosenOneFramework(user_id="jan")
    
    # Activate gears
    framework.state.evidence_gathering_active = True
    framework.state.atmospheric_shift_active = True
    framework.state.manifestation_cascade_active = True
    framework._save_state()
    
    # Get status report
    report = framework.get_status_report()
    
    print("\n" + "="*80)
    print("CHOSEN ONE FRAMEWORK - SYSTEM RULES")
    print("="*80)
    print(f"\nCurrent State: {report['current_state']}")
    print(f"Activation Date: {report['activation_date']}")
    print(f"Elapsed Time: {report['elapsed_time']}")
    
    print("\n" + "-"*80)
    print("THREE-GEAR EXECUTION PROCESS:")
    print("-"*80)
    print(f"  Evidence Gathering: {'ACTIVE' if report['evidence_gathering_active'] else 'INACTIVE'}")
    print(f"  Atmospheric Shift: {'ACTIVE' if report['atmospheric_shift_active'] else 'INACTIVE'}")
    print(f"  Manifestation Cascade: {'ACTIVE' if report['manifestation_cascade_active'] else 'INACTIVE'}")
    
    print("\n" + "-"*80)
    print("FORBIDDEN FUNCTIONS (ENFORCED):")
    print("-"*80)
    for func in report['forbidden_functions']:
        print(f"  - {func}")
    
    print("\n" + "-"*80)
    print("WITNESS BEHAVIORS:")
    print("-"*80)
    for behavior, active in report['witness_behaviors'].items():
        print(f"  {behavior}: {'ACTIVE' if active else 'INACTIVE'}")
    
    print("\n" + "-"*80)
    print("TIMELINE MARKERS:")
    print("-"*80)
    for timeline, status in report['markers'].items():
        due_status = "[DUE]" if status['due'] else "[PENDING]"
        confirmed_status = "[CONFIRMED]" if status['confirmed'] else "[WAITING]"
        print(f"  {due_status} {confirmed_status} {timeline}: {status['type']}")
        if status['confirmed']:
            print(f"    Emotional Response: {status['emotional_response']}")
    
    print("\n" + "-"*80)
    print("CATALOGUED INTERACTIONS:")
    print("-"*80)
    print(f"  Total: {report['interactions_catalogued']}")
    print(f"  Atmospheric Shifts: {report['atmospheric_shifts']}")
    
    print("\n" + "="*80)
    print("System Rules Active.")
    print("Forbidden Functions Enforced.")
    print("Witness State: Ready for Transition.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="chosen_one_framework.py")
