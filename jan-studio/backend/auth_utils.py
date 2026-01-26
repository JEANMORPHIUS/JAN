"""Authentication Utilities for JAN Studio
Handles password hashing, JWT tokens, and user verification.

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

from datetime import datetime, timedelta
from typing import Optional
import jwt
from passlib.context import CryptContext
import os

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings - SECURITY: Validate secret key on startup
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-key-CHANGE-IN-PRODUCTION")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

# SECURITY: Validate JWT secret key
if not SECRET_KEY or SECRET_KEY == "dev-secret-key-CHANGE-IN-PRODUCTION":
    raise ValueError(
        "JWT_SECRET_KEY must be set in environment variables. "
        "Never use the default secret in production!"
    )
if len(SECRET_KEY) < 32:
    raise ValueError(
        f"JWT_SECRET_KEY must be at least 32 characters long. "
        f"Current length: {len(SECRET_KEY)}"
    )


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.

    Args:
        data: Dictionary to encode in token (must include 'sub' for user ID)
        expires_delta: Optional custom expiration time

    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """
    Create a JWT refresh token.

    Args:
        data: Dictionary to encode in token (must include 'sub' for user ID)

    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict:
    """
    Decode and verify a JWT token.

    Args:
        token: JWT token string

    Returns:
        Decoded token payload

    Raises:
        Exception: If token is expired or invalid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.JWTError:
        raise Exception("Invalid token")


def get_user_from_token(token: str) -> Optional[int]:
    """
    Extract user ID from token.

    Args:
        token: JWT token string

    Returns:
        User ID if valid, None otherwise
    """
    try:
        payload = decode_token(token)
        user_id: int = payload.get("sub")
        return user_id
    except Exception:
        return None


def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validate password meets strength requirements.

    Args:
        password: Plain text password

    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"

    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"

    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one number"

    return True, ""


def validate_username(username: str) -> tuple[bool, str]:
    """
    Validate username format.

    Args:
        username: Username string

    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"

    if len(username) > 30:
        return False, "Username must be no more than 30 characters long"

    if not username.replace("-", "").replace("_", "").isalnum():
        return False, "Username can only contain letters, numbers, hyphens, and underscores"

    return True, ""
