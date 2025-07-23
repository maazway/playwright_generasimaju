import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_only_phone_number(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_phone_number()
    login_page.click_masuk_button()
    login_page.is_invalid_short_password()

def test_login_short_password(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_invalid_short_password()
    login_page.is_invalid_short_password()

def test_login_short_phone(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_invalid_short_phone()
    login_page.is_invalid_short_phone()

def test_login_valid(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_phone_number()
    login_page.fill_password()
    login_page.click_masuk_button()
    login_page.is_login_successful()

def test_login_fill_and_clear_password(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_and_clear_password()
    login_page.is_invalid_password()

def test_login_long_phone(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_invalid_long_phone()
    login_page.is_invalid_long_phone()

def test_login_only_password(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_cookie_consent()
    home_page.click_masuk_button()
    login_page.fill_password()
    login_page.click_masuk_button()
    login_page.is_password_null()
