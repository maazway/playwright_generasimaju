import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page(playwright):
    browser = playwright.chromium.launch(headless=os.getenv("HEADLESS", "true") == "true")
    context = browser.new_context(user_agent=os.getenv("USER_AGENT", None))
    page = context.new_page()
    yield page
    context.close()
    browser.close()
