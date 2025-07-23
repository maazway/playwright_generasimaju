from pages.home_page import HomePage
from helpers.login_helpers import login_valid

def test_zat_besi_bunda(page):
    # Gunakan reusable login
    login_valid(page)

    # Interaksi setelah login
    home_page = HomePage(page)
    home_page.hover_kalkulator_menu()
    home_page.click_submenu_bunda()

    # Assertion: pastikan URL berubah ke halaman zat besi bunda
    assert "zat-besi-bunda" in page.url

