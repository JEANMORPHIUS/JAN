"""
FACTUAL KNOWLEDGE API
Sciences, mathematics, and factual knowledge to retain and build upon.

We are here to fix, not throw away. We keep what is true and refine it.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
from pathlib import Path
from datetime import datetime
import json
import uuid
import logging

router = APIRouter(prefix="/api/knowledge", tags=["Factual Knowledge"])
logger = logging.getLogger(__name__)

BASE_DATA_DIR = Path(__file__).parent.parent.parent / "data" / "factual_knowledge"
SCIENCES_FILE = BASE_DATA_DIR / "sciences_registry.json"
MATH_FILE = BASE_DATA_DIR / "mathematics_registry.json"
FACTS_FILE = BASE_DATA_DIR / "facts_registry.json"

BASE_DATA_DIR.mkdir(parents=True, exist_ok=True)


class KnowledgeEntry(BaseModel):
    entry_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    discipline: str
    summary: str
    facts: List[str] = Field(default_factory=list)
    sources: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_date: datetime = Field(default_factory=datetime.now)


def _default_registry(name: str) -> Dict[str, Any]:
    return {
        "registry": {
            "name": name,
            "purpose": "Preserve and advance factual knowledge",
            "last_updated": datetime.now().isoformat()
        },
        "entries": []
    }


def _load_registry(path: Path, name: str) -> Dict[str, Any]:
    if not path.exists():
        return _default_registry(name)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        logger.warning(f"Failed to read registry {path}: {exc}")
        return _default_registry(name)


def _save_registry(path: Path, registry: Dict[str, Any]) -> None:
    registry.setdefault("registry", {})
    registry["registry"]["last_updated"] = datetime.now().isoformat()
    path.write_text(json.dumps(registry, indent=2), encoding="utf-8")


def _registry_path_for(discipline: str) -> Path:
    key = discipline.strip().lower()
    if key in {"science", "sciences"}:
        return SCIENCES_FILE
    if key in {"mathematics", "math"}:
        return MATH_FILE
    if key in {"factual", "facts", "knowledge"}:
        return FACTS_FILE
    raise HTTPException(status_code=400, detail=f"Unknown discipline: {discipline}")


@router.get("/sources")
async def get_sources():
    return {
        "status": "success",
        "sources": {
            "sciences": str(SCIENCES_FILE),
            "mathematics": str(MATH_FILE),
            "factual": str(FACTS_FILE)
        },
        "exists": {
            "sciences": SCIENCES_FILE.exists(),
            "mathematics": MATH_FILE.exists(),
            "factual": FACTS_FILE.exists()
        },
        "message": "Knowledge sources mapped. Preserve the truth and keep building."
    }


@router.get("/summary")
async def get_summary():
    sciences = _load_registry(SCIENCES_FILE, "Sciences")
    mathematics = _load_registry(MATH_FILE, "Mathematics")
    factual = _load_registry(FACTS_FILE, "Factual Knowledge")

    return {
        "status": "success",
        "totals": {
            "sciences": len(sciences.get("entries", [])),
            "mathematics": len(mathematics.get("entries", [])),
            "factual": len(factual.get("entries", []))
        },
        "message": "We retain what is true and refine it forward."
    }


@router.get("/all")
async def get_all(
    discipline: Optional[str] = Query(None, description="Filter by discipline")
):
    registries = {
        "sciences": _load_registry(SCIENCES_FILE, "Sciences"),
        "mathematics": _load_registry(MATH_FILE, "Mathematics"),
        "factual": _load_registry(FACTS_FILE, "Factual Knowledge")
    }

    if discipline:
        path = _registry_path_for(discipline)
        if path == SCIENCES_FILE:
            return {"status": "success", "discipline": "sciences", "entries": registries["sciences"]["entries"]}
        if path == MATH_FILE:
            return {"status": "success", "discipline": "mathematics", "entries": registries["mathematics"]["entries"]}
        return {"status": "success", "discipline": "factual", "entries": registries["factual"]["entries"]}

    return {
        "status": "success",
        "entries": {
            "sciences": registries["sciences"]["entries"],
            "mathematics": registries["mathematics"]["entries"],
            "factual": registries["factual"]["entries"]
        }
    }


@router.post("/register")
async def register_knowledge(entry: KnowledgeEntry):
    path = _registry_path_for(entry.discipline)
    if path == SCIENCES_FILE:
        registry = _load_registry(SCIENCES_FILE, "Sciences")
    elif path == MATH_FILE:
        registry = _load_registry(MATH_FILE, "Mathematics")
    else:
        registry = _load_registry(FACTS_FILE, "Factual Knowledge")

    registry.setdefault("entries", [])
    registry["entries"].append(entry.model_dump())

    try:
        _save_registry(path, registry)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to save knowledge: {exc}")

    return {
        "status": "success",
        "entry_id": entry.entry_id,
        "discipline": entry.discipline,
        "message": "Knowledge preserved and integrated."
    }
