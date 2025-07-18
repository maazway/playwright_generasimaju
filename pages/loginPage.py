import os
from playwright.sync_api import Page
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

class loginPage:
    def __init__(self, page: Page):
        self.page = page
    #Fungtionality
    def open(self):
        self.page.goto("https://www.generasimaju.co.id/klub-generasi-maju/login")
    def fill_phone_number(self):
        phone = os.getenv("PHONE_NUMBER")
        self.page.locator('input[placeholder*="Masukkan Nomor Handphone"]').fill(phone)
    def fill_password(self):
        password = os.getenv("PASSWORD")
        self.page.locator('input[placeholder*="Masukkan Password"]').fill(password)
    def click_masuk_button(self):
        self.page.locator("#handphone-submit").click()
    #Assertion
    def is_login_successful(self):
        locator = self.page.locator("text=Login Berhasil")
        locator.wait_for(timeout=10000)
        assert locator.is_visible()
    def is_phone_number_null(self):
        locator = self.page.locator("Nomor Handphone belum diisi")
        locator.wait_for(timeout=10000)
        assert locator.is_visible()
    def is_password_null(self):
        locator = self.page.locator("text=Password minimal 8 karakter")
        locator.wait_for(timeout=10000)
        assert locator.is_visible()
