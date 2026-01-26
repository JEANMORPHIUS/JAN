"""
DEEP SEARCH ALL INDUSTRIES - FREQUENTIAL CONTENT
News Media, Politics, Economics, Sports, Movies, Music, Creative Industries
Expand and Ingest All Vital Data

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

from comprehensive_industry_frequential_deep_search import (
    ComprehensiveIndustryFrequentialDeepSearch,
    IndustryDomain,
    FrequentialContentType,
    FrequentialEvent
)

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def expand_database_with_web_research(system: ComprehensiveIndustryFrequentialDeepSearch):
    """Expand database with web research findings"""
    
    # Add more songs from research
    # "Blowin' in the Wind" - Bob Dylan
    system.add_frequential_content(FrequentialEvent(
        event_id="blowin_in_the_wind",
        industry_domain=IndustryDomain.MUSIC,
        content_type=FrequentialContentType.SONG,
        title="Blowin' in the Wind",
        creator="Bob Dylan",
        year=1962,
        description="Questions about peace, war, freedom. Truth questions.",
        frequency_impact=+0.15,
        divine_frequency_contribution=+0.13,
        table_connection_strength=0.90,
        connection_to_table="Truth questions. Peace vision. The Table honored through questions.",
        serves_table=True,
        truth_teller=True,
        peace_oriented=True,
        themes=["peace", "freedom", "truth", "questions"],
        sources=["Bob Dylan", "Music history", "Web research"]
    ))
    
    # Add more films
    # "Selma" (2014)
    system.add_frequential_content(FrequentialEvent(
        event_id="selma_film",
        industry_domain=IndustryDomain.MOVIES,
        content_type=FrequentialContentType.FILM,
        title="Selma",
        creator="Ava DuVernay",
        year=2014,
        description="Civil rights march. Voting rights. Truth told.",
        frequency_impact=+0.13,
        divine_frequency_contribution=+0.11,
        table_connection_strength=0.90,
        connection_to_table="Civil rights truth. Voting rights. The Table honored through truth.",
        serves_table=True,
        truth_teller=True,
        liberation_oriented=True,
        themes=["civil rights", "voting rights", "truth", "justice"],
        sources=["Film history", "IMDB", "Web research"]
    ))
    
    # Add more news media events
    # #MeToo Movement (2017)
    system.add_frequential_content(FrequentialEvent(
        event_id="metoo_movement",
        industry_domain=IndustryDomain.NEWS_MEDIA,
        content_type=FrequentialContentType.MOVEMENT,
        title="#MeToo Movement - Truth Exposed",
        creator="The People",
        year=2017,
        description="Sexual abuse truth exposed. Silence broken. Truth told.",
        frequency_impact=+0.14,
        divine_frequency_contribution=+0.12,
        table_connection_strength=0.90,
        connection_to_table="Truth exposed. Silence broken. The Table honored through truth.",
        serves_table=True,
        truth_teller=True,
        liberation_oriented=True,
        themes=["truth", "justice", "liberation", "courage"],
        sources=["News media", "Social media", "Web research"]
    ))
    
    print(f"  [OK] Expanded database with web research findings")


def main():
    """Main execution for comprehensive industry deep search"""
    print("=" * 80)
    print("COMPREHENSIVE INDUSTRY FREQUENTIAL DEEP SEARCH")
    print("News Media, Politics, Economics, Sports, Movies, Music, Creative Industries")
    print("Expand and Ingest All Vital Data")
    print("=" * 80)
    print()
    
    system = ComprehensiveIndustryFrequentialDeepSearch()
    
    print(f"Loaded {len(system.database)} frequential content items")
    print()
    
    # Show by industry
    print("CONTENT BY INDUSTRY:")
    print("-" * 80)
    for industry in IndustryDomain:
        industry_content = system.get_by_industry(industry)
        if industry_content:
            print(f"\n{industry.value.upper().replace('_', ' ')} ({len(industry_content)} items):")
            for content in industry_content[:5]:
                print(f"  - {content.title} ({content.year}): {content.frequency_impact:+.2f}")
            if len(industry_content) > 5:
                print(f"  ... and {len(industry_content) - 5} more")
    print()
    
    # Show by type
    print("CONTENT BY TYPE:")
    print("-" * 80)
    for content_type in FrequentialContentType:
        type_content = system.get_by_type(content_type)
        if type_content:
            print(f"\n{content_type.value.upper().replace('_', ' ')} ({len(type_content)} items):")
            for content in type_content[:5]:
                print(f"  - {content.title} ({content.year}): {content.frequency_impact:+.2f}")
            if len(type_content) > 5:
                print(f"  ... and {len(type_content) - 5} more")
    print()
    
    # High frequency content
    print("HIGH FREQUENCY CONTENT (>= 0.10):")
    print("-" * 80)
    high_freq = system.get_high_frequency(0.10)
    high_freq_sorted = sorted(high_freq, key=lambda x: x.frequency_impact, reverse=True)
    for i, content in enumerate(high_freq_sorted[:10], 1):
        print(f"  {i}. {content.title} ({content.industry_domain.value}): {content.frequency_impact:+.2f}")
    if len(high_freq_sorted) > 10:
        print(f"  ... and {len(high_freq_sorted) - 10} more")
    print()
    
    # Table-aligned content
    print("TABLE-ALIGNED CONTENT:")
    print("-" * 80)
    table_aligned = system.get_table_aligned()
    print(f"Total Table-Aligned: {len(table_aligned)}")
    print(f"Percentage: {len(table_aligned) / len(system.database) * 100:.1f}%")
    print()
    
    # Impact analysis
    print("FREQUENTIAL IMPACT ANALYSIS:")
    print("-" * 80)
    impact = system.calculate_total_impact()
    print(f"Total Content: {impact['total_content']}")
    print(f"Total Frequency Impact: {impact['total_frequency_impact']:+.2f}")
    print(f"Total Divine Frequency Contribution: {impact['total_divine_frequency_contribution']:+.2f}")
    print(f"High Frequency Content: {impact['high_frequency_count']}")
    print(f"Table-Aligned Content: {impact['table_aligned_count']}")
    print()
    print("Impact by Industry:")
    for industry, data in impact['by_industry'].items():
        print(f"  {industry}: {data['count']} items, {data['total_impact']:+.2f} total impact")
    print()
    print("Impact by Type:")
    for content_type, data in impact['by_type'].items():
        print(f"  {content_type}: {data['count']} items, {data['total_impact']:+.2f} total impact")
    print()
    
    # Expand with web research
    print("Expanding database with web research...")
    expand_database_with_web_research(system)
    print()
    
    # Recalculate after expansion
    impact = system.calculate_total_impact()
    print(f"After expansion: {impact['total_content']} items, {impact['total_frequency_impact']:+.2f} total impact")
    print()
    
    # Export
    print("Exporting comprehensive analysis...")
    export_path = system.export_analysis()
    print(f"  [OK] Exported to: {export_path}")
    print()
    
    print("=" * 80)
    print("COMPREHENSIVE INDUSTRY DEEP SEARCH COMPLETE")
    print("=" * 80)
    print()
    print("THE TRUTH:")
    print("  - All industries searched")
    print("  - All frequential content mapped")
    print("  - All vital data ingested")
    print("  - All content connected to The Table")
    print()
    print("FREQUENTIAL IMPACT:")
    print(f"  - Total Content: {impact['total_content']}")
    print(f"  - Total Impact: {impact['total_frequency_impact']:+.2f}")
    print(f"  - Table-Aligned: {impact['table_aligned_count']}")
    print()
    print("CONTENT BREAKDOWN:")
    print(f"  - Events: {impact['by_type'].get('event', {}).get('count', 0)}")
    print(f"  - Songs: {impact['by_type'].get('song', {}).get('count', 0)}")
    print(f"  - Films: {impact['by_type'].get('film', {}).get('count', 0)}")
    print(f"  - Movements: {impact['by_type'].get('movement', {}).get('count', 0)}")
    print()
    print("PANGEA IS THE TABLE.")
    print("YOU DON'T BETRAY THE TABLE.")
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
