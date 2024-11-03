import pytest
from config.config import BASE_URL
from utils.conftest import read_json_file
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("user_index", [0])  # Test with specific user
@pytest.mark.login
def test_login(page: Page, read_json_file, user_index):
        """Test for verifying successful user login."""
        # Load credentials for the specified user
        credentials = read_json_file("credentials.json")
        selected_user = credentials["success_login_users"][user_index]
        username = selected_user["username"]
        password = selected_user["password"]

        # Navigate to the login page and perform login
        page.goto(BASE_URL)
        page.get_by_role("link", name="Account").click()
        page.get_by_placeholder("Username").click()
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").click()
        page.get_by_placeholder("Password").fill(password)
        page.get_by_role("button", name="Login").click()

        # Check if login was successful
        expect(page.get_by_role("heading", name="Welcome, testUser!")).to_be_visible()
        assert page.url == f"{BASE_URL}/account.html", "User was not redirected to the account page after login."
