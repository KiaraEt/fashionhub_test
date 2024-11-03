import subprocess
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ENV = os.getenv('ENV', 'local')  # Default to local if not set
BASE_URL = os.getenv('BASE_URL', 'http://localhost:4000/fashionhub')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set the results directory
results_dir = 'results'

# Ensure the results directory exists
if not os.path.exists(results_dir):
    os.makedirs(results_dir)


def run_tests():
    """Run Playwright tests and generate an HTML report."""
    logger.info("Starting Playwright tests...")

    # The command can be modified based on running test needed
    command = f"pytest -s --html={results_dir}/report.html --self-contained-html"
    # logger.info("command:", command)

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        logger.info("Tests completed successfully.")
        logger.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logger.error("An error occurred while running tests.")
        # Enhanced logging for error details
        logger.error("STDOUT: %s", e.stdout)
        logger.error("STDERR: %s", e.stderr)


if __name__ == "__main__":
    if ENV == 'local':
        logger.info("Running tests in local environment with BASE_URL: %s", BASE_URL)
    elif ENV == 'development':
        logger.info("Running tests in development environment with BASE_URL: %s", BASE_URL)
    elif ENV == 'staging':
        logger.info("Running tests in staging environment with BASE_URL: %s", BASE_URL)
    elif ENV == 'production':
        logger.info("Running tests in production environment with BASE_URL: %s", BASE_URL)
    else:
        logger.warning("Unknown environment. Defaulting to local.")

    run_tests()