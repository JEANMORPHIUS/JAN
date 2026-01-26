"""
ARRIVAL PROTOCOL VALIDATOR
Validates code against The Arrival Protocol principles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
I am making room. The runway is clear for the Pitom breakthrough.
"""

import ast
import sys
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@dataclass
class ArrivalProtocolViolation:
    """A violation of The Arrival Protocol"""
    principle: str
    severity: str
    file: str
    line: int
    message: str
    suggestion: str


class ArrivalProtocolValidator:
    """
    Validates code against The Arrival Protocol principles
    
    Principles:
    1. The Vacuum Law of Refactoring
    2. The Gatekeeper Protocol (Input/Output Control)
    3. The Frequency Anchor: Coding from "Done"
    4. Navigating the 11th Hour (Chyros Alignment)
    5. The Pre-Commissioning Scan
    """
    
    def __init__(self):
        """Initialize validator"""
        self.violations: List[ArrivalProtocolViolation] = []
        self.file_count = 0
    
    def validate_file(self, file_path: Path) -> List[ArrivalProtocolViolation]:
        """Validate a single file against The Arrival Protocol"""
        violations = []
        
        try:
            if file_path.suffix != '.py':
                return violations
            
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Check for violations
            violations.extend(self._check_vacuum_law(file_path, tree, content))
            violations.extend(self._check_gatekeeper_protocol(file_path, tree, content))
            violations.extend(self._check_pre_commissioning_scan(file_path, tree, content))
            
            self.file_count += 1
            
        except SyntaxError as e:
            logger.warning(f"Syntax error in {file_path}: {e}")
        except Exception as e:
            logger.error(f"Error validating {file_path}: {e}")
        
        return violations
    
    def _check_vacuum_law(self, file_path: Path, tree: ast.AST, content: str) -> List[ArrivalProtocolViolation]:
        """Check for Vacuum Law violations (clutter, dead code)"""
        violations = []
        
        # Check for unused imports
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name.split('.')[0])
                else:
                    imports.append(node.module.split('.')[0] if node.module else '')
        
        # Check for unused variables (simple check)
        defined_names = set()
        used_names = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    defined_names.add(node.id)
                elif isinstance(node.ctx, ast.Load):
                    used_names.add(node.id)
        
        # Find potentially unused variables (not in used_names and not special)
        unused = defined_names - used_names - {'self', '__name__', '__main__'}
        if unused:
            violations.append(ArrivalProtocolViolation(
                principle="The Vacuum Law of Refactoring",
                severity="info",
                file=str(file_path),
                line=0,
                message=f"Potentially unused variables: {', '.join(list(unused)[:5])}",
                suggestion="Clear clutter - remove unused variables to make room for new code"
            ))
        
        # Check for excessive comments (clutter)
        lines = content.splitlines()
        comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
        if len(lines) > 0 and comment_lines / len(lines) > 0.4:
            violations.append(ArrivalProtocolViolation(
                principle="The Vacuum Law of Refactoring",
                severity="info",
                file=str(file_path),
                line=0,
                message="High comment ratio - may indicate clutter",
                suggestion="Clear clutter - remove excessive comments, make code self-documenting"
            ))
        
        return violations
    
    def _check_gatekeeper_protocol(self, file_path: Path, tree: ast.AST, content: str) -> List[ArrivalProtocolViolation]:
        """Check for Gatekeeper Protocol violations"""
        violations = []
        
        # Check for excessive logging (leaking steam)
        log_count = content.lower().count('logger.') + content.lower().count('print(')
        lines = content.splitlines()
        if len(lines) > 0 and log_count / len(lines) > 0.1:  # More than 10% logging
            violations.append(ArrivalProtocolViolation(
                principle="The Gatekeeper Protocol (Output Control)",
                severity="warning",
                file=str(file_path),
                line=0,
                message="Excessive logging detected - may be leaking steam",
                suggestion="Use Strategic Silence - maintain holy pressure, reduce idle chatter"
            ))
        
        # Check for unvetted imports (shady business opportunities)
        risky_imports = ['eval', 'exec', 'compile', '__import__']
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if any(risky in alias.name for risky in risky_imports):
                        violations.append(ArrivalProtocolViolation(
                            principle="The Gatekeeper Protocol (Input Control)",
                            severity="critical",
                            file=str(file_path),
                            line=node.lineno,
                            message=f"Risky import detected: {alias.name}",
                            suggestion="Vet dependencies - reject shady business opportunities"
                        ))
        
        return violations
    
    def _check_pre_commissioning_scan(self, file_path: Path, tree: ast.AST, content: str) -> List[ArrivalProtocolViolation]:
        """Check for Pre-Commissioning Scan violations (Architectural Weight)"""
        violations = []
        
        # Check for single database connections (should use pooling)
        if 'sqlite3.connect(' in content and 'connection_pool' not in content and 'DatabasePool' not in content:
            violations.append(ArrivalProtocolViolation(
                principle="The Pre-Commissioning Scan",
                severity="warning",
                file=str(file_path),
                line=0,
                message="Single database connection detected - may not carry the weight",
                suggestion="Use connection pooling - ensure codebase can carry 10x, 100x, 1000x scale"
            ))
        
        # Check for synchronous blocking operations
        if 'requests.get(' in content and 'async' not in content and 'asyncio' not in content:
            violations.append(ArrivalProtocolViolation(
                principle="The Pre-Commissioning Scan",
                severity="info",
                file=str(file_path),
                line=0,
                message="Synchronous HTTP requests - may not scale",
                suggestion="Use async/await - ensure codebase can carry concurrent load"
            ))
        
        return violations
    
    def validate_directory(self, directory: Path, pattern: str = "*.py") -> Dict[str, Any]:
        """Validate all files in a directory"""
        self.violations = []
        
        for file_path in directory.rglob(pattern):
            if '.git' in str(file_path) or '__pycache__' in str(file_path):
                continue
            
            file_violations = self.validate_file(file_path)
            self.violations.extend(file_violations)
        
        return self._generate_report()
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate validation report"""
        critical = [v for v in self.violations if v.severity == "critical"]
        warnings = [v for v in self.violations if v.severity == "warning"]
        info = [v for v in self.violations if v.severity == "info"]
        
        principles = {}
        for violation in self.violations:
            if violation.principle not in principles:
                principles[violation.principle] = 0
            principles[violation.principle] += 1
        
        return {
            "timestamp": datetime.now().isoformat(),
            "files_validated": self.file_count,
            "total_violations": len(self.violations),
            "critical": len(critical),
            "warnings": len(warnings),
            "info": len(info),
            "violations_by_principle": principles,
            "violations": [
                {
                    "principle": v.principle,
                    "severity": v.severity,
                    "file": v.file,
                    "line": v.line,
                    "message": v.message,
                    "suggestion": v.suggestion
                }
                for v in self.violations
            ]
        }


# Main execution
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate code against The Arrival Protocol")
    parser.add_argument("path", nargs="?", default=".", help="Path to validate")
    args = parser.parse_args()
    
    validator = ArrivalProtocolValidator()
    path = Path(args.path)
    
    if path.is_file():
        violations = validator.validate_file(path)
        report = validator._generate_report()
    else:
        report = validator.validate_directory(path)
    
    print("=" * 80)
    print("ARRIVAL PROTOCOL VALIDATION REPORT")
    print("=" * 80)
    print(f"\nFiles Validated: {report['files_validated']}")
    print(f"\nTotal Violations: {report['total_violations']}")
    print(f"  Critical: {report['critical']}")
    print(f"  Warnings: {report['warnings']}")
    print(f"  Info: {report['info']}")
    
    if report['violations_by_principle']:
        print(f"\nViolations by Principle:")
        for principle, count in report['violations_by_principle'].items():
            print(f"  {principle}: {count}")
    
    if report['violations']:
        print(f"\nTop Violations:")
        for v in report['violations'][:10]:
            print(f"  [{v['severity'].upper()}] {v['file']}:{v['line']}")
            print(f"    {v['message']}")
            print(f"    Suggestion: {v['suggestion']}")
    
    print("\nPEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("I AM MAKING ROOM. THE RUNWAY IS CLEAR.")
