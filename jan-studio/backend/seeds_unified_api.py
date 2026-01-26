"""UNIFIED SEEDS API
All seed sources from first, now, and beyond.

This aggregates seeds from protocols, searches, alerts, and future entries
into a single access layer.

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

from fastapi import APIRouter, HTTPException, Query, Body
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
from datetime import datetime
from pathlib import Path
import json
import uuid

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


router = APIRouter(prefix="/api/seeds", tags=["Seeds"])

BASE_OUTPUT_DIR = Path(__file__).parent.parent.parent / "SIYEM" / "output"
SEED_EXTRACTIONS_DIR = BASE_OUTPUT_DIR / "seed_extractions"
NASA_SEED_SEARCH_DIR = BASE_OUTPUT_DIR / "nasa_seed_search"
ENERGY_ALERTS_DIR = BASE_OUTPUT_DIR / "energy_alerts"
SEEDS_UNIFIED_DIR = BASE_OUTPUT_DIR / "seeds_unified"
SEED_TO_MOVEMENT_FILE = BASE_OUTPUT_DIR / "seed_to_movement_phases.json"

SEEDS_UNIFIED_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# MODELS
# ============================================================================

class SeedRecord(BaseModel):
    seed_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    seed_type: str
    origin: str
    description: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# HELPERS
# ============================================================================

def _safe_read_json(path: Path) -> Optional[Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

def _load_json_dir(dir_path: Path, filename_contains: Optional[str] = None) -> List[Dict[str, Any]]:
    if not dir_path.exists():
        return []
    entries: List[Dict[str, Any]] = []
    for file_path in dir_path.iterdir():
        if not file_path.is_file() or file_path.suffix.lower() != ".json":
            continue
        if filename_contains and filename_contains not in file_path.name:
            continue
        data = _safe_read_json(file_path)
        if data is None:
            continue
        entries.append({
            "source_path": str(file_path),
            "file_name": file_path.name,
            "file_modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
            "data": data
        })
    return entries

def _seed_record(
    seed_id: str,
    source: str,
    seed_type: str,
    origin: str,
    timestamp: Optional[str],
    data: Any,
    source_path: Optional[str] = None
) -> Dict[str, Any]:
    return {
        "seed_id": seed_id,
        "source": source,
        "seed_type": seed_type,
        "origin": origin,
        "timestamp": timestamp,
        "source_path": source_path,
        "data": data
    }

def _collect_protocol_seeds() -> List[Dict[str, Any]]:
    try:
        from seed_extraction_protocol import get_seed_extraction_protocol
        protocol = get_seed_extraction_protocol()
        seeds = protocol.get_seeds()
        records = []
        for seed in seeds:
            records.append(_seed_record(
                seed_id=seed.seed_id,
                source="seed_extraction_protocol",
                seed_type="identified_seed",
                origin=seed.org_id,
                timestamp=seed.identified_date.isoformat() if hasattr(seed, "identified_date") else None,
                data={
                    "org_id": seed.org_id,
                    "location": seed.location,
                    "coordinates": seed.coordinates,
                    "resonance_score": seed.resonance_score,
                    "shell_resonance": seed.shell_resonance,
                    "family_frequency_match": seed.family_frequency_match,
                    "extraction_status": seed.extraction_status.value,
                    "safe_passage_status": seed.safe_passage_status
                }
            ))
        return records
    except Exception:
        return []

def _collect_nasa_seed_search() -> List[Dict[str, Any]]:
    try:
        from nasa_seed_search import get_nasa_seed_search
        seed_search = get_nasa_seed_search()
        records: List[Dict[str, Any]] = []
        for scan in seed_search.scan_results.values():
            for potential in scan.potential_seeds:
                seed_id = potential.get("seed_id") or potential.get("id") or f"NASA_POTENTIAL_{scan.scan_id}"
                records.append(_seed_record(
                    seed_id=seed_id,
                    source="nasa_seed_search_memory",
                    seed_type="potential_seed",
                    origin=scan.operation_id if hasattr(scan, "operation_id") else scan.scan_id,
                    timestamp=scan.timestamp.isoformat(),
                    data={
                        "scan_id": scan.scan_id,
                        "bridge_alignment": scan.bridge_alignment.value,
                        "target_coordinate": scan.target_coordinate,
                        "potential_seed": potential
                    }
                ))
        return records
    except Exception:
        return []

def _collect_seed_files() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for entry in _load_json_dir(SEED_EXTRACTIONS_DIR):
        data = entry["data"]
        seed_id = data.get("seed_id") if isinstance(data, dict) else entry["file_name"]
        origin = data.get("org_id") if isinstance(data, dict) else "seed_extractions_file"
        records.append(_seed_record(
            seed_id=seed_id,
            source="seed_extractions_file",
            seed_type="extraction_record",
            origin=origin,
            timestamp=entry["file_modified"],
            data=data,
            source_path=entry["source_path"]
        ))
    return records

def _collect_nasa_search_files() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for entry in _load_json_dir(NASA_SEED_SEARCH_DIR):
        data = entry["data"]
        seed_id = data.get("operation_id") if isinstance(data, dict) else entry["file_name"]
        records.append(_seed_record(
            seed_id=seed_id,
            source="nasa_seed_search_file",
            seed_type="nasa_search_record",
            origin="nasa_seed_search",
            timestamp=entry["file_modified"],
            data=data,
            source_path=entry["source_path"]
        ))
    return records

def _collect_energy_alert_seeds() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for entry in _load_json_dir(ENERGY_ALERTS_DIR, filename_contains="SEED"):
        data = entry["data"]
        seed_id = data.get("user_id") if isinstance(data, dict) else entry["file_name"]
        origin = data.get("user_id") if isinstance(data, dict) else "energy_alert"
        timestamp = data.get("timestamp") if isinstance(data, dict) else entry["file_modified"]
        records.append(_seed_record(
            seed_id=seed_id,
            source="energy_alerts",
            seed_type="energy_alert_seed",
            origin=origin,
            timestamp=timestamp,
            data=data,
            source_path=entry["source_path"]
        ))
    return records

def _collect_unified_seed_files() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for entry in _load_json_dir(SEEDS_UNIFIED_DIR):
        data = entry["data"]
        seed_id = data.get("seed_id") if isinstance(data, dict) else entry["file_name"]
        origin = data.get("origin") if isinstance(data, dict) else "unified_seed"
        timestamp = data.get("created_date") if isinstance(data, dict) else entry["file_modified"]
        records.append(_seed_record(
            seed_id=seed_id,
            source="seeds_unified",
            seed_type=data.get("seed_type") if isinstance(data, dict) else "unified_seed",
            origin=origin,
            timestamp=timestamp,
            data=data,
            source_path=entry["source_path"]
        ))
    return records

def _load_seed_to_movement() -> Optional[Any]:
    if not SEED_TO_MOVEMENT_FILE.exists():
        return None
    return _safe_read_json(SEED_TO_MOVEMENT_FILE)

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.get("/sources")
async def get_seed_sources():
    """
    List seed sources and filesystem availability.
    """
    return {
        "status": "success",
        "sources": {
            "seed_extractions_dir": str(SEED_EXTRACTIONS_DIR),
            "nasa_seed_search_dir": str(NASA_SEED_SEARCH_DIR),
            "energy_alerts_dir": str(ENERGY_ALERTS_DIR),
            "seeds_unified_dir": str(SEEDS_UNIFIED_DIR),
            "seed_to_movement_file": str(SEED_TO_MOVEMENT_FILE)
        },
        "exists": {
            "seed_extractions_dir": SEED_EXTRACTIONS_DIR.exists(),
            "nasa_seed_search_dir": NASA_SEED_SEARCH_DIR.exists(),
            "energy_alerts_dir": ENERGY_ALERTS_DIR.exists(),
            "seeds_unified_dir": SEEDS_UNIFIED_DIR.exists(),
            "seed_to_movement_file": SEED_TO_MOVEMENT_FILE.exists()
        },
        "message": "All seed sources are mapped. First, now, and beyond."
    }

@router.get("/summary")
async def get_seed_summary():
    """
    Summary counts of all seed sources.
    """
    sources = {
        "seed_extraction_protocol": len(_collect_protocol_seeds()),
        "nasa_seed_search_memory": len(_collect_nasa_seed_search()),
        "seed_extractions_file": len(_collect_seed_files()),
        "nasa_seed_search_file": len(_collect_nasa_search_files()),
        "energy_alerts": len(_collect_energy_alert_seeds()),
        "seeds_unified": len(_collect_unified_seed_files())
    }
    total = sum(sources.values())
    movement = _load_seed_to_movement()

    return {
        "status": "success",
        "total_seeds": total,
        "by_source": sources,
        "seed_to_movement_phases": movement,
        "message": "All seeds from first to now, and the path beyond."
    }

@router.get("/all")
async def get_all_seeds(
    source: Optional[str] = Query(None, description="Filter by source"),
    limit: int = Query(500, description="Max records to return")
):
    """
    Return all seeds across protocols, files, alerts, and future entries.
    """
    records: List[Dict[str, Any]] = []
    records.extend(_collect_protocol_seeds())
    records.extend(_collect_nasa_seed_search())
    records.extend(_collect_seed_files())
    records.extend(_collect_nasa_search_files())
    records.extend(_collect_energy_alert_seeds())
    records.extend(_collect_unified_seed_files())

    total_available = len(records)

    if source:
        records = [r for r in records if r.get("source") == source]

    def _sort_key(item: Dict[str, Any]) -> str:
        return item.get("timestamp") or ""

    records.sort(key=_sort_key, reverse=True)

    if limit:
        records = records[:limit]

    counts: Dict[str, int] = {}
    for record in records:
        counts[record["source"]] = counts.get(record["source"], 0) + 1

    return {
        "status": "success",
        "total_available": total_available,
        "returned": len(records),
        "by_source": counts,
        "seeds": records
    }

@router.post("/register")
async def register_seed(seed: SeedRecord):
    """
    Register a new seed for future tracking ("and beyond").
    """
    record = seed.model_dump()
    file_name = f"seed_{seed.seed_id}_{seed.seed_type}_{seed.created_date.strftime('%Y%m%d_%H%M%S')}.json"
    file_path = SEEDS_UNIFIED_DIR / file_name

    try:
        file_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save seed: {e}")

    return {
        "status": "success",
        "seed_id": seed.seed_id,
        "seed_type": seed.seed_type,
        "origin": seed.origin,
        "source_path": str(file_path),
        "message": "Seed registered for the future path."
    }
