# JAN Studio Operations Manual

**Runbooks and operational procedures for maintaining JAN Studio in production.**

---

## Table of Contents

1. [Daily Operations](#daily-operations)
2. [Monitoring & Alerting](#monitoring--alerting)
3. [Scaling Procedures](#scaling-procedures)
4. [Backup & Recovery](#backup--recovery)
5. [Incident Response](#incident-response)
6. [Maintenance Windows](#maintenance-windows)
7. [Log Management](#log-management)
8. [Performance Tuning](#performance-tuning)

---

## Daily Operations

### Morning Health Check

Run this checklist every morning:

```bash
#!/bin/bash
# daily_health_check.sh

echo "=== JAN Studio Daily Health Check ==="
echo "Date: $(date)"
echo ""

# 1. Check all containers
echo "1. Container Status:"
docker-compose -f docker-compose.production.yml ps

# 2. Check API health
echo ""
echo "2. API Health:"
curl -s http://localhost:8000/health | jq

# 3. Check disk space
echo ""
echo "3. Disk Space:"
df -h /var/lib/docker

# 4. Check memory usage
echo ""
echo "4. Memory Usage:"
free -h

# 5. Check recent errors
echo ""
echo "5. Recent Errors (last 100 lines):"
docker-compose -f docker-compose.production.yml logs --tail=100 2>&1 | grep -i error | tail -10

echo ""
echo "=== Health Check Complete ==="
```

### Weekly Maintenance Tasks

| Task | Frequency | Command |
|------|-----------|---------|
| Database backup | Weekly (Sunday 2 AM) | `./scripts/backup_database.sh` |
| Log rotation | Weekly | `docker system prune -f` |
| SSL cert check | Weekly | `./scripts/check_ssl.sh` |
| Dependency audit | Weekly | `npm audit` / `pip-audit` |

---

## Monitoring & Alerting

### Prometheus Metrics

Access Prometheus at `http://localhost:9090`

#### Key Metrics to Watch

| Metric | Warning Threshold | Critical Threshold |
|--------|-------------------|-------------------|
| `http_request_duration_seconds` | > 1s (p95) | > 5s (p95) |
| `http_requests_total{status="5xx"}` | > 10/min | > 50/min |
| `process_resident_memory_bytes` | > 1GB | > 2GB |
| `active_connections` | > 100 | > 500 |

#### Sample Alert Rules

Create `prometheus/rules/alerts.yml`:

```yaml
groups:
  - name: jan_studio_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: High error rate detected
          description: Error rate is {{ $value | humanizePercentage }}

      - alert: APILatencyHigh
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: API latency is high
          description: 95th percentile latency is {{ $value }}s

      - alert: HighMemoryUsage
        expr: process_resident_memory_bytes > 1.5e9
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: High memory usage
          description: Memory usage is {{ $value | humanize }}

      - alert: ContainerDown
        expr: up{job="jan-api"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: JAN API container is down
          description: The API container has been down for more than 1 minute
```

### Grafana Dashboards

Access Grafana at `http://localhost:3000`

Default credentials:
- Username: `admin`
- Password: Set in `GRAFANA_ADMIN_PASSWORD` env var

#### Key Dashboards

1. **System Overview** - CPU, memory, disk, network
2. **API Performance** - Request rate, latency, error rate
3. **Database Stats** - Connection pool, query times
4. **Container Health** - Per-container metrics

---

## Scaling Procedures

### Horizontal Scaling (Add Workers)

```bash
# Update GUNICORN_WORKERS in .env.production
# Formula: (2 * CPU_CORES) + 1

# Apply changes
docker-compose -f docker-compose.production.yml up -d --no-deps jan-api
```

### Vertical Scaling (More Resources)

```bash
# Update docker-compose.production.yml
services:
  jan-api:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 4G
        reservations:
          cpus: '2'
          memory: 2G

# Apply changes
docker-compose -f docker-compose.production.yml up -d
```

### Load Balancing (Multiple Instances)

For high availability, deploy multiple API instances behind a load balancer:

```yaml
# docker-compose.production.yml
services:
  jan-api:
    deploy:
      replicas: 3
    # ... rest of config
```

---

## Backup & Recovery

### Automated Backup Script

```bash
#!/bin/bash
# backup_database.sh

BACKUP_DIR="/var/backups/jan-studio"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=30

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
docker exec jan-api sqlite3 /app/data/jan_studio.db ".backup '/tmp/backup.db'"
docker cp jan-api:/tmp/backup.db $BACKUP_DIR/jan_studio_$DATE.db

# Compress
gzip $BACKUP_DIR/jan_studio_$DATE.db

# Clean old backups
find $BACKUP_DIR -name "*.gz" -mtime +$RETENTION_DAYS -delete

echo "Backup completed: $BACKUP_DIR/jan_studio_$DATE.db.gz"
```

### Recovery Procedure

```bash
#!/bin/bash
# restore_database.sh

BACKUP_FILE=$1

if [ -z "$BACKUP_FILE" ]; then
    echo "Usage: ./restore_database.sh <backup_file.db.gz>"
    exit 1
fi

# Stop API
docker-compose -f docker-compose.production.yml stop jan-api

# Decompress if needed
if [[ $BACKUP_FILE == *.gz ]]; then
    gunzip -c $BACKUP_FILE > /tmp/restore.db
    BACKUP_FILE=/tmp/restore.db
fi

# Restore
docker cp $BACKUP_FILE jan-api:/app/data/jan_studio.db

# Start API
docker-compose -f docker-compose.production.yml start jan-api

# Verify
sleep 5
curl http://localhost:8000/health
```

### Backup Verification

Weekly verification of backup integrity:

```bash
#!/bin/bash
# verify_backup.sh

LATEST_BACKUP=$(ls -t /var/backups/jan-studio/*.gz | head -1)

# Decompress to temp
gunzip -c $LATEST_BACKUP > /tmp/verify.db

# Check integrity
sqlite3 /tmp/verify.db "PRAGMA integrity_check;"

# Cleanup
rm /tmp/verify.db

echo "Backup verification complete"
```

---

## Incident Response

### Severity Levels

| Level | Description | Response Time | Example |
|-------|-------------|---------------|---------|
| P1 - Critical | Service down | 15 minutes | API unresponsive |
| P2 - High | Major degradation | 1 hour | > 50% error rate |
| P3 - Medium | Minor degradation | 4 hours | Slow response times |
| P4 - Low | Minor issue | 24 hours | UI bug |

### P1 Response Playbook

```
1. ACKNOWLEDGE (5 min)
   - Confirm alert received
   - Start incident channel
   - Assign incident commander

2. DIAGNOSE (10 min)
   - Check container status: docker-compose ps
   - Check logs: docker-compose logs --tail=100
   - Check resources: docker stats
   - Check external dependencies

3. MITIGATE (ASAP)
   - If container down: docker-compose restart jan-api
   - If resource exhaustion: Scale up or restart
   - If dependency failure: Failover or wait

4. COMMUNICATE
   - Update status page
   - Notify stakeholders
   - Document timeline

5. RESOLVE
   - Confirm service restored
   - Monitor for stability (15 min)
   - Close incident

6. POST-MORTEM (within 48 hours)
   - Root cause analysis
   - Action items
   - Process improvements
```

### Emergency Contacts

| Role | Name | Contact |
|------|------|---------|
| Primary On-Call | TBD | TBD |
| Secondary On-Call | TBD | TBD |
| Engineering Lead | TBD | TBD |

---

## Maintenance Windows

### Scheduled Maintenance

Standard maintenance window: **Sundays 02:00-04:00 UTC**

### Maintenance Procedure

```bash
#!/bin/bash
# maintenance.sh

echo "Starting maintenance window..."

# 1. Enable maintenance mode (return 503 to new requests)
docker exec jan-nginx touch /etc/nginx/maintenance.flag
docker exec jan-nginx nginx -s reload

# 2. Wait for active requests to complete
sleep 30

# 3. Perform maintenance tasks
docker-compose -f docker-compose.production.yml pull
docker-compose -f docker-compose.production.yml up -d

# 4. Health check
sleep 10
if curl -s http://localhost:8000/health | grep -q "healthy"; then
    echo "Health check passed"
else
    echo "HEALTH CHECK FAILED - Rolling back"
    exit 1
fi

# 5. Disable maintenance mode
docker exec jan-nginx rm /etc/nginx/maintenance.flag
docker exec jan-nginx nginx -s reload

echo "Maintenance complete"
```

---

## Log Management

### Log Locations

| Service | Location | Retention |
|---------|----------|-----------|
| API | Docker logs | 7 days |
| Nginx | `/var/log/nginx/` | 30 days |
| Prometheus | Volume | 15 days |

### Log Rotation

```bash
# /etc/logrotate.d/jan-studio
/var/log/jan-studio/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        docker-compose -f /opt/jan-studio/docker-compose.production.yml kill -s USR1 jan-api
    endscript
}
```

### Log Aggregation

For production, consider:
- **Loki** - Grafana's log aggregation
- **ELK Stack** - Elasticsearch, Logstash, Kibana
- **CloudWatch** - If on AWS

---

## Performance Tuning

### Gunicorn Settings

```python
# gunicorn_config.py
import multiprocessing

# Workers
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Connections
worker_connections = 1000
max_requests = 500
max_requests_jitter = 50

# Timeouts
timeout = 30
graceful_timeout = 30
keepalive = 5
```

### Database Optimization

```sql
-- Run periodically to optimize SQLite
PRAGMA optimize;
VACUUM;
ANALYZE;
```

### Nginx Tuning

```nginx
# nginx.conf optimizations
worker_processes auto;
worker_rlimit_nofile 65535;

events {
    worker_connections 4096;
    use epoll;
    multi_accept on;
}

http {
    # Buffering
    client_body_buffer_size 10K;
    client_header_buffer_size 1k;
    client_max_body_size 8m;
    large_client_header_buffers 4 32k;

    # Timeouts
    client_body_timeout 12;
    client_header_timeout 12;
    keepalive_timeout 15;
    send_timeout 10;

    # Gzip
    gzip on;
    gzip_comp_level 5;
    gzip_min_length 256;
    gzip_types application/json text/plain text/css application/javascript;
}
```

---

## Quick Reference Commands

```bash
# View running containers
docker-compose -f docker-compose.production.yml ps

# View logs
docker-compose -f docker-compose.production.yml logs -f

# Restart service
docker-compose -f docker-compose.production.yml restart jan-api

# Stop all
docker-compose -f docker-compose.production.yml down

# Start all
docker-compose -f docker-compose.production.yml up -d

# View resource usage
docker stats

# Enter container shell
docker exec -it jan-api /bin/bash

# Database backup
docker exec jan-api sqlite3 /app/data/jan_studio.db ".backup '/tmp/backup.db'"
```

---

**Last Updated:** 2026-01-25
**Version:** 1.0.0
