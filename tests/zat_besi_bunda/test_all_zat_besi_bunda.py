from pages.home_page import HomePage
from pages.zat_besi_bunda import ZatBesiBunda
from helpers.login_helpers import login_valid

def test_zat_besi_bunda(page):
    # Gunakan reusable login
    login_valid(page)

    # Interaksi setelah login
    home_page = HomePage(page)
    home_page.hover_kalkulator_menu()
    home_page.click_submenu_bunda()

    # Inisialisasi halaman ZatBesiBunda
    zat_besi_bunda_page = ZatBesiBunda(page)
    zat_besi_bunda_page.fill_nama_bunda()
    zat_besi_bunda_page.click_condition_sedang_hamil()


    page.wait_for_timeout(10000)
