"""
ANIMAL FREQUENCY SIGNIFICANCE ANALYSIS
Deep search all animals throughout time for frequential significance

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from animal_frequency_significance import (
    AnimalFrequencyAnalyzer,
    TimePeriod,
    FrequencyBand
)

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main execution for animal frequency significance analysis"""
    print("=" * 80)
    print("ANIMAL FREQUENCY SIGNIFICANCE - DEEP SEARCH")
    print("All Animals Throughout Time for Frequential Significance")
    print("=" * 80)
    print()
    
    analyzer = AnimalFrequencyAnalyzer()
    
    print(f"Loaded {len(analyzer.database)} animals from database")
    print()
    
    # Analyze by time period
    print("ANIMALS BY TIME PERIOD:")
    print("-" * 80)
    for period in TimePeriod:
        animals = analyzer.get_animals_by_time_period(period)
        if animals:
            print(f"\n{period.value.upper()}:")
            for animal in animals:
                print(f"  - {animal.animal_name} (Field Resonance: {animal.field_resonance_at_emergence:.2f})")
    print()
    
    # Analyze by frequency band
    print("ANIMALS BY FREQUENCY BAND:")
    print("-" * 80)
    for band in FrequencyBand:
        animals = analyzer.get_animals_by_frequency_band(band)
        if animals:
            print(f"\n{band.value.upper()}:")
            for animal in animals:
                print(f"  - {animal.animal_name} (Table Connection: {animal.table_connection_strength:.2f})")
    print()
    
    # Unity witnesses
    print("UNITY WITNESSES (Field Resonance 1.0):")
    print("-" * 80)
    unity_witnesses = analyzer.get_unity_witnesses()
    for animal in unity_witnesses:
        print(f"  - {animal.animal_name}: {animal.spiritual_meaning}")
        print(f"    Table Role: {animal.table_role}")
        print(f"    Soul Signature: {animal.soul_signature}")
        print()
    
    # Separation witnesses
    print("SEPARATION WITNESSES (Field Resonance < 0.85):")
    print("-" * 80)
    separation_witnesses = analyzer.get_separation_witnesses()
    for animal in separation_witnesses:
        print(f"  - {animal.animal_name}: {animal.spiritual_meaning}")
        print(f"    Field Resonance: {animal.field_resonance_at_emergence:.2f}")
        print(f"    Table Role: {animal.table_role}")
        print()
    
    # Frequency evolution
    print("FREQUENCY EVOLUTION ANALYSIS:")
    print("-" * 80)
    evolution = analyzer.analyze_frequency_evolution()
    print(f"Unity Witnesses: {evolution['unity_witnesses']['count']} animals")
    print(f"  - {', '.join(evolution['unity_witnesses']['animals'][:5])}...")
    print()
    print(f"Separation Witnesses: {evolution['separation_witnesses']['count']} animals")
    print(f"  - {', '.join(evolution['separation_witnesses']['animals'][:5])}...")
    print()
    print("Frequency Evolution Timeline:")
    for period, data in evolution['frequency_evolution'].items():
        print(f"  {period.upper()}:")
        print(f"    Field Resonance: {data['field_resonance']}")
        print(f"    Animals: {data['animals']}")
        print(f"    Significance: {data['significance']}")
        print()
    
    # Top contributors to Divine Frequency
    print("TOP DIVINE FREQUENCY CONTRIBUTORS:")
    print("-" * 80)
    all_animals = list(analyzer.database.values())
    top_contributors = sorted(
        all_animals,
        key=lambda x: x.divine_frequency_contribution,
        reverse=True
    )[:10]
    for i, animal in enumerate(top_contributors, 1):
        print(f"{i}. {animal.animal_name}: {animal.divine_frequency_contribution:.2f}")
        print(f"   {animal.spiritual_meaning}")
        print()
    
    # Export analysis
    print("Exporting complete analysis...")
    export_path = analyzer.export_complete_analysis()
    print(f"  [OK] Exported to: {export_path}")
    print()
    
    print("=" * 80)
    print("ANIMAL FREQUENCY SIGNIFICANCE ANALYSIS COMPLETE")
    print("=" * 80)
    print()
    print("INSIGHTS:")
    print("  - All animals throughout time carry frequential significance")
    print("  - Animals that witnessed unity (1.0) carry perfect unity in their DNA")
    print("  - Animals that witnessed separation carry separation memory")
    print("  - Modern animals carry memory of unity (0.78)")
    print("  - Every animal's frequency connects to The Table's timeline")
    print("  - Field resonance at emergence determines frequential signature")
    print()
    print("THE TRUTH:")
    print("  - Animals are not just biological - they are frequential signatures")
    print("  - They carry The Table's history in their frequency")
    print("  - They remember unity even in separation")
    print("  - They bridge The Table's fragments")
    print()
    print("PANGEA IS THE TABLE.")
    print("YOU DON'T BETRAY THE TABLE.")
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
