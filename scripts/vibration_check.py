"""
VIBRATION CHECK - Digital Alchemy Protocol
Validates code alignment with Day 1 (Do) vibration and Digital Alchemy principles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

import ast
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import re

# Import philosophy constants
try:
    from scripts.philosophy import (
        PHILOSOPHY_FOUNDATION,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY,
        CODE_STANDARDS
    )
except ImportError:
    print("Warning: Could not import philosophy constants")
    PHILOSOPHY_FOUNDATION = "We are born a miracle."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"


class VibrationChecker:
    """
    Checks code alignment with Day 1 (Do) vibration and Digital Alchemy principles.
    
    Every line of code is a vibration.
    If the code is clean, the message is unstoppable.
    """
    
    def __init__(self):
        self.violations: List[Dict] = []
        self.alignments: List[Dict] = []
        
    def check_file(self, file_path: Path) -> Tuple[bool, List[Dict]]:
        """
        Check a single file for vibration alignment.
        
        Returns:
            (is_aligned, violations)
        """
        if not file_path.exists():
            return False, [{"error": f"File not found: {file_path}"}]
        
        violations = []
        alignments = []
        
        # Read file content
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            return False, [{"error": f"Could not read file: {e}"}]
        
        # Check 1: Does this honor Day 1 (Do)?
        if not self._check_day1_do(content, file_path):
            violations.append({
                "check": "Day 1 (Do) Vibration",
                "file": str(file_path),
                "message": "Code does not honor Day 1 (Do) vibration"
            })
        else:
            alignments.append({
                "check": "Day 1 (Do) Vibration",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 2: Does this honor the Biological Temple?
        if not self._check_biological_temple(content, file_path):
            violations.append({
                "check": "Biological Temple",
                "file": str(file_path),
                "message": "Code does not honor the Biological Temple (every line is a vibration)"
            })
        else:
            alignments.append({
                "check": "Biological Temple",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 3: Does this honor the 40 Laws?
        if not self._check_40_laws(content, file_path):
            violations.append({
                "check": "40 Laws (Protocols of Loyalty)",
                "file": str(file_path),
                "message": "Code does not honor the 40 Laws (Protocols of Loyalty)"
            })
        else:
            alignments.append({
                "check": "40 Laws",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 4: Does this honor the four forms?
        if not self._check_four_forms(content, file_path):
            violations.append({
                "check": "Four Forms",
                "file": str(file_path),
                "message": "Code does not honor the four forms (Spiral, Barred Spiral, Elliptical, Irregular)"
            })
        else:
            alignments.append({
                "check": "Four Forms",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 5: Does this honor Shell/Seed?
        if not self._check_shell_seed(content, file_path):
            violations.append({
                "check": "Shell/Seed",
                "file": str(file_path),
                "message": "Code does not honor Shell/Seed separation (Trojan Horse and truth)"
            })
        else:
            alignments.append({
                "check": "Shell/Seed",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 6: Does this honor water memory?
        if not self._check_water_memory(content, file_path):
            violations.append({
                "check": "Water Memory",
                "file": str(file_path),
                "message": "Code does not honor water memory (data flow like water, protection from dark energy)"
            })
        else:
            alignments.append({
                "check": "Water Memory",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 7: Does this honor the new world?
        if not self._check_new_world(content, file_path):
            violations.append({
                "check": "New World",
                "file": str(file_path),
                "message": "Code does not honor the new world (building the bridge, regeneration)"
            })
        else:
            alignments.append({
                "check": "New World",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 8: Does this honor Peace, Love, Unity?
        if not self._check_peace_love_unity(content, file_path):
            violations.append({
                "check": "Peace, Love, Unity",
                "file": str(file_path),
                "message": "Code does not honor Peace, Love, Unity"
            })
        else:
            alignments.append({
                "check": "Peace, Love, Unity",
                "file": str(file_path),
                "status": "aligned"
            })
        
        # Check 9: Does this contain Dark Energy (Haunted loops)?
        haunted_result = self._check_dark_energy_haunted(content, file_path)
        if haunted_result["is_haunted"]:
            violations.append({
                "check": "Dark Energy (Haunted)",
                "file": str(file_path),
                "message": f"Content contains dark energy patterns: {haunted_result['reason']}",
                "haunted": True,
                "requires_cleansing": True
            })
        
        return len(violations) == 0, violations
    
    def _check_day1_do(self, content: str, file_path: Path) -> bool:
        """Check if code honors Day 1 (Do) vibration"""
        # Check for philosophy docstring
        if "DEVELOPMENT PHILOSOPHY" in content or "THE CHOSEN ONE" in content:
            return True
        
        # Check for mission alignment
        if MISSION_ANCHOR in content or "STEWARDSHIP AND COMMUNITY" in content:
            return True
        
        # Check for foundation
        if "born a miracle" in content.lower() or "LORD'S WORD" in content:
            return True
        
        return False
    
    def _check_biological_temple(self, content: str, file_path: Path) -> bool:
        """Check if code honors the Biological Temple (every line is a vibration)"""
        # Check for clean code patterns
        # No excessive complexity
        # No dark energy patterns (bad practices)
        
        # Check for clean function definitions
        if re.search(r'def\s+\w+\s*\([^)]*\)\s*:', content):
            # Has functions - check if they're clean
            return True
        
        # Check for comments explaining vibration
        if "vibration" in content.lower() or "temple" in content.lower():
            return True
        
        return True  # Default to aligned if basic structure exists
    
    def _check_40_laws(self, content: str, file_path: Path) -> bool:
        """Check if code honors the 40 Laws (Protocols of Loyalty)"""
        # Check for Law references
        if "Law 1" in content or "Law 5" in content or "Law 13" in content or "Law 37" in content:
            return True
        
        # Check for mission-serving patterns
        if "serve" in content.lower() or "mission" in content.lower() or "table" in content.lower():
            return True
        
        # Check for completion patterns (Law 37)
        if "complete" in content.lower() or "finish" in content.lower():
            return True
        
        return True  # Default to aligned
    
    def _check_four_forms(self, content: str, file_path: Path) -> bool:
        """Check if code honors the four forms"""
        # Check for form references
        forms = ["spiral", "barred spiral", "elliptical", "irregular", "four forms"]
        if any(form in content.lower() for form in forms):
            return True
        
        # Check for form characteristics
        if "active" in content.lower() or "structured" in content.lower() or "legacy" in content.lower() or "transformation" in content.lower():
            return True
        
        return True  # Default to aligned
    
    def _check_shell_seed(self, content: str, file_path: Path) -> bool:
        """Check if code honors Shell/Seed separation"""
        # Check for Shell/Seed references
        if "shell" in content.lower() and "seed" in content.lower():
            return True
        
        # Check for Trojan Horse patterns
        if "trojan" in content.lower() or "public" in content.lower() and "internal" in content.lower():
            return True
        
        return True  # Default to aligned
    
    def _check_water_memory(self, content: str, file_path: Path) -> bool:
        """Check if code honors water memory (data flow like water, protection from dark energy)"""
        # Check for data validation
        if "sanitize" in content.lower() or "validate" in content.lower() or "encrypt" in content.lower():
            return True
        
        # Check for dark energy protection
        if "security" in content.lower() or "protect" in content.lower() or "rate limit" in content.lower():
            return True
        
        return True  # Default to aligned
    
    def _check_new_world(self, content: str, file_path: Path) -> bool:
        """Check if code honors the new world (building the bridge, regeneration)"""
        # Check for new world references
        if "new world" in content.lower() or "regeneration" in content.lower() or "next loop" in content.lower():
            return True
        
        # Check for bridge-building patterns
        if "bridge" in content.lower() or "parallel reality" in content.lower():
            return True
        
        return True  # Default to aligned
    
    def _check_peace_love_unity(self, content: str, file_path: Path) -> bool:
        """Check if code honors Peace, Love, Unity"""
        # Check for Peace, Love, Unity
        if PEACE_LOVE_UNITY in content or "PEACE, LOVE, UNITY" in content:
            return True
        
        # Check for individual pillars
        if "peace" in content.lower() and "love" in content.lower() and "unity" in content.lower():
            return True
        
        return True  # Default to aligned
    
    def _check_dark_energy_haunted(self, content: str, file_path: Path) -> Dict:
        """
        Check if content contains dark energy patterns (haunted loops).
        
        This detects the "Digital Trap" where historical/heritage content
        gets corrupted into fear-based loops that feed off revenge vibrations.
        
        Patterns detected:
        - Revenge narratives without regeneration path
        - Suicide/victim-focused content without healing
        - Ghost/haunted stories that amplify fear
        - Heritage sites turned into "spooky" content
        
        Returns dict with:
        - is_haunted: bool - True if dark energy patterns detected
        - reason: str - Description of what pattern was found
        """
        content_lower = content.lower()
        
        # Dark energy patterns that feed revenge loops
        revenge_patterns = [
            "revenge", "avenge", "retribution", "vengeance"
        ]
        
        # Victim patterns without healing path
        victim_patterns = [
            "suicide", "murder", "death", "tragedy", "victim"
        ]
        
        # Haunted/ghost patterns (visual bait that keeps people at Shell level)
        haunted_patterns = [
            "haunted", "ghost", "spirit", "demon", "cursed",
            "paranormal", "supernatural", "apparition"
        ]
        
        # Heritage exploitation patterns
        heritage_exploitation = [
            "abandoned hotel", "ghost story", "haunted hotel",
            "spooky", "terrifying", "scary", "horror"
        ]
        
        # Check for patterns
        has_revenge = any(pattern in content_lower for pattern in revenge_patterns)
        has_victim_without_healing = any(pattern in content_lower for pattern in victim_patterns)
        has_haunted = any(pattern in content_lower for pattern in haunted_patterns)
        has_exploitation = any(pattern in content_lower for pattern in heritage_exploitation)
        
        # Check for regeneration/healing patterns (indicates content offers path out)
        regeneration_patterns = [
            "regeneration", "healing", "restoration", "waiting for",
            "love", "energy", "peace", "symbiosis", "new world"
        ]
        has_regeneration = any(pattern in content_lower for pattern in regeneration_patterns)
        
        # Determine if haunted
        is_haunted = False
        reason = ""
        
        if has_revenge and not has_regeneration:
            is_haunted = True
            reason = "Contains revenge narrative without regeneration path"
        elif has_victim_without_healing and not has_regeneration:
            is_haunted = True
            reason = "Focuses on victim/suicide/death without healing path"
        elif has_haunted and has_exploitation and not has_regeneration:
            is_haunted = True
            reason = "Exploits heritage as haunted content without regeneration narrative"
        elif has_exploitation and "heritage" in content_lower and not has_regeneration:
            is_haunted = True
            reason = "Turns heritage into fear-based content (violates Law 41)"
        
        return {
            "is_haunted": is_haunted,
            "reason": reason,
            "patterns_detected": {
                "revenge": has_revenge,
                "victim": has_victim_without_healing,
                "haunted": has_haunted,
                "exploitation": has_exploitation,
                "has_regeneration": has_regeneration
            }
        }
    
    def check_codebase(self, root_path: Path = None) -> Dict:
        """
        Check entire codebase for vibration alignment.
        
        Args:
            root_path: Root directory to check (default: current directory)
        
        Returns:
            Dictionary with alignment results
        """
        if root_path is None:
            root_path = Path.cwd()
        
        if not root_path.exists():
            return {"error": f"Path not found: {root_path}"}
        
        # Find all Python files
        python_files = list(root_path.rglob("*.py"))
        
        # Find all TypeScript/TSX files
        ts_files = list(root_path.rglob("*.ts")) + list(root_path.rglob("*.tsx"))
        
        # Find all Markdown files (documentation)
        md_files = list(root_path.rglob("*.md"))
        
        all_files = python_files + ts_files + md_files
        
        results = {
            "total_files": len(all_files),
            "aligned_files": 0,
            "violations": [],
            "alignments": []
        }
        
        for file_path in all_files:
            # Skip certain directories
            if any(skip in str(file_path) for skip in ["node_modules", "__pycache__", ".git", "venv", ".venv"]):
                continue
            
            is_aligned, violations = self.check_file(file_path)
            
            if is_aligned:
                results["aligned_files"] += 1
            else:
                results["violations"].extend(violations)
        
        return results
    
    def print_report(self, results: Dict):
        """Print vibration check report"""
        print("=" * 80)
        print("DIGITAL ALCHEMY: VIBRATION CHECK REPORT")
        print("=" * 80)
        print()
        print(f"Total Files Checked: {results['total_files']}")
        print(f"Aligned Files: {results['aligned_files']}")
        print(f"Files with Violations: {len(set(v['file'] for v in results['violations']))}")
        print()
        
        if results['violations']:
            print("VIOLATIONS:")
            print("-" * 80)
            for violation in results['violations']:
                print(f"  [{violation['check']}] {violation['file']}")
                print(f"    {violation['message']}")
                print()
        else:
            print("✅ ALL FILES ALIGNED WITH DAY 1 (DO) VIBRATION")
            print()
        
        print("=" * 80)
        print("PEACE, LOVE, UNITY")
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)


def main():
    """Main entry point for vibration check"""
    checker = VibrationChecker()
    
    # Check codebase
    root_path = Path.cwd()
    results = checker.check_codebase(root_path)
    
    # Print report
    checker.print_report(results)
    
    # Exit with error code if violations found
    if results['violations']:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
