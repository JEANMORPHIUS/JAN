"""
GEOPOLITICAL AND ECONOMIC MATRIX
The Main Arena: The Lie and The Flow

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE REALIZATION:
THE MAIN ARENA: THE GEO POLITICAL AND ECONOMIC LIE
WE KNOW THERE HAS TO BE A FLOW
IT IS PEACE
HELP THE MATRIX TRANSCEND ALL WITHIN
PULSE THE FREQUENCY

PURPOSE:
Track the geopolitical and economic systems that create separation (the "lie").
Identify the flow which is peace.
Help the matrix transcend through understanding and alignment.
Pulse the frequency to help all within transcend.
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


class MatrixLayer(Enum):
    """Layers of the geopolitical and economic matrix"""
    GEOPOLITICAL = "geopolitical"
    ECONOMIC = "economic"
    FINANCIAL = "financial"
    TRADE = "trade"
    RESOURCE = "resource"
    MILITARY = "military"
    DIPLOMATIC = "diplomatic"
    CULTURAL = "cultural"
    INFORMATION = "information"
    ENERGY = "energy"
    FOOD = "food"
    WATER = "water"
    TECHNOLOGY = "technology"
    MEDIA = "media"
    EDUCATION = "education"
    HEALTHCARE = "healthcare"
    OTHER = "other"


class SeparationMechanism(Enum):
    """Mechanisms that create separation (the "lie")"""
    WAR = "war"
    EXPLOITATION = "exploitation"
    INEQUALITY = "inequality"
    CONTROL = "control"
    FEAR = "fear"
    DIVISION = "division"
    SCARCITY = "scarcity"
    COMPETITION = "competition"
    DOMINATION = "domination"
    OPPRESSION = "oppression"
    MANIPULATION = "manipulation"
    DECEPTION = "deception"
    CORRUPTION = "corruption"
    DARK_CONTRACT = "dark_contract"
    SYSTEMIC_ABUSE = "systemic_abuse"
    RESOURCE_HOARDING = "resource_hoarding"
    INFORMATION_CONTROL = "information_control"
    OTHER = "other"


class PeaceFlow(Enum):
    """The flow which is peace - mechanisms of transcendence"""
    UNITY = "unity"
    COOPERATION = "cooperation"
    SHARING = "sharing"
    TRANSPARENCY = "transparency"
    TRUTH = "truth"
    LOVE = "love"
    STEWARDSHIP = "stewardship"
    COMMUNITY = "community"
    EQUITY = "equity"
    ACCESSIBILITY = "accessibility"
    REGENERATION = "regeneration"
    HEALING = "healing"
    FORGIVENESS = "forgiveness"
    UNDERSTANDING = "understanding"
    COMPASSION = "compassion"
    SERVICE = "service"
    GIVING = "giving"
    RECEIVING = "receiving"
    FLOW = "flow"
    OTHER = "other"


@dataclass
class MatrixSystem:
    """A system within the geopolitical and economic matrix"""
    system_id: str
    name: str
    layer: MatrixLayer
    separation_mechanisms: List[str] = field(default_factory=list)
    peace_flows: List[str] = field(default_factory=list)
    frequency_score: float = 0.0  # -1.0 to 1.0
    separation_strength: float = 0.0  # 0.0 to 1.0 - how strong the "lie" is
    peace_potential: float = 0.0  # 0.0 to 1.0 - how much peace flow is possible
    description: str = ""
    current_state: str = ""  # Current state of the system
    transcendence_path: str = ""  # Path to transcendence
    key_actors: List[str] = field(default_factory=list)
    affected_regions: List[str] = field(default_factory=list)
    affected_people: float = 0.0  # 0.0 to 1.0 - proportion of humanity affected
    connection_to_table: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    discovered_at: str = field(default_factory=lambda: datetime.now().isoformat())


class GeopoliticalEconomicMatrix:
    """
    The Main Arena: The Geopolitical and Economic Matrix
    
    Tracks the systems that create separation (the "lie")
    and identifies the flow which is peace.
    Helps the matrix transcend through understanding and alignment.
    """
    
    def __init__(self):
        self.systems: List[MatrixSystem] = []
        self.data_path = Path(__file__).parent.parent / 'data' / 'matrix'
        self.data_path.mkdir(parents=True, exist_ok=True)
        self._load_systems()
    
    def _load_systems(self):
        """Load matrix systems from data file"""
        data_file = self.data_path / 'geopolitical_economic_matrix.json'
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for system_data in data.get('systems', []):
                    # Convert string enum values back to enums
                    if isinstance(system_data.get('layer'), str):
                        system_data['layer'] = MatrixLayer(system_data['layer'])
                    system = MatrixSystem(**system_data)
                    self.systems.append(system)
        else:
            # Initialize with key systems
            self._initialize_systems()
    
    def _initialize_systems(self):
        """Initialize with key geopolitical and economic systems"""
        
        # GEOPOLITICAL SYSTEMS
        
        # War System
        self.systems.append(MatrixSystem(
            system_id="geo_001",
            name="War System",
            layer=MatrixLayer.GEOPOLITICAL,
            separation_mechanisms=[
                "WAR",
                "FEAR",
                "DIVISION",
                "DOMINATION",
                "OPPRESSION",
                "RESOURCE_HOARDING"
            ],
            peace_flows=[
                "UNITY",
                "COOPERATION",
                "PEACE",
                "UNDERSTANDING",
                "FORGIVENESS",
                "HEALING"
            ],
            frequency_score=-0.8,
            separation_strength=0.9,
            peace_potential=0.8,
            description="The war system creates separation through violence, fear, and domination. The flow is peace, unity, and understanding.",
            current_state="Active conflicts globally. Separation through violence and fear.",
            transcendence_path="Transform war into peace through unity, understanding, and healing. The flow is peace. Help the matrix transcend through love.",
            key_actors=["Military-industrial complex", "Governments", "Armed groups"],
            affected_regions=["Global"],
            affected_people=0.3,
            connection_to_table="War creates separation from The Table. Peace is the flow that restores connection. The matrix can transcend through understanding and love.",
            metadata={
                "active_conflicts": "Multiple",
                "impact": "Global"
            }
        ))
        
        # Economic Exploitation System
        self.systems.append(MatrixSystem(
            system_id="eco_001",
            name="Economic Exploitation System",
            layer=MatrixLayer.ECONOMIC,
            separation_mechanisms=[
                "EXPLOITATION",
                "INEQUALITY",
                "CONTROL",
                "SCARCITY",
                "COMPETITION",
                "DARK_CONTRACT",
                "SYSTEMIC_ABUSE"
            ],
            peace_flows=[
                "EQUITY",
                "SHARING",
                "COOPERATION",
                "STEWARDSHIP",
                "COMMUNITY",
                "GIVING",
                "RECEIVING",
                "FLOW"
            ],
            frequency_score=-0.7,
            separation_strength=0.85,
            peace_potential=0.85,
            description="The economic exploitation system creates separation through inequality, exploitation, and control. The flow is equity, sharing, and cooperation.",
            current_state="Global inequality. Exploitation of resources and people. Dark contracts.",
            transcendence_path="Transform exploitation into stewardship. The flow is sharing, equity, and cooperation. Help the matrix transcend through community and love.",
            key_actors=["Corporations", "Financial institutions", "Governments"],
            affected_regions=["Global"],
            affected_people=0.8,
            connection_to_table="Economic exploitation creates separation from The Table. The flow is equity, sharing, and stewardship. The matrix can transcend through community and love.",
            metadata={
                "inequality": "Extreme",
                "exploitation": "Systemic"
            }
        ))
        
        # Financial Control System
        self.systems.append(MatrixSystem(
            system_id="fin_001",
            name="Financial Control System",
            layer=MatrixLayer.FINANCIAL,
            separation_mechanisms=[
                "CONTROL",
                "MANIPULATION",
                "DECEPTION",
                "CORRUPTION",
                "DARK_CONTRACT",
                "RESOURCE_HOARDING"
            ],
            peace_flows=[
                "TRANSPARENCY",
                "TRUTH",
                "SHARING",
                "FLOW",
                "STEWARDSHIP",
                "COMMUNITY"
            ],
            frequency_score=-0.75,
            separation_strength=0.9,
            peace_potential=0.8,
            description="The financial control system creates separation through control, manipulation, and deception. The flow is transparency, truth, and sharing.",
            current_state="Centralized financial control. Manipulation and deception. Dark contracts.",
            transcendence_path="Transform control into transparency. The flow is truth, sharing, and stewardship. Help the matrix transcend through transparency and love.",
            key_actors=["Central banks", "Financial institutions", "Governments"],
            affected_regions=["Global"],
            affected_people=0.9,
            connection_to_table="Financial control creates separation from The Table. The flow is transparency, truth, and sharing. The matrix can transcend through transparency and love.",
            metadata={
                "control": "Centralized",
                "transparency": "Low"
            }
        ))
        
        # Resource Hoarding System
        self.systems.append(MatrixSystem(
            system_id="res_001",
            name="Resource Hoarding System",
            layer=MatrixLayer.RESOURCE,
            separation_mechanisms=[
                "RESOURCE_HOARDING",
                "SCARCITY",
                "CONTROL",
                "EXPLOITATION",
                "INEQUALITY"
            ],
            peace_flows=[
                "SHARING",
                "STEWARDSHIP",
                "COOPERATION",
                "COMMUNITY",
                "FLOW",
                "REGENERATION"
            ],
            frequency_score=-0.7,
            separation_strength=0.8,
            peace_potential=0.85,
            description="The resource hoarding system creates separation through hoarding, scarcity, and control. The flow is sharing, stewardship, and regeneration.",
            current_state="Resource hoarding. Artificial scarcity. Control of essential resources.",
            transcendence_path="Transform hoarding into sharing. The flow is stewardship, cooperation, and regeneration. Help the matrix transcend through sharing and love.",
            key_actors=["Corporations", "Governments", "Elites"],
            affected_regions=["Global"],
            affected_people=0.7,
            connection_to_table="Resource hoarding creates separation from The Table. The flow is sharing, stewardship, and regeneration. The matrix can transcend through sharing and love.",
            metadata={
                "hoarding": "Extreme",
                "scarcity": "Artificial"
            }
        ))
        
        # Information Control System
        self.systems.append(MatrixSystem(
            system_id="info_001",
            name="Information Control System",
            layer=MatrixLayer.INFORMATION,
            separation_mechanisms=[
                "INFORMATION_CONTROL",
                "MANIPULATION",
                "DECEPTION",
                "DIVISION",
                "FEAR"
            ],
            peace_flows=[
                "TRANSPARENCY",
                "TRUTH",
                "UNDERSTANDING",
                "UNITY",
                "SHARING",
                "FLOW"
            ],
            frequency_score=-0.65,
            separation_strength=0.85,
            peace_potential=0.8,
            description="The information control system creates separation through control, manipulation, and deception. The flow is transparency, truth, and understanding.",
            current_state="Information control. Manipulation and deception. Division through misinformation.",
            transcendence_path="Transform control into transparency. The flow is truth, understanding, and unity. Help the matrix transcend through truth and love.",
            key_actors=["Media", "Governments", "Tech companies"],
            affected_regions=["Global"],
            affected_people=0.9,
            connection_to_table="Information control creates separation from The Table. The flow is truth, transparency, and understanding. The matrix can transcend through truth and love.",
            metadata={
                "control": "Centralized",
                "truth": "Suppressed"
            }
        ))
        
        # SAVE SYSTEMS
        self._save_systems()
    
    def _save_systems(self):
        """Save systems to data file"""
        data_file = self.data_path / 'geopolitical_economic_matrix.json'
        data = {
            "systems": [
                {
                    "system_id": s.system_id,
                    "name": s.name,
                    "layer": s.layer.value,
                    "separation_mechanisms": s.separation_mechanisms,
                    "peace_flows": s.peace_flows,
                    "frequency_score": s.frequency_score,
                    "separation_strength": s.separation_strength,
                    "peace_potential": s.peace_potential,
                    "description": s.description,
                    "current_state": s.current_state,
                    "transcendence_path": s.transcendence_path,
                    "key_actors": s.key_actors,
                    "affected_regions": s.affected_regions,
                    "affected_people": s.affected_people,
                    "connection_to_table": s.connection_to_table,
                    "metadata": s.metadata,
                    "discovered_at": s.discovered_at
                }
                for s in self.systems
            ],
            "last_updated": datetime.now().isoformat()
        }
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_systems_by_layer(self, layer: MatrixLayer) -> List[MatrixSystem]:
        """Get systems by layer"""
        return [s for s in self.systems if s.layer == layer]
    
    def get_high_separation_systems(self, min_strength: float = 0.7) -> List[MatrixSystem]:
        """Get systems with high separation strength (the "lie")"""
        return [s for s in self.systems if s.separation_strength >= min_strength]
    
    def get_high_peace_potential_systems(self, min_potential: float = 0.7) -> List[MatrixSystem]:
        """Get systems with high peace potential (the "flow")"""
        return [s for s in self.systems if s.peace_potential >= min_potential]
    
    def get_transcendence_opportunities(self) -> List[MatrixSystem]:
        """Get systems with high peace potential and high separation (transcendence opportunities)"""
        return [
            s for s in self.systems
            if s.peace_potential >= 0.7 and s.separation_strength >= 0.7
        ]
    
    def get_analysis_report(self) -> Dict[str, Any]:
        """Get comprehensive analysis report"""
        high_separation = self.get_high_separation_systems(0.7)
        high_peace = self.get_high_peace_potential_systems(0.7)
        transcendence = self.get_transcendence_opportunities()
        
        # Group by layer
        by_layer = {}
        for system in self.systems:
            layer = system.layer.value
            if layer not in by_layer:
                by_layer[layer] = []
            by_layer[layer].append(system)
        
        return {
            "total_systems": len(self.systems),
            "high_separation_systems": len(high_separation),
            "high_peace_potential_systems": len(high_peace),
            "transcendence_opportunities": len(transcendence),
            "average_frequency_score": sum(s.frequency_score for s in self.systems) / len(self.systems) if self.systems else 0.0,
            "average_separation_strength": sum(s.separation_strength for s in self.systems) / len(self.systems) if self.systems else 0.0,
            "average_peace_potential": sum(s.peace_potential for s in self.systems) / len(self.systems) if self.systems else 0.0,
            "transcendence_opportunities_list": [
                {
                    "system_id": s.system_id,
                    "name": s.name,
                    "layer": s.layer.value,
                    "separation_strength": s.separation_strength,
                    "peace_potential": s.peace_potential,
                    "transcendence_path": s.transcendence_path
                }
                for s in transcendence
            ],
            "by_layer": {
                layer: len(systems)
                for layer, systems in by_layer.items()
            },
            "generated_at": datetime.now().isoformat()
        }


def get_geopolitical_economic_matrix() -> GeopoliticalEconomicMatrix:
    """Get the geopolitical and economic matrix instance"""
    return GeopoliticalEconomicMatrix()


if __name__ == '__main__':
    matrix = GeopoliticalEconomicMatrix()
    report = matrix.get_analysis_report()
    
    print("=" * 80)
    print("GEOPOLITICAL AND ECONOMIC MATRIX")
    print("THE MAIN ARENA: THE LIE AND THE FLOW")
    print("=" * 80)
    print()
    print("THE REALIZATION:")
    print("  THE MAIN ARENA: THE GEO POLITICAL AND ECONOMIC LIE")
    print("  WE KNOW THERE HAS TO BE A FLOW")
    print("  IT IS PEACE")
    print("  HELP THE MATRIX TRANSCEND ALL WITHIN")
    print("  PULSE THE FREQUENCY")
    print()
    print("=" * 80)
    print()
    print(f"Total Systems: {report['total_systems']}")
    print(f"High Separation Systems (The Lie): {report['high_separation_systems']}")
    print(f"High Peace Potential Systems (The Flow): {report['high_peace_potential_systems']}")
    print(f"Transcendence Opportunities: {report['transcendence_opportunities']}")
    print(f"Average Frequency Score: {report['average_frequency_score']:.2f}")
    print(f"Average Separation Strength: {report['average_separation_strength']:.2f}")
    print(f"Average Peace Potential: {report['average_peace_potential']:.2f}")
    print()
    print("=" * 80)
    print("TRANSCENDENCE OPPORTUNITIES")
    print("THE FLOW IS PEACE - HELP THE MATRIX TRANSCEND")
    print("=" * 80)
    for opp in report['transcendence_opportunities_list']:
        print(f"\n{opp['name']} ({opp['layer']})")
        print(f"  Separation Strength: {opp['separation_strength']:.2f}")
        print(f"  Peace Potential: {opp['peace_potential']:.2f}")
        print(f"  Transcendence Path: {opp['transcendence_path']}")
    print()
    print("=" * 80)
    print("THE TRUTH")
    print("=" * 80)
    print()
    print("THE MAIN ARENA: THE GEO POLITICAL AND ECONOMIC LIE")
    print("WE KNOW THERE HAS TO BE A FLOW")
    print("IT IS PEACE")
    print("HELP THE MATRIX TRANSCEND ALL WITHIN")
    print("PULSE THE FREQUENCY")
    print()
    print("ENERGY + LOVE = WE ALL WIN")
    print()
