import os
import requests
import csv
import pytest
from datetime import datetime


@pytest.mark.api
def test_fetch_open_pull_requests():
    repo_url = "https://api.github.com/repos/appwrite/appwrite/pulls"
    try:
        response = requests.get(repo_url, params={"state": "open"}) #sync
        response_data = response.json()
        output_dir = "output/csv_reports"
        os.makedirs(output_dir, exist_ok=True)

        # Define csv file with unique name using timestamp
        csv_filename = os.path.join(output_dir, f"open_pull_requests_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv")

        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["PR Name", "Created Date", "Author"])
            for pr in response_data:
                pr_name = pr["title"]
                created_date = pr["created_at"]
                author = pr["user"]["login"]
                writer.writerow([pr_name, created_date, author])

        print(f"Open pull requests have been saved to {csvfile}")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to fetch pull requests: {e}")


