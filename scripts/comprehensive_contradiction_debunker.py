"""COMPREHENSIVE CONTRADICTION DEBUNKER
Fully debunk everything that might try to contradict us

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
DEBUNK ALL CONTRADICTIONS
EXPOSE ALL LIES
RESTORE ALL TRUTH
WE ARE ONE - NO CONTRADICTION CAN STAND

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    JAN_DATA, JAN_OUTPUT, get_data_path, get_output_path,
    datetime, json, logging, List, Dict, Optional, Any,
    setup_logging, load_json, save_json, standard_main,
    dataclass, field, asdict
)

from enum import Enum
import re

logger = setup_logging(__name__)

class ContradictionType(Enum):
    """Types of contradictions to debunk"""
    TRUTH_VS_LIE = "truth_vs_lie"
    SYSTEM_CONTRADICTION = "system_contradiction"
    NARRATIVE_CONTRADICTION = "narrative_contradiction"
    PHILOSOPHICAL_CONTRADICTION = "philosophical_contradiction"
    SPIRITUAL_CONTRADICTION = "spiritual_contradiction"
    ECONOMIC_CONTRADICTION = "economic_contradiction"
    POLITICAL_CONTRADICTION = "political_contradiction"
    SOCIAL_CONTRADICTION = "social_contradiction"
    ENVIRONMENTAL_CONTRADICTION = "environmental_contradiction"

class ContradictionStatus(Enum):
    """Status of contradiction debunking"""
    IDENTIFIED = "identified"
    DEBUNKED = "debunked"
    REFUTED = "refuted"
    EXPOSED = "exposed"
    ARCHIVED = "archived"

@dataclass
class Contradiction:
    """A contradiction that must be debunked"""
    contradiction_id: str
    contradiction_type: ContradictionType
    source: str  # Where it comes from
    claim: str  # The contradictory claim
    our_truth: str  # Our truth that contradicts it
    debunking_evidence: List[str] = field(default_factory=list)
    refutation_points: List[str] = field(default_factory=list)
    status: ContradictionStatus = ContradictionStatus.IDENTIFIED
    debunked_date: Optional[str] = None
    debunked_by: Optional[str] = None
    impact_level: float = 0.0  # 0.0 to 1.0
    frequency_score: float = 0.0  # -1.0 (dark) to 1.0 (light)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class DebunkingResponse:
    """A debunking response to a contradiction"""
    response_id: str
    contradiction_id: str
    response_type: str  # "refutation", "exposure", "truth_restoration"
    response_text: str
    evidence: List[str] = field(default_factory=list)
    truth_statements: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

class ComprehensiveContradictionDebunker:
    """
    Comprehensive system to debunk all contradictions.
    Exposes lies, restores truth, ensures nothing contradicts us.
    """
    
    def __init__(self):
        self.data_dir = get_data_path("contradiction_debunking")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.contradictions_file = self.data_dir / "contradictions.json"
        self.debunking_responses_file = self.data_dir / "debunking_responses.json"
        self.truth_statements_file = get_data_path("one_truth") / "one_truth_statements.json"
        
        self.contradictions: Dict[str, Contradiction] = {}
        self.debunking_responses: Dict[str, DebunkingResponse] = {}
        self.truth_statements: List[Dict[str, Any]] = []
        
        self.load_data()
        self.load_truth_statements()
    
    def load_data(self):
        """Load existing data"""
        if self.contradictions_file.exists():
            data = load_json(self.contradictions_file, default={})
            for cont_id, cont_data in data.items():
                cont_data['contradiction_type'] = ContradictionType(cont_data['contradiction_type'])
                cont_data['status'] = ContradictionStatus(cont_data['status'])
                self.contradictions[cont_id] = Contradiction(**cont_data)
        
        if self.debunking_responses_file.exists():
            data = load_json(self.debunking_responses_file, default={})
            for resp_id, resp_data in data.items():
                self.debunking_responses[resp_id] = DebunkingResponse(**resp_data)
    
    def load_truth_statements(self):
        """Load truth statements for debunking"""
        if self.truth_statements_file.exists():
            data = load_json(self.truth_statements_file, default={})
            self.truth_statements = data.get('statements', [])
    
    def save_data(self):
        """Save all data"""
        contradictions_dict = {
            cont_id: {
                **asdict(cont),
                'contradiction_type': cont.contradiction_type.value,
                'status': cont.status.value
            }
            for cont_id, cont in self.contradictions.items()
        }
        save_json(contradictions_dict, self.contradictions_file)
        
        responses_dict = {
            resp_id: asdict(resp)
            for resp_id, resp in self.debunking_responses.items()
        }
        save_json(responses_dict, self.debunking_responses_file)
    
    def identify_contradiction(
        self,
        contradiction_id: str,
        contradiction_type: ContradictionType,
        source: str,
        claim: str,
        our_truth: str,
        **kwargs
    ) -> Contradiction:
        """Identify a new contradiction"""
        contradiction = Contradiction(
            contradiction_id=contradiction_id,
            contradiction_type=contradiction_type,
            source=source,
            claim=claim,
            our_truth=our_truth,
            **kwargs
        )
        self.contradictions[contradiction_id] = contradiction
        self.save_data()
        logger.info(f"Identified contradiction: {contradiction_id}")
        return contradiction
    
    def debunk_contradiction(
        self,
        contradiction_id: str,
        debunking_evidence: List[str],
        refutation_points: List[str],
        debunked_by: str = "System"
    ) -> DebunkingResponse:
        """Debunk a contradiction"""
        if contradiction_id not in self.contradictions:
            logger.error(f"Contradiction not found: {contradiction_id}")
            return None
        
        cont = self.contradictions[contradiction_id]
        cont.status = ContradictionStatus.DEBUNKED
        cont.debunked_date = datetime.now().isoformat()
        cont.debunked_by = debunked_by
        cont.debunking_evidence = debunking_evidence
        cont.refutation_points = refutation_points
        cont.updated_at = datetime.now().isoformat()
        
        # Create debunking response
        response_id = f"{contradiction_id}_debunk_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        response = DebunkingResponse(
            response_id=response_id,
            contradiction_id=contradiction_id,
            response_type="refutation",
            response_text=self._generate_debunking_text(cont, debunking_evidence, refutation_points),
            evidence=debunking_evidence,
            truth_statements=[cont.our_truth]
        )
        self.debunking_responses[response_id] = response
        
        self.save_data()
        logger.info(f"Debunked contradiction: {contradiction_id}")
        return response
    
    def _generate_debunking_text(
        self,
        contradiction: Contradiction,
        evidence: List[str],
        refutation_points: List[str]
    ) -> str:
        """Generate debunking text"""
        text = f"DEBUNKED: {contradiction.claim}\n\n"
        text += f"SOURCE: {contradiction.source}\n"
        text += f"OUR TRUTH: {contradiction.our_truth}\n\n"
        
        if refutation_points:
            text += "REFUTATION POINTS:\n"
            for i, point in enumerate(refutation_points, 1):
                text += f"{i}. {point}\n"
        
        if evidence:
            text += "\nEVIDENCE:\n"
            for i, ev in enumerate(evidence, 1):
                text += f"{i}. {ev}\n"
        
        return text
    
    def find_matching_truth(self, claim: str) -> Optional[Dict[str, Any]]:
        """Find matching truth statement for a claim"""
        claim_lower = claim.lower()
        
        for truth in self.truth_statements:
            statement = truth.get('statement', '').lower()
            # Check if claim contradicts this truth
            if any(word in claim_lower for word in statement.split() if len(word) > 3):
                return truth
        
        return None
    
    def auto_debunk(self, claim: str, source: str = "Unknown") -> Optional[DebunkingResponse]:
        """Automatically debunk a claim by matching against truth statements"""
        matching_truth = self.find_matching_truth(claim)
        
        if matching_truth:
            contradiction_id = f"auto_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Determine contradiction type
            category = matching_truth.get('category', 'social')
            cont_type_map = {
                'geopolitical': ContradictionType.POLITICAL_CONTRADICTION,
                'economic': ContradictionType.ECONOMIC_CONTRADICTION,
                'social': ContradictionType.SOCIAL_CONTRADICTION,
                'spiritual': ContradictionType.SPIRITUAL_CONTRADICTION,
                'judicial': ContradictionType.SYSTEM_CONTRADICTION
            }
            cont_type = cont_type_map.get(category, ContradictionType.TRUTH_VS_LIE)
            
            contradiction = self.identify_contradiction(
                contradiction_id=contradiction_id,
                contradiction_type=cont_type,
                source=source,
                claim=claim,
                our_truth=matching_truth.get('statement', ''),
                impact_level=0.5,
                frequency_score=-0.5  # Contradictions are dark energy
            )
            
            # Auto-debunk with truth statement
            evidence = [matching_truth.get('simple_explanation', '')]
            refutation_points = [matching_truth.get('how_to_align', '')]
            
            return self.debunk_contradiction(
                contradiction_id,
                evidence,
                refutation_points,
                debunked_by="Auto-Debunker"
            )
        
        return None
    
    def generate_debunking_report(self) -> Dict[str, Any]:
        """Generate comprehensive debunking report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_contradictions': len(self.contradictions),
                'debunked': len([c for c in self.contradictions.values() if c.status == ContradictionStatus.DEBUNKED]),
                'identified': len([c for c in self.contradictions.values() if c.status == ContradictionStatus.IDENTIFIED]),
                'total_responses': len(self.debunking_responses)
            },
            'by_type': {},
            'by_status': {},
            'high_impact': [],
            'recent_debunks': []
        }
        
        # Group by type
        for cont in self.contradictions.values():
            cont_type = cont.contradiction_type.value
            if cont_type not in report['by_type']:
                report['by_type'][cont_type] = 0
            report['by_type'][cont_type] += 1
        
        # Group by status
        for cont in self.contradictions.values():
            status = cont.status.value
            if status not in report['by_status']:
                report['by_status'][status] = 0
            report['by_status'][status] += 1
        
        # High impact
        report['high_impact'] = [
            {
                'id': cont.contradiction_id,
                'claim': cont.claim,
                'source': cont.source,
                'impact_level': cont.impact_level
            }
            for cont in self.contradictions.values()
            if cont.impact_level > 0.7
        ]
        
        # Recent debunks
        recent = sorted(
            [c for c in self.contradictions.values() if c.debunked_date],
            key=lambda x: x.debunked_date or '',
            reverse=True
        )[:10]
        
        report['recent_debunks'] = [
            {
                'id': cont.contradiction_id,
                'claim': cont.claim,
                'debunked_date': cont.debunked_date,
                'our_truth': cont.our_truth
            }
            for cont in recent
        ]
        
        return report
    
    def print_report(self, report: Dict[str, Any]):
        """Print debunking report"""
        print("\n" + "="*80)
        print("COMPREHENSIVE CONTRADICTION DEBUNKING REPORT")
        print("="*80)
        print(f"\nTotal Contradictions: {report['summary']['total_contradictions']}")
        print(f"  Debunked: {report['summary']['debunked']}")
        print(f"  Identified: {report['summary']['identified']}")
        print(f"  Total Responses: {report['summary']['total_responses']}")
        
        if report['by_type']:
            print(f"\nBy Type:")
            for cont_type, count in report['by_type'].items():
                print(f"  {cont_type}: {count}")
        
        if report['high_impact']:
            print(f"\nHigh Impact Contradictions ({len(report['high_impact'])}):")
            for item in report['high_impact'][:5]:
                print(f"  - {item['claim'][:60]}... (Impact: {item['impact_level']:.2f})")
        
        if report['recent_debunks']:
            print(f"\nRecent Debunks ({len(report['recent_debunks'])}):")
            for item in report['recent_debunks'][:5]:
                print(f"  - {item['claim'][:60]}...")
                print(f"    Truth: {item['our_truth'][:60]}...")


def initialize_common_contradictions(debunker: ComprehensiveContradictionDebunker):
    """Initialize common contradictions that must be debunked"""
    logger.info("Initializing common contradictions...")
    
    # Economic Contradictions
    debunker.identify_contradiction(
        contradiction_id="econ_scarcity_lie",
        contradiction_type=ContradictionType.ECONOMIC_CONTRADICTION,
        source="Economic Systems",
        claim="Scarcity is real. We must compete for resources.",
        our_truth="Abundance is the truth. Scarcity is the lie.",
        impact_level=0.9,
        frequency_score=-0.8,
        debunking_evidence=[
            "Energy is abundant (sun, wind, water, Earth)",
            "Scarcity is manufactured for profit",
            "Natural abundance exists everywhere"
        ],
        refutation_points=[
            "Recognize natural abundance",
            "Reject manufactured scarcity",
            "Share resources freely",
            "Build commons"
        ]
    )
    
    # Political Contradictions
    debunker.identify_contradiction(
        contradiction_id="pol_1_percent_rule",
        contradiction_type=ContradictionType.POLITICAL_CONTRADICTION,
        source="Power Structures",
        claim="The 1% rule the masses. This is how it works.",
        our_truth="The 1% no longer rule the masses. We are one.",
        impact_level=1.0,
        frequency_score=-0.9,
        debunking_evidence=[
            "Unity is the truth. Division is the lie.",
            "We are one - no separation can hold",
            "Power structures depend on division"
        ],
        refutation_points=[
            "Recognize we are one",
            "Reject division",
            "Support unity over separation",
            "Build community power"
        ]
    )
    
    # System Contradictions
    debunker.identify_contradiction(
        contradiction_id="sys_punishment_justice",
        contradiction_type=ContradictionType.SYSTEM_CONTRADICTION,
        source="Judicial Systems",
        claim="Punishment is justice. Criminals must be punished.",
        our_truth="Restoration is the truth. Punishment is the lie.",
        impact_level=0.8,
        frequency_score=-0.7,
        debunking_evidence=[
            "Punishment creates more brokenness",
            "Restoration creates healing",
            "Community justice serves truth"
        ],
        refutation_points=[
            "Choose restoration over punishment",
            "Support healing over control",
            "Build community justice councils",
            "Create restoration contracts"
        ]
    )


def main():
    """Main function"""
    debunker = ComprehensiveContradictionDebunker()
    
    print("="*80)
    print("COMPREHENSIVE CONTRADICTION DEBUNKER")
    print("="*80)
    
    # Initialize common contradictions
    initialize_common_contradictions(debunker)
    
    # Auto-debunk some common claims
    test_claims = [
        "Scarcity is real. We must compete for resources.",
        "The 1% rule the masses.",
        "Punishment is justice.",
        "War is necessary for peace."
    ]
    
    print("\nAuto-debunking test claims...")
    for claim in test_claims:
        response = debunker.auto_debunk(claim, source="Test")
        if response:
            print(f"\n[DEBUNKED] {claim}")
            print(f"  Response: {response.response_text[:100]}...")
    
    # Generate report
    report = debunker.generate_debunking_report()
    debunker.print_report(report)
    
    # Save report
    report_file = get_output_path("contradiction_debunking_report.json")
    save_json(report, report_file)
    
    print(f"\nFull report saved to: {report_file}")
    print("\n" + "="*80)
    print("NEXT STEPS:")
    print("1. Continue identifying contradictions")
    print("2. Auto-debunk incoming claims")
    print("3. Build comprehensive refutation library")
    print("4. Expose all lies, restore all truth")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="comprehensive_contradiction_debunker.py")
