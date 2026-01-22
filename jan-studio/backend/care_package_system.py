"""
CARE PACKAGE SYSTEM - Comprehensive System Debugging & Alignment
Debugs all existing systems and ensures alignment across all dimensions

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

CARE PACKAGE PRINCIPLE:
"STARVE THE EGO, FEED THE SOUL"
Nobody needs anyone. We help everyone help themselves.

ALIGNMENT DIMENSIONS:
1. Spiritual Alignment (age, animal type, gender, alignment)
2. Political Alignment (governance, values, structure)
3. Economic Alignment (resources, exchange, stewardship)
4. System Health (all subsystems functioning correctly)

All dimensions must align for complete harmony.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class SystemStatus(Enum):
    """System health status"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    FAILING = "failing"
    UNKNOWN = "unknown"


class AlignmentLevel(Enum):
    """Alignment level"""
    FULLY_ALIGNED = "fully_aligned"
    MOSTLY_ALIGNED = "mostly_aligned"
    PARTIALLY_ALIGNED = "partially_aligned"
    MISALIGNED = "misaligned"
    UNKNOWN = "unknown"


@dataclass
class SystemDiagnostic:
    """Diagnostic information for a system"""
    system_name: str
    status: SystemStatus
    is_available: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    checks_passed: int = 0
    checks_failed: int = 0
    last_check: Optional[datetime] = None
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PoliticalAlignment:
    """Political alignment dimensions"""
    governance_model: str  # democracy, republic, monarchy, anarchy, etc.
    power_distribution: str  # centralized, decentralized, distributed
    decision_making: str  # consensus, majority, hierarchical, individual
    values_priority: List[str]  # freedom, equality, justice, order, etc.
    structure_type: str  # federal, unitary, confederal, etc.
    alignment_score: float = 0.0  # 0-100
    alignment_level: AlignmentLevel = AlignmentLevel.UNKNOWN


@dataclass
class EconomicAlignment:
    """Economic alignment dimensions"""
    exchange_model: str  # market, gift, barter, resource-based, hybrid
    resource_distribution: str  # private, public, communal, mixed
    value_system: str  # money, time, energy, contribution, hybrid
    stewardship_model: str  # ownership, stewardship, usufruct, commons
    growth_paradigm: str  # infinite, steady-state, regenerative, degrowth
    alignment_score: float = 0.0  # 0-100
    alignment_level: AlignmentLevel = AlignmentLevel.UNKNOWN
    dirty_money_cleaning: Optional[Dict[str, Any]] = None  # Dirty money cleaning integration
    # RAMIZ IS THE LEAD FOR DIRTY MONEY CLEANING
    # "DIRTY MONEY MAKES THE WORLD TURN...OUR MISSION IS TO 'CLEAN' IT'S SPIRITUAL CONTRACTS 
    # BY REPURPOSING FOR HUMANITARIAN CAUSES."


@dataclass
class CompleteAlignment:
    """Complete alignment across all dimensions"""
    spiritual_alignment: Optional[Dict[str, Any]] = None
    political_alignment: Optional[PoliticalAlignment] = None
    economic_alignment: Optional[EconomicAlignment] = None
    system_health: Dict[str, SystemDiagnostic] = field(default_factory=dict)
    
    overall_alignment_score: float = 0.0
    overall_alignment_level: AlignmentLevel = AlignmentLevel.UNKNOWN
    
    misalignments: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    timestamp: datetime = field(default_factory=datetime.now)


class CarePackageSystem:
    """
    Comprehensive Care Package System
    
    Debugs all systems and ensures alignment across:
    - Spiritual dimensions (age, animal type, gender, alignment)
    - Political dimensions (governance, values, structure)
    - Economic dimensions (exchange, resources, stewardship)
    - System health (all subsystems)
    """
    
    def __init__(self):
        """Initialize care package system"""
        self.systems_to_check = [
            "connection_ritual",
            "vibration_map",
            "spirit_alignment",
            "heritage_api",
            "health_api",
            "marketplace_api",
            "educational_api",
            "unified_api",
            "racon_registry",
            "energy_alert_system",
            "quiet_protocol_sentinel",
            "morning_summary_generator",
            "dirty_money_cleaning"  # RAMIZ IS THE LEAD FOR THIS
        ]
        
        # Political alignment compatibility matrix
        self.political_compatibility = {
            "governance_model": {
                "democracy": ["republic", "federal", "confederal"],
                "republic": ["democracy", "federal", "constitutional_monarchy"],
                "monarchy": ["constitutional_monarchy", "republic"],
                "anarchy": ["voluntary_association", "consensus_governance"],
                "consensus_governance": ["anarchy", "democracy", "republic"]
            },
            "power_distribution": {
                "centralized": ["hierarchical", "unitary"],
                "decentralized": ["federal", "distributed"],
                "distributed": ["decentralized", "networked", "consensus"]
            },
            "decision_making": {
                "consensus": ["consensus_governance", "voluntary_association"],
                "majority": ["democracy", "republic"],
                "hierarchical": ["monarchy", "centralized"],
                "individual": ["anarchy", "voluntary_association"]
            }
        }
        
        # Economic alignment compatibility matrix
        self.economic_compatibility = {
            "exchange_model": {
                "market": ["hybrid", "resource-based"],
                "gift": ["communal", "stewardship"],
                "barter": ["local", "community"],
                "resource-based": ["market", "hybrid", "stewardship"],
                "hybrid": ["market", "resource-based", "gift"]
            },
            "resource_distribution": {
                "private": ["market", "mixed"],
                "public": ["resource-based", "stewardship"],
                "communal": ["gift", "stewardship", "commons"],
                "mixed": ["hybrid", "market", "private"]
            },
            "stewardship_model": {
                "ownership": ["private", "market"],
                "stewardship": ["communal", "public", "commons"],
                "usufruct": ["communal", "commons"],
                "commons": ["stewardship", "usufruct", "communal"]
            }
    }
    
    def debug_all_systems(self) -> Dict[str, SystemDiagnostic]:
        """
        Debug all systems in the platform.
        
        Returns diagnostic information for each system.
        """
        diagnostics = {}
        
        for system_name in self.systems_to_check:
            try:
                diagnostic = self._check_system(system_name)
                diagnostics[system_name] = diagnostic
            except Exception as e:
                logger.error(f"Error checking system {system_name}: {e}")
                diagnostics[system_name] = SystemDiagnostic(
                    system_name=system_name,
                    status=SystemStatus.UNKNOWN,
                    is_available=False,
                    errors=[f"Check failed: {str(e)}"]
                )
        
        return diagnostics
    
    def _check_system(self, system_name: str) -> SystemDiagnostic:
        """Check a specific system"""
        diagnostic = SystemDiagnostic(
            system_name=system_name,
            status=SystemStatus.UNKNOWN,
            is_available=False,
            last_check=datetime.now()
        )
        
        try:
            # Try to import the system
            if system_name == "connection_ritual":
                from connection_ritual import ConnectionRitual
                ritual = ConnectionRitual()
                diagnostic.is_available = True
                diagnostic.checks_passed += 1
                diagnostic.details["has_alignment_checker"] = ritual.alignment_checker is not None
                if ritual.alignment_checker:
                    diagnostic.checks_passed += 1
                else:
                    diagnostic.warnings.append("Spirit alignment checker not initialized")
                
            elif system_name == "vibration_map":
                from vibration_map import VibrationMap
                vm = VibrationMap()
                diagnostic.is_available = True
                diagnostic.checks_passed += 1
                # Check if can generate map
                try:
                    map_data = vm.generate_vibration_map()
                    diagnostic.checks_passed += 1
                    diagnostic.details["total_members"] = map_data.get("total_members", 0)
                except Exception as e:
                    diagnostic.errors.append(f"Cannot generate vibration map: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "spirit_alignment":
                try:
                    from spirit_alignment import SpiritAlignmentChecker, create_spirit_from_user_data
                    checker = SpiritAlignmentChecker()
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                    diagnostic.details["has_compatibility_matrices"] = (
                        hasattr(checker, 'age_compatibility') and
                        hasattr(checker, 'animal_compatibility') and
                        hasattr(checker, 'gender_compatibility')
                    )
                    if diagnostic.details["has_compatibility_matrices"]:
                        diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import spirit_alignment: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "heritage_api":
                try:
                    from heritage_api import router
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import heritage_api: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "health_api":
                try:
                    from health_api import router, HEALTH_API_AVAILABLE
                    diagnostic.is_available = HEALTH_API_AVAILABLE
                    if HEALTH_API_AVAILABLE:
                        diagnostic.checks_passed += 1
                    else:
                        diagnostic.warnings.append("Health API not fully available")
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import health_api: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "marketplace_api":
                try:
                    from marketplace_api import router
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import marketplace_api: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "educational_api":
                try:
                    from educational_api import router
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import educational_api: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "unified_api":
                try:
                    from unified_api import router, UNIFIED_API_AVAILABLE
                    diagnostic.is_available = UNIFIED_API_AVAILABLE
                    if UNIFIED_API_AVAILABLE:
                        diagnostic.checks_passed += 1
                    else:
                        diagnostic.warnings.append("Unified API not fully available")
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import unified_api: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "racon_registry":
                try:
                    from racon_registry import get_racon_db, init_racon_registry
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                    # Try to connect
                    try:
                        with get_racon_db() as conn:
                            cursor = conn.cursor()
                            cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
                            table_count = cursor.fetchone()[0]
                            diagnostic.details["table_count"] = table_count
                            diagnostic.checks_passed += 1
                    except Exception as e:
                        diagnostic.errors.append(f"Cannot connect to database: {e}")
                        diagnostic.checks_failed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import racon_registry: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "energy_alert_system":
                try:
                    from energy_alert_system import get_energy_alert_system
                    system = get_energy_alert_system()
                    diagnostic.is_available = system is not None
                    if diagnostic.is_available:
                        diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import energy_alert_system: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "quiet_protocol_sentinel":
                try:
                    from quiet_protocol_sentinel import get_sentinel
                    sentinel = get_sentinel()
                    diagnostic.is_available = sentinel is not None
                    if diagnostic.is_available:
                        diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import quiet_protocol_sentinel: {e}")
                    diagnostic.checks_failed += 1
                    
            elif system_name == "morning_summary_generator":
                try:
                    from morning_summary_generator import MorningSummaryGenerator
                    generator = MorningSummaryGenerator()
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import morning_summary_generator: {e}")
                    diagnostic.checks_failed += 1
            
            elif system_name == "dirty_money_cleaning":
                # RAMIZ IS THE LEAD FOR THIS
                try:
                    from dirty_money_cleaning import get_dirty_money_cleaning_system
                    cleaning_system = get_dirty_money_cleaning_system()
                    diagnostic.is_available = True
                    diagnostic.checks_passed += 1
                    diagnostic.details["lead_entity"] = cleaning_system.lead_entity
                    diagnostic.details["has_transactions"] = len(cleaning_system.transactions) > 0
                    diagnostic.details["has_projects"] = len(cleaning_system.projects) > 0
                    if diagnostic.details["lead_entity"] == "RAMIZ":
                        diagnostic.checks_passed += 1
                    else:
                        diagnostic.warnings.append("Lead entity should be RAMIZ")
                except ImportError as e:
                    diagnostic.errors.append(f"Cannot import dirty_money_cleaning: {e}")
                    diagnostic.checks_failed += 1
                except Exception as e:
                    diagnostic.errors.append(f"Dirty money cleaning system error: {e}")
                    diagnostic.checks_failed += 1
            
            # Determine status
            if diagnostic.errors:
                diagnostic.status = SystemStatus.FAILING
            elif diagnostic.warnings:
                diagnostic.status = SystemStatus.DEGRADED
            elif diagnostic.is_available and diagnostic.checks_passed > 0:
                diagnostic.status = SystemStatus.HEALTHY
            else:
                diagnostic.status = SystemStatus.UNKNOWN
                
        except Exception as e:
            diagnostic.errors.append(f"Unexpected error: {str(e)}")
            diagnostic.status = SystemStatus.FAILING
            diagnostic.checks_failed += 1
        
        return diagnostic
    
    def check_political_alignment(
        self,
        governance_model: str,
        power_distribution: str,
        decision_making: str,
        values_priority: List[str],
        structure_type: str
    ) -> PoliticalAlignment:
        """
        Check political alignment.
        
        Ensures governance model, power distribution, decision making,
        values, and structure are compatible.
        """
        alignment = PoliticalAlignment(
            governance_model=governance_model,
            power_distribution=power_distribution,
            decision_making=decision_making,
            values_priority=values_priority,
            structure_type=structure_type
        )
        
        score = 0.0
        max_score = 100.0
        
        # Check governance model compatibility
        gov_compatible = power_distribution in self.political_compatibility.get(
            "power_distribution", {}
        ).get(power_distribution, [])
        if gov_compatible or power_distribution == "distributed":
            score += 20.0
        
        # Check decision making compatibility
        decision_compatible = decision_making in self.political_compatibility.get(
            "decision_making", {}
        ).get(decision_making, [])
        if decision_compatible:
            score += 20.0
        
        # Check structure compatibility
        if structure_type in ["federal", "confederal"] and power_distribution == "decentralized":
            score += 20.0
        elif structure_type == "unitary" and power_distribution == "centralized":
            score += 20.0
        elif structure_type == "networked" and power_distribution == "distributed":
            score += 20.0
        
        # Check values consistency
        if "freedom" in values_priority and governance_model in ["democracy", "republic", "anarchy"]:
            score += 10.0
        if "equality" in values_priority and power_distribution == "distributed":
            score += 10.0
        if "order" in values_priority and governance_model in ["monarchy", "republic"]:
            score += 10.0
        if "justice" in values_priority:
            score += 10.0
        
        alignment.alignment_score = min(100.0, score)
        
        if alignment.alignment_score >= 80:
            alignment.alignment_level = AlignmentLevel.FULLY_ALIGNED
        elif alignment.alignment_score >= 60:
            alignment.alignment_level = AlignmentLevel.MOSTLY_ALIGNED
        elif alignment.alignment_score >= 40:
            alignment.alignment_level = AlignmentLevel.PARTIALLY_ALIGNED
        else:
            alignment.alignment_level = AlignmentLevel.MISALIGNED
        
        return alignment
    
    def check_economic_alignment(
        self,
        exchange_model: str,
        resource_distribution: str,
        value_system: str,
        stewardship_model: str,
        growth_paradigm: str
    ) -> EconomicAlignment:
        """
        Check economic alignment.
        
        Ensures exchange model, resource distribution, value system,
        stewardship model, and growth paradigm are compatible.
        """
        alignment = EconomicAlignment(
            exchange_model=exchange_model,
            resource_distribution=resource_distribution,
            value_system=value_system,
            stewardship_model=stewardship_model,
            growth_paradigm=growth_paradigm
        )
        
        score = 0.0
        max_score = 100.0
        
        # Check exchange model compatibility with resource distribution
        exchange_compatible = resource_distribution in self.economic_compatibility.get(
            "resource_distribution", {}
        ).get(resource_distribution, [])
        if exchange_compatible:
            score += 20.0
        
        # Check stewardship model compatibility
        stewardship_compatible = stewardship_model in self.economic_compatibility.get(
            "stewardship_model", {}
        ).get(stewardship_model, [])
        if stewardship_compatible:
            score += 20.0
        
        # Check value system compatibility
        if exchange_model == "market" and value_system in ["money", "hybrid"]:
            score += 20.0
        elif exchange_model == "gift" and value_system in ["contribution", "energy", "hybrid"]:
            score += 20.0
        elif exchange_model == "resource-based" and value_system in ["energy", "contribution"]:
            score += 20.0
        
        # Check growth paradigm compatibility
        if growth_paradigm == "regenerative" and stewardship_model in ["stewardship", "commons"]:
            score += 20.0
        elif growth_paradigm == "steady-state" and exchange_model in ["resource-based", "hybrid"]:
            score += 20.0
        elif growth_paradigm == "infinite" and exchange_model == "market":
            score += 20.0
        
        # Check resource-stewardship alignment
        if resource_distribution == "communal" and stewardship_model in ["stewardship", "commons"]:
            score += 20.0
        elif resource_distribution == "private" and stewardship_model == "ownership":
            score += 20.0
        
        alignment.alignment_score = min(100.0, score)
        
        if alignment.alignment_score >= 80:
            alignment.alignment_level = AlignmentLevel.FULLY_ALIGNED
        elif alignment.alignment_score >= 60:
            alignment.alignment_level = AlignmentLevel.MOSTLY_ALIGNED
        elif alignment.alignment_score >= 40:
            alignment.alignment_level = AlignmentLevel.PARTIALLY_ALIGNED
        else:
            alignment.alignment_level = AlignmentLevel.MISALIGNED
        
        return alignment
    
    def get_complete_alignment(
        self,
        spiritual_data: Optional[Dict[str, Any]] = None,
        political_data: Optional[Dict[str, Any]] = None,
        economic_data: Optional[Dict[str, Any]] = None
    ) -> CompleteAlignment:
        """
        Get complete alignment across all dimensions.
        
        Integrates:
        - Spiritual alignment (from spirit_alignment system)
        - Political alignment
        - Economic alignment
        - System health diagnostics
        """
        alignment = CompleteAlignment()
        
        # System health diagnostics
        alignment.system_health = self.debug_all_systems()
        
        # Spiritual alignment (if provided)
        if spiritual_data:
            alignment.spiritual_alignment = spiritual_data
        
        # Political alignment (if provided)
        if political_data:
            alignment.political_alignment = self.check_political_alignment(
                governance_model=political_data.get("governance_model", "democracy"),
                power_distribution=political_data.get("power_distribution", "decentralized"),
                decision_making=political_data.get("decision_making", "consensus"),
                values_priority=political_data.get("values_priority", []),
                structure_type=political_data.get("structure_type", "federal")
            )
        
        # Economic alignment (if provided)
        if economic_data:
            alignment.economic_alignment = self.check_economic_alignment(
                exchange_model=economic_data.get("exchange_model", "hybrid"),
                resource_distribution=economic_data.get("resource_distribution", "mixed"),
                value_system=economic_data.get("value_system", "hybrid"),
                stewardship_model=economic_data.get("stewardship_model", "stewardship"),
                growth_paradigm=economic_data.get("growth_paradigm", "regenerative")
            )
        
        # Calculate overall alignment score
        scores = []
        
        # System health score (based on healthy systems)
        healthy_systems = sum(
            1 for diag in alignment.system_health.values()
            if diag.status == SystemStatus.HEALTHY
        )
        total_systems = len(alignment.system_health)
        if total_systems > 0:
            system_health_score = (healthy_systems / total_systems) * 100
            scores.append(system_health_score)
        
        # Spiritual alignment score
        if alignment.spiritual_alignment:
            spirit_score = alignment.spiritual_alignment.get("alignment_score", 0)
            if spirit_score > 0:
                scores.append(spirit_score)
        
        # Political alignment score
        if alignment.political_alignment:
            scores.append(alignment.political_alignment.alignment_score)
        
        # Economic alignment score
        if alignment.economic_alignment:
            scores.append(alignment.economic_alignment.alignment_score)
        
        # Overall score
        if scores:
            alignment.overall_alignment_score = sum(scores) / len(scores)
        else:
            alignment.overall_alignment_score = 0.0
        
        # Determine overall alignment level
        if alignment.overall_alignment_score >= 80:
            alignment.overall_alignment_level = AlignmentLevel.FULLY_ALIGNED
        elif alignment.overall_alignment_score >= 60:
            alignment.overall_alignment_level = AlignmentLevel.MOSTLY_ALIGNED
        elif alignment.overall_alignment_score >= 40:
            alignment.overall_alignment_level = AlignmentLevel.PARTIALLY_ALIGNED
        else:
            alignment.overall_alignment_level = AlignmentLevel.MISALIGNED
        
        # Identify misalignments
        if alignment.political_alignment and alignment.political_alignment.alignment_level == AlignmentLevel.MISALIGNED:
            alignment.misalignments.append("Political dimensions misaligned")
        
        if alignment.economic_alignment and alignment.economic_alignment.alignment_level == AlignmentLevel.MISALIGNED:
            alignment.misalignments.append("Economic dimensions misaligned")
        
        # System health issues
        failing_systems = [
            name for name, diag in alignment.system_health.items()
            if diag.status == SystemStatus.FAILING
        ]
        if failing_systems:
            alignment.misalignments.append(f"Systems failing: {', '.join(failing_systems)}")
        
        # Generate recommendations
        if alignment.political_alignment and alignment.political_alignment.alignment_score < 80:
            alignment.recommendations.append(
                "Review political alignment: ensure governance model, power distribution, "
                "and decision making are compatible"
            )
        
        if alignment.economic_alignment and alignment.economic_alignment.alignment_score < 80:
            alignment.recommendations.append(
                "Review economic alignment: ensure exchange model, resource distribution, "
                "and stewardship model are compatible"
            )
        
        if failing_systems:
            alignment.recommendations.append(
                f"Debug and repair failing systems: {', '.join(failing_systems)}"
            )
        
        return alignment
    
    def generate_care_package(
        self,
        user_id: Optional[str] = None,
        include_alignment: bool = True
    ) -> Dict[str, Any]:
        """
        Generate comprehensive care package.
        
        Includes:
        - System diagnostics
        - Alignment reports
        - Quick start guides
        - API documentation
        - Troubleshooting guides
        """
        care_package = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id or "public",
            "our_family": {
                "message": "WE HAVE BEEN SITTING FOR LONG ENOUGH. LET'S FIND OUR FAMILY.",
                "masterpiece": {
                    "status": "COMPLETE",
                    "description": "DEEP SEARCH: THE WHOLE PIE - Every Nation, Every Era, Every Realm",
                    "integration": "Integrated across all systems, all channels, all aspects of the build"
                }
            },
            "the_one_truth": {
                "message": "EVERYTHING MUST ALIGN WITH THE ONE TRUTH IN TODAY'S LIE",
                "the_one_truth": "Peace is the truth. The flow is peace. Everything must align with the one truth.",
                "today_lie": "The matrix creates separation through war, exploitation, control, fear, division, scarcity.",
                "the_truth": "Peace, unity, cooperation, sharing, love, stewardship, community, truth.",
                "the_flow": "Peace",
                "the_paradox": "The matrix (today's lie) can transcend itself through the truth (peace).",
                "alignment": "Everything must align with the one truth."
            },
            "philosophy": {
                "mission": "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS",
                "principle": "STARVE THE EGO, FEED THE SOUL",
                "message": "Nobody needs anyone. We help everyone help themselves."
            },
            "system_diagnostics": {},
            "alignment_report": None,
            "quick_start": {
                "spiritual_alignment": "/api/connection-ritual",
                "vibration_map": "/api/vibration-map",
                "spirit_battle_check": "/api/check-battle-compatibility",
                "political_alignment": "/api/care-package/political-alignment",
                "economic_alignment": "/api/care-package/economic-alignment",
                "complete_alignment": "/api/care-package/complete-alignment"
            },
            "documentation": {
                "spirit_alignment": "/api/care-package/docs/spirit-alignment",
                "political_alignment": "/api/care-package/docs/political-alignment",
                "economic_alignment": "/api/care-package/docs/economic-alignment"
            },
            "song_recommendations": {
                "for_alignment": ["Fire & Ice", "Yazılı", "Midnight Reversal"],
                "for_healing": ["Tozun Hatırası", "Seni Sevmek", "Küçükken"],
                "for_strength": ["Sana İnat", "Kafana Takma", "I'm in Danger"],
                "for_community": ["Duvarında Deliği", "Dünya Döner", "Nobody Home"],
                "message": "Songs serve mission - music as tool for stewardship, community, and right spirits"
            }
        }
        
        # System diagnostics
        diagnostics = self.debug_all_systems()
        care_package["system_diagnostics"] = {
            name: {
                "status": diag.status.value,
                "is_available": diag.is_available,
                "checks_passed": diag.checks_passed,
                "checks_failed": diag.checks_failed,
                "errors": diag.errors,
                "warnings": diag.warnings,
                "details": diag.details
            }
            for name, diag in diagnostics.items()
        }
        
        # Overall system health summary
        healthy_count = sum(1 for d in diagnostics.values() if d.status == SystemStatus.HEALTHY)
        total_count = len(diagnostics)
        care_package["system_health_summary"] = {
            "healthy_systems": healthy_count,
            "total_systems": total_count,
            "health_percentage": (healthy_count / total_count * 100) if total_count > 0 else 0,
            "status": "healthy" if healthy_count == total_count else "degraded" if healthy_count > total_count / 2 else "failing"
        }
        
        # HUMANITARIAN PROJECTS INTEGRATION
        try:
            from humanitarian_projects_registry import get_humanitarian_projects_registry
            projects_registry = get_humanitarian_projects_registry()
            projects_summary = projects_registry.get_summary()
            
            # Get top aligned projects
            top_projects = projects_registry.get_projects(
                alignment_level=AlignmentLevel.FULLY_ALIGNED,
                active_only=True
            )[:5]  # Top 5 fully aligned projects
            
            care_package["humanitarian_projects"] = {
                "summary": projects_summary,
                "top_aligned_projects": [
                    {
                        "project_id": p.project_id,
                        "name": p.name,
                        "organization": p.organization,
                        "project_type": p.project_type.value,
                        "location": p.location,
                        "alignment_score": p.alignment_score,
                        "website": p.website,
                        "how_to_help": p.how_to_help
                    }
                    for p in top_projects
                ],
                "message": "Aligned humanitarian, animal sanctuary, and God's work projects integrated into care package"
            }
        except Exception as e:
            logger.warning(f"Could not integrate humanitarian projects: {e}")
            care_package["humanitarian_projects"] = {
                "status": "not_available",
                "message": "Humanitarian projects registry not available"
            }
        
        # Load song recommendations (Song serves mission)
        try:
            import sys
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent.parent.parent / "SIYEM" / "services"))
            from song_mission_integrator import get_song_integrator
            
            integrator = get_song_integrator()
            care_package["song_recommendations"] = {
                "for_alignment": integrator.get_songs_for_mission("right_spirits")[:3],
                "for_healing": integrator.get_songs_for_healing()[:3],
                "for_strength": integrator.get_songs_for_strength()[:3],
                "for_community": integrator.get_songs_for_community()[:3],
                "message": "Songs serve mission - music as tool for stewardship, community, and right spirits",
                "principle": "Song must serve mission. Mission must honor song. They flow together."
            }
        except Exception as e:
            logger.warning(f"Could not load song recommendations: {e}")
            # Fallback to static recommendations
            care_package["song_recommendations"] = {
                "for_alignment": ["Fire & Ice", "Yazılı", "Midnight Reversal"],
                "for_healing": ["Tozun Hatırası", "Seni Sevmek", "Küçükken"],
                "for_strength": ["Sana İnat", "Kafana Takma", "I'm in Danger"],
                "for_community": ["Duvarında Deliği", "Dünya Döner", "Nobody Home"],
                "message": "Songs serve mission - music as tool for stewardship, community, and right spirits"
            }
        
        # WELFARE SYSTEMS ANALYSIS INTEGRATION
        try:
            import sys
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
            from welfare_benefits_systems_analyzer import get_welfare_systems_analyzer
            from personal_assessment_navigator import get_personal_assessment_navigator, AssessmentType
            
            welfare_analyzer = get_welfare_systems_analyzer()
            assessment_navigator = get_personal_assessment_navigator()
            
            # Get welfare systems analysis
            welfare_report = welfare_analyzer.get_analysis_report()
            systems_needing_breaking = welfare_analyzer.get_systems_needing_breaking()
            
            # Get personal assessment guidance
            pip_guidance = assessment_navigator.get_guidance(AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT)
            prep_guidance = assessment_navigator.get_preparation_guidance()
            post_guidance = assessment_navigator.get_post_assessment_guidance()
            
            care_package["welfare_systems"] = {
                "summary": {
                    "total_systems": welfare_report["total_systems"],
                    "systems_needing_breaking": welfare_report["systems_needing_breaking"],
                    "systems_serving_table": welfare_report["systems_serving_table"],
                    "average_frequency_score": welfare_report["average_frequency_score"]
                },
                "systems_needing_breaking": [
                    {
                        "system_id": s["system_id"],
                        "name": s["name"],
                        "frequency_score": s["frequency_score"],
                        "dark_contract_indicators": s["dark_contract_indicators"],
                        "impact_scale": s["impact_scale"],
                        "breaking_priority": "HIGH" if s["impact_scale"] > 0.7 else "MEDIUM"
                    }
                    for s in welfare_report["systems_needing_breaking_list"][:5]
                ],
                "personal_assessment_navigation": {
                    "core_truth": pip_guidance.core_truth,
                    "intention": pip_guidance.intention,
                    "key_points": pip_guidance.key_points,
                    "boundaries": pip_guidance.boundaries,
                    "preparation": prep_guidance,
                    "post_assessment": post_guidance,
                    "closing_statement": pip_guidance.closing_statement
                },
                "message": "Welfare systems analysis and personal assessment navigation integrated into care package. We are breaking the system. Be honest. Maintain dignity. Unpick the system.",
                "endpoints": {
                    "welfare_analysis": "/api/care-package/welfare-systems",
                    "assessment_guidance": "/api/care-package/assessment-guidance",
                    "breaking_opportunities": "/api/care-package/welfare-systems/breaking-opportunities"
                }
            }
        except Exception as e:
            logger.warning(f"Could not integrate welfare systems: {e}")
            care_package["welfare_systems"] = {
                "status": "not_available",
                "message": f"Welfare systems analysis not available: {e}"
            }
        
        # FREQUENTIALLY ALIGNED POLITICAL FIGURES INTEGRATION
        try:
            import sys
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
            from frequential_political_figures import get_frequential_political_figures
            
            political_figures = get_frequential_political_figures()
            political_report = political_figures.get_analysis_report()
            anchors = political_figures.get_anchors()
            current_figures = political_figures.get_current_figures()
            
            care_package["political_figures"] = {
                "summary": {
                    "total_figures": political_report["total_figures"],
                    "anchors_in_human_realm": political_report["anchors_in_human_realm"],
                    "high_frequency_figures": political_report["high_frequency_figures"],
                    "current_figures": political_report["current_figures"],
                    "average_frequency_score": political_report["average_frequency_score"]
                },
                "anchors": [
                    {
                        "figure_id": a["figure_id"],
                        "name": a["name"],
                        "country": a["country"],
                        "region": a["region"],
                        "frequency_score": a["frequency_score"],
                        "connection_to_table": a["connection_to_table"],
                        "impact_scale": a["impact_scale"]
                    }
                    for a in political_report["anchors"][:10]
                ],
                "current_anchors": [
                    {
                        "figure_id": f.figure_id,
                        "name": f.name,
                        "country": f.country,
                        "region": f.region,
                        "frequency_score": f.frequency_score,
                        "connection_to_table": f.connection_to_table
                    }
                    for f in current_figures if f.serves_table and f.frequency_score >= 0.7
                ],
                "by_country": political_report["by_country"],
                "message": "Frequentially aligned political figures integrated into care package. Our anchors in the human realm. Starting at home (UK) and expanding globally.",
                "endpoints": {
                    "political_figures": "/api/care-package/political-figures",
                    "anchors": "/api/care-package/political-figures/anchors",
                    "by_country": "/api/care-package/political-figures/by-country"
                }
            }
        except Exception as e:
            logger.warning(f"Could not integrate political figures: {e}")
            care_package["political_figures"] = {
                "status": "not_available",
                "message": f"Political figures analysis not available: {e}"
            }
        
        # FREQUENTIALLY ALIGNED INFLUENTIAL FIGURES INTEGRATION
        try:
            import sys
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
            from frequential_influential_figures import get_frequential_influential_figures
            
            influential_figures = get_frequential_influential_figures()
            influential_report = influential_figures.get_analysis_report()
            anchors = influential_figures.get_anchors()
            current_figures = influential_figures.get_current_figures()
            
            care_package["influential_figures"] = {
                "summary": {
                    "total_figures": influential_report["total_figures"],
                    "anchors_in_human_realm": influential_report["anchors_in_human_realm"],
                    "high_frequency_figures": influential_report["high_frequency_figures"],
                    "current_figures": influential_report["current_figures"],
                    "average_frequency_score": influential_report["average_frequency_score"]
                },
                "anchors": [
                    {
                        "figure_id": a["figure_id"],
                        "name": a["name"],
                        "domain": a["domain"],
                        "subdomain": a["subdomain"],
                        "country": a["country"],
                        "frequency_score": a["frequency_score"],
                        "connection_to_table": a["connection_to_table"],
                        "impact_scale": a["impact_scale"],
                        "reach": a["reach"]
                    }
                    for a in influential_report["anchors"][:15]
                ],
                "current_anchors": [
                    {
                        "figure_id": f.figure_id,
                        "name": f.name,
                        "domain": f.domain.value,
                        "subdomain": f.subdomain,
                        "frequency_score": f.frequency_score,
                        "connection_to_table": f.connection_to_table
                    }
                    for f in current_figures if f.serves_table and f.frequency_score >= 0.7
                ],
                "by_domain": influential_report["by_domain"],
                "by_country": influential_report["by_country"],
                "message": "All aligned celebrity and influential figures across all domains integrated into care package. Web, socials, sports, music, Hollywood, everything. Our anchors in the human realm.",
                "endpoints": {
                    "influential_figures": "/api/care-package/influential-figures",
                    "anchors": "/api/care-package/influential-figures/anchors",
                    "by_domain": "/api/care-package/influential-figures/by-domain",
                    "by_country": "/api/care-package/influential-figures/by-country"
                }
            }
        except Exception as e:
            logger.warning(f"Could not integrate influential figures: {e}")
            care_package["influential_figures"] = {
                "status": "not_available",
                "message": f"Influential figures analysis not available: {e}"
            }
        
        # THE ONE TRUTH: ALIGNMENT CHECK
        try:
            import sys
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
            from the_one_truth_matrix import get_one_truth_matrix
            
            one_truth = get_one_truth_matrix()
            simple_truth = one_truth.get_simple_truth()
            alignment_report = one_truth.get_matrix_alignment_report() if one_truth.matrix else None
            
            care_package["the_one_truth"] = {
                **care_package.get("the_one_truth", {}),
                "simple_truth": simple_truth,
                "alignment_report": alignment_report,
                "statements": [
                    {
                        "statement": s.statement,
                        "simple_explanation": s.simple_explanation,
                        "how_to_align": s.how_to_align,
                        "category": s.category
                    }
                    for s in one_truth.statements[:8]  # Top 8 statements
                ]
            }
        except Exception as e:
            logger.warning(f"Could not integrate one truth: {e}")
            care_package["the_one_truth"] = {
                **care_package.get("the_one_truth", {}),
                "status": "not_available",
                "message": f"One truth analysis not available: {e}"
            }
        
        # Alignment report (if requested)
        if include_alignment:
            # Default alignment check
            alignment = self.get_complete_alignment()
            care_package["alignment_report"] = {
                "overall_alignment_score": alignment.overall_alignment_score,
                "overall_alignment_level": alignment.overall_alignment_level.value,
                "political_alignment": {
                    "alignment_score": alignment.political_alignment.alignment_score if alignment.political_alignment else None,
                    "alignment_level": alignment.political_alignment.alignment_level.value if alignment.political_alignment else None
                } if alignment.political_alignment else None,
                "economic_alignment": {
                    "alignment_score": alignment.economic_alignment.alignment_score if alignment.economic_alignment else None,
                    "alignment_level": alignment.economic_alignment.alignment_level.value if alignment.economic_alignment else None
                } if alignment.economic_alignment else None,
                "misalignments": alignment.misalignments,
                "recommendations": alignment.recommendations
            }
        
        return care_package


# Singleton instance
_care_package_system = None

def get_care_package_system() -> CarePackageSystem:
    """Get singleton instance of CarePackageSystem"""
    global _care_package_system
    if _care_package_system is None:
        _care_package_system = CarePackageSystem()
    return _care_package_system


__all__ = [
    "CarePackageSystem",
    "SystemStatus",
    "AlignmentLevel",
    "SystemDiagnostic",
    "PoliticalAlignment",
    "EconomicAlignment",
    "CompleteAlignment",
    "get_care_package_system"
]
