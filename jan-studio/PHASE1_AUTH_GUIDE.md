# Phase 1: Authentication System Implementation Guide

**Goal:** Enable user accounts and authentication for JAN Studio marketplace.

**Timeline:** Week 1-2
**Priority:** 🔴 Critical (blocks all other features)

---

## Overview

This guide walks through implementing a complete authentication system for the JAN Studio marketplace, enabling:
- User registration and login
- Session management with JWT
- Protected routes and API endpoints
- User dashboard access

---

## Technology Stack

**Backend:**
- FastAPI (existing)
- SQLite (existing)
- PyJWT (for tokens)
- passlib + bcrypt (for passwords)

**Frontend:**
- Next.js 14 (existing)
- React Context (for auth state)
- axios (existing)
- localStorage (for token storage)

---

## Architecture Decision: Simple JWT Auth

**Why JWT over OAuth (for MVP)?**
✅ Faster to implement (2-3 days vs 1-2 weeks)
✅ No external dependencies
✅ Full control over flow
✅ Easy to test
✅ Can add OAuth later

**We can upgrade to OAuth later when needed.**

---

## Step 1: Install Dependencies

### Backend

```bash
cd backend
pip install pyjwt passlib[bcrypt] python-multipart
```

Update `requirements.txt`:
```txt
# Add to existing requirements.txt
pyjwt==2.8.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
```

---

## Step 2: Database Schema Updates

### Add Authentication Fields

```sql
-- Update users table (in marketplace_db.py init_database())

-- Drop and recreate users table with new fields
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add auth_tokens table for refresh tokens
CREATE TABLE auth_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    refresh_token_hash TEXT NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_auth_tokens_user ON auth_tokens(user_id);
CREATE INDEX idx_auth_tokens_hash ON auth_tokens(refresh_token_hash);
```

---

## Step 3: Authentication Utilities

### Create `backend/auth_utils.py`

```python
"""
Authentication utilities for JAN Studio.
Handles password hashing, JWT tokens, and user verification.
"""

from datetime import datetime, timedelta
from typing import Optional
import jwt
from passlib.context import CryptContext
import os

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7


def hash_password(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """Create a JWT refresh token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict:
    """Decode and verify a JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.JWTError:
        raise Exception("Invalid token")


def get_user_from_token(token: str) -> Optional[int]:
    """Extract user ID from token."""
    try:
        payload = decode_token(token)
        user_id: int = payload.get("sub")
        return user_id
    except Exception:
        return None
```

---

## Step 4: Authentication API

### Create `backend/auth_api.py`

```python
"""
Authentication API Endpoints
"""

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional
import marketplace_db as db
import auth_utils
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/auth", tags=["Authentication"])
security = HTTPBearer()


# Request/Response Models

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool
    created_at: str


# Dependency: Get current user from token

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """Extract and verify user from JWT token."""
    token = credentials.credentials
    user_id = auth_utils.get_user_from_token(token)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    user = db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    if not user.get("is_active"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    return user


# Endpoints

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    """Register a new user."""
    # Check if user exists
    existing_user = db.get_user_by_email(request.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    existing_username = db.get_user_by_username(request.username)
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken"
        )

    # Validate password strength
    if len(request.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters"
        )

    # Hash password and create user
    password_hash = auth_utils.hash_password(request.password)
    user_id = db.create_user_with_password(
        username=request.username,
        email=request.email,
        password_hash=password_hash
    )

    # Get created user
    user = db.get_user_by_id(user_id)
    return UserResponse(**user)


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """Login and get access token."""
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
    db.store_refresh_token(user["id"], auth_utils.hash_password(refresh_token))

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str):
    """Get new access token using refresh token."""
    try:
        payload = auth_utils.decode_token(refresh_token)

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type"
            )

        user_id = payload.get("sub")
        user = db.get_user_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        # Create new access token
        access_token = auth_utils.create_access_token(data={"sub": user_id})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    """Get current user information."""
    return UserResponse(**current_user)


@router.post("/logout")
async def logout(
    refresh_token: str,
    current_user: dict = Depends(get_current_user)
):
    """Logout user (invalidate refresh token)."""
    db.delete_refresh_token(current_user["id"], auth_utils.hash_password(refresh_token))
    return {"message": "Logged out successfully"}
```

---

## Step 5: Database Functions

### Update `marketplace_db.py`

Add these functions:

```python
def create_user_with_password(username: str, email: str, password_hash: str) -> int:
    """Create a new user with password."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        return cursor.lastrowid


def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Get user by ID."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Get user by email."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        return dict(row) if row else None


def store_refresh_token(user_id: int, token_hash: str):
    """Store a refresh token."""
    with get_db() as conn:
        cursor = conn.cursor()
        expires_at = datetime.now() + timedelta(days=7)
        cursor.execute(
            "INSERT INTO auth_tokens (user_id, refresh_token_hash, expires_at) VALUES (?, ?, ?)",
            (user_id, token_hash, expires_at)
        )


def delete_refresh_token(user_id: int, token_hash: str):
    """Delete a refresh token."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM auth_tokens WHERE user_id = ? AND refresh_token_hash = ?",
            (user_id, token_hash)
        )
```

---

## Step 6: Update main.py

Add auth router to main.py:

```python
# In main.py, add:

try:
    from auth_api import router as auth_router
    app.include_router(auth_router)
except ImportError as e:
    print(f"Warning: Could not import auth_router: {e}")
```

---

## Step 7: Frontend - Auth Context

### Create `frontend/src/contexts/AuthContext.tsx`

```typescript
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { login as apiLogin, register as apiRegister, logout as apiLogout, getCurrentUser } from '@/api/auth';

interface User {
  id: number;
  username: string;
  email: string;
  is_admin: boolean;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (username: string, email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Load user on mount
  useEffect(() => {
    loadUser();
  }, []);

  const loadUser = async () => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      setLoading(false);
      return;
    }

    try {
      const userData = await getCurrentUser();
      setUser(userData);
    } catch (err) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    } finally {
      setLoading(false);
    }
  };

  const login = async (email: string, password: string) => {
    const { access_token, refresh_token } = await apiLogin(email, password);
    localStorage.setItem('access_token', access_token);
    localStorage.setItem('refresh_token', refresh_token);
    await loadUser();
  };

  const register = async (username: string, email: string, password: string) => {
    await apiRegister(username, email, password);
    // Auto-login after registration
    await login(email, password);
  };

  const logout = async () => {
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
      try {
        await apiLogout(refreshToken);
      } catch (err) {
        // Ignore errors on logout
      }
    }
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        register,
        logout,
        isAuthenticated: !!user,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}
```

---

## Step 8: Frontend - Auth API

### Create `frontend/src/api/auth.ts`

```typescript
import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      const refreshToken = localStorage.getItem('refresh_token');
      if (refreshToken) {
        try {
          const { access_token } = await refreshAccessToken(refreshToken);
          localStorage.setItem('access_token', access_token);
          originalRequest.headers.Authorization = `Bearer ${access_token}`;
          return api(originalRequest);
        } catch (err) {
          // Refresh failed, logout
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          window.location.href = '/login';
        }
      }
    }

    return Promise.reject(error);
  }
);

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
  is_admin: boolean;
  created_at: string;
}

export async function register(username: string, email: string, password: string): Promise<User> {
  const response = await api.post('/api/auth/register', { username, email, password });
  return response.data;
}

export async function login(email: string, password: string): Promise<LoginResponse> {
  const response = await api.post('/api/auth/login', { email, password });
  return response.data;
}

export async function logout(refreshToken: string): Promise<void> {
  await api.post('/api/auth/logout', { refresh_token: refreshToken });
}

export async function getCurrentUser(): Promise<User> {
  const response = await api.get('/api/auth/me');
  return response.data;
}

export async function refreshAccessToken(refreshToken: string): Promise<{ access_token: string }> {
  const response = await api.post('/api/auth/refresh', { refresh_token: refreshToken });
  return response.data;
}

export default api;
```

---

## Step 9: Update _app.tsx

Wrap app with AuthProvider:

```typescript
// In pages/_app.tsx

import { AuthProvider } from '@/contexts/AuthContext';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  );
}
```

---

## Step 10: Create Login/Register Pages

### `frontend/src/pages/login.tsx`

```typescript
import { useState } from 'react';
import { useRouter } from 'next/router';
import Link from 'next/link';
import { useAuth } from '@/contexts/AuthContext';

export default function Login() {
  const router = useRouter();
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await login(email, password);
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '4rem auto', padding: '2rem' }}>
      <h1>Login to JAN Studio</h1>

      {error && (
        <div className="error" style={{ marginBottom: '1rem' }}>
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '1rem' }}>
          <label className="label">Email</label>
          <input
            type="email"
            className="input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div style={{ marginBottom: '1rem' }}>
          <label className="label">Password</label>
          <input
            type="password"
            className="input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <button
          type="submit"
          className="button"
          disabled={loading}
          style={{ width: '100%', marginBottom: '1rem' }}
        >
          {loading ? 'Logging in...' : 'Login'}
        </button>
      </form>

      <p style={{ textAlign: 'center', color: '#999' }}>
        Don't have an account?{' '}
        <Link href="/register" style={{ color: '#4a9eff' }}>
          Register
        </Link>
      </p>
    </div>
  );
}
```

### `frontend/src/pages/register.tsx`

Similar to login, with username field added.

---

## Step 11: Protected Routes

### Create `frontend/src/components/ProtectedRoute.tsx`

```typescript
import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '@/contexts/AuthContext';

export default function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !isAuthenticated) {
      router.push('/login');
    }
  }, [isAuthenticated, loading, router]);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (!isAuthenticated) {
    return null;
  }

  return <>{children}</>;
}
```

---

## Step 12: Testing Checklist

### Backend Tests

```bash
# Test registration
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"password123"}'

# Test login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Test protected endpoint
curl -X GET http://localhost:8000/api/auth/me \
  -H "Authorization: Bearer <access_token>"
```

### Frontend Tests

- [ ] Register new user
- [ ] Login with credentials
- [ ] Access protected route
- [ ] Logout
- [ ] Try accessing protected route after logout
- [ ] Token refresh works
- [ ] Invalid credentials show error

---

## Environment Variables

Add to `.env`:

```env
# JWT Configuration
JWT_SECRET_KEY=your-super-secret-key-change-in-production

# Token Expiry (minutes)
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Session Length (days)
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## Security Checklist

- [ ] Passwords are hashed with bcrypt
- [ ] JWT secret is strong and in .env
- [ ] Tokens have expiry
- [ ] Password minimum length enforced
- [ ] Email validation
- [ ] HTTPS only in production
- [ ] Rate limiting on auth endpoints
- [ ] Secure cookie settings
- [ ] CORS configured correctly

---

## Next Steps After Implementation

Once auth is working:

1. **Week 2:** Build creator dashboard
2. **Add user menu** to header
3. **Protect marketplace submit** (require login)
4. **Associate personas with users**
5. **Add "My Personas"** to dashboard

---

## Troubleshooting

### Token not working
- Check JWT_SECRET_KEY is set
- Verify token format: "Bearer <token>"
- Check token hasn't expired

### Registration fails
- Check username/email uniqueness
- Verify password length
- Check database permissions

### Frontend not authenticated
- Check localStorage has tokens
- Verify API_URL is correct
- Check CORS settings

---

**Version:** 1.0
**Created:** 2026-01-13
**Status:** Ready for Implementation
**Estimated Time:** 2-3 days for experienced developer
