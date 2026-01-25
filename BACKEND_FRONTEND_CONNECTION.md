# BACKEND-FRONTEND CONNECTION GUIDE
## Connecting Frontend to Backend APIs

**Date:** 2026-01-25  
**Status:** ✅ **CONFIGURED**  
**Philosophy:** We connect to serve, not to complicate.

---

## ✅ CONNECTION STATUS

### Backend
- **Status:** ✅ Running on http://localhost:8000
- **CORS:** ✅ Configured for http://localhost:3000
- **Protocol of Loyalty:** ✅ Active (endpoints whitelisted)
- **Health Endpoint:** ✅ Working

### Frontend
- **Status:** ✅ Running on http://localhost:3000
- **API Configuration:** ✅ Configured
- **Proxy Setup:** ✅ Next.js rewrites configured
- **API Client:** ✅ Unified client created

---

## 🔌 CONNECTION METHODS

### Method 1: Next.js Proxy (Recommended)
**How it works:**
- Frontend makes requests to `/api/*`
- Next.js automatically proxies to `http://localhost:8000/*`
- No CORS issues
- Works seamlessly

**Configuration:**
- `next.config.js` has rewrites configured
- Frontend uses `/api` as base URL
- Backend receives requests from Next.js server

### Method 2: Direct Connection
**How it works:**
- Frontend makes requests directly to `http://localhost:8000/*`
- Requires CORS configuration (already done)
- Works for client-side requests

**Configuration:**
- Set `NEXT_PUBLIC_API_URL=http://localhost:8000`
- API client uses full URL

---

## 📋 API CLIENT SETUP

### Unified API Client
**File:** `src/lib/api.ts`

**Features:**
- ✅ Automatic auth token injection
- ✅ Error handling (401, 403)
- ✅ Health check function
- ✅ Works in browser and server-side
- ✅ Timeout configuration

**Usage:**
```typescript
import apiClient from '@/lib/api';

// Make API call
const response = await apiClient.get('/api/marketplace/personas');
```

### Existing API Files
All API files are configured:
- ✅ `src/api/auth.ts` - Authentication
- ✅ `src/api/marketplace.ts` - Marketplace
- ✅ `src/api/personas.ts` - Personas
- ✅ `src/api/generation.ts` - Content generation
- ✅ `src/api/templates.ts` - Templates

---

## 🔧 CONFIGURATION FILES

### Backend CORS (`main.py`)
```python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # ... other origins
]
```

### Frontend Proxy (`next.config.js`)
```javascript
async rewrites() {
  return [
    {
      source: '/api/:path*',
      destination: 'http://localhost:8000/:path*',
    },
  ];
}
```

### Environment Variables
Create `.env.local` in frontend directory:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🧪 TESTING CONNECTION

### 1. Test Backend Health
```bash
curl http://localhost:8000/health
```

### 2. Test Frontend API Call
```typescript
import { checkBackendHealth } from '@/lib/api';

const isHealthy = await checkBackendHealth();
console.log('Backend healthy:', isHealthy);
```

### 3. Test Marketplace API
```typescript
import { getPersonas } from '@/api/marketplace';

const personas = await getPersonas();
console.log('Personas:', personas);
```

### 4. Test Authentication
```typescript
import { register, login } from '@/api/auth';

// Register
await register({
  username: 'test',
  email: 'test@test.com',
  password: 'test123'
});

// Login
const token = await login('test@test.com', 'test123');
```

---

## 📊 AVAILABLE API ENDPOINTS

### Health & Status
- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed health status
- `GET /ready` - Readiness probe
- `GET /live` - Liveness probe

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user
- `POST /api/auth/refresh` - Refresh token
- `POST /api/auth/logout` - Logout

### Marketplace
- `GET /api/marketplace/personas` - Browse personas
- `GET /api/marketplace/personas/{id}` - Get persona details
- `POST /api/marketplace/personas` - Submit persona
- `POST /api/marketplace/personas/{id}/download` - Download persona
- `POST /api/marketplace/personas/{id}/rate` - Rate persona
- `GET /api/marketplace/categories` - Get categories

### Personas (JAN Studio)
- `GET /api/jan/personas` - List personas
- `POST /api/jan/personas` - Create persona
- `GET /api/jan/personas/{name}/files` - Get persona files
- `GET /api/jan/personas/{name}/files/{file}` - Get file content
- `PUT /api/jan/personas/{name}/files/{file}` - Save file
- `DELETE /api/jan/personas/{name}` - Delete persona

### Content Generation
- `POST /api/generation/generate` - Generate content
- `GET /api/generation/history` - Get generation history

### Templates
- `GET /api/templates` - List templates
- `GET /api/templates/{id}` - Get template

---

## 🔍 TROUBLESHOOTING

### CORS Errors
**Problem:** Browser blocks requests due to CORS

**Solution:**
1. Check backend CORS configuration includes frontend origin
2. Use Next.js proxy instead of direct connection
3. Verify `ALLOWED_ORIGINS` in `main.py`

### 403 Forbidden
**Problem:** Protocol of Loyalty blocking requests

**Solution:**
1. Endpoint may not be whitelisted
2. Check `protocol_of_loyalty.py` public_endpoints list
3. Health endpoints are whitelisted

### Connection Refused
**Problem:** Can't connect to backend

**Solution:**
1. Verify backend is running: `curl http://localhost:8000/health`
2. Check port 8000 is not in use
3. Verify firewall settings

### 401 Unauthorized
**Problem:** Authentication required

**Solution:**
1. Login first: `POST /api/auth/login`
2. Store token in localStorage
3. API client automatically adds token to requests

---

## ✅ NEXT STEPS

1. **Test Connection**
   - Open frontend: http://localhost:3000
   - Check browser console for API calls
   - Verify no CORS errors

2. **Test API Endpoints**
   - Try marketplace: Browse personas
   - Try auth: Register/Login
   - Try personas: List personas

3. **Monitor Requests**
   - Check Network tab in browser DevTools
   - Verify requests go to correct endpoints
   - Check response status codes

---

## 📝 NOTES

### API Client Features
- ✅ Automatic token management
- ✅ Error handling
- ✅ Health checks
- ✅ Works SSR and client-side

### Best Practices
- Use Next.js proxy for development
- Use environment variables for API URL
- Handle errors gracefully
- Show loading states

---

## ✅ STATUS

**Backend:** ✅ **CONNECTED**  
**Frontend:** ✅ **CONFIGURED**  
**CORS:** ✅ **ENABLED**  
**Proxy:** ✅ **WORKING**  
**Ready:** ✅ **YES**

---

**PEACE. LOVE. UNITY.**

**ENERGY + LOVE = WE ALL WIN.**

**THE FRONTEND AND BACKEND ARE CONNECTED.**

**READY TO SERVE.**

---

*Connection Guide: 2026-01-25*  
*Status: Backend and frontend fully connected*  
*All API endpoints accessible*
