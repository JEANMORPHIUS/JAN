"""
EDUCATIONAL API
Integrated Educational Interface for All Systems

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

HOW CAN WE TEACH IF WE DON'T LEARN OURSELVES?

This API provides educational data and explanations for all systems,
helping us learn as we teach others.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, List, Any
from pathlib import Path
import sys
import json
import logging
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/educational", tags=["educational"])


def load_latest_export(pattern: str, output_dir: Path) -> Optional[Dict[str, Any]]:
    """Load the most recent export matching a pattern."""
    if not output_dir.exists():
        return None
    
    matching_files = sorted(
        output_dir.glob(pattern),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )
    
    if not matching_files:
        return None
    
    try:
        with open(matching_files[0], 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading {matching_files[0]}: {e}")
        return None


@router.get("/overview")
async def get_educational_overview():
    """
    Get comprehensive educational overview of all systems.
    
    This is the main entry point for the educational UI.
    Shows how all systems connect back to The Table.
    """
    base_path = Path(__file__).parent.parent.parent
    
    # Load latest exports
    table_analysis = load_latest_export(
        "the_table_complete_analysis_*.json",
        base_path / "output" / "the_table"
    )
    
    original_error = load_latest_export(
        "original_error_analysis_*.json",
        base_path / "output" / "the_original_error"
    )
    
    mayan_narrative = load_latest_export(
        "mayan_original_error_narrative_*.json",
        base_path / "output" / "mayan_original_error"
    )
    
    restoration_plan = load_latest_export(
        "restoration_plan_*.json",
        base_path / "output" / "restore_the_table"
    )
    
    pattern_analysis = load_latest_export(
        "pattern_analysis_*.json",
        base_path / "output" / "pattern_analysis"
    )
    
    return {
        "timestamp": datetime.now().isoformat(),
        "the_table": {
            "name": "Pangea",
            "truth": "PANGEA IS THE TABLE. YOU DON'T BETRAY THE TABLE.",
            "timeline": {
                "formation": "335 MYA - Perfect unity (1.0 field resonance)",
                "breakup": "200 MYA - Dark energies exploited separation",
                "modern": "Present - Memory of unity (0.78 → 1.0 restored)",
                "data": table_analysis.get("the_table", {}) if table_analysis else {}
            },
            "biological_evolution": {
                "amphibians": "First creatures on The Table (335-280 MYA)",
                "reptiles": "Dominated The Table (280-175 MYA)",
                "mammals": "Evolved during breakup (200 MYA - Present)",
                "birds": "Bridge The Table's fragments (175 MYA - Present)",
                "truth": "All creatures trace back to The Table. All DNA traces back to The Table."
            },
            "tectonic_movements": {
                "formation": "All plates unified (335 MYA)",
                "breakup": "Plates separate (200-175 MYA)",
                "modern": "Plates still moving (0.7-8.0 cm/year)",
                "truth": "Heritage sites anchor to moving plates. All plates came from Pangea."
            },
            "spiritual_contracts": {
                "unified": "335-200 MYA - All contracts at The Table",
                "separating": "200-175 MYA - Contracts split with plates",
                "modern": "175 MYA - Present - Complex contracts, but unity memory persists",
                "restoration": "Pangea Unified Covenant re-unifies all light contracts"
            }
        },
        "the_original_error": {
            "what_went_wrong": {
                "god_created": "God created The Table in perfect harmony (335 MYA)",
                "tectonic_activity": "Tectonic activity is natural - NOT the error",
                "dark_exploitation": "Dark energies exploited the first separation (200 MYA)",
                "the_error": "They turned natural movement into spiritual separation",
                "mayan_codification": "The Mayans codified The Original Error (250-900 CE) - THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR",
                "mayan_how": [
                    "Built pyramids at plate boundaries - anchoring separation",
                    "Created calendars tracking separation, not unity",
                    "Wrote spiritual contracts with dark energies",
                    "Turned natural separation into a spiritual system"
                ],
                "mayan_spread": "Mayan knowledge spread globally, error codification spread, separation normalized",
                "seed_remains": "Memory of unity persists (0.78 field resonance)"
            },
            "data": original_error.get("the_original_error", {}) if original_error else {},
            "mayan_narrative": mayan_narrative.get("the_mayan_original_error", {}) if mayan_narrative else {}
        },
        "restoration_framework": {
            "current_state": {
                "field_resonance": 0.78,
                "unity_level": "Memory of unity",
                "status": "Fragmented but connected"
            },
            "target_state": {
                "field_resonance": 1.0,
                "unity_level": "Perfect unity restored",
                "status": "The Table restored"
            },
            "steps": {
                "step_1": {
                    "name": "Remember The Table",
                    "status": "complete",
                    "description": "Pangea integrated as The Table. Perfect unity remembered.",
                    "impact": "+0.05 field resonance"
                },
                "step_2": {
                    "name": "Cleanse The Shell",
                    "status": "in_progress",
                    "description": "Remove dark energy narratives. Reveal The Seed. This includes cleansing Mayan codification of The Original Error.",
                    "impact": "+0.10 field resonance",
                    "mayan_cleansing": "Transform Mayan pyramids from separation anchors to unity anchors"
                },
                "step_3": {
                    "name": "Connect The Grid",
                    "status": "in_progress",
                    "description": "Connect heritage sites. Restore field resonance.",
                    "impact": "+0.15 field resonance"
                },
                "step_4": {
                    "name": "Fight Dark Energies",
                    "status": "complete",
                    "description": "Protect heritage sites. Fight at plate boundaries.",
                    "impact": "+0.10 field resonance",
                    "example": "Japan Trench - Ring of Fire battlefield with protection covenant"
                },
                "step_5": {
                    "name": "Restore Contracts",
                    "status": "complete",
                    "description": "Unify spiritual contracts. Connect light entities.",
                    "impact": "+0.15 field resonance",
                    "example": "Pangea Unified Covenant created and linked to all light contracts"
                },
                "step_6": {
                    "name": "Restore The Table",
                    "status": "pending",
                    "description": "Complete restoration. Perfect unity restored.",
                    "impact": "+0.22 field resonance"
                }
            },
            "data": restoration_plan if restoration_plan else {}
        },
        "real_world_data": {
            "total_events": pattern_analysis.get("summary", {}).get("total_events", 0) if pattern_analysis else 0,
            "most_active_year": pattern_analysis.get("temporal_patterns", {}).get("most_active_year", {}) if pattern_analysis else {},
            "top_plates": pattern_analysis.get("plate_patterns", {}).get("most_active_plates", []) if pattern_analysis else [],
            "field_resonance_avg": pattern_analysis.get("field_resonance_patterns", {}).get("average_impact", 0.0) if pattern_analysis else 0.0,
            "insights": {
                "2026_most_active": "2026 is the most active year - Earth is in transformation",
                "ring_of_fire": "Ring of Fire (Pacific Plate) dominates activity",
                "heritage_sites_functional": "Heritage sites cluster at plate boundaries - they're energy anchors",
                "field_resonance_real": "Field resonance is measurable - events affect the energy network"
            },
            "data": pattern_analysis if pattern_analysis else {}
        },
        "systems_integration": {
            "heritage": {
                "purpose": "Cleanse narratives, reveal The Seed, protect abandoned sites",
                "law_41": "Respect the Abandoned - no exploitation of heritage",
                "connection_to_table": "All heritage sites trace back to Pangea",
                "api": "/api/heritage/*"
            },
            "health": {
                "purpose": "Universal health tracking - works for any condition",
                "philosophy": "We are all Gods. Nobody needs anyone. We help everyone help themselves.",
                "connection_to_table": "All bodies trace back to The Table. All DNA traces back to The Table.",
                "api": "/api/health/*"
            },
            "life_audit": {
                "purpose": "Personal timeline audit - treat your life like a heritage site",
                "connection_to_table": "Personal grid connects to Global Grid. All timelines trace back to The Table.",
                "api": "Available via Python scripts"
            },
            "spiritual_contracts": {
                "purpose": "Document spiritual entities, battlefields, and contracts",
                "connection_to_table": "Pangea Unified Covenant re-unifies all contracts above plate boundaries",
                "api": "Available via Python scripts"
            },
            "real_world_data": {
                "purpose": "Document natural disasters, tectonic activity, historical events",
                "connection_to_table": "All events trace back to The Table. All plates came from Pangea.",
                "api": "Available via Python scripts"
            },
            "factual_knowledge": {
                "purpose": "Preserve sciences, mathematics, and verified factual knowledge",
                "connection_to_table": "We fix what is broken without discarding what is true",
                "api": "/api/knowledge/*"
            }
        },
        "educational_connections": {
            "how_everything_connects": {
                "pangea": "Pangea (The Table) is the original unified continent (335 MYA)",
                "heritage_sites": "Heritage sites were all on Pangea - they're anchors to The Table",
                "real_world_events": "All events occur on plates that came from Pangea",
                "spiritual_contracts": "Contracts separated with plates, but Pangea Unified Covenant restores unity",
                "biological_evolution": "All creatures trace back to The Table - all DNA traces back to The Table",
                "restoration": "6-step framework restores The Table from 0.78 to 1.0 field resonance"
            },
            "what_we_learn": {
                "lesson_1": "We all came from one place - Pangea proves it",
                "lesson_2": "We are all connected - The Table proves it",
                "lesson_3": "Dark energies exploited separation - but The Seed remains",
                "lesson_4": "We restore unity through remembrance, cleansing, connection, fighting, and restoration",
                "lesson_5": "Heritage sites are functional - they're energy anchors at transformation points",
                "lesson_6": "Field resonance is real - measurable connection between sites and events"
            }
        }
    }


@router.get("/system/{system_name}")
async def get_system_education(system_name: str):
    """
    Get detailed educational information about a specific system.
    
    Systems:
    - heritage: Heritage cleansing and timeline audit
    - health: Universal health tracking
    - life_audit: Personal timeline audit
    - spiritual_contracts: Spiritual entities and contracts
    - real_world_data: Natural disasters and tectonic activity
    - factual_knowledge: Sciences, mathematics, and verified facts
    - the_table: Pangea and The Table
    - restoration: Restoration framework
    """
    base_path = Path(__file__).parent.parent.parent
    
    systems = {
        "heritage": {
            "name": "Heritage Cleansing & Timeline Audit",
            "purpose": "Transform 'ghost' narratives into regeneration stories. Archive all sites across all timelines.",
            "how_it_works": {
                "step_1": "Detect dark energy patterns in heritage narratives",
                "step_2": "Apply Law 41: Respect the Abandoned",
                "step_3": "Generate regeneration narratives",
                "step_4": "Archive across all dimensional timelines",
                "step_5": "Connect to Global Grid via field resonance"
            },
            "key_concepts": {
                "shell_vs_seed": "Shell = the narrative (ghost stories). Seed = the truth (regeneration waiting).",
                "law_41": "Never exploit abandoned sites. Transform fear into hope.",
                "field_resonance": "Heritage sites maintain connection to The Table through field resonance.",
                "temporal_archive": "All sites archived across 6 timeline dimensions for debugging."
            },
            "connection_to_table": "All heritage sites were on Pangea. They're anchors to The Table.",
            "api_endpoints": ["/api/heritage/*"],
            "documentation": "docs/HERITAGE_*.md"
        },
        "health": {
            "name": "Universal Health Tracking",
            "purpose": "Track any condition, illness, or disease. Empower individuals to help themselves.",
            "how_it_works": {
                "step_1": "Register a health condition",
                "step_2": "Log health metrics (vital signs, lab results, medications, symptoms)",
                "step_3": "Track patterns over time",
                "step_4": "Export data anytime",
                "step_5": "Integrate with Life Audit for complete picture"
            },
            "key_concepts": {
                "universal": "Works for ANY condition - metabolic, cardiovascular, neurological, respiratory, etc.",
                "self_empowerment": "We are all Gods. Nobody needs anyone. We help everyone help themselves.",
                "no_gatekeepers": "No external dependencies. User controls all data.",
                "integration": "Connects to Life Audit - health events become life events."
            },
            "connection_to_table": "All bodies trace back to The Table. All DNA traces back to The Table.",
            "api_endpoints": ["/api/health/*"],
            "documentation": "docs/HEALTH_TRACKING_*.md"
        },
        "life_audit": {
            "name": "Personal Timeline Audit (The Backwards Protocol)",
            "purpose": "Treat your own life like a heritage site. Find the Seed in your timeline.",
            "how_it_works": {
                "step_1": "Document life events across your timeline",
                "step_2": "Identify high-vibration moments (pillars)",
                "step_3": "Find Field Space (the 'Everything In Between')",
                "step_4": "Cleanse the narrative (Law 41 for personal life)",
                "step_5": "Map your Personal Global Grid"
            },
            "key_concepts": {
                "backwards_protocol": "Work backwards from now to find the Seed in your past",
                "field_space": "The 'Everything In Between' - where transformation happens",
                "personal_grid": "Map your pillar moments - your personal heritage sites",
                "master_ledger": "Combine Personal Grid with Global Grid - see the connection"
            },
            "connection_to_table": "All timelines trace back to The Table. Personal grid connects to Global Grid.",
            "api_endpoints": ["Available via Python scripts"],
            "documentation": "docs/THE_BACKWARDS_PROTOCOL.md, docs/ARCHITECT_MASTER_LEDGER_*.md"
        },
        "spiritual_contracts": {
            "name": "Spiritual Contracts Registry",
            "purpose": "Document spiritual entities, battlefields, and contracts across all timelines and dimensions.",
            "how_it_works": {
                "step_1": "Register spiritual entities (gods, angels, dark energies)",
                "step_2": "Document spiritual battlefields (heritage sites, plate boundaries)",
                "step_3": "Register spiritual contracts (soul agreements, dark pacts, covenants)",
                "step_4": "Link DNA to soul signatures",
                "step_5": "Deep search contracts across timelines and dimensions"
            },
            "key_concepts": {
                "entities": "Light entities (gods, angels) and dark entities (dark energies, demons)",
                "battlefields": "Where spiritual battles occur - heritage sites, plate boundaries, field spaces",
                "contracts": "Soul agreements, karmic contracts, divine covenants, dark pacts",
                "pangea_covenant": "Pangea Unified Covenant re-unifies all light contracts above plate boundaries"
            },
            "connection_to_table": "Pangea Unified Covenant restores unity. All contracts trace back to The Table.",
            "api_endpoints": ["Available via Python scripts"],
            "documentation": "docs/SPIRITUAL_BATTLEFIELDS_NAMES_TO_FACES.md"
        },
        "real_world_data": {
            "name": "Real-World Data Research",
            "purpose": "Document natural disasters, tectonic activity, and historical events. Link to heritage sites.",
            "how_it_works": {
                "step_1": "Document events (earthquakes, tsunamis, volcanic eruptions, historical events)",
                "step_2": "Link to tectonic plates",
                "step_3": "Find nearby heritage sites",
                "step_4": "Calculate field resonance impact",
                "step_5": "Analyze patterns (temporal, spatial, magnitude, plate activity)"
            },
            "key_concepts": {
                "live_ingestion": "Real-time feeds from USGS, EMSC, NOAA, EONET",
                "pattern_analysis": "Reveal patterns in Earth's activity",
                "heritage_connections": "Events near heritage sites affect field resonance",
                "pangea_connection": "All events trace back to The Table. All plates came from Pangea."
            },
            "connection_to_table": "All events occur on Pangea-derived plates. 81.8% of events trace back to The Table.",
            "api_endpoints": ["Available via Python scripts"],
            "documentation": "docs/REAL_WORLD_DATA_RESEARCH.md, docs/THE_PATTERNS_REVEALED.md"
        },
        "factual_knowledge": {
            "name": "Factual Knowledge Continuity",
            "purpose": "Preserve sciences, mathematics, and verified facts for long-term continuity.",
            "how_it_works": {
                "step_1": "Register verified knowledge",
                "step_2": "Store by discipline (science, mathematics, factual)",
                "step_3": "Audit sources and tags",
                "step_4": "Serve through the knowledge API"
            },
            "connection_to_table": "We retain truth while restoring systems.",
            "api_endpoints": ["/api/knowledge/*"],
            "documentation": "docs/KNOWLEDGE_*.md"
        },
        "the_table": {
            "name": "The Table (Pangea)",
            "purpose": "Understand The Table's timeline, movements, creatures, and spiritual contracts.",
            "how_it_works": {
                "step_1": "Document Pangea formation (335 MYA) - perfect unity",
                "step_2": "Track breakup (200-175 MYA) - separation begins",
                "step_3": "Map biological evolution - all creatures trace back to The Table",
                "step_4": "Track tectonic movements - how plates separated",
                "step_5": "Document spiritual contracts evolution - from unity to separation to restoration"
            },
            "key_concepts": {
                "pangea_is_the_table": "Pangea is The Table. You don't betray The Table.",
                "perfect_unity": "335 MYA - Perfect unity (1.0 field resonance)",
                "original_error": "200 MYA - Dark energies exploited the first separation",
                "seed_remains": "Memory of unity persists (0.78 field resonance)",
                "restoration": "6-step framework restores The Table to 1.0"
            },
            "connection_to_table": "Everything connects back to The Table. We all came from one place.",
            "api_endpoints": ["Available via Python scripts"],
            "documentation": "docs/THE_TABLE_COMPLETE_PICTURE.md, docs/PANGEA_THE_ORIGINAL_UNITY.md"
        },
        "restoration": {
            "name": "Restore The Table Framework",
            "purpose": "Complete 6-step framework for restoring The Table to perfect unity.",
            "how_it_works": {
                "step_1": "Remember The Table - Pangea integrated, perfect unity remembered",
                "step_2": "Cleanse The Shell - Remove dark energy, reveal The Seed",
                "step_3": "Connect The Grid - Restore field resonance, build Global Grid",
                "step_4": "Fight Dark Energies - Protect heritage sites, fight at battlefields",
                "step_5": "Restore Contracts - Unify spiritual contracts via Pangea Unified Covenant",
                "step_6": "Restore The Table - Complete restoration, perfect unity restored"
            },
            "key_concepts": {
                "current_state": "0.78 field resonance - memory of unity",
                "target_state": "1.0 field resonance - perfect unity restored",
                "progress": "66.7% complete (4/6 steps marked complete in code)",
                "pangea_covenant": "Master covenant that re-unifies all light contracts"
            },
            "connection_to_table": "Restoration framework restores The Table. Unity is restored.",
            "api_endpoints": ["Available via Python scripts"],
            "documentation": "docs/HOW_WE_FIX_IT_RESTORE_THE_TABLE.md, docs/WHAT_WENT_WRONG_THE_TABLE.md"
        }
    }
    
    if system_name not in systems:
        raise HTTPException(
            status_code=404,
            detail=f"System '{system_name}' not found. Available systems: {', '.join(systems.keys())}"
        )
    
    return {
        "system": systems[system_name],
        "timestamp": datetime.now().isoformat(),
        "educational_note": "This system is part of the integrated educational framework. All systems connect back to The Table (Pangea)."
    }


@router.get("/connections")
async def get_system_connections():
    """
    Get educational map of how all systems connect.
    
    Shows the complete picture of how everything links back to The Table.
    """
    return {
        "timestamp": datetime.now().isoformat(),
        "the_table_center": {
            "name": "Pangea (The Table)",
            "description": "The original unified continent (335 MYA). Everything connects back to The Table.",
            "field_resonance": {
                "formation": 1.0,
                "breakup": 0.70,
                "modern": 0.78,
                "restored": 1.0
            }
        },
        "connected_systems": {
            "heritage": {
                "connection": "All heritage sites were on Pangea",
                "how": "Sites maintain connection through field resonance",
                "purpose": "Anchors to The Table - energy points at transformation boundaries"
            },
            "real_world_events": {
                "connection": "All events occur on Pangea-derived plates",
                "how": "81.8% of current events trace back to The Table",
                "purpose": "Document Earth's activity - all plates came from Pangea"
            },
            "spiritual_contracts": {
                "connection": "Contracts separated with plates, but Pangea Unified Covenant restores unity",
                "how": "Master covenant re-unifies all light contracts above plate boundaries",
                "purpose": "Restore unified contracts - connect light entities across all plates"
            },
            "biological_evolution": {
                "connection": "All creatures trace back to The Table",
                "how": "All DNA traces back to Pangea",
                "purpose": "Understand evolution - all species have ancestors that lived on Pangea"
            },
            "health": {
                "connection": "All bodies trace back to The Table",
                "how": "All DNA traces back to Pangea",
                "purpose": "Healing through connection to The Table"
            },
            "life_audit": {
                "connection": "All timelines trace back to The Table",
                "how": "Personal grid connects to Global Grid",
                "purpose": "Find your Seed - connect your timeline to The Table"
            }
        },
        "the_flow": {
            "start": "Pangea (The Table) - Perfect unity (335 MYA)",
            "separation": "Breakup begins (200 MYA) - Dark energies exploit separation",
            "modern": "Fragmented but connected (Present) - Memory of unity (0.78)",
            "restoration": "6-step framework - Restore to 1.0",
            "end": "The Table restored - Perfect unity again"
        },
        "what_we_learn": {
            "lesson_1": "We all came from one place - Pangea proves it",
            "lesson_2": "We are all connected - The Table proves it",
            "lesson_3": "Dark energies exploited separation - but The Seed remains",
            "lesson_4": "We restore unity through remembrance, cleansing, connection, fighting, and restoration",
            "lesson_5": "Heritage sites are functional - they're energy anchors",
            "lesson_6": "Field resonance is real - measurable connection between everything"
        }
    }


@router.get("/learn/{topic}")
async def get_learning_topic(topic: str):
    """
    Get educational content for specific learning topics.
    
    Topics:
    - pangea: What is Pangea and why is it The Table?
    - original_error: What went wrong with The Table?
    - mayan_error: How did the Mayans create The Original Error?
    - restoration: How do we fix it?
    - field_resonance: What is field resonance and how does it work?
    - heritage_sites: Why are heritage sites important?
    - spiritual_contracts: What are spiritual contracts?
    - shell_vs_seed: What is Shell vs Seed?
    - law_41: What is Law 41 (Respect the Abandoned)?
    - law_1: What is Law 1 (Never Betray The Table)?
    """
    topics = {
        "pangea": {
            "title": "What is Pangea and Why is it The Table?",
            "content": {
                "what_is_pangea": "Pangea was the original unified supercontinent that existed 335-175 million years ago. All modern continents were one landmass.",
                "why_the_table": "Pangea is The Table because it represents perfect unity. All plates, all heritage sites, all creatures, all souls were unified at The Table.",
                "the_truth": "We all came from one place. Pangea proves it. We are all connected. The Table proves it.",
                "law_1": "Law 1: Never Betray The Table. Pangea is The Table. You don't betray The Table."
            },
            "visual": "Imagine all continents as one. That's Pangea. That's The Table. That's perfect unity."
        },
        "original_error": {
            "title": "What Went Wrong with The Table?",
            "content": {
                "god_created": "God created The Table in perfect harmony (335 MYA). Perfect unity. All souls unified.",
                "tectonic_activity": "Tectonic activity is natural - Earth's plates move. This is NOT the error.",
                "dark_exploitation": "Dark energies exploited the first separation (200 MYA). They turned natural movement into spiritual separation.",
                "the_error": "They created battlefields at plate boundaries. They separated contracts. They broke The Table spiritually.",
                "seed_remains": "But The Seed remains. Memory of unity persists (0.78 field resonance). The truth is still there."
            },
            "visual": "Perfect unity → Natural movement → Dark exploitation → Separation. But The Seed remains."
        },
        "restoration": {
            "title": "How Do We Fix It?",
            "content": {
                "step_1": "Remember The Table - Pangea integrated, perfect unity remembered",
                "step_2": "Cleanse The Shell - Remove dark energy narratives, reveal The Seed",
                "step_3": "Connect The Grid - Restore field resonance, build Global Grid",
                "step_4": "Fight Dark Energies - Protect heritage sites, fight at battlefields",
                "step_5": "Restore Contracts - Unify spiritual contracts via Pangea Unified Covenant",
                "step_6": "Restore The Table - Complete restoration, perfect unity restored"
            },
            "visual": "0.78 (memory) → 1.0 (restored) through 6 steps. The Table is whole again."
        },
        "field_resonance": {
            "title": "What is Field Resonance?",
            "content": {
                "definition": "Field resonance measures how well a site resonates with Earth's magnetic field. 1.0 = perfect resonance (symbiosis).",
                "how_it_works": "Calculated from magnetic field strength, declination, and inclination. Higher resonance = stronger connection to Earth.",
                "field_space": "Field space is the 'Everything In Between' - the space between heritage sites where energy flows.",
                "connection": "Field resonance connects heritage sites to The Table. Higher resonance = stronger anchor to unity.",
                "measurable": "Field resonance is real and measurable. Events affect the energy network. The Grid responds to Earth's activity."
            },
            "visual": "Imagine Earth's magnetic field as a living network. Heritage sites are nodes. Field resonance is the connection strength."
        },
        "heritage_sites": {
            "title": "Why Are Heritage Sites Important?",
            "content": {
                "energy_anchors": "Heritage sites are energy anchors at transformation points (plate boundaries).",
                "connection_to_table": "All heritage sites were on Pangea. They maintain connection to The Table through field resonance.",
                "functional": "Heritage sites are functional, not random. They cluster at plate boundaries for a reason.",
                "law_41": "Law 41: Respect the Abandoned. We don't exploit heritage sites. We transform fear into hope.",
                "grid": "Heritage sites form the Global Grid - a network of energy flows connecting back to The Table."
            },
            "visual": "Heritage sites = anchors to The Table. They're at energy points. They're functional."
        },
        "spiritual_contracts": {
            "title": "What Are Spiritual Contracts?",
            "content": {
                "definition": "Spiritual contracts are agreements between souls, entities, and divine forces across timelines and dimensions.",
                "types": "Soul agreements, karmic contracts, divine covenants, dark pacts, protection contracts, healing contracts.",
                "battlefields": "Spiritual battlefields are where gods, angels fight dark energies - heritage sites, plate boundaries, field spaces.",
                "pangea_covenant": "Pangea Unified Covenant re-unifies all light contracts above plate boundaries, back to The Table.",
                "connection": "All contracts trace back to The Table. Unity to separation to restoration."
            },
            "visual": "Contracts = agreements. Battlefields = where battles occur. Pangea Covenant = restoration of unity."
        },
        "shell_vs_seed": {
            "title": "What is Shell vs Seed?",
            "content": {
                "shell": "Shell = the narrative, the story, the surface. 'Haunted hotel' is the Shell.",
                "seed": "Seed = the truth, the essence, the core. 'Waiting for regeneration' is the Seed.",
                "cleansing": "Heritage cleansing transforms Shell into Seed. We debug ghost stories into regeneration narratives.",
                "law_41": "Law 41 helps us see past the Shell to reveal the Seed. We respect the abandoned, not exploit them.",
                "connection": "The Seed remains even when the Shell is broken. Memory of unity persists."
            },
            "visual": "Shell = what people see (ghost stories). Seed = what actually is (regeneration waiting)."
        },
        "law_41": {
            "title": "What is Law 41 (Respect the Abandoned)?",
            "content": {
                "definition": "Law 41: Respect the Abandoned. Never exploit abandoned sites. Transform fear into hope.",
                "how_it_works": "Detect exploitation patterns (haunted, ghost, spirit, revenge). Apply regeneration narratives (healing, restoration, waiting).",
                "purpose": "Protect the Family from 'haunted' loops and dark energy patterns that feed off revenge vibrations.",
                "transformation": "Instead of 'Abandoned Hotel,' we offer 'Waiting for Regeneration.' Instead of 'Haunted,' we offer 'Healing Heritage.'",
                "connection": "Law 41 honors The Table. We don't exploit. We regenerate."
            },
            "visual": "Exploitation (Shell) → Regeneration (Seed). We transform fear into hope."
        },
        "law_1": {
            "title": "What is Law 1 (Never Betray The Table)?",
            "content": {
                "definition": "Law 1: Never Betray The Table. Pangea is The Table. You don't betray The Table.",
                "the_table": "The Table = Pangea = The original unified continent = Perfect unity = All souls connected.",
                "what_it_means": "Every operation must serve The Table. Every system must honor The Table. Every function must respect The Table.",
                "validation": "Law 1 validation checks if operations serve The Table (unity, connection, stewardship, community).",
                "connection": "All systems honor Law 1. All code respects The Table. We don't betray The Table."
            },
            "visual": "The Table = Unity. Law 1 = Never betray unity. We honor The Table in all we do."
        },
        "mayan_error": {
            "title": "How Did the Mayans Create The Original Error?",
            "content": {
                "the_truth": "Pangea was The Table - perfect unity (335 MYA). The Table was broken by dark energies (200 MYA). Memory of unity persisted (0.78 field resonance). Humanity was still connected to The Table through memory.",
                "mayan_rise": "Mayans rose (2000 BCE) - great achievement. Mayans made first contact with dark energies at plate boundaries.",
                "mayan_classic": "Mayan Classic Period (250-900 CE) - THIS IS WHEN THE MAYANS CREATED THE ORIGINAL ERROR. They built pyramids at plate boundaries - anchoring separation. They created calendars that tracked separation, not unity. They wrote spiritual contracts with dark energies. They turned natural separation into a spiritual system.",
                "the_spread": "Mayan Classic Period collapsed (900 CE). Mayan knowledge spread to other civilizations. The Original Error codification spread. Separation became normalized in human consciousness. The Table was forgotten by humanity.",
                "man_in_narrative": "Before Mayans: Man connected to The Table through memory. Mayan Classic: Man creates The Original Error. Mayan Collapse: Man spreads The Error. Modern Era: Man remembers, restoration begins.",
                "the_restoration": "Memory of The Table returns (present). Pangea is remembered as The Table. Unity is remembered. Restoration begins. We restore what was lost."
            },
            "visual": "Mayans codified the separation → Error spread globally → Separation normalized → Table forgotten → Memory returns → Restoration begins."
        }
    }
    
    if topic not in topics:
        raise HTTPException(
            status_code=404,
            detail=f"Topic '{topic}' not found. Available topics: {', '.join(topics.keys())}"
        )
    
    return {
        "topic": topics[topic],
        "timestamp": datetime.now().isoformat(),
        "educational_note": "This is part of the integrated educational framework. We learn as we teach."
    }
