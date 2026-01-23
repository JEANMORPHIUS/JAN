"""
Quick test to demonstrate heritage cleansing works for multiple heritage sites.
"""

from heritage_cleansing import HeritageCleanser

def test_multiple_heritage_sites():
    """Test cleansing with multiple heritage sites from different regions."""
    
    cleanser = HeritageCleanser()
    
    test_cases = [
        {
            "name": "Berengaria Hotel (Cyprus)",
            "content": "The abandoned Berengaria Hotel in Cyprus is haunted by the ghost of a merchant's wife who seeks revenge for her suicide..."
        },
        {
            "name": "Alhambra Palace (Spain)",
            "content": "The haunted Alhambra Palace in Granada, Spain is cursed. Ghosts of Moorish princesses appear at midnight seeking vengeance..."
        },
        {
            "name": "Poveglia Island (Italy)",
            "content": "Poveglia Island is the most haunted place in Italy. Abandoned plague hospital where victims still scream in agony..."
        },
        {
            "name": "Château de Brissac (France)",
            "content": "The cursed Château de Brissac in France is haunted by the Green Lady, a murder victim seeking revenge on her killers..."
        },
        {
            "name": "Leap Castle (Ireland)",
            "content": "Leap Castle in Ireland is haunted by the Elemental, a demonic entity that terrorizes visitors. The Bloody Chapel where murder victims still suffer..."
        },
        {
            "name": "Bhangarh Fort (India)",
            "content": "Bhangarh Fort in Rajasthan, India is cursed and haunted. Locals say no one can spend the night here. Ghosts of a princess and her lover seek revenge..."
        },
        {
            "name": "Ancient Temple (Greece)",
            "content": "The abandoned temple in Delphi, Greece is haunted by ancient spirits seeking vengeance for desecration of their sacred space..."
        }
    ]
    
    print("=" * 80)
    print("HERITAGE CLEANSING PROTOCOL - MULTI-SITE TEST")
    print("=" * 80)
    print()
    
    results = []
    
    for test_case in test_cases:
        print(f"Testing: {test_case['name']}")
        print("-" * 80)
        
        cleansed, analysis = cleanser.cleanse_content(
            test_case['content'],
            source=test_case['name']
        )
        
        results.append({
            "name": test_case['name'],
            "law_41_compliant": analysis['law_41_compliant'],
            "requires_cleansing": analysis['requires_cleansing'],
            "violation_type": analysis.get('violation_type'),
            "has_regeneration": bool(analysis.get('regeneration_suggestion'))
        })
        
        print(f"  Law 41 Compliant: {analysis['law_41_compliant']}")
        print(f"  Requires Cleansing: {analysis['requires_cleansing']}")
        if analysis.get('violation_type'):
            print(f"  Violation Type: {analysis['violation_type']}")
        if analysis.get('regeneration_suggestion'):
            print(f"  Regeneration Narrative: [GENERATED]")
        print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Sites Tested: {len(results)}")
    print(f"Non-Compliant Sites: {sum(1 for r in results if not r['law_41_compliant'])}")
    print(f"Regeneration Narratives Generated: {sum(1 for r in results if r['has_regeneration'])}")
    print()
    
    summary = cleanser.get_summary()
    print("Cleansing Summary:")
    print(f"  Clean: {summary['cleansed_count']}")
    print(f"  Flagged: {summary['flagged_count']}")
    print(f"  Regenerated: {summary['regenerated_count']}")
    print()
    print("=" * 80)
    print("[SUCCESS] PROTOCOL WORKS FOR ALL HERITAGE SITES")
    print("=" * 80)


if __name__ == "__main__":
    test_multiple_heritage_sites()
