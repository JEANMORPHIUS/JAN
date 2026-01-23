"""
COMMON IMPORTS
Consolidated common imports used across scripts

This module provides commonly used imports to reduce duplication
and ensure consistency across all scripts.
"""

# Standard library imports
import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime, date, timedelta
from typing import List, Dict, Set, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
import subprocess
import re
import shutil
import hashlib
from collections import defaultdict

# Re-export commonly used items
__all__ = [
    'os', 'sys', 'json', 'logging', 'Path', 'datetime', 'date', 'timedelta',
    'List', 'Dict', 'Set', 'Any', 'Optional', 'Tuple',
    'dataclass', 'field', 'asdict',
    'subprocess', 're', 'shutil', 'hashlib', 'defaultdict'
]
