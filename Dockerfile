# Use the official slim Python 3.12.5 image
FROM python:3.12.5-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies early to optimize caching
COPY requirements.txt .

# Install system dependencies required for Playwright
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libglib2.0-0 \
        libnss3 \
        libnspr4 \
        libdbus-1-3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libxkbcommon0 \
        libatspi2.0-0 \
        libxcomposite1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
        libpango-1.0-0 \
        libcairo2 \
        libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and required browsers
RUN pip install playwright && playwright install --with-deps

# Copy the rest of the project files
COPY . .

# Set the environment variable to signal running in Docker
ENV RUNNING_IN_DOCKER=true

# Expose port if needed by the application
EXPOSE 8000

# Default command to run the main.py script
CMD ["python", "main.py"]