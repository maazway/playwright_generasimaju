import pytest
from pages.homePage import HomePage
from pages.loginPage import loginPage

def test_click_masuk(page):
    home_page = HomePage(page)
    login_page = loginPage(page)

    # Buka homepage
    home_page.open()
    #click cookie consent
    home_page.click_cookie_consent()
    # Klik tombol Masuk
    home_page.click_masuk_button()
    # Input nomor hp
    login_page.fill_phone_number()
    # Klik button login
    login_page.click_masuk_button()
    # Verify password belum diisi
    login_page.is_password_null()
