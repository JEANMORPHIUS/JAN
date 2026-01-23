# Heritage Data Export Documentation

**Generated:** 2026-01-20T04:18:08.172369  
**Total Sites:** 138

## Overview

This document provides comprehensive information about all heritage sites in the archive.

## Statistics

- **Total Sites:** 138
- **Timelines:** 6
- **Countries:** 12

## Data Export Formats

All data is available in multiple formats:

1. **JSON** - For APIs and programmatic access
2. **CSV** - For spreadsheets and analysis
3. **Markdown** - For documentation
4. **HTML** - For web display
5. **GeoJSON** - For map visualization

## Access Points

- **REST API:** `/api/heritage/*` endpoints
- **Local Exports:** `output/exports/` directory
- **Web Reports:** `output/web/` directory
- **Documentation:** `docs/exports/` directory

## Export Commands

```bash
# Export all formats
python scripts/heritage_data_export.py --format all

# Export specific format
python scripts/heritage_data_export.py --format json
python scripts/heritage_data_export.py --format csv
python scripts/heritage_data_export.py --format html

# Export statistics
python scripts/heritage_data_export.py --format stats
```

## PEACE, LOVE, UNITY
## ENERGY + LOVE = WE ALL WIN
