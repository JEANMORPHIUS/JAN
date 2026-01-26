"""JAN Studio Test Configuration
Pytest fixtures and configuration for testing.

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

import pytest
import os
import sys
from pathlib import Path
from typing import Generator
from unittest.mock import MagicMock

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Set test environment
os.environ["ENVIRONMENT"] = "test"
os.environ["DEBUG"] = "true"
os.environ["DATABASE_PATH"] = ":memory:"


@pytest.fixture(scope="session")
def test_config():
    """Test configuration fixture"""
    return {
        "environment": "test",
        "debug": True,
        "database_path": ":memory:",
        "jwt_secret": "test-secret-key-for-testing-only",
        "jwt_algorithm": "HS256",
        "access_token_expire_minutes": 30,
    }


@pytest.fixture
def mock_database():
    """Mock database connection for tests"""
    mock_db = MagicMock()
    mock_db.execute.return_value = MagicMock()
    mock_db.fetchall.return_value = []
    mock_db.fetchone.return_value = None
    return mock_db


@pytest.fixture
def sample_persona():
    """Sample persona data for testing"""
    return {
        "id": "test-persona-1",
        "name": "Test Persona",
        "archetype": "Storyteller",
        "voice": "Friendly and warm",
        "purpose": "Testing purposes",
        "specialization": "Test content generation",
        "themes": ["testing", "quality"],
        "phrases": ["Hello, test!", "Testing in progress"],
        "color": "#FF5733"
    }


@pytest.fixture
def sample_template():
    """Sample prompt template for testing"""
    return {
        "id": "test-template-1",
        "name": "Test Template",
        "entity": "TEST",
        "content": """You are a test persona.

Task: {{task}}

Please respond in a friendly manner.""",
        "variables": ["task"],
        "category": "general"
    }


@pytest.fixture
def auth_headers(test_config):
    """Generate test authentication headers"""
    # In a real test, this would generate a valid JWT token
    return {
        "Authorization": "Bearer test-token-for-testing"
    }


@pytest.fixture
def mock_gemini_response():
    """Mock Gemini API response"""
    return {
        "candidates": [{
            "content": {
                "parts": [{
                    "text": "This is a test response from the mocked Gemini API."
                }]
            }
        }]
    }


@pytest.fixture(scope="function")
def clean_test_dir(tmp_path):
    """Create a clean temporary directory for each test"""
    test_dir = tmp_path / "jan_test"
    test_dir.mkdir()
    return test_dir


# Pytest configuration
def pytest_configure(config):
    """Configure pytest markers"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "security: marks tests as security tests"
    )
