# Getting Started with JAN Studio

Welcome to JAN Studio! This guide will help you get up and running quickly.

---

## What is JAN Studio?

JAN Studio is a creative identity and content management system that combines:
- **Oracle SIYEM**: Transparent RNG engine with 40 Laws interpretation
- **Campaign Automation**: Email and social media campaign management
- **JAN Personas**: Markdown-based creative identity system
- **Anti-Addiction Design**: Success metrics that track creation, not consumption

---

## Quick Start (5 Minutes)

### 1. Prerequisites

- **Python 3.11+** (or Docker)
- **API Keys** (optional): Anthropic, Gemini, SMTP credentials

### 2. Installation

#### Option A: Docker (Easiest)

```bash
git clone <repository-url>
cd JAN
docker-compose up -d
```

Visit: http://localhost:8000/docs

#### Option B: Local Development

```bash
git clone <repository-url>
cd JAN/jan-studio/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Your First Oracle Cast

```bash
curl -X POST "http://localhost:8000/api/oracle-siyem/cast" \
  -H "Content-Type: application/json" \
  -d '{
    "user_intent": "I need creative guidance for my writing project",
    "creative_context": "Fiction novel, first chapter"
  }'
```

You'll receive:
- A Law from the Book of Racon (1-40)
- Context-specific interpretation
- Actionable creative prompt
- Full transparency data (seed, hexagram, mapping)

---

## Core Concepts

### Oracle SIYEM

The Oracle uses transparent randomness to guide creative decisions:

1. **Seed Generation**: Your intent + timestamp → SHA-256 hash
2. **Hexagram**: Seed → I Ching hexagram (0-63)
3. **Law Mapping**: Hexagram → Book of Racon Law (1-40)
4. **Interpretation**: Law applied to your creative context

**Key Principle**: Success = Create and Leave (not consume and stay)

### Campaign Automation

Manage contacts, send emails, schedule social posts:

1. **Import Contacts**: CSV import or API
2. **Create Campaign**: Email or social media
3. **Schedule**: Export to Later, Metricool, Publer, Buffer
4. **Track**: Analytics and response tracking

### JAN Personas

Create reusable creative identities:

```
persona-name/
├── profile.md              # Identity and purpose
├── creative_rules.md        # Guidelines
└── prompt_templates/       # Reusable templates
```

---

## Next Steps

1. **Read the Docs**: `/docs` endpoint for full API documentation
2. **Try Examples**: Check `/examples/` for sample personas
3. **Explore Oracle**: Cast multiple times, see how Laws guide you
4. **Create Persona**: Use templates in `/jan-studio/templates/`

---

## Common Tasks

### Cast Oracle for Creative Guidance

```python
import requests

response = requests.post(
    "http://localhost:8000/api/oracle-siyem/cast",
    json={
        "user_intent": "How do I structure my story?",
        "creative_context": "Short story, 2000 words"
    }
)

oracle_result = response.json()
law = oracle_result["oracle_interpretation"]["law"]
print(f"Law {law['law_number']}: {law['law_title']}")
```

### Import Contacts

```python
import requests

with open("contacts.csv", "rb") as f:
    response = requests.post(
        "http://localhost:8000/api/campaign/contacts/import",
        files={"file": f}
    )
```

### Create Social Media Post

```python
import requests

response = requests.post(
    "http://localhost:8000/api/campaign/social/create",
    json={
        "platform": "twitter",
        "content": "The Oracle has spoken. Law 1: The Table Never Lies.",
        "scheduled_at": "2026-01-29T10:00:00"
    }
)
```

---

## Troubleshooting

### Port Already in Use

```bash
# Change port in docker-compose.yml or use:
uvicorn main:app --port 8001
```

### Database Errors

```bash
# Database files are created automatically
# If issues persist, delete and recreate:
rm SIYEM/data/*.db
# Restart server
```

### API Keys Not Working

- Check environment variables are set
- Verify API keys are valid
- Check API quotas/limits

---

## Getting Help

- **Documentation**: `/docs` endpoint
- **Issues**: GitHub Issues
- **Community**: [Specify community channels]

---

**Ready to create? Cast your first Oracle and let the Laws guide you.** 🎯
