# home_page.py (updated for CI safety)
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.generasimaju.co.id/")
        self.page.wait_for_load_state("networkidle")

    def click_cookie_consent(self):
        try:
            self.page.locator("#footer_tc_privacy_button").click(timeout=5000)
        except:
            pass

    def click_masuk_button(self):
        # Tunggu tombol muncul (CI-friendly)
        self.page.wait_for_selector("text=Masuk", timeout=10000)
        self.page.locator("text=Masuk").first.click()

    def hover_kalkulator_menu(self):
        self.page.get_by_role("link", name="Kalkulator Zat Besi").hover()

    def click_submenu_bunda(self):
        self.page.get_by_role("link", name="Bunda", exact=True).click()

    def click_artikel_menu(self):
        self.page.locator("text=Artikel").first.click()
