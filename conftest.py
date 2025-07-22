import os
import pytest

pytest_plugins = ["pytest_playwright.plugin"]

@pytest.fixture(scope="function")
def page(playwright):
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    user_agent = os.getenv("USER_AGENT", None)

    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(user_agent=user_agent)
    page = context.new_page()

    yield page

    context.close()
    browser.close()
