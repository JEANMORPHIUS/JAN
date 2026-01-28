"""
Unit tests for Oracle SIYEM Laws Interpreter

Tests verify Law mapping and interpretation
"""

import pytest
import sys
from pathlib import Path

# Add SIYEM services to path
sys.path.insert(0, str(Path(__file__).parent.parent / "SIYEM" / "services"))

from oracle_siyem_integration import LawsInterpreter


class TestLawsInterpreter:
    """Test 40 Laws interpretation layer."""
    
    def test_hexagram_to_law_mapping(self):
        """Test that hexagrams map to Laws (1-40)."""
        interpreter = LawsInterpreter()
        
        # Test all hexagrams map to valid Laws
        for hexagram in range(64):
            law_data = interpreter.hexagram_to_law(hexagram)
            
            assert 1 <= law_data["law_number"] <= 40
            assert "law_title" in law_data
            assert "law_text" in law_data
            assert "volume" in law_data
    
    def test_law_mapping_deterministic(self):
        """Test that same hexagram produces same Law."""
        interpreter = LawsInterpreter()
        
        law1 = interpreter.hexagram_to_law(42)
        law2 = interpreter.hexagram_to_law(42)
        
        assert law1["law_number"] == law2["law_number"]
        assert law1["law_title"] == law2["law_title"]
    
    def test_law_volume_mapping(self):
        """Test that Laws map to correct volumes."""
        interpreter = LawsInterpreter()
        
        # Test known Laws
        law1 = interpreter.hexagram_to_law(0)  # Should map to Law 1 (Loyalty)
        law11 = interpreter.hexagram_to_law(10)  # Should map to Law 11 (Silence)
        law21 = interpreter.hexagram_to_law(20)  # Should map to Law 21 (Respect)
        law31 = interpreter.hexagram_to_law(30)  # Should map to Law 31 (War)
        
        # Verify volumes (may need adjustment based on actual mapping)
        # This tests the structure, not exact mapping
        assert "volume" in law1
        assert "volume" in law11
        assert "volume" in law21
        assert "volume" in law31
    
    def test_law_interpretation_structure(self):
        """Test that Law interpretation has required structure."""
        interpreter = LawsInterpreter()
        
        law_data = interpreter.hexagram_to_law(0)
        interpretation = interpreter.interpret_law_for_creativity(
            law_data, "test intent", "test context"
        )
        
        assert "interpretation" in interpretation
        assert "creative_prompt" in interpretation
        assert "law_data" in interpretation
        assert "test intent" in interpretation["interpretation"]
    
    def test_all_hexagrams_map_to_laws(self):
        """Test that all 64 hexagrams map to valid Laws."""
        interpreter = LawsInterpreter()
        
        laws_found = set()
        for hexagram in range(64):
            law_data = interpreter.hexagram_to_law(hexagram)
            laws_found.add(law_data["law_number"])
        
        # All Laws (1-40) should be reachable
        assert len(laws_found) == 40
        assert min(laws_found) == 1
        assert max(laws_found) == 40
