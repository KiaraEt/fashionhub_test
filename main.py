import subprocess
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ENV = os.getenv('ENV', 'production')  # Set default if not set
BASE_URL = os.getenv('BASE_URL', 'https://pocketaces2.github.io/fashionhub')
RUNNING_IN_DOCKER = os.getenv('RUNNING_IN_DOCKER', 'false').lower() == 'true'

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set the results directory
results_dir = 'results'

# Ensure the results directory exists
if not os.path.exists(results_dir):
    os.makedirs(results_dir)


def run_tests():
    """Run Playwright tests in multiple browsers (if in Docker) and generate HTML reports."""
    logger.info("Starting Playwright tests...")

    # Define the list of browsers for multi-browser testing
    browsers = ["chromium", "firefox", "webkit"] if RUNNING_IN_DOCKER else ["chromium"]

    for browser in browsers:
        # Generate a separate report for each browser
        report_file = f"{results_dir}/report_{browser}.html"
        command = f"pytest -s --html={report_file} --self-contained-html --browser={browser}"

        logger.info(f"Running tests in {browser}...")

        try:
            # Run the tests
            result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            logger.info(f"Tests completed successfully in {browser}.")
            logger.info(result.stdout)
        except subprocess.CalledProcessError as e:
            logger.error(f"An error occurred while running tests in {browser}.")
            logger.error("STDOUT: %s", e.stdout)
            logger.error("STDERR: %s", e.stderr)


if __name__ == "__main__":
    if ENV == 'local':
        logger.info("Running tests in local environment with BASE_URL: %s", BASE_URL)
    elif ENV == 'staging':
        logger.info("Running tests in staging environment with BASE_URL: %s", BASE_URL)
    elif ENV == 'production':
        logger.info("Running tests in production environment with BASE_URL: %s", BASE_URL)
    else:
        logger.warning("Unknown environment. Defaulting to local.")

    run_tests()
