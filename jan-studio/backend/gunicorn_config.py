"""
Gunicorn Production Configuration
Production ASGI server for FastAPI

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PRODUCTION DEPLOYMENT:
Gunicorn + Uvicorn workers for production
Never use development server in production
"""

import multiprocessing
import os

# Server socket
bind = os.getenv("GUNICORN_BIND", "0.0.0.0:8000")
backlog = int(os.getenv("GUNICORN_BACKLOG", "2048"))

# Worker processes
# Formula: (CPU_COUNT * 2) + 1
workers = int(os.getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1))
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = int(os.getenv("GUNICORN_WORKER_CONNECTIONS", "1000"))
timeout = int(os.getenv("GUNICORN_TIMEOUT", "120"))
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", "5"))

# Restart workers after this many requests (prevent memory leaks)
max_requests = int(os.getenv("GUNICORN_MAX_REQUESTS", "1000"))
max_requests_jitter = int(os.getenv("GUNICORN_MAX_REQUESTS_JITTER", "50"))

# Logging
accesslog = os.getenv("GUNICORN_ACCESS_LOG", "-")  # stdout
errorlog = os.getenv("GUNICORN_ERROR_LOG", "-")  # stderr
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "jan-studio-api"

# Server mechanics
daemon = False
pidfile = os.getenv("GUNICORN_PIDFILE", None)
umask = 0
user = os.getenv("GUNICORN_USER", None)
group = os.getenv("GUNICORN_GROUP", None)
tmp_upload_dir = None

# SSL (if terminating at Gunicorn, otherwise use Nginx)
keyfile = os.getenv("GUNICORN_KEYFILE", None)
certfile = os.getenv("GUNICORN_CERTFILE", None)

# Graceful timeout for worker shutdown
graceful_timeout = int(os.getenv("GUNICORN_GRACEFUL_TIMEOUT", "30"))

# Preload app (faster worker spawn, but uses more memory)
preload_app = os.getenv("GUNICORN_PRELOAD", "false").lower() == "true"

# Worker tmp directory
worker_tmp_dir = os.getenv("GUNICORN_WORKER_TMP_DIR", "/dev/shm")

def on_starting(server):
    """Called just before the master process is initialized."""
    server.log.info("Starting JAN Studio API - Production Server")
    server.log.info(f"Workers: {workers}, Worker Class: {worker_class}")
    server.log.info("THE MISSION: STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS")

def on_reload(server):
    """Called to recycle workers during a reload via SIGHUP."""
    server.log.info("Reloading workers...")

def worker_int(worker):
    """Called when a worker receives INT or QUIT signal."""
    worker.log.info("Worker received INT/QUIT signal")

def pre_fork(server, worker):
    """Called just before a worker is forked."""
    pass

def post_fork(server, worker):
    """Called just after a worker has been forked."""
    server.log.info(f"Worker spawned (pid: {worker.pid})")

def post_worker_init(worker):
    """Called just after a worker has initialized the application."""
    worker.log.info("Worker initialized")

def worker_abort(worker):
    """Called when a worker times out."""
    worker.log.warning("Worker timed out")

def on_exit(server):
    """Called just before exiting Gunicorn."""
    server.log.info("Shutting down JAN Studio API - Production Server")
