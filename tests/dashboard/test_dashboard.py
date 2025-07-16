
import pytest
from playwright.sync_api import sync_playwright

def test_open_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.generasimaju.co.id/")
        assert "Generasi Maju" in page.title()
        browser.close()
