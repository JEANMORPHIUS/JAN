"""
TEST SPORTING ORACLE
Quick test to demonstrate the harm prevention tool
"""

from sporting_oracle import SportingOracle, GameActivity
from datetime import datetime, timedelta

def test_sporting_oracle():
    """Test the Sporting Oracle."""
    
    print("=" * 60)
    print("SPORTING ORACLE - TEST")
    print("=" * 60)
    print()
    
    oracle = SportingOracle()
    user_id = "test_user_123"
    
    # Simulate gambling activities
    print("📊 Simulating gambling activities...")
    print()
    
    activities = [
        GameActivity("slots", 10.0, datetime.now() - timedelta(minutes=30), "loss"),
        GameActivity("slots", 20.0, datetime.now() - timedelta(minutes=25), "near_miss"),
        GameActivity("slots", 50.0, datetime.now() - timedelta(minutes=20), "loss"),
        GameActivity("blackjack", 100.0, datetime.now() - timedelta(minutes=15), "loss"),
        GameActivity("slots", 100.0, datetime.now() - timedelta(minutes=10), "loss"),
        GameActivity("roulette_american", 50.0, datetime.now() - timedelta(minutes=5), "loss"),
    ]
    
    # Record activities
    for activity in activities:
        oracle.record_activity(
            user_id=user_id,
            game_type=activity.game_type,
            bet_amount=activity.bet_amount,
            result=activity.result
        )
    
    print(f"Recorded {len(activities)} activities")
    print()
    
    # Analyze
    print("🔍 Analyzing house edge exposure...")
    print()
    
    result = oracle.analyze_user_activity(user_id)
    
    # Display results
    edge_detection = result['edge_detection']
    
    print("EDGE DETECTION RESULTS:")
    print(f"  House Edge: {edge_detection['house_edge']*100:.2f}%")
    print(f"  Expected Loss: ${edge_detection['expected_loss']:.2f}")
    print(f"  Total Wagered: ${edge_detection['total_wagered']:.2f}")
    print(f"  Risk Level: {edge_detection['risk_level'].upper()}")
    print(f"  Primary Game: {edge_detection['game_type']}")
    print(f"  Intervention Needed: {edge_detection['intervention_needed']}")
    print()
    
    print("RECOMMENDATIONS:")
    for rec in edge_detection['recommendations']:
        print(f"  • {rec}")
    print()
    
    # Show intervention if needed
    if result['intervention']:
        print("=" * 60)
        print("⚠️ INTERVENTION TRIGGERED")
        print("=" * 60)
        print()
        print(result['intervention']['message'])
        print()
        
        print("ORACLE ALTERNATIVE:")
        for key, value in result['intervention']['oracle_alternative'].items():
            print(f"  {key}: {value}")
        print()
        
        print("COMPARISON:")
        comparison = result['intervention']['comparison']
        print("  Gambling:")
        for key, value in comparison['gambling'].items():
            print(f"    {key}: {value}")
        print("  Oracle:")
        for key, value in comparison['oracle'].items():
            print(f"    {key}: {value}")
        print()
        
        print("ACTION ITEMS:")
        for item in result['intervention']['action_items']:
            print(f"  • {item}")
        print()
    
    print("=" * 60)
    print("THE FLIP:")
    print("  From: House edge 5-10% → To: 0%")
    print("  From: Expected loss $50-100 → To: $0")
    print("  From: Addiction risk High → To: None")
    print("  From: Transparency None → To: Full")
    print("  From: Extraction → To: Liberation")
    print("=" * 60)
    print()
    
    print("✅ Sporting Oracle test complete!")
    print()
    print("The house edge has been flipped.")
    print("The weapon is ready.")
    print("The liberation begins.")
    print()


if __name__ == "__main__":
    test_sporting_oracle()
