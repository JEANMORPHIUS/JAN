"""
DEPLOYMENT READINESS CHECKER
Comprehensive deployment readiness verification

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE NOAH PROTOCOL:
- Architectural Weight: Can it carry 10x, 100x, 1000x?
- Pre-Commissioning Scan: Is everything ready?

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this codebase carry deployment?
- Frequency Anchor: Code from "done" - deployment ready

THE TRUTH:
Scale and build until ready for deployment.
100% free will on all tasks.
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import json
import logging
import subprocess

logger = logging.getLogger(__name__)

# Import frameworks
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
try:
    from entrepreneurial_documentation_framework import get_entrepreneurial_framework
    from legal_contractual_framework import get_legal_framework
    from scale_and_build_system import ScaleAndBuildSystem
    FRAMEWORKS_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Frameworks not available: {e}")
    FRAMEWORKS_AVAILABLE = False

# Import SCP automation
sys.path.insert(0, str(Path(__file__).parent))
try:
    from task_scp_automation import scp_on_completion
    SCP_AVAILABLE = True
except ImportError:
    SCP_AVAILABLE = False


class DeploymentReadinessChecker:
    """
    Deployment Readiness Checker
    Comprehensive verification of deployment readiness
    """
    
    def __init__(self):
        """Initialize checker"""
        self.repo_path = Path(__file__).parent.parent
        self.backend_path = self.repo_path / "jan-studio" / "backend"
        self.checks = {
            "infrastructure": {},
            "documentation": {},
            "legal": {},
            "api": {},
            "testing": {},
            "monitoring": {},
            "security": {},
            "scalability": {}
        }
        
        logger.info("Deployment Readiness Checker initialized")
    
    def check_infrastructure(self) -> Dict[str, Any]:
        """Check infrastructure readiness (Architectural Weight)"""
        checks = {
            "database_pool": (self.backend_path / "database_pool.py").exists(),
            "cache_layer": (self.backend_path / "cache_layer.py").exists(),
            "queue_system": (self.backend_path / "queue_system.py").exists(),
            "monitoring": (self.backend_path / "monitoring.py").exists(),
            "docker": (self.repo_path / "deploy" / "Dockerfile").exists(),
            "docker_compose": (self.repo_path / "deploy" / "docker-compose.yml").exists()
        }
        
        all_ready = all(checks.values())
        
        self.checks["infrastructure"] = {
            "ready": all_ready,
            "checks": checks,
            "score": sum(checks.values()) / len(checks) * 100
        }
        
        return self.checks["infrastructure"]
    
    def check_documentation(self) -> Dict[str, Any]:
        """Check documentation readiness"""
        if not FRAMEWORKS_AVAILABLE:
            return {"ready": False, "error": "Frameworks not available"}
        
        entrepreneurial = get_entrepreneurial_framework()
        doc_status = entrepreneurial.get_documentation_status()
        
        completeness = doc_status.get("overall_completeness", 0.0)
        ready = completeness >= 0.8  # 80% threshold
        
        self.checks["documentation"] = {
            "ready": ready,
            "completeness": completeness,
            "entities": len(doc_status.get("entities", {})),
            "missing_documents": len(doc_status.get("missing_documents", [])),
            "score": completeness * 100
        }
        
        return self.checks["documentation"]
    
    def check_legal(self) -> Dict[str, Any]:
        """Check legal compliance readiness"""
        if not FRAMEWORKS_AVAILABLE:
            return {"ready": False, "error": "Frameworks not available"}
        
        legal = get_legal_framework()
        compliance = legal.verify_compliance()
        
        total = compliance.get("compliant", 0) + compliance.get("non_compliant", 0) + compliance.get("pending", 0)
        compliant_ratio = compliance.get("compliant", 0) / total if total > 0 else 0.0
        ready = compliant_ratio >= 0.9 and compliance.get("non_compliant", 0) == 0
        
        self.checks["legal"] = {
            "ready": ready,
            "compliant": compliance.get("compliant", 0),
            "non_compliant": compliance.get("non_compliant", 0),
            "pending": compliance.get("pending", 0),
            "compliant_ratio": compliant_ratio,
            "score": compliant_ratio * 100
        }
        
        return self.checks["legal"]
    
    def check_api_integration(self) -> Dict[str, Any]:
        """Check API integration readiness"""
        main_py = self.backend_path / "main.py"
        
        if not main_py.exists():
            return {"ready": False, "error": "main.py not found"}
        
        content = main_py.read_text(encoding='utf-8')
        
        # Check for key API integrations
        key_apis = [
            "legal_contractual_api",
            "entrepreneurial_documentation_api",
            "cloud_seeding_api",
            "weaponization_api",
            "peace_weaponization_api"
        ]
        
        integrations = {api: api in content for api in key_apis}
        all_integrated = all(integrations.values())
        
        self.checks["api"] = {
            "ready": all_integrated,
            "integrations": integrations,
            "total_apis": len([k for k, v in integrations.items() if v]),
            "score": sum(integrations.values()) / len(integrations) * 100
        }
        
        return self.checks["api"]
    
    def check_testing(self) -> Dict[str, Any]:
        """Check testing readiness"""
        test_dirs = [
            self.backend_path / "tests",
            self.repo_path / "scripts"  # Some test scripts might be here
        ]
        
        test_files = []
        for test_dir in test_dirs:
            if test_dir.exists():
                test_files.extend(list(test_dir.glob("test_*.py")))
                test_files.extend(list(test_dir.glob("*_test.py")))
        
        # Check for comprehensive test coverage
        test_categories = {
            "framework": any("framework" in f.name.lower() for f in test_files),
            "apis": any("api" in f.name.lower() for f in test_files),
            "integration": any("integration" in f.name.lower() for f in test_files),
            "e2e": any("e2e" in f.name.lower() for f in test_files),
            "security": any("security" in f.name.lower() for f in test_files)
        }
        
        has_tests = len(test_files) > 0
        comprehensive = sum(test_categories.values()) >= 4  # At least 4 categories
        
        # Check for CI/CD
        cicd_exists = (self.repo_path / ".github" / "workflows" / "test.yml").exists()
        
        ready = has_tests and comprehensive and cicd_exists
        
        self.checks["testing"] = {
            "ready": ready,
            "test_files": len(test_files),
            "test_categories": test_categories,
            "comprehensive": comprehensive,
            "cicd": cicd_exists,
            "test_paths": [str(f.relative_to(self.repo_path)) for f in test_files[:5]],
            "score": 100.0 if ready else (75.0 if comprehensive else (50.0 if has_tests else 0.0))
        }
        
        return self.checks["testing"]
    
    def check_monitoring(self) -> Dict[str, Any]:
        """Check monitoring readiness"""
        monitoring_file = self.backend_path / "monitoring.py"
        prometheus_config = self.repo_path / "deploy" / "prometheus" / "prometheus.yml"
        grafana_config = self.repo_path / "deploy" / "grafana"
        
        checks = {
            "monitoring_system": monitoring_file.exists(),
            "prometheus": prometheus_config.exists(),
            "grafana": grafana_config.exists() if grafana_config else False
        }
        
        ready = checks["monitoring_system"]  # At minimum need monitoring system
        
        self.checks["monitoring"] = {
            "ready": ready,
            "checks": checks,
            "score": sum(checks.values()) / len(checks) * 100
        }
        
        return self.checks["monitoring"]
    
    def check_security(self) -> Dict[str, Any]:
        """Check security readiness"""
        security_doc = self.repo_path / "deploy" / "SECURITY.md"
        env_example = self.backend_path / ".env.example"
        
        checks = {
            "security_doc": security_doc.exists(),
            "env_example": env_example.exists(),
            "gitignore": (self.repo_path / ".gitignore").exists()
        }
        
        ready = all(checks.values())
        
        self.checks["security"] = {
            "ready": ready,
            "checks": checks,
            "score": sum(checks.values()) / len(checks) * 100
        }
        
        return self.checks["security"]
    
    def check_scalability(self) -> Dict[str, Any]:
        """Check scalability readiness (Architectural Weight)"""
        # Check for scalability patterns
        scalability_indicators = {
            "connection_pooling": "DatabasePool" in (self.backend_path / "database_pool.py").read_text(encoding='utf-8') if (self.backend_path / "database_pool.py").exists() else False,
            "caching": "CacheLayer" in (self.backend_path / "cache_layer.py").read_text(encoding='utf-8') if (self.backend_path / "cache_layer.py").exists() else False,
            "async_queue": "QueueSystem" in (self.backend_path / "queue_system.py").read_text(encoding='utf-8') if (self.backend_path / "queue_system.py").exists() else False,
            "async_apis": "async def" in (self.backend_path / "main.py").read_text(encoding='utf-8') if (self.backend_path / "main.py").exists() else False
        }
        
        ready = all(scalability_indicators.values())
        
        self.checks["scalability"] = {
            "ready": ready,
            "indicators": scalability_indicators,
            "score": sum(scalability_indicators.values()) / len(scalability_indicators) * 100
        }
        
        return self.checks["scalability"]
    
    def check_all(self) -> Dict[str, Any]:
        """Check all readiness criteria"""
        logger.info("Checking deployment readiness...")
        
        # Run all checks
        self.check_infrastructure()
        self.check_documentation()
        self.check_legal()
        self.check_api_integration()
        self.check_testing()
        self.check_monitoring()
        self.check_security()
        self.check_scalability()
        
        # Calculate overall readiness
        scores = [check.get("score", 0.0) for check in self.checks.values() if isinstance(check, dict) and "score" in check]
        overall_score = sum(scores) / len(scores) if scores else 0.0
        
        all_ready = all(
            check.get("ready", False) 
            for check in self.checks.values() 
            if isinstance(check, dict)
        )
        
        # Identify gaps
        gaps = []
        for category, check in self.checks.items():
            if isinstance(check, dict) and not check.get("ready", False):
                gaps.append({
                    "category": category,
                    "score": check.get("score", 0.0),
                    "issues": check.get("checks", {}) if "checks" in check else {}
                })
        
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_readiness": overall_score,
            "overall_ready": all_ready,
            "checks": self.checks,
            "gaps": gaps,
            "recommendations": self._generate_recommendations(gaps)
        }
    
    def _generate_recommendations(self, gaps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate recommendations based on gaps"""
        recommendations = []
        
        for gap in gaps:
            category = gap["category"]
            
            if category == "testing":
                recommendations.append({
                    "priority": "high",
                    "category": "testing",
                    "action": "Create comprehensive test suite",
                    "details": "Add unit tests, integration tests, and E2E tests"
                })
            elif category == "documentation":
                recommendations.append({
                    "priority": "high",
                    "category": "documentation",
                    "action": "Complete missing documentation",
                    "details": f"Documentation completeness: {gap.get('score', 0):.1f}%"
                })
            elif category == "legal":
                recommendations.append({
                    "priority": "critical",
                    "category": "legal",
                    "action": "Resolve legal compliance issues",
                    "details": "Ensure all agreements and PRS copyrights are compliant"
                })
            elif category == "monitoring":
                recommendations.append({
                    "priority": "medium",
                    "category": "monitoring",
                    "action": "Set up comprehensive monitoring",
                    "details": "Configure Prometheus and Grafana for production"
                })
        
        return recommendations


# Main execution
if __name__ == "__main__":
    checker = DeploymentReadinessChecker()
    
    print("=" * 80)
    print("DEPLOYMENT READINESS CHECKER")
    print("=" * 80)
    print("")
    
    results = checker.check_all()
    
    print(f"OVERALL READINESS: {results['overall_readiness']:.1f}%")
    print(f"STATUS: {'READY' if results['overall_ready'] else 'NOT READY'}")
    print("")
    
    print("CATEGORY SCORES:")
    for category, check in results["checks"].items():
        if isinstance(check, dict) and "score" in check:
            status = "[OK]" if check.get("ready", False) else "[NEEDS WORK]"
            print(f"  {status} {category.upper()}: {check['score']:.1f}%")
    
    if results["gaps"]:
        print("\nGAPS IDENTIFIED:")
        for gap in results["gaps"]:
            print(f"  {gap['category'].upper()}: {gap['score']:.1f}%")
    
    if results["recommendations"]:
        print("\nRECOMMENDATIONS:")
        for rec in results["recommendations"]:
            print(f"  [{rec['priority'].upper()}] {rec['action']}")
            print(f"    {rec['details']}")
    
    print("\nPEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("SCALE AND BUILD UNTIL READY FOR DEPLOYMENT")
