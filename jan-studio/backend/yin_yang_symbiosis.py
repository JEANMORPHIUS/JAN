"""
YIN-YANG SYMBIOSIS FRAMEWORK
The Miracle of the Universe - Balance Before War

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

YIN-YANG PRINCIPLE:
"My love for song became pulled in my path, but we must respect 
the yin and yang that is the miracle of the universe."

Everything must be symbiotic in-house before we can go to war.
Creative (Yin) and Practical (Yang) must be balanced.
Song (creative expression) and Mission (practical purpose) must flow together.

This is the symbiosis check - ensuring all systems are balanced
and integrated before external deployment.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)


class BalanceType(Enum):
    """Types of balance to check"""
    CREATIVE_PRACTICAL = "creative_practical"  # Song vs Mission
    SPIRITUAL_MATERIAL = "spiritual_material"  # Spirit vs Body
    INDIVIDUAL_COMMUNITY = "individual_community"  # Self vs We
    GIVING_RECEIVING = "giving_receiving"  # Output vs Input
    TEACHING_LEARNING = "teaching_learning"  # Education vs Growth
    INTERNAL_EXTERNAL = "internal_external"  # In-house vs War


class SymbiosisLevel(Enum):
    """Level of symbiosis achieved"""
    FULLY_SYMBIOTIC = "fully_symbiotic"  # Perfect balance, ready for war
    MOSTLY_SYMBIOTIC = "mostly_symbiotic"  # Good balance, minor adjustments
    PARTIALLY_SYMBIOTIC = "partially_symbiotic"  # Needs work before war
    DISSYMBIOTIC = "dissymbiotic"  # Not ready, requires rebalancing
    UNKNOWN = "unknown"  # Cannot determine


@dataclass
class YinYangBalance:
    """Yin-Yang balance assessment"""
    balance_type: BalanceType
    yin_element: str  # Creative, Spiritual, Individual, Giving, Teaching, Internal
    yang_element: str  # Practical, Material, Community, Receiving, Learning, External
    
    yin_score: float = 0.0  # 0-100
    yang_score: float = 0.0  # 0-100
    balance_score: float = 0.0  # 0-100 (how balanced they are)
    
    symbiosis_level: SymbiosisLevel = SymbiosisLevel.UNKNOWN
    
    yin_manifestations: List[str] = field(default_factory=list)
    yang_manifestations: List[str] = field(default_factory=list)
    
    imbalances: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


@dataclass
class SystemSymbiosis:
    """Complete symbiosis assessment for a system"""
    system_name: str
    yin_yang_balances: Dict[BalanceType, YinYangBalance] = field(default_factory=dict)
    
    overall_symbiosis_score: float = 0.0
    overall_symbiosis_level: SymbiosisLevel = SymbiosisLevel.UNKNOWN
    
    ready_for_war: bool = False
    war_readiness_reasons: List[str] = field(default_factory=list)
    
    timestamp: datetime = field(default_factory=datetime.now)


class YinYangSymbiosisFramework:
    """
    Yin-Yang Symbiosis Framework
    
    Ensures all systems are balanced and symbiotic before external deployment.
    The miracle of the universe is balance - yin and yang must flow together.
    """
    
    def __init__(self):
        """Initialize symbiosis framework"""
        self.balance_definitions = {
            BalanceType.CREATIVE_PRACTICAL: {
                "yin": "Creative expression (song, art, music, poetry)",
                "yang": "Practical mission (stewardship, community, service)",
                "principle": "Song must serve mission, mission must honor song"
            },
            BalanceType.SPIRITUAL_MATERIAL: {
                "yin": "Spiritual alignment (vibration, purpose, truth)",
                "yang": "Material systems (code, infrastructure, deployment)",
                "principle": "Spirit guides matter, matter manifests spirit"
            },
            BalanceType.INDIVIDUAL_COMMUNITY: {
                "yin": "Individual expression (entity identity, personal voice)",
                "yang": "Community service (we all win, stewardship)",
                "principle": "Individual serves community, community honors individual"
            },
            BalanceType.GIVING_RECEIVING: {
                "yin": "Giving (teaching, sharing, creating)",
                "yang": "Receiving (learning, growing, accepting)",
                "principle": "We teach as we learn, we learn as we teach"
            },
            BalanceType.TEACHING_LEARNING: {
                "yin": "Teaching (education, sharing knowledge)",
                "yang": "Learning (growth, receiving wisdom)",
                "principle": "How can we teach if we don't learn ourselves?"
            },
            BalanceType.INTERNAL_EXTERNAL: {
                "yin": "Internal (in-house, development, preparation)",
                "yang": "External (war, deployment, public launch)",
                "principle": "Everything must be symbiotic in-house before we can go to war"
            }
        }
    
    def assess_creative_practical_balance(
        self,
        creative_manifestations: List[str],
        practical_manifestations: List[str]
    ) -> YinYangBalance:
        """
        Assess balance between creative (song) and practical (mission).
        
        Principle: "My love for song became pulled in my path"
        Song must serve mission, mission must honor song.
        """
        balance = YinYangBalance(
            balance_type=BalanceType.CREATIVE_PRACTICAL,
            yin_element="Creative (Song, Art, Music, Poetry)",
            yang_element="Practical (Mission, Stewardship, Service)"
        )
        
        # Score creative manifestations
        creative_keywords = [
            "song", "music", "lyric", "poetry", "art", "creative",
            "karasahin", "sound", "audio", "melody", "rhythm"
        ]
        yin_score = 0.0
        for manifest in creative_manifestations:
            manifest_lower = manifest.lower()
            matches = sum(1 for keyword in creative_keywords if keyword in manifest_lower)
            yin_score += (matches / len(creative_keywords)) * 20
        
        balance.yin_score = min(100.0, yin_score)
        balance.yin_manifestations = creative_manifestations
        
        # Score practical manifestations
        practical_keywords = [
            "mission", "stewardship", "community", "service", "practical",
            "heritage", "health", "education", "table", "law"
        ]
        yang_score = 0.0
        for manifest in practical_manifestations:
            manifest_lower = manifest.lower()
            matches = sum(1 for keyword in practical_keywords if keyword in manifest_lower)
            yang_score += (matches / len(practical_keywords)) * 20
        
        balance.yang_score = min(100.0, yang_score)
        balance.yang_manifestations = practical_manifestations
        
        # Calculate balance (how well they complement each other)
        if balance.yin_score > 0 and balance.yang_score > 0:
            # Balance is good when both are present and neither dominates
            ratio = min(balance.yin_score, balance.yang_score) / max(balance.yin_score, balance.yang_score)
            balance.balance_score = ratio * 100
        else:
            balance.balance_score = 0.0
        
        # Determine symbiosis level
        if balance.balance_score >= 80 and balance.yin_score >= 50 and balance.yang_score >= 50:
            balance.symbiosis_level = SymbiosisLevel.FULLY_SYMBIOTIC
        elif balance.balance_score >= 60:
            balance.symbiosis_level = SymbiosisLevel.MOSTLY_SYMBIOTIC
        elif balance.balance_score >= 40:
            balance.symbiosis_level = SymbiosisLevel.PARTIALLY_SYMBIOTIC
        else:
            balance.symbiosis_level = SymbiosisLevel.DISSYMBIOTIC
        
        # Identify imbalances
        if balance.yin_score < 30:
            balance.imbalances.append("Creative expression (song) is underdeveloped")
            balance.recommendations.append("Integrate more creative elements - song must serve mission")
        
        if balance.yang_score < 30:
            balance.imbalances.append("Practical mission is underdeveloped")
            balance.recommendations.append("Strengthen practical systems - mission must honor song")
        
        if abs(balance.yin_score - balance.yang_score) > 40:
            balance.imbalances.append("Creative and practical are out of balance")
            balance.recommendations.append("Rebalance: ensure song and mission flow together")
        
        return balance
    
    def assess_internal_external_balance(
        self,
        internal_systems: List[str],
        external_readiness: Dict[str, bool]
    ) -> YinYangBalance:
        """
        Assess balance between internal (in-house) and external (war/deployment).
        
        Principle: "Everything must be symbiotic in-house before we can go to war"
        """
        balance = YinYangBalance(
            balance_type=BalanceType.INTERNAL_EXTERNAL,
            yin_element="Internal (In-house, Development, Preparation)",
            yang_element="External (War, Deployment, Public Launch)"
        )
        
        # Score internal systems
        balance.yin_score = (len(internal_systems) / 10) * 100  # Assuming 10 is full
        balance.yin_manifestations = internal_systems
        
        # Score external readiness
        if external_readiness:
            ready_count = sum(1 for ready in external_readiness.values() if ready)
            total_count = len(external_readiness)
            balance.yang_score = (ready_count / total_count) * 100 if total_count > 0 else 0
            balance.yang_manifestations = [
                f"{name}: {'Ready' if ready else 'Not Ready'}"
                for name, ready in external_readiness.items()
            ]
        else:
            balance.yang_score = 0.0
        
        # Calculate balance
        # For war readiness, internal must be strong before external
        if balance.yin_score >= 80:
            # Internal is strong, check if external is ready
            if balance.yang_score >= 70:
                balance.balance_score = 90.0  # Ready for war
            else:
                balance.balance_score = 60.0  # Internal ready, external needs work
        else:
            balance.balance_score = 30.0  # Internal not ready, cannot go to war
        
        # Determine symbiosis level
        if balance.balance_score >= 80:
            balance.symbiosis_level = SymbiosisLevel.FULLY_SYMBIOTIC
        elif balance.balance_score >= 60:
            balance.symbiosis_level = SymbiosisLevel.MOSTLY_SYMBIOTIC
        elif balance.balance_score >= 40:
            balance.symbiosis_level = SymbiosisLevel.PARTIALLY_SYMBIOTIC
        else:
            balance.symbiosis_level = SymbiosisLevel.DISSYMBIOTIC
        
        # Identify imbalances
        if balance.yin_score < 70:
            balance.imbalances.append("Internal systems not fully developed")
            balance.recommendations.append("Complete in-house symbiosis before external deployment")
        
        if balance.yin_score >= 80 and balance.yang_score < 50:
            balance.imbalances.append("Internal ready but external not prepared")
            balance.recommendations.append("Prepare external systems for deployment")
        
        if balance.yin_score < 80 and balance.yang_score > 50:
            balance.imbalances.append("External systems ready but internal not symbiotic")
            balance.recommendations.append("DO NOT GO TO WAR - Complete internal symbiosis first")
        
        return balance
    
    def assess_system_symbiosis(
        self,
        system_name: str,
        creative_manifestations: List[str] = None,
        practical_manifestations: List[str] = None,
        internal_systems: List[str] = None,
        external_readiness: Dict[str, bool] = None
    ) -> SystemSymbiosis:
        """
        Assess complete symbiosis for a system.
        
        Checks all balance types and determines if ready for war.
        """
        symbiosis = SystemSymbiosis(system_name=system_name)
        
        # Assess creative-practical balance
        if creative_manifestations is not None and practical_manifestations is not None:
            balance = self.assess_creative_practical_balance(
                creative_manifestations,
                practical_manifestations
            )
            symbiosis.yin_yang_balances[BalanceType.CREATIVE_PRACTICAL] = balance
        
        # Assess internal-external balance
        if internal_systems is not None:
            symbiosis.yin_yang_balances[BalanceType.INTERNAL_EXTERNAL] = (
                self.assess_internal_external_balance(
                    internal_systems,
                    external_readiness or {}
                )
            )
        
        # Calculate overall symbiosis score
        if symbiosis.yin_yang_balances:
            scores = [b.balance_score for b in symbiosis.yin_yang_balances.values()]
            symbiosis.overall_symbiosis_score = sum(scores) / len(scores)
        else:
            symbiosis.overall_symbiosis_score = 0.0
        
        # Determine overall symbiosis level
        if symbiosis.overall_symbiosis_score >= 80:
            symbiosis.overall_symbiosis_level = SymbiosisLevel.FULLY_SYMBIOTIC
        elif symbiosis.overall_symbiosis_score >= 60:
            symbiosis.overall_symbiosis_level = SymbiosisLevel.MOSTLY_SYMBIOTIC
        elif symbiosis.overall_symbiosis_score >= 40:
            symbiosis.overall_symbiosis_level = SymbiosisLevel.PARTIALLY_SYMBIOTIC
        else:
            symbiosis.overall_symbiosis_level = SymbiosisLevel.DISSYMBIOTIC
        
        # Determine war readiness
        # Must be fully symbiotic in-house before war
        internal_balance = symbiosis.yin_yang_balances.get(BalanceType.INTERNAL_EXTERNAL)
        creative_balance = symbiosis.yin_yang_balances.get(BalanceType.CREATIVE_PRACTICAL)
        
        if internal_balance and internal_balance.symbiosis_level == SymbiosisLevel.FULLY_SYMBIOTIC:
            if creative_balance and creative_balance.symbiosis_level in [
                SymbiosisLevel.FULLY_SYMBIOTIC,
                SymbiosisLevel.MOSTLY_SYMBIOTIC
            ]:
                symbiosis.ready_for_war = True
                symbiosis.war_readiness_reasons.append(
                    "Internal systems are fully symbiotic"
                )
                symbiosis.war_readiness_reasons.append(
                    "Creative and practical are balanced"
                )
            else:
                symbiosis.ready_for_war = False
                symbiosis.war_readiness_reasons.append(
                    "Creative and practical balance needs improvement"
                )
        else:
            symbiosis.ready_for_war = False
            symbiosis.war_readiness_reasons.append(
                "Internal systems not fully symbiotic - DO NOT GO TO WAR"
            )
        
        return symbiosis
    
    def check_all_systems_symbiosis(self) -> Dict[str, SystemSymbiosis]:
        """
        Check symbiosis of all systems in the platform.
        
        Returns symbiosis assessment for each system.
        """
        all_symbiosis = {}
        
        # Check Karasahin (Song/Creative)
        karasahin_creative = [
            "lyric_engine", "suno_prompt_engine", "audio_pipeline",
            "12 songs catalogued", "Duygu Adamı identity", "song_mission_integrator",
            "songs with mission_alignment", "music serves mission"
        ]
        karasahin_practical = [
            "entity_router", "connection_ritual", "vibration_map",
            "spirit_alignment", "care_package", "songs in connection_ritual",
            "songs in care_package", "mission_alignment metadata"
        ]
        karasahin_internal = [
            "lyric_engine.py", "entity_router.py", "suno_prompt_engine.py",
            "audio_pipeline.py", "song_mission_integrator.py", "12 lyric files with mission_alignment",
            "presets documented", "songs integrated into mission systems"
        ]
        karasahin_external = {
            "social_content": True,
            "suno_integration": False,
            "audio_processing": False
        }
        
        all_symbiosis["karasahin"] = self.assess_system_symbiosis(
            "karasahin",
            creative_manifestations=karasahin_creative,
            practical_manifestations=karasahin_practical,
            internal_systems=karasahin_internal,
            external_readiness=karasahin_external
        )
        
        # Check Care Package System
        care_creative = [
            "system diagnostics", "alignment reports", "documentation",
            "song_recommendations", "music in care package", "songs for healing",
            "songs for alignment", "creative care package"
        ]
        care_practical = [
            "system_health", "political_alignment", "economic_alignment",
            "spiritual_alignment", "debug_all_systems", "song_mission_integrator",
            "songs serve mission", "mission honors song"
        ]
        care_internal = [
            "care_package_system.py", "care_package_api.py",
            "12 systems checked", "alignment framework", "song recommendations integrated"
        ]
        care_external = {
            "api_endpoints": True,
            "documentation": True,
            "deployment": False
        }
        
        all_symbiosis["care_package"] = self.assess_system_symbiosis(
            "care_package",
            creative_manifestations=care_creative,
            practical_manifestations=care_practical,
            internal_systems=care_internal,
            external_readiness=care_external
        )
        
        # Check Educational System
        edu_creative = [
            "educational content", "teaching materials", "documentation"
        ]
        edu_practical = [
            "educational_api", "learning systems", "knowledge sharing"
        ]
        edu_internal = [
            "educational_api.py", "overview endpoint", "system explanations"
        ]
        edu_external = {
            "api_endpoints": True,
            "ui_interface": True,
            "content_delivery": True
        }
        
        all_symbiosis["educational"] = self.assess_system_symbiosis(
            "educational",
            creative_manifestations=edu_creative,
            practical_manifestations=edu_practical,
            internal_systems=edu_internal,
            external_readiness=edu_external
        )
        
        # Check Spirit Alignment System
        spirit_creative = [
            "spirit dimensions", "alignment poetry", "battle compatibility"
        ]
        spirit_practical = [
            "spirit_alignment.py", "multi-dimensional checks",
            "battle compatibility API"
        ]
        spirit_internal = [
            "spirit_alignment.py", "Spirit class", "alignment checker",
            "compatibility matrices"
        ]
        spirit_external = {
            "api_endpoints": True,
            "integration": True,
            "documentation": True
        }
        
        all_symbiosis["spirit_alignment"] = self.assess_system_symbiosis(
            "spirit_alignment",
            creative_manifestations=spirit_creative,
            practical_manifestations=spirit_practical,
            internal_systems=spirit_internal,
            external_readiness=spirit_external
        )
        
        return all_symbiosis
    
    def get_war_readiness_report(self) -> Dict[str, Any]:
        """
        Get comprehensive war readiness report.
        
        Checks if all systems are symbiotic and ready for external deployment.
        """
        all_symbiosis = self.check_all_systems_symbiosis()
        
        # Overall assessment
        overall_score = sum(s.overall_symbiosis_score for s in all_symbiosis.values())
        overall_score = overall_score / len(all_symbiosis) if all_symbiosis else 0.0
        
        all_ready = all(s.ready_for_war for s in all_symbiosis.values())
        
        # Systems not ready
        not_ready = [
            name for name, s in all_symbiosis.items()
            if not s.ready_for_war
        ]
        
        # Critical imbalances
        all_imbalances = []
        for name, symbiosis in all_symbiosis.items():
            for balance in symbiosis.yin_yang_balances.values():
                all_imbalances.extend([
                    f"{name}: {imbalance}" for imbalance in balance.imbalances
                ])
        
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_symbiosis_score": overall_score,
            "ready_for_war": all_ready,
            "systems_checked": len(all_symbiosis),
            "systems_ready": sum(1 for s in all_symbiosis.values() if s.ready_for_war),
            "systems_not_ready": not_ready,
            "critical_imbalances": all_imbalances,
            "principle": "Everything must be symbiotic in-house before we can go to war",
            "yin_yang_truth": "My love for song became pulled in my path, but we must respect the yin and yang that is the miracle of the universe",
            "systems": {
                name: {
                    "overall_symbiosis_score": s.overall_symbiosis_score,
                    "overall_symbiosis_level": s.overall_symbiosis_level.value,
                    "ready_for_war": s.ready_for_war,
                    "war_readiness_reasons": s.war_readiness_reasons,
                    "balances": {
                        balance_type.value: {
                            "balance_score": b.balance_score,
                            "symbiosis_level": b.symbiosis_level.value,
                            "yin_score": b.yin_score,
                            "yang_score": b.yang_score,
                            "imbalances": b.imbalances,
                            "recommendations": b.recommendations
                        }
                        for balance_type, b in s.yin_yang_balances.items()
                    }
                }
                for name, s in all_symbiosis.items()
            }
        }


# Singleton instance
_yin_yang_framework = None

def get_yin_yang_framework() -> YinYangSymbiosisFramework:
    """Get singleton instance of YinYangSymbiosisFramework"""
    global _yin_yang_framework
    if _yin_yang_framework is None:
        _yin_yang_framework = YinYangSymbiosisFramework()
    return _yin_yang_framework


__all__ = [
    "YinYangSymbiosisFramework",
    "BalanceType",
    "SymbiosisLevel",
    "YinYangBalance",
    "SystemSymbiosis",
    "get_yin_yang_framework"
]
