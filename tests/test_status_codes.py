import pytest
from playwright.sync_api import sync_playwright,Page, expect
from config.config import BASE_URL
# from playwright.async_api import Page, expect, async_playwright


@pytest.mark.links
def test_link_status_codes(page: Page):
    """Test all links on the homepage to ensure they return successful status codes."""
    page.goto(BASE_URL)

    # Extract all link URLs
    links = page.eval_on_selector_all("a", "elements => elements.map(e => e.href)")

    for link in links:
        try:
            response = page.goto(link)
            assert response.status in range(200, 400), f"{link} returned status {response.status}"
        except Exception as e:
            pytest.fail(f"Failed to load {link}: {str(e)}")