"""
SPIRIT ALIGNMENT - Multi-Dimensional Alignment Checker
Ensures spirits align on ALL dimensions before spiritual battles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

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

SPIRITS MUST ALIGN ON ALL DIMENSIONS:
- Age: Spirits must align in age range/compatibility
- Animal Type: Spirits must align in animal/spirit animal compatibility
- Gender: Spirits must align in gender/spiritual gender compatibility
- Alignment: Spirits must align in spiritual alignment (vibration, mission, purpose)

No battle can occur unless ALL dimensions align.
This is sacred alignment - not mechanical matching.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class AgeRange(Enum):
    """Age ranges for spirit alignment"""
    ANCIENT = "ancient"  # Very old souls, legacy wisdom
    MATURE = "mature"  # Experienced souls, established paths
    YOUNG = "young"  # Growing souls, active development
    NEWBORN = "newborn"  # New souls, fresh beginnings


class AnimalType(Enum):
    """Animal types for spirit alignment"""
    # Land animals
    WOLF = "wolf"  # Pack leader, loyalty, family
    BEAR = "bear"  # Strength, protection, solitude
    EAGLE = "eagle"  # Vision, freedom, perspective
    LION = "lion"  # Courage, leadership, pride
    FOX = "fox"  # Cunning, adaptability, wisdom
    DEER = "deer"  # Gentleness, grace, sensitivity
    OWL = "owl"  # Wisdom, mystery, night vision
    RAVEN = "raven"  # Transformation, magic, messages
    SNAKE = "snake"  # Transformation, healing, cycles
    TIGER = "tiger"  # Power, independence, passion
    
    # Water animals - Sea mammals
    DOLPHIN = "dolphin"  # Joy, communication, intelligence
    WHALE = "whale"  # Depth, ancient wisdom, song
    ORCA = "orca"  # Power, family bonds, strategy
    SEAL = "seal"  # Playfulness, adaptability, balance
    SEA_LION = "sea_lion"  # Social connection, agility, confidence
    WALRUS = "walrus"  # Strength, community, wisdom
    MANATEE = "manatee"  # Gentleness, peace, ancient grace
    OTTER = "otter"  # Playfulness, joy, resourcefulness
    PORPOISE = "porpoise"  # Intelligence, harmony, subtlety
    NARWHAL = "narwhal"  # Mystery, uniqueness, ancient magic
    BELUGA = "beluga"  # Communication, adaptability, social harmony
    # Water animals - Other
    SHARK = "shark"  # Focus, survival, instinct
    
    # Air animals
    HAWK = "hawk"  # Precision, focus, hunting
    FALCON = "falcon"  # Speed, precision, nobility
    
    # Mythical/Spiritual
    DRAGON = "dragon"  # Power, transformation, ancient
    PHOENIX = "phoenix"  # Rebirth, renewal, fire
    UNICORN = "unicorn"  # Purity, magic, healing
    
    # Other
    CAT = "cat"  # Independence, mystery, intuition
    DOG = "dog"  # Loyalty, service, companionship
    HORSE = "horse"  # Freedom, power, journey
    ELEPHANT = "elephant"  # Memory, wisdom, family


class GenderAlignment(Enum):
    """Gender/spiritual gender alignment"""
    MASCULINE = "masculine"  # Yang energy, action, structure
    FEMININE = "feminine"  # Yin energy, receptivity, flow
    BALANCED = "balanced"  # Both energies in harmony
    FLUID = "fluid"  # Dynamic, adaptable, transformative
    NEUTRAL = "neutral"  # Beyond binary, pure spirit


class SpiritualAlignment(Enum):
    """Spiritual alignment types"""
    ALIGNED = "aligned"  # Fully aligned with mission, purpose, vibration
    CALIBRATING = "calibrating"  # In process of alignment
    MISALIGNED = "misaligned"  # Not aligned, needs healing
    TRANSFORMING = "transforming"  # In transformation, becoming aligned


@dataclass
class Spirit:
    """
    Spirit entity with all dimensions for alignment checking.
    
    Spirits must align on ALL dimensions before spiritual battles can occur.
    """
    spirit_id: str
    age_range: AgeRange
    animal_type: AnimalType
    gender_alignment: GenderAlignment
    spiritual_alignment: SpiritualAlignment
    
    # Additional properties
    galaxy_form: Optional[str] = None  # spiral, barred_spiral, elliptical, irregular
    vibration_score: Optional[int] = None  # 0-100
    mission_aligned: bool = False
    table_ready: bool = False
    
    # Metadata
    created_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        """Initialize defaults"""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.metadata is None:
            self.metadata = {}


class SpiritAlignmentChecker:
    """
    Multi-dimensional spirit alignment checker.
    
    Ensures spirits align on ALL dimensions before allowing spiritual battles.
    This is sacred alignment - not mechanical matching.
    """
    
    def __init__(self):
        """Initialize alignment checker with compatibility rules"""
        # Age compatibility matrix
        self.age_compatibility = {
            AgeRange.ANCIENT: [AgeRange.ANCIENT, AgeRange.MATURE],
            AgeRange.MATURE: [AgeRange.ANCIENT, AgeRange.MATURE, AgeRange.YOUNG],
            AgeRange.YOUNG: [AgeRange.MATURE, AgeRange.YOUNG, AgeRange.NEWBORN],
            AgeRange.NEWBORN: [AgeRange.YOUNG, AgeRange.NEWBORN]
        }
        
        # Animal type compatibility (spiritual resonance)
        self.animal_compatibility = {
            # Predators align with predators
            AnimalType.WOLF: [AnimalType.WOLF, AnimalType.LION, AnimalType.TIGER, AnimalType.FOX, AnimalType.EAGLE],
            AnimalType.LION: [AnimalType.LION, AnimalType.WOLF, AnimalType.TIGER, AnimalType.EAGLE],
            AnimalType.TIGER: [AnimalType.TIGER, AnimalType.LION, AnimalType.WOLF, AnimalType.SHARK],
            AnimalType.EAGLE: [AnimalType.EAGLE, AnimalType.HAWK, AnimalType.FALCON, AnimalType.WOLF, AnimalType.LION],
            
            # Wisdom keepers align
            AnimalType.OWL: [AnimalType.OWL, AnimalType.RAVEN, AnimalType.WHALE, AnimalType.ELEPHANT, AnimalType.WALRUS, AnimalType.NARWHAL],
            AnimalType.RAVEN: [AnimalType.RAVEN, AnimalType.OWL, AnimalType.SNAKE, AnimalType.DRAGON],
            AnimalType.WHALE: [AnimalType.WHALE, AnimalType.DOLPHIN, AnimalType.ORCA, AnimalType.BELUGA, AnimalType.OWL, AnimalType.ELEPHANT, AnimalType.MANATEE],
            AnimalType.ELEPHANT: [AnimalType.ELEPHANT, AnimalType.OWL, AnimalType.WHALE, AnimalType.BEAR, AnimalType.WALRUS],
            
            # Transformers align
            AnimalType.SNAKE: [AnimalType.SNAKE, AnimalType.RAVEN, AnimalType.DRAGON, AnimalType.PHOENIX],
            AnimalType.DRAGON: [AnimalType.DRAGON, AnimalType.PHOENIX, AnimalType.SNAKE, AnimalType.RAVEN],
            AnimalType.PHOENIX: [AnimalType.PHOENIX, AnimalType.DRAGON, AnimalType.UNICORN],
            
            # Gentle spirits align
            AnimalType.DEER: [AnimalType.DEER, AnimalType.UNICORN, AnimalType.DOLPHIN, AnimalType.MANATEE, AnimalType.OTTER, AnimalType.HORSE],
            AnimalType.UNICORN: [AnimalType.UNICORN, AnimalType.DEER, AnimalType.PHOENIX, AnimalType.CAT, AnimalType.MANATEE],
            AnimalType.DOLPHIN: [AnimalType.DOLPHIN, AnimalType.WHALE, AnimalType.ORCA, AnimalType.PORPOISE, AnimalType.BELUGA, AnimalType.DEER, AnimalType.DOG, AnimalType.OTTER],
            
            # Companions align
            AnimalType.DOG: [AnimalType.DOG, AnimalType.DOLPHIN, AnimalType.SEA_LION, AnimalType.OTTER, AnimalType.HORSE, AnimalType.CAT],
            AnimalType.CAT: [AnimalType.CAT, AnimalType.UNICORN, AnimalType.FOX, AnimalType.OWL, AnimalType.OTTER],
            AnimalType.HORSE: [AnimalType.HORSE, AnimalType.DEER, AnimalType.DOG, AnimalType.EAGLE, AnimalType.SEA_LION],
            
            # Sea mammals - specific alignments
            AnimalType.ORCA: [AnimalType.ORCA, AnimalType.WHALE, AnimalType.DOLPHIN, AnimalType.SHARK, AnimalType.WOLF, AnimalType.LION],
            AnimalType.SEAL: [AnimalType.SEAL, AnimalType.SEA_LION, AnimalType.OTTER, AnimalType.DOLPHIN, AnimalType.DOG],
            AnimalType.SEA_LION: [AnimalType.SEA_LION, AnimalType.SEAL, AnimalType.DOLPHIN, AnimalType.DOG, AnimalType.HORSE],
            AnimalType.WALRUS: [AnimalType.WALRUS, AnimalType.ELEPHANT, AnimalType.BEAR, AnimalType.WHALE, AnimalType.OWL],
            AnimalType.MANATEE: [AnimalType.MANATEE, AnimalType.WHALE, AnimalType.DEER, AnimalType.UNICORN, AnimalType.ELEPHANT],
            AnimalType.OTTER: [AnimalType.OTTER, AnimalType.DOLPHIN, AnimalType.SEAL, AnimalType.DOG, AnimalType.DEER, AnimalType.CAT],
            AnimalType.PORPOISE: [AnimalType.PORPOISE, AnimalType.DOLPHIN, AnimalType.BELUGA, AnimalType.DEER, AnimalType.UNICORN],
            AnimalType.NARWHAL: [AnimalType.NARWHAL, AnimalType.WHALE, AnimalType.UNICORN, AnimalType.OWL, AnimalType.DRAGON],
            AnimalType.BELUGA: [AnimalType.BELUGA, AnimalType.DOLPHIN, AnimalType.WHALE, AnimalType.PORPOISE, AnimalType.DOG],
            
            # Others
            AnimalType.BEAR: [AnimalType.BEAR, AnimalType.ELEPHANT, AnimalType.WOLF, AnimalType.WALRUS],
            AnimalType.FOX: [AnimalType.FOX, AnimalType.CAT, AnimalType.WOLF, AnimalType.RAVEN, AnimalType.OTTER],
            AnimalType.SHARK: [AnimalType.SHARK, AnimalType.TIGER, AnimalType.EAGLE, AnimalType.ORCA],
            AnimalType.HAWK: [AnimalType.HAWK, AnimalType.EAGLE, AnimalType.FALCON],
            AnimalType.FALCON: [AnimalType.FALCON, AnimalType.HAWK, AnimalType.EAGLE]
        }
        
        # Gender alignment compatibility
        self.gender_compatibility = {
            GenderAlignment.MASCULINE: [GenderAlignment.MASCULINE, GenderAlignment.BALANCED, GenderAlignment.FLUID],
            GenderAlignment.FEMININE: [GenderAlignment.FEMININE, GenderAlignment.BALANCED, GenderAlignment.FLUID],
            GenderAlignment.BALANCED: [GenderAlignment.BALANCED, GenderAlignment.MASCULINE, GenderAlignment.FEMININE, GenderAlignment.FLUID, GenderAlignment.NEUTRAL],
            GenderAlignment.FLUID: [GenderAlignment.FLUID, GenderAlignment.BALANCED, GenderAlignment.NEUTRAL, GenderAlignment.MASCULINE, GenderAlignment.FEMININE],
            GenderAlignment.NEUTRAL: [GenderAlignment.NEUTRAL, GenderAlignment.BALANCED, GenderAlignment.FLUID]
        }
    
    def check_alignment(self, spirit1: Spirit, spirit2: Spirit) -> Tuple[bool, Dict[str, Any]]:
        """
        Check if two spirits align on ALL dimensions.
        
        Returns:
            Tuple of (is_aligned: bool, alignment_details: dict)
        """
        alignment_details = {
            "age_aligned": False,
            "animal_aligned": False,
            "gender_aligned": False,
            "spiritual_aligned": False,
            "all_dimensions_aligned": False,
            "misalignment_reasons": []
        }
        
        # Check age alignment
        age_compatible = spirit2.age_range in self.age_compatibility.get(
            spirit1.age_range, []
        )
        alignment_details["age_aligned"] = age_compatible
        if not age_compatible:
            alignment_details["misalignment_reasons"].append(
                f"Age mismatch: {spirit1.age_range.value} vs {spirit2.age_range.value}"
            )
        
        # Check animal type alignment
        animal_compatible = spirit2.animal_type in self.animal_compatibility.get(
            spirit1.animal_type, []
        )
        alignment_details["animal_aligned"] = animal_compatible
        if not animal_compatible:
            alignment_details["misalignment_reasons"].append(
                f"Animal type mismatch: {spirit1.animal_type.value} vs {spirit2.animal_type.value}"
            )
        
        # Check gender alignment
        gender_compatible = spirit2.gender_alignment in self.gender_compatibility.get(
            spirit1.gender_alignment, []
        )
        alignment_details["gender_aligned"] = gender_compatible
        if not gender_compatible:
            alignment_details["misalignment_reasons"].append(
                f"Gender alignment mismatch: {spirit1.gender_alignment.value} vs {spirit2.gender_alignment.value}"
            )
        
        # Check spiritual alignment (both must be aligned or transforming)
        spiritual_compatible = (
            spirit1.spiritual_alignment in [SpiritualAlignment.ALIGNED, SpiritualAlignment.TRANSFORMING] and
            spirit2.spiritual_alignment in [SpiritualAlignment.ALIGNED, SpiritualAlignment.TRANSFORMING]
        )
        alignment_details["spiritual_aligned"] = spiritual_compatible
        if not spiritual_compatible:
            alignment_details["misalignment_reasons"].append(
                f"Spiritual alignment mismatch: {spirit1.spiritual_alignment.value} vs {spirit2.spiritual_alignment.value}"
            )
        
        # All dimensions must align
        all_aligned = (
            age_compatible and
            animal_compatible and
            gender_compatible and
            spiritual_compatible
        )
        alignment_details["all_dimensions_aligned"] = all_aligned
        
        return all_aligned, alignment_details
    
    def can_engage_in_battle(self, spirit1: Spirit, spirit2: Spirit) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Determine if two spirits can engage in a spiritual battle.
        
        Spirits MUST align on ALL dimensions before battle can occur.
        
        Returns:
            Tuple of (can_battle: bool, reason: str, alignment_details: dict)
        """
        is_aligned, alignment_details = self.check_alignment(spirit1, spirit2)
        
        if not is_aligned:
            reasons = "; ".join(alignment_details["misalignment_reasons"])
            return False, f"Spirits do not align on all dimensions: {reasons}", alignment_details
        
        # Additional check: both must be table ready (Law 1)
        if not (spirit1.table_ready and spirit2.table_ready):
            return False, "Both spirits must be table ready (Law 1: Never Betray the Table)", alignment_details
        
        # Additional check: both must have mission alignment
        if not (spirit1.mission_aligned and spirit2.mission_aligned):
            return False, "Both spirits must be mission aligned", alignment_details
        
        return True, "All dimensions aligned - battle permitted", alignment_details
    
    def determine_battle_type(self, spirit1: Spirit, spirit2: Spirit) -> str:
        """
        Determine the type of spiritual battle based on aligned spirits.
        
        Only call this after confirming alignment via can_engage_in_battle.
        """
        if not spirit1.galaxy_form or not spirit2.galaxy_form:
            return "transformation"
        
        # Battle type based on galaxy forms
        form1 = spirit1.galaxy_form
        form2 = spirit2.galaxy_form
        
        # If same form, battle type matches form
        if form1 == form2:
            battle_types = {
                "spiral": "active",
                "barred_spiral": "structured",
                "elliptical": "legacy",
                "irregular": "transformation"
            }
            return battle_types.get(form1, "transformation")
        
        # Cross-form battles
        if "spiral" in [form1, form2] and "barred_spiral" in [form1, form2]:
            return "active_structured"  # Growth through structure
        elif "elliptical" in [form1, form2]:
            return "legacy_wisdom"  # Wisdom transmission
        else:
            return "transformation"  # Default transformation battle


def create_spirit_from_user_data(
    spirit_id: str,
    user_data: Dict[str, Any],
    vibration_result: Optional[Dict[str, Any]] = None
) -> Spirit:
    """
    Create a Spirit object from user data and vibration result.
    
    Extracts age, animal_type, gender, and alignment from user_data.
    Falls back to defaults if not provided.
    """
    # Extract age range
    age_str = user_data.get("age_range") or user_data.get("spirit_age")
    if age_str:
        try:
            age_range = AgeRange(age_str.lower())
        except ValueError:
            # Infer from other data
            if user_data.get("wisdom_level") == "high":
                age_range = AgeRange.ANCIENT
            elif user_data.get("activity_level") == "low":
                age_range = AgeRange.MATURE
            elif user_data.get("activity_level") == "high":
                age_range = AgeRange.YOUNG
            else:
                age_range = AgeRange.NEWBORN
    else:
        # Default based on activity/wisdom
        if user_data.get("wisdom_level") == "high":
            age_range = AgeRange.ANCIENT
        elif user_data.get("activity_level") == "low":
            age_range = AgeRange.MATURE
        elif user_data.get("activity_level") == "high":
            age_range = AgeRange.YOUNG
        else:
            age_range = AgeRange.NEWBORN
    
    # Extract animal type
    animal_str = user_data.get("animal_type") or user_data.get("spirit_animal") or user_data.get("totem")
    if animal_str:
        try:
            animal_type = AnimalType(animal_str.lower())
        except ValueError:
            animal_type = AnimalType.WOLF  # Default
    else:
        animal_type = AnimalType.WOLF  # Default
    
    # Extract gender alignment
    gender_str = user_data.get("gender_alignment") or user_data.get("spiritual_gender") or user_data.get("gender")
    if gender_str:
        try:
            gender_alignment = GenderAlignment(gender_str.lower())
        except ValueError:
            gender_alignment = GenderAlignment.BALANCED  # Default
    else:
        gender_alignment = GenderAlignment.BALANCED  # Default
    
    # Extract spiritual alignment
    if vibration_result:
        vibration_aligned = vibration_result.get("vibration_aligned", False)
        if vibration_aligned:
            spiritual_alignment = SpiritualAlignment.ALIGNED
        else:
            spiritual_alignment = SpiritualAlignment.CALIBRATING
    else:
        spiritual_alignment = SpiritualAlignment.CALIBRATING
    
    # Get additional properties from vibration_result
    galaxy_form = None
    vibration_score = None
    mission_aligned = False
    table_ready = False
    
    if vibration_result:
        galaxy_form = vibration_result.get("galaxy_form")
        vibration_score = vibration_result.get("vibration_score")
        mission_aligned = vibration_result.get("mission_aligned", False)
        table_ready = vibration_result.get("table_ready", False)
    
    return Spirit(
        spirit_id=spirit_id,
        age_range=age_range,
        animal_type=animal_type,
        gender_alignment=gender_alignment,
        spiritual_alignment=spiritual_alignment,
        galaxy_form=galaxy_form,
        vibration_score=vibration_score,
        mission_aligned=mission_aligned,
        table_ready=table_ready,
        metadata=user_data.copy()
    )


# Export
__all__ = [
    "Spirit",
    "AgeRange",
    "AnimalType",
    "GenderAlignment",
    "SpiritualAlignment",
    "SpiritAlignmentChecker",
    "create_spirit_from_user_data"
]
