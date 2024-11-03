import pytest
from config.config import BASE_URL
# from playwright.async_api import Page, expect, async_playwright
from playwright.sync_api import Page, expect


@pytest.mark.console
def test_console_errors(page: Page):
    """Test to ensure no console errors appear on the About page."""
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.goto(f"{BASE_URL}/about.html")
    assert not errors, f"Console errors found: {errors}"

