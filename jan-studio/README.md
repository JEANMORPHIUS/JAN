# JAN Studio

**Professional web interface for creating and managing JAN personas.**

[![Status](https://img.shields.io/badge/status-beta-yellow)]()
[![Version](https://img.shields.io/badge/version-1.0.0-blue)]()

---

## What is JAN Studio?

JAN Studio is a full-stack web application for creating and managing **JAN personas** — markdown-based creative identity systems for AI personalities, creative workflows, and content generation.

**No AI API keys required** — Works standalone. API keys only needed for AI generation features.

---

## Quick Start

```bash
# 1. Setup
cd S:/JAN/jan-studio
cp .env.example .env

# 2. Backend
cd backend
pip install -r requirements.txt
python setup_jan_structure.py
python main.py

# 3. Frontend (new terminal)
cd ../frontend
npm install
npm run dev

# 4. Open browser → http://localhost:3000
```

**See [QUICKSTART.md](QUICKSTART.md) for detailed guide.**

---

## Features

- ✅ **Persona Management** - Create, edit, delete personas
- ✅ **Template System** - Save and reuse persona templates
- ✅ **JAN Compatible** - Full compliance with JAN format
- ✅ **Cross-Platform** - Windows, Mac, Linux
- ✅ **Docker Ready** - Deploy with Docker Compose
- ✅ **API Access** - RESTful API for automation

---

## Installation

**Detailed instructions:** [INSTALL.md](INSTALL.md)

### Prerequisites
- Python 3.8+
- Node.js 18+
- Optional: Docker

### Quick Install

```bash
# Backend
cd backend && pip install -r requirements.txt

# Frontend
cd frontend && npm install
```

---

## Documentation

- **[INSTALL.md](INSTALL.md)** - Complete installation guide
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute quick start
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues
- **[API Docs](http://localhost:8000/docs)** - Interactive API reference

---

## Tech Stack

- **Backend:** FastAPI (Python), SQLite
- **Frontend:** Next.js 14 (React/TypeScript)
- **Storage:** Local filesystem (markdown)
- **Deploy:** Docker Compose

---

## Usage

### Create Persona (UI)
1. Open http://localhost:3000
2. Click "Create New Persona"
3. Edit profile and rules

### Create Persona (API)
```bash
curl -X POST http://localhost:8000/api/jan/personas \
  -H "Content-Type: application/json" \
  -d '{"name":"my-persona"}'
```

---

## Docker

```bash
cd S:/JAN
docker-compose up -d
```

**Services:**
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

---

## JAN Integration

Works with existing JAN directories:
```env
JAN_ROOT=S:/JAN
```

All personas in `JAN_ROOT/Siyem.org/` appear automatically.

---

## Troubleshooting

**See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)**

Quick fixes:
```bash
# Backend issues
pip install -r requirements.txt

# Frontend issues
rm -rf node_modules && npm install

# Check health
curl http://localhost:8000/health
```

---

## Status

**Current:** Beta (Week 2 Testing)
- ✅ Core Features: Stable
- ✅ Templates: Stable
- ✅ Docker: Stable
- ⚠️ AI Generation: Placeholder

---

**Version:** 1.0.0 | **Updated:** 2026-01-13 | **[Get Started →](QUICKSTART.md)**
