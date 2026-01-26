"""
UNIFIED FREQUENTIAL ALIGNMENT API
Aligned entities, communities, political figures, and influential figures.

We set the Table with aligned presence. We respond, we don't rush.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
from pathlib import Path
from datetime import datetime
import logging
import json
import uuid
import hashlib

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


router = APIRouter(prefix="/api/frequential", tags=["Frequential Alignment"])
logger = logging.getLogger(__name__)

BASE_DATA_DIR = Path(__file__).parent.parent.parent / "data"
POLITICAL_FIGURES_FILE = BASE_DATA_DIR / "political_figures" / "frequential_political_figures.json"
INFLUENTIAL_FIGURES_FILE = BASE_DATA_DIR / "influential_figures" / "frequential_influential_figures.json"
RESONANCE_PIONEERS_FILE = BASE_DATA_DIR / "intent_alignment_audit" / "resonance_pioneers.json"
FREQUENTIAL_UNIFIED_DIR = BASE_DATA_DIR / "frequential_unified"

FREQUENTIAL_UNIFIED_DIR.mkdir(parents=True, exist_ok=True)


class FrequentialRecord(BaseModel):
    record_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: str
    description: Optional[str] = None
    origin: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_date: datetime = Field(default_factory=datetime.now)


class SyncResult(BaseModel):
    total_seen: int
    created: int
    skipped: int
    dry_run: bool


def _safe_read_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        logger.warning(f"Could not read JSON {path}: {exc}")
        return None


def _collect_political_figures() -> List[Dict[str, Any]]:
    data = _safe_read_json(POLITICAL_FIGURES_FILE) or {}
    figures = data.get("figures", [])
    for figure in figures:
        figure.setdefault("category", "political_figure")
        figure.setdefault("source", str(POLITICAL_FIGURES_FILE))
    return figures


def _collect_influential_figures() -> List[Dict[str, Any]]:
    data = _safe_read_json(INFLUENTIAL_FIGURES_FILE) or {}
    figures = data.get("figures", [])
    for figure in figures:
        figure.setdefault("category", "influential_figure")
        figure.setdefault("source", str(INFLUENTIAL_FIGURES_FILE))
    return figures


def _collect_resonance_pioneers() -> List[Dict[str, Any]]:
    data = _safe_read_json(RESONANCE_PIONEERS_FILE) or {}
    pioneers = data.get("pioneers", [])
    for pioneer in pioneers:
        pioneer.setdefault("category", "community")
        pioneer.setdefault("source", str(RESONANCE_PIONEERS_FILE))
    return pioneers


def _collect_aligned_entities() -> List[Dict[str, Any]]:
    try:
        from aligned_entities_api import tracker as aligned_tracker
        if aligned_tracker is None:
            return []
        entities = []
        for entity in aligned_tracker.entities.values():
            entities.append({
                "entity_id": entity.entity_id,
                "name": entity.name,
                "entity_type": entity.entity_type,
                "industry": entity.industry,
                "description": entity.description,
                "alignment_score": entity.alignment_score,
                "alignment_level": entity.alignment_level,
                "how_they_align": entity.how_they_align,
                "supports_restoration": entity.supports_restoration,
                "frequency_contribution": entity.frequency_contribution,
                "website": entity.website,
                "location": entity.location,
                "category": "aligned_entity",
                "source": "aligned_entities_tracker"
            })
        return entities
    except Exception as exc:
        logger.warning(f"Aligned entities tracker not available: {exc}")
        return []


def _collect_unified_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for file_path in FREQUENTIAL_UNIFIED_DIR.glob("*.json"):
        data = _safe_read_json(file_path)
        if not isinstance(data, dict):
            continue
        data.setdefault("category", "frequential_record")
        data.setdefault("source", str(file_path))
        records.append(data)
    return records


def _dedupe_key(record: Dict[str, Any]) -> str:
    name = str(record.get("name", "")).strip().lower()
    category = str(record.get("category", "")).strip().lower()
    origin = str(record.get("origin") or record.get("source") or "").strip().lower()
    return f"{name}|{category}|{origin}"


def _normalize_record(record: Dict[str, Any], category: str, origin: str) -> Dict[str, Any]:
    normalized = {
        "record_id": record.get("record_id"),
        "name": record.get("name") or record.get("title") or "unknown",
        "category": category,
        "description": record.get("description"),
        "origin": origin,
        "metadata": record,
        "created_date": record.get("created_date") or datetime.now().isoformat()
    }
    return normalized


def _write_unified_record(record: Dict[str, Any], dry_run: bool) -> bool:
    record_id = record.get("record_id") or str(uuid.uuid4())
    record["record_id"] = record_id
    file_name = f"frequential_{record_id}_{record['category']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    file_path = FREQUENTIAL_UNIFIED_DIR / file_name
    if dry_run:
        return True
    try:
        file_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
        return True
    except Exception as exc:
        logger.warning(f"Failed to write unified record: {exc}")
        return False


def _collect_communities_from_entities(entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {
            **entity,
            "category": "community",
            "source": entity.get("source", "aligned_entities_tracker")
        }
        for entity in entities
        if str(entity.get("entity_type", "")).lower() == "community"
    ]


def _build_records() -> Dict[str, List[Dict[str, Any]]]:
    aligned_entities = _collect_aligned_entities()
    political_figures = _collect_political_figures()
    influential_figures = _collect_influential_figures()
    resonance_pioneers = _collect_resonance_pioneers()
    community_entities = _collect_communities_from_entities(aligned_entities)
    unified_records = _collect_unified_records()

    return {
        "aligned_entities": aligned_entities,
        "communities": community_entities + resonance_pioneers,
        "political_figures": political_figures,
        "influential_figures": influential_figures,
        "resonance_pioneers": resonance_pioneers,
        "frequential_records": unified_records
    }


def _sync_to_unified(dry_run: bool = False) -> SyncResult:
    existing = _collect_unified_records()
    existing_keys = {_dedupe_key(r) for r in existing}
    records = _build_records()

    flat_records: List[Dict[str, Any]] = []
    for group, values in records.items():
        if group == "frequential_records":
            continue
        for value in values:
            category = value.get("category") or group
            origin = value.get("source") or group
            flat_records.append(_normalize_record(value, category, origin))

    created = 0
    skipped = 0
    for record in flat_records:
        record_key = _dedupe_key(record)
        if record_key in existing_keys:
            skipped += 1
            continue
        if _write_unified_record(record, dry_run):
            created += 1
            existing_keys.add(record_key)
        else:
            skipped += 1

    return SyncResult(
        total_seen=len(flat_records),
        created=created,
        skipped=skipped,
        dry_run=dry_run
    )


@router.get("/sources")
async def get_sources():
    """List frequential data sources."""
    return {
        "status": "success",
        "sources": {
            "political_figures": str(POLITICAL_FIGURES_FILE),
            "influential_figures": str(INFLUENTIAL_FIGURES_FILE),
            "resonance_pioneers": str(RESONANCE_PIONEERS_FILE),
            "aligned_entities": "aligned_entities_tracker",
            "frequential_records": str(FREQUENTIAL_UNIFIED_DIR)
        },
        "exists": {
            "political_figures": POLITICAL_FIGURES_FILE.exists(),
            "influential_figures": INFLUENTIAL_FIGURES_FILE.exists(),
            "resonance_pioneers": RESONANCE_PIONEERS_FILE.exists(),
            "frequential_records": FREQUENTIAL_UNIFIED_DIR.exists()
        },
        "message": "All frequential alignment sources mapped."
    }


@router.get("/summary")
async def get_summary():
    """Summary counts for all aligned groups."""
    records = _build_records()
    summary = {key: len(values) for key, values in records.items()}
    total = sum(summary.values())

    return {
        "status": "success",
        "total_records": total,
        "by_category": summary,
        "message": "The Table is set. We respond, we do not rush."
    }


@router.get("/all")
async def get_all(
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: int = Query(500, description="Max records to return"),
    dedupe: bool = Query(True, description="Deduplicate by name/category/origin")
):
    """Get all frequentially aligned records."""
    records = _build_records()
    all_records: List[Dict[str, Any]] = []
    for values in records.values():
        all_records.extend(values)

    if category:
        all_records = [r for r in all_records if r.get("category") == category]

    def _sort_key(item: Dict[str, Any]) -> str:
        return (
            item.get("discovered_at")
            or item.get("last_updated")
            or item.get("timestamp")
            or ""
        )

    all_records.sort(key=_sort_key, reverse=True)

    if dedupe:
        deduped: Dict[str, Dict[str, Any]] = {}
        for record in all_records:
            key = _dedupe_key(record)
            deduped[key] = record
        all_records = list(deduped.values())

    if limit:
        all_records = all_records[:limit]

    return {
        "status": "success",
        "returned": len(all_records),
        "records": all_records
    }


@router.get("/political-figures")
async def get_political_figures():
    return {
        "status": "success",
        "records": _collect_political_figures()
    }


@router.get("/influential-figures")
async def get_influential_figures():
    return {
        "status": "success",
        "records": _collect_influential_figures()
    }


@router.get("/communities")
async def get_communities():
    entities = _collect_aligned_entities()
    communities = _collect_communities_from_entities(entities)
    pioneers = _collect_resonance_pioneers()
    return {
        "status": "success",
        "records": communities + pioneers
    }


@router.get("/aligned-entities")
async def get_aligned_entities():
    return {
        "status": "success",
        "records": _collect_aligned_entities()
    }


@router.post("/sync")
async def sync_records(
    dry_run: bool = Query(True, description="Only report, do not write files")
):
    """
    Sync current sources into the unified registry with deduping.
    """
    result = _sync_to_unified(dry_run=dry_run)
    return {
        "status": "success",
        "result": result.model_dump()
    }


@router.post("/register")
async def register_frequential_record(record: FrequentialRecord):
    """
    Register a new aligned entity/community/figure for future alignment.
    """
    payload = record.model_dump()
    file_name = f"frequential_{record.record_id}_{record.category}_{record.created_date.strftime('%Y%m%d_%H%M%S')}.json"
    file_path = FREQUENTIAL_UNIFIED_DIR / file_name

    try:
        file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to save record: {exc}")

    return {
        "status": "success",
        "record_id": record.record_id,
        "category": record.category,
        "source_path": str(file_path),
        "message": "Record registered. We respond, we don't rush."
    }
