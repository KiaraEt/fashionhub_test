import json
import pytest


@pytest.fixture(scope="session")
def read_json_file():
    """Fixture to read JSON files located in the data directory."""
    def _read_json_file(file_name):
        try:
            with open(f"data/{file_name}") as file:
                json_data = json.load(file)
                return json_data
        except FileNotFoundError:
            pytest.fail(f"File {file_name} not found in the data directory.")
        except json.JSONDecodeError:
            pytest.fail(f"Error decoding JSON from the file {file_name}.")
        except Exception as ex:
            pytest.fail(f"Unexpected exception raised: {ex}")
    return _read_json_file