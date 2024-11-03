FROM python:3.12.5-slim

WORKDIR /app

COPY . .
COPY requirements.txt .
COPY .env ./

RUN apt-get update && apt-get install build-essential -y
#RUN apt-get install -y curl
#RUN apt-get install nodejs npm -y


RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN pip install playwright
RUN playwright install

EXPOSE 8000

## Run the main.py script
CMD ["python", "main.py"]

## Set the ENV variable when you run the container using the -e flag.
# docker run -e ENV=development -p 8000:8000 your_image_name