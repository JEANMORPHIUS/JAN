"""
Pytest configuration and fixtures
"""

import pytest
import sys
from pathlib import Path
import tempfile
import shutil

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "SIYEM" / "services"))
sys.path.insert(0, str(project_root / "jan-studio" / "backend"))


@pytest.fixture
def temp_db_dir():
    """Create temporary directory for test databases."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def test_user_id():
    """Test user ID for Oracle tests."""
    return "test_user"


@pytest.fixture
def sample_intent():
    """Sample user intent for Oracle tests."""
    return "I need creative guidance for my project"


@pytest.fixture
def sample_context():
    """Sample context for Oracle tests."""
    return "Fiction writing, first chapter"
