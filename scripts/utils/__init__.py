"""SHARED UTILITIES FOR JAN SCRIPTS
Common imports, functions, and configurations

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

PEACE, LOVE, UNITY

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from .common_imports import *
from .helpers import *
from .paths import *
from .data_collectors import *

__all__ = [
    # Common imports
    'datetime', 'json', 'logging', 'Path', 'sys', 'os',
    # Helpers
    'setup_logging', 'load_json', 'save_json', 'standard_main',
    # Paths
    'JAN_ROOT', 'SIYEM_ROOT', 'get_data_path', 'get_output_path',
    # Data collectors
    'save_event_data', 'load_event_data', 'format_event_summary'
]
