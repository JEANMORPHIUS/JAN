"""SHARED HELPER FUNCTIONS
Common utility functions used across scripts

Extracts common patterns to reduce duplication and improve maintainability.

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
import logging
import sys
from pathlib import Path
from typing import Any, Dict, Optional, List
from datetime import datetime

def setup_logging(
    name: str = __name__,
    level: int = logging.INFO,
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    Set up standardized logging configuration
    
    Args:
        name: Logger name (typically __name__)
        level: Logging level (default: INFO)
        format_string: Custom format string (optional)
    
    Returns:
        Configured logger instance
    """
    if format_string is None:
        format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(format_string)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def load_json(file_path: Path, default: Any = None) -> Any:
    """
    Load JSON file with error handling
    
    Args:
        file_path: Path to JSON file
        default: Default value if file doesn't exist or can't be parsed
    
    Returns:
        Parsed JSON data or default value
    """
    try:
        if not file_path.exists():
            if default is not None:
                return default
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON from {file_path}: {e}")
        if default is not None:
            return default
        raise
    except Exception as e:
        logging.error(f"Error loading JSON from {file_path}: {e}")
        if default is not None:
            return default
        raise

def save_json(data: Any, file_path: Path, indent: int = 2, ensure_ascii: bool = False) -> None:
    """
    Save data to JSON file with error handling
    
    Args:
        data: Data to serialize to JSON
        file_path: Path to save JSON file
        indent: JSON indentation (default: 2)
        ensure_ascii: Ensure ASCII encoding (default: False)
    """
    try:
        # Ensure directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
        
        logging.info(f"Saved JSON to {file_path}")
    except Exception as e:
        logging.error(f"Error saving JSON to {file_path}: {e}")
        raise

def standard_main(
    main_func,
    script_name: Optional[str] = None,
    logger_name: Optional[str] = None
) -> None:
    """
    Standard main function wrapper with error handling
    
    Args:
        main_func: Main function to execute
        script_name: Name of script for logging (optional)
        logger_name: Logger name (optional)
    """
    logger = setup_logging(logger_name or script_name or __name__)
    
    if script_name:
        logger.info(f"Starting {script_name}")
    
    try:
        main_func()
        if script_name:
            logger.info(f"Completed {script_name} successfully")
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error in {script_name or 'script'}: {e}", exc_info=True)
        sys.exit(1)

def load_data_file(file_path: Path, default: Any = None) -> Any:
    """
    Load data file (JSON, with fallback handling)
    
    Args:
        file_path: Path to data file
        default: Default value if file doesn't exist
    
    Returns:
        Loaded data or default
    """
    if file_path.suffix == '.json':
        return load_json(file_path, default)
    else:
        # For other file types, read as text
        try:
            if not file_path.exists():
                return default
            return file_path.read_text(encoding='utf-8')
        except Exception as e:
            logging.error(f"Error loading file {file_path}: {e}")
            return default

def get_timestamp(format_string: str = "%Y%m%d_%H%M%S") -> str:
    """
    Get current timestamp string
    
    Args:
        format_string: DateTime format string
    
    Returns:
        Formatted timestamp string
    """
    return datetime.now().strftime(format_string)

def create_report(
    data: Dict[str, Any],
    output_dir: Path,
    filename: Optional[str] = None,
    format: str = 'json'
) -> Path:
    """
    Create a standardized report file
    
    Args:
        data: Report data dictionary
        output_dir: Output directory
        filename: Filename (optional, will generate if not provided)
        format: Report format ('json' or 'txt')
    
    Returns:
        Path to created report file
    """
    if filename is None:
        timestamp = get_timestamp()
        filename = f"report_{timestamp}.{format}"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / filename
    
    if format == 'json':
        save_json(data, report_path)
    else:
        # Text format - simple key-value output
        with open(report_path, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
    
    return report_path

__all__ = [
    'setup_logging', 'load_json', 'save_json', 'standard_main',
    'load_data_file', 'get_timestamp', 'create_report'
]
