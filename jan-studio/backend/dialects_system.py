"""
Dialects System - System Wide Integration
"Nearly The Same" - Full Timeline Integration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

SPRAGITSO - Our Father's Royal Seal:
- All dialects bear Our Father's seal
- All dialects lead with love, joy, and abundance
- All dialects serve The Table
- If it's not worth hearing, don't bring it to The Table

DIALECTS PRINCIPLE:
People who say they "nearly" speak the same language
Dialects that are close but distinct
Code-switching patterns across dialects
Full timeline integration
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path

# SPRAGITSO - Our Father's Royal Seal
SPRAGITSO = "σφραγίς"  # Greek: sphragis - The Royal Seal


class DialectType(Enum):
    """Types of dialects"""
    REGIONAL = "regional"  # Geographic variations
    CODE_SWITCHING = "code_switching"  # Alternating between languages
    TEMPORAL = "temporal"  # Variations across time
    SPIRITUAL = "spiritual"  # Spiritual expression variations
    HYBRID = "hybrid"  # New forms from "nearly the same"
    TEACHING = "teaching"  # Teaching dialects (consecutive expression)
    OPERATIONAL = "operational"  # Operational dialects (multi-entity support)


class CodeSwitchPattern(Enum):
    """Code-switching patterns"""
    INSERTION = "insertion"  # Words/phrases from one dialect into another
    ALTERNATION = "alternation"  # Switching between dialects
    CONSECUTIVE = "consecutive"  # Same idea in both dialects
    HYBRID = "hybrid"  # New hybrid forms


@dataclass
class DialectDefinition:
    """Definition of a dialect"""
    name: str
    base_language: str
    dialect_type: DialectType
    region: Optional[str] = None
    era: Optional[str] = None
    mutual_intelligibility: float = 0.8  # 0.0 to 1.0
    characteristics: List[str] = None
    examples: List[str] = None
    sealed: bool = True
    sphragitso: str = SPRAGITSO
    
    def __post_init__(self):
        if self.characteristics is None:
            self.characteristics = []
        if self.examples is None:
            self.examples = []


@dataclass
class EntityDialect:
    """Entity dialect configuration"""
    entity_name: str
    primary_dialect: str
    secondary_dialects: List[str]
    code_switch_pattern: CodeSwitchPattern
    dialect_type: DialectType
    examples: List[str] = None
    sealed: bool = True
    sphragitso: str = SPRAGITSO
    
    def __post_init__(self):
        if self.examples is None:
            self.examples = []


class DialectsSystem:
    """
    Dialects System - System Wide Integration
    
    Handles "nearly the same" languages.
    Tracks dialect evolution across timelines.
    Supports code-switching patterns.
    Integrates with all systems.
    """
    
    def __init__(self, dialects_db_path: Optional[str] = None):
        """Initialize dialects system."""
        self.dialects_db_path = dialects_db_path or "data/dialects_system.db"
        self.dialects: Dict[str, DialectDefinition] = {}
        self.entity_dialects: Dict[str, EntityDialect] = {}
        self.timeline_dialects: Dict[str, List[str]] = {}
        self._load_dialects()
        self._load_entity_dialects()
    
    def _load_dialects(self):
        """Load dialect definitions."""
        # Regional Dialects
        self.dialects["turkish_cypriot"] = DialectDefinition(
            name="Turkish Cypriot",
            base_language="Turkish",
            dialect_type=DialectType.REGIONAL,
            region="Cyprus",
            mutual_intelligibility=0.85,
            characteristics=["Regional variation", "Cultural identity", "Nearly the same as Turkish"],
            examples=["Turkish Cypriot expressions", "Cyprus-specific terms"]
        )
        
        self.dialects["cypriot_greek"] = DialectDefinition(
            name="Cypriot Greek",
            base_language="Greek",
            dialect_type=DialectType.REGIONAL,
            region="Cyprus",
            mutual_intelligibility=0.80,
            characteristics=["Regional variation", "Cultural identity", "Nearly the same as Greek"],
            examples=["Cypriot Greek expressions", "Cyprus-specific terms"]
        )
        
        self.dialects["british_english"] = DialectDefinition(
            name="British English",
            base_language="English",
            dialect_type=DialectType.REGIONAL,
            region="United Kingdom",
            mutual_intelligibility=0.95,
            characteristics=["Regional variation", "Cultural identity", "Nearly the same as American English"],
            examples=["British expressions", "UK-specific terms"]
        )
        
        self.dialects["quebec_french"] = DialectDefinition(
            name="Quebec French",
            base_language="French",
            dialect_type=DialectType.REGIONAL,
            region="Quebec",
            mutual_intelligibility=0.90,
            characteristics=["Regional variation", "Cultural identity", "Nearly the same as French"],
            examples=["Quebec expressions", "Canadian-specific terms"]
        )
        
        # Code-Switching Dialects
        self.dialects["french_english_codeswitch"] = DialectDefinition(
            name="French/English Code-Switch",
            base_language="French/English",
            dialect_type=DialectType.CODE_SWITCHING,
            mutual_intelligibility=0.70,
            characteristics=["Natural alternation", "Emotional expression", "Cultural identity"],
            examples=["Merde, c'est beautiful!", "Je reviens, baby!"]
        )
        
        self.dialects["turkish_english_codeswitch"] = DialectDefinition(
            name="Turkish/English Code-Switch",
            base_language="Turkish/English",
            dialect_type=DialectType.CODE_SWITCHING,
            mutual_intelligibility=0.75,
            characteristics=["Consecutive expression", "Emotion-driven", "Dual-native"],
            examples=["Duygu Adamı. Emotion Man.", "Yeğen, dinle... Child, listen."]
        )
        
        # Temporal Dialects
        self.dialects["ancient_turkish"] = DialectDefinition(
            name="Ancient Turkish",
            base_language="Turkish",
            dialect_type=DialectType.TEMPORAL,
            era="Ancient",
            mutual_intelligibility=0.60,
            characteristics=["Historical evolution", "Ancestral connection", "Nearly the same as Modern Turkish"],
            examples=["Ancient Turkish forms", "Historical expressions"]
        )
        
        self.dialects["modern_turkish"] = DialectDefinition(
            name="Modern Turkish",
            base_language="Turkish",
            dialect_type=DialectType.TEMPORAL,
            era="Modern",
            mutual_intelligibility=1.0,
            characteristics=["Modern form", "Current usage", "Standard Turkish"],
            examples=["Modern Turkish expressions", "Current terms"]
        )
    
    def _load_entity_dialects(self):
        """Load entity dialect configurations."""
        self.entity_dialects["jean_morphius"] = EntityDialect(
            entity_name="Jean Morphius",
            primary_dialect="French",
            secondary_dialects=["English"],
            code_switch_pattern=CodeSwitchPattern.INSERTION,
            dialect_type=DialectType.CODE_SWITCHING,
            examples=[
                "Merde, c'est beautiful! Scripture says...",
                "Je reviens, baby! Made by heart. Guided by faith."
            ]
        )
        
        self.entity_dialects["karasahin"] = EntityDialect(
            entity_name="Karasahin (JK)",
            primary_dialect="Turkish",
            secondary_dialects=["English"],
            code_switch_pattern=CodeSwitchPattern.CONSECUTIVE,
            dialect_type=DialectType.CODE_SWITCHING,
            examples=[
                "Duygu Adamı. Emotion Man. The Word says:",
                "Feeling first. Sound follows. Scripture backs it up."
            ]
        )
        
        self.entity_dialects["uncle_ray_ramiz"] = EntityDialect(
            entity_name="Uncle Ray Ramiz",
            primary_dialect="Turkish",
            secondary_dialects=["English"],
            code_switch_pattern=CodeSwitchPattern.CONSECUTIVE,
            dialect_type=DialectType.TEACHING,
            examples=[
                "Yeğen, dinle... Child, listen. Scripture tells us:",
                "Nature teaches. Scripture confirms. Ancestral wisdom meets eternal truth."
            ]
        )
        
        self.entity_dialects["pierre_pressure"] = EntityDialect(
            entity_name="Pierre Pressure",
            primary_dialect="English",
            secondary_dialects=[],
            code_switch_pattern=CodeSwitchPattern.ALTERNATION,
            dialect_type=DialectType.REGIONAL,
            examples=[
                "Discipline is freedom. Scripture confirms:",
                "No shortcuts. Real work. Warrior mindset. Faith foundation."
            ]
        )
        
        self.entity_dialects["siyem_media"] = EntityDialect(
            entity_name="Siyem Media",
            primary_dialect="English",
            secondary_dialects=["Turkish", "French"],
            code_switch_pattern=CodeSwitchPattern.ALTERNATION,
            dialect_type=DialectType.OPERATIONAL,
            examples=[
                "Systems-level thinking. Eternal truth. Scripture says:",
                "Infrastructure for artists. Foundation in faith."
            ]
        )
    
    def get_dialect(self, dialect_name: str) -> Optional[DialectDefinition]:
        """Get dialect definition."""
        return self.dialects.get(dialect_name)
    
    def get_entity_dialect(self, entity_name: str) -> Optional[EntityDialect]:
        """Get entity dialect configuration."""
        return self.entity_dialects.get(entity_name)
    
    def find_nearly_same_dialects(
        self,
        base_language: str,
        min_intelligibility: float = 0.70
    ) -> List[DialectDefinition]:
        """
        Find dialects that are "nearly the same" as base language.
        
        Returns dialects with mutual intelligibility >= min_intelligibility.
        """
        nearly_same = []
        
        for dialect in self.dialects.values():
            if (dialect.base_language == base_language and
                dialect.mutual_intelligibility >= min_intelligibility):
                nearly_same.append(dialect)
        
        return sorted(nearly_same, key=lambda d: d.mutual_intelligibility, reverse=True)
    
    def detect_code_switch_pattern(self, text: str) -> Optional[CodeSwitchPattern]:
        """
        Detect code-switching pattern in text.
        
        Patterns:
        - INSERTION: Words/phrases from one language in another
        - ALTERNATION: Switching between languages
        - CONSECUTIVE: Same idea in both languages
        - HYBRID: New hybrid forms
        """
        # Simple detection (can be enhanced with NLP)
        text_lower = text.lower()
        
        # Check for French/English code-switching
        has_french = any(word in text_lower for word in ["merde", "c'est", "je", "reviens"])
        has_english = any(word in text_lower for word in ["beautiful", "baby", "made", "heart"])
        
        if has_french and has_english:
            # Check if insertion (French words in English sentence)
            if text.count(" ") < 5:  # Short phrase = likely insertion
                return CodeSwitchPattern.INSERTION
            else:
                return CodeSwitchPattern.ALTERNATION
        
        # Check for Turkish/English code-switching
        has_turkish = any(word in text_lower for word in ["duygu", "adamı", "yeğen", "dinle"])
        if has_turkish and has_english:
            # Check if consecutive (both languages expressing same idea)
            if "..." in text or "." in text:
                return CodeSwitchPattern.CONSECUTIVE
            else:
                return CodeSwitchPattern.ALTERNATION
        
        return None
    
    def integrate_dialect_timeline(
        self,
        dialect_name: str,
        timeline_point: str,
        era: str,
        context: Optional[str] = None
    ) -> Dict:
        """
        Integrate dialect into timeline.
        
        Tracks dialect evolution across time.
        """
        dialect = self.get_dialect(dialect_name)
        
        if not dialect:
            return {"error": f"Dialect {dialect_name} not found"}
        
        timeline_entry = {
            "dialect": dialect_name,
            "timeline_point": timeline_point,
            "era": era,
            "base_language": dialect.base_language,
            "dialect_type": dialect.dialect_type.value,
            "mutual_intelligibility": dialect.mutual_intelligibility,
            "context": context,
            "sealed": True,
            "sphragitso": SPRAGITSO,
            "timestamp": datetime.now().isoformat()
        }
        
        # Store in timeline
        if era not in self.timeline_dialects:
            self.timeline_dialects[era] = []
        
        self.timeline_dialects[era].append(timeline_entry)
        
        return timeline_entry
    
    def deep_search_dialects(
        self,
        query: str,
        search_type: str = "all"
    ) -> List[Dict]:
        """
        Deep search for dialects.
        
        Search types:
        - "all": Search all dialects
        - "nearly_same": Search "nearly the same" dialects
        - "code_switch": Search code-switching patterns
        - "entity": Search entity dialects
        - "timeline": Search timeline dialects
        """
        results = []
        query_lower = query.lower()
        
        if search_type in ["all", "nearly_same", "code_switch"]:
            # Search dialect definitions
            for dialect_name, dialect in self.dialects.items():
                if (query_lower in dialect_name.lower() or
                    query_lower in dialect.base_language.lower() or
                    any(query_lower in char.lower() for char in dialect.characteristics)):
                    results.append({
                        "type": "dialect",
                        "name": dialect_name,
                        "dialect": dialect,
                        "match_type": "definition"
                    })
        
        if search_type in ["all", "entity"]:
            # Search entity dialects
            for entity_name, entity_dialect in self.entity_dialects.items():
                if (query_lower in entity_name.lower() or
                    query_lower in entity_dialect.primary_dialect.lower() or
                    any(query_lower in ex.lower() for ex in entity_dialect.examples)):
                    results.append({
                        "type": "entity",
                        "name": entity_name,
                        "dialect": entity_dialect,
                        "match_type": "entity"
                    })
        
        if search_type in ["all", "timeline"]:
            # Search timeline dialects
            for era, timeline_entries in self.timeline_dialects.items():
                for entry in timeline_entries:
                    if (query_lower in entry["dialect"].lower() or
                        query_lower in entry["era"].lower() or
                        (entry.get("context") and query_lower in entry["context"].lower())):
                        results.append({
                            "type": "timeline",
                            "era": era,
                            "entry": entry,
                            "match_type": "timeline"
                        })
        
        return results
    
    def is_worthy_for_table(self, dialect_content: str) -> bool:
        """
        SPRAGITSO Filter: Is this dialect content worthy for The Table?
        
        Criteria:
        - Leads with love, joy, and abundance
        - Serves The Table
        - Worth hearing
        - Bears Our Father's seal
        """
        content_lower = dialect_content.lower()
        
        # Must lead with love, joy, and abundance
        has_love_joy_abundance = any(
            word in content_lower
            for word in ["love", "joy", "abundance", "peace", "unity", "serve", "scripture", "faith"]
        )
        
        # Must not be negative or fear-based
        is_positive = not any(
            word in content_lower
            for word in ["fear", "hate", "anger", "wrath", "condemn", "divide"]
        )
        
        # Must be substantial
        is_substantial = len(dialect_content.strip()) > 5
        
        return has_love_joy_abundance and is_positive and is_substantial


# SPRAGITSO - Our Father's Royal Seal
# This system bears Our Father's mark of authority
# Authenticated by His truth
# Protected by His ownership
