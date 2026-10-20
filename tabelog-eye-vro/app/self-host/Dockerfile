# syntax=docker/dockerfile:1
FROM python:3.11-slim

LABEL maintainer="Tabelog·Eye Team"
LABEL description="Tabelog·Eye + VRO Autonomous Booking & De-Biasing Service (Zero-Dependency Node)"

# Security: Run as non-root user
RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -m -s /bin/bash appuser

WORKDIR /app

# Create data directory for SQLite taste asset vault
RUN mkdir -p /app/data && chown -R appuser:appuser /app

COPY --chown=appuser:appuser server.py /app/server.py
RUN chmod +x /app/server.py

USER appuser

ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    HOST=0.0.0.0 \
    VAULT_DB_PATH=/app/data/taste_vault.db \
    DEFAULT_MONTHLY_BUDGET_CAP=100.00 \
    DEVICE_SALT=tabelog-eye-vro-local-salt-2026 \
    ALLOW_CORS=true

EXPOSE 8080

VOLUME ["/app/data"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health', timeout=4)" || exit 1

ENTRYPOINT ["python", "-u", "server.py"]
