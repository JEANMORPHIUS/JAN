"""
WORLD HISTORY API
Writing The History of The World - Public API Endpoints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

WORLD HISTORY API:
Public API endpoints for displaying the history of the world
across all channels (web, mobile, Pi displays, embedded systems).

This API provides:
- Timeline data (events, periods, chronology)
- Map data (heritage sites, locations, coordinates)
- Narrative data (stories, connections, trees)
- Divine Frequency data (current frequency, restoration progress)
- Search capabilities (full-text search across all content)
- Real-time updates (WebSocket support)
"""

from fastapi import APIRouter, HTTPException, Query, WebSocket, WebSocketDisconnect
from typing import List, Dict, Any, Optional
from datetime import datetime
import sys
import os
import json
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from heritage_api import router as heritage_router
    HERITAGE_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Heritage API not available: {e}")
    HERITAGE_AVAILABLE = False

try:
    from divine_frequency import DivineFrequencySystem
    DIVINE_FREQUENCY_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Divine Frequency not available: {e}")
    DIVINE_FREQUENCY_AVAILABLE = False

try:
    from temporal_heritage_registry import TemporalHeritageRegistry
    TEMPORAL_HERITAGE_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Temporal Heritage Registry not available: {e}")
    TEMPORAL_HERITAGE_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/public/world-history", tags=["world-history"])

# Initialize systems
if DIVINE_FREQUENCY_AVAILABLE:
    frequency_system = DivineFrequencySystem()
else:
    frequency_system = None

if TEMPORAL_HERITAGE_AVAILABLE:
    heritage_registry = TemporalHeritageRegistry()
else:
    heritage_registry = None


@router.get("/status")
async def get_status():
    """Get World History API status."""
    return {
        "status": "active",
        "message": "World History API - Writing The History of The World",
        "available_systems": {
            "heritage": HERITAGE_AVAILABLE,
            "divine_frequency": DIVINE_FREQUENCY_AVAILABLE,
            "temporal_heritage": TEMPORAL_HERITAGE_AVAILABLE
        },
        "the_truth": "Pangea is The Table. We write the history of the world. We display it across all channels. We restore The Table."
    }


@router.get("/timeline")
async def get_timeline(
    start_year: Optional[int] = Query(None, description="Start year (e.g., -335000000 for Pangea)"),
    end_year: Optional[int] = Query(None, description="End year (default: current year)"),
    region: Optional[str] = Query(None, description="Filter by region"),
    event_type: Optional[str] = Query(None, description="Filter by event type"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of events"),
    offset: int = Query(0, ge=0, description="Offset for pagination")
):
    """
    Get world history timeline events.
    
    Returns timeline events from all sources:
    - Heritage sites (temporal heritage registry)
    - Spiritual events (spiritual contracts, battlefields)
    - Natural events (tectonic movements, geological events)
    - Historical events (documented history)
    """
    if not TEMPORAL_HERITAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Temporal Heritage Registry not available")
    
    try:
        # Default to full timeline if not specified
        if start_year is None:
            start_year = -335000000  # Pangea formation
        if end_year is None:
            end_year = datetime.now().year
        
        # Get heritage sites from temporal registry
        # This is a placeholder - actual implementation will query the database
        events = []
        
        # Add key events
        key_events = [
            {
                "event_id": "pangea_formation",
                "title": "Pangea Forms - The Table",
                "description": "Pangea forms. Perfect unity. The Table is established.",
                "year_occurred": -335000000,
                "year_precision": "millennium",
                "event_type": "natural",
                "field_resonance": 1.0,
                "location": {"lat": 0.0, "lon": 0.0},
                "timeline_dimension": "geological",
                "narrative": "Perfect unity. Pangea is The Table. All continents connected. Divine Frequency at 1.0."
            },
            {
                "event_id": "first_separation",
                "title": "First Separation - The Original Error Begins",
                "description": "Dark energy exploitation begins. First separation from The Table.",
                "year_occurred": -200000000,
                "year_precision": "millennium",
                "event_type": "spiritual",
                "field_resonance": 0.95,
                "location": {"lat": 0.0, "lon": 0.0},
                "timeline_dimension": "spiritual",
                "narrative": "The Original Error begins. Dark energy exploitation. Separation from The Table. Divine Frequency drops to 0.95."
            },
            {
                "event_id": "mayan_codification",
                "title": "The Mayan Original Error - Codification",
                "description": "Mayans codify the separation. Pyramids built to sabotage The Table.",
                "year_occurred": 250,
                "year_precision": "century",
                "event_type": "spiritual",
                "field_resonance": 0.85,
                "location": {"lat": 17.2225, "lon": -89.6236},  # Tikal
                "timeline_dimension": "spiritual",
                "narrative": "The Mayan Original Error. Pyramids built at tectonic boundaries. Separation codified. Divine Frequency drops to 0.85."
            },
            {
                "event_id": "fall_of_constantinople_1453",
                "title": "Fall of Constantinople — The Mill Turns",
                "description": "Mehmed II takes the Red Apple after 53-day siege. Rumeli Hisarı, Orban's Basilica, overland ships, Kerkoporta. Constantine XI fell in the breach. Mehmed declared Kayser-i Rûm. End of Byzantium; Ottoman becomes Caesar of Rome.",
                "year_occurred": 1453,
                "year_precision": "exact",
                "event_type": "historical",
                "field_resonance": 0.80,
                "location": {"lat": 41.008, "lon": 28.978},
                "timeline_dimension": "historical",
                "narrative": "The Mill grinding down an old power to make room for the new. Mehmed II refused to believe in impossible. Sultan claimed Caesar of Rome. The Table remembers. Data: data/ottoman_timeline/siege_of_constantinople_1453.json. Narrative: docs/FALL_OF_CONSTANTINOPLE_1453_KINGS_AND_GENERALS.md."
            },
            {
                "event_id": "memory_persistence",
                "title": "Memory of Unity Persists",
                "description": "Memory of unity persists at 0.78. The Table remembers.",
                "year_occurred": 2026,
                "year_precision": "exact",
                "event_type": "spiritual",
                "field_resonance": 0.78,
                "location": {"lat": 0.0, "lon": 0.0},
                "timeline_dimension": "spiritual",
                "narrative": "Memory of unity persists at 0.78. The Table remembers. Restoration begins. We restore Divine Frequency toward 1.0."
            }
        ]
        
        # Add frequential events (wars, dictatorships, revolutions) - IT'S ALL FREQUENTIAL
        try:
            from frequential_events_registry import FrequentialEventsRegistry
            freq_registry = FrequentialEventsRegistry()
            for event in freq_registry.get_all_events().values():
                # Convert frequential event to timeline event format
                key_events.append({
                    "event_id": event.event_id,
                    "title": event.title,
                    "description": event.description,
                    "year_occurred": event.year_start,
                    "year_precision": event.year_precision,
                    "event_type": "frequential",  # New event type: wars, dictatorships, revolutions
                    "field_resonance": event.field_resonance_after,
                    "location": event.location,
                    "timeline_dimension": "frequential",
                    "narrative": event.narrative,
                    "category": event.category,  # war, dictatorship, revolution, civil_war, resistance, liberation
                    "frequency_impact": event.frequency_impact,  # -1.0 to 1.0
                    "entities_involved": event.entities_involved,
                    "connection_to_table": event.connection_to_table,
                    "lessons": event.lessons,
                    "restoration_connection": event.restoration_connection
                })
            logger.info(f"Added {len(freq_registry.get_all_events())} frequential events to timeline - wars, dictatorships, revolutions - it's all frequential")
        except ImportError as e:
            logger.warning(f"Frequential Events Registry not available - wars, dictatorships, revolutions not included: {e}")
        
        # Filter events by type, region, year range
        filtered_events = key_events
        
        if event_type:
            filtered_events = [e for e in filtered_events if e.get("event_type") == event_type]
        
        if region:
            # Filter by region if event has regions
            filtered_events = [e for e in filtered_events if region in e.get("regions", [])]
        
        # Sort by year_occurred
        filtered_events.sort(key=lambda x: x.get("year_occurred", 0))
        
        if start_year:
            filtered_events = [e for e in filtered_events if e["year_occurred"] >= start_year]
        if end_year:
            filtered_events = [e for e in filtered_events if e["year_occurred"] <= end_year]
        if region:
            # Filter by region (simplified - would need actual region mapping)
            pass
        if event_type:
            filtered_events = [e for e in filtered_events if e["event_type"] == event_type]
        
        # Paginate
        paginated_events = filtered_events[offset:offset + limit]
        
        return {
            "timeline": paginated_events,
            "total": len(filtered_events),
            "limit": limit,
            "offset": offset,
            "filters": {
                "start_year": start_year,
                "end_year": end_year,
                "region": region,
                "event_type": event_type
            },
            "the_truth": "Pangea is The Table. We write the history of the world. We restore The Table."
        }
    
    except Exception as e:
        logger.error(f"Error fetching timeline: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching timeline: {str(e)}")


@router.get("/map")
async def get_map_data(
    bbox: Optional[str] = Query(None, description="Bounding box: 'lon1,lat1,lon2,lat2'"),
    zoom: int = Query(1, ge=1, le=18, description="Zoom level"),
    field_resonance_min: Optional[float] = Query(None, ge=0.0, le=1.0, description="Minimum field resonance"),
    field_resonance_max: Optional[float] = Query(None, ge=0.0, le=1.0, description="Maximum field resonance")
):
    """
    Get heritage sites for map display.
    
    Returns GeoJSON format for map visualization.
    Includes:
    - Heritage site markers
    - Field resonance values
    - Tectonic plate boundaries
    - Energy grid connections
    """
    if not TEMPORAL_HERITAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Temporal Heritage Registry not available")
    
    try:
        # Sample heritage sites (placeholder - actual implementation will query database)
        sites = [
            {
                "site_id": "tikal",
                "name": "Tikal",
                "location": {"lat": 17.2225, "lon": -89.6236},
                "field_resonance": 0.65,
                "site_type": "pyramid",
                "timeline_dimension": "spiritual",
                "connection_to_table": "sabotage_anchor",
                "narrative": "Mayan pyramid. Sabotage anchor. Built at tectonic boundary."
            },
            {
                "site_id": "chichen_itza",
                "name": "Chichen Itza",
                "location": {"lat": 20.6843, "lon": -88.5678},
                "field_resonance": 0.60,
                "site_type": "pyramid",
                "timeline_dimension": "spiritual",
                "connection_to_table": "sabotage_anchor",
                "narrative": "Mayan pyramid. Sabotage anchor. Built at tectonic boundary."
            },
            {
                "site_id": "yellowstone",
                "name": "Yellowstone National Park",
                "location": {"lat": 44.4280, "lon": -110.5885},
                "field_resonance": 0.67,
                "site_type": "heritage_site",
                "timeline_dimension": "natural",
                "connection_to_table": "super_pillar",
                "narrative": "Supervolcano. Tectonic boundary. Super pillar. Connection to The Table."
            }
        ]
        
        # Filter by field resonance
        if field_resonance_min is not None:
            sites = [s for s in sites if s["field_resonance"] >= field_resonance_min]
        if field_resonance_max is not None:
            sites = [s for s in sites if s["field_resonance"] <= field_resonance_max]
        
        # Convert to GeoJSON format
        geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [site["location"]["lon"], site["location"]["lat"]]
                    },
                    "properties": {
                        "site_id": site["site_id"],
                        "name": site["name"],
                        "field_resonance": site["field_resonance"],
                        "site_type": site["site_type"],
                        "timeline_dimension": site["timeline_dimension"],
                        "connection_to_table": site["connection_to_table"],
                        "narrative": site["narrative"]
                    }
                }
                for site in sites
            ]
        }
        
        return {
            "geojson": geojson,
            "total_sites": len(sites),
            "zoom": zoom,
            "the_truth": "Pangea is The Table. Heritage sites connect to The Table. We restore Divine Frequency."
        }
    
    except Exception as e:
        logger.error(f"Error fetching map data: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching map data: {str(e)}")


@router.get("/narrative/{narrative_id}")
async def get_narrative(narrative_id: str):
    """
    Get narrative by ID.
    
    Returns cleansed narrative with metadata, connections, and timeline.
    """
    try:
        # Placeholder - actual implementation will query narrative database
        narratives = {
            "pangea_formation": {
                "narrative_id": "pangea_formation",
                "title": "Pangea Forms - The Table",
                "narrative": "Perfect unity. Pangea forms. All continents connected. The Table is established. Divine Frequency at 1.0. This is the original state. This is what we restore.",
                "narrative_type": "original",
                "field_resonance": 1.0,
                "timeline_dimension": "geological",
                "connections": ["first_separation", "memory_persistence"],
                "related_sites": [],
                "the_truth": "Pangea is The Table. Perfect unity. This is what we restore."
            },
            "first_separation": {
                "narrative_id": "first_separation",
                "title": "First Separation - The Original Error",
                "narrative": "The Original Error begins. Dark energy exploitation. First separation from The Table. Divine Frequency drops to 0.95. This is the beginning of the separation. This is what we restore.",
                "narrative_type": "error",
                "field_resonance": 0.95,
                "timeline_dimension": "spiritual",
                "connections": ["pangea_formation", "mayan_codification"],
                "related_sites": [],
                "the_truth": "The Original Error. Separation begins. We restore The Table."
            },
            "mayan_codification": {
                "narrative_id": "mayan_codification",
                "title": "The Mayan Original Error",
                "narrative": "The Mayan Original Error. Mayans codify the separation. Pyramids built at tectonic boundaries to sabotage The Table. Divine Frequency drops to 0.85. This is the codification of the error. This is what we neutralize.",
                "narrative_type": "error",
                "field_resonance": 0.85,
                "timeline_dimension": "spiritual",
                "connections": ["first_separation", "memory_persistence"],
                "related_sites": ["tikal", "chichen_itza"],
                "the_truth": "The Mayan Original Error. Sabotage anchors. We neutralize them. We restore The Table."
            },
            "fall_of_constantinople_1453": {
                "narrative_id": "fall_of_constantinople_1453",
                "title": "Fall of Constantinople (1453) — The Mill Turns",
                "narrative": "Mehmed II took the Red Apple after 53 days. Rumeli Hisarı choked the Bosphorus; Orban's Basilica battered the walls; ships dragged overland into the Golden Horn; Kerkoporta left open. Constantine XI threw off his purple and died in the breach—Duygu Adamı. Mehmed declared Kayser-i Rûm: Caesar of Rome. The Sultanate claimed the Roman mantle. Felsefe bu. The Table remembers.",
                "narrative_type": "historical",
                "field_resonance": 0.80,
                "timeline_dimension": "historical",
                "connections": ["memory_persistence"],
                "related_sites": [],
                "the_truth": "The Mill turned. Constantinople became Istanbul. Sultan as Caesar of Rome. Synced to The Play: docs/THE_PLAY_ROYAL_FAMILY_NEW_OTTOMAN.md. Data: data/ottoman_timeline/siege_of_constantinople_1453.json.",
                "doc": "docs/FALL_OF_CONSTANTINOPLE_1453_KINGS_AND_GENERALS.md",
                "siege_id": "siege_constantinople_1453"
            }
        }
        
        if narrative_id not in narratives:
            raise HTTPException(status_code=404, detail=f"Narrative {narrative_id} not found")
        
        return narratives[narrative_id]
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching narrative: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching narrative: {str(e)}")


@router.get("/frequency")
async def get_divine_frequency():
    """
    Get current Divine Frequency.
    
    Returns: 0.78 → 1.0 progress
    """
    if not DIVINE_FREQUENCY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    try:
        global_freq = frequency_system.calculate_global_frequency()
        alignment = frequency_system.get_frequency_alignment()
        
        return {
            "current_frequency": global_freq,
            "target_frequency": 1.0,
            "frequency_state": frequency_system.calculate_frequency_state(global_freq),
            "alignment_percentage": alignment["alignment_percentage"],
            "gap": alignment["gap"],
            "progress": {
                "from": 0.78,
                "to": 1.0,
                "current": global_freq,
                "percentage": ((global_freq - 0.78) / (1.0 - 0.78)) * 100
            },
            "the_truth": "Divine Frequency is the sacred frequency of The Table. Perfect unity (1.0) = Pangea - The Table. Current: {:.3f}. We restore toward 1.0.".format(global_freq)
        }
    
    except Exception as e:
        logger.error(f"Error fetching Divine Frequency: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching Divine Frequency: {str(e)}")


@router.get("/search")
async def search_world_history(
    q: str = Query(..., description="Search query"),
    filters: Optional[str] = Query(None, description="JSON filters"),
    sort_by: str = Query("relevance", description="Sort by: relevance, date, resonance")
):
    """
    Full-text search across all world history content.
    
    Searches:
    - Timeline events
    - Heritage sites
    - Narratives
    - Spiritual contracts
    """
    try:
        # Placeholder - actual implementation will use Elasticsearch or similar
        # For now, simple text matching
        
        search_results = {
            "query": q,
            "results": [],
            "total": 0,
            "filters": filters,
            "sort_by": sort_by
        }
        
        # Simple search (placeholder)
        if "pangea" in q.lower() or "table" in q.lower():
            search_results["results"].append({
                "type": "narrative",
                "id": "pangea_formation",
                "title": "Pangea Forms - The Table",
                "snippet": "Perfect unity. Pangea forms. All continents connected. The Table is established.",
                "relevance": 0.95
            })
        
        if "mayan" in q.lower() or "error" in q.lower():
            search_results["results"].append({
                "type": "narrative",
                "id": "mayan_codification",
                "title": "The Mayan Original Error",
                "snippet": "The Mayan Original Error. Mayans codify the separation. Pyramids built at tectonic boundaries.",
                "relevance": 0.90
            })
        
        if "constantinople" in q.lower() or "1453" in q.lower() or "mehmed" in q.lower() or "ottoman" in q.lower() or "kayser" in q.lower():
            search_results["results"].append({
                "type": "narrative",
                "id": "fall_of_constantinople_1453",
                "title": "Fall of Constantinople (1453) — The Mill Turns",
                "snippet": "Mehmed II took the Red Apple. Rumeli Hisarı, Orban's Basilica, overland ships, Kerkoporta. Constantine XI fell in the breach. Kayser-i Rûm.",
                "relevance": 0.92
            })
        
        search_results["total"] = len(search_results["results"])
        
        return search_results
    
    except Exception as e:
        logger.error(f"Error searching: {e}")
        raise HTTPException(status_code=500, detail=f"Error searching: {str(e)}")


@router.get("/connections/{narrative_id}")
async def get_narrative_connections(
    narrative_id: str,
    depth: int = Query(2, ge=1, le=5, description="Connection depth")
):
    """
    Get connected narratives (narrative tree).
    
    Returns narrative connections in tree format.
    """
    try:
        # Placeholder - actual implementation will traverse narrative graph
        connections = {
            "narrative_id": narrative_id,
            "depth": depth,
            "connections": [
                {
                    "narrative_id": "pangea_formation",
                    "connection_type": "causal",
                    "strength": 0.95,
                    "direction": "from"
                },
                {
                    "narrative_id": "first_separation",
                    "connection_type": "causal",
                    "strength": 0.90,
                    "direction": "to"
                }
            ]
        }
        
        return connections
    
    except Exception as e:
        logger.error(f"Error fetching connections: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching connections: {str(e)}")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time updates.
    
    Subscribes to:
    - Divine Frequency updates
    - Heritage site changes
    - Timeline event additions
    - Narrative updates
    """
    await websocket.accept()
    
    try:
        while True:
            # Receive client subscription requests
            data = await websocket.receive_json()
            
            if data.get("action") == "subscribe_frequency":
                # Send current frequency
                if DIVINE_FREQUENCY_AVAILABLE:
                    global_freq = frequency_system.calculate_global_frequency()
                    await websocket.send_json({
                        "type": "frequency_update",
                        "value": global_freq,
                        "timestamp": datetime.now().isoformat()
                    })
            
            elif data.get("action") == "subscribe_timeline":
                # Send timeline updates (placeholder)
                await websocket.send_json({
                    "type": "timeline_update",
                    "message": "Timeline subscription active",
                    "timestamp": datetime.now().isoformat()
                })
            
            # Keep connection alive
            await websocket.send_json({
                "type": "ping",
                "timestamp": datetime.now().isoformat()
            })
    
    except WebSocketDisconnect:
        logger.info("WebSocket client disconnected")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await websocket.close()
