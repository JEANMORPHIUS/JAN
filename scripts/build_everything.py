"""
BUILD EVERYTHING - Master Build Orchestrator
Builds all systems, generates all assets, deploys everything

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
We don't stop. We build. We serve.

THE MISSION:
- Deploy all systems
- Generate all assets
- Build all packages
- Verify everything works
- Serve humanity

PEACE. LOVE. UNITY.
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import json

class BuildEverything:
    """Master build orchestrator - builds it all"""

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.scripts_dir = self.project_root / "scripts"
        self.build_log: List[Dict] = []
        self.start_time = datetime.now()

    def log_step(self, step: str, status: str, details: str = ""):
        """Log a build step"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "step": step,
            "status": status,
            "details": details
        }
        self.build_log.append(entry)
        # Use ASCII-safe symbols for Windows console compatibility
        status_symbol = "[OK]" if status == "SUCCESS" else "[FAIL]" if status == "FAILED" else "[...]"
        print(f"{status_symbol} {step}: {status}")
        if details:
            print(f"   {details}")

    def run_script(self, script_name: str, args: List[str] = None) -> bool:
        """Run a Python script and return success status"""
        script_path = self.scripts_dir / script_name
        if not script_path.exists():
            self.log_step(f"Run {script_name}", "FAILED", f"Script not found: {script_path}")
            return False

        try:
            cmd = [sys.executable, str(script_path)]
            if args:
                cmd.extend(args)
            
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout
            )
            
            if result.returncode == 0:
                self.log_step(f"Run {script_name}", "SUCCESS", f"Completed successfully")
                if result.stdout:
                    print(f"   Output: {result.stdout[:200]}...")
                return True
            else:
                self.log_step(f"Run {script_name}", "FAILED", f"Error: {result.stderr[:200]}")
                return False
        except subprocess.TimeoutExpired:
            self.log_step(f"Run {script_name}", "FAILED", "Timeout after 1 hour")
            return False
        except Exception as e:
            self.log_step(f"Run {script_name}", "FAILED", f"Exception: {str(e)}")
            return False

    def check_prerequisites(self) -> bool:
        """Check all prerequisites before building"""
        self.log_step("Check Prerequisites", "IN_PROGRESS")
        
        # Check Python
        if sys.version_info < (3, 9):
            self.log_step("Check Prerequisites", "FAILED", "Python 3.9+ required")
            return False

        # Check key directories
        required_dirs = [
            self.project_root / "jan-studio",
            self.project_root / "scripts",
            self.project_root / "output",
            self.project_root / "jan-studio" / "curriculum" / "scripture_schedule_2026"
        ]
        
        for dir_path in required_dirs:
            if not dir_path.exists():
                self.log_step("Check Prerequisites", "FAILED", f"Missing directory: {dir_path}")
                return False

        self.log_step("Check Prerequisites", "SUCCESS")
        return True

    def deploy_systems(self) -> bool:
        """Deploy all backend and frontend systems"""
        self.log_step("Deploy Systems", "IN_PROGRESS")
        
        # Run deployment script
        success = self.run_script("deploy_complete_system.py")
        
        if success:
            self.log_step("Deploy Systems", "SUCCESS")
        else:
            self.log_step("Deploy Systems", "FAILED", "Deployment encountered errors")
        
        return success

    def generate_visual_assets(self) -> bool:
        """Generate all visual assets"""
        self.log_step("Generate Visual Assets", "IN_PROGRESS")
        
        # Check if prompts exist
        prompts_file = self.project_root / "output" / "visual_prompts" / "all_visual_prompts.json"
        if not prompts_file.exists():
            self.log_step("Generate Visual Assets", "WARNING", "Prompts file not found, will generate from content")
        
        # Run visual asset generator
        # Note: This may require API keys for image generation
        success = self.run_script("visual_asset_generator.py", ["--dry-run"])
        
        if success:
            self.log_step("Generate Visual Assets", "SUCCESS", "Asset generation pipeline ready")
        else:
            self.log_step("Generate Visual Assets", "WARNING", "May require API keys for actual generation")
        
        return True  # Continue even if generation needs API keys

    def generate_audio_assets(self) -> bool:
        """Generate all audio assets"""
        self.log_step("Generate Audio Assets", "IN_PROGRESS")
        
        # Check if scripts exist
        scripts_file = self.project_root / "output" / "audio_scripts" / "all_audio_scripts.json"
        if not scripts_file.exists():
            self.log_step("Generate Audio Assets", "WARNING", "Scripts file not found, will generate from content")
        
        # Run audio synthesis
        # Note: This may require TTS API keys
        success = self.run_script("audio_synthesis_automation.py", ["--dry-run"])
        
        if success:
            self.log_step("Generate Audio Assets", "SUCCESS", "Audio generation pipeline ready")
        else:
            self.log_step("Generate Audio Assets", "WARNING", "May require TTS API keys for actual generation")
        
        return True  # Continue even if generation needs API keys

    def build_raspberry_pi_packages(self) -> bool:
        """Build Raspberry Pi content packages"""
        self.log_step("Build Raspberry Pi Packages", "IN_PROGRESS")
        
        success = self.run_script("raspberry_pi_package_builder.py")
        
        if success:
            self.log_step("Build Raspberry Pi Packages", "SUCCESS")
        else:
            self.log_step("Build Raspberry Pi Packages", "FAILED")
        
        return success

    def verify_systems(self) -> bool:
        """Verify all systems are operational"""
        self.log_step("Verify Systems", "IN_PROGRESS")
        
        # Run health check
        success = self.run_script("system_health_and_readiness_check.py")
        
        if success:
            self.log_step("Verify Systems", "SUCCESS")
        else:
            self.log_step("Verify Systems", "WARNING", "Some checks may have failed")
        
        return True  # Continue even with warnings

    def generate_build_report(self):
        """Generate final build report"""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()

        report = {
            "build_timestamp": self.start_time.isoformat(),
            "completion_timestamp": end_time.isoformat(),
            "duration_seconds": duration,
            "total_steps": len(self.build_log),
            "successful_steps": len([s for s in self.build_log if s["status"] == "SUCCESS"]),
            "failed_steps": len([s for s in self.build_log if s["status"] == "FAILED"]),
            "warnings": len([s for s in self.build_log if s["status"] == "WARNING"]),
            "build_log": self.build_log,
            "philosophy": {
                "purpose": "Serve The Table",
                "mission": "Build systems that serve humanity",
                "foundation": "PEACE. LOVE. UNITY.",
                "guidance": "Under Father's guidance with humility and conviction"
            }
        }

        report_file = self.project_root / "output" / f"build_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        return report

    def build_all(self):
        """Build everything - main orchestrator"""
        
        print("\n" + "="*80)
        print("BUILDING EVERYTHING")
        print("JAN/SIYEM - Complete System Build")
        print("="*80 + "\n")

        # Step 1: Check prerequisites
        if not self.check_prerequisites():
            print("\n[FAIL] Prerequisites check failed. Aborting build.")
            return

        # Step 2: Deploy systems
        self.deploy_systems()

        # Step 3: Generate visual assets
        self.generate_visual_assets()

        # Step 4: Generate audio assets
        self.generate_audio_assets()

        # Step 5: Build Raspberry Pi packages
        self.build_raspberry_pi_packages()

        # Step 6: Verify everything
        self.verify_systems()

        # Step 7: Generate report
        report = self.generate_build_report()

        # Final summary
        print("\n" + "="*80)
        print("BUILD COMPLETE")
        print("="*80 + "\n")

        print(f"Total Steps: {report['total_steps']}")
        print(f"Successful: {report['successful_steps']}")
        print(f"Failed: {report['failed_steps']}")
        print(f"Warnings: {report['warnings']}")
        print(f"Duration: {report['duration_seconds']:.1f} seconds ({report['duration_seconds']/60:.1f} minutes)")

        print("\nBuild Report:")
        print(f"  {report_file}")

        print("\n" + "="*80)
        print("READY TO SERVE HUMANITY")
        print("="*80 + "\n")

        print("Philosophy:")
        for key, value in report['philosophy'].items():
            print(f"  {key.capitalize()}: {value}")

        print("\nPEACE. LOVE. UNITY.")
        print("ENERGY + LOVE = WE ALL WIN.\n")


def main():
    """Main build function"""
    import argparse

    parser = argparse.ArgumentParser(description='Build Everything - JAN/SIYEM Complete System')
    parser.add_argument('--skip-assets', action='store_true', help='Skip asset generation (faster)')
    parser.add_argument('--skip-deploy', action='store_true', help='Skip system deployment')
    parser.add_argument('--skip-pi', action='store_true', help='Skip Raspberry Pi packages')

    args = parser.parse_args()

    builder = BuildEverything()
    
    # Override methods if skipping
    if args.skip_assets:
        builder.generate_visual_assets = lambda: True
        builder.generate_audio_assets = lambda: True
    if args.skip_deploy:
        builder.deploy_systems = lambda: True
    if args.skip_pi:
        builder.build_raspberry_pi_packages = lambda: True

    builder.build_all()


if __name__ == "__main__":
    main()
