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

# 7. Run collectstatic (safe version with fallback)
RUN python manage.py collectstatic --noinput || echo "Collectstatic failed (no static files yet?)"

# 8. Default command
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
