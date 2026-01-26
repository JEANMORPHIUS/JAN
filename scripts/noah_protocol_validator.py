"""
NOAH PROTOCOL VALIDATOR
Validates code against The Noah Protocol & Divine Acceleration principles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
We do not build plastic tables.
We build arks.
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
class NoahProtocolViolation:
    """A violation of The Noah Protocol"""
    principle: str
    severity: str  # "critical", "warning", "info"
    file: str
    line: int
    message: str
    suggestion: str


class NoahProtocolValidator:
    """
    Validates code against The Noah Protocol principles
    
    Principles:
    1. Architectural Weight (Cavode Principle)
    2. The Noah Protocol (Three-Layer Defense)
    3. Strategic Silence (Anti-Preacher Complex)
    4. Generational Cycle Breaking
    5. Shalam & Time Compression
    6. The Steward's Anchor
    """
    
    def __init__(self):
        """Initialize validator"""
        self.violations: List[NoahProtocolViolation] = []
        self.file_count = 0
        self.line_count = 0
    
    def validate_file(self, file_path: Path) -> List[NoahProtocolViolation]:
        """Validate a single file against The Noah Protocol"""
        violations = []
        
        try:
            if file_path.suffix != '.py':
                return violations
            
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Check for violations
            violations.extend(self._check_architectural_weight(file_path, tree, content))
            violations.extend(self._check_noah_protocol(file_path, tree, content))
            violations.extend(self._check_strategic_silence(file_path, tree, content))
            violations.extend(self._check_stewards_anchor(file_path, tree, content))
            
            self.file_count += 1
            self.line_count += len(content.splitlines())
            
        except SyntaxError as e:
            logger.warning(f"Syntax error in {file_path}: {e}")
        except Exception as e:
            logger.error(f"Error validating {file_path}: {e}")
        
        return violations
    
    def _check_architectural_weight(self, file_path: Path, tree: ast.AST, content: str) -> List[NoahProtocolViolation]:
        """Check for Architectural Weight violations (Cavode Principle)"""
        violations = []
        
        # Check for single database connections (should use pooling)
        if 'sqlite3.connect(' in content and 'connection_pool' not in content:
            violations.append(NoahProtocolViolation(
                principle="Architectural Weight",
                severity="warning",
                file=str(file_path),
                line=0,
                message="Single database connection detected - consider connection pooling for scale",
                suggestion="Use connection pooling to handle 10x, 100x, 1000x scale"
            ))
        
        # Check for synchronous blocking operations
        if 'requests.get(' in content and 'async' not in content and 'asyncio' not in content:
            violations.append(NoahProtocolViolation(
                principle="Architectural Weight",
                severity="info",
                file=str(file_path),
                line=0,
                message="Synchronous HTTP requests detected - consider async for scale",
                suggestion="Use async/await for I/O operations to handle concurrent requests"
            ))
        
        return violations
    
    def _check_noah_protocol(self, file_path: Path, tree: ast.AST, content: str) -> List[NoahProtocolViolation]:
        """Check for Noah Protocol violations (Three-Layer Defense)"""
        violations = []
        
        # Check for missing error handling (The Pitch)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check for unhandled external calls
                if isinstance(node.func, ast.Name):
                    if node.func.id in ['open', 'requests.get', 'subprocess.run']:
                        # Check if in try/except
                        parent = self._get_parent(node, tree)
                        if not self._is_in_try_except(parent):
                            violations.append(NoahProtocolViolation(
                                principle="The Pitch (Internal Seal)",
                                severity="warning",
                                file=str(file_path),
                                line=node.lineno,
                                message=f"Unhandled external call: {node.func.id} - component not waterproof",
                                suggestion="Wrap in try/except to maintain internal seal"
                            ))
        
        # Check for global state (The Perimeter)
        for node in ast.walk(tree):
            if isinstance(node, ast.Global):
                violations.append(NoahProtocolViolation(
                    principle="The Perimeter (Jurisdiction)",
                    severity="warning",
                    file=str(file_path),
                    line=node.lineno,
                    message="Global state detected - jurisdiction not clear",
                    suggestion="Use dependency injection instead of global state"
                ))
        
        return violations
    
    def _check_strategic_silence(self, file_path: Path, tree: ast.AST, content: str) -> List[NoahProtocolViolation]:
        """Check for Strategic Silence violations (Anti-Preacher Complex)"""
        violations = []
        
        # Count comment lines
        lines = content.splitlines()
        comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
        code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
        
        if code_lines > 0:
            comment_ratio = comment_lines / code_lines
            if comment_ratio > 0.3:  # More than 30% comments
                violations.append(NoahProtocolViolation(
                    principle="Strategic Silence",
                    severity="info",
                    file=str(file_path),
                    line=0,
                    message=f"High comment ratio ({comment_ratio:.1%}) - may be leaking power through preaching",
                    suggestion="Make code self-documenting with clear names and type hints"
                ))
        
        return violations
    
    def _check_stewards_anchor(self, file_path: Path, tree: ast.AST, content: str) -> List[NoahProtocolViolation]:
        """Check for Steward's Anchor violations"""
        violations = []
        
        # Check for type hints (clean standards)
        has_type_hints = 'typing' in content or '->' in content
        if not has_type_hints and len(content.splitlines()) > 50:
            violations.append(NoahProtocolViolation(
                principle="The Steward's Anchor",
                severity="info",
                file=str(file_path),
                line=0,
                message="Missing type hints - not anchored in clean standards",
                suggestion="Add type hints to maintain standards during acceleration"
            ))
        
        # Check for docstrings
        has_docstrings = '"""' in content or "'''" in content
        if not has_docstrings and len(content.splitlines()) > 100:
            violations.append(NoahProtocolViolation(
                principle="The Steward's Anchor",
                severity="info",
                file=str(file_path),
                line=0,
                message="Missing docstrings - documentation anchor missing",
                suggestion="Add module/function docstrings to anchor knowledge"
            ))
        
        return violations
    
    def _get_parent(self, node: ast.AST, tree: ast.AST) -> Optional[ast.AST]:
        """Get parent node (simplified)"""
        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                if child == node:
                    return parent
        return None
    
    def _is_in_try_except(self, node: Optional[ast.AST]) -> bool:
        """Check if node is within try/except"""
        if node is None:
            return False
        if isinstance(node, (ast.Try, ast.ExceptHandler)):
            return True
        return False
    
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
            "lines_validated": self.line_count,
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
    
    parser = argparse.ArgumentParser(description="Validate code against The Noah Protocol")
    parser.add_argument("path", nargs="?", default=".", help="Path to validate")
    args = parser.parse_args()
    
    validator = NoahProtocolValidator()
    path = Path(args.path)
    
    if path.is_file():
        violations = validator.validate_file(path)
        report = validator._generate_report()
    else:
        report = validator.validate_directory(path)
    
    print("=" * 80)
    print("NOAH PROTOCOL VALIDATION REPORT")
    print("=" * 80)
    print(f"\nFiles Validated: {report['files_validated']}")
    print(f"Lines Validated: {report['lines_validated']}")
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
    print("THE NOAH PROTOCOL IS ACTIVE")
