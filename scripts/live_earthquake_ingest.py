"""
LIVE EARTHQUAKE INGEST
Real-time ingestion of global earthquake data into the Real World Data Research framework.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Connect real-time global earthquake feeds (USGS, EMSC) to our
RealWorldDataResearch system so the Grid and Temporal Archive
stay in sync with the living Earth.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from real_world_data_research import RealWorldDataResearch, EventType


USGS_FEED_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
    "all_hour.geojson"
)


def _safe_get(d: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Small helper for dict lookups."""
    return d.get(key, default) if isinstance(d, dict) else default


def fetch_usgs_feed(url: str = USGS_FEED_URL) -> Dict[str, Any]:
    """Fetch USGS GeoJSON earthquake feed."""
    req = Request(url, headers={"User-Agent": "JAN-GlobalGrid/1.0"})
    try:
        with urlopen(req, timeout=15) as resp:
            data = resp.read().decode("utf-8")
        return json.loads(data)
    except (URLError, HTTPError, json.JSONDecodeError) as exc:
        print(f"[USGS] Error fetching feed: {exc}")
        return {}


def map_usgs_feature_to_event_args(
    feature: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """
    Map a single USGS GeoJSON feature into arguments
    for RealWorldDataResearch.document_event.
    """
    props = _safe_get(feature, "properties", {})
    geom = _safe_get(feature, "geometry", {})
    coords = _safe_get(geom, "coordinates", [])

    if not isinstance(coords, list) or len(coords) < 2:
        return None

    lon, lat = coords[0], coords[1]
    mag = _safe_get(props, "mag")
    place = _safe_get(props, "place", "Unknown location")
    time_ms = _safe_get(props, "time")

    # Convert epoch ms to date
    if isinstance(time_ms, (int, float)):
        dt = datetime.fromtimestamp(time_ms / 1000.0, tz=timezone.utc)
    else:
        dt = datetime.now(timezone.utc)

    # Very lightweight region/country extraction from 'place'
    region = place
    country = "Unknown"

    # Basic tectonic plate guess placeholder - can be enhanced later
    tectonic_plates = ["unknown"]

    return {
        "event_name": f"USGS {place}",
        "event_type": EventType.NATURAL_DISASTER.value,
        "date": dt.date(),
        "location": {"lat": float(lat), "lon": float(lon)},
        "region": region,
        "country": country,
        "tectonic_plates": tectonic_plates,
        "magnitude": float(mag) if mag is not None else None,
        "description": f"USGS real-time earthquake: {place}, magnitude {mag}",
        "sources": ["USGS"],
        "research_notes": "Ingested from USGS real-time GeoJSON feed (all_hour).",
    }


def ingest_usgs_recent(
    research: Optional[RealWorldDataResearch] = None,
    max_events: int = 50,
) -> List[str]:
    """
    Ingest recent earthquakes from USGS feed into RealWorldDataResearch.

    Args:
        research: Optional existing RealWorldDataResearch instance.
        max_events: Limit number of events to ingest from feed.

    Returns:
        List of event_ids that were created.
    """
    if research is None:
        research = RealWorldDataResearch()

    feed = fetch_usgs_feed()
    features = _safe_get(feed, "features", [])

    if not features:
        print("[USGS] No features in feed.")
        return []

    created_ids: List[str] = []
    count = 0

    for feature in features:
        if count >= max_events:
            break

        args = map_usgs_feature_to_event_args(feature)
        if not args:
            continue

        # Construct prospective event_id to avoid duplicate ingest
        prospective_id = (
            f"{args['event_type']}_{args['date'].isoformat()}_"
            f"{args['event_name'].lower().replace(' ', '_')}"
        )

        if any(ev.event_id == prospective_id for ev in research.events):
            # Already documented
            continue

        event = research.document_event(**args)
        created_ids.append(event.event_id)
        count += 1

    print(f"[USGS] Ingested {len(created_ids)} new earthquake events.")
    return created_ids


def main() -> None:
    """CLI entrypoint for live earthquake ingest."""
    print("=" * 80)
    print("LIVE EARTHQUAKE INGEST")
    print("USGS Real-Time Feed -> RealWorldDataResearch")
    print("=" * 80)
    print()

    research = RealWorldDataResearch()
    before_count = len(research.events)

    created = ingest_usgs_recent(research=research, max_events=50)

    after_count = len(research.events)
    print()
    print(f"Total events before ingest: {before_count}")
    print(f"Total events after ingest:  {after_count}")
    print(f"New events ingested:       {len(created)}")
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()

