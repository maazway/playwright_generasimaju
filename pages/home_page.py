from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.generasimaju.co.id/")

    def click_artikel_menu(self):
        self.page.locator("text=Artikel").first.click()

    def current_url(self):
        return self.page.url