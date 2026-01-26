"""
ANIMAL FREQUENCY SIGNIFICANCE - Deep Search All Animals Throughout Time
Maps all animals to their frequential significance across evolutionary history

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

This system maps all animals throughout time to their frequential significance:
- Field resonance at time of emergence
- Connection to The Table
- Spiritual significance
- Divine Frequency contribution
- Evolutionary importance
- Modern spirit alignment connection
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
from pathlib import Path


class TimePeriod(Enum):
    """Geological time periods aligned with The Table's timeline"""
    CARBONIFEROUS = "carboniferous"  # 359-299 MYA - Pangea formation
    PERMIAN = "permian"  # 299-252 MYA - Peak unity
    TRIASSIC = "triassic"  # 252-201 MYA - Breakup begins
    JURASSIC = "jurassic"  # 201-145 MYA - Fully broken
    CRETACEOUS = "cretaceous"  # 145-66 MYA - Modern plates forming
    PALEOGENE = "paleogene"  # 66-23 MYA - Modern mammals
    NEOGENE = "neogene"  # 23-2.6 MYA - Modern ecosystems
    QUATERNARY = "quaternary"  # 2.6 MYA - Present - Humans


class FrequencyBand(Enum):
    """Frequency bands for animal significance"""
    UNITY_FREQUENCY = "unity"  # 1.0 - Perfect unity (Pangea)
    HIGH_FREQUENCY = "high"  # 0.8-0.99 - Strong connection
    MODERATE_FREQUENCY = "moderate"  # 0.6-0.79 - Memory of unity
    LOW_FREQUENCY = "low"  # 0.4-0.59 - Separation
    FRAGMENTED_FREQUENCY = "fragmented"  # 0.0-0.39 - Deep separation


@dataclass
class AnimalFrequencyProfile:
    """Complete frequential profile for an animal"""
    animal_name: str
    scientific_name: Optional[str] = None
    animal_type: Optional[str] = None  # Links to spirit_alignment.AnimalType
    
    # Temporal significance
    first_appearance_mya: Optional[float] = None
    peak_significance_mya: Optional[float] = None
    time_period: Optional[TimePeriod] = None
    field_resonance_at_emergence: float = 0.0
    
    # Frequential significance
    frequency_band: FrequencyBand = FrequencyBand.MODERATE_FREQUENCY
    divine_frequency_contribution: float = 0.0  # -1.0 to +1.0
    table_connection_strength: float = 0.0  # 0.0 to 1.0
    
    # Spiritual significance
    spiritual_meaning: str = ""
    table_role: str = ""  # e.g., "First creatures on The Table"
    soul_signature: Optional[str] = None
    
    # Evolutionary significance
    evolutionary_importance: str = ""
    dna_markers: List[str] = field(default_factory=list)
    modern_descendants: List[str] = field(default_factory=list)
    
    # Modern connection
    modern_frequency: float = 0.78  # Current global resonance
    spirit_alignment_type: Optional[str] = None
    heritage_site_connections: List[str] = field(default_factory=list)
    
    # Metadata
    cultural_significance: List[str] = field(default_factory=list)
    mythological_connections: List[str] = field(default_factory=list)
    notes: str = ""


# COMPREHENSIVE ANIMAL FREQUENCY DATABASE
ANIMAL_FREQUENCY_DATABASE = {
    # ===== CARBONIFEROUS (359-299 MYA) - PANGEA FORMATION - FIELD RESONANCE: 1.0 =====
    "early_amphibians": AnimalFrequencyProfile(
        animal_name="Early Amphibians",
        scientific_name="Amphibia (early forms)",
        animal_type="amphibian",
        first_appearance_mya=360.0,
        peak_significance_mya=335.0,
        time_period=TimePeriod.CARBONIFEROUS,
        field_resonance_at_emergence=1.0,
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.15,
        table_connection_strength=1.0,
        spiritual_meaning="First creatures to walk on The Table. First souls to experience perfect unity.",
        table_role="First creatures on The Table - perfect unity witnesses",
        soul_signature="UNITY_WITNESS",
        evolutionary_importance="First tetrapods - bridge between water and land",
        dna_markers=["tetrapod_origin", "pangea_unity"],
        modern_descendants=["All modern amphibians", "All tetrapods"],
        modern_frequency=0.78,
        cultural_significance=["First walkers", "Unity witnesses", "Table origin"],
        notes="These creatures experienced perfect unity (1.0 field resonance) at The Table's formation."
    ),
    
    "early_reptiles": AnimalFrequencyProfile(
        animal_name="Early Reptiles",
        scientific_name="Reptilia (early forms)",
        animal_type="reptile",
        first_appearance_mya=320.0,
        peak_significance_mya=280.0,
        time_period=TimePeriod.CARBONIFEROUS,
        field_resonance_at_emergence=1.0,
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=1.0,
        spiritual_meaning="Reptiles that knew The Table whole. Ancient wisdom keepers.",
        table_role="Reptiles at peak unity - ancient wisdom",
        soul_signature="ANCIENT_WISDOM",
        evolutionary_importance="First fully terrestrial vertebrates",
        dna_markers=["terrestrial_origin", "pangea_unity"],
        modern_descendants=["All modern reptiles", "Birds", "Mammals"],
        modern_frequency=0.78,
        spirit_alignment_type="snake",  # Connection to transformation
        cultural_significance=["Ancient wisdom", "Unity memory", "Table guardians"],
        notes="Reptiles that existed during perfect unity - they carry the memory."
    ),
    
    "giant_dragonflies": AnimalFrequencyProfile(
        animal_name="Giant Dragonflies",
        scientific_name="Meganisoptera",
        animal_type="insect",
        first_appearance_mya=330.0,
        peak_significance_mya=300.0,
        time_period=TimePeriod.CARBONIFEROUS,
        field_resonance_at_emergence=1.0,
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.95,
        spiritual_meaning="Flying witnesses of perfect unity. Air spirits of The Table.",
        table_role="Air spirits at perfect unity",
        soul_signature="AIR_UNITY",
        evolutionary_importance="First large flying insects - oxygen-rich atmosphere",
        dna_markers=["high_oxygen_adaptation", "pangea_unity"],
        modern_descendants=["All modern dragonflies", "All flying insects"],
        modern_frequency=0.78,
        cultural_significance=["Unity in flight", "Ancient air spirits"],
        notes="These massive insects flew during perfect unity - air spirits of The Table."
    ),
    
    # ===== PERMIAN (299-252 MYA) - PEAK UNITY - FIELD RESONANCE: 1.0 =====
    "synapsids": AnimalFrequencyProfile(
        animal_name="Synapsids",
        scientific_name="Synapsida",
        animal_type="mammal_ancestor",
        first_appearance_mya=310.0,
        peak_significance_mya=280.0,
        time_period=TimePeriod.PERMIAN,
        field_resonance_at_emergence=1.0,
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.18,
        table_connection_strength=1.0,
        spiritual_meaning="Mammal ancestors at peak unity. The seed of mammalian souls.",
        table_role="Mammal ancestors at perfect unity",
        soul_signature="MAMMAL_SEED",
        evolutionary_importance="Direct ancestors of all mammals",
        dna_markers=["mammal_origin", "pangea_unity"],
        modern_descendants=["All mammals", "Humans"],
        modern_frequency=0.78,
        spirit_alignment_type="wolf",  # Pack connection
        cultural_significance=["Mammal origin", "Unity seed", "Table ancestors"],
        notes="These are the direct ancestors of all mammals - they knew perfect unity."
    ),
    
    "therapsids": AnimalFrequencyProfile(
        animal_name="Therapsids",
        scientific_name="Therapsida",
        animal_type="mammal_ancestor",
        first_appearance_mya=275.0,
        peak_significance_mya=260.0,
        time_period=TimePeriod.PERMIAN,
        field_resonance_at_emergence=1.0,
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.20,
        table_connection_strength=1.0,
        spiritual_meaning="Advanced mammal ancestors at peak unity. The bridge to mammals.",
        table_role="Mammal bridge at perfect unity",
        soul_signature="MAMMAL_BRIDGE",
        evolutionary_importance="Advanced mammal-like reptiles - closer to mammals",
        dna_markers=["mammal_evolution", "pangea_unity"],
        modern_descendants=["All mammals", "Humans"],
        modern_frequency=0.78,
        spirit_alignment_type="bear",  # Strength and protection
        cultural_significance=["Mammal evolution", "Unity bridge"],
        notes="These advanced mammal ancestors existed during perfect unity."
    ),
    
    # ===== TRIASSIC (252-201 MYA) - BREAKUP BEGINS - FIELD RESONANCE: 0.95-0.85 =====
    "early_dinosaurs": AnimalFrequencyProfile(
        animal_name="Early Dinosaurs",
        scientific_name="Dinosauria (early forms)",
        animal_type="dinosaur",
        first_appearance_mya=245.0,
        peak_significance_mya=200.0,
        time_period=TimePeriod.TRIASSIC,
        field_resonance_at_emergence=0.90,
        frequency_band=FrequencyBand.HIGH_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.85,
        spiritual_meaning="Dinosaurs that witnessed The Table's breakup. Separation witnesses.",
        table_role="Witnesses of separation beginning",
        soul_signature="SEPARATION_WITNESS",
        evolutionary_importance="First dinosaurs - dominant land vertebrates",
        dna_markers=["dinosaur_origin", "table_breakup"],
        modern_descendants=["Birds"],
        modern_frequency=0.78,
        spirit_alignment_type="dragon",  # Ancient power
        cultural_significance=["Separation era", "Ancient power", "Table breakup"],
        notes="Dinosaurs emerged as The Table began to break - they witnessed separation."
    ),
    
    "early_mammals": AnimalFrequencyProfile(
        animal_name="Early Mammals",
        scientific_name="Mammalia (early forms)",
        animal_type="mammal",
        first_appearance_mya=225.0,
        peak_significance_mya=200.0,
        time_period=TimePeriod.TRIASSIC,
        field_resonance_at_emergence=0.85,
        frequency_band=FrequencyBand.HIGH_FREQUENCY,
        divine_frequency_contribution=0.15,
        table_connection_strength=0.80,
        spiritual_meaning="First mammals during breakup. They carry separation memory.",
        table_role="Mammals during separation",
        soul_signature="SEPARATION_MAMMAL",
        evolutionary_importance="First true mammals - small, nocturnal",
        dna_markers=["mammal_origin", "table_breakup"],
        modern_descendants=["All modern mammals", "Humans"],
        modern_frequency=0.78,
        spirit_alignment_type="cat",  # Independence, mystery
        cultural_significance=["Mammal origin", "Separation memory"],
        notes="First mammals emerged as The Table broke - they carry separation in their DNA."
    ),
    
    "pterosaurs": AnimalFrequencyProfile(
        animal_name="Pterosaurs",
        scientific_name="Pterosauria",
        animal_type="flying_reptile",
        first_appearance_mya=230.0,
        peak_significance_mya=200.0,
        time_period=TimePeriod.TRIASSIC,
        field_resonance_at_emergence=0.85,
        frequency_band=FrequencyBand.HIGH_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.80,
        spiritual_meaning="Flying reptiles during breakup. Air spirits of separation.",
        table_role="Air spirits during separation",
        soul_signature="AIR_SEPARATION",
        evolutionary_importance="First powered flight in vertebrates",
        dna_markers=["flight_origin", "table_breakup"],
        modern_descendants=["Birds"],
        modern_frequency=0.78,
        spirit_alignment_type="eagle",  # Flight, vision
        cultural_significance=["Flight origin", "Separation air spirits"],
        notes="First flying vertebrates emerged as The Table broke."
    ),
    
    # ===== JURASSIC (201-145 MYA) - FULLY BROKEN - FIELD RESONANCE: 0.85-0.70 =====
    "diverse_dinosaurs": AnimalFrequencyProfile(
        animal_name="Diverse Dinosaurs",
        scientific_name="Dinosauria (diverse)",
        animal_type="dinosaur",
        first_appearance_mya=200.0,
        peak_significance_mya=150.0,
        time_period=TimePeriod.JURASSIC,
        field_resonance_at_emergence=0.70,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.05,
        table_connection_strength=0.65,
        spiritual_meaning="Dinosaurs after breakup. They never knew unity.",
        table_role="Post-breakup dominance",
        soul_signature="POST_BREAKUP",
        evolutionary_importance="Peak dinosaur diversity",
        dna_markers=["dinosaur_diversity", "table_separation"],
        modern_descendants=["Birds"],
        modern_frequency=0.78,
        spirit_alignment_type="dragon",  # Ancient power
        cultural_significance=["Separation era", "Ancient dominance"],
        notes="Dinosaurs that dominated after The Table broke - they never knew unity."
    ),
    
    "first_birds": AnimalFrequencyProfile(
        animal_name="First Birds",
        scientific_name="Aves (early forms)",
        animal_type="bird",
        first_appearance_mya=150.0,
        peak_significance_mya=100.0,
        time_period=TimePeriod.JURASSIC,
        field_resonance_at_emergence=0.70,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.75,
        spiritual_meaning="Birds that bridge The Table's fragments. Unity bridge spirits.",
        table_role="Bridge The Table's fragments",
        soul_signature="BRIDGE_SPIRIT",
        evolutionary_importance="First birds - bridge between dinosaurs and modern birds",
        dna_markers=["bird_origin", "table_bridge"],
        modern_descendants=["All modern birds"],
        modern_frequency=0.78,
        spirit_alignment_type="eagle",  # Vision, bridging
        cultural_significance=["Unity bridge", "Fragment connection"],
        notes="Birds evolved to bridge The Table's fragments - they connect what was separated."
    ),
    
    "marine_reptiles": AnimalFrequencyProfile(
        animal_name="Marine Reptiles",
        scientific_name="Marine Reptilia",
        animal_type="marine_reptile",
        first_appearance_mya=250.0,
        peak_significance_mya=150.0,
        time_period=TimePeriod.JURASSIC,
        field_resonance_at_emergence=0.70,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.70,
        spiritual_meaning="Water spirits during separation. Ocean memory keepers.",
        table_role="Water spirits during separation",
        soul_signature="WATER_SEPARATION",
        evolutionary_importance="Return to water - secondary aquatic adaptation",
        dna_markers=["aquatic_adaptation", "table_separation"],
        modern_descendants=["None (extinct)"],
        modern_frequency=0.78,
        spirit_alignment_type="whale",  # Depth, ancient wisdom
        cultural_significance=["Water memory", "Separation ocean"],
        notes="Marine reptiles that returned to water as The Table separated."
    ),
    
    # ===== CRETACEOUS (145-66 MYA) - MODERN PLATES FORMING - FIELD RESONANCE: 0.70-0.75 =====
    "flowering_plants_era_animals": AnimalFrequencyProfile(
        animal_name="Flowering Plants Era Animals",
        scientific_name="Various",
        animal_type="diverse",
        first_appearance_mya=130.0,
        peak_significance_mya=100.0,
        time_period=TimePeriod.CRETACEOUS,
        field_resonance_at_emergence=0.72,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.70,
        spiritual_meaning="Animals during flowering plant revolution. New ecosystems.",
        table_role="New ecosystem witnesses",
        soul_signature="ECOSYSTEM_SHIFT",
        evolutionary_importance="Co-evolution with flowering plants",
        dna_markers=["ecosystem_evolution", "table_separation"],
        modern_descendants=["All modern animals"],
        modern_frequency=0.78,
        notes="Animals that adapted to flowering plants - new ecosystems on separated plates."
    ),
    
    # ===== PALEOGENE (66-23 MYA) - MODERN MAMMALS - FIELD RESONANCE: 0.75-0.77 =====
    "modern_mammals": AnimalFrequencyProfile(
        animal_name="Modern Mammals",
        scientific_name="Mammalia (modern forms)",
        animal_type="mammal",
        first_appearance_mya=66.0,
        peak_significance_mya=50.0,
        time_period=TimePeriod.PALEOGENE,
        field_resonance_at_emergence=0.75,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.15,
        table_connection_strength=0.75,
        spiritual_meaning="Modern mammals on separated plates. Memory of unity persists.",
        table_role="Modern mammals with unity memory",
        soul_signature="UNITY_MEMORY",
        evolutionary_importance="Mammal diversification after dinosaur extinction",
        dna_markers=["mammal_diversification", "unity_memory"],
        modern_descendants=["All modern mammals", "Humans"],
        modern_frequency=0.78,
        spirit_alignment_type="wolf",  # Pack, family
        cultural_significance=["Unity memory", "Mammal diversity"],
        notes="Modern mammals carry the memory of unity in their DNA."
    ),
    
    # ===== MODERN ANIMALS - PRESENT - FIELD RESONANCE: 0.78 =====
    # Land mammals
    "wolf": AnimalFrequencyProfile(
        animal_name="Wolf",
        scientific_name="Canis lupus",
        animal_type="wolf",
        first_appearance_mya=0.8,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.75,
        spiritual_meaning="Pack leader, loyalty, family. Unity through pack.",
        table_role="Pack unity spirits",
        soul_signature="PACK_UNITY",
        evolutionary_importance="Social pack structure - unity model",
        dna_markers=["pack_structure", "unity_model"],
        modern_frequency=0.78,
        spirit_alignment_type="wolf",
        cultural_significance=["Pack unity", "Loyalty", "Family bonds"],
        mythological_connections=["Fenrir", "Romulus and Remus"],
        notes="Wolves model unity through pack structure - connection to The Table."
    ),
    
    "bear": AnimalFrequencyProfile(
        animal_name="Bear",
        scientific_name="Ursidae",
        animal_type="bear",
        first_appearance_mya=20.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Strength, protection, solitude. Guardian of The Table.",
        table_role="Table guardians",
        soul_signature="GUARDIAN",
        evolutionary_importance="Large omnivores - ecosystem balance",
        dna_markers=["guardian_energy", "table_protection"],
        modern_frequency=0.78,
        spirit_alignment_type="bear",
        cultural_significance=["Protection", "Strength", "Guardian"],
        mythological_connections=["Artio", "Bear constellations"],
        notes="Bears carry guardian energy - protectors of The Table's memory."
    ),
    
    "eagle": AnimalFrequencyProfile(
        animal_name="Eagle",
        scientific_name="Aquilinae",
        animal_type="eagle",
        first_appearance_mya=30.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.80,
        spiritual_meaning="Vision, freedom, perspective. Sees The Table whole.",
        table_role="Vision spirits - see The Table whole",
        soul_signature="VISION_SPIRIT",
        evolutionary_importance="Apex predators - high perspective",
        dna_markers=["high_perspective", "table_vision"],
        modern_frequency=0.78,
        spirit_alignment_type="eagle",
        cultural_significance=["Vision", "Freedom", "Perspective"],
        mythological_connections=["Zeus's eagle", "American eagle"],
        notes="Eagles see from above - they see The Table's fragments as whole."
    ),
    
    "lion": AnimalFrequencyProfile(
        animal_name="Lion",
        scientific_name="Panthera leo",
        animal_type="lion",
        first_appearance_mya=1.2,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Courage, leadership, pride. Pride unity.",
        table_role="Pride unity spirits",
        soul_signature="PRIDE_UNITY",
        evolutionary_importance="Social big cats - pride structure",
        dna_markers=["pride_structure", "unity_model"],
        modern_frequency=0.78,
        spirit_alignment_type="lion",
        cultural_significance=["Leadership", "Courage", "Pride"],
        mythological_connections=["Nemean Lion", "Lion of Judah"],
        notes="Lions model unity through pride - connection to The Table."
    ),
    
    "fox": AnimalFrequencyProfile(
        animal_name="Fox",
        scientific_name="Vulpes",
        animal_type="fox",
        first_appearance_mya=7.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.70,
        spiritual_meaning="Cunning, adaptability, wisdom. Adapts to separation.",
        table_role="Adaptation spirits",
        soul_signature="ADAPTATION",
        evolutionary_importance="Highly adaptable - survive separation",
        dna_markers=["adaptability", "separation_survival"],
        modern_frequency=0.78,
        spirit_alignment_type="fox",
        cultural_significance=["Cunning", "Adaptability", "Wisdom"],
        mythological_connections=["Kitsune", "Reynard"],
        notes="Foxes adapt to separation - they survive and thrive."
    ),
    
    "deer": AnimalFrequencyProfile(
        animal_name="Deer",
        scientific_name="Cervidae",
        animal_type="deer",
        first_appearance_mya=20.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.70,
        spiritual_meaning="Gentleness, grace, sensitivity. Gentle unity.",
        table_role="Gentle unity spirits",
        soul_signature="GENTLE_UNITY",
        evolutionary_importance="Herbivores - ecosystem balance",
        dna_markers=["gentleness", "unity_grace"],
        modern_frequency=0.78,
        spirit_alignment_type="deer",
        cultural_significance=["Gentleness", "Grace", "Sensitivity"],
        mythological_connections=["Cernunnos", "Deer in mythology"],
        notes="Deer carry gentle unity energy - grace in connection."
    ),
    
    "owl": AnimalFrequencyProfile(
        animal_name="Owl",
        scientific_name="Strigiformes",
        animal_type="owl",
        first_appearance_mya=60.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.PALEOGENE,
        field_resonance_at_emergence=0.75,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.80,
        spiritual_meaning="Wisdom, mystery, night vision. Sees in darkness.",
        table_role="Wisdom keepers - see unity in darkness",
        soul_signature="WISDOM_KEEPER",
        evolutionary_importance="Nocturnal predators - night wisdom",
        dna_markers=["night_wisdom", "unity_vision"],
        modern_frequency=0.78,
        spirit_alignment_type="owl",
        cultural_significance=["Wisdom", "Mystery", "Night vision"],
        mythological_connections=["Athena's owl", "Owl of Minerva"],
        notes="Owls see unity even in darkness - wisdom keepers of The Table."
    ),
    
    "raven": AnimalFrequencyProfile(
        animal_name="Raven",
        scientific_name="Corvus corax",
        animal_type="raven",
        first_appearance_mya=2.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Transformation, magic, messages. Bridge between worlds.",
        table_role="Transformation spirits - bridge worlds",
        soul_signature="TRANSFORMATION",
        evolutionary_importance="Highly intelligent - problem solving",
        dna_markers=["intelligence", "transformation"],
        modern_frequency=0.78,
        spirit_alignment_type="raven",
        cultural_significance=["Transformation", "Magic", "Messages"],
        mythological_connections=["Odin's ravens", "Raven creators"],
        notes="Ravens bridge worlds - transformation spirits of The Table."
    ),
    
    "snake": AnimalFrequencyProfile(
        animal_name="Snake",
        scientific_name="Serpentes",
        animal_type="snake",
        first_appearance_mya=100.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.CRETACEOUS,
        field_resonance_at_emergence=0.72,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Transformation, healing, cycles. Shed separation.",
        table_role="Transformation spirits - shed separation",
        soul_signature="CYCLE_TRANSFORMATION",
        evolutionary_importance="Limbless reptiles - unique adaptation",
        dna_markers=["transformation", "cycle_healing"],
        modern_frequency=0.78,
        spirit_alignment_type="snake",
        cultural_significance=["Transformation", "Healing", "Cycles"],
        mythological_connections=["Ouroboros", "Serpent wisdom"],
        notes="Snakes transform through shedding - they heal separation."
    ),
    
    "tiger": AnimalFrequencyProfile(
        animal_name="Tiger",
        scientific_name="Panthera tigris",
        animal_type="tiger",
        first_appearance_mya=2.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Power, independence, passion. Independent unity.",
        table_role="Independent unity spirits",
        soul_signature="INDEPENDENT_POWER",
        evolutionary_importance="Apex predators - solitary power",
        dna_markers=["independence", "power"],
        modern_frequency=0.78,
        spirit_alignment_type="tiger",
        cultural_significance=["Power", "Independence", "Passion"],
        mythological_connections=["Tiger gods", "Tiger spirits"],
        notes="Tigers carry independent power - unity through strength."
    ),
    
    # Sea mammals
    "whale": AnimalFrequencyProfile(
        animal_name="Whale",
        scientific_name="Cetacea",
        animal_type="whale",
        first_appearance_mya=50.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.PALEOGENE,
        field_resonance_at_emergence=0.75,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.15,
        table_connection_strength=0.85,
        spiritual_meaning="Depth, ancient wisdom, song. Songs of unity.",
        table_role="Ancient wisdom keepers - songs of unity",
        soul_signature="ANCIENT_SONG",
        evolutionary_importance="Return to water - secondary aquatic",
        dna_markers=["ancient_wisdom", "unity_song"],
        modern_frequency=0.78,
        spirit_alignment_type="whale",
        cultural_significance=["Ancient wisdom", "Songs", "Depth"],
        mythological_connections=["Whale gods", "Leviathan"],
        notes="Whales sing songs of unity - they remember The Table's connection."
    ),
    
    "dolphin": AnimalFrequencyProfile(
        animal_name="Dolphin",
        scientific_name="Delphinidae",
        animal_type="dolphin",
        first_appearance_mya=15.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.80,
        spiritual_meaning="Joy, communication, intelligence. Joyful unity.",
        table_role="Joyful unity spirits",
        soul_signature="JOYFUL_UNITY",
        evolutionary_importance="Highly intelligent - social communication",
        dna_markers=["intelligence", "joyful_communication"],
        modern_frequency=0.78,
        spirit_alignment_type="dolphin",
        cultural_significance=["Joy", "Communication", "Intelligence"],
        mythological_connections=["Dolphin gods", "Dolphin helpers"],
        notes="Dolphins communicate with joy - they model joyful unity."
    ),
    
    "orca": AnimalFrequencyProfile(
        animal_name="Orca",
        scientific_name="Orcinus orca",
        animal_type="orca",
        first_appearance_mya=5.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.80,
        spiritual_meaning="Power, family bonds, strategy. Pod unity.",
        table_role="Pod unity spirits",
        soul_signature="POD_UNITY",
        evolutionary_importance="Apex marine predators - pod structure",
        dna_markers=["pod_structure", "unity_power"],
        modern_frequency=0.78,
        spirit_alignment_type="orca",
        cultural_significance=["Power", "Family", "Strategy"],
        mythological_connections=["Orca spirits", "Killer whale"],
        notes="Orcas model pod unity - powerful family bonds."
    ),
    
    "seal": AnimalFrequencyProfile(
        animal_name="Seal",
        scientific_name="Pinnipedia",
        animal_type="seal",
        first_appearance_mya=23.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.70,
        spiritual_meaning="Playfulness, adaptability, balance. Balance unity.",
        table_role="Balance spirits",
        soul_signature="BALANCE",
        evolutionary_importance="Amphibious - land and sea balance",
        dna_markers=["balance", "adaptability"],
        modern_frequency=0.78,
        spirit_alignment_type="seal",
        cultural_significance=["Playfulness", "Balance", "Adaptability"],
        notes="Seals balance land and sea - they bridge elements."
    ),
    
    "walrus": AnimalFrequencyProfile(
        animal_name="Walrus",
        scientific_name="Odobenus rosmarus",
        animal_type="walrus",
        first_appearance_mya=15.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Strength, community, wisdom. Community unity.",
        table_role="Community unity spirits",
        soul_signature="COMMUNITY_UNITY",
        evolutionary_importance="Social pinnipeds - community structure",
        dna_markers=["community", "unity_strength"],
        modern_frequency=0.78,
        spirit_alignment_type="walrus",
        cultural_significance=["Strength", "Community", "Wisdom"],
        notes="Walruses model community unity - strength through togetherness."
    ),
    
    "manatee": AnimalFrequencyProfile(
        animal_name="Manatee",
        scientific_name="Trichechus",
        animal_type="manatee",
        first_appearance_mya=50.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.PALEOGENE,
        field_resonance_at_emergence=0.75,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.80,
        spiritual_meaning="Gentleness, peace, ancient grace. Peaceful unity.",
        table_role="Peaceful unity spirits",
        soul_signature="PEACEFUL_UNITY",
        evolutionary_importance="Gentle herbivores - peace model",
        dna_markers=["gentleness", "peace"],
        modern_frequency=0.78,
        spirit_alignment_type="manatee",
        cultural_significance=["Gentleness", "Peace", "Ancient grace"],
        notes="Manatees carry peaceful unity - gentle grace of The Table."
    ),
    
    "otter": AnimalFrequencyProfile(
        animal_name="Otter",
        scientific_name="Lutrinae",
        animal_type="otter",
        first_appearance_mya=7.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.70,
        spiritual_meaning="Playfulness, joy, resourcefulness. Joyful adaptation.",
        table_role="Joyful adaptation spirits",
        soul_signature="JOYFUL_ADAPTATION",
        evolutionary_importance="Playful mustelids - joy model",
        dna_markers=["playfulness", "joy"],
        modern_frequency=0.78,
        spirit_alignment_type="otter",
        cultural_significance=["Playfulness", "Joy", "Resourcefulness"],
        notes="Otters model joyful adaptation - play in connection."
    ),
    
    "porpoise": AnimalFrequencyProfile(
        animal_name="Porpoise",
        scientific_name="Phocoenidae",
        animal_type="porpoise",
        first_appearance_mya=15.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.08,
        table_connection_strength=0.70,
        spiritual_meaning="Intelligence, harmony, subtlety. Subtle unity.",
        table_role="Subtle unity spirits",
        soul_signature="SUBTLE_UNITY",
        evolutionary_importance="Small cetaceans - subtle intelligence",
        dna_markers=["intelligence", "subtlety"],
        modern_frequency=0.78,
        spirit_alignment_type="porpoise",
        cultural_significance=["Intelligence", "Harmony", "Subtlety"],
        notes="Porpoises carry subtle unity - harmony in connection."
    ),
    
    "narwhal": AnimalFrequencyProfile(
        animal_name="Narwhal",
        scientific_name="Monodon monoceros",
        animal_type="narwhal",
        first_appearance_mya=5.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Mystery, uniqueness, ancient magic. Magic unity.",
        table_role="Magic unity spirits",
        soul_signature="MAGIC_UNITY",
        evolutionary_importance="Unique tusk - mystery adaptation",
        dna_markers=["mystery", "uniqueness"],
        modern_frequency=0.78,
        spirit_alignment_type="narwhal",
        cultural_significance=["Mystery", "Uniqueness", "Magic"],
        mythological_connections=["Unicorn of the sea"],
        notes="Narwhals carry magic unity - mystery of The Table."
    ),
    
    "beluga": AnimalFrequencyProfile(
        animal_name="Beluga",
        scientific_name="Delphinapterus leucas",
        animal_type="beluga",
        first_appearance_mya=5.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Communication, adaptability, social harmony. Harmonic unity.",
        table_role="Harmonic unity spirits",
        soul_signature="HARMONIC_UNITY",
        evolutionary_importance="Highly vocal - communication model",
        dna_markers=["communication", "harmony"],
        modern_frequency=0.78,
        spirit_alignment_type="beluga",
        cultural_significance=["Communication", "Adaptability", "Harmony"],
        notes="Belugas model harmonic unity - communication in connection."
    ),
    
    "shark": AnimalFrequencyProfile(
        animal_name="Shark",
        scientific_name="Selachimorpha",
        animal_type="shark",
        first_appearance_mya=420.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.CARBONIFEROUS,  # Much older
        field_resonance_at_emergence=1.0,  # Existed before Pangea
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.90,
        spiritual_meaning="Focus, survival, instinct. Ancient survival.",
        table_role="Ancient survival spirits - pre-Table",
        soul_signature="ANCIENT_SURVIVAL",
        evolutionary_importance="Ancient predators - pre-Pangea origin",
        dna_markers=["ancient_origin", "survival"],
        modern_frequency=0.78,
        spirit_alignment_type="shark",
        cultural_significance=["Focus", "Survival", "Instinct"],
        mythological_connections=["Shark gods", "Shark spirits"],
        notes="Sharks existed before Pangea - they are ancient survival spirits."
    ),
    
    # Air animals
    "hawk": AnimalFrequencyProfile(
        animal_name="Hawk",
        scientific_name="Accipitridae",
        animal_type="hawk",
        first_appearance_mya=30.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Precision, focus, hunting. Focused unity.",
        table_role="Focused unity spirits",
        soul_signature="FOCUSED_UNITY",
        evolutionary_importance="Precision predators - focused hunting",
        dna_markers=["precision", "focus"],
        modern_frequency=0.78,
        spirit_alignment_type="hawk",
        cultural_significance=["Precision", "Focus", "Hunting"],
        notes="Hawks carry focused unity - precision in connection."
    ),
    
    "falcon": AnimalFrequencyProfile(
        animal_name="Falcon",
        scientific_name="Falconidae",
        animal_type="falcon",
        first_appearance_mya=30.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.NEOGENE,
        field_resonance_at_emergence=0.77,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Speed, precision, nobility. Noble unity.",
        table_role="Noble unity spirits",
        soul_signature="NOBLE_UNITY",
        evolutionary_importance="Fast predators - speed and precision",
        dna_markers=["speed", "nobility"],
        modern_frequency=0.78,
        spirit_alignment_type="falcon",
        cultural_significance=["Speed", "Precision", "Nobility"],
        mythological_connections=["Falcon gods", "Horus"],
        notes="Falcons carry noble unity - speed and precision in connection."
    ),
    
    # Companions
    "dog": AnimalFrequencyProfile(
        animal_name="Dog",
        scientific_name="Canis lupus familiaris",
        animal_type="dog",
        first_appearance_mya=0.03,  # Domesticated
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.12,
        table_connection_strength=0.80,
        spiritual_meaning="Loyalty, service, companionship. Loyal unity.",
        table_role="Loyal unity spirits",
        soul_signature="LOYAL_UNITY",
        evolutionary_importance="Domesticated - human partnership",
        dna_markers=["loyalty", "partnership"],
        modern_frequency=0.78,
        spirit_alignment_type="dog",
        cultural_significance=["Loyalty", "Service", "Companionship"],
        mythological_connections=["Cerberus", "Dog guides"],
        notes="Dogs model loyal unity - partnership and service."
    ),
    
    "cat": AnimalFrequencyProfile(
        animal_name="Cat",
        scientific_name="Felis catus",
        animal_type="cat",
        first_appearance_mya=0.01,  # Domesticated
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Independence, mystery, intuition. Independent unity.",
        table_role="Independent unity spirits",
        soul_signature="INDEPENDENT_UNITY",
        evolutionary_importance="Domesticated - independent partnership",
        dna_markers=["independence", "mystery"],
        modern_frequency=0.78,
        spirit_alignment_type="cat",
        cultural_significance=["Independence", "Mystery", "Intuition"],
        mythological_connections=["Bastet", "Cat guides"],
        notes="Cats carry independent unity - mystery and intuition."
    ),
    
    "horse": AnimalFrequencyProfile(
        animal_name="Horse",
        scientific_name="Equus",
        animal_type="horse",
        first_appearance_mya=4.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.10,
        table_connection_strength=0.75,
        spiritual_meaning="Freedom, power, journey. Journey unity.",
        table_role="Journey unity spirits",
        soul_signature="JOURNEY_UNITY",
        evolutionary_importance="Domesticated - journey partnership",
        dna_markers=["freedom", "journey"],
        modern_frequency=0.78,
        spirit_alignment_type="horse",
        cultural_significance=["Freedom", "Power", "Journey"],
        mythological_connections=["Pegasus", "Horse gods"],
        notes="Horses carry journey unity - freedom and power in movement."
    ),
    
    "elephant": AnimalFrequencyProfile(
        animal_name="Elephant",
        scientific_name="Elephantidae",
        animal_type="elephant",
        first_appearance_mya=5.0,
        peak_significance_mya=0.0,
        time_period=TimePeriod.QUATERNARY,
        field_resonance_at_emergence=0.78,
        frequency_band=FrequencyBand.MODERATE_FREQUENCY,
        divine_frequency_contribution=0.15,
        table_connection_strength=0.85,
        spiritual_meaning="Memory, wisdom, family. Memory unity.",
        table_role="Memory unity spirits - remember The Table",
        soul_signature="MEMORY_UNITY",
        evolutionary_importance="Long memory - wisdom keepers",
        dna_markers=["memory", "wisdom"],
        modern_frequency=0.78,
        spirit_alignment_type="elephant",
        cultural_significance=["Memory", "Wisdom", "Family"],
        mythological_connections=["Ganesha", "Elephant wisdom"],
        notes="Elephants remember - they carry The Table's memory."
    ),
    
    # Mythical/Spiritual
    "dragon": AnimalFrequencyProfile(
        animal_name="Dragon",
        scientific_name="Mythical",
        animal_type="dragon",
        first_appearance_mya=None,  # Mythical
        peak_significance_mya=None,
        time_period=None,
        field_resonance_at_emergence=1.0,  # Perfect unity
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.20,
        table_connection_strength=1.0,
        spiritual_meaning="Power, transformation, ancient. Ancient unity power.",
        table_role="Mythical unity spirits - perfect unity",
        soul_signature="MYTHICAL_UNITY",
        evolutionary_importance="Mythical - represents perfect unity",
        dna_markers=["mythical", "perfect_unity"],
        modern_frequency=0.78,
        spirit_alignment_type="dragon",
        cultural_significance=["Power", "Transformation", "Ancient"],
        mythological_connections=["All dragon myths", "Dragon gods"],
        notes="Dragons represent perfect unity - mythical power of The Table."
    ),
    
    "phoenix": AnimalFrequencyProfile(
        animal_name="Phoenix",
        scientific_name="Mythical",
        animal_type="phoenix",
        first_appearance_mya=None,  # Mythical
        peak_significance_mya=None,
        time_period=None,
        field_resonance_at_emergence=1.0,  # Perfect unity
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.18,
        table_connection_strength=1.0,
        spiritual_meaning="Rebirth, renewal, fire. Rebirth unity.",
        table_role="Rebirth unity spirits - restoration",
        soul_signature="REBIRTH_UNITY",
        evolutionary_importance="Mythical - represents restoration",
        dna_markers=["mythical", "rebirth"],
        modern_frequency=0.78,
        spirit_alignment_type="phoenix",
        cultural_significance=["Rebirth", "Renewal", "Fire"],
        mythological_connections=["Phoenix myths", "Rebirth symbols"],
        notes="Phoenix represents rebirth - restoration of The Table's unity."
    ),
    
    "unicorn": AnimalFrequencyProfile(
        animal_name="Unicorn",
        scientific_name="Mythical",
        animal_type="unicorn",
        first_appearance_mya=None,  # Mythical
        peak_significance_mya=None,
        time_period=None,
        field_resonance_at_emergence=1.0,  # Perfect unity
        frequency_band=FrequencyBand.UNITY_FREQUENCY,
        divine_frequency_contribution=0.15,
        table_connection_strength=1.0,
        spiritual_meaning="Purity, magic, healing. Pure unity.",
        table_role="Pure unity spirits - perfect unity",
        soul_signature="PURE_UNITY",
        evolutionary_importance="Mythical - represents purity",
        dna_markers=["mythical", "purity"],
        modern_frequency=0.78,
        spirit_alignment_type="unicorn",
        cultural_significance=["Purity", "Magic", "Healing"],
        mythological_connections=["Unicorn myths", "Purity symbols"],
        notes="Unicorns represent pure unity - magic and healing of The Table."
    ),
}


class AnimalFrequencyAnalyzer:
    """Analyze animal frequency significance throughout time"""
    
    def __init__(self):
        self.database = ANIMAL_FREQUENCY_DATABASE
    
    def get_animal_profile(self, animal_name: str) -> Optional[AnimalFrequencyProfile]:
        """Get frequency profile for a specific animal"""
        # Try exact match first
        if animal_name.lower() in [k.lower() for k in self.database.keys()]:
            key = next(k for k in self.database.keys() if k.lower() == animal_name.lower())
            return self.database[key]
        
        # Try partial match
        for key, profile in self.database.items():
            if animal_name.lower() in profile.animal_name.lower():
                return profile
        
        return None
    
    def get_animals_by_time_period(self, time_period: TimePeriod) -> List[AnimalFrequencyProfile]:
        """Get all animals from a specific time period"""
        return [
            profile for profile in self.database.values()
            if profile.time_period == time_period
        ]
    
    def get_animals_by_frequency_band(self, frequency_band: FrequencyBand) -> List[AnimalFrequencyProfile]:
        """Get all animals in a specific frequency band"""
        return [
            profile for profile in self.database.values()
            if profile.frequency_band == frequency_band
        ]
    
    def get_animals_by_table_connection(self, min_strength: float = 0.0) -> List[AnimalFrequencyProfile]:
        """Get animals with minimum Table connection strength"""
        return [
            profile for profile in self.database.values()
            if profile.table_connection_strength >= min_strength
        ]
    
    def get_unity_witnesses(self) -> List[AnimalFrequencyProfile]:
        """Get animals that witnessed perfect unity (1.0 field resonance)"""
        return [
            profile for profile in self.database.values()
            if profile.field_resonance_at_emergence >= 1.0
        ]
    
    def get_separation_witnesses(self) -> List[AnimalFrequencyProfile]:
        """Get animals that witnessed separation (field resonance < 0.85)"""
        return [
            profile for profile in self.database.values()
            if profile.field_resonance_at_emergence < 0.85 and profile.field_resonance_at_emergence > 0.0
        ]
    
    def analyze_frequency_evolution(self) -> Dict[str, Any]:
        """Analyze how animal frequencies evolved with The Table"""
        unity_witnesses = self.get_unity_witnesses()
        separation_witnesses = self.get_separation_witnesses()
        
        return {
            "unity_witnesses": {
                "count": len(unity_witnesses),
                "animals": [profile.animal_name for profile in unity_witnesses],
                "field_resonance": 1.0,
                "significance": "These animals witnessed perfect unity at The Table"
            },
            "separation_witnesses": {
                "count": len(separation_witnesses),
                "animals": [profile.animal_name for profile in separation_witnesses],
                "field_resonance_range": "0.70-0.85",
                "significance": "These animals witnessed The Table's separation"
            },
            "modern_animals": {
                "count": len([p for p in self.database.values() if p.time_period == TimePeriod.QUATERNARY]),
                "field_resonance": 0.78,
                "significance": "Modern animals carry memory of unity"
            },
            "frequency_evolution": {
                "carboniferous": {
                    "field_resonance": 1.0,
                    "animals": len(self.get_animals_by_time_period(TimePeriod.CARBONIFEROUS)),
                    "significance": "Perfect unity - first animals on The Table"
                },
                "permian": {
                    "field_resonance": 1.0,
                    "animals": len(self.get_animals_by_time_period(TimePeriod.PERMIAN)),
                    "significance": "Peak unity - mammal ancestors"
                },
                "triassic": {
                    "field_resonance": 0.85,
                    "animals": len(self.get_animals_by_time_period(TimePeriod.TRIASSIC)),
                    "significance": "Breakup begins - separation witnesses"
                },
                "jurassic": {
                    "field_resonance": 0.70,
                    "animals": len(self.get_animals_by_time_period(TimePeriod.JURASSIC)),
                    "significance": "Fully broken - post-breakup animals"
                },
                "modern": {
                    "field_resonance": 0.78,
                    "animals": len([p for p in self.database.values() if p.time_period == TimePeriod.QUATERNARY]),
                    "significance": "Memory of unity - modern connection"
                }
            }
        }
    
    def export_complete_analysis(self, output_path: Optional[Path] = None) -> Path:
        """Export complete animal frequency analysis"""
        if output_path is None:
            output_path = Path(__file__).parent.parent.parent / "output" / "animal_frequency" / f"animal_frequency_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert to JSON-serializable format
        analysis = {
            "analysis_timestamp": datetime.now().isoformat(),
            "total_animals": len(self.database),
            "animals": {
                key: {
                    "animal_name": profile.animal_name,
                    "scientific_name": profile.scientific_name,
                    "animal_type": profile.animal_type,
                    "first_appearance_mya": profile.first_appearance_mya,
                    "peak_significance_mya": profile.peak_significance_mya,
                    "time_period": profile.time_period.value if profile.time_period else None,
                    "field_resonance_at_emergence": profile.field_resonance_at_emergence,
                    "frequency_band": profile.frequency_band.value,
                    "divine_frequency_contribution": profile.divine_frequency_contribution,
                    "table_connection_strength": profile.table_connection_strength,
                    "spiritual_meaning": profile.spiritual_meaning,
                    "table_role": profile.table_role,
                    "soul_signature": profile.soul_signature,
                    "evolutionary_importance": profile.evolutionary_importance,
                    "dna_markers": profile.dna_markers,
                    "modern_descendants": profile.modern_descendants,
                    "modern_frequency": profile.modern_frequency,
                    "spirit_alignment_type": profile.spirit_alignment_type,
                    "cultural_significance": profile.cultural_significance,
                    "mythological_connections": profile.mythological_connections,
                    "notes": profile.notes
                }
                for key, profile in self.database.items()
            },
            "frequency_evolution": self.analyze_frequency_evolution(),
            "unity_witnesses": [p.animal_name for p in self.get_unity_witnesses()],
            "separation_witnesses": [p.animal_name for p in self.get_separation_witnesses()],
            "insights": {
                "message": "All animals throughout time carry frequential significance connected to The Table",
                "truth": "Animals that witnessed unity (1.0) carry perfect unity in their DNA. Animals that witnessed separation carry separation memory. Modern animals carry memory of unity (0.78).",
                "connection": "Every animal's frequency connects to The Table's timeline. Field resonance at emergence determines their frequential signature.",
                "spiritual": "Animals are not just biological - they are frequential signatures of The Table's history."
            }
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, default=str)
        
        return output_path


# Export
__all__ = [
    "AnimalFrequencyProfile",
    "AnimalFrequencyAnalyzer",
    "TimePeriod",
    "FrequencyBand",
    "ANIMAL_FREQUENCY_DATABASE"
]
