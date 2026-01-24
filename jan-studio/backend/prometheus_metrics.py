"""
Prometheus Metrics for JAN Studio API
Production monitoring and observability

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import Response
import time

# Request metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_DURATION = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0]
)

# Active connections
ACTIVE_CONNECTIONS = Gauge(
    'http_active_connections',
    'Number of active HTTP connections'
)

# Oracle system metrics
ORACLE_CASTS_TOTAL = Counter(
    'oracle_casts_total',
    'Total oracle casts',
    ['oracle_type']
)

ORACLE_CAST_DURATION = Histogram(
    'oracle_cast_duration_seconds',
    'Oracle cast duration in seconds',
    ['oracle_type'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

# System metrics
SYSTEM_CPU_PERCENT = Gauge(
    'system_cpu_percent',
    'CPU usage percentage'
)

SYSTEM_MEMORY_PERCENT = Gauge(
    'system_memory_percent',
    'Memory usage percentage'
)

SYSTEM_MEMORY_AVAILABLE = Gauge(
    'system_memory_available_bytes',
    'Available memory in bytes'
)


def record_request_metrics(method: str, endpoint: str, status_code: int, duration: float):
    """Record request metrics for Prometheus."""
    REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=str(status_code)).inc()
    REQUEST_DURATION.labels(method=method, endpoint=endpoint).observe(duration)


def record_oracle_cast(oracle_type: str, duration: float):
    """Record oracle cast metrics."""
    ORACLE_CASTS_TOTAL.labels(oracle_type=oracle_type).inc()
    ORACLE_CAST_DURATION.labels(oracle_type=oracle_type).observe(duration)


def update_system_metrics():
    """Update system resource metrics."""
    try:
        import psutil
        SYSTEM_CPU_PERCENT.set(psutil.cpu_percent(interval=0.1))
        memory = psutil.virtual_memory()
        SYSTEM_MEMORY_PERCENT.set(memory.percent)
        SYSTEM_MEMORY_AVAILABLE.set(memory.available)
    except ImportError:
        pass


def get_metrics_response() -> Response:
    """Get Prometheus metrics response."""
    update_system_metrics()
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )
