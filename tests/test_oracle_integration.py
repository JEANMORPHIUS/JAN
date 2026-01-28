"""
Integration tests for Oracle SIYEM

Tests the complete Oracle casting flow
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime

# Add SIYEM services to path
sys.path.insert(0, str(Path(__file__).parent.parent / "SIYEM" / "services"))

from oracle_siyem_integration import OracleSIYEM, AntiAddictionMetrics


class TestOracleIntegration:
    """Test complete Oracle SIYEM integration."""
    
    def test_complete_oracle_cast(self):
        """Test complete Oracle cast flow."""
        oracle = OracleSIYEM()
        
        result = oracle.cast_oracle(
            user_intent="Test creative guidance",
            context="Test context",
            user_id="test_user"
        )
        
        # Verify structure
        assert "timestamp" in result
        assert "user_id" in result
        assert "user_intent" in result
        assert "transparency" in result
        assert "oracle_interpretation" in result
        assert "ethical_guardrails" in result
        assert "session" in result
        assert "success_score" in result
    
    def test_transparency_data_complete(self):
        """Test that transparency data is complete."""
        oracle = OracleSIYEM()
        
        result = oracle.cast_oracle(
            user_intent="Test",
            context="Test",
            user_id="test_user"
        )
        
        transparency = result["transparency"]
        
        assert "seed" in transparency
        assert "hexagram" in transparency
        assert "law_mapping" in transparency
        assert transparency["verifiable"] is True
        
        # Verify seed structure
        assert "seed" in transparency["seed"]
        assert "components" in transparency["seed"]
        assert "method" in transparency["seed"]
        
        # Verify hexagram structure
        assert "hexagram_number" in transparency["hexagram"]
        assert "hexagram_binary" in transparency["hexagram"]
        assert "method" in transparency["hexagram"]
        
        # Verify law mapping
        assert "law_number" in transparency["law_mapping"]
        assert "method" in transparency["law_mapping"]
    
    def test_mechanism_visualization_present(self):
        """Test that mechanism visualization is included."""
        oracle = OracleSIYEM()
        
        result = oracle.cast_oracle(
            user_intent="Test",
            context="Test",
            user_id="test_user"
        )
        
        assert "mechanism_visualization" in result
        visualization = result["mechanism_visualization"]
        
        assert "flow" in visualization
        assert "verification_steps" in visualization
        assert "transparency_level" in visualization
        assert len(visualization["flow"]) == 4  # 4 steps
    
    def test_success_metrics_present(self):
        """Test that success metrics are included."""
        oracle = OracleSIYEM()
        
        result = oracle.cast_oracle(
            user_intent="Test",
            context="Test",
            user_id="test_user"
        )
        
        assert "success_metrics" in result
        metrics = result["success_metrics"]
        
        assert "success_score" in metrics
        assert "cast_count" in metrics
        assert "creative_outputs" in metrics
        assert "is_healthy" in metrics
        assert "interpretation" in metrics
    
    def test_ethical_guardrails_function(self):
        """Test that ethical guardrails work correctly."""
        oracle = OracleSIYEM()
        metrics = AntiAddictionMetrics()
        
        # Cast multiple times
        for i in range(5):
            oracle.cast_oracle(
                user_intent=f"Test {i}",
                user_id="test_user_guardrails"
            )
        
        guardrails = metrics.check_ethical_guardrails("test_user_guardrails")
        
        assert "status" in guardrails
        assert "recommendations" in guardrails
        assert guardrails["status"] in ["healthy", "break_suggested", "reflection_suggested", "execution_nudged"]
    
    def test_success_score_calculation(self):
        """Test success score calculation."""
        metrics = AntiAddictionMetrics()
        
        # Create session with casts but no outputs
        oracle = OracleSIYEM()
        oracle.cast_oracle(user_intent="Test", user_id="test_score")
        
        score1 = metrics.calculate_success_score("test_score")
        assert score1 == 0.0  # No outputs yet
        
        # Record output
        metrics.record_creative_output("test_score")
        score2 = metrics.calculate_success_score("test_score")
        assert score2 > 0.0  # Should have positive score now


class TestAntiAddictionMetrics:
    """Test anti-addiction metrics system."""
    
    def test_session_creation(self):
        """Test that sessions are created correctly."""
        metrics = AntiAddictionMetrics()
        
        session = metrics.get_user_session("test_session_user")
        
        assert "user_id" in session
        assert "session_date" in session
        assert "cast_count" in session
        assert "creative_outputs" in session
        assert session["cast_count"] == 0
    
    def test_cast_recording(self):
        """Test that casts are recorded."""
        metrics = AntiAddictionMetrics()
        
        session_before = metrics.get_user_session("test_cast_user")
        initial_count = session_before["cast_count"]
        
        metrics.record_cast("test_cast_user")
        
        session_after = metrics.get_user_session("test_cast_user")
        assert session_after["cast_count"] == initial_count + 1
    
    def test_creative_output_recording(self):
        """Test that creative outputs are recorded."""
        metrics = AntiAddictionMetrics()
        
        session_before = metrics.get_user_session("test_output_user")
        initial_outputs = session_before.get("creative_outputs", 0)
        
        metrics.record_creative_output("test_output_user")
        
        session_after = metrics.get_user_session("test_output_user")
        assert session_after.get("creative_outputs", 0) == initial_outputs + 1
    
    def test_success_score_with_outputs(self):
        """Test success score when user creates outputs."""
        metrics = AntiAddictionMetrics()
        
        # Cast 3 times, create 5 outputs (healthy practice)
        oracle = OracleSIYEM()
        for i in range(3):
            oracle.cast_oracle(user_intent=f"Test {i}", user_id="test_healthy")
        
        for i in range(5):
            metrics.record_creative_output("test_healthy")
        
        score = metrics.calculate_success_score("test_healthy")
        assert score > 50.0  # Should be healthy (more outputs than casts)
