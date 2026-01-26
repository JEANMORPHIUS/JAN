"""PATH CONFIGURATION
Centralized path management using Path objects

Replaces hardcoded paths with environment-aware configuration.

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

import os
from pathlib import Path
from typing import Optional

# Base paths - use environment variables if available, otherwise defaults
def _get_drive_letter() -> str:
    """Get drive letter from environment or default to S:"""
    return os.getenv('JAN_DRIVE', 'S:')

def _get_siyem_drive_letter() -> str:
    """Get SIYEM drive letter from environment or default to S:"""
    return os.getenv('SIYEM_DRIVE', 'S:')

# Root paths
JAN_ROOT = Path(f"{_get_drive_letter()}\\JAN")
SIYEM_ROOT = Path(f"{_get_siyem_drive_letter()}\\SIYEM")

# Common subdirectories
JAN_SCRIPTS = JAN_ROOT / "scripts"
JAN_DATA = JAN_ROOT / "data"
JAN_OUTPUT = JAN_ROOT / "output"
JAN_DOCS = JAN_ROOT / "docs"
JAN_ARCHIVE = JAN_ROOT / "ARCHIVE"

SIYEM_CORE = SIYEM_ROOT / "00_CORE"
SIYEM_PRODUCTION = SIYEM_ROOT / "03_PRODUCTION"
SIYEM_PUBLISHING = SIYEM_ROOT / "05_PUBLISHING"
SIYEM_WEB_DEV = SIYEM_ROOT / "08_WEB_DEV"

# Jan Studio paths
JAN_STUDIO = JAN_ROOT / "jan-studio"
JAN_STUDIO_BACKEND = JAN_STUDIO / "backend"
JAN_STUDIO_FRONTEND = JAN_STUDIO / "frontend"

# Homeostasis paths
HOMEOSTASIS_ROOT = JAN_ROOT / "homeostasis-sentinel"

def get_data_path(subpath: Optional[str] = None) -> Path:
    """Get data directory path, optionally with subpath"""
    if subpath:
        return JAN_DATA / subpath
    return JAN_DATA

def get_output_path(subpath: Optional[str] = None) -> Path:
    """Get output directory path, optionally with subpath"""
    if subpath:
        return JAN_OUTPUT / subpath
    return JAN_OUTPUT

def get_archive_path(subpath: Optional[str] = None) -> Path:
    """Get archive directory path, optionally with subpath"""
    if subpath:
        return JAN_ARCHIVE / subpath
    return JAN_ARCHIVE

def ensure_path(path: Path) -> Path:
    """Ensure a path exists, creating directories if needed"""
    if path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
    else:
        path.mkdir(parents=True, exist_ok=True)
    return path

__all__ = [
    'JAN_ROOT', 'SIYEM_ROOT',
    'JAN_SCRIPTS', 'JAN_DATA', 'JAN_OUTPUT', 'JAN_DOCS', 'JAN_ARCHIVE',
    'SIYEM_CORE', 'SIYEM_PRODUCTION', 'SIYEM_PUBLISHING', 'SIYEM_WEB_DEV',
    'JAN_STUDIO', 'JAN_STUDIO_BACKEND', 'JAN_STUDIO_FRONTEND',
    'HOMEOSTASIS_ROOT',
    'get_data_path', 'get_output_path', 'get_archive_path', 'ensure_path'
]
