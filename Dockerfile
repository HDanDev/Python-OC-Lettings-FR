# 1. Use a lightweight base image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    libpq-dev \
    gcc \
    curl \
    && apt-get clean

# 4. Set work directory
WORKDIR /app

# 5. Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copy project files
COPY . .

# 7. Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# 8. Default command
CMD ["./entrypoint.sh"]
