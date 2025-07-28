from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect, Page

def login_valid(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_phone_number()
    login_page.fill_password()
    login_page.click_masuk_button()

    # Tutup popup jika muncul
    try:
        close_button = page.locator('xpath=//*[@id="modalErrorMessage"]/div/div/div[1]/button')
        expect(close_button).to_be_visible(timeout=10000)
        close_button.click(force=True)
    except:
        pass


def wait_until_page_ready(page: Page, timeout: int = 10000):
    # Tunggu hingga network idle dan ada elemen utama muncul (misalnya <body> atau loader hilang)
    page.wait_for_load_state("networkidle", timeout=timeout)

    # Tambahan: pastikan elemen penting muncul (misalnya heading, atau kontainer utama)
    expect(page.locator("body")).to_be_visible(timeout=timeout)

def wait_10s(page: Page):
    # Tunggu selama 10 detik
    page.wait_for_timeout(10000)
