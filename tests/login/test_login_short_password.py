import pytest
from pages.homePage import HomePage
from pages.loginPage import loginPage

def test_login_short_password(page):
    home_page = HomePage(page)
    login_page = loginPage(page)

    # Buka homepage
    home_page.open()
    #click cookie consent
    home_page.click_cookie_consent()
    # Klik tombol Masuk
    home_page.click_masuk_button()
    # Input nomor hp pendek
    login_page.fill_invalid_short_password()
    # Verify nomor hp pendek
    login_page.is_invalid_short_password()
