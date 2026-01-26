"""Security Utilities for JAN Studio
Input sanitization, validation, and security helpers.

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

This code protects the system, the data, and the community.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import re
from html import escape
from typing import Optional
import unicodedata


def sanitize_input(text: str, max_length: Optional[int] = None) -> str:
    """
    Sanitize user input to prevent XSS and injection attacks.
    
    Args:
        text: Input string to sanitize
        max_length: Optional maximum length (truncate if exceeded)
    
    Returns:
        Sanitized string
    """
    if not isinstance(text, str):
        text = str(text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Escape HTML special characters
    text = escape(text)
    
    # Remove control characters (except newlines and tabs)
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    
    # Normalize Unicode
    text = unicodedata.normalize('NFKC', text)
    
    # Trim whitespace
    text = text.strip()
    
    # Apply length limit if specified
    if max_length and len(text) > max_length:
        text = text[:max_length]
    
    return text


def validate_turkish_text(text: str) -> tuple[bool, str]:
    """
    Validate Turkish character encoding.
    
    Args:
        text: Text to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        # Try to encode as UTF-8
        text.encode('utf-8')
        
        # Check for valid Turkish characters
        turkish_chars = set('çğıöşüÇĞIİÖŞÜ')
        if any(char in turkish_chars for char in text):
            # Verify proper Turkish character handling
            normalized = unicodedata.normalize('NFC', text)
            if normalized != text:
                return False, "Turkish characters must be properly normalized"
        
        return True, ""
    except UnicodeEncodeError:
        return False, "Invalid character encoding"


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to prevent path traversal and injection.
    
    Args:
        filename: Original filename
    
    Returns:
        Sanitized filename
    """
    # Remove path components
    filename = filename.replace('..', '').replace('/', '').replace('\\', '')
    
    # Remove control characters
    filename = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', filename)
    
    # Keep only alphanumeric, dots, hyphens, underscores
    filename = re.sub(r'[^a-zA-Z0-9._-]', '', filename)
    
    # Limit length
    if len(filename) > 255:
        filename = filename[:255]
    
    return filename


def validate_email(email: str) -> tuple[bool, str]:
    """
    Validate email format (basic validation).
    
    Args:
        email: Email address to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not email or len(email) > 254:
        return False, "Email address is invalid or too long"
    
    # Basic email regex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False, "Email address format is invalid"
    
    return True, ""


def validate_url(url: str, allowed_schemes: Optional[list] = None) -> tuple[bool, str]:
    """
    Validate URL format and scheme.
    
    Args:
        url: URL to validate
        allowed_schemes: List of allowed URL schemes (default: ['http', 'https'])
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if allowed_schemes is None:
        allowed_schemes = ['http', 'https']
    
    if not url or len(url) > 2048:
        return False, "URL is invalid or too long"
    
    # Check scheme
    if '://' not in url:
        return False, "URL must include scheme (http:// or https://)"
    
    scheme = url.split('://')[0].lower()
    if scheme not in allowed_schemes:
        return False, f"URL scheme must be one of: {', '.join(allowed_schemes)}"
    
    return True, ""


def check_sql_injection_pattern(text: str) -> bool:
    """
    Check for common SQL injection patterns (basic check).
    Note: This is a basic check. Always use parameterized queries!
    
    Args:
        text: Text to check
    
    Returns:
        True if suspicious pattern found, False otherwise
    """
    sql_patterns = [
        r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|EXEC|EXECUTE)\b)",
        r"(--|#|/\*|\*/)",
        r"(\b(OR|AND)\s+\d+\s*=\s*\d+)",
        r"('|(\\')|(;)|(\|)|(\*))",
    ]
    
    text_upper = text.upper()
    for pattern in sql_patterns:
        if re.search(pattern, text_upper, re.IGNORECASE):
            return True
    
    return False
