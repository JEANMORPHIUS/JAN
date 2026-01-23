"""
LOOPHOLE IDENTIFIER
Systematically identify bureaucratic loopholes and workarounds

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
IDENTIFY EVERY LOOPHOLE
DOCUMENT EVERY WORKAROUND
VERIFY EVERY POSSIBILITY
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    JAN_DATA, JAN_OUTPUT, get_data_path, get_output_path,
    datetime, json, logging, List, Dict, Optional,
    setup_logging, load_json, save_json, standard_main
)

from bureaucratic_verification_system import (
    BureaucraticVerificationSystem, LoopholeType, RequirementStatus
)

logger = setup_logging(__name__)

class LoopholeIdentifier:
    """Identify and analyze bureaucratic loopholes"""
    
    def __init__(self, verification_system: BureaucraticVerificationSystem):
        self.system = verification_system
        self.loophole_patterns = [
            {
                'pattern': 'timing',
                'keywords': ['deadline', 'expiry', 'renewal', 'grace period', 'extension'],
                'type': LoopholeType.TIMING_LOOPHOLE
            },
            {
                'pattern': 'jurisdiction',
                'keywords': ['territory', 'region', 'consulate', 'embassy', 'border'],
                'type': LoopholeType.JURISDICTION_LOOPHOLE
            },
            {
                'pattern': 'interpretation',
                'keywords': ['may', 'could', 'should', 'interpretation', 'discretion'],
                'type': LoopholeType.INTERPRETATION_LOOPHOLE
            },
            {
                'pattern': 'procedural',
                'keywords': ['process', 'procedure', 'form', 'application', 'submission'],
                'type': LoopholeType.PROCEDURAL_LOOPHOLE
            },
            {
                'pattern': 'technical',
                'keywords': ['online', 'digital', 'system', 'platform', 'automated'],
                'type': LoopholeType.TECHNICAL_LOOPHOLE
            }
        ]
    
    def analyze_requirement_for_loopholes(self, requirement_id: str) -> List[Dict[str, Any]]:
        """Analyze a requirement to identify potential loopholes"""
        if requirement_id not in self.system.requirements:
            logger.error(f"Requirement not found: {requirement_id}")
            return []
        
        req = self.system.requirements[requirement_id]
        identified = []
        
        # Check for timing loopholes
        if req.validity_period or req.renewal_required:
            identified.append({
                'type': LoopholeType.TIMING_LOOPHOLE,
                'description': f"Timing-based workaround possible with {req.validity_period or 'renewal'}",
                'risk_level': 0.3,
                'effectiveness': 0.7
            })
        
        # Check for jurisdiction loopholes
        if 'consulate' in req.description.lower() or 'embassy' in req.description.lower():
            identified.append({
                'type': LoopholeType.JURISDICTION_LOOPHOLE,
                'description': "Different consulate/embassy may have different requirements",
                'risk_level': 0.4,
                'effectiveness': 0.6
            })
        
        # Check for procedural loopholes
        if req.complexity_score > 0.7:
            identified.append({
                'type': LoopholeType.PROCEDURAL_LOOPHOLE,
                'description': "High complexity suggests procedural workarounds may exist",
                'risk_level': 0.5,
                'effectiveness': 0.5
            })
        
        # Check for technical loopholes
        if req.metadata.get('online_available', False):
            identified.append({
                'type': LoopholeType.TECHNICAL_LOOPHOLE,
                'description': "Online system may have technical workarounds",
                'risk_level': 0.2,
                'effectiveness': 0.8
            })
        
        return identified
    
    def identify_common_loopholes(self) -> List[Dict[str, Any]]:
        """Identify common loopholes across jurisdictions"""
        common_loopholes = [
            {
                'name': 'Consulate Shopping',
                'type': LoopholeType.JURISDICTION_LOOPHOLE,
                'description': 'Apply at different consulate/embassy with easier requirements',
                'risk_level': 0.4,
                'effectiveness': 0.7,
                'conditions': ['Multiple consulates available', 'Different processing standards']
            },
            {
                'name': 'Timing Optimization',
                'type': LoopholeType.TIMING_LOOPHOLE,
                'description': 'Apply during off-peak periods or before policy changes',
                'risk_level': 0.2,
                'effectiveness': 0.6,
                'conditions': ['Flexible timing', 'Policy change awareness']
            },
            {
                'name': 'Digital vs Physical',
                'type': LoopholeType.TECHNICAL_LOOPHOLE,
                'description': 'Use digital application if available (often faster/easier)',
                'risk_level': 0.1,
                'effectiveness': 0.9,
                'conditions': ['Digital option available']
            },
            {
                'name': 'Interpretation Flexibility',
                'type': LoopholeType.INTERPRETATION_LOOPHOLE,
                'description': 'Leverage ambiguous language in requirements',
                'risk_level': 0.6,
                'effectiveness': 0.5,
                'conditions': ['Ambiguous wording', 'Discretionary approval']
            },
            {
                'name': 'Exception Categories',
                'type': LoopholeType.LEGAL_LOOPHOLE,
                'description': 'Qualify for exception categories (student, investor, etc.)',
                'risk_level': 0.3,
                'effectiveness': 0.8,
                'conditions': ['Exception categories exist', 'Qualification possible']
            }
        ]
        
        return common_loopholes
    
    def generate_loophole_report(self) -> Dict[str, Any]:
        """Generate comprehensive loophole analysis report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'identified_loopholes': [],
            'by_type': {},
            'by_risk_level': {'low': [], 'medium': [], 'high': []},
            'by_effectiveness': {'high': [], 'medium': [], 'low': []},
            'recommendations': []
        }
        
        # Analyze all requirements
        for req_id, req in self.system.requirements.items():
            loopholes = self.analyze_requirement_for_loopholes(req_id)
            for loop in loopholes:
                loop['requirement_id'] = req_id
                loop['requirement_name'] = req.name
                loop['jurisdiction'] = req.jurisdiction
                # Convert Enum to string for JSON serialization
                loop['type'] = loop['type'].value if hasattr(loop['type'], 'value') else str(loop['type'])
                report['identified_loopholes'].append(loop)
                
                # Group by type
                loop_type = loop['type']
                if loop_type not in report['by_type']:
                    report['by_type'][loop_type] = []
                report['by_type'][loop_type].append(loop)
                
                # Group by risk
                if loop['risk_level'] < 0.4:
                    report['by_risk_level']['low'].append(loop)
                elif loop['risk_level'] < 0.7:
                    report['by_risk_level']['medium'].append(loop)
                else:
                    report['by_risk_level']['high'].append(loop)
                
                # Group by effectiveness
                if loop['effectiveness'] > 0.7:
                    report['by_effectiveness']['high'].append(loop)
                elif loop['effectiveness'] > 0.4:
                    report['by_effectiveness']['medium'].append(loop)
                else:
                    report['by_effectiveness']['low'].append(loop)
        
        # Add common loopholes (convert Enum to string)
        common = self.identify_common_loopholes()
        for loop in common:
            if 'type' in loop and hasattr(loop['type'], 'value'):
                loop['type'] = loop['type'].value
        report['common_loopholes'] = common
        
        # Generate recommendations
        high_effect_low_risk = [
            l for l in report['identified_loopholes']
            if l['effectiveness'] > 0.7 and l['risk_level'] < 0.4
        ]
        
        if high_effect_low_risk:
            report['recommendations'].append({
                'priority': 'high',
                'description': f"Found {len(high_effect_low_risk)} high-effectiveness, low-risk loopholes",
                'loopholes': high_effect_low_risk[:5]
            })
        
        return report


def main():
    """Main function"""
    system = BureaucraticVerificationSystem()
    identifier = LoopholeIdentifier(system)
    
    print("="*80)
    print("LOOPHOLE IDENTIFIER")
    print("="*80)
    
    # Analyze all requirements
    report = identifier.generate_loophole_report()
    
    print(f"\nIdentified Loopholes: {len(report['identified_loopholes'])}")
    print(f"By Type:")
    for loop_type, loops in report['by_type'].items():
        print(f"  {loop_type}: {len(loops)}")
    
    print(f"\nBy Risk Level:")
    print(f"  Low: {len(report['by_risk_level']['low'])}")
    print(f"  Medium: {len(report['by_risk_level']['medium'])}")
    print(f"  High: {len(report['by_risk_level']['high'])}")
    
    print(f"\nBy Effectiveness:")
    print(f"  High: {len(report['by_effectiveness']['high'])}")
    print(f"  Medium: {len(report['by_effectiveness']['medium'])}")
    print(f"  Low: {len(report['by_effectiveness']['low'])}")
    
    if report['recommendations']:
        print(f"\nRecommendations:")
        for rec in report['recommendations']:
            print(f"  [{rec['priority'].upper()}] {rec['description']}")
    
    # Save report
    report_file = get_output_path("loophole_analysis_report.json")
    save_json(report, report_file)
    
    print(f"\nFull report saved to: {report_file}")

if __name__ == "__main__":
    standard_main(main, script_name="loophole_identifier.py")
