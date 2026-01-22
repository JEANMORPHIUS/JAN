"""
Test script for spiritual vibration-based entity routing
Demonstrates how biological + spiritual state determines creative routing
"""

from entity_router import EntityRouter

def test_vibration_routing():
    print("="*80)
    print("SPIRITUAL VIBRATION ROUTING TEST".center(80))
    print("Biological + Spiritual State -> Entity Routing".center(80))
    print("="*80)
    
    router = EntityRouter()
    
    # Test scenarios
    scenarios = [
        {
            "name": "CRITICAL Biological State",
            "vibration": 5.0,
            "bio_status": "CRITICAL",
            "cw_state": False,
            "entity_pref": None
        },
        {
            "name": "ELEVATED Biological State",
            "vibration": 6.0,
            "bio_status": "ELEVATED",
            "cw_state": False,
            "entity_pref": None
        },
        {
            "name": "LOW Vibration (Recovery Mode)",
            "vibration": 2.5,
            "bio_status": "STABLE",
            "cw_state": False,
            "entity_pref": None
        },
        {
            "name": "BASELINE Vibration (Maintenance)",
            "vibration": 5.0,
            "bio_status": "STABLE",
            "cw_state": False,
            "entity_pref": None
        },
        {
            "name": "HIGH Vibration (Flow State)",
            "vibration": 7.5,
            "bio_status": "STABLE",
            "cw_state": False,
            "entity_pref": "jean_mahram"
        },
        {
            "name": "CW STATE (God-Level Vibing)",
            "vibration": 8.0,
            "bio_status": "STABLE",
            "cw_state": True,
            "entity_pref": "karasahin"
        },
        {
            "name": "PEAK Vibration (Foundation Work)",
            "vibration": 9.5,
            "bio_status": "STABLE",
            "cw_state": True,
            "entity_pref": "karasahin"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n[TEST {i}] {scenario['name']}")
        print(f"   Spiritual Vibration: {scenario['vibration']}/10")
        print(f"   Biological Status: {scenario['bio_status']}")
        print(f"   CW State: {scenario['cw_state']}")
        if scenario['entity_pref']:
            print(f"   Entity Preference: {scenario['entity_pref']}")
        
        routing = router.route_by_vibration(
            spiritual_vibration=scenario['vibration'],
            biological_status=scenario['bio_status'],
            cw_state=scenario['cw_state'],
            entity_preference=scenario['entity_pref']
        )
        
        print(f"\n   -> PRIMARY ENTITY: {routing['primary_entity']}")
        if routing['secondary_entity']:
            print(f"   -> SECONDARY ENTITY: {routing['secondary_entity']}")
        print(f"   -> MODE: {routing['mode']}")
        print(f"   -> WORK TYPE: {routing['work_type']}")
        print(f"   -> NOTE: {routing['note']}")
        
        if 'recommendations' in routing:
            print(f"\n   RECOMMENDATIONS:")
            for rec in routing['recommendations']:
                print(f"      • {rec}")
        
        print(f"\n   Duration Limit: {routing['duration_limit']}")
        print("-"*80)
    
    print("\n" + "="*80)
    print("[OK] Vibration-based routing operational".center(80))
    print("Spiritual state now determines creative capacity".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    test_vibration_routing()

