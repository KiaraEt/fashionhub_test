# Fashionhub Test Automation

This project is an automated testing suite for the FashionHub e-commerce application. It utilizes Playwright and Python to ensure the reliability and functionality of the web application across different environments (local, staging, and production). The suite includes tests for critical features such as user authentication, page accessibility, and API responses.
## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Docker Integration](#docker-integration)

## Prerequisites

Before running this project, make sure the following tools and dependencies are installed and set up:


- Python 3.x
- Docker
- Jenkins (if applicable)
- Other requirements: Playwright, Playwright,..

Ensure that all the requirements are installed along with the necessary browsers. This can be done via the requirements.txt file.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
2. Set up a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install dependencies
   ```bash
   pip install -r requirements.txt
## Running Tests
To run the automated tests in this project, ensure you have followed the installation steps and set up your environment. Use the following commands based on your requirements:

1. Run All Tests: To execute all tests in the tests directory, use the following command:
   ```bash
   pytest
2. Run Specific Test Files: If you want to run a specific test file, specify the path to the test file like this:
   ```bash
   pytest tests/test_github_requests.py
3. Run Tests with Markers: You can run tests that are marked with a specific marker (e.g., api, login) using the -m option. For example, to run only tests marked as login, use:
   ```bash
   pytest -m login
4. Generate a Test Report: To create a test report in a specific format (like HTML), you can use the --html option (requires pytest-html to be installed). Here’s an example command to generate an HTML report:
   ```bash
   pytest --html=results/report.html --self-contained-html
5. Using Environment Variables: If your tests rely on environment-specific configurations (like URLs or credentials), ensure to set the necessary environment variables before running the tests. You can use a .env file in conjunction with python-dotenv to load these variables automatically.

## Docker Integration
1. Build the Docker image:
   ```bash
   docker build -t my_playwright_tests .

2. Run the tests in a Docker container:
   ```bash
   docker run --rm -v $(pwd)/results:/app/results playwright-automation

3. Run the test in a Docker container for a specific environment:
   ```bash
   docker run -e ENV=development -p 8000:8000 your_image_name
   
4. 