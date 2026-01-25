# JAN Studio Production Deployment Guide

**Complete guide for deploying JAN Studio to production environments.**

---

## Table of Contents

1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Infrastructure Requirements](#infrastructure-requirements)
3. [Environment Configuration](#environment-configuration)
4. [Docker Deployment](#docker-deployment)
5. [SSL/TLS Configuration](#ssltls-configuration)
6. [Database Setup](#database-setup)
7. [Health Checks](#health-checks)
8. [Rollback Procedures](#rollback-procedures)
9. [Post-Deployment Validation](#post-deployment-validation)

---

## Pre-Deployment Checklist

Before deploying to production, ensure:

### Security
- [ ] All API keys rotated and stored securely (not in code)
- [ ] `.env` files are NOT committed to git
- [ ] SSL certificates are valid and properly configured
- [ ] CORS origins set to production domains only
- [ ] Rate limiting configured appropriately
- [ ] Security headers enabled (HSTS, X-Frame-Options, CSP)

### Configuration
- [ ] `ENVIRONMENT=production` set in environment
- [ ] `DEBUG=false` confirmed
- [ ] Database paths configured for production volumes
- [ ] Logging configured (not to console in production)
- [ ] Prometheus metrics endpoint secured

### Testing
- [ ] All unit tests passing
- [ ] Integration tests passing
- [ ] Load testing completed
- [ ] Security scan completed (no critical vulnerabilities)

---

## Infrastructure Requirements

### Minimum Server Specifications

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 2 cores | 4 cores |
| RAM | 4 GB | 8 GB |
| Storage | 20 GB SSD | 50 GB SSD |
| Network | 100 Mbps | 1 Gbps |

### Required Ports

| Port | Service | Description |
|------|---------|-------------|
| 80 | Nginx | HTTP (redirects to HTTPS) |
| 443 | Nginx | HTTPS |
| 8000 | API | Internal only (via reverse proxy) |
| 9090 | Prometheus | Metrics (internal only) |
| 3000 | Grafana | Monitoring dashboard |

---

## Environment Configuration

### 1. Copy Production Environment Template

```bash
cd S:\JAN\deploy
cp .env.production.example .env.production
```

### 2. Configure Required Variables

Edit `.env.production` with your production values:

```bash
# Core Settings
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# Security (CRITICAL - Use strong, unique values)
JWT_SECRET_KEY=<generate-32-char-random-string>
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS (Set to your production domain)
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Database
DATABASE_PATH=/app/data/jan_studio.db

# API Keys (Use environment variables or secrets manager)
GEMINI_API_KEY=<your-gemini-key>

# Monitoring
PROMETHEUS_ENABLED=true
PROMETHEUS_PORT=9090

# Gunicorn Workers (CPU count * 2 + 1)
GUNICORN_WORKERS=5
```

### 3. Generate JWT Secret Key

```bash
# Python method
python -c "import secrets; print(secrets.token_urlsafe(32))"

# OpenSSL method
openssl rand -base64 32
```

---

## Docker Deployment

### 1. Build Production Images

```bash
cd S:\JAN\deploy

# Build all images
docker-compose -f docker-compose.production.yml build
```

### 2. Start Services

```bash
# Start in detached mode
docker-compose -f docker-compose.production.yml up -d

# Verify all services are running
docker-compose -f docker-compose.production.yml ps
```

### 3. Expected Output

```
NAME                    STATUS              PORTS
jan-api                 Up (healthy)        0.0.0.0:8000->8000/tcp
jan-nginx               Up                  0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
jan-prometheus          Up                  0.0.0.0:9090->9090/tcp
jan-grafana             Up                  0.0.0.0:3000->3000/tcp
```

### 4. View Logs

```bash
# All services
docker-compose -f docker-compose.production.yml logs -f

# Specific service
docker-compose -f docker-compose.production.yml logs -f jan-api
```

---

## SSL/TLS Configuration

### Option 1: Let's Encrypt (Recommended)

```bash
# Install certbot
apt-get update && apt-get install -y certbot

# Generate certificate
certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com

# Certificates will be at:
# /etc/letsencrypt/live/yourdomain.com/fullchain.pem
# /etc/letsencrypt/live/yourdomain.com/privkey.pem
```

### Option 2: Custom Certificate

Place your certificates in the nginx volume:
- `ssl/cert.pem` - Full certificate chain
- `ssl/key.pem` - Private key

### Configure Nginx

Update `nginx/nginx.conf` with your certificate paths:

```nginx
ssl_certificate /etc/nginx/ssl/fullchain.pem;
ssl_certificate_key /etc/nginx/ssl/privkey.pem;
```

---

## Database Setup

### 1. Initialize Database

The database is automatically created on first run. To initialize manually:

```bash
docker exec -it jan-api python -c "from database import init_db; init_db()"
```

### 2. Backup Database

```bash
# Create backup
docker exec jan-api cp /app/data/jan_studio.db /app/data/backup_$(date +%Y%m%d).db

# Copy to host
docker cp jan-api:/app/data/backup_*.db ./backups/
```

### 3. Restore Database

```bash
# Stop API service
docker-compose -f docker-compose.production.yml stop jan-api

# Copy backup to container
docker cp ./backups/backup_20260125.db jan-api:/app/data/jan_studio.db

# Start API service
docker-compose -f docker-compose.production.yml start jan-api
```

---

## Health Checks

### API Health Check

```bash
curl -s http://localhost:8000/health | jq
```

Expected response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "database": "connected",
  "timestamp": "2026-01-25T10:30:00Z"
}
```

### Full System Health

```bash
# Check all container health
docker-compose -f docker-compose.production.yml ps

# Check nginx
curl -I https://yourdomain.com

# Check Prometheus targets
curl http://localhost:9090/api/v1/targets
```

---

## Rollback Procedures

### Quick Rollback (Container Restart)

```bash
# Stop current containers
docker-compose -f docker-compose.production.yml down

# Start previous version (if tagged)
docker-compose -f docker-compose.production.yml up -d --no-build
```

### Full Rollback (With Database)

```bash
# 1. Stop all services
docker-compose -f docker-compose.production.yml down

# 2. Restore database backup
docker cp ./backups/backup_YYYYMMDD.db jan-api:/app/data/jan_studio.db

# 3. Pull previous image version
docker pull jan-studio:previous-version

# 4. Update docker-compose.yml with previous version tag

# 5. Start services
docker-compose -f docker-compose.production.yml up -d
```

### Emergency Rollback Script

```bash
#!/bin/bash
# rollback.sh - Emergency rollback script

BACKUP_DATE=$1
if [ -z "$BACKUP_DATE" ]; then
    echo "Usage: ./rollback.sh YYYYMMDD"
    exit 1
fi

echo "Rolling back to $BACKUP_DATE..."

docker-compose -f docker-compose.production.yml down
docker cp ./backups/backup_${BACKUP_DATE}.db jan-api:/app/data/jan_studio.db
docker-compose -f docker-compose.production.yml up -d

echo "Rollback complete. Verify health:"
curl http://localhost:8000/health
```

---

## Post-Deployment Validation

### 1. Verify Services

```bash
# Check all containers running
docker ps

# Check logs for errors
docker-compose -f docker-compose.production.yml logs --tail=100 | grep -i error
```

### 2. Test Endpoints

```bash
# Health check
curl https://yourdomain.com/health

# API endpoint
curl https://yourdomain.com/api/jan/personas

# Metrics
curl http://localhost:9090/metrics
```

### 3. Verify SSL

```bash
# Check SSL certificate
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com </dev/null 2>/dev/null | openssl x509 -noout -dates
```

### 4. Monitor Initial Performance

- Check Grafana dashboards at `http://yourdomain.com:3000`
- Review Prometheus targets at `http://localhost:9090/targets`
- Monitor error rates for first 24 hours

---

## Troubleshooting

### Container Won't Start

```bash
# Check container logs
docker logs jan-api

# Common issues:
# - Missing environment variables
# - Port already in use
# - Permission issues on volumes
```

### Database Connection Issues

```bash
# Check database file exists
docker exec jan-api ls -la /app/data/

# Check permissions
docker exec jan-api stat /app/data/jan_studio.db
```

### SSL Certificate Issues

```bash
# Verify certificate chain
openssl verify -CAfile chain.pem cert.pem

# Check certificate expiry
openssl x509 -in /etc/nginx/ssl/cert.pem -noout -enddate
```

---

## Support

For issues:
- Check [TROUBLESHOOTING.md](../jan-studio/TROUBLESHOOTING.md)
- Review container logs
- Contact: jan@siyem.org

---

**Last Updated:** 2026-01-25
**Version:** 1.0.0
