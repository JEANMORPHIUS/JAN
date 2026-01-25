"""
TEST ALL SYSTEMS - AUTOMATED
Test all endpoints and workflows automatically

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Test everything. Verify all systems.

PEACE. LOVE. UNITY.
"""

import sys
import requests
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

project_root = Path(__file__).parent.parent
backend_url = "http://localhost:8000"

class SystemTester:
    """Test all systems automatically"""
    
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "tests_passed": [],
            "tests_failed": [],
            "total_tests": 0
        }
        
    def test_endpoint(self, name: str, endpoint: str, method: str = "GET", data: dict = None) -> bool:
        """Test a single endpoint"""
        self.results["total_tests"] += 1
        try:
            if method == "GET":
                response = requests.get(f"{backend_url}{endpoint}", timeout=5)
            elif method == "POST":
                response = requests.post(f"{backend_url}{endpoint}", json=data, timeout=10)
            else:
                return False
                
            if response.status_code in [200, 201]:
                print(f"[OK] {name}: PASSED")
                self.results["tests_passed"].append(name)
                return True
            else:
                print(f"[FAIL] {name}: FAILED ({response.status_code})")
                self.results["tests_failed"].append(f"{name}: {response.status_code}")
                return False
        except Exception as e:
            print(f"[FAIL] {name}: ERROR ({str(e)})")
            self.results["tests_failed"].append(f"{name}: {str(e)}")
            return False
            
    def test_all(self):
        """Test all systems"""
        print("\n" + "="*80)
        print("TESTING ALL SYSTEMS")
        print("="*80 + "\n")
        
        # Core endpoints
        self.test_endpoint("Health Check", "/health")
        self.test_endpoint("API Docs", "/docs")
        
        # JAN APIs
        self.test_endpoint("JAN Personas List", "/api/jan/personas")
        self.test_endpoint("JAN Templates", "/api/templates/list")
        
        # Marketplace
        self.test_endpoint("Marketplace Browse", "/api/marketplace/personas")
        self.test_endpoint("Marketplace Categories", "/api/marketplace/categories")
        
        # Channel Collaboration
        self.test_endpoint("Channel Collaboration", "/api/channel-collaboration/channels")
        self.test_endpoint("Present Purpose", "/api/channel-collaboration/present-purpose")
        
        # Educational
        self.test_endpoint("Educational Overview", "/api/educational/overview")
        
        # Heritage
        self.test_endpoint("Heritage Meridian API", "/api/heritage-meridian/overview")
        
        # Save report
        report_file = project_root / "output" / "system_test_report.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.results["status"] = "COMPLETE"
        self.results["pass_rate"] = len(self.results["tests_passed"]) / self.results["total_tests"] * 100 if self.results["total_tests"] > 0 else 0
        
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
            
        print("\n" + "="*80)
        print("TESTING COMPLETE")
        print("="*80 + "\n")
        print(f"[OK] Passed: {len(self.results['tests_passed'])}/{self.results['total_tests']}")
        print(f"[FAIL] Failed: {len(self.results['tests_failed'])}/{self.results['total_tests']}")
        print(f"Pass Rate: {self.results['pass_rate']:.1f}%")
        print(f"\nReport: {report_file}\n")

if __name__ == "__main__":
    tester = SystemTester()
    tester.test_all()
