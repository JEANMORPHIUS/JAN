"""
Comprehensive API Test Suite
Tests all API endpoints across the system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
We test to serve, not to break.

THE MISSION:
Test all APIs:
- Marketplace APIs
- Authentication APIs
- Content APIs
- Heritage APIs
- Health checks

PEACE. LOVE. UNITY.
"""

import sys
import requests
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class APITester:
    """Comprehensive API testing suite"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip('/')
        self.results: List[Dict] = []
        self.session = requests.Session()
    
    def test_endpoint(self, method: str, path: str, expected_status: int = 200, 
                     data: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict:
        """Test a single API endpoint"""
        url = f"{self.base_url}{path}"
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers, timeout=5)
            elif method.upper() == "POST":
                response = self.session.post(url, json=data, headers=headers, timeout=5)
            elif method.upper() == "PUT":
                response = self.session.put(url, json=data, headers=headers, timeout=5)
            elif method.upper() == "DELETE":
                response = self.session.delete(url, headers=headers, timeout=5)
            else:
                return {"status": "FAILED", "error": f"Unsupported method: {method}"}
            
            success = response.status_code == expected_status
            result = {
                "method": method,
                "path": path,
                "expected_status": expected_status,
                "actual_status": response.status_code,
                "success": success,
                "timestamp": datetime.now().isoformat()
            }
            
            if not success:
                result["error"] = f"Expected {expected_status}, got {response.status_code}"
                try:
                    result["response"] = response.text[:200]
                except:
                    pass
            
            self.results.append(result)
            return result
            
        except requests.exceptions.ConnectionError:
            result = {
                "method": method,
                "path": path,
                "success": False,
                "error": "Connection refused - server not running",
                "timestamp": datetime.now().isoformat()
            }
            self.results.append(result)
            return result
        except Exception as e:
            result = {
                "method": method,
                "path": path,
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            self.results.append(result)
            return result
    
    def test_health_endpoints(self):
        """Test health check endpoints"""
        print("\n[TEST] Testing Health Endpoints...")
        self.test_endpoint("GET", "/health")
        self.test_endpoint("GET", "/api/health")
    
    def test_marketplace_apis(self):
        """Test marketplace API endpoints"""
        print("\n[TEST] Testing Marketplace APIs...")
        self.test_endpoint("GET", "/api/marketplace/personas")
        self.test_endpoint("GET", "/api/marketplace/categories")
        # Note: POST endpoints require authentication in production
    
    def test_auth_apis(self):
        """Test authentication API endpoints"""
        print("\n[TEST] Testing Authentication APIs...")
        # Test registration (may fail if validation is strict)
        self.test_endpoint("POST", "/api/auth/register", 
                          data={"username": "test", "email": "test@test.com", "password": "test123"},
                          expected_status=201)  # May be 400 if validation fails
    
    def test_content_apis(self):
        """Test content API endpoints"""
        print("\n[TEST] Testing Content APIs...")
        # These may not exist yet, but we test for graceful failures
        self.test_endpoint("GET", "/api/content/lessons", expected_status=200)
        self.test_endpoint("GET", "/api/content/posts", expected_status=200)
    
    def test_heritage_apis(self):
        """Test heritage API endpoints"""
        print("\n[TEST] Testing Heritage APIs...")
        self.test_endpoint("GET", "/api/heritage/sites", expected_status=200)
        self.test_endpoint("GET", "/api/heritage/timeline", expected_status=200)
    
    def run_all_tests(self):
        """Run all API tests"""
        print("="*80)
        print("COMPREHENSIVE API TEST SUITE")
        print("JAN/SIYEM Complete System")
        print("="*80)
        print(f"\nTesting against: {self.base_url}")
        print("\nNote: Some tests may fail if server is not running or endpoints don't exist yet.")
        
        self.test_health_endpoints()
        self.test_marketplace_apis()
        self.test_auth_apis()
        self.test_content_apis()
        self.test_heritage_apis()
        
        # Generate report
        self.generate_report()
    
    def generate_report(self):
        """Generate test report"""
        total = len(self.results)
        successful = sum(1 for r in self.results if r.get("success", False))
        failed = total - successful
        
        print("\n" + "="*80)
        print("TEST RESULTS")
        print("="*80)
        print(f"\nTotal Tests: {total}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        
        if failed > 0:
            print("\nFailed Tests:")
            for result in self.results:
                if not result.get("success", False):
                    print(f"  [FAIL] {result['method']} {result['path']}")
                    if "error" in result:
                        print(f"         Error: {result['error']}")
        
        # Save report
        report_file = Path(__file__).parent.parent / "output" / f"api_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "base_url": self.base_url,
            "total_tests": total,
            "successful": successful,
            "failed": failed,
            "results": self.results
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\nReport saved: {report_file}")
        print("\n" + "="*80)
        print("PEACE. LOVE. UNITY.")
        print("="*80 + "\n")


def main():
    """Main test function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test All APIs')
    parser.add_argument('--url', default='http://localhost:8000', help='Base URL for API')
    
    args = parser.parse_args()
    
    tester = APITester(base_url=args.url)
    tester.run_all_tests()


if __name__ == "__main__":
    main()
