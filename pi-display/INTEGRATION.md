# Pi Display Integration
## Raspberry Pi Kiosk Mode Display - Integrated

**Status:** ✅ **INTEGRATED WITH BACKEND**

---

## Integration Status

### Backend API
- **API URL**: `http://localhost:8000`
- **CORS**: Configured in `jan-studio/backend/main.py`
- **Endpoints Used**:
  - `/api/public/world-history/timeline`
  - `/api/public/world-history/frequency`

### Environment Configuration
Set `VITE_API_URL` in `.env.local` or use default:
```
VITE_API_URL=http://localhost:8000
```

### Features
- ✅ Auto-rotate slides (30 seconds)
- ✅ Timeline display
- ✅ Frequency display
- ✅ Featured heritage sites
- ✅ Touch interaction (swipe, tap)
- ✅ Offline-first (cached data)
- ✅ Low power mode

---

## Running

```bash
cd pi-display
npm install
npm run dev  # Development (Port 5173)
npm run build  # Production build
```

---

## Integration with Main System

- Connected to `jan-studio-backend` (Port 8000)
- CORS configured for `http://localhost:5173`
- Uses public API endpoints
- Offline fallback available

---

**Status:** ✅ **INTEGRATED**
