"""REAL WORLD LIVE INGESTION
Pulls live data (USGS, EONET) into the real-world integration system.

Usage:
    python scripts/real_world_live_ingest.py

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

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

import os
from typing import List

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from real_world_integration import get_real_world_integration_system


def parse_sources(raw: str) -> List[str]:
    if not raw:
        return ["usgs", "eonet"]
    return [item.strip().lower() for item in raw.split(",") if item.strip()]


def main() -> None:
    sources = parse_sources(os.getenv("REAL_WORLD_SOURCES", "usgs,eonet"))
    max_items = int(os.getenv("REAL_WORLD_MAX_ITEMS", "50"))

    system = get_real_world_integration_system()
    result = system.ingest_sources(sources=sources, max_items=max_items)

    print("Ingestion complete")
    print(result)


if __name__ == "__main__":
    main()
