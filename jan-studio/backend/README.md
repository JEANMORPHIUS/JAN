# JAN Studio Backend

This directory should be a symlink to your existing SIYEM FastAPI server.

## Setup

### Create Symlink

**Windows (PowerShell as Administrator):**
```powershell
New-Item -ItemType SymbolicLink -Path "S:\JAN\jan-studio\backend" -Target "S:\SIYEM\07_AUTOMATION_AI"
```

**Linux/Mac:**
```bash
ln -s /path/to/SIYEM/07_AUTOMATION_AI backend
```

## API Endpoints Required

The frontend expects these endpoints:

- `GET /api/jan/personas` - List all personas
- `POST /api/jan/personas` - Create new persona
- `GET /api/jan/personas/{name}/files` - List persona files
- `GET /api/jan/personas/{name}/files/{filename}` - Get file content
- `PUT /api/jan/personas/{name}/files/{filename}` - Save file content
- `DELETE /api/jan/personas/{name}` - Delete persona

## Implementation

Add these endpoints to your SIYEM FastAPI server in:
`S:\SIYEM\07_AUTOMATION_AI\api\jan_studio.py`

See `jan-studio-api-example.py` for reference implementation.

