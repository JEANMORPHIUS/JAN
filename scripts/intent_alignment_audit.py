"""
INTENT & ALIGNMENT AUDIT
Analyze industries, systems, and movements for alignment gaps

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script performs Intent & Alignment Audits on industries, systems, and movements
to identify where pure intention was lost and how to restore alignment.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass, asdict

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

import logging
logger = logging.getLogger(__name__)


@dataclass
class AlignmentGap:
    """Represents a gap between intention and impact."""
    industry: str
    original_intention: str
    current_impact: str
    break_point: str
    gap_severity: float
    rift_connection: str
    yin_yang_assessment: Dict[str, Any]
    re_alignment_path: List[str]


class IntentAlignmentAudit:
    """
    The Intent & Alignment Audit system.
    
    Analyzes industries, systems, and movements to identify where alignment
    was lost and how to restore connection to higher purpose.
    """
    
    def __init__(self):
        """Initialize the Intent & Alignment Audit system."""
        self.data_path = Path(__file__).parent.parent / "data" / "intent_alignment_audit"
        self.industries_data = self._load_json("industries_audit.json")
        self.pioneers_data = self._load_json("resonance_pioneers.json")
        self.gap_framework = self._load_json("gap_analysis_framework.json")
    
    def _load_json(self, filename: str) -> Dict[str, Any]:
        """Load a JSON file from the data directory."""
        file_path = self.data_path / filename
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"File not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing {filename}: {e}")
            return {}
    
    def audit_industry(self, industry_name: str) -> Optional[AlignmentGap]:
        """
        Perform a complete audit on an industry.
        
        Args:
            industry_name: Name of industry to audit (finance, healthcare, education, etc.)
        
        Returns:
            AlignmentGap object with full analysis
        """
        industries = self.industries_data.get("industries", {})
        industry_data = industries.get(industry_name.lower())
        
        if not industry_data:
            logger.warning(f"Industry not found: {industry_name}")
            return None
        
        # Build the gap analysis
        gap = AlignmentGap(
            industry=industry_name,
            original_intention=industry_data.get("original_intention", ""),
            current_impact=industry_data.get("the_gap", {}).get("impact", ""),
            break_point=", ".join(industry_data.get("where_it_broke", [])),
            gap_severity=industry_data.get("the_gap", {}).get("severity", 0.0),
            rift_connection=industry_data.get("the_gap", {}).get("rift_connection", ""),
            yin_yang_assessment=industry_data.get("yin_yang_balance", {}),
            re_alignment_path=list(industry_data.get("re_alignment_path", {}).values())
        )
        
        return gap
    
    def get_resonance_pioneers(self, industry: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get resonance pioneers, optionally filtered by industry.
        
        Args:
            industry: Optional industry name to filter pioneers
        
        Returns:
            List of resonance pioneer dictionaries
        """
        pioneers = self.pioneers_data.get("resonance_pioneers", {}).get("pioneers", [])
        
        if industry:
            # Filter pioneers that relate to this industry
            filtered = []
            for pioneer in pioneers:
                # Check if pioneer relates to industry (simple keyword matching)
                industry_lower = industry.lower()
                if industry_lower in pioneer.get("name", "").lower() or \
                   industry_lower in str(pioneer.get("type", "")).lower():
                    filtered.append(pioneer)
            return filtered
        
        return pioneers
    
    def perform_gap_analysis(self, industry_name: str) -> Dict[str, Any]:
        """
        Perform a complete gap analysis using the framework.
        
        Args:
            industry_name: Name of industry to analyze
        
        Returns:
            Complete gap analysis dictionary
        """
        gap = self.audit_industry(industry_name)
        if not gap:
            return {}
        
        # Get resonance pioneers for this industry
        pioneers = self.get_resonance_pioneers(industry_name)
        
        # Get gap severity description
        severity_scale = self.gap_framework.get("gap_severity_scale", {})
        severity_key = None
        for key_range in severity_scale.keys():
            min_val, max_val = map(float, key_range.split("-"))
            if min_val <= gap.gap_severity <= max_val:
                severity_key = key_range
                break
        
        severity_info = severity_scale.get(severity_key, {})
        
        return {
            "industry": gap.industry,
            "original_intention": gap.original_intention,
            "current_impact": gap.current_impact,
            "break_point": gap.break_point,
            "gap_severity": gap.gap_severity,
            "severity_description": severity_info.get("description", ""),
            "recommended_action": severity_info.get("action", ""),
            "rift_connection": gap.rift_connection,
            "yin_yang_assessment": gap.yin_yang_assessment,
            "re_alignment_path": gap.re_alignment_path,
            "resonance_pioneers": pioneers,
            "pioneer_playbook": self.pioneers_data.get("resonance_pioneers", {}).get("pioneer_playbook", {})
        }
    
    def generate_audit_report(self, industry_name: str, output_path: Optional[Path] = None) -> Path:
        """
        Generate a complete audit report for an industry.
        
        Args:
            industry_name: Name of industry to audit
            output_path: Optional path for output file
        
        Returns:
            Path to generated report
        """
        if output_path is None:
            output_path = Path(__file__).parent.parent / "output" / "intent_alignment_audit" / f"{industry_name}_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        analysis = self.perform_gap_analysis(industry_name)
        
        report = {
            "audit_timestamp": datetime.now().isoformat(),
            "industry": industry_name,
            "gap_analysis": analysis,
            "universal_alignment_principles": self.gap_framework.get("universal_alignment_principles", {}),
            "the_truth": {
                "message": "No two people are the same - honor all paths, all forms, all journeys",
                "principle": "Separate pure intention from distorted outcome",
                "mission": "Debug the connection to higher purpose"
            }
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"Audit report generated: {output_path}")
        return output_path
    
    def print_audit_summary(self, industry_name: str):
        """Print a summary of the audit for an industry."""
        analysis = self.perform_gap_analysis(industry_name)
        
        if not analysis:
            print(f"Industry '{industry_name}' not found in audit data.")
            return
        
        print("=" * 80)
        print(f"INTENT & ALIGNMENT AUDIT: {industry_name.upper()}")
        print("=" * 80)
        print()
        
        print("ORIGINAL INTENTION:")
        print("-" * 80)
        print(analysis["original_intention"])
        print()
        
        print("CURRENT IMPACT:")
        print("-" * 80)
        print(analysis["current_impact"])
        print()
        
        print("THE GAP:")
        print("-" * 80)
        print(f"Severity: {analysis['gap_severity']:.1%}")
        print(f"Description: {analysis['severity_description']}")
        print(f"Action: {analysis['recommended_action']}")
        print()
        
        print("BREAK POINT:")
        print("-" * 80)
        print(analysis["break_point"])
        print()
        
        print("RIFT CONNECTION:")
        print("-" * 80)
        print(analysis["rift_connection"])
        print()
        
        print("YIN-YANG ASSESSMENT:")
        print("-" * 80)
        yin_yang = analysis["yin_yang_assessment"]
        print(f"Yang Function: {yin_yang.get('yang_function', 'N/A')}")
        print(f"Yin Intention: {yin_yang.get('yin_intention', 'N/A')}")
        print(f"Current State: {yin_yang.get('current_state', 'N/A')}")
        print(f"Target State: {yin_yang.get('target_state', 'N/A')}")
        print()
        
        print("RE-ALIGNMENT PATH:")
        print("-" * 80)
        for i, step in enumerate(analysis["re_alignment_path"], 1):
            print(f"{i}. {step}")
        print()
        
        print("RESONANCE PIONEERS:")
        print("-" * 80)
        pioneers = analysis["resonance_pioneers"]
        if pioneers:
            for pioneer in pioneers[:3]:  # Show first 3
                print(f"- {pioneer.get('name', 'N/A')}")
                print(f"  What Worked: {', '.join(pioneer.get('what_worked', [])[:2])}")
                print(f"  Resonance: {pioneer.get('resonance_frequency', 0.0):.1%}")
                print()
        else:
            print("No specific pioneers found for this industry.")
            print()
        
        print("=" * 80)
        print("THE TRUTH")
        print("=" * 80)
        print()
        print("No two people are the same - honor all paths, all forms, all journeys.")
        print()
        print("Separate pure intention from distorted outcome.")
        print("Debug the connection to higher purpose.")
        print()
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)


def main():
    """Main execution for Intent & Alignment Audit."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Perform Intent & Alignment Audit on industries")
    parser.add_argument("industry", nargs="?", help="Industry to audit (finance, healthcare, education, technology, media)")
    parser.add_argument("--list", action="store_true", help="List available industries")
    parser.add_argument("--report", action="store_true", help="Generate JSON report")
    args = parser.parse_args()
    
    audit = IntentAlignmentAudit()
    
    if args.list:
        industries = audit.industries_data.get("industries", {})
        print("Available industries:")
        for industry in industries.keys():
            print(f"  - {industry}")
        return
    
    if not args.industry:
        print("Please specify an industry to audit, or use --list to see available industries.")
        return
    
    # Print summary
    audit.print_audit_summary(args.industry)
    
    # Generate report if requested
    if args.report:
        report_path = audit.generate_audit_report(args.industry)
        print(f"\n[OK] Report generated: {report_path}")


if __name__ == "__main__":
    main()
