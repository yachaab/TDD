# --- Stage 1: build environment ---
FROM python:3.13.3-alpine AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install build tools and dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    netcat-openbsd \
    && pip install --upgrade pip

# Create working directory
WORKDIR /usr/src/app

# Copy requirements and build wheels
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels

# --- Stage 2: production environment ---
FROM python:3.13.3-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install only runtime dependencies
RUN apk add --no-cache \
    libpq \
    netcat-openbsd

# Create working directory
WORKDIR /usr/src/app

# Copy built wheels and install
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

# Copy the rest of your code
COPY . .

# Ensure entrypoint is executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

