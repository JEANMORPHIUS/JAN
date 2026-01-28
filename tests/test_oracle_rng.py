"""
Unit tests for Oracle SIYEM Transparent RNG Engine

Tests verify deterministic behavior: same seed = same result
"""

import pytest
import sys
from pathlib import Path

# Add SIYEM services to path
sys.path.insert(0, str(Path(__file__).parent.parent / "SIYEM" / "services"))

from oracle_siyem_integration import TransparentRNG


class TestTransparentRNG:
    """Test transparent RNG engine for deterministic behavior."""
    
    def test_seed_generation_deterministic(self):
        """Test that same inputs produce same seed."""
        rng = TransparentRNG()
        
        # Same inputs
        seed1 = rng.generate_seed("test", "2026-01-28T10:00:00", "context", "user1")
        seed2 = rng.generate_seed("test", "2026-01-28T10:00:00", "context", "user1")
        
        assert seed1["seed"] == seed2["seed"]
        assert seed1["components"] == seed2["components"]
        assert seed1["verifiable"] is True
    
    def test_seed_generation_different_inputs(self):
        """Test that different inputs produce different seeds."""
        rng = TransparentRNG()
        
        seed1 = rng.generate_seed("test1", "2026-01-28T10:00:00", "context", "user1")
        seed2 = rng.generate_seed("test2", "2026-01-28T10:00:00", "context", "user1")
        
        assert seed1["seed"] != seed2["seed"]
    
    def test_seed_components_visible(self):
        """Test that seed components are visible for transparency."""
        rng = TransparentRNG()
        
        seed = rng.generate_seed("test", "2026-01-28T10:00:00", "context", "user1")
        
        assert "components" in seed
        assert seed["components"]["user_intent"] == "test"
        assert seed["components"]["timestamp"] == "2026-01-28T10:00:00"
        assert seed["components"]["context"] == "context"
        assert seed["components"]["user_id"] == "user1"
        assert seed["verifiable"] is True
    
    def test_hexagram_calculation_deterministic(self):
        """Test that same seed produces same hexagram."""
        rng = TransparentRNG()
        
        seed = "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"
        hex1 = rng.seed_to_hexagram(seed)
        hex2 = rng.seed_to_hexagram(seed)
        
        assert hex1["hexagram_number"] == hex2["hexagram_number"]
        assert hex1["hexagram_binary"] == hex2["hexagram_binary"]
        assert hex1["transparent"] is True
    
    def test_hexagram_range(self):
        """Test that hexagram is in valid range (0-63)."""
        rng = TransparentRNG()
        
        # Test multiple seeds
        for i in range(10):
            seed = f"test_seed_{i}" * 10  # Generate different seeds
            seed_hash = rng.generate_seed(seed, "2026-01-28T10:00:00", "", "user1")["seed"]
            hexagram = rng.seed_to_hexagram(seed_hash)
            
            assert 0 <= hexagram["hexagram_number"] <= 63
            assert len(hexagram["hexagram_binary"]) == 6
            assert all(c in "01" for c in hexagram["hexagram_binary"])
    
    def test_hexagram_binary_format(self):
        """Test that hexagram binary is 6-bit format."""
        rng = TransparentRNG()
        
        seed = rng.generate_seed("test", "2026-01-28T10:00:00", "", "user1")["seed"]
        hexagram = rng.seed_to_hexagram(seed)
        
        assert len(hexagram["hexagram_binary"]) == 6
        assert all(c in "01" for c in hexagram["hexagram_binary"])
        assert hexagram["hexagram_number"] == int(hexagram["hexagram_binary"], 2)


class TestRNGVerification:
    """Test that users can verify RNG process."""
    
    def test_user_can_recreate_seed(self):
        """Test that user can recreate seed from components."""
        import hashlib
        
        rng = TransparentRNG()
        seed_data = rng.generate_seed("test", "2026-01-28T10:00:00", "context", "user1")
        
        # User recreates seed
        components = seed_data["components"]
        seed_string = f"{components['user_intent']}:{components['timestamp']}:{components['context']}:{components['user_id']}"
        user_seed = hashlib.sha256(seed_string.encode('utf-8')).hexdigest()
        
        assert user_seed == seed_data["seed"]
    
    def test_user_can_verify_hexagram(self):
        """Test that user can verify hexagram calculation."""
        rng = TransparentRNG()
        seed_data = rng.generate_seed("test", "2026-01-28T10:00:00", "", "user1")
        hexagram_data = rng.seed_to_hexagram(seed_data["seed"])
        
        # User verifies hexagram
        seed_int = int(seed_data["seed"][:16], 16)
        user_hexagram = seed_int % 64
        user_binary = format(user_hexagram, '06b')
        
        assert user_hexagram == hexagram_data["hexagram_number"]
        assert user_binary == hexagram_data["hexagram_binary"]
