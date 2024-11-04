FROM python:3.12.5-slim

WORKDIR /app

# Copy requirements and .env before copying other files
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


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install Playwright browsers
RUN pip install playwright
RUN playwright install

EXPOSE 8000

## Run the main.py script
CMD ["python", "main.py"]

## Set the ENV variable when you run the container using the -e flag.
# docker run -e ENV=development -p 8000:8000 your_image_name