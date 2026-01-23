"""
JAN Studio Backend - Core Backend Components

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

# Core exports
from .temporal_heritage_registry import (
    register_heritage_site,
    add_heritage_narrative,
    get_sites_by_timeline,
    get_chronology_by_year,
    get_temporal_patterns,
    TimelineDimension,
    TimePeriod,
    get_temporal_heritage_db
)

from .racon_registry import (
    check_law_41_respect_abandoned,
    log_immutable_audit
)

from .logging_config import (
    setup_jan_logging,
    get_logger
)

from .database import (
    DatabasePool,
    get_heritage_pool,
    get_racon_pool
)

from .api_error_handler import (
    heritage_api_error_handler
)

from .philosophy_validation import (
    requires_alignment,
    requires_law_5,
    requires_law_41,
    check_alignment,
    validate_philosophy_alignment
)

__all__ = [
    # Temporal Heritage Registry
    "register_heritage_site",
    "add_heritage_narrative",
    "get_sites_by_timeline",
    "get_chronology_by_year",
    "get_temporal_patterns",
    "TimelineDimension",
    "TimePeriod",
    "get_temporal_heritage_db",
    # Racon Registry
    "check_law_41_respect_abandoned",
    "log_immutable_audit",
    # Logging
    "setup_jan_logging",
    "get_logger",
    # Database
    "DatabasePool",
    "get_heritage_pool",
    "get_racon_pool",
    # API
    "heritage_api_error_handler",
    # Philosophy Validation
    "requires_alignment",
    "requires_law_5",
    "requires_law_41",
    "check_alignment",
    "validate_philosophy_alignment",
]
