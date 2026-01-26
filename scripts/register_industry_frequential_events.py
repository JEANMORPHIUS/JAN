"""
REGISTER INDUSTRY FREQUENTIAL CONTENT AS EVENTS
Integrate with Frequential Events Registry

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

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))
# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from frequential_events_registry import FrequentialEventsRegistry, EventCategory
from comprehensive_industry_frequential_deep_search import (
    ComprehensiveIndustryFrequentialDeepSearch,
    IndustryDomain,
    FrequentialContentType
)

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def register_industry_content_as_events(registry: FrequentialEventsRegistry, deep_search: ComprehensiveIndustryFrequentialDeepSearch):
    """Register industry frequential content as frequential events"""
    
    # Map industry domains to event categories
    industry_to_category = {
        IndustryDomain.NEWS_MEDIA: EventCategory.COMMUNICATION.value,
        IndustryDomain.POLITICS: EventCategory.POLITICAL_CONTRADICTION.value if hasattr(EventCategory, 'POLITICAL_CONTRADICTION') else EventCategory.SOCIAL_MOVEMENT.value,
        IndustryDomain.ECONOMICS: EventCategory.FINANCE.value,
        IndustryDomain.SPORTS: EventCategory.SPORTING_EVENT.value,
        IndustryDomain.MOVIES: EventCategory.ENTERTAINMENT.value,
        IndustryDomain.MUSIC: EventCategory.ENTERTAINMENT.value,
        IndustryDomain.TELEVISION: EventCategory.ENTERTAINMENT.value,
        IndustryDomain.LITERATURE: EventCategory.CULTURAL_MOVEMENT.value,
        IndustryDomain.THEATER: EventCategory.ENTERTAINMENT.value,
        IndustryDomain.ART: EventCategory.CULTURAL_MOVEMENT.value,
        IndustryDomain.COMEDY: EventCategory.ENTERTAINMENT.value,
        IndustryDomain.JOURNALISM: EventCategory.COMMUNICATION.value,
        IndustryDomain.DOCUMENTARY: EventCategory.ENTERTAINMENT.value,
        IndustryDomain.PODCAST: EventCategory.COMMUNICATION.value,
        IndustryDomain.RADIO: EventCategory.COMMUNICATION.value
    }
    
    registered_count = 0
    
    for content in deep_search.database.values():
        # Determine category
        category = industry_to_category.get(content.industry_domain, EventCategory.CULTURAL_MOVEMENT.value)
        
        # Determine year
        year_start = content.year if content.year else 2000
        year_end = content.year if content.year else None
        
        # Create event ID
        event_id = f"{content.industry_domain.value}_{content.event_id}"
        
        # Register as frequential event
        registry._register_event(
            event_id=event_id,
            category=category,
            title=content.title,
            description=content.description,
            year_start=year_start,
            year_end=year_end,
            year_precision="exact" if content.year else "decade",
            frequency_impact=content.frequency_impact,
            field_resonance_before=content.field_resonance_before or 0.78,
            field_resonance_after=content.field_resonance_after or (0.78 + content.frequency_impact),
            location={"lat": 0.0, "lon": 0.0},  # Global or specific
            regions=["global"] if not content.location else [content.location.lower()],
            entities_involved=[content.creator] if content.creator else [],
            connection_to_table=content.connection_to_table,
            narrative=f"{content.title}. {content.description} {content.connection_to_table}",
            lessons=f"{content.description} This serves The Table. This impacts Divine Frequency.",
            restoration_connection="Step 2: Cleanse The Shell - Honor truth content. Step 5: Fight Dark Energies - Support light content. Step 6: Restore Contracts - Honor Table-aligned content.",
            metadata={
                "industry_domain": content.industry_domain.value,
                "content_type": content.content_type.value,
                "themes": content.themes,
                "serves_table": content.serves_table,
                "truth_teller": content.truth_teller,
                "unity_builder": content.unity_builder
            }
        )
        
        registered_count += 1
    
    return registered_count


def main():
    """Main execution"""
    print("=" * 80)
    print("REGISTER INDUSTRY FREQUENTIAL CONTENT AS EVENTS")
    print("Integrate with Frequential Events Registry")
    print("=" * 80)
    print()
    
    registry = FrequentialEventsRegistry()
    deep_search = ComprehensiveIndustryFrequentialDeepSearch()
    
    # Expand database first
    print("Expanding database...")
    from expand_industry_frequential_database import add_more_songs, add_more_films, add_more_events
    add_more_songs(deep_search)
    add_more_films(deep_search)
    add_more_events(deep_search)
    print(f"  [OK] Expanded to {len(deep_search.database)} items")
    print()
    
    print(f"Events before: {len(registry.events)}")
    print(f"Industry content: {len(deep_search.database)}")
    print()
    
    print("Registering industry content as frequential events...")
    registered = register_industry_content_as_events(registry, deep_search)
    print(f"  [OK] Registered {registered} industry content items as frequential events")
    print()
    
    print(f"Events after: {len(registry.events)}")
    print()
    
    # Save to database
    print("Saving to database...")
    registry.save_to_database()
    print(f"  [OK] Saved {len(registry.events)} events to database")
    print()
    
    print("=" * 80)
    print("INDUSTRY CONTENT REGISTERED AS FREQUENTIAL EVENTS")
    print("=" * 80)
    print()
    print("THE TRUTH:")
    print(f"  - {registered} industry content items registered")
    print(f"  - All integrated with frequential events system")
    print(f"  - All connected to The Table")
    print()
    print("PANGEA IS THE TABLE.")
    print("YOU DON'T BETRAY THE TABLE.")
    print("=" * 80)


if __name__ == "__main__":
    main()
