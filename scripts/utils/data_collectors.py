"""DATA COLLECTOR HELPERS
Shared functions for data collection scripts

Extracts common patterns from scripts like deep_research_collector.py

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

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

from .paths import get_data_path, get_output_path
from .helpers import save_json, load_json, setup_logging

logger = setup_logging(__name__)

def save_event_data(events: List[Dict[str, Any]], filename: str, subdirectory: Optional[str] = None) -> Path:
    """
    Save event data to JSON file
    
    Args:
        events: List of event dictionaries
        filename: Output filename
        subdirectory: Optional subdirectory in data folder
    
    Returns:
        Path to saved file
    """
    output_dir = get_data_path(subdirectory) if subdirectory else get_data_path()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / filename
    
    data = {
        'timestamp': datetime.now().isoformat(),
        'event_count': len(events),
        'events': events
    }
    
    save_json(data, output_file)
    logger.info(f"Saved {len(events)} events to {output_file}")
    
    return output_file

def load_event_data(filepath: Path) -> List[Dict[str, Any]]:
    """
    Load event data from JSON file
    
    Args:
        filepath: Path to event data file
    
    Returns:
        List of event dictionaries
    """
    data = load_json(filepath, default={'events': []})
    return data.get('events', [])

def format_event_summary(events: List[Dict[str, Any]]) -> str:
    """
    Format a summary of events for display
    
    Args:
        events: List of event dictionaries
    
    Returns:
        Formatted summary string
    """
    if not events:
        return "No events found."
    
    summary_lines = [
        f"Total Events: {len(events)}",
        ""
    ]
    
    # Group by date
    by_date = {}
    for event in events:
        date_str = event.get('date', 'Unknown')
        if date_str not in by_date:
            by_date[date_str] = []
        by_date[date_str].append(event)
    
    for date_str in sorted(by_date.keys()):
        events_on_date = by_date[date_str]
        summary_lines.append(f"{date_str}: {len(events_on_date)} events")
        for event in events_on_date[:3]:  # Show first 3
            name = event.get('event_name', 'Unknown')
            summary_lines.append(f"  - {name}")
        if len(events_on_date) > 3:
            summary_lines.append(f"  ... and {len(events_on_date) - 3} more")
    
    return "\n".join(summary_lines)

__all__ = [
    'save_event_data', 'load_event_data', 'format_event_summary'
]
