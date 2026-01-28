"""
Integration tests for API endpoints

Tests API endpoints using FastAPI TestClient
"""

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

# Import app (may need adjustment based on actual structure)
try:
    from main import app
    client = TestClient(app)
except ImportError:
    pytest.skip("Could not import app - API tests skipped", allow_module_level=True)


class TestOracleAPI:
    """Test Oracle SIYEM API endpoints."""
    
    def test_cast_oracle_endpoint(self):
        """Test POST /api/oracle-siyem/cast."""
        response = client.post(
            "/api/oracle-siyem/cast",
            json={
                "user_intent": "Test creative guidance",
                "creative_context": "Test context",
                "user_id": "test_api_user"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "timestamp" in data
        assert "user_id" in data
        assert "transparency" in data
        assert "oracle_interpretation" in data
        assert "success_metrics" in data
        assert "mechanism_visualization" in data
    
    def test_get_session_endpoint(self):
        """Test GET /api/oracle-siyem/session."""
        response = client.get("/api/oracle-siyem/session?user_id=test_api_user")
        
        assert response.status_code == 200
        data = response.json()
        
        assert "user_id" in data
        assert "session" in data
        assert "success_score" in data
    
    def test_record_output_endpoint(self):
        """Test POST /api/oracle-siyem/record-output."""
        response = client.post("/api/oracle-siyem/record-output?user_id=test_api_user")
        
        assert response.status_code == 200
        data = response.json()
        
        assert "message" in data
        assert "success_score" in data
    
    def test_get_metrics_endpoint(self):
        """Test GET /api/oracle-siyem/metrics."""
        response = client.get("/api/oracle-siyem/metrics?user_id=test_api_user")
        
        assert response.status_code == 200
        data = response.json()
        
        assert "success_score" in data
        assert "metrics" in data
        assert "guardrails" in data


class TestCampaignAPI:
    """Test Campaign Automation API endpoints."""
    
    def test_add_contact_endpoint(self):
        """Test POST /api/campaign/contacts."""
        response = client.post(
            "/api/campaign/contacts",
            json={
                "email": "test@example.com",
                "name": "Test User",
                "category": "test"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "id" in data
        assert "email" in data
        assert data["email"] == "test@example.com"
    
    def test_get_contacts_endpoint(self):
        """Test GET /api/campaign/contacts."""
        response = client.get("/api/campaign/contacts?category=test")
        
        assert response.status_code == 200
        data = response.json()
        
        assert "contacts" in data
        assert "count" in data
        assert isinstance(data["contacts"], list)
    
    def test_create_social_post_endpoint(self):
        """Test POST /api/campaign/social/create."""
        response = client.post(
            "/api/campaign/social/create",
            json={
                "platform": "twitter",
                "content": "Test post content",
                "scheduled_at": "2026-01-29T10:00:00"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "id" in data
        assert "platform" in data
        assert data["platform"] == "twitter"
