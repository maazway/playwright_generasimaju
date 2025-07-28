from pages.home_page import HomePage
from pages.zat_besi_bunda import ZatBesiBunda
from helpers.login_helpers import login_valid

def test_pragnant_untick_login_berisiko(page):
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
    zat_besi_bunda_page.klik_lanjutkan()
    # Verifikasi bahwa navigasi berhasil
    zat_besi_bunda_page.is_navigated_to_zat_besi_bunda()
    # jawab pertanyaan
    zat_besi_bunda_page.q1_ya_click()
    zat_besi_bunda_page.q2_ya_click()
    zat_besi_bunda_page.q3_ya_click()
    zat_besi_bunda_page.q4_ya_click()
    zat_besi_bunda_page.q5_ya_click()
    zat_besi_bunda_page.q6_ya_click()
    zat_besi_bunda_page.q7_ya_click()
    zat_besi_bunda_page.q8_ya_click()
    zat_besi_bunda_page.q9_ya_click()
    zat_besi_bunda_page.q10_ya_click()
    # klik tombol submit
    zat_besi_bunda_page.klik_submit()
    # Verifikasi berhasil submit
    zat_besi_bunda_page.is_memiliki_resiko()

    # Delay untuk observasi manual (opsional - bisa dihapus di production)
    page.wait_for_timeout(10000) # delay 10 detik

