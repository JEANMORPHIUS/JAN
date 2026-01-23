"""
LOGGING CONFIGURATION
Unified logging system for JAN codebase

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

Honors truth through transparent logging.
Honors Law 5 (Your Word Is Your Bond) - no silent failures.
"""

import logging
import sys
from pathlib import Path
from typing import Optional
from logging.handlers import RotatingFileHandler


def setup_jan_logging(
    log_level: str = "INFO",
    log_dir: Optional[Path] = None,
    console_output: bool = True,
    file_output: bool = True
) -> logging.Logger:
    """
    Configure logging for JAN system.
    
    Honors truth through transparent logging.
    Honors Law 5 (Your Word Is Your Bond) - proper error reporting.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir: Directory for log files (default: logs/ in project root)
        console_output: Whether to output logs to console
        file_output: Whether to output logs to file
    
    Returns:
        Configured root logger
    """
    # Determine log directory
    if log_dir is None:
        # Default to logs/ directory in project root (S:\JAN\logs)
        project_root = Path(__file__).parent.parent.parent
        log_dir = project_root / "logs"
    
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all levels, filter by handlers
    
    # Remove existing handlers to avoid duplicates
    root_logger.handlers.clear()
    
    # File handler (all logs with rotation)
    if file_output:
        file_handler = RotatingFileHandler(
            log_dir / "jan_system.log",
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)  # All levels to file
        file_handler.setFormatter(detailed_formatter)
        root_logger.addHandler(file_handler)
        
        # Separate error log
        error_handler = RotatingFileHandler(
            log_dir / "jan_errors.log",
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
            encoding='utf-8'
        )
        error_handler.setLevel(logging.ERROR)  # Only errors
        error_handler.setFormatter(detailed_formatter)
        root_logger.addHandler(error_handler)
    
    # Console handler (info and above)
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
        console_handler.setFormatter(detailed_formatter)
        root_logger.addHandler(console_handler)
    
    # Log initialization
    root_logger.info("JAN logging system initialized")
    root_logger.info(f"Log level: {log_level.upper()}")
    root_logger.info(f"Log directory: {log_dir}")
    
    return root_logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for a module.
    
    Usage:
        logger = get_logger(__name__)
        logger.info("Message")
        logger.error("Error occurred", exc_info=True)
    
    Args:
        name: Logger name (typically __name__)
    
    Returns:
        Logger instance
    """
    return logging.getLogger(name)


# Initialize logging on import (if not already initialized)
_initialized = False

def initialize_logging_if_needed():
    """Initialize logging if not already done."""
    global _initialized
    if not _initialized:
        setup_jan_logging()
        _initialized = True

# Auto-initialize if this module is imported
# (Can be disabled by setting environment variable)
import os
if os.getenv("JAN_AUTO_INIT_LOGGING", "true").lower() == "true":
    initialize_logging_if_needed()
