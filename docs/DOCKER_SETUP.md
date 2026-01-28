# Docker Setup Guide

**Complete guide for running JAN Studio with Docker.**

---

## Quick Start

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop
docker-compose down
```

---

## Environment Variables

### Required Variables

None required for basic operation. All have defaults.

### Optional Variables

#### SMTP (Email Campaigns)

```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

#### AI APIs (Optional)

```bash
ANTHROPIC_API_KEY=your-anthropic-key
GEMINI_API_KEY=your-gemini-key
```

#### CORS Configuration

```bash
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001,https://yourdomain.com
```

#### Logging

```bash
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
LOG_FORMAT=json  # json or text
```

---

## Docker Compose Configuration

### Services

- **backend**: FastAPI application server

### Volumes

- `./data:/app/data`: Application data
- `./SIYEM/data:/app/SIYEM/data`: SIYEM service data
- `./logs:/app/logs`: Application logs

### Health Checks

- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3
- **Start Period**: 40 seconds

---

## Production Deployment

### Environment File

Create `.env` file:

```bash
# .env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password
ANTHROPIC_API_KEY=your-key
GEMINI_API_KEY=your-key
LOG_LEVEL=INFO
ALLOWED_ORIGINS=https://yourdomain.com
```

### Run with Environment File

```bash
docker-compose --env-file .env up -d
```

### Security Best Practices

1. **Never commit `.env` file** to version control
2. **Use secrets management** in production (Docker secrets, Kubernetes secrets)
3. **Rotate API keys** regularly
4. **Use HTTPS** in production
5. **Restrict CORS** to your domains only

---

## Multi-Stage Build

The Dockerfile uses multi-stage build:

1. **Builder stage**: Compiles dependencies
2. **Production stage**: Minimal runtime image

**Benefits:**
- Smaller final image
- Faster builds (cached layers)
- Production-optimized

---

## Health Checks

### Container Health Check

Docker health check runs every 30 seconds:
- Checks `/health` endpoint
- Marks container as unhealthy if fails 3 times

### Manual Health Check

```bash
# Check container health
docker ps

# Check health endpoint
curl http://localhost:8000/health
```

---

## Logging

### View Logs

```bash
# All logs
docker-compose logs

# Follow logs
docker-compose logs -f backend

# Last 100 lines
docker-compose logs --tail=100 backend
```

### Log Configuration

Logs are stored in:
- Container: `/app/logs`
- Host: `./logs` (mounted volume)

**Log Rotation:**
- Max size: 10MB per file
- Max files: 3
- Format: JSON (structured logging)

---

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs backend

# Check health
docker-compose ps

# Restart
docker-compose restart backend
```

### Database Issues

```bash
# Database files are in ./data
# If corrupted, delete and restart:
rm -rf ./data/*.db
docker-compose restart backend
```

### Port Already in Use

```bash
# Change port in docker-compose.yml:
ports:
  - "8001:8000"  # Use 8001 instead of 8000
```

### Permission Issues

```bash
# Fix data directory permissions
sudo chown -R $USER:$USER ./data
sudo chown -R $USER:$USER ./logs
```

---

## Development vs Production

### Development

```bash
# Use docker-compose.yml (default)
docker-compose up
```

### Production

```bash
# Use production overrides
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

**Production Considerations:**
- Use reverse proxy (nginx, Traefik)
- Enable HTTPS
- Set up monitoring
- Configure backups
- Use secrets management

---

## Scaling

### Horizontal Scaling

```bash
# Scale backend service
docker-compose up -d --scale backend=3
```

**Note:** SQLite doesn't support concurrent writes. For scaling, migrate to PostgreSQL.

### Database Migration

For production scaling, consider:
- PostgreSQL instead of SQLite
- Redis for caching
- Message queue for async tasks

---

## Backup and Recovery

### Backup Data

```bash
# Backup database files
tar -czf backup-$(date +%Y%m%d).tar.gz ./data
```

### Restore Data

```bash
# Stop services
docker-compose down

# Restore backup
tar -xzf backup-YYYYMMDD.tar.gz

# Start services
docker-compose up -d
```

---

## Monitoring

### Container Metrics

```bash
# Container stats
docker stats jan-studio-backend

# Resource usage
docker-compose top
```

### Application Metrics

- Health endpoint: `/health`
- Metrics endpoint: `/metrics` (if Prometheus enabled)
- API docs: `/docs`

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**

**Docker serves deployment. Transparency serves trust. The Laws guide all.**
