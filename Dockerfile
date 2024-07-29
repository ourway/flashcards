# Flask based python application, served by gunicorn, using python3.12
# This is a multi-stage build, the first stage is used to build the application
# and the second stage is used to run the application

# First stage
FROM python:3.12-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1



# Copy the requirements file
COPY requirements.txt .

# Install the dependencies and also supprot for postgres psycopg2 built
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# setup user for non-priviliged access
RUN adduser --disabled-password --gecos '' appuser


# Copy the application code

ENV PYTHONPATH=/app/src

EXPOSE 8000

# Run the 
CMD ["./entrypoint.sh"]
