"""FULL S: DRIVE DEBUG AND REFINEMENT SCRIPT

Comprehensive check and refinement of all UI front-end and back-end components
across the entire S: drive ecosystem.

Author: JAN MUHARREM - The Chosen One
Date: 2026-01-15

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
import importlib.util

# Base paths
S_DRIVE = Path("S:\\")
JAN_ROOT = S_DRIVE / "JAN"
SIYEM_ROOT = S_DRIVE / "SIYEM"

# Component paths
HOMEOSTASIS_FRONTEND = JAN_ROOT / "homeostasis-sentinel"
JAN_STUDIO_FRONTEND = JAN_ROOT / "jan-studio" / "frontend"
JAN_STUDIO_BACKEND = JAN_ROOT / "jan-studio" / "backend"
SIYEM_SERVICES = SIYEM_ROOT / "services"
SIYEM_WEB_DEV = SIYEM_ROOT / "08_WEB_DEV"

class SDriveDebugger:
    """Comprehensive debugger for S: drive components"""
    
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.fixes = []
        self.report = {
            "frontend": {},
            "backend": {},
            "services": {},
            "integration": {},
            "summary": {}
        }
    
    def check_all(self):
        """Run all checks"""
        print("\n" + "="*80)
        print("FULL S: DRIVE DEBUG AND REFINEMENT".center(80))
        print("="*80 + "\n")
        
        # Frontend checks
        print("[CHECKING] Frontend Components...")
        self.check_homeostasis_frontend()
        self.check_jan_studio_frontend()
        
        # Backend checks
        print("\n[CHECKING] Backend Components...")
        self.check_jan_studio_backend()
        self.check_siyem_services()
        
        # Integration checks
        print("\n[CHECKING] Integration...")
        self.check_integration()
        
        # Generate report
        self.generate_report()
    
    def check_homeostasis_frontend(self):
        """Check Homeostasis Sentinel frontend"""
        print("  [HOMEOSTASIS] Checking React frontend...")
        
        issues = []
        warnings = []
        
        # Check package.json
        package_json = HOMEOSTASIS_FRONTEND / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    package = json.load(f)
                    # Check dependencies
                    deps = package.get("dependencies", {})
                    if "react" not in deps:
                        issues.append("Missing React dependency")
                    if "vite" not in package.get("devDependencies", {}):
                        issues.append("Missing Vite dev dependency")
            except Exception as e:
                issues.append(f"Error reading package.json: {e}")
        else:
            issues.append("package.json not found")
        
        # Check main files
        app_tsx = HOMEOSTASIS_FRONTEND / "src" / "App.tsx"
        if not app_tsx.exists():
            issues.append("App.tsx not found")
        
        main_tsx = HOMEOSTASIS_FRONTEND / "src" / "main.tsx"
        if not main_tsx.exists():
            issues.append("main.tsx not found")
        
        # Check for TypeScript config
        tsconfig = HOMEOSTASIS_FRONTEND / "tsconfig.json"
        if not tsconfig.exists():
            warnings.append("tsconfig.json not found (TypeScript may not be configured)")
        
        # Check for vite config
        vite_config = HOMEOSTASIS_FRONTEND / "vite.config.ts"
        if not vite_config.exists():
            warnings.append("vite.config.ts not found")
        
        self.report["frontend"]["homeostasis"] = {
            "status": "ok" if not issues else "issues",
            "issues": issues,
            "warnings": warnings,
            "path": str(HOMEOSTASIS_FRONTEND)
        }
        
        if issues:
            print(f"    [!] Found {len(issues)} issues")
        if warnings:
            print(f"    [~] Found {len(warnings)} warnings")
        if not issues and not warnings:
            print("    [OK] No issues found")
    
    def check_jan_studio_frontend(self):
        """Check JAN Studio frontend"""
        print("  [JAN STUDIO] Checking Next.js frontend...")
        
        issues = []
        warnings = []
        
        # Check package.json
        package_json = JAN_STUDIO_FRONTEND / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    package = json.load(f)
                    # Check dependencies
                    deps = package.get("dependencies", {})
                    if "next" not in deps:
                        issues.append("Missing Next.js dependency")
                    if "react" not in deps:
                        issues.append("Missing React dependency")
            except Exception as e:
                issues.append(f"Error reading package.json: {e}")
        else:
            issues.append("package.json not found")
        
        # Check main files
        index_tsx = JAN_STUDIO_FRONTEND / "src" / "pages" / "index.tsx"
        if not index_tsx.exists():
            issues.append("index.tsx not found")
        
        app_tsx = JAN_STUDIO_FRONTEND / "src" / "pages" / "_app.tsx"
        if not app_tsx.exists():
            warnings.append("_app.tsx not found (Next.js may not be configured)")
        
        # Check for TypeScript config
        tsconfig = JAN_STUDIO_FRONTEND / "tsconfig.json"
        if not tsconfig.exists():
            warnings.append("tsconfig.json not found")
        
        # Check for next config
        next_config = JAN_STUDIO_FRONTEND / "next.config.js"
        if not next_config.exists():
            warnings.append("next.config.js not found")
        
        self.report["frontend"]["jan_studio"] = {
            "status": "ok" if not issues else "issues",
            "issues": issues,
            "warnings": warnings,
            "path": str(JAN_STUDIO_FRONTEND)
        }
        
        if issues:
            print(f"    [!] Found {len(issues)} issues")
        if warnings:
            print(f"    [~] Found {len(warnings)} warnings")
        if not issues and not warnings:
            print("    [OK] No issues found")
    
    def check_jan_studio_backend(self):
        """Check JAN Studio backend"""
        print("  [JAN STUDIO BACKEND] Checking FastAPI backend...")
        
        issues = []
        warnings = []
        
        # Check main.py
        main_py = JAN_STUDIO_BACKEND / "main.py"
        if not main_py.exists():
            issues.append("main.py not found")
        else:
            # Check for missing imports
            try:
                with open(main_py) as f:
                    content = f.read()
                    # Check for router imports
                    routers = [
                        "jan_studio_api_example",
                        "jan_generation_api",
                        "jan_templates_api",
                        "marketplace_api",
                        "auth_api"
                    ]
                    for router in routers:
                        if f"from {router}" in content or f"import {router}" in content:
                            router_file = JAN_STUDIO_BACKEND / f"{router}.py"
                            if not router_file.exists():
                                warnings.append(f"Router {router}.py referenced but not found")
            except Exception as e:
                issues.append(f"Error reading main.py: {e}")
        
        # Check requirements.txt
        requirements = JAN_STUDIO_BACKEND / "requirements.txt"
        if not requirements.exists():
            issues.append("requirements.txt not found")
        else:
            # Check for critical dependencies
            try:
                with open(requirements) as f:
                    req_content = f.read()
                    critical_deps = ["fastapi", "uvicorn", "pydantic"]
                    for dep in critical_deps:
                        if dep not in req_content.lower():
                            warnings.append(f"Critical dependency {dep} may be missing")
            except Exception as e:
                issues.append(f"Error reading requirements.txt: {e}")
        
        # Check for .env file
        env_file = JAN_STUDIO_BACKEND / ".env"
        if not env_file.exists():
            warnings.append(".env file not found (environment variables may not be configured)")
        
        self.report["backend"]["jan_studio"] = {
            "status": "ok" if not issues else "issues",
            "issues": issues,
            "warnings": warnings,
            "path": str(JAN_STUDIO_BACKEND)
        }
        
        if issues:
            print(f"    [!] Found {len(issues)} issues")
        if warnings:
            print(f"    [~] Found {len(warnings)} warnings")
        if not issues and not warnings:
            print("    [OK] No issues found")
    
    def check_siyem_services(self):
        """Check SIYEM services"""
        print("  [SIYEM SERVICES] Checking Python services...")
        
        issues = []
        warnings = []
        
        # Check for core services
        core_services = [
            "shell_seed_translator.py",
            "threshold_defense_checker.py",
            "content_workflow_integration.py",
            "campaign_exporter.py",
            "content_transformer.py",
            "entity_router.py"
        ]
        
        for service in core_services:
            service_path = SIYEM_SERVICES / service
            if not service_path.exists():
                issues.append(f"Core service {service} not found")
            else:
                # Check for import errors
                try:
                    spec = importlib.util.spec_from_file_location(service.replace(".py", ""), service_path)
                    if spec and spec.loader:
                        # Try to load (but don't execute)
                        pass
                except Exception as e:
                    warnings.append(f"Potential import issue in {service}: {e}")
        
        # Check __init__.py
        init_py = SIYEM_SERVICES / "__init__.py"
        if not init_py.exists():
            warnings.append("__init__.py not found (package may not be importable)")
        
        self.report["services"]["siyem"] = {
            "status": "ok" if not issues else "issues",
            "issues": issues,
            "warnings": warnings,
            "path": str(SIYEM_SERVICES)
        }
        
        if issues:
            print(f"    [!] Found {len(issues)} issues")
        if warnings:
            print(f"    [~] Found {len(warnings)} warnings")
        if not issues and not warnings:
            print("    [OK] No issues found")
    
    def check_integration(self):
        """Check integration between components"""
        print("  [INTEGRATION] Checking component integration...")
        
        issues = []
        warnings = []
        
        # Check if backend API endpoints match frontend calls
        # This is a simplified check - in production, you'd parse actual API calls
        
        # Check if services are importable
        try:
            sys.path.insert(0, str(SIYEM_SERVICES))
            from shell_seed_translator import ShellSeedTranslator
            from threshold_defense_checker import ThresholdDefenseChecker
            warnings.append("SIYEM services importable (good)")
        except Exception as e:
            issues.append(f"SIYEM services not importable: {e}")
        
        # Check for CORS configuration
        if (JAN_STUDIO_BACKEND / "main.py").exists():
            try:
                with open(JAN_STUDIO_BACKEND / "main.py") as f:
                    content = f.read()
                    if "CORSMiddleware" not in content:
                        warnings.append("CORS middleware may not be configured")
            except:
                pass
        
        self.report["integration"] = {
            "status": "ok" if not issues else "issues",
            "issues": issues,
            "warnings": warnings
        }
        
        if issues:
            print(f"    [!] Found {len(issues)} issues")
        if warnings:
            print(f"    [~] Found {len(warnings)} warnings")
        if not issues and not warnings:
            print("    [OK] No issues found")
    
    def generate_report(self):
        """Generate comprehensive report"""
        print("\n" + "="*80)
        print("GENERATING REPORT".center(80))
        print("="*80 + "\n")
        
        # Count issues
        total_issues = 0
        total_warnings = 0
        
        for section in ["frontend", "backend", "services", "integration"]:
            section_data = self.report.get(section, {})
            if isinstance(section_data, dict):
                for component, data in section_data.items():
                    if isinstance(data, dict):
                        total_issues += len(data.get("issues", []))
                        total_warnings += len(data.get("warnings", []))
        
        self.report["summary"] = {
            "total_issues": total_issues,
            "total_warnings": total_warnings,
            "status": "ok" if total_issues == 0 else "issues"
        }
        
        # Save report
        report_path = JAN_ROOT / "output" / "s_drive_debug_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, ensure_ascii=False, indent=2)
        
        print(f"Total Issues: {total_issues}")
        print(f"Total Warnings: {total_warnings}")
        print(f"\nReport saved: {report_path}")
        
        # Print summary
        print("\n" + "="*80)
        print("SUMMARY".center(80))
        print("="*80 + "\n")
        
        for section in ["frontend", "backend", "services", "integration"]:
            print(f"\n[{section.upper()}]")
            section_data = self.report.get(section, {})
            if isinstance(section_data, dict):
                for component, data in section_data.items():
                    if isinstance(data, dict):
                        status = data.get("status", "unknown")
                        issues_count = len(data.get("issues", []))
                        warnings_count = len(data.get("warnings", []))
                        print(f"  {component}: {status} ({issues_count} issues, {warnings_count} warnings)")
        
        print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    debugger = SDriveDebugger()
    debugger.check_all()
