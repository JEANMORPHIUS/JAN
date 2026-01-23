"""
ALIGNED INVESTMENTS
Specific Investment Projects for All Investors at All Levels

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

ALIGNED INVESTMENTS:
Specific investment projects aligned with The Table.
For all investors at all levels.
Starting with the man in the street.
Giving them tips.
Helping them invest in alignment.

THIS STARTS WITH US.
HELP THE MAN IN THE STREET.
GIVE THEM TIPS.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, date
from dataclasses import dataclass, field, asdict
from enum import Enum
import hashlib

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from aligned_entities_tracker import AlignedEntitiesTracker
    from vices_and_markets_tracker import VicesAndMarketsTracker
    from divine_frequency import DivineFrequencySystem
    SYSTEMS_AVAILABLE = True
except ImportError:
    SYSTEMS_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)


class InvestmentLevel(Enum):
    """Investment levels for different investors."""
    SMALL = "small"  # $1-$1,000 - The man in the street
    MEDIUM = "medium"  # $1,000-$10,000 - Growing investors
    LARGE = "large"  # $10,000-$100,000 - Established investors
    INSTITUTIONAL = "institutional"  # $100,000+ - Institutions


class InvestmentType(Enum):
    """Types of investments."""
    DIRECT = "direct"  # Direct investment in project/entity
    FUND = "fund"  # Investment fund
    COOPERATIVE = "cooperative"  # Cooperative membership
    CROWDFUNDING = "crowdfunding"  # Crowdfunding platform
    COMMUNITY = "community"  # Community investment
    IMPACT = "impact"  # Impact investment
    ESG = "esg"  # ESG investment
    DIVIDEND = "dividend"  # Dividend-paying investment
    GROWTH = "growth"  # Growth investment
    INCOME = "income"  # Income-generating investment


class RiskLevel(Enum):
    """Risk levels for investments."""
    VERY_LOW = "very_low"  # Very low risk
    LOW = "low"  # Low risk
    MODERATE = "moderate"  # Moderate risk
    HIGH = "high"  # High risk
    VERY_HIGH = "very_high"  # Very high risk


@dataclass
class InvestmentProject:
    """A specific investment project aligned with The Table."""
    project_id: str
    name: str
    description: str
    investment_type: str
    investment_level: str
    risk_level: str
    minimum_investment: float
    alignment_score: float  # 0.0 to 1.0
    frequency_contribution: float
    how_it_aligns: List[str] = field(default_factory=list)
    expected_return: Optional[str] = None
    time_horizon: Optional[str] = None
    liquidity: Optional[str] = None
    website: Optional[str] = None
    contact: Optional[str] = None
    tips: List[str] = field(default_factory=list)  # Tips for investors
    notes: str = ""


@dataclass
class InvestmentTip:
    """A tip for investors, especially the man in the street."""
    tip_id: str
    category: str
    title: str
    description: str
    for_level: str  # Investment level
    actionable: bool = True
    examples: List[str] = field(default_factory=list)
    notes: str = ""


class AlignedInvestments:
    """Track and recommend aligned investment projects."""
    
    def __init__(self):
        self.aligned_entities = AlignedEntitiesTracker() if SYSTEMS_AVAILABLE else None
        self.vices_tracker = VicesAndMarketsTracker() if SYSTEMS_AVAILABLE else None
        self.frequency_system = DivineFrequencySystem() if SYSTEMS_AVAILABLE else None
        self.projects: Dict[str, InvestmentProject] = {}
        self.tips: Dict[str, InvestmentTip] = {}
    
    def register_project(
        self,
        name: str,
        description: str,
        investment_type: str,
        investment_level: str,
        risk_level: str,
        minimum_investment: float,
        alignment_score: float,
        frequency_contribution: float = 0.0,
        how_it_aligns: List[str] = None,
        expected_return: Optional[str] = None,
        time_horizon: Optional[str] = None,
        liquidity: Optional[str] = None,
        website: Optional[str] = None,
        contact: Optional[str] = None,
        tips: List[str] = None,
        notes: str = ""
    ) -> InvestmentProject:
        """Register an aligned investment project."""
        project_id = f"project_{hashlib.sha256(name.encode()).hexdigest()[:8]}"
        
        project = InvestmentProject(
            project_id=project_id,
            name=name,
            description=description,
            investment_type=investment_type,
            investment_level=investment_level,
            risk_level=risk_level,
            minimum_investment=minimum_investment,
            alignment_score=alignment_score,
            frequency_contribution=frequency_contribution,
            how_it_aligns=how_it_aligns or [],
            expected_return=expected_return,
            time_horizon=time_horizon,
            liquidity=liquidity,
            website=website,
            contact=contact,
            tips=tips or [],
            notes=notes
        )
        
        self.projects[project_id] = project
        logger.info(f"Registered investment project: {name} ({investment_level}, min: ${minimum_investment:.2f})")
        return project
    
    def register_tip(
        self,
        category: str,
        title: str,
        description: str,
        for_level: str,
        actionable: bool = True,
        examples: List[str] = None,
        notes: str = ""
    ) -> InvestmentTip:
        """Register an investment tip."""
        tip_id = f"tip_{hashlib.sha256(title.encode()).hexdigest()[:8]}"
        
        tip = InvestmentTip(
            tip_id=tip_id,
            category=category,
            title=title,
            description=description,
            for_level=for_level,
            actionable=actionable,
            examples=examples or [],
            notes=notes
        )
        
        self.tips[tip_id] = tip
        logger.info(f"Registered investment tip: {title} ({for_level})")
        return tip
    
    def get_projects_by_level(self, level: str) -> List[InvestmentProject]:
        """Get projects for a specific investment level."""
        return [p for p in self.projects.values() if p.investment_level == level]
    
    def get_projects_by_type(self, investment_type: str) -> List[InvestmentProject]:
        """Get projects of a specific type."""
        return [p for p in self.projects.values() if p.investment_type == investment_type]
    
    def get_tips_for_level(self, level: str) -> List[InvestmentTip]:
        """Get tips for a specific investment level."""
        return [t for t in self.tips.values() if t.for_level == level]
    
    def get_investment_guide(self, level: str) -> Dict[str, Any]:
        """Get complete investment guide for a level."""
        projects = self.get_projects_by_level(level)
        tips = self.get_tips_for_level(level)
        
        return {
            "level": level,
            "total_projects": len(projects),
            "total_tips": len(tips),
            "projects": [
                {
                    "name": p.name,
                    "description": p.description,
                    "investment_type": p.investment_type,
                    "risk_level": p.risk_level,
                    "minimum_investment": p.minimum_investment,
                    "alignment_score": p.alignment_score,
                    "tips": p.tips
                }
                for p in projects
            ],
            "tips": [
                {
                    "category": t.category,
                    "title": t.title,
                    "description": t.description,
                    "actionable": t.actionable,
                    "examples": t.examples
                }
                for t in tips
            ]
        }
    
    def get_complete_analysis(self) -> Dict[str, Any]:
        """Get complete investment analysis."""
        return {
            "analysis_timestamp": datetime.now().isoformat(),
            "total_projects": len(self.projects),
            "total_tips": len(self.tips),
            "projects_by_level": {
                level.value: len(self.get_projects_by_level(level.value))
                for level in InvestmentLevel
            },
            "projects_by_type": {
                itype.value: len(self.get_projects_by_type(itype.value))
                for itype in InvestmentType
            },
            "all_projects": [asdict(p) for p in self.projects.values()],
            "all_tips": [asdict(t) for t in self.tips.values()],
            "investment_guides": {
                level.value: self.get_investment_guide(level.value)
                for level in InvestmentLevel
            },
            "the_truth": {
                "message": "THIS STARTS WITH US. HELP THE MAN IN THE STREET. GIVE THEM TIPS.",
                "alignment": "All investments must align with The Table. They serve, not exploit.",
                "purpose": "Help all investors at all levels invest in alignment with The Table."
            }
        }
    
    def export_analysis(self, output_path: Optional[Path] = None) -> Path:
        """Export complete investment analysis."""
        if output_path is None:
            output_path = Path(__file__).parent.parent / "output" / "aligned_investments" / f"investment_guide_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        analysis = self.get_complete_analysis()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, default=str)
        
        logger.info(f"Investment guide exported to {output_path}")
        return output_path


def main():
    """Main execution for aligned investments."""
    print("=" * 80)
    print("ALIGNED INVESTMENTS")
    print("Specific Investment Projects for All Investors at All Levels")
    print("THIS STARTS WITH US. HELP THE MAN IN THE STREET. GIVE THEM TIPS.")
    print("=" * 80)
    print()
    
    investments = AlignedInvestments()
    
    # Register investment projects for SMALL investors (The man in the street)
    print("Registering investment projects for SMALL investors ($1-$1,000)...")
    
    investments.register_project(
        name="Local Credit Union Savings Account",
        description="Open a savings account at a local credit union - member-owned, not profit-driven",
        investment_type=InvestmentType.COOPERATIVE.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.VERY_LOW.value,
        minimum_investment=1.0,
        alignment_score=0.84,
        frequency_contribution=0.01,
        how_it_aligns=["Member ownership", "No exploitation", "Community service", "Unity"],
        expected_return="2-3% APY",
        time_horizon="Flexible",
        liquidity="High - withdraw anytime",
        tips=[
            "Start with $25-50 if that's what you have",
            "Set up automatic transfers of $10-20/month",
            "Credit unions are member-owned, not profit-driven",
            "Your money stays in your community"
        ],
        notes="Perfect starting point for the man in the street"
    )
    
    investments.register_project(
        name="Community Solar Cooperative",
        description="Join a community solar cooperative - own a share of local solar energy",
        investment_type=InvestmentType.COOPERATIVE.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.LOW.value,
        minimum_investment=100.0,
        alignment_score=0.88,
        frequency_contribution=0.02,
        how_it_aligns=["Community ownership", "Renewable energy", "No exploitation", "Stewardship"],
        expected_return="5-8% annually",
        time_horizon="5-10 years",
        liquidity="Moderate - can sell share",
        tips=[
            "Start with $100-500 if possible",
            "Reduces your electricity bill",
            "Supports renewable energy",
            "Community-owned, not corporate"
        ],
        notes="Community solar aligns with Earth stewardship"
    )
    
    investments.register_project(
        name="Local Food Cooperative Membership",
        description="Join a local food cooperative - support local farmers, get better food",
        investment_type=InvestmentType.COOPERATIVE.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.VERY_LOW.value,
        minimum_investment=50.0,
        alignment_score=0.85,
        frequency_contribution=0.01,
        how_it_aligns=["Community support", "Local economy", "No exploitation", "Unity"],
        expected_return="10-20% discount on food",
        time_horizon="Ongoing",
        liquidity="High - can withdraw membership",
        tips=[
            "Start with $50-100 membership",
            "Get discounts on food",
            "Support local farmers",
            "Build community connections"
        ],
        notes="Food co-ops support local communities"
    )
    
    investments.register_project(
        name="Micro-Lending to Aligned Businesses",
        description="Lend small amounts to aligned businesses through micro-lending platforms",
        investment_type=InvestmentType.IMPACT.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.MODERATE.value,
        minimum_investment=25.0,
        alignment_score=0.86,
        frequency_contribution=0.02,
        how_it_aligns=["Support aligned businesses", "Community service", "No exploitation", "Unity"],
        expected_return="4-6% annually",
        time_horizon="1-3 years",
        liquidity="Low - locked until repayment",
        tips=[
            "Start with $25-100",
            "Diversify across multiple loans",
            "Support aligned businesses",
            "Help others while earning"
        ],
        notes="Micro-lending supports aligned businesses"
    )
    
    investments.register_project(
        name="Homeless Support Organizations - Direct Donation",
        description="Direct donations to organizations providing housing and meals for the homeless",
        investment_type=InvestmentType.IMPACT.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.VERY_LOW.value,
        minimum_investment=1.0,
        alignment_score=0.95,
        frequency_contribution=0.05,
        how_it_aligns=["NO ONE GETS LEFT BEHIND", "Roof over head", "Hot meal a day", "Community service", "Unity"],
        expected_return="Lives changed, community strengthened",
        time_horizon="Immediate impact",
        liquidity="N/A - donation",
        tips=[
            "Start with $1-10 if that's what you have",
            "Set up monthly recurring donation of $5-25",
            "Research local homeless shelters and food programs",
            "May the Lord give them a roof over their head and one hot meal a day",
            "Every dollar helps - even $1 provides a meal"
        ],
        notes="NO ONE GETS LEFT BEHIND. May the Lord give them a roof over their head and one hot meal a day."
    )
    
    investments.register_project(
        name="Housing First Programs",
        description="Support Housing First programs that provide permanent housing for the homeless",
        investment_type=InvestmentType.IMPACT.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.VERY_LOW.value,
        minimum_investment=10.0,
        alignment_score=0.94,
        frequency_contribution=0.08,
        how_it_aligns=["NO ONE GETS LEFT BEHIND", "Roof over head", "Permanent housing", "Community service", "Unity"],
        expected_return="Lives transformed, community strengthened",
        time_horizon="Ongoing support",
        liquidity="N/A - donation",
        tips=[
            "Start with $10-50 monthly",
            "Housing First programs are proven effective",
            "Provides permanent housing, not just shelter",
            "May the Lord give them a roof over their head"
        ],
        notes="Housing First provides permanent housing - highest alignment with NO ONE GETS LEFT BEHIND"
    )
    
    investments.register_project(
        name="Community Meal Programs",
        description="Support community meal programs providing hot meals for the homeless",
        investment_type=InvestmentType.IMPACT.value,
        investment_level=InvestmentLevel.SMALL.value,
        risk_level=RiskLevel.VERY_LOW.value,
        minimum_investment=5.0,
        alignment_score=0.93,
        frequency_contribution=0.04,
        how_it_aligns=["NO ONE GETS LEFT BEHIND", "Hot meal a day", "Community service", "Unity"],
        expected_return="Lives nourished, community strengthened",
        time_horizon="Ongoing support",
        liquidity="N/A - donation",
        tips=[
            "Start with $5-20 monthly",
            "$5 can provide one hot meal",
            "Support local soup kitchens and meal programs",
            "May the Lord give them one hot meal a day",
            "Volunteer time if you can't donate money"
        ],
        notes="Community meal programs provide hot meals - one hot meal a day"
    )
    
    print(f"  [OK] {len([p for p in investments.projects.values() if p.investment_level == InvestmentLevel.SMALL.value])} projects for SMALL investors")
    print()
    
    # Register investment tips for SMALL investors
    print("Registering investment tips for SMALL investors...")
    
    investments.register_tip(
        category="Getting Started",
        title="Start Where You Are",
        description="You don't need thousands to start. Start with what you have, even if it's $10.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "Open a credit union savings account with $25",
            "Set up automatic $10/month transfers",
            "Join a food co-op with $50",
            "Start a small emergency fund"
        ],
        notes="The man in the street can start small"
    )
    
    investments.register_tip(
        category="Building Wealth",
        title="Pay Yourself First",
        description="Before paying bills, pay yourself. Even $10/month adds up.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "Set up automatic transfer on payday",
            "Start with $10/month, increase when you can",
            "Treat savings like a bill",
            "Watch it grow over time"
        ],
        notes="Small amounts compound over time"
    )
    
    investments.register_tip(
        category="Avoiding Exploitation",
        title="Avoid High-Fee Investments",
        description="Avoid investments with high fees - they drain your money. Look for low-fee options.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "Credit unions have lower fees than banks",
            "Avoid investment products with 2%+ fees",
            "Look for no-fee or low-fee options",
            "Read the fine print on fees"
        ],
        notes="High fees are exploitation"
    )
    
    investments.register_tip(
        category="Community Investment",
        title="Invest in Your Community",
        description="Invest in your local community - credit unions, co-ops, local businesses.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "Join a credit union",
            "Join a food co-op",
            "Support local businesses",
            "Invest in community solar"
        ],
        notes="Community investment builds unity"
    )
    
    investments.register_tip(
        category="Alignment",
        title="Invest in Alignment",
        description="Invest in things that align with The Table - they serve, not exploit.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "Credit unions (member-owned)",
            "Co-ops (community-owned)",
            "Renewable energy",
            "Local businesses"
        ],
        notes="Alignment means serving The Table"
    )
    
    investments.register_tip(
        category="Homeless Support",
        title="Help the Homeless - NO ONE GETS LEFT BEHIND",
        description="Support the homeless. May the Lord give them a roof over their head and one hot meal a day.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "Donate $1-10 to local homeless shelter",
            "Set up $5-25/month recurring donation",
            "Support Housing First programs",
            "Support community meal programs",
            "Volunteer time if you can't donate money",
            "Even $1 provides a meal"
        ],
        notes="NO ONE GETS LEFT BEHIND. May the Lord give them a roof over their head and one hot meal a day."
    )
    
    investments.register_tip(
        category="Homeless Support",
        title="Start Small - Every Dollar Helps",
        description="You don't need much to help. Even $1 provides a meal. Even $5 helps.",
        for_level=InvestmentLevel.SMALL.value,
        actionable=True,
        examples=[
            "$1 can provide a meal",
            "$5 can provide 5 meals",
            "$10 can provide shelter for a night",
            "$25 can provide a week of meals",
            "Start with what you have"
        ],
        notes="Every dollar helps. Start with what you have."
    )
    
    print(f"  [OK] {len([t for t in investments.tips.values() if t.for_level == InvestmentLevel.SMALL.value])} tips for SMALL investors")
    print()
    
    # Register projects for MEDIUM investors
    print("Registering investment projects for MEDIUM investors ($1,000-$10,000)...")
    
    investments.register_project(
        name="Impact Investment Fund",
        description="Invest in impact investment funds that support aligned businesses",
        investment_type=InvestmentType.IMPACT.value,
        investment_level=InvestmentLevel.MEDIUM.value,
        risk_level=RiskLevel.MODERATE.value,
        minimum_investment=1000.0,
        alignment_score=0.85,
        frequency_contribution=0.05,
        how_it_aligns=["Positive impact", "No exploitation", "Social good", "Stewardship"],
        expected_return="6-10% annually",
        time_horizon="5-10 years",
        liquidity="Moderate",
        tips=[
            "Start with $1,000-5,000",
            "Diversify across multiple funds",
            "Look for low-fee impact funds",
            "Support aligned businesses"
        ],
        notes="Impact investing aligns capital with positive outcomes"
    )
    
    investments.register_project(
        name="ESG Index Fund",
        description="Invest in ESG (Environmental, Social, Governance) index funds",
        investment_type=InvestmentType.ESG.value,
        investment_level=InvestmentLevel.MEDIUM.value,
        risk_level=RiskLevel.MODERATE.value,
        minimum_investment=1000.0,
        alignment_score=0.82,
        frequency_contribution=0.04,
        how_it_aligns=["ESG criteria", "No exploitation", "Social good", "Stewardship"],
        expected_return="7-10% annually",
        time_horizon="5-10 years",
        liquidity="High",
        tips=[
            "Start with $1,000-3,000",
            "Look for low-fee ESG funds",
            "Diversify across sectors",
            "Long-term growth focus"
        ],
        notes="ESG funds align with The Table"
    )
    
    investments.register_project(
        name="Community Development Financial Institution (CDFI) Investment",
        description="Invest in CDFIs that serve underserved communities",
        investment_type=InvestmentType.IMPACT.value,
        investment_level=InvestmentLevel.MEDIUM.value,
        risk_level=RiskLevel.LOW.value,
        minimum_investment=1000.0,
        alignment_score=0.86,
        frequency_contribution=0.05,
        how_it_aligns=["Community service", "No exploitation", "Financial inclusion", "Unity"],
        expected_return="2-4% annually",
        time_horizon="3-5 years",
        liquidity="Low",
        tips=[
            "Start with $1,000-5,000",
            "Support underserved communities",
            "Low risk, community impact",
            "Helps others while earning"
        ],
        notes="CDFIs serve communities without exploitation"
    )
    
    print(f"  [OK] {len([p for p in investments.projects.values() if p.investment_level == InvestmentLevel.MEDIUM.value])} projects for MEDIUM investors")
    print()
    
    # Register projects for LARGE investors
    print("Registering investment projects for LARGE investors ($10,000-$100,000)...")
    
    investments.register_project(
        name="Direct Investment in Aligned Businesses",
        description="Direct investment in aligned businesses (renewable energy, co-ops, etc.)",
        investment_type=InvestmentType.DIRECT.value,
        investment_level=InvestmentLevel.LARGE.value,
        risk_level=RiskLevel.HIGH.value,
        minimum_investment=10000.0,
        alignment_score=0.88,
        frequency_contribution=0.10,
        how_it_aligns=["Direct alignment", "No exploitation", "Community service", "Stewardship"],
        expected_return="8-15% annually",
        time_horizon="5-10 years",
        liquidity="Low",
        tips=[
            "Start with $10,000-25,000",
            "Diversify across multiple businesses",
            "Do due diligence",
            "Support aligned businesses"
        ],
        notes="Direct investment in aligned businesses"
    )
    
    investments.register_project(
        name="Renewable Energy Infrastructure Fund",
        description="Invest in renewable energy infrastructure funds",
        investment_type=InvestmentType.FUND.value,
        investment_level=InvestmentLevel.LARGE.value,
        risk_level=RiskLevel.MODERATE.value,
        minimum_investment=10000.0,
        alignment_score=0.88,
        frequency_contribution=0.10,
        how_it_aligns=["Renewable energy", "No exploitation", "Stewardship", "Earth restoration"],
        expected_return="7-12% annually",
        time_horizon="10+ years",
        liquidity="Moderate",
        tips=[
            "Start with $10,000-50,000",
            "Long-term investment",
            "Supports renewable energy",
            "Earth stewardship"
        ],
        notes="Renewable energy aligns with Earth stewardship"
    )
    
    print(f"  [OK] {len([p for p in investments.projects.values() if p.investment_level == InvestmentLevel.LARGE.value])} projects for LARGE investors")
    print()
    
    # Get guides
    print("Generating investment guides...")
    small_guide = investments.get_investment_guide(InvestmentLevel.SMALL.value)
    print(f"  [OK] SMALL investor guide: {small_guide['total_projects']} projects, {small_guide['total_tips']} tips")
    print()
    
    # Export
    print("Exporting investment guide...")
    export_path = investments.export_analysis()
    print(f"  [OK] Exported to: {export_path}")
    print()
    
    print("=" * 80)
    print("THE TRUTH: ALIGNED INVESTMENTS")
    print("=" * 80)
    print()
    print("THIS STARTS WITH US.")
    print("HELP THE MAN IN THE STREET.")
    print("GIVE THEM TIPS.")
    print()
    print("INVESTMENT LEVELS:")
    print("  - SMALL ($1-$1,000): The man in the street")
    print("  - MEDIUM ($1,000-$10,000): Growing investors")
    print("  - LARGE ($10,000-$100,000): Established investors")
    print("  - INSTITUTIONAL ($100,000+): Institutions")
    print()
    print("ALIGNMENT:")
    print("  - All investments align with The Table")
    print("  - They serve, not exploit")
    print("  - They support restoration")
    print("  - They contribute to Divine Frequency")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("THIS STARTS WITH US")
    print("HELP THE MAN IN THE STREET")
    print("=" * 80)


if __name__ == "__main__":
    main()
