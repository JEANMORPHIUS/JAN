"""
PHILOSOPHY VALIDATION DECORATORS
Enforce THE CHOSEN ONE philosophy alignment at function level

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

These decorators ensure that functions honor the philosophy before execution.
"""

from functools import wraps
from typing import Callable, Any, Optional
import logging

logger = logging.getLogger(__name__)


def check_alignment(
    purpose: str,
    serves_mission: bool = True,
    serves_love: bool = True,
    serves_truth: bool = True,
    serves_community: bool = True
) -> bool:
    """
    Check if a purpose aligns with THE CHOSEN ONE philosophy.
    
    Args:
        purpose: Description of what the function does
        serves_mission: Does it serve stewardship and community?
        serves_love: Does it serve love (highest mastery)?
        serves_truth: Does it serve truth over convenience?
        serves_community: Does it serve "We All Win"?
    
    Returns:
        True if aligned, False otherwise
    """
    purpose_lower = purpose.lower()
    
    # Mission keywords: stewardship, community, right spirits
    mission_keywords = [
        "stewardship", "community", "right spirits", "heritage",
        "temporal", "registry", "cleansing", "regeneration"
    ]
    
    # Love keywords: love, highest mastery, energy
    love_keywords = [
        "love", "highest mastery", "energy", "healing", "regeneration",
        "waiting for", "sanctuary", "biological temple"
    ]
    
    # Truth keywords: truth, integrity, word, bond, immutable
    truth_keywords = [
        "truth", "integrity", "word", "bond", "immutable", "audit",
        "log", "transparent", "honest"
    ]
    
    # Community keywords: we all win, peace, unity, family
    community_keywords = [
        "we all win", "peace", "unity", "family", "serve", "access",
        "transparent", "open", "cooperation"
    ]
    
    alignment_checks = []
    
    if serves_mission:
        alignment_checks.append(
            any(keyword in purpose_lower for keyword in mission_keywords)
        )
    
    if serves_love:
        alignment_checks.append(
            any(keyword in purpose_lower for keyword in love_keywords)
        )
    
    if serves_truth:
        alignment_checks.append(
            any(keyword in purpose_lower for keyword in truth_keywords)
        )
    
    if serves_community:
        alignment_checks.append(
            any(keyword in purpose_lower for keyword in community_keywords)
        )
    
    # All required checks must pass
    return all(alignment_checks) if alignment_checks else True


def requires_alignment(
    serves_mission: bool = True,
    serves_love: bool = True,
    serves_truth: bool = True,
    serves_community: bool = True,
    strict: bool = False
):
    """
    Decorator to enforce philosophical alignment on functions.
    
    Use this to guard critical operations that must honor THE CHOSEN ONE philosophy.
    
    Args:
        serves_mission: Function must serve stewardship and community
        serves_love: Function must serve love (highest mastery)
        serves_truth: Function must serve truth over convenience
        serves_community: Function must serve "We All Win"
        strict: If True, raises ValueError on misalignment. If False, logs warning.
    
    Example:
        @requires_alignment(serves_mission=True, serves_community=True)
        def register_heritage_site(...):
            \"\"\"Register a heritage site across a specific timeline dimension.\"\"\"
            # Implementation honors the philosophy automatically
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Get function purpose from docstring or name
            purpose = func.__doc__ or func.__name__
            
            # Check alignment
            is_aligned = check_alignment(
                purpose,
                serves_mission=serves_mission,
                serves_love=serves_love,
                serves_truth=serves_truth,
                serves_community=serves_community
            )
            
            if not is_aligned:
                error_msg = (
                    f"Function {func.__name__} violates THE CHOSEN ONE philosophy alignment. "
                    f"Purpose: {purpose[:100]}..."
                )
                
                if strict:
                    raise ValueError(error_msg)
                else:
                    logger.warning(
                        error_msg,
                        extra={
                            "function": func.__name__,
                            "purpose": purpose,
                            "serves_mission": serves_mission,
                            "serves_love": serves_love,
                            "serves_truth": serves_truth,
                            "serves_community": serves_community
                        }
                    )
            
            # Execute function
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


def requires_law_5(func: Callable) -> Callable:
    """
    Decorator to enforce Law 5: Your Word Is Your Bond.
    
    Functions decorated with this must:
    - Not silently fail (no except: pass)
    - Log all errors properly
    - Maintain word integrity (broken code = broken word)
    
    Example:
        @requires_law_5
        def critical_operation():
            # Must log errors, not silence them
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Law 5: Broken code = broken word = broken integrity
            # Must log, not silence
            logger.error(
                f"Law 5 violation in {func.__name__}: {e}",
                exc_info=True,
                extra={
                    "function": func.__name__,
                    "law": "Law 5: Your Word Is Your Bond",
                    "error": str(e)
                }
            )
            raise  # Re-raise to maintain integrity
    
    return wrapper


def requires_law_41(func: Callable) -> Callable:
    """
    Decorator to enforce Law 41: Respect the Abandoned.
    
    Functions decorated with this must:
    - Honor the silence of abandoned properties
    - Not exploit heritage sites as "haunted" content
    - Offer regeneration paths, not fear-based loops
    
    Example:
        @requires_law_41
        def process_heritage_content(content: str):
            # Must respect abandoned, offer regeneration
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Check if content argument exists
        content = None
        if args and isinstance(args[0], str):
            content = args[0]
        elif 'content' in kwargs:
            content = kwargs['content']
        elif 'narrative_content' in kwargs:
            content = kwargs['narrative_content']
        
        # If content found, check Law 41 compliance
        if content:
            try:
                from .racon_registry import check_law_41_respect_abandoned
                
                if not check_law_41_respect_abandoned(content):
                    logger.warning(
                        f"Law 41 violation detected in {func.__name__}",
                        extra={
                            "function": func.__name__,
                            "law": "Law 41: Respect the Abandoned",
                            "content_preview": content[:100] + "..." if len(content) > 100 else content
                        }
                    )
            except ImportError:
                # If racon_registry not available, skip check
                pass
        
        return func(*args, **kwargs)
    
    return wrapper


def validate_philosophy_alignment(func: Callable) -> bool:
    """
    Validate that a function's docstring aligns with THE CHOSEN ONE philosophy.
    
    This is a utility function for checking alignment without enforcing it.
    
    Returns:
        True if aligned, False otherwise
    """
    purpose = func.__doc__ or func.__name__
    return check_alignment(purpose)


# Example usage in docstring
__all__ = [
    "requires_alignment",
    "requires_law_5",
    "requires_law_41",
    "check_alignment",
    "validate_philosophy_alignment"
]
