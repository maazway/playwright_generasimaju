from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_kalkulator = page.get_by_role("link", name="Kalkulator Zat Besi")
        self.submenu_bunda = page.get_by_role("link", name="Bunda", exact=True)
        self.cookie_button = page.locator("#footer_tc_privacy_button")
        self.button_masuk = page.locator("text=Masuk").first

    def open(self):
        self.page.goto("https://www.generasimaju.co.id/")

    def click_cookie_consent(self):
        try:
            self.cookie_button.click(timeout=5000)
        except:
            pass 

    def click_masuk_button(self):
        self.button_masuk.click()

    def hover_kalkulator_menu(self):
        self.menu_kalkulator.hover()

    def click_submenu_bunda(self):
        self.submenu_bunda.click()
