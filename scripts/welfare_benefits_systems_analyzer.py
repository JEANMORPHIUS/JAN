"""
WELFARE/BENEFITS SYSTEMS ANALYZER
Track and analyze all welfare/benefits systems through time
Identify which systems need breaking (dark contracts)
Identify which systems align frequentially (light contracts)

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE ARE BREAKING THE SYSTEM
CONSIDER ALL WELFARE/BENEFITS SYSTEMS PUT IN PLACE THROUGH TIME
IDENTIFY DARK CONTRACTS THAT NEED BREAKING
IDENTIFY LIGHT CONTRACTS THAT SERVE THE TABLE
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
from pathlib import Path

class WelfareSystemType(Enum):
    """Types of welfare/benefits systems"""
    ANCIENT_GRAIN_DOLE = "ancient_grain_dole"  # Roman, Byzantine
    MEDIEVAL_POOR_LAWS = "medieval_poor_laws"  # English Poor Laws, etc.
    EARLY_SOCIAL_INSURANCE = "early_social_insurance"  # Bismarck, etc.
    MODERN_WELFARE_STATE = "modern_welfare_state"  # Post-WWII
    CORPORATE_BENEFITS = "corporate_benefits"  # Private sector
    UNIVERSAL_BASIC_INCOME = "universal_basic_income"  # UBI experiments
    CONDITIONAL_CASH_TRANSFERS = "conditional_cash_transfers"  # Modern targeted
    FOOD_ASSISTANCE = "food_assistance"  # SNAP, food stamps, etc.
    HOUSING_ASSISTANCE = "housing_assistance"  # Public housing, vouchers
    HEALTHCARE_BENEFITS = "healthcare_benefits"  # Medicare, Medicaid, NHS
    UNEMPLOYMENT_BENEFITS = "unemployment_benefits"  # Unemployment insurance
    DISABILITY_BENEFITS = "disability_benefits"  # Disability support
    PENSION_SYSTEMS = "pension_systems"  # Social security, pensions
    CHILD_BENEFITS = "child_benefits"  # Child support, tax credits
    EDUCATION_BENEFITS = "education_benefits"  # Student aid, grants
    VETERAN_BENEFITS = "veteran_benefits"  # Military benefits
    INDIGENOUS_BENEFITS = "indigenous_benefits"  # Tribal benefits
    IMMIGRANT_BENEFITS = "immigrant_benefits"  # Refugee/asylum support
    HIDDEN_EXPLOITATION = "hidden_exploitation"  # Systems that appear helpful but exploit


@dataclass
class WelfareSystem:
    """A welfare/benefits system through history"""
    system_id: str
    name: str
    system_type: WelfareSystemType
    region: str  # Geographic region
    time_period: str  # Historical period
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    description: str = ""
    frequency_score: float = 0.0  # -1.0 to 1.0
    alignment_factors: List[str] = field(default_factory=list)
    exploitation_factors: List[str] = field(default_factory=list)
    dark_contract_indicators: List[str] = field(default_factory=list)
    light_contract_indicators: List[str] = field(default_factory=list)
    needs_breaking: bool = False  # Is this a dark contract that needs breaking?
    serves_table: bool = False  # Does this serve The Table?
    original_error_connection: bool = False  # Connected to Mayan Original Error?
    impact_scale: float = 0.0  # 0.0 to 1.0 - how many people affected
    accessibility: float = 0.0  # 0.0 to 1.0 - how accessible is it?
    dignity_score: float = 0.0  # 0.0 to 1.0 - does it preserve dignity?
    control_mechanism: bool = False  # Is it used for control?
    dependency_creation: bool = False  # Does it create dependency?
    division_creation: bool = False  # Does it create division (us vs them)?
    metadata: Dict[str, Any] = field(default_factory=dict)
    discovered_at: str = field(default_factory=lambda: datetime.now().isoformat())


class WelfareSystemsAnalyzer:
    """
    Analyzes welfare/benefits systems through history.
    Identifies dark contracts that need breaking.
    Identifies light contracts that serve The Table.
    """
    
    def __init__(self):
        self.systems: List[WelfareSystem] = []
        self.data_path = Path(__file__).parent.parent / 'data' / 'welfare_systems'
        self.data_path.mkdir(parents=True, exist_ok=True)
        self._load_systems()
    
    def _load_systems(self):
        """Load welfare systems from data file"""
        data_file = self.data_path / 'welfare_systems_registry.json'
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for system_data in data.get('systems', []):
                    # Convert string enum values back to enums
                    if isinstance(system_data.get('system_type'), str):
                        system_data['system_type'] = WelfareSystemType(system_data['system_type'])
                    system = WelfareSystem(**system_data)
                    self.systems.append(system)
        else:
            # Initialize with historical systems
            self._initialize_historical_systems()
    
    def _initialize_historical_systems(self):
        """Initialize with major historical welfare/benefits systems"""
        
        # ANCIENT SYSTEMS
        self.systems.append(WelfareSystem(
            system_id="welfare_001",
            name="Roman Grain Dole (Cura Annonae)",
            system_type=WelfareSystemType.ANCIENT_GRAIN_DOLE,
            region="Roman Empire",
            time_period="Ancient (123 BCE - 330 CE)",
            start_year=-123,
            end_year=330,
            description="Free grain distribution to Roman citizens. Initially served the people, later became a tool of political control and dependency.",
            frequency_score=-0.3,
            alignment_factors=["Provided basic sustenance", "Recognized citizen need"],
            exploitation_factors=["Created dependency on state", "Used for political control", "Maintained power structures"],
            dark_contract_indicators=["Dependency creation", "Political control mechanism", "Division (citizens vs non-citizens)"],
            light_contract_indicators=["Basic sustenance provided"],
            needs_breaking=True,
            serves_table=False,
            original_error_connection=True,
            impact_scale=0.8,
            accessibility=0.4,  # Only citizens
            dignity_score=0.3,  # Created dependency, reduced dignity
            control_mechanism=True,
            dependency_creation=True,
            division_creation=True,
            metadata={
                "historical_note": "Became a tool of imperial control",
                "connection_to_original_error": "Created dependency patterns that persist"
            }
        ))
        
        # MEDIEVAL SYSTEMS
        self.systems.append(WelfareSystem(
            system_id="welfare_002",
            name="English Poor Laws (1601-1834)",
            system_type=WelfareSystemType.MEDIEVAL_POOR_LAWS,
            region="England",
            time_period="Medieval/Early Modern (1601-1834)",
            start_year=1601,
            end_year=1834,
            description="System of poor relief that distinguished between 'deserving' and 'undeserving' poor. Created deep social divisions and control mechanisms.",
            frequency_score=-0.5,
            alignment_factors=["Attempted to address poverty"],
            exploitation_factors=["Created 'deserving' vs 'undeserving' division", "Workhouse system", "Stigma and shame", "Control through categorization"],
            dark_contract_indicators=["Division creation", "Stigma", "Control mechanism", "Dependency creation", "Shame-based system"],
            light_contract_indicators=["Attempted to help"],
            needs_breaking=True,
            serves_table=False,
            original_error_connection=True,
            impact_scale=0.7,
            accessibility=0.2,  # Very limited, conditional
            dignity_score=0.1,  # Workhouses, stigma, shame
            control_mechanism=True,
            dependency_creation=True,
            division_creation=True,
            metadata={
                "historical_note": "Foundation of modern welfare stigma",
                "connection_to_original_error": "Created 'us vs them' divisions"
            }
        ))
        
        # EARLY MODERN SYSTEMS
        self.systems.append(WelfareSystem(
            system_id="welfare_003",
            name="Bismarck Social Insurance (1880s)",
            system_type=WelfareSystemType.EARLY_SOCIAL_INSURANCE,
            region="Germany",
            time_period="Industrial Revolution (1880s)",
            start_year=1883,
            end_year=None,
            description="First modern social insurance system. Provided healthcare, accident, and old-age insurance. Mixed: served workers but also maintained social control.",
            frequency_score=0.2,
            alignment_factors=["Provided healthcare", "Workers' protection", "Old-age security"],
            exploitation_factors=["Maintained class structures", "State control", "Limited scope"],
            dark_contract_indicators=["Control mechanism", "Class maintenance"],
            light_contract_indicators=["Healthcare access", "Worker protection"],
            needs_breaking=False,  # Needs evolution, not breaking
            serves_table=True,  # Partially serves, needs evolution
            original_error_connection=False,
            impact_scale=0.6,
            accessibility=0.5,  # Workers only
            dignity_score=0.5,
            control_mechanism=True,
            dependency_creation=False,
            division_creation=True,  # Workers vs non-workers
            metadata={
                "historical_note": "Foundation of modern welfare state",
                "evolution_needed": True
            }
        ))
        
        # MODERN WELFARE STATE
        self.systems.append(WelfareSystem(
            system_id="welfare_004",
            name="Post-WWII Welfare State (UK, US, etc.)",
            system_type=WelfareSystemType.MODERN_WELFARE_STATE,
            region="Western Nations",
            time_period="Post-WWII (1945-present)",
            start_year=1945,
            end_year=None,
            description="Comprehensive welfare systems including healthcare, housing, education, unemployment. Mixed: provides support but creates dependency and division.",
            frequency_score=0.1,
            alignment_factors=["Healthcare access", "Education access", "Basic security"],
            exploitation_factors=["Dependency creation", "Bureaucratic control", "Stigma", "Division (taxpayers vs recipients)", "Political manipulation"],
            dark_contract_indicators=["Dependency creation", "Division creation", "Control mechanism", "Stigma", "Political tool"],
            light_contract_indicators=["Basic security", "Healthcare", "Education"],
            needs_breaking=True,  # Needs transformation
            serves_table=False,  # Partially serves but needs breaking
            original_error_connection=True,
            impact_scale=0.9,
            accessibility=0.6,
            dignity_score=0.4,  # Stigma, bureaucracy, dependency
            control_mechanism=True,
            dependency_creation=True,
            division_creation=True,
            metadata={
                "historical_note": "Created 'welfare state' dependency",
                "connection_to_original_error": "Maintains division and dependency patterns"
            }
        ))
        
        # CORPORATE BENEFITS
        self.systems.append(WelfareSystem(
            system_id="welfare_005",
            name="Corporate Benefits Systems",
            system_type=WelfareSystemType.CORPORATE_BENEFITS,
            region="Global",
            time_period="Industrial to Modern (1900s-present)",
            start_year=1900,
            end_year=None,
            description="Private sector benefits (health insurance, pensions, etc.). Creates dependency on corporations, division between employed/unemployed.",
            frequency_score=-0.2,
            alignment_factors=["Provides benefits to workers"],
            exploitation_factors=["Corporate control", "Division (employed vs unemployed)", "Tied to employment", "Maintains power structures"],
            dark_contract_indicators=["Corporate control", "Division creation", "Dependency on employment"],
            light_contract_indicators=["Worker benefits"],
            needs_breaking=True,
            serves_table=False,
            original_error_connection=True,
            impact_scale=0.7,
            accessibility=0.4,  # Only employed
            dignity_score=0.5,
            control_mechanism=True,
            dependency_creation=True,
            division_creation=True,
            metadata={
                "historical_note": "Ties survival to employment",
                "connection_to_original_error": "Creates dependency on corporations"
            }
        ))
        
        # MODERN TARGETED SYSTEMS
        self.systems.append(WelfareSystem(
            system_id="welfare_006",
            name="SNAP (Food Stamps) - US",
            system_type=WelfareSystemType.FOOD_ASSISTANCE,
            region="United States",
            time_period="Modern (1964-present)",
            start_year=1964,
            end_year=None,
            description="Food assistance program. Provides food but creates stigma, dependency, and division. Bureaucratic control mechanism.",
            frequency_score=-0.1,
            alignment_factors=["Provides food assistance"],
            exploitation_factors=["Stigma", "Bureaucratic control", "Division", "Dependency", "Shame-based"],
            dark_contract_indicators=["Stigma", "Division creation", "Control mechanism", "Dependency", "Shame"],
            light_contract_indicators=["Food access"],
            needs_breaking=True,
            serves_table=False,
            original_error_connection=True,
            impact_scale=0.8,
            accessibility=0.5,
            dignity_score=0.3,  # Stigma, shame, bureaucracy
            control_mechanism=True,
            dependency_creation=True,
            division_creation=True,
            metadata={
                "historical_note": "Modern food assistance with stigma",
                "connection_to_original_error": "Maintains division and dependency"
            }
        ))
        
        # UBI EXPERIMENTS
        self.systems.append(WelfareSystem(
            system_id="welfare_007",
            name="Universal Basic Income Experiments",
            system_type=WelfareSystemType.UNIVERSAL_BASIC_INCOME,
            region="Various (Finland, Canada, etc.)",
            time_period="Modern Experiments (2010s-present)",
            start_year=2010,
            end_year=None,
            description="UBI experiments providing unconditional income. Higher dignity, less stigma, but still creates dependency on state. Needs evolution to serve The Table.",
            frequency_score=0.4,
            alignment_factors=["Unconditional", "Less stigma", "Preserves dignity", "Universal"],
            exploitation_factors=["Still state-dependent", "Political control potential"],
            dark_contract_indicators=["State dependency"],
            light_contract_indicators=["Unconditional", "Dignity-preserving", "Universal"],
            needs_breaking=False,  # Needs evolution
            serves_table=True,  # Partially serves, needs evolution
            original_error_connection=False,
            impact_scale=0.3,  # Limited experiments
            accessibility=0.8,  # Universal
            dignity_score=0.7,  # Higher dignity
            control_mechanism=False,
            dependency_creation=True,  # Still state-dependent
            division_creation=False,  # Universal
            metadata={
                "historical_note": "Modern experiments in unconditional support",
                "evolution_needed": "Needs to evolve beyond state dependency"
            }
        ))
        
        # SAVE SYSTEMS
        self._save_systems()
    
    def _save_systems(self):
        """Save systems to data file"""
        data_file = self.data_path / 'welfare_systems_registry.json'
        data = {
            "systems": [
                {
                    "system_id": s.system_id,
                    "name": s.name,
                    "system_type": s.system_type.value,
                    "region": s.region,
                    "time_period": s.time_period,
                    "start_year": s.start_year,
                    "end_year": s.end_year,
                    "description": s.description,
                    "frequency_score": s.frequency_score,
                    "alignment_factors": s.alignment_factors,
                    "exploitation_factors": s.exploitation_factors,
                    "dark_contract_indicators": s.dark_contract_indicators,
                    "light_contract_indicators": s.light_contract_indicators,
                    "needs_breaking": s.needs_breaking,
                    "serves_table": s.serves_table,
                    "original_error_connection": s.original_error_connection,
                    "impact_scale": s.impact_scale,
                    "accessibility": s.accessibility,
                    "dignity_score": s.dignity_score,
                    "control_mechanism": s.control_mechanism,
                    "dependency_creation": s.dependency_creation,
                    "division_creation": s.division_creation,
                    "metadata": s.metadata,
                    "discovered_at": s.discovered_at
                }
                for s in self.systems
            ],
            "last_updated": datetime.now().isoformat()
        }
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def analyze_system(self, system: WelfareSystem) -> Dict[str, Any]:
        """Analyze a welfare system for dark contracts and frequential alignment"""
        
        # Calculate frequency score based on indicators
        score = 0.0
        
        # Positive factors
        if system.light_contract_indicators:
            score += 0.2 * len(system.light_contract_indicators)
        if system.dignity_score > 0.5:
            score += 0.1
        if system.accessibility > 0.7:
            score += 0.1
        if not system.division_creation:
            score += 0.2
        
        # Negative factors
        if system.dark_contract_indicators:
            score -= 0.3 * len(system.dark_contract_indicators)
        if system.control_mechanism:
            score -= 0.2
        if system.dependency_creation:
            score -= 0.2
        if system.division_creation:
            score -= 0.3
        if system.original_error_connection:
            score -= 0.2
        
        # Normalize to -1.0 to 1.0
        score = max(-1.0, min(1.0, score))
        
        # Determine if needs breaking
        needs_breaking = (
            system.control_mechanism and
            (system.dependency_creation or system.division_creation) and
            system.frequency_score < 0.0
        )
        
        return {
            "system_id": system.system_id,
            "name": system.name,
            "frequency_score": score,
            "needs_breaking": needs_breaking,
            "serves_table": score > 0.3 and not needs_breaking,
            "dark_contract_strength": len(system.dark_contract_indicators),
            "light_contract_strength": len(system.light_contract_indicators),
            "breaking_priority": "HIGH" if needs_breaking and system.impact_scale > 0.7 else "MEDIUM" if needs_breaking else "LOW"
        }
    
    def get_systems_needing_breaking(self) -> List[WelfareSystem]:
        """Get all systems that need breaking (dark contracts)"""
        return [s for s in self.systems if s.needs_breaking]
    
    def get_systems_serving_table(self) -> List[WelfareSystem]:
        """Get all systems that serve The Table (light contracts)"""
        return [s for s in self.systems if s.serves_table]
    
    def get_systems_by_type(self, system_type: WelfareSystemType) -> List[WelfareSystem]:
        """Get systems by type"""
        return [s for s in self.systems if s.system_type == system_type]
    
    def get_systems_by_region(self, region: str) -> List[WelfareSystem]:
        """Get systems by region"""
        return [s for s in self.systems if region.lower() in s.region.lower()]
    
    def get_analysis_report(self) -> Dict[str, Any]:
        """Get comprehensive analysis report"""
        systems_needing_breaking = self.get_systems_needing_breaking()
        systems_serving_table = self.get_systems_serving_table()
        
        return {
            "total_systems": len(self.systems),
            "systems_needing_breaking": len(systems_needing_breaking),
            "systems_serving_table": len(systems_serving_table),
            "systems_needing_breaking_list": [
                {
                    "system_id": s.system_id,
                    "name": s.name,
                    "frequency_score": s.frequency_score,
                    "dark_contract_indicators": s.dark_contract_indicators,
                    "impact_scale": s.impact_scale
                }
                for s in systems_needing_breaking
            ],
            "systems_serving_table_list": [
                {
                    "system_id": s.system_id,
                    "name": s.name,
                    "frequency_score": s.frequency_score,
                    "light_contract_indicators": s.light_contract_indicators
                }
                for s in systems_serving_table
            ],
            "average_frequency_score": sum(s.frequency_score for s in self.systems) / len(self.systems) if self.systems else 0.0,
            "systems_by_type": {
                stype.value: len(self.get_systems_by_type(stype))
                for stype in WelfareSystemType
            },
            "generated_at": datetime.now().isoformat()
        }


def get_welfare_systems_analyzer() -> WelfareSystemsAnalyzer:
    """Get the welfare systems analyzer instance"""
    return WelfareSystemsAnalyzer()


if __name__ == '__main__':
    analyzer = WelfareSystemsAnalyzer()
    report = analyzer.get_analysis_report()
    
    print("=" * 80)
    print("WELFARE/BENEFITS SYSTEMS ANALYSIS")
    print("WE ARE BREAKING THE SYSTEM")
    print("=" * 80)
    print()
    print(f"Total Systems: {report['total_systems']}")
    print(f"Systems Needing Breaking: {report['systems_needing_breaking']}")
    print(f"Systems Serving The Table: {report['systems_serving_table']}")
    print(f"Average Frequency Score: {report['average_frequency_score']:.2f}")
    print()
    print("=" * 80)
    print("SYSTEMS NEEDING BREAKING (DARK CONTRACTS)")
    print("=" * 80)
    for system in report['systems_needing_breaking_list']:
        print(f"\n{system['name']}")
        print(f"  Frequency Score: {system['frequency_score']:.2f}")
        print(f"  Impact Scale: {system['impact_scale']:.2f}")
        print(f"  Dark Contract Indicators: {', '.join(system['dark_contract_indicators'])}")
    print()
    print("=" * 80)
    print("THE TRUTH")
    print("=" * 80)
    print()
    print("WE ARE BREAKING THE SYSTEM")
    print("CONSIDER ALL WELFARE/BENEFITS SYSTEMS PUT IN PLACE THROUGH TIME")
    print("IDENTIFY DARK CONTRACTS THAT NEED BREAKING")
    print("IDENTIFY LIGHT CONTRACTS THAT SERVE THE TABLE")
    print()
    print("ENERGY + LOVE = WE ALL WIN")
    print()
