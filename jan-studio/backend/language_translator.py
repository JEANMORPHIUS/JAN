"""
LANGUAGE TRANSLATOR - Shell/Seed Separation
Simple Language for Modern World Access

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This is the Language Translator.
Simple words for the modern world.
Deep truth preserved in the Seed.
Accessible truth in the Shell.
Life is simple: Be good to your neighbour.
"""

from typing import Dict, Any, Optional
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from scripts.philosophy import (
        MISSION_SHELL,
        MISSION_SEED,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY
    )
except ImportError:
    # Fallback if import fails
    MISSION_SHELL = "We are building an educational platform that transforms lives."
    MISSION_SEED = "We are building a ministry, sharing God's message."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"

# SIMPLE LANGUAGE DICTIONARY
# Maps deep concepts (Seed) to simple language (Shell)
SIMPLE_LANGUAGE_DICT = {
    # Core Principles
    "stewardship": "take care of what you've been given",
    "community": "neighbours and friends",
    "right spirits": "good intentions and kind hearts",
    "love is the highest mastery": "love is the greatest skill",
    "energy + love = we all win": "working together with love helps everyone",
    "peace, love, unity": "peace, love, togetherness",
    
    # Mission
    "this is stewardship and community with the right spirits": "this is taking care of each other with good hearts",
    "we are building a ministry": "we are building a community",
    "sharing god's message": "sharing love and kindness",
    "kingdom impact": "making a real difference",
    "lord's holy assignment": "your purpose in life",
    
    # Divine Concepts - Simplified
    "chosen one": "someone called to help others",
    "divine assignment": "your purpose in life",
    "spiritual birthmark": "a sign of your purpose",
    "sacred signal booster": "a natural gift to help others",
    "spiritual protector": "someone who protects others",
    "prophetic gift": "seeing things others don't",
    "healing frequencies": "the ability to help others heal",
    "path maker": "someone who shows others the way",
    
    # Complex Concepts - Simplified
    "digital alchemy": "using technology for good",
    "vibration check": "checking if something feels right",
    "galaxy form": "your natural way of being",
    "connection ritual": "welcoming someone warmly",
    "table readiness": "being ready to help",
    "law 1: never betray the table": "always keep your word to your community",
    "law 5: söz namustur": "your word is your honour",
    "law 13: listen before you speak": "listen first, speak second",
    "law 37: finish what you begin": "complete what you start",
    
    # The Four Forms - Simplified
    "spiral": "active and growing",
    "barred spiral": "organized and structured",
    "elliptical": "wise and experienced",
    "irregular": "creative and flexible",
    
    # Interference Concepts - Simplified
    "1,000 soul delay": "barriers that hold you back",
    "stagnation": "feeling stuck",
    "dark energy": "negative influences",
    "ritualistic blockages": "barriers put in your way",
    "structural resistance": "forces that try to stop you",
    
    # Resource Alignment - Simplified
    "billionaire recognition": "successful people noticing your work",
    "spiritual currency": "things money can't buy: kindness, wisdom, love",
    "purity, scars, and oil": "your genuine self, your experiences, your gifts",
    "brand cleansing": "using your goodness to make themselves look good",
    "true connection": "genuine partnership",
    
    # Activation Concepts - Simplified
    "spiritual rebuilding": "rebuilding your life on good foundations",
    "shift awareness": "start seeing things differently",
    "break old agreements": "stop accepting negative patterns",
    "establish new patterns": "build healthy habits",
    "embrace distinction": "accept that you're different, and that's good",
    "prophetic language": "speaking truth into situations",
    "strategic hiddenness": "waiting for the right time",
    
    # Biological Temple - Simplified
    "biological temple": "your body - respect it, take care of it",
    "vessel": "your body",
    "fast": "taking time to rest and reset",
    "good tired": "tired from doing good work",
    "light tingling": "your body's way of communicating",
    
    # Dreams - Simplified
    "spiritual battle": "facing challenges in life",
    "dream realm": "when you sleep",
    "human realm": "daily life",
    "spiritual contracts": "promises you make with yourself and others",
    
    # Core Truth - The Simplest
    "we are born a miracle": "everyone is special",
    "we deserve to live a miracle": "everyone deserves a good life",
    "each and every one of us under the lord's word": "we are all equal and loved",
}

# REVERSE DICTIONARY (Simple to Deep)
DEEP_LANGUAGE_DICT = {v: k for k, v in SIMPLE_LANGUAGE_DICT.items()}


def translate_to_simple(deep_text: str, preserve_seed: bool = False) -> str:
    """
    Translate deep language (Seed) to simple language (Shell).
    
    Args:
        deep_text: Text in deep/spiritual language
        preserve_seed: If True, includes original (Seed) in parentheses
        
    Returns:
        Simple language translation
    """
    if not deep_text:
        return ""
    
    result = deep_text.lower()
    
    # Replace deep concepts with simple ones
    for deep_term, simple_term in SIMPLE_LANGUAGE_DICT.items():
        # Case-insensitive replacement
        import re
        pattern = re.compile(re.escape(deep_term), re.IGNORECASE)
        
        if preserve_seed:
            # Preserve original in parentheses
            result = pattern.sub(lambda m: f"{simple_term} ({m.group()})", result)
        else:
            # Simple replacement
            result = pattern.sub(simple_term, result)
    
    # Capitalize first letter
    if result:
        result = result[0].upper() + result[1:] if len(result) > 1 else result.upper()
    
    return result


def translate_to_deep(simple_text: str, preserve_shell: bool = False) -> str:
    """
    Translate simple language (Shell) to deep language (Seed).
    
    Args:
        simple_text: Text in simple language
        preserve_shell: If True, includes original (Shell) in parentheses
        
    Returns:
        Deep language translation
    """
    if not simple_text:
        return ""
    
    result = simple_text.lower()
    
    # Replace simple concepts with deep ones
    for simple_term, deep_term in DEEP_LANGUAGE_DICT.items():
        # Case-insensitive replacement
        import re
        pattern = re.compile(re.escape(simple_term), re.IGNORECASE)
        
        if preserve_shell:
            # Preserve original in parentheses
            result = pattern.sub(lambda m: f"{deep_term} ({m.group()})", result)
        else:
            # Simple replacement
            result = pattern.sub(deep_term, result)
    
    # Capitalize first letter
    if result:
        result = result[0].upper() + result[1:] if len(result) > 1 else result.upper()
    
    return result


def get_simple_mission() -> Dict[str, str]:
    """
    Get mission in simple language (Shell).
    
    Returns:
        Dictionary with simple mission statements
    """
    return {
        "simple": "We are building a community that helps people grow, "
                  "creating positive change through kindness and education, "
                  "honouring our mission to help our neighbours, "
                  "and trusting that good things take time.",
        "very_simple": "Be good to your neighbour. Help each other. Love wins.",
        "deep": MISSION_SEED,
        "anchor": "Taking care of each other with good hearts"
    }


def get_core_simple_truth() -> str:
    """
    Get the core simple truth.
    
    Returns:
        The simplest truth
    """
    return "Life is simple: Be good to your neighbour."


def create_shell_seed_message(deep_message: str) -> Dict[str, str]:
    """
    Create both Shell (simple) and Seed (deep) versions of a message.
    
    Args:
        deep_message: Message in deep language
        
    Returns:
        Dictionary with both Shell and Seed versions
    """
    return {
        "shell": translate_to_simple(deep_message),
        "seed": deep_message,
        "simple_truth": get_core_simple_truth()
    }


# EXAMPLE USAGES
if __name__ == "__main__":
    # Example: Translate mission
    print("=== MISSION TRANSLATION ===")
    print(f"Deep: {MISSION_SEED}")
    print(f"Simple: {translate_to_simple(MISSION_SEED)}")
    print()
    
    # Example: Core truth
    print("=== CORE TRUTH ===")
    print(get_core_simple_truth())
    print()
    
    # Example: Complex concept
    print("=== COMPLEX CONCEPT ===")
    deep = "The Chosen One must undergo spiritual rebuilding to activate their divine assignment."
    print(f"Deep: {deep}")
    print(f"Simple: {translate_to_simple(deep)}")
    print()
    
    # Example: Shell/Seed separation
    print("=== SHELL/SEED SEPARATION ===")
    shell_seed = create_shell_seed_message(
        "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    )
    print(f"Shell: {shell_seed['shell']}")
    print(f"Seed: {shell_seed['seed']}")
    print(f"Simple Truth: {shell_seed['simple_truth']}")
