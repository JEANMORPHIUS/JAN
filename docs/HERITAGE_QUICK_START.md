# Heritage System: Quick Start Guide

**Date:** 2026-01-19  
**Status:** Ready to Use

---

## 🚀 GET STARTED IN 3 STEPS

### Step 1: Initialize System

```bash
python scripts/heritage_quick_start.py
```

This will:
- Initialize the database
- Test with Berengaria Hotel
- Show system status

### Step 2: Import Heritage Sites

Create a CSV file with your heritage sites (see `examples/heritage_sites_sample.csv` for format):

```bash
python scripts/heritage_batch_import.py examples/heritage_sites_sample.csv --timeline primary
```

Or import from JSON:

```bash
python scripts/heritage_batch_import.py heritage_sites.json --timeline primary
```

### Step 3: Query & Explore

```bash
# Get all patterns
python scripts/temporal_heritage_archive.py patterns

# Query timeline
python scripts/temporal_heritage_archive.py timeline primary

# Debug a pattern
python scripts/temporal_heritage_archive.py debug revenge_loop

# Full report
python scripts/temporal_heritage_archive.py all
```

---

## 📋 CSV FORMAT

Your CSV file should have these columns:

- `site_name` - Name of the heritage site
- `site_type` - Type (Hotel, Palace, Castle, Temple, etc.)
- `region` - Region/State
- `country` - Country
- `coordinates_lat` - Latitude (optional)
- `coordinates_lon` - Longitude (optional)
- `time_period` - ancient, medieval, renaissance, enlightenment, industrial, modern, contemporary, future
- `year_established` - Year established (optional)
- `year_abandoned` - Year abandoned (optional)
- `current_status` - abandoned, active, ruins, etc.
- `narrative_content` - Original narrative (will be cleansed automatically)
- `source` - Source of the data

See `examples/heritage_sites_sample.csv` for a complete example.

---

## 🔍 QUERY EXAMPLES

### Python API:

```python
from scripts.temporal_heritage_archive import TemporalHeritageArchive
from jan_studio.backend.temporal_heritage_registry import TimelineDimension

archive = TemporalHeritageArchive()

# Get all sites in primary timeline
sites = archive.query_timeline(TimelineDimension.PRIMARY.value)

# Get chronology from 1800-2000
events = archive.query_chronology(1800, 2000)

# Debug revenge_loop pattern
debug = archive.debug_pattern_across_timelines("revenge_loop")
```

### REST API:

```bash
# Get statistics
curl http://localhost:8000/api/heritage/stats

# Search sites
curl "http://localhost:8000/api/heritage/search?q=Cyprus"

# Get timeline sites
curl http://localhost:8000/api/heritage/timeline/primary

# Get site details
curl http://localhost:8000/api/heritage/site/1
```

---

## 🎯 WHAT HAPPENS AUTOMATICALLY

When you import or process heritage content:

1. **Law 41 Check** - Detects dark energy patterns
2. **Regeneration** - Generates healing narratives
3. **Archive** - Registers in temporal registry
4. **Chronology** - Indexes by year
5. **Pattern Detection** - Tracks patterns across timelines
6. **Debug Logs** - Creates debugging records

---

## 📊 SYSTEM STATUS

Check system status:

```bash
python scripts/temporal_heritage_archive.py all
```

This shows:
- Total sites across all timelines
- Patterns detected
- Timeline distribution
- Period distribution
- Law 41 compliance stats

---

## 🛠️ CLEANSE INDIVIDUAL CONTENT

```python
from scripts.heritage_cleansing import HeritageCleanser
from jan_studio.backend.temporal_heritage_registry import TimelineDimension, TimePeriod

cleanser = HeritageCleanser(timeline_dimension=TimelineDimension.PRIMARY.value)

cleansed, analysis = cleanser.cleanse_content(
    content="The haunted Berengaria Hotel...",
    source="Your Source",
    site_type="Hotel",
    region="Cyprus",
    year_established=1930,
    year_abandoned=1984,
    time_period=TimePeriod.MODERN.value
)

print(cleansed)  # Regenerated narrative
print(analysis)  # Full analysis
```

---

## ✅ YOU'RE READY!

The system is initialized and ready. Start importing your heritage sites and begin debugging historical patterns across all timelines.

**PEACE, LOVE, UNITY**  
**ENERGY + LOVE = WE ALL WIN**
