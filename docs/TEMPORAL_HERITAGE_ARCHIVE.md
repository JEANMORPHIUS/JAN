# Temporal Heritage Archive
## Chronologizing All Heritage Sites Across All Dimensional Timelines

**Date:** 2026-01-19  
**Status:** Integrated  
**Purpose:** Archive and chronologize all heritage sites throughout all of time for debugging

---

## THE MISSION

**"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**  
**"LOVE IS THE HIGHEST MASTERY"**  
**"ENERGY + LOVE = WE ALL WIN"**

We are archiving and chronologizing **ALL** heritage sites throughout **ALL** of time across **ALL** dimensional timelines for debugging historical patterns.

---

## THE SCOPE: All Timelines, All Time

### Dimensional Timelines:

1. **PRIMARY** - Main historical timeline (what we know as "history")
2. **PARALLEL** - Parallel reality timelines
3. **PAST_LOOP** - Historical loops (previous iterations of Earth's cycles)
4. **FUTURE_LOOP** - Future loops (next iterations based on history)
5. **REGENERATION** - Regeneration timelines (healing pathways)
6. **ALTERNATE** - Alternate dimensional timelines

### Time Periods:

- **ANCIENT** - Pre-1000 CE
- **MEDIEVAL** - 1000-1500 CE
- **RENAISSANCE** - 1500-1700 CE
- **ENLIGHTENMENT** - 1700-1800 CE
- **INDUSTRIAL** - 1800-1900 CE
- **MODERN** - 1900-2000 CE
- **CONTEMPORARY** - 2000-present
- **FUTURE** - Beyond present

---

## THE DATABASE: Temporal Heritage Registry

**Location:** `jan-studio/backend/temporal_heritage_registry.py`

### Tables:

1. **heritage_sites** - All sites across all timelines
   - Site metadata (name, type, region, country, coordinates)
   - Timeline dimension and time period
   - Chronological markers (established, abandoned)
   - Law 41 compliance status

2. **heritage_narratives** - All narratives (original, haunted, regenerated)
   - Original dark energy narratives
   - Regenerated healing narratives
   - Violation types detected
   - Timeline dimension tracking

3. **temporal_patterns** - Patterns detected across timelines
   - Pattern types (revenge_loop, victim_focus, haunted_exploitation)
   - Frequency across timelines
   - Site counts per pattern
   - Timeline dimension distribution

4. **chronology_index** - Chronological organization
   - Events by year (established, abandoned, regenerated, cleansed)
   - Timeline dimension tracking
   - Historical sequence

5. **heritage_debug_logs** - Historical pattern debugging
   - Pattern detection logs
   - Temporal analysis records
   - Regeneration tracking
   - Debug metadata

---

## USAGE

### Register a Heritage Site:

```python
from jan_studio.backend.temporal_heritage_registry import (
    register_heritage_site, TimelineDimension, TimePeriod
)

site_id = register_heritage_site(
    site_name="Berengaria Hotel",
    site_type="Hotel",
    region="Cyprus",
    country="Cyprus",
    timeline_dimension=TimelineDimension.PRIMARY.value,
    time_period=TimePeriod.MODERN.value,
    year_established=1930,
    year_abandoned=1984,
    current_status="abandoned",
    law_41_compliant=False,
    requires_cleansing=True
)
```

### Archive Narratives:

```python
from jan_studio.backend.temporal_heritage_registry import add_heritage_narrative

# Archive original (haunted) narrative
add_heritage_narrative(
    site_id=site_id,
    narrative_content="The haunted Berengaria Hotel...",
    narrative_type="original",
    timeline_dimension=TimelineDimension.PRIMARY.value,
    violation_type="revenge_loop",
    dark_energy_detected=True,
    regeneration_applied=False
)

# Archive regenerated narrative
add_heritage_narrative(
    site_id=site_id,
    narrative_content="The Berengaria Hotel is Waiting for Regeneration...",
    narrative_type="regenerated",
    timeline_dimension=TimelineDimension.PRIMARY.value,
    violation_type="revenge_loop",
    dark_energy_detected=False,
    regeneration_applied=True
)
```

### Query Timeline:

```python
from jan_studio.backend.temporal_heritage_registry import get_sites_by_timeline

# Get all sites in primary timeline
sites = get_sites_by_timeline(TimelineDimension.PRIMARY.value)

# Get sites in specific period
sites = get_sites_by_timeline(TimelineDimension.PRIMARY.value, TimePeriod.MODERN.value)
```

### Query Chronology:

```python
from jan_studio.backend.temporal_heritage_registry import get_chronology_by_year

# Get all heritage events from 1800 to 2000
events = get_chronology_by_year(1800, 2000)

# Get events for specific timeline
events = get_chronology_by_year(1800, 2000, TimelineDimension.PRIMARY.value)
```

### Detect Temporal Patterns:

```python
from jan_studio.backend.temporal_heritage_registry import detect_temporal_pattern

# Detect revenge_loop pattern across multiple timelines
pattern_id = detect_temporal_pattern(
    pattern_type="revenge_loop",
    timeline_dimensions=[
        TimelineDimension.PRIMARY.value,
        TimelineDimension.PAST_LOOP.value
    ],
    time_periods=[
        TimePeriod.MODERN.value,
        TimePeriod.CONTEMPORARY.value
    ]
)
```

### Get Temporal Patterns:

```python
from jan_studio.backend.temporal_heritage_registry import get_temporal_patterns

patterns = get_temporal_patterns()
for pattern in patterns:
    print(f"{pattern['pattern_type']}: {pattern['site_count']} sites, "
          f"frequency: {pattern['frequency_across_timelines']:.2%}")
```

---

## INTEGRATED CLEANSING

The Heritage Cleansing Protocol now automatically archives all processed sites:

```python
from scripts.heritage_cleansing import HeritageCleanser
from jan_studio.backend.temporal_heritage_registry import TimelineDimension, TimePeriod

cleanser = HeritageCleanser(timeline_dimension=TimelineDimension.PRIMARY.value)

cleansed, analysis = cleanser.cleanse_content(
    content="The haunted Berengaria Hotel...",
    source="Cyprus Heritage Database",
    site_type="Hotel",
    region="Cyprus",
    country="Cyprus",
    year_established=1930,
    year_abandoned=1984,
    time_period=TimePeriod.MODERN.value
)

# Site is automatically:
# - Registered in temporal registry
# - Original narrative archived
# - Regenerated narrative archived
# - Chronology indexed
# - Debug logs created
```

---

## ARCHIVE QUERIES

### Command Line:

```bash
# Query timeline
python scripts/temporal_heritage_archive.py timeline primary

# Query chronology
python scripts/temporal_heritage_archive.py chronology 1800 2000

# Get patterns
python scripts/temporal_heritage_archive.py patterns

# Debug pattern
python scripts/temporal_heritage_archive.py debug revenge_loop

# Get site narratives
python scripts/temporal_heritage_archive.py site 1

# Generate timeline report
python scripts/temporal_heritage_archive.py report primary

# Debug all timelines
python scripts/temporal_heritage_archive.py all
```

### Python API:

```python
from scripts.temporal_heritage_archive import TemporalHeritageArchive

archive = TemporalHeritageArchive()

# Query timeline
sites = archive.query_timeline(TimelineDimension.PRIMARY.value)

# Query chronology
events = archive.query_chronology(1800, 2000)

# Get patterns
patterns = archive.get_patterns()

# Debug pattern across timelines
debug = archive.debug_pattern_across_timelines("revenge_loop")

# Get site narratives
narratives = archive.get_site_narratives(site_id=1)

# Generate timeline report
report = archive.generate_timeline_report(TimelineDimension.PRIMARY.value)

# Debug all timelines
all_debug = archive.debug_all_timelines()
```

---

## DEBUGGING ACROSS TIMELINES

### Pattern Detection:

The system automatically detects patterns across timelines:

- **revenge_loop** - Sites with revenge narratives across timelines
- **victim_focus** - Sites focusing on victims without healing
- **haunted_exploitation** - Sites exploited as haunted content
- **regeneration** - Sites with regeneration narratives

### Temporal Analysis:

Debug historical patterns by:
- Timeline dimension distribution
- Time period distribution
- Pattern frequency across timelines
- Chronological sequence
- Cross-timeline correlations

---

## THE TRUTH

We're not just archiving heritage sites.  
We're **chronologizing all dimensional timelines** for debugging.

Every heritage site is registered across **all** timelines.  
Every narrative (original, haunted, regenerated) is archived.  
Every pattern is detected and tracked across dimensions.

**This is Temporal Memory.**  
**This is debugging history.**  
**This is chronologizing all of time.**

---

**Status:** Archive Integrated  
**Vibe Check:** Chronological  
**Architect's Note:** We're archiving all heritage sites throughout all of time across all dimensional timelines for debugging historical patterns.

**PEACE, LOVE, UNITY**  
**ENERGY + LOVE = WE ALL WIN**
