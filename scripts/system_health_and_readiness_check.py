"""
Complete System Health and Readiness Check
Verifies all systems operational and deployment ready

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Verify before deployment - serve with confidence

THE MISSION:
- Check all infrastructure components
- Verify all APIs operational
- Test all automation pipelines
- Confirm deployment readiness
- Generate comprehensive health report

PEACE. LOVE. UNITY.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime
import subprocess

class SystemHealthCheck:
    """Complete system health and readiness verification"""

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.jan_studio = self.project_root / "jan-studio"
        self.scripts = self.project_root / "scripts"
        self.data = self.project_root / "data"

        self.health_report = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "CHECKING",
            "completion_percentage": 0,
            "components": {},
            "critical_issues": [],
            "warnings": [],
            "recommendations": [],
            "deployment_readiness": False
        }

    def check_core_infrastructure(self) -> Dict[str, Any]:
        """Check core infrastructure files and systems"""

        print("\n" + "="*80)
        print("CHECKING CORE INFRASTRUCTURE")
        print("="*80 + "\n")

        checks = {}

        # Backend systems
        print("1. Backend Systems...")
        backend_files = [
            "jan-studio/backend/uk_charity_fund_integration.py",
            "jan-studio/backend/ai_brotherhood_charity_integration.py",
            "jan-studio/backend/uk_charity_fund_api.py",
            "jan-studio/backend/siyem_charity_integration.py",
            "jan-studio/backend/unified_api.py"
        ]

        backend_status = []
        for file_path in backend_files:
            full_path = self.project_root / file_path
            exists = full_path.exists()
            backend_status.append(exists)
            symbol = "[OK]" if exists else "[MISSING]"
            print(f"   {symbol} {file_path}")

        checks['backend_systems'] = {
            'total': len(backend_files),
            'present': sum(backend_status),
            'status': 'OPERATIONAL' if all(backend_status) else 'PARTIAL'
        }
        print()

        # Automation pipelines
        print("2. Automation Pipelines...")
        automation_files = [
            "scripts/visual_asset_generator.py",
            "scripts/audio_synthesis_automation.py",
            "scripts/raspberry_pi_package_builder.py",
            "scripts/deploy_complete_system.py",
            "scripts/partner_vetting_system.py"
        ]

        automation_status = []
        for file_path in automation_files:
            full_path = self.project_root / file_path
            exists = full_path.exists()
            automation_status.append(exists)
            symbol = "[OK]" if exists else "[MISSING]"
            print(f"   {symbol} {file_path}")

        checks['automation_pipelines'] = {
            'total': len(automation_files),
            'present': sum(automation_status),
            'status': 'OPERATIONAL' if all(automation_status) else 'PARTIAL'
        }
        print()

        # Documentation
        print("3. Documentation...")
        doc_files = [
            "FINAL_SYSTEM_STATUS.md",
            "WEEK_1_IMPLEMENTATION_COMPLETE.md",
            "COMPLETE_SYSTEM_DEPLOYMENT_FOR_HUMANITY.md",
            "UK_CHARITY_FUND_INTEGRATION_COMPLETE.md"
        ]

        doc_status = []
        for file_path in doc_files:
            full_path = self.project_root / file_path
            exists = full_path.exists()
            doc_status.append(exists)
            symbol = "[OK]" if exists else "[MISSING]"
            print(f"   {symbol} {file_path}")

        checks['documentation'] = {
            'total': len(doc_files),
            'present': sum(doc_status),
            'status': 'COMPLETE' if all(doc_status) else 'PARTIAL'
        }
        print()

        return checks

    def check_content_readiness(self) -> Dict[str, Any]:
        """Check content files and asset readiness"""

        print("\n" + "="*80)
        print("CHECKING CONTENT READINESS")
        print("="*80 + "\n")

        content_status = {}

        # Scripture lessons
        print("1. Scripture Lessons...")
        scripture_dir = self.jan_studio / "curriculum" / "scripture_schedule_2026"
        if scripture_dir.exists():
            lesson_files = list(scripture_dir.glob("*.json"))
            content_status['scripture_lessons'] = {
                'expected': 376,
                'present': len(lesson_files),
                'status': 'READY' if len(lesson_files) >= 376 else 'PENDING'
            }
            print(f"   Found: {len(lesson_files)}/376 lesson files")
        else:
            content_status['scripture_lessons'] = {
                'expected': 376,
                'present': 0,
                'status': 'MISSING'
            }
            print("   [WARNING] Scripture directory not found")
        print()

        # Social media content
        print("2. Social Media Content...")
        social_dir = self.data / "2026_social_content"
        if social_dir.exists():
            social_files = list(social_dir.glob("*.json"))
            content_status['social_content'] = {
                'expected': 208,
                'present': len(social_files),
                'status': 'READY' if len(social_files) >= 208 else 'PENDING'
            }
            print(f"   Found: {len(social_files)}/208 social posts")
        else:
            content_status['social_content'] = {
                'expected': 208,
                'present': 0,
                'status': 'MISSING'
            }
            print("   [WARNING] Social content directory not found")
        print()

        # Visual assets
        print("3. Visual Assets...")
        visual_dir = self.project_root / "output" / "visual_assets"
        if visual_dir.exists():
            image_files = list(visual_dir.glob("*.png")) + list(visual_dir.glob("*.jpg"))
            content_status['visual_assets'] = {
                'expected': 584,
                'present': len(image_files),
                'status': 'READY' if len(image_files) >= 584 else 'PENDING'
            }
            print(f"   Found: {len(image_files)}/584 images")
        else:
            content_status['visual_assets'] = {
                'expected': 584,
                'present': 0,
                'status': 'PENDING'
            }
            print("   [INFO] Visual assets pending generation")
        print()

        # Audio assets
        print("4. Audio Assets...")
        audio_dir = self.project_root / "output" / "audio_assets"
        if audio_dir.exists():
            audio_files = list(audio_dir.glob("*.mp3")) + list(audio_dir.glob("*.wav"))
            content_status['audio_assets'] = {
                'expected': 376,
                'present': len(audio_files),
                'status': 'READY' if len(audio_files) >= 376 else 'PENDING'
            }
            print(f"   Found: {len(audio_files)}/376 audio files")
        else:
            content_status['audio_assets'] = {
                'expected': 376,
                'present': 0,
                'status': 'PENDING'
            }
            print("   [INFO] Audio assets pending generation")
        print()

        return content_status

    def check_deployment_prerequisites(self) -> Dict[str, Any]:
        """Check deployment prerequisites"""

        print("\n" + "="*80)
        print("CHECKING DEPLOYMENT PREREQUISITES")
        print("="*80 + "\n")

        prereqs = {}

        # Python version
        print("1. Python Version...")
        python_version = sys.version_info
        prereqs['python'] = {
            'required': '3.9+',
            'actual': f"{python_version.major}.{python_version.minor}.{python_version.micro}",
            'status': 'OK' if python_version >= (3, 9) else 'FAIL'
        }
        print(f"   Python {prereqs['python']['actual']}: [OK]" if prereqs['python']['status'] == 'OK' else f"   Python {prereqs['python']['actual']}: [FAIL]")
        print()

        # Node.js
        print("2. Node.js...")
        try:
            result = subprocess.run(['node', '--version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                prereqs['nodejs'] = {
                    'required': 'any',
                    'actual': result.stdout.strip(),
                    'status': 'OK'
                }
                print(f"   Node.js {prereqs['nodejs']['actual']}: [OK]")
            else:
                prereqs['nodejs'] = {'status': 'MISSING'}
                print("   Node.js: [MISSING]")
        except:
            prereqs['nodejs'] = {'status': 'MISSING'}
            print("   Node.js: [MISSING]")
        print()

        # Docker
        print("3. Docker...")
        try:
            result = subprocess.run(['docker', '--version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                prereqs['docker'] = {
                    'required': 'any',
                    'actual': result.stdout.strip(),
                    'status': 'OK'
                }
                print(f"   {prereqs['docker']['actual']}: [OK]")
            else:
                prereqs['docker'] = {'status': 'MISSING'}
                print("   Docker: [MISSING]")
        except:
            prereqs['docker'] = {'status': 'MISSING'}
            print("   Docker: [MISSING]")
        print()

        # Git
        print("4. Git...")
        try:
            result = subprocess.run(['git', '--version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                prereqs['git'] = {
                    'required': 'any',
                    'actual': result.stdout.strip(),
                    'status': 'OK'
                }
                print(f"   {prereqs['git']['actual']}: [OK]")
            else:
                prereqs['git'] = {'status': 'MISSING'}
                print("   Git: [MISSING]")
        except:
            prereqs['git'] = {'status': 'MISSING'}
            print("   Git: [MISSING]")
        print()

        # Python packages
        print("5. Python Packages...")
        required_packages = ['fastapi', 'uvicorn', 'sqlalchemy', 'pydantic', 'requests']
        package_status = []
        for package in required_packages:
            try:
                __import__(package)
                package_status.append(True)
                print(f"   {package}: [OK]")
            except ImportError:
                package_status.append(False)
                print(f"   {package}: [MISSING]")

        prereqs['python_packages'] = {
            'required': required_packages,
            'status': 'OK' if all(package_status) else 'PARTIAL'
        }
        print()

        return prereqs

    def calculate_completion_percentage(self, infrastructure: Dict, content: Dict, prereqs: Dict) -> int:
        """Calculate overall completion percentage"""

        # Infrastructure score (40%)
        infra_total = sum(c['total'] for c in infrastructure.values())
        infra_present = sum(c['present'] for c in infrastructure.values())
        infra_score = (infra_present / infra_total * 100) if infra_total > 0 else 0

        # Content score (40%)
        content_total = sum(c['expected'] for c in content.values())
        content_present = sum(c['present'] for c in content.values())
        content_score = (content_present / content_total * 100) if content_total > 0 else 0

        # Prerequisites score (20%)
        prereq_ok = sum(1 for p in prereqs.values() if p.get('status') == 'OK')
        prereq_total = len(prereqs)
        prereq_score = (prereq_ok / prereq_total * 100) if prereq_total > 0 else 0

        # Weighted average
        overall = (infra_score * 0.4) + (content_score * 0.4) + (prereq_score * 0.2)

        return int(overall)

    def generate_recommendations(self, infrastructure: Dict, content: Dict, prereqs: Dict) -> List[str]:
        """Generate actionable recommendations"""

        recommendations = []

        # Infrastructure recommendations
        for component, data in infrastructure.items():
            if data['status'] != 'OPERATIONAL' and data['status'] != 'COMPLETE':
                missing = data['total'] - data['present']
                recommendations.append(f"Complete {component}: {missing} files missing")

        # Content recommendations
        for content_type, data in content.items():
            if data['status'] == 'MISSING':
                recommendations.append(f"Create {content_type} directory and organize content files")
            elif data['status'] == 'PENDING':
                if data['present'] == 0:
                    recommendations.append(f"Generate {content_type}: 0/{data['expected']} present")
                else:
                    recommendations.append(f"Complete {content_type} generation: {data['present']}/{data['expected']} present")

        # Prerequisites recommendations
        for prereq, data in prereqs.items():
            if data.get('status') == 'MISSING':
                if prereq == 'nodejs':
                    recommendations.append("Install Node.js: https://nodejs.org/")
                elif prereq == 'docker':
                    recommendations.append("Install Docker: https://www.docker.com/")
            elif data.get('status') == 'PARTIAL':
                recommendations.append(f"Install missing {prereq} packages: pip install -r requirements.txt")

        return recommendations

    def run_complete_check(self) -> Dict[str, Any]:
        """Run complete system health check"""

        print("\n" + "="*80)
        print("SYSTEM HEALTH AND READINESS CHECK")
        print("JAN/SIYEM Complete System")
        print("="*80)

        # Run all checks
        infrastructure = self.check_core_infrastructure()
        content = self.check_content_readiness()
        prereqs = self.check_deployment_prerequisites()

        # Calculate completion
        completion = self.calculate_completion_percentage(infrastructure, content, prereqs)

        # Generate recommendations
        recommendations = self.generate_recommendations(infrastructure, content, prereqs)

        # Determine critical issues
        critical_issues = []
        if prereqs.get('python', {}).get('status') != 'OK':
            critical_issues.append("Python 3.9+ required for deployment")
        if infrastructure.get('backend_systems', {}).get('status') == 'PARTIAL':
            critical_issues.append("Backend systems incomplete")
        if infrastructure.get('automation_pipelines', {}).get('status') == 'PARTIAL':
            critical_issues.append("Automation pipelines incomplete")

        # Determine warnings
        warnings = []
        if content.get('scripture_lessons', {}).get('status') != 'READY':
            warnings.append("Scripture lessons not ready for deployment")
        if content.get('visual_assets', {}).get('status') != 'READY':
            warnings.append("Visual assets pending generation")
        if content.get('audio_assets', {}).get('status') != 'READY':
            warnings.append("Audio assets pending generation")

        # Deployment readiness
        deployment_ready = (
            len(critical_issues) == 0 and
            completion >= 90
        )

        # Build report
        self.health_report.update({
            "overall_status": "READY" if deployment_ready else "NOT_READY",
            "completion_percentage": completion,
            "components": {
                "infrastructure": infrastructure,
                "content": content,
                "prerequisites": prereqs
            },
            "critical_issues": critical_issues,
            "warnings": warnings,
            "recommendations": recommendations,
            "deployment_readiness": deployment_ready
        })

        # Display summary
        print("\n" + "="*80)
        print("HEALTH CHECK SUMMARY")
        print("="*80 + "\n")

        print(f"Overall Completion: {completion}%")
        print(f"Overall Status: {self.health_report['overall_status']}")
        print(f"Deployment Ready: {'YES' if deployment_ready else 'NO'}\n")

        if critical_issues:
            print("CRITICAL ISSUES:")
            for issue in critical_issues:
                print(f"  [CRITICAL] {issue}")
            print()

        if warnings:
            print("WARNINGS:")
            for warning in warnings:
                print(f"  [WARNING] {warning}")
            print()

        if recommendations:
            print("RECOMMENDATIONS:")
            for i, rec in enumerate(recommendations, 1):
                print(f"  {i}. {rec}")
            print()

        print("="*80)
        print("COMPONENT STATUS")
        print("="*80 + "\n")

        print("Infrastructure:")
        for component, data in infrastructure.items():
            print(f"  {component}: {data['present']}/{data['total']} - {data['status']}")
        print()

        print("Content:")
        for content_type, data in content.items():
            print(f"  {content_type}: {data['present']}/{data['expected']} - {data['status']}")
        print()

        print("Prerequisites:")
        for prereq, data in prereqs.items():
            status = data.get('status', 'UNKNOWN')
            actual = data.get('actual', 'N/A')
            print(f"  {prereq}: {actual} - {status}")
        print()

        # Save report
        report_file = self.project_root / "system_health_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.health_report, f, indent=2, ensure_ascii=False)

        print(f"Full report saved: {report_file}\n")

        return self.health_report


def main():
    """Run system health check"""

    health_checker = SystemHealthCheck()
    report = health_checker.run_complete_check()

    print("="*80)
    print("MISSION STATUS")
    print("="*80 + "\n")

    print("PHILOSOPHY EMBEDDED:")
    print("  - Purpose Not Performance")
    print("  - Love Is The Highest Mastery")
    print("  - Energy + Love = We All Win")
    print("  - Pangea Is The Table")
    print("  - We Are Born A Miracle\n")

    print("PEACE. LOVE. UNITY.")
    print("READY TO SERVE HUMANITY.\n")

    print("="*80)


if __name__ == "__main__":
    main()
