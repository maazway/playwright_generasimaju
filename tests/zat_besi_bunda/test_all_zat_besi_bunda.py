from pages.home_page import HomePage
from pages.zat_besi_bunda import ZatBesiBunda
from helpers.login_helpers import login_valid

def test_zat_besi_bunda(page):
    # Login
    login_valid(page)

    # Navigasi ke halaman Zat Besi Bunda
    home_page = HomePage(page)
    home_page.hover_kalkulator_menu()
    home_page.click_submenu_bunda()

    # Isi form
    zat_besi_bunda_page = ZatBesiBunda(page)
    zat_besi_bunda_page.fill_nama_bunda()
    zat_besi_bunda_page.click_condition_sedang_hamil()
    zat_besi_bunda_page.pilih_tanggal_hpht_feb_12_2025()
    zat_besi_bunda_page.klik_consent_checkbox()
    # Delay untuk observasi manual (opsional - bisa dihapus di production)
    page.wait_for_timeout(5000)
