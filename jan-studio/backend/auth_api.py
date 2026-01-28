"""Authentication API Endpoints

Provides user registration, login, logout, and token management.

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

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Depends, status, Request, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import marketplace_db as db
import auth_utils
from datetime import datetime, timedelta
import jwt

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Rate limiting (if available)
try:
    from slowapi import Limiter
    from slowapi.util import get_remote_address
    RATE_LIMITING_AVAILABLE = True
    # Limiter will be set from app state in main.py
    limiter = None
except ImportError:
    RATE_LIMITING_AVAILABLE = False
    limiter = None

router = APIRouter(prefix="/api/auth", tags=["Authentication"])
security = HTTPBearer()


# ============================================================================
# Request/Response Models
# ============================================================================

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "jan",
                "email": "jan@example.com",
                "password": "SecurePass123!"
            }
        }

    @validator('username')
    def validate_username(cls, v):
        is_valid, error = auth_utils.validate_username(v)
        if not is_valid:
            raise ValueError(error)
        return v

    @validator('password')
    def validate_password(cls, v):
        is_valid, error = auth_utils.validate_password_strength(v)
        if not is_valid:
            raise ValueError(error)
        return v


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "jan@example.com",
                "password": "SecurePass123!"
            }
        }


class RefreshRequest(BaseModel):
    refresh_token: str

    class Config:
        schema_extra = {
            "example": {
                "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsInR5cGUiOiJyZWZyZXNoIiwiZXhwIjoxNzA2NDQ4MDAwfQ.example"
            }
        }


class LogoutRequest(BaseModel):
    refresh_token: str

    class Config:
        schema_extra = {
            "example": {
                "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsInR5cGUiOiJyZWZyZXNoIiwiZXhwIjoxNzA2NDQ4MDAwfQ.example"
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool = False
    created_at: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "jan",
                "email": "jan@example.com",
                "is_admin": False,
                "created_at": "2026-01-27T18:00:00"
            }
        }


# ============================================================================
# Dependencies
# ============================================================================

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """
    Extract and verify user from JWT token.

    Dependency for protected endpoints that require authentication.
    """
    token = credentials.credentials
    user_id = auth_utils.get_user_from_token(token)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.get("is_active", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    return user


async def get_current_admin_user(
    current_user: dict = Depends(get_current_user)
) -> dict:
    """
    Verify current user is an admin.

    Dependency for admin-only endpoints.
    """
    if not current_user.get("is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return current_user


# ============================================================================
# Endpoints
# ============================================================================

def apply_rate_limit(func):
    """Decorator to apply rate limiting if available"""
    if RATE_LIMITING_AVAILABLE and limiter:
        return limiter.limit("5/minute")(func)
    return func

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    request: RegisterRequest = Body(
        examples={
            "default": {
                "summary": "Default registration",
                "value": {
                    "username": "jan",
                    "email": "jan@example.com",
                    "password": "SecurePass123!"
                }
            }
        }
    )
):
    """
    Register a new user account.

    Requires:
    - Unique username (3-30 chars, alphanumeric with hyphens/underscores)
    - Unique email address
    - Strong password (8+ chars, upper, lower, number)

    Returns user object on success.
    """
    # Check if email exists
    existing_user = db.get_user_by_email(request.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Check if username exists
    existing_username = db.get_user_by_username(request.username)
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken"
        )

    # Hash password and create user
    password_hash = auth_utils.hash_password(request.password)

    try:
        user_id = db.create_user_with_password(
            username=request.username,
            email=request.email,
            password_hash=password_hash
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create user: {str(e)}"
        )

    # Get created user
    user = db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="User created but could not be retrieved"
        )
    
    # Ensure all required fields are present
    user_data = {
        "id": user.get("id", user_id),
        "username": user.get("username", request.username),
        "email": user.get("email", request.email),
        "is_admin": user.get("is_admin", False),
        "created_at": user.get("created_at", datetime.utcnow().isoformat())
    }
    
    return UserResponse(**user_data)


@router.post("/login", response_model=TokenResponse)
async def login(
    request: LoginRequest = Body(
        examples={
            "default": {
                "summary": "Default login",
                "value": {
                    "email": "jan@example.com",
                    "password": "SecurePass123!"
                }
            }
        }
    )
):
    """
    Login with email and password.

    Returns access token and refresh token on success.
    Access token expires in 30 minutes, refresh token in 7 days.
    """
    # Get user by email
    user = db.get_user_by_email(request.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    # Verify password
    if not auth_utils.verify_password(request.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    # Check if active
    if not user.get("is_active", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive"
        )

    # Create tokens
    access_token = auth_utils.create_access_token(data={"sub": user["id"]})
    refresh_token = auth_utils.create_refresh_token(data={"sub": user["id"]})

    # Store refresh token hash
    try:
        from datetime import timedelta
        expires_at = datetime.utcnow() + timedelta(days=auth_utils.REFRESH_TOKEN_EXPIRE_DAYS)
        db.store_refresh_token(user["id"], auth_utils.hash_password(refresh_token), expires_at)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to store token: {str(e)}"
        )

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    request: RefreshRequest = Body(
        examples={
            "default": {
                "summary": "Refresh token",
                "value": {
                    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsInR5cGUiOiJyZWZyZXNoIiwiZXhwIjoxNzA2NDQ4MDAwfQ.example"
                }
            }
        }
    )
):
    """
    Get new access token using refresh token.
    
    Seamless session management - no "static" of disconnected sessions.
    Law 37: Finish what we begin - complete the refresh flow.

    Use this when access token expires. Returns new access token
    while keeping the same refresh token. Automatically validates
    refresh token against stored hash for security.
    """
    try:
        # Decode and validate refresh token
        payload = auth_utils.decode_token(request.refresh_token)

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
                headers={"WWW-Authenticate": "Bearer"}
            )

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={"WWW-Authenticate": "Bearer"}
            )

        # Verify user exists and is active
        user = db.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"}
            )

        if not user.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive"
            )

        # Verify refresh token hash matches stored hash (security check)
        # This ensures the refresh token hasn't been revoked
        refresh_token_hash = auth_utils.hash_password(request.refresh_token)
        stored_token = db.get_refresh_token(refresh_token_hash)
        
        if stored_token:
            # Token exists in database - valid
            # Check if token has expired (database query already filters expired, but double-check)
            if stored_token.get("expires_at"):
                try:
                    # Handle both string and datetime objects
                    expires_at = stored_token["expires_at"]
                    if isinstance(expires_at, str):
                        expires_at = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
                    if expires_at < datetime.utcnow():
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Refresh token has expired",
                            headers={"WWW-Authenticate": "Bearer"}
                        )
                except (ValueError, TypeError):
                    # If parsing fails, token is invalid
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid token expiration",
                        headers={"WWW-Authenticate": "Bearer"}
                    )
        else:
            # Token not found - might be revoked
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token invalid or revoked",
                headers={"WWW-Authenticate": "Bearer"}
            )

        # Create new access token (seamless refresh)
        access_token = auth_utils.create_access_token(data={"sub": user_id})

        # Return tokens - refresh token remains the same for seamless experience
        return TokenResponse(
            access_token=access_token,
            refresh_token=request.refresh_token,
            expires_in=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )

    except HTTPException:
        raise
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token has expired. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except jwt.JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Token refresh failed: {str(e)}"
        )


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    """
    Get current authenticated user information.

    Requires valid access token in Authorization header.
    """
    return UserResponse(**current_user)


@router.post("/logout")
async def logout(
    request: LogoutRequest = Body(
        examples={
            "default": {
                "summary": "Logout",
                "value": {
                    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsInR5cGUiOiJyZWZyZXNoIiwiZXhwIjoxNzA2NDQ4MDAwfQ.example"
                }
            }
        }
    ),
    current_user: dict = Depends(get_current_user)
):
    """
    Logout user and invalidate refresh token.

    Removes refresh token from database to prevent reuse.
    Client should also clear stored tokens.
    """
    try:
        db.delete_refresh_token(auth_utils.hash_password(request.refresh_token))
        return {"message": "Logged out successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Logout failed: {str(e)}"
        )


# ============================================================================
# Admin Endpoints
# ============================================================================

@router.get("/admin/users", dependencies=[Depends(get_current_admin_user)])
async def list_users(limit: int = 50, offset: int = 0):
    """
    List all users (admin only).

    Paginated list of users with basic information.
    """
    users = db.list_all_users(limit=limit, offset=offset)
    return {"users": users, "count": len(users)}


@router.put("/admin/users/{user_id}/status", dependencies=[Depends(get_current_admin_user)])
async def update_user_status(user_id: int, is_active: bool):
    """
    Activate or deactivate a user account (admin only).

    Inactive users cannot log in or access protected endpoints.
    """
    db.update_user_status(user_id, is_active)
    return {"message": "User status updated"}
