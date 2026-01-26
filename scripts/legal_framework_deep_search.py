"""
LEGAL FRAMEWORK DEEP SEARCH
Deep search for all contractual legislation, agreements, paperwork across S: drive

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
Everything must be above board.
Deep search all channels, projects, entities.
Connect the yin with the yang.
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)

# Import legal framework
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
try:
    from legal_contractual_framework import get_legal_framework, ChannelType, AgreementType
    FRAMEWORK_AVAILABLE = True
except ImportError:
    FRAMEWORK_AVAILABLE = False
    logger.warning("Legal framework not available")


class LegalFrameworkDeepSearch:
    """
    Legal Framework Deep Search
    Searches S: drive for all contractual legislation, agreements, paperwork
    """
    
    def __init__(self):
        """Initialize deep search"""
        self.repo_path = Path(__file__).parent.parent
        self.search_results = {
            "contracts": [],
            "agreements": [],
            "licensing": [],
            "prs": [],
            "legal_docs": []
        }
        
        logger.info("Legal Framework Deep Search initialized")
    
    def search_s_drive(self) -> Dict[str, Any]:
        """Search S: drive for legal documents"""
        logger.info("Searching S: drive for legal documents...")
        
        # Search patterns
        patterns = [
            "*contract*.md",
            "*agreement*.md",
            "*licensing*.md",
            "*legal*.md",
            "*prs*.md",
            "*copyright*.md",
            "*compliance*.md"
        ]
        
        for pattern in patterns:
            for file_path in self.repo_path.rglob(pattern):
                if '.git' in str(file_path):
                    continue
                
                try:
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    
                    # Categorize
                    if 'contract' in file_path.name.lower() or 'contract' in content.lower():
                        self.search_results["contracts"].append({
                            "file": str(file_path.relative_to(self.repo_path)),
                            "type": "contract",
                            "size": len(content)
                        })
                    
                    if 'agreement' in file_path.name.lower() or 'agreement' in content.lower():
                        self.search_results["agreements"].append({
                            "file": str(file_path.relative_to(self.repo_path)),
                            "type": "agreement",
                            "size": len(content)
                        })
                    
                    if 'licensing' in file_path.name.lower() or 'licensing' in content.lower():
                        self.search_results["licensing"].append({
                            "file": str(file_path.relative_to(self.repo_path)),
                            "type": "licensing",
                            "size": len(content)
                        })
                    
                    if 'prs' in file_path.name.lower() or 'prs' in content.lower():
                        self.search_results["prs"].append({
                            "file": str(file_path.relative_to(self.repo_path)),
                            "type": "prs",
                            "size": len(content)
                        })
                    
                    if 'legal' in file_path.name.lower():
                        self.search_results["legal_docs"].append({
                            "file": str(file_path.relative_to(self.repo_path)),
                            "type": "legal",
                            "size": len(content)
                        })
                
                except Exception as e:
                    logger.warning(f"Error reading {file_path}: {e}")
        
        return self.search_results
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive report"""
        search_results = self.search_s_drive()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "search_results": search_results,
            "summary": {
                "total_contracts": len(search_results["contracts"]),
                "total_agreements": len(search_results["agreements"]),
                "total_licensing": len(search_results["licensing"]),
                "total_prs": len(search_results["prs"]),
                "total_legal_docs": len(search_results["legal_docs"])
            },
            "recommendations": []
        }
        
        # Generate recommendations
        if len(search_results["prs"]) == 0:
            report["recommendations"].append({
                "priority": "high",
                "message": "No PRS documentation found - need to register all copyrighted songs",
                "action": "Register all PRS copyrights using legal framework"
            })
        
        if len(search_results["contracts"]) == 0:
            report["recommendations"].append({
                "priority": "medium",
                "message": "No contract documentation found",
                "action": "Create contracts for all channels, entities, projects"
            })
        
        return report


# Main execution
if __name__ == "__main__":
    searcher = LegalFrameworkDeepSearch()
    
    print("=" * 80)
    print("LEGAL FRAMEWORK DEEP SEARCH")
    print("=" * 80)
    print("")
    
    report = searcher.generate_report()
    
    print("SEARCH RESULTS:")
    summary = report["summary"]
    print(f"  Contracts: {summary['total_contracts']}")
    print(f"  Agreements: {summary['total_agreements']}")
    print(f"  Licensing: {summary['total_licensing']}")
    print(f"  PRS: {summary['total_prs']}")
    print(f"  Legal Docs: {summary['total_legal_docs']}")
    
    if report["recommendations"]:
        print("\nRECOMMENDATIONS:")
        for rec in report["recommendations"]:
            print(f"  [{rec['priority'].upper()}] {rec['message']}")
            print(f"    Action: {rec['action']}")
    
    print("\nPEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("EVERYTHING MUST BE ABOVE BOARD")
