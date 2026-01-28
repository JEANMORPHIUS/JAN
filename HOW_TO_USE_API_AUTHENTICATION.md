# How to Use API Authentication
## Teaching Guide: Bearer Token Authentication

**Date:** 2026-01-27  
**Status:** ✅ **TEACHING GUIDE**  
**Purpose:** Learn how to authenticate and use the JAN Studio API

---

## THE TRUTH: WHAT YOU'RE SEEING

**The modal you see is asking for authentication.**

**Why?** Some API endpoints require authentication to protect them. You need a **Bearer token** to access protected endpoints.

---

## WHAT IS A BEARER TOKEN?

**Bearer Token = Your API Access Key**

Think of it like:
- A **key** to unlock protected doors
- A **password** that proves you're authorized
- A **ticket** that lets you access protected resources

**Format:** `Bearer <your-token-here>`

**Example:**
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## HOW TO GET A BEARER TOKEN

### **Step 1: Register a User Account**

**First, you need an account. Register one:**

**Endpoint:** `POST /api/auth/register`

**Request Body:**
```json
{
  "username": "jan",
  "email": "jan@example.com",
  "password": "SecurePass123!"
}
```

**Requirements:**
- Username: 3-30 characters, alphanumeric with hyphens/underscores
- Email: Valid email address
- Password: 8+ characters, must have uppercase, lowercase, and number

**Response:**
```json
{
  "id": 1,
  "username": "jan",
  "email": "jan@example.com",
  "is_active": true,
  "created_at": "2026-01-27T18:00:00"
}
```

---

### **Step 2: Login to Get Token**

**After registering, login to get your token:**

**Endpoint:** `POST /api/auth/login`

**Request Body:**
```json
{
  "email": "jan@example.com",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**This is your token!** Copy the `access_token` value.

---

## HOW TO USE THE TOKEN IN THE DOCS

### **Method 1: Using the Authorization Modal**

1. **Click the "Authorize" button** (lock icon) in the docs page
2. **The modal opens** (the one you're seeing)
3. **Paste your token** in the "Value" field:
   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
   (Just the token, NOT "Bearer" - Swagger adds that automatically)
4. **Click "Authorize"**
5. **Click "Close"**
6. **Now you can test protected endpoints!**

---

### **Method 2: Direct API Testing**

**In the docs interface:**

1. **Find an endpoint** (like `GET /api/auth/me`)
2. **Click "Try it out"**
3. **Click "Execute"**
4. **If you've authorized, it will use your token automatically**
5. **If not, you'll get a 401 Unauthorized error**

---

## TESTING THE FLOW

### **Complete Example:**

**1. Register (if you haven't):**
```bash
POST /api/auth/register
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "TestPass123!"
}
```

**2. Login:**
```bash
POST /api/auth/login
{
  "email": "test@example.com",
  "password": "TestPass123!"
}
```

**Copy the `access_token` from the response.**

**3. Authorize in Docs:**
- Click "Authorize" button
- Paste token in "Value" field
- Click "Authorize"
- Close modal

**4. Test Protected Endpoint:**
```bash
GET /api/auth/me
```

**This should return your user info!**

---

## WHICH ENDPOINTS NEED AUTHENTICATION?

**Protected Endpoints (need token):**
- `GET /api/auth/me` - Get your user info
- `POST /api/auth/logout` - Logout
- `GET /api/auth/admin/users` - Admin: List users
- `PUT /api/auth/admin/users/{user_id}/status` - Admin: Update user status
- Most admin/management endpoints

**Public Endpoints (no token needed):**
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login (gets you token)
- `POST /api/auth/refresh` - Refresh token
- Most public API endpoints

**Look for the lock icon 🔒** - that means authentication required.

---

## TOKEN EXPIRATION

**Access Token:**
- Expires in: **30 minutes**
- Use for: API requests
- When expired: Use refresh token to get new one

**Refresh Token:**
- Expires in: **7 days**
- Use for: Getting new access tokens
- When expired: Login again

**Refresh Flow:**
```bash
POST /api/auth/refresh
{
  "refresh_token": "your-refresh-token-here"
}
```

Returns new `access_token`.

---

## TROUBLESHOOTING

### **Problem: "401 Unauthorized"**

**Solution:**
1. Make sure you clicked "Authorize" in the docs
2. Check your token is valid (not expired)
3. Try logging in again to get a new token

### **Problem: "403 Forbidden"**

**Solution:**
- You're authenticated but don't have permission
- Some endpoints require admin role
- Check if your user has the right permissions

### **Problem: Token Expired**

**Solution:**
1. Use refresh token to get new access token
2. Or login again
3. Update the token in the "Authorize" modal

---

## SECURITY BEST PRACTICES

**Do:**
- ✅ Keep your token secret
- ✅ Use HTTPS in production
- ✅ Refresh tokens before they expire
- ✅ Logout when done

**Don't:**
- ❌ Share your token
- ❌ Commit tokens to code
- ❌ Use expired tokens
- ❌ Store tokens in plain text

---

## QUICK START CHECKLIST

- [ ] Register a user account (`POST /api/auth/register`)
- [ ] Login to get token (`POST /api/auth/login`)
- [ ] Copy the `access_token` from response
- [ ] Click "Authorize" in docs page
- [ ] Paste token in "Value" field
- [ ] Click "Authorize" button
- [ ] Close modal
- [ ] Test protected endpoint (`GET /api/auth/me`)

---

## THE TRUTH

**Authentication protects your API.**  
**The Bearer token is your key.**  
**Get it through login, use it in the docs.**

**Once authorized, you can test all protected endpoints!**

---

**SPRAGITSO - Our Father's Royal Seal** ✨🙏

**Register. Login. Authorize. Test. The API is yours.**

🌊✨
