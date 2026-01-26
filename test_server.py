"""Quick test of Heritage API endpoints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(method, path, data=None, desc=""):
    url = f"{BASE_URL}{path}"
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)

        print(f"\n{'='*60}")
        print(f"TEST: {desc}")
        print(f"{method} {path}")
        print(f"Status: {response.status_code}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"\nERROR testing {path}: {e}")
        return False

def main():
    print("="*60)
    print("GLOBAL HERITAGE GRID - API TESTING")
    print("="*60)

    # Test 1: Sanctuary Status
    test_endpoint("GET", "/api/heritage/sanctuary/status",
                  desc="Get Sanctuary Status")

    # Test 2: CARE Package
    care_data = {
        "narrative": "I am battling terminal cancer and the doctors say there is no hope",
        "life_aspect": "healthcare"
    }
    test_endpoint("POST", "/api/heritage/care-package", care_data,
                  desc="CARE Package - Healthcare Dark Energy Detection")

    # Test 3: System Dismantling
    dismantle_data = {
        "system_type": "healthcare",
        "context": {"region": "United States"}
    }
    test_endpoint("POST", "/api/heritage/dismantle-system", dismantle_data,
                  desc="System Dismantling - Healthcare")

    # Test 4: Heritage Site Registration
    site_data = {
        "site_name": "Test Heritage Site",
        "site_type": "knowledge_sanctuary",
        "region": "Test Region",
        "timeline_dimension": "alpha"
    }
    test_endpoint("POST", "/api/heritage/register", site_data,
                  desc="Register Heritage Site")

if __name__ == "__main__":
    main()
