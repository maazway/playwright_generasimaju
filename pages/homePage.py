from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.generasimaju.co.id/")

    def click_cookie_consent(self):
        self.page.locator("#footer_tc_privacy_button").click()

    def click_artikel_menu(self):
        self.page.locator("text=Artikel").first.click()

    def click_masuk_button(self):
        # Klik tombol "Masuk" (ambil elemen pertama)
        self.page.locator("text=Masuk").first.click()
    
    def close_broser(self):
        return self.page
