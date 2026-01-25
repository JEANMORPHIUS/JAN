# JAN Studio Security Hardening Guide

**Security best practices and hardening checklist for JAN Studio.**

---

## Table of Contents

1. [Security Checklist](#security-checklist)
2. [Authentication & Authorization](#authentication--authorization)
3. [Secrets Management](#secrets-management)
4. [Network Security](#network-security)
5. [Input Validation](#input-validation)
6. [Security Headers](#security-headers)
7. [Logging & Auditing](#logging--auditing)
8. [Dependency Security](#dependency-security)
9. [Incident Response](#incident-response)

---

## Security Checklist

### Pre-Deployment Security Review

#### Critical (Must Fix)
- [ ] No API keys or secrets in source code
- [ ] `.env` files excluded from git (check `.gitignore`)
- [ ] JWT secret key is strong (32+ characters, random)
- [ ] HTTPS enforced in production
- [ ] CORS configured for production domains only
- [ ] Rate limiting enabled
- [ ] Input validation on all endpoints

#### High Priority
- [ ] Security headers configured (HSTS, CSP, X-Frame-Options)
- [ ] Authentication required for sensitive endpoints
- [ ] Password hashing using bcrypt/argon2
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF protection enabled

#### Medium Priority
- [ ] Audit logging enabled
- [ ] Failed login attempt tracking
- [ ] Session timeout configured
- [ ] File upload restrictions
- [ ] Error messages don't leak sensitive info

---

## Authentication & Authorization

### JWT Configuration

```python
# Recommended JWT settings
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Never hardcode!
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Validate JWT secret is strong enough
def validate_jwt_secret():
    secret = os.getenv("JWT_SECRET_KEY", "")
    if len(secret) < 32:
        raise ValueError("JWT_SECRET_KEY must be at least 32 characters")
    if secret == "your-secret-key" or "example" in secret.lower():
        raise ValueError("JWT_SECRET_KEY appears to be a default value")
```

### Token Storage (Frontend)

**Do:**
- Store access tokens in memory (JavaScript variable)
- Use httpOnly cookies for refresh tokens
- Clear tokens on logout

**Don't:**
- Store tokens in localStorage (XSS vulnerable)
- Store tokens in sessionStorage (XSS vulnerable)
- Include tokens in URLs

### Role-Based Access Control

```python
# Define roles
ROLES = {
    "admin": ["read", "write", "delete", "admin"],
    "editor": ["read", "write"],
    "viewer": ["read"],
}

# Protect endpoints
@router.delete("/api/personas/{id}")
@require_role(["admin"])
async def delete_persona(id: str, current_user: User = Depends(get_current_user)):
    # Only admins can delete
    pass
```

---

## Secrets Management

### Environment Variables

**Required secrets:**
- `JWT_SECRET_KEY` - JWT signing key
- `GEMINI_API_KEY` - Gemini API key
- `DATABASE_ENCRYPTION_KEY` - If using encrypted DB

### Secret Rotation

```bash
# Generate new JWT secret
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Rotation procedure:
# 1. Generate new secret
# 2. Update in secrets manager / environment
# 3. Restart services (existing tokens will be invalidated)
# 4. Monitor for authentication errors
```

### Secrets Scanning

Add to CI/CD pipeline:

```yaml
# .github/workflows/security.yml
- name: Scan for secrets
  uses: trufflesecurity/trufflehog@main
  with:
    path: ./
    base: main
    head: HEAD
```

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Check for potential secrets
if git diff --cached --name-only | xargs grep -l -E "(api[_-]?key|password|secret|token)" 2>/dev/null; then
    echo "WARNING: Potential secrets detected in staged files"
    echo "Please verify no actual secrets are being committed"
    # Uncomment to block commit:
    # exit 1
fi
```

---

## Network Security

### HTTPS Configuration

```nginx
# Force HTTPS
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    # Modern TLS only
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;

    # HSTS
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
}
```

### Rate Limiting

```nginx
# Nginx rate limiting
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=auth:10m rate=5r/m;

location /api/ {
    limit_req zone=api burst=20 nodelay;
}

location /api/auth/ {
    limit_req zone=auth burst=5 nodelay;
}
```

### Firewall Rules

```bash
# Only allow necessary ports
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp    # SSH
ufw allow 80/tcp    # HTTP
ufw allow 443/tcp   # HTTPS
ufw enable
```

---

## Input Validation

### Request Validation

```python
from pydantic import BaseModel, validator, constr
from typing import Optional
import re

class PersonaCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    archetype: str
    voice: Optional[str]
    color: Optional[str]

    @validator('name')
    def name_alphanumeric(cls, v):
        if not re.match(r'^[\w\s-]+$', v):
            raise ValueError('Name must be alphanumeric')
        return v

    @validator('color')
    def color_is_hex(cls, v):
        if v and not re.match(r'^#[0-9A-Fa-f]{6}$', v):
            raise ValueError('Color must be valid hex code')
        return v

    @validator('archetype')
    def archetype_allowed(cls, v):
        allowed = ['Storyteller', 'Educator', 'Coach', 'Artist', 'Mentor']
        if v not in allowed:
            raise ValueError(f'Archetype must be one of: {allowed}')
        return v
```

### SQL Injection Prevention

```python
# ALWAYS use parameterized queries
# GOOD
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# BAD - NEVER DO THIS
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

### File Upload Security

```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def validate_upload(file):
    # Check extension
    ext = file.filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError("File type not allowed")

    # Check file size
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    if size > MAX_FILE_SIZE:
        raise ValueError("File too large")

    # Verify file content matches extension
    import imghdr
    if imghdr.what(file) not in ALLOWED_EXTENSIONS:
        raise ValueError("File content does not match extension")
```

---

## Security Headers

### Recommended Headers

```python
# FastAPI middleware
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        # Prevent MIME type sniffing
        response.headers["X-Content-Type-Options"] = "nosniff"

        # Prevent clickjacking
        response.headers["X-Frame-Options"] = "DENY"

        # XSS protection
        response.headers["X-XSS-Protection"] = "1; mode=block"

        # Referrer policy
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

        # Content Security Policy
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: https:; "
            "font-src 'self'; "
            "connect-src 'self' https://api.example.com"
        )

        # HSTS (only on HTTPS)
        if request.url.scheme == "https":
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains"
            )

        # Permissions Policy
        response.headers["Permissions-Policy"] = (
            "geolocation=(), microphone=(), camera=()"
        )

        return response

app.add_middleware(SecurityHeadersMiddleware)
```

---

## Logging & Auditing

### Security Event Logging

```python
import logging
from datetime import datetime

security_logger = logging.getLogger("security")

def log_security_event(event_type: str, user_id: str, details: dict):
    security_logger.info({
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "user_id": user_id,
        "details": details,
        "ip_address": get_client_ip(),
    })

# Log authentication events
log_security_event("LOGIN_SUCCESS", user.id, {"method": "password"})
log_security_event("LOGIN_FAILURE", email, {"reason": "invalid_password"})
log_security_event("PASSWORD_RESET", user.id, {})
log_security_event("PERMISSION_DENIED", user.id, {"resource": "/admin"})
```

### Audit Trail

Track all sensitive operations:
- User creation/deletion
- Permission changes
- Configuration changes
- Data exports
- API key generation

---

## Dependency Security

### Regular Audits

```bash
# Python
pip-audit
safety check

# JavaScript
npm audit
npm audit fix

# Docker
docker scan jan-studio:latest
```

### Automated Updates

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10

  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
```

---

## Incident Response

### Security Incident Levels

| Level | Description | Response Time | Example |
|-------|-------------|---------------|---------|
| P1 | Active breach | Immediate | Data exfiltration detected |
| P2 | Vulnerability exploited | 1 hour | Unauthorized access |
| P3 | Vulnerability found | 24 hours | SQL injection possible |
| P4 | Security improvement | 1 week | Missing header |

### Incident Response Procedure

1. **Detect & Confirm**
   - Verify the security incident
   - Assess scope and impact
   - Document initial findings

2. **Contain**
   - Isolate affected systems
   - Block malicious IPs
   - Revoke compromised credentials

3. **Eradicate**
   - Patch vulnerabilities
   - Remove malicious code
   - Update affected credentials

4. **Recover**
   - Restore from clean backups
   - Verify system integrity
   - Resume normal operations

5. **Post-Incident**
   - Document timeline
   - Root cause analysis
   - Update procedures

### Emergency Contacts

| Role | Contact |
|------|---------|
| Security Lead | TBD |
| Engineering Lead | TBD |
| Legal/Compliance | TBD |

---

## Security Testing

### OWASP Top 10 Checklist

- [ ] A01:2021 – Broken Access Control
- [ ] A02:2021 – Cryptographic Failures
- [ ] A03:2021 – Injection
- [ ] A04:2021 – Insecure Design
- [ ] A05:2021 – Security Misconfiguration
- [ ] A06:2021 – Vulnerable Components
- [ ] A07:2021 – Authentication Failures
- [ ] A08:2021 – Software and Data Integrity Failures
- [ ] A09:2021 – Security Logging and Monitoring Failures
- [ ] A10:2021 – Server-Side Request Forgery

### Penetration Testing

Schedule regular security assessments:
- Internal security review: Quarterly
- External penetration test: Annually
- Bug bounty program: Consider for production

---

**Last Updated:** 2026-01-25
**Version:** 1.0.0
