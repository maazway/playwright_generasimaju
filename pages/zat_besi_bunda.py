import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_phone = page.locator('input[placeholder*="Masukkan Nomor Handphone"]')
        self.input_password = page.locator('input[placeholder*="Masukkan Password"]')
        self.button_masuk = page.locator("#handphone-submit")

    # Navigation
    def open(self):
        self.page.goto("https://www.generasimaju.co.id/klub-generasi-maju/login")

    # Fill actions
    def fill_phone_number(self):
        self.input_phone.fill(os.getenv("PHONE_NUMBER"))

    def fill_password(self):
        self.input_password.fill(os.getenv("PASSWORD"))

    def fill_invalid_short_phone(self):
        self.input_phone.fill(os.getenv("INVALID_PHONE_SHORT"))

    def fill_invalid_long_phone(self):
        self.input_phone.fill(os.getenv("INVALID_PHONE_LONG"))

    def fill_invalid_short_password(self):
        self.input_password.fill(os.getenv("INVALID_PASSWORD_SHORT"))

    def fill_invalid_password(self):
        self.input_password.fill(os.getenv("INVALID_PASSWORD"))

    def fill_and_clear_password(self):
        self.fill_password()
        self.clear_password()

    def clear_password(self):
        self.input_password.fill("")

    def click_masuk_button(self):
        self.button_masuk.click()

    # Assertions
    def is_login_successful(self):
        expect(self.page.locator("text=Login Berhasil")).to_be_visible(timeout=10000)

    def is_phone_number_null(self):
        expect(self.page.locator("text=Nomor Handphone belum diisi")).to_be_visible(timeout=10000)

    def is_password_null(self):
        expect(self.page.locator("text=Nomor Handphone harus diisi angka")).to_be_visible(timeout=10000)

    def is_invalid_short_phone(self):
        expect(self.page.locator("text=Nomor Handphone minimal 10")).to_be_visible(timeout=10000)

    def is_invalid_long_phone(self):
        expect(self.page.locator("text=Nomor Handphone maksimal 13")).to_be_visible(timeout=10000)

    def is_invalid_short_password(self):
        expect(self.page.locator("text=Password minimal 8 karakter")).to_be_visible(timeout=10000)

    def is_invalid_password(self):
        expect(self.page.locator("text=Password belum diisi")).to_be_visible(timeout=10000)
