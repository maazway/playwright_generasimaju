from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect

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
