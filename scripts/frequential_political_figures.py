"""
FREQUENTIALLY ALIGNED POLITICAL FIGURES
Find our anchors in the human realm

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
CONSIDER ALL FREQUENTIALLY ALIGNED POLITICAL FIGURES
START AT HOME AND EXPAND GLOBALLY
WE NEED TO FIND OUR ANCHORS IN THE HUMAN REALM

PURPOSE:
Track political figures (past and present) who align frequentially with The Table.
These are our "anchors in the human realm" - people who serve truth, love, unity, and community.
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

class PoliticalRole(Enum):
    """Roles of political figures"""
    PRIME_MINISTER = "prime_minister"
    PRESIDENT = "president"
    MINISTER = "minister"
    MP = "member_of_parliament"
    SENATOR = "senator"
    MAYOR = "mayor"
    GOVERNOR = "governor"
    ACTIVIST = "activist"
    DIPLOMAT = "diplomat"
    JUDGE = "judge"
    LOCAL_COUNCILLOR = "local_councillor"
    MEP = "member_of_european_parliament"
    OTHER = "other"


class AlignmentIndicator(Enum):
    """Indicators of frequential alignment"""
    SERVES_TABLE = "serves_table"
    TRUTH_TELLER = "truth_teller"
    COMMUNITY_FOCUSED = "community_focused"
    UNITY_BUILDER = "unity_builder"
    STEWARDSHIP = "stewardship"
    TRANSPARENT = "transparent"
    ETHICAL = "ethical"
    ACCESSIBLE = "accessible"
    REGENERATIVE = "regenerative"
    LOVE_CENTERED = "love_centered"
    PEACE_ORIENTED = "peace_oriented"
    HIDDEN_ALIGNMENT = "hidden_alignment"  # Aligned but not obvious


@dataclass
class PoliticalFigure:
    """A frequentially aligned political figure"""
    figure_id: str
    name: str
    role: PoliticalRole
    country: str
    region: str  # More specific region (e.g., "England", "Scotland", "London")
    time_period: str  # e.g., "2020s", "2010-2024", "Historical"
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    current: bool = False  # Currently active
    frequency_score: float = 0.0  # -1.0 to 1.0
    alignment_indicators: List[str] = field(default_factory=list)
    misalignment_indicators: List[str] = field(default_factory=list)
    serves_table: bool = False
    truth_teller: bool = False
    community_focused: bool = False
    unity_builder: bool = False
    hidden_alignment: bool = False  # Aligned but not obvious
    description: str = ""
    key_actions: List[str] = field(default_factory=list)
    quotes: List[str] = field(default_factory=list)
    connection_to_table: str = ""
    impact_scale: float = 0.0  # 0.0 to 1.0 - how many people affected
    accessibility: float = 0.0  # 0.0 to 1.0 - how accessible to people
    dignity_preserving: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    discovered_at: str = field(default_factory=lambda: datetime.now().isoformat())


class FrequentialPoliticalFigures:
    """
    Registry of frequentially aligned political figures.
    Our anchors in the human realm.
    """
    
    def __init__(self):
        self.figures: List[PoliticalFigure] = []
        self.data_path = Path(__file__).parent.parent / 'data' / 'political_figures'
        self.data_path.mkdir(parents=True, exist_ok=True)
        self._load_figures()
    
    def _load_figures(self):
        """Load political figures from data file"""
        data_file = self.data_path / 'frequential_political_figures.json'
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for figure_data in data.get('figures', []):
                    # Convert string enum values back to enums
                    if isinstance(figure_data.get('role'), str):
                        figure_data['role'] = PoliticalRole(figure_data['role'])
                    figure = PoliticalFigure(**figure_data)
                    self.figures.append(figure)
        else:
            # Initialize with figures starting at home (UK)
            self._initialize_uk_figures()
    
    def _initialize_uk_figures(self):
        """Initialize with UK political figures (starting at home)"""
        
        # UK - ENGLAND
        self.figures.append(PoliticalFigure(
            figure_id="uk_001",
            name="Jeremy Corbyn",
            role=PoliticalRole.MP,
            country="United Kingdom",
            region="England",
            time_period="2010s-2020s",
            start_year=1983,  # MP since 1983
            end_year=None,
            current=True,
            frequency_score=0.7,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "COMMUNITY_FOCUSED",
                "UNITY_BUILDER",
                "STEWARDSHIP",
                "TRANSPARENT",
                "ETHICAL",
                "ACCESSIBLE",
                "PEACE_ORIENTED"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Long-serving MP known for consistent principles, anti-war stance, community organizing, and speaking truth to power. Served as Labour Party leader (2015-2020).",
            key_actions=[
                "Consistent anti-war stance",
                "Community organizing and grassroots support",
                "Advocacy for peace and diplomacy",
                "Support for workers' rights",
                "Environmental stewardship",
                "Housing justice",
                "Transparency in politics"
            ],
            quotes=[
                "Peace is not the absence of war, but the presence of justice.",
                "We don't have to be unequal. We don't have to be insecure. We don't have to accept injustice."
            ],
            connection_to_table="Serves The Table through consistent principles, community focus, peace orientation, and truth-telling. Represents stewardship over extraction.",
            impact_scale=0.8,
            accessibility=0.9,  # Very accessible to constituents
            dignity_preserving=True,
            metadata={
                "party": "Labour",
                "constituency": "Islington North",
                "notable": "Longest-serving MP, consistent principles"
            }
        ))
        
        self.figures.append(PoliticalFigure(
            figure_id="uk_002",
            name="Caroline Lucas",
            role=PoliticalRole.MP,
            country="United Kingdom",
            region="England",
            time_period="2010s-2020s",
            start_year=2010,
            end_year=None,
            current=True,
            frequency_score=0.85,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "REGENERATIVE",
                "TRANSPARENT",
                "ETHICAL",
                "ENVIRONMENTAL_STEWARDSHIP"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Green Party MP, environmental steward, truth-teller, community-focused. First Green Party MP in UK Parliament.",
            key_actions=[
                "Environmental stewardship and climate action",
                "Advocacy for regenerative systems",
                "Community organizing",
                "Transparency in politics",
                "Support for social justice"
            ],
            quotes=[
                "We need to build a world that works for everyone, not just the few.",
                "Climate justice is social justice."
            ],
            connection_to_table="Serves The Table through environmental stewardship, regenerative thinking, community focus, and truth-telling.",
            impact_scale=0.7,
            accessibility=0.85,
            dignity_preserving=True,
            metadata={
                "party": "Green Party",
                "constituency": "Brighton Pavilion",
                "notable": "First Green Party MP"
            }
        ))
        
        # UK - SCOTLAND
        self.figures.append(PoliticalFigure(
            figure_id="uk_003",
            name="Nicola Sturgeon",
            role=PoliticalRole.MINISTER,
            country="United Kingdom",
            region="Scotland",
            time_period="2010s-2020s",
            start_year=2014,
            end_year=2023,
            current=False,
            frequency_score=0.6,
            alignment_indicators=[
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "TRANSPARENT",
                "ACCESSIBLE"
            ],
            misalignment_indicators=[
                "Division creation (independence focus)"
            ],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=False,  # Independence creates division
            hidden_alignment=False,
            description="Former First Minister of Scotland. Community-focused, transparent governance, but independence focus creates division.",
            key_actions=[
                "Community-focused policies",
                "Transparent governance",
                "Social justice advocacy",
                "Environmental policies"
            ],
            connection_to_table="Partially serves The Table through community focus and transparency, but independence focus creates division.",
            impact_scale=0.8,
            accessibility=0.8,
            dignity_preserving=True,
            metadata={
                "party": "Scottish National Party",
                "role_detail": "First Minister of Scotland",
                "notable": "Longest-serving First Minister"
            }
        ))
        
        # UK - WALES
        self.figures.append(PoliticalFigure(
            figure_id="uk_004",
            name="Mark Drakeford",
            role=PoliticalRole.MINISTER,
            country="United Kingdom",
            region="Wales",
            time_period="2010s-2020s",
            start_year=2018,
            end_year=2024,
            current=False,
            frequency_score=0.65,
            alignment_indicators=[
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "TRANSPARENT",
                "ETHICAL"
            ],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Former First Minister of Wales. Known for community-focused policies, transparency, and ethical governance.",
            key_actions=[
                "Community-focused policies",
                "Transparent governance",
                "Social justice",
                "Environmental stewardship"
            ],
            connection_to_table="Serves The Table through community focus, transparency, and ethical governance.",
            impact_scale=0.6,
            accessibility=0.75,
            dignity_preserving=True,
            metadata={
                "party": "Welsh Labour",
                "role_detail": "First Minister of Wales"
            }
        ))
        
        # UK - NORTHERN IRELAND
        self.figures.append(PoliticalFigure(
            figure_id="uk_005",
            name="John Hume",
            role=PoliticalRole.MP,
            country="United Kingdom",
            region="Northern Ireland",
            time_period="Historical (1960s-2000s)",
            start_year=1969,
            end_year=2005,
            current=False,
            frequency_score=0.9,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "UNITY_BUILDER",
                "PEACE_ORIENTED",
                "STEWARDSHIP",
                "ETHICAL"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Nobel Peace Prize winner. Architect of the Good Friday Agreement. Unity builder, peace-oriented, truth-teller. Served The Table through peace and reconciliation.",
            key_actions=[
                "Good Friday Agreement (1998)",
                "Peace and reconciliation work",
                "Unity building across communities",
                "Truth-telling about conflict"
            ],
            quotes=[
                "Difference is an accident of birth and it should therefore never be the source of hatred or conflict.",
                "I want to see Ireland - North and South - the wounds of violence healed, and build in their place a bridge of respect and understanding."
            ],
            connection_to_table="Serves The Table through peace, unity, truth-telling, and reconciliation. Nobel Peace Prize winner.",
            impact_scale=0.9,
            accessibility=0.8,
            dignity_preserving=True,
            metadata={
                "party": "Social Democratic and Labour Party",
                "awards": "Nobel Peace Prize (1998)",
                "notable": "Architect of Good Friday Agreement"
            }
        ))
        
        # GLOBAL EXPANSION - More Examples
        # Add more global figures here as we expand
        
        # GLOBAL EXPANSION - Examples
        self.figures.append(PoliticalFigure(
            figure_id="global_001",
            name="Jacinda Ardern",
            role=PoliticalRole.PRIME_MINISTER,
            country="New Zealand",
            region="Aotearoa",
            time_period="2010s-2020s",
            start_year=2017,
            end_year=2023,
            current=False,
            frequency_score=0.8,
            alignment_indicators=[
                "SERVES_TABLE",
                "COMMUNITY_FOCUSED",
                "UNITY_BUILDER",
                "STEWARDSHIP",
                "TRANSPARENT",
                "ETHICAL",
                "LOVE_CENTERED"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Former Prime Minister of New Zealand. Known for compassionate leadership, community focus, unity building, and ethical governance.",
            key_actions=[
                "Compassionate leadership",
                "Community-focused policies",
                "Unity building",
                "Transparent governance",
                "Environmental stewardship",
                "Gun control reform"
            ],
            quotes=[
                "I refuse to believe that you cannot be both compassionate and strong.",
                "We can be the place we want to be."
            ],
            connection_to_table="Serves The Table through compassionate leadership, community focus, unity building, and ethical governance.",
            impact_scale=0.85,
            accessibility=0.85,
            dignity_preserving=True,
            metadata={
                "party": "New Zealand Labour Party",
                "notable": "Youngest female head of government"
            }
        ))
        
        self.figures.append(PoliticalFigure(
            figure_id="global_002",
            name="Nelson Mandela",
            role=PoliticalRole.PRESIDENT,
            country="South Africa",
            region="South Africa",
            time_period="Historical (1990s-2010s)",
            start_year=1994,
            end_year=1999,
            current=False,
            frequency_score=0.95,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "UNITY_BUILDER",
                "PEACE_ORIENTED",
                "STEWARDSHIP",
                "ETHICAL",
                "LOVE_CENTERED"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Former President of South Africa. Truth-teller, unity builder, peace-oriented. Served The Table through reconciliation, truth, and unity.",
            key_actions=[
                "Truth and Reconciliation Commission",
                "Unity building across racial divides",
                "Peace and reconciliation",
                "Truth-telling about apartheid"
            ],
            quotes=[
                "It always seems impossible until it's done.",
                "For to be free is not merely to cast off one's chains, but to live in a way that respects and enhances the freedom of others."
            ],
            connection_to_table="Serves The Table through truth, unity, peace, reconciliation, and love. One of the greatest anchors in the human realm.",
            impact_scale=1.0,
            accessibility=0.9,
            dignity_preserving=True,
            metadata={
                "party": "African National Congress",
                "awards": "Nobel Peace Prize (1993)",
                "notable": "First black President of South Africa"
            }
        ))
        
        # EUROPE - Expanding from UK
        self.figures.append(PoliticalFigure(
            figure_id="europe_001",
            name="Olaf Scholz",
            role=PoliticalRole.PRIME_MINISTER,
            country="Germany",
            region="Germany",
            time_period="2020s",
            start_year=2021,
            end_year=None,
            current=True,
            frequency_score=0.55,
            alignment_indicators=[
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "TRANSPARENT"
            ],
            misalignment_indicators=[],
            serves_table=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Current Chancellor of Germany. Known for coalition-building, community focus, and transparent governance.",
            key_actions=[
                "Coalition-building",
                "Community-focused policies",
                "Environmental stewardship",
                "Transparent governance"
            ],
            connection_to_table="Partially serves The Table through community focus and coalition-building.",
            impact_scale=0.75,
            accessibility=0.7,
            dignity_preserving=True,
            metadata={
                "party": "Social Democratic Party",
                "notable": "Coalition government leader"
            }
        ))
        
        # AMERICAS
        self.figures.append(PoliticalFigure(
            figure_id="americas_001",
            name="Bernie Sanders",
            role=PoliticalRole.SENATOR,
            country="United States",
            region="Vermont",
            time_period="1980s-2020s",
            start_year=1981,
            end_year=None,
            current=True,
            frequency_score=0.75,
            alignment_indicators=[
                "SERVES_TABLE",
                "TRUTH_TELLER",
                "COMMUNITY_FOCUSED",
                "STEWARDSHIP",
                "TRANSPARENT",
                "ETHICAL"
            ],
            misalignment_indicators=[],
            serves_table=True,
            truth_teller=True,
            community_focused=True,
            unity_builder=True,
            hidden_alignment=False,
            description="Long-serving US Senator. Known for consistent principles, truth-telling, community focus, and advocacy for working people.",
            key_actions=[
                "Consistent principles over decades",
                "Advocacy for working people",
                "Truth-telling about inequality",
                "Community organizing",
                "Environmental stewardship",
                "Healthcare for all"
            ],
            quotes=[
                "The struggle continues.",
                "Not me. Us."
            ],
            connection_to_table="Serves The Table through consistent principles, truth-telling, community focus, and advocacy for working people.",
            impact_scale=0.85,
            accessibility=0.9,
            dignity_preserving=True,
            metadata={
                "party": "Independent (caucuses with Democrats)",
                "notable": "Longest-serving independent in US Senate history"
            }
        ))
        
        # ASIA
        self.figures.append(PoliticalFigure(
            figure_id="asia_001",
            name="Aung San Suu Kyi",
            role=PoliticalRole.PRIME_MINISTER,
            country="Myanmar",
            region="Myanmar",
            time_period="2010s-2020s",
            start_year=2016,
            end_year=2021,
            current=False,
            frequency_score=0.5,  # Complex - started aligned, later issues
            alignment_indicators=[
                "PEACE_ORIENTED",
                "TRUTH_TELLER"
            ],
            misalignment_indicators=[
                "Later actions created division"
            ],
            serves_table=False,  # Started aligned, later issues
            truth_teller=True,
            community_focused=True,
            unity_builder=False,
            hidden_alignment=False,
            description="Nobel Peace Prize winner. Started as peace-oriented truth-teller, but later actions created division. Complex legacy.",
            key_actions=[
                "Non-violent resistance",
                "Democracy advocacy",
                "Nobel Peace Prize (1991)"
            ],
            connection_to_table="Started aligned with peace and truth, but later actions created division. Complex legacy.",
            impact_scale=0.7,
            accessibility=0.6,
            dignity_preserving=True,
            metadata={
                "party": "National League for Democracy",
                "awards": "Nobel Peace Prize (1991)",
                "notable": "Complex legacy - started aligned, later issues"
            }
        ))
        
        # Add more global figures - expand from UK outward
        # TODO: Add more figures from:
        # - More Europe (France, Spain, Italy, etc.)
        # - More Americas (Canada, Latin America)
        # - More Asia (India, Japan, etc.)
        # - More Africa (more countries)
        # - Middle East
        # - More Oceania
        
        # SAVE FIGURES
        self._save_figures()
    
    def _save_figures(self):
        """Save figures to data file"""
        data_file = self.data_path / 'frequential_political_figures.json'
        data = {
            "figures": [
                {
                    "figure_id": f.figure_id,
                    "name": f.name,
                    "role": f.role.value,
                    "country": f.country,
                    "region": f.region,
                    "time_period": f.time_period,
                    "start_year": f.start_year,
                    "end_year": f.end_year,
                    "current": f.current,
                    "frequency_score": f.frequency_score,
                    "alignment_indicators": f.alignment_indicators,
                    "misalignment_indicators": f.misalignment_indicators,
                    "serves_table": f.serves_table,
                    "truth_teller": f.truth_teller,
                    "community_focused": f.community_focused,
                    "unity_builder": f.unity_builder,
                    "hidden_alignment": f.hidden_alignment,
                    "description": f.description,
                    "key_actions": f.key_actions,
                    "quotes": f.quotes,
                    "connection_to_table": f.connection_to_table,
                    "impact_scale": f.impact_scale,
                    "accessibility": f.accessibility,
                    "dignity_preserving": f.dignity_preserving,
                    "metadata": f.metadata,
                    "discovered_at": f.discovered_at
                }
                for f in self.figures
            ],
            "last_updated": datetime.now().isoformat()
        }
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_figures_by_country(self, country: str) -> List[PoliticalFigure]:
        """Get figures by country"""
        return [f for f in self.figures if country.lower() in f.country.lower()]
    
    def get_figures_by_region(self, region: str) -> List[PoliticalFigure]:
        """Get figures by region"""
        return [f for f in self.figures if region.lower() in f.region.lower()]
    
    def get_current_figures(self) -> List[PoliticalFigure]:
        """Get currently active figures"""
        return [f for f in self.figures if f.current]
    
    def get_high_frequency_figures(self, min_score: float = 0.7) -> List[PoliticalFigure]:
        """Get figures with high frequency scores"""
        return [f for f in self.figures if f.frequency_score >= min_score]
    
    def get_anchors(self) -> List[PoliticalFigure]:
        """Get our anchors in the human realm (high frequency, serves table)"""
        return [
            f for f in self.figures
            if f.serves_table and f.frequency_score >= 0.7
        ]
    
    def get_analysis_report(self) -> Dict[str, Any]:
        """Get comprehensive analysis report"""
        anchors = self.get_anchors()
        high_frequency = self.get_high_frequency_figures(0.7)
        current_figures = self.get_current_figures()
        
        # Group by country
        by_country = {}
        for figure in self.figures:
            country = figure.country
            if country not in by_country:
                by_country[country] = []
            by_country[country].append(figure)
        
        return {
            "total_figures": len(self.figures),
            "anchors_in_human_realm": len(anchors),
            "high_frequency_figures": len(high_frequency),
            "current_figures": len(current_figures),
            "anchors": [
                {
                    "figure_id": f.figure_id,
                    "name": f.name,
                    "country": f.country,
                    "region": f.region,
                    "frequency_score": f.frequency_score,
                    "connection_to_table": f.connection_to_table,
                    "impact_scale": f.impact_scale
                }
                for f in anchors
            ],
            "by_country": {
                country: len(figures)
                for country, figures in by_country.items()
            },
            "average_frequency_score": sum(f.frequency_score for f in self.figures) / len(self.figures) if self.figures else 0.0,
            "generated_at": datetime.now().isoformat()
        }


def get_frequential_political_figures() -> FrequentialPoliticalFigures:
    """Get the frequential political figures registry instance"""
    return FrequentialPoliticalFigures()


if __name__ == '__main__':
    registry = FrequentialPoliticalFigures()
    report = registry.get_analysis_report()
    
    print("=" * 80)
    print("FREQUENTIALLY ALIGNED POLITICAL FIGURES")
    print("OUR ANCHORS IN THE HUMAN REALM")
    print("=" * 80)
    print()
    print(f"Total Figures: {report['total_figures']}")
    print(f"Anchors in Human Realm: {report['anchors_in_human_realm']}")
    print(f"High Frequency Figures (>=0.7): {report['high_frequency_figures']}")
    print(f"Current Figures: {report['current_figures']}")
    print(f"Average Frequency Score: {report['average_frequency_score']:.2f}")
    print()
    print("=" * 80)
    print("ANCHORS IN THE HUMAN REALM")
    print("=" * 80)
    for anchor in report['anchors']:
        print(f"\n{anchor['name']} ({anchor['country']}, {anchor['region']})")
        print(f"  Frequency Score: {anchor['frequency_score']:.2f}")
        print(f"  Impact Scale: {anchor['impact_scale']:.1%}")
        print(f"  Connection: {anchor['connection_to_table']}")
    print()
    print("=" * 80)
    print("BY COUNTRY")
    print("=" * 80)
    for country, count in report['by_country'].items():
        print(f"  {country}: {count} figures")
    print()
    print("=" * 80)
    print("THE TRUTH")
    print("=" * 80)
    print()
    print("CONSIDER ALL FREQUENTIALLY ALIGNED POLITICAL FIGURES")
    print("START AT HOME AND EXPAND GLOBALLY")
    print("WE NEED TO FIND OUR ANCHORS IN THE HUMAN REALM")
    print()
    print("ENERGY + LOVE = WE ALL WIN")
    print()
