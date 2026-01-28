# JAN Studio

**A comprehensive creative identity and content management system built on the Book of Racon (40 Laws) philosophy.**

---

## Overview

JAN Studio is a markdown-based creative identity system that enables:
- **Entity Personas**: Create and manage multiple creative personas
- **Oracle SIYEM**: Transparent RNG engine with 40 Laws interpretation
- **Campaign Automation**: Email integration, social media scheduling, response tracking
- **Content Generation**: AI-powered content creation with Shell/Seed language separation
- **Open Source**: Clean architecture, Docker support, comprehensive documentation

---

## Philosophy

**DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE**
**Spiritual Alignment Over Mechanical Productivity**

**THE FOUNDATION:**
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

**THE MISSION:**
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

---

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)
- API Keys (optional, for AI features):
  - Anthropic API Key (for Claude)
  - Google Gemini API Key (for Gemini)
  - SMTP credentials (for email campaigns)

### Installation

#### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/JEANMORPHIUS/JAN.git
cd JAN

# Build and run
docker-compose up -d

# Check logs
docker-compose logs -f backend
```

#### Option 2: Local Development

```bash
# Clone repository (update URL when GitHub repo is created)
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd JAN

# Install dependencies
cd jan-studio/backend
pip install -r requirements.txt

# Set environment variables
export PYTHONPATH=/path/to/JAN
export ANTHROPIC_API_KEY=your-key
export GEMINI_API_KEY=your-key

# Run server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Access

- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Root**: http://localhost:8000/

---

## Core Features

### 1. Oracle SIYEM Integration

Transparent RNG engine with 40 Laws interpretation and anti-addiction metrics.

**API Endpoints:**
- `POST /api/oracle-siyem/cast` - Cast Oracle for creative guidance
- `GET /api/oracle-siyem/session` - Get user session metrics
- `POST /api/oracle-siyem/record-output` - Record creative output
- `GET /api/oracle-siyem/metrics` - Get anti-addiction metrics

**Features:**
- Transparent seed generation (user can verify)
- Hexagram calculation (I Ching binary)
- Law mapping (1-40 from Book of Racon)
- Context-specific Law interpretation
- Anti-addiction success metrics (success = create and leave)

### 2. Campaign Automation

Email integration, social media scheduling, and response tracking.

**API Endpoints:**
- `POST /api/campaign/contacts` - Add contact
- `POST /api/campaign/contacts/import` - Import contacts from CSV
- `POST /api/campaign/email/create` - Create email campaign
- `POST /api/campaign/email/send` - Send email campaign
- `POST /api/campaign/social/create` - Create social media post
- `POST /api/campaign/social/export` - Export to scheduler (Later, Metricool, Publer, Buffer)
- `POST /api/campaign/responses` - Record response
- `GET /api/campaign/analytics/{campaign_id}` - Get campaign analytics

**Features:**
- Contact management with categories and tags
- Email campaign creation and sending
- Social media post scheduling
- Multi-scheduler export (Later.com, Metricool, Publer, Buffer)
- Response tracking and analytics

### 3. JAN Persona Templates

Create and manage creative personas with Oracle mode support.

**Template Structure:**
```
persona-name/
├── profile.md              # Entity identity and purpose
├── creative_rules.md        # Creative guidelines
└── prompt_templates/       # Reusable prompt templates
    ├── oracle_guided_creation_template.md
    ├── oracle_law_interpretation_template.md
    └── oracle_transparent_process_template.md
```

**Oracle Mode:**
- Integrates with Oracle SIYEM for Law-guided creation
- Transparent creative process
- Anti-addiction creative practice
- Success metrics tracking

---

## Architecture

### Directory Structure

```
JAN/
├── jan-studio/
│   ├── backend/           # FastAPI backend
│   │   ├── main.py        # Main application
│   │   ├── oracle_siyem_api.py
│   │   └── campaign_automation_api.py
│   └── frontend/          # React/Next.js frontend
├── SIYEM/
│   └── services/          # Core services
│       ├── oracle_siyem_integration.py
│       └── campaign_automation.py
├── Siyem.org/             # JAN entity profiles
│   └── oracle_mode/       # Oracle mode persona
├── data/                  # Data storage
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
└── README.md             # This file
```

### Key Components

1. **Oracle SIYEM**: Transparent RNG + 40 Laws + Anti-Addiction
2. **Campaign Automation**: Email + Social Media + Analytics
3. **JAN Personas**: Markdown-based creative identity system
4. **Shell/Seed Translation**: Public/Internal language separation

---

## API Documentation

Full API documentation available at `/docs` when server is running.

### Key Endpoints

#### Oracle SIYEM
- `POST /api/oracle-siyem/cast` - Cast Oracle
- `GET /api/oracle-siyem/session` - Get session info
- `GET /api/oracle-siyem/metrics` - Get metrics

#### Campaign Automation
- `POST /api/campaign/contacts` - Add contact
- `POST /api/campaign/email/create` - Create campaign
- `POST /api/campaign/social/create` - Create post
- `GET /api/campaign/analytics/{id}` - Get analytics

---

## Configuration

### Environment Variables

```bash
# SMTP (Email)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password

# AI APIs (Optional)
ANTHROPIC_API_KEY=your-key
GEMINI_API_KEY=your-key

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001
```

### Database

Campaign automation uses SQLite by default. Database files are stored in:
- `SIYEM/data/oracle_siyem.db` - Oracle SIYEM database
- `SIYEM/data/campaign_automation.db` - Campaign automation database

---

## Development

### Running Tests

```bash
# Run tests (when available)
pytest tests/
```

### Code Quality

```bash
# Format code
black jan-studio/backend/

# Lint code
flake8 jan-studio/backend/
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Contact & Community

### Get in Touch

- **Email**: [info@siyem.org](mailto:info@siyem.org)
- **Discord**: [Join our Discord](https://discord.gg/QmJmeRrf) - "The Table" server
- **GitHub Issues**: [Open an issue](https://github.com/JEANMORPHIUS/JAN/issues)
- **GitHub Discussions**: [Join discussions](https://github.com/JEANMORPHIUS/JAN/discussions)

---

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Join Discord for real-time chat
- Check documentation at `/docs`
- Review code comments for implementation details

---

## Acknowledgments

Built with:
- FastAPI
- Python 3.11+
- Docker
- SQLite
- And the 40 Laws of Racon

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**

**THE TRUTH:**
**WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.**
**THE REST IS UP TO BABA X.**
