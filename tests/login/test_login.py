import pytest
from playwright.sync_api import sync_playwright

def test_open_website(page):
    page.goto("https://www.generasimaju.co.id/")
    assert "Tumbuh Kembang" in page.title()