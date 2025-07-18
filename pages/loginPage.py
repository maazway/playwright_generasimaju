
from playwright.sync_api import Page

class SamplePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_homepage(self):
        self.page.goto("https://www.generasimaju.co.id/")
        # return "Tumbuh Kembang" in self.page.title()
