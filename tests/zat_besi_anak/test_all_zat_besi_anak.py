from pages.home_page import HomePage
from pages.zat_besi_anak import ZatBesiAnak
from helpers.login_helpers import login_valid
from helpers.login_helpers import wait_until_page_ready 
from helpers.login_helpers import wait_10s

def test_male_tick_login_berisiko(page):
    login_valid(page)

    wait_until_page_ready(page) 

    home_page = HomePage(page)
    home_page.hover_kalkulator_menu()
    home_page.click_submenu_anak()

    wait_until_page_ready(page)  

    zat_besi_anak = ZatBesiAnak(page)
    zat_besi_anak.click_cek_sekarang()
    zat_besi_anak.pilih_jenis_kelamin('Laki-laki')
    zat_besi_anak.pilih_tanngal_lahir_jun_12_2024()
    zat_besi_anak.pilih_asupan("ASI")
    zat_besi_anak.klik_consent_checkbox()
    zat_besi_anak.klik_lanjutkan()

def test_male_untick_login_berisiko(page):
    login_valid(page)

    wait_until_page_ready(page) 

    home_page = HomePage(page)
    home_page.hover_kalkulator_menu()
    home_page.click_submenu_anak()

    wait_until_page_ready(page)  

    zat_besi_anak = ZatBesiAnak(page)
    zat_besi_anak.click_cek_sekarang()
    zat_besi_anak.pilih_jenis_kelamin('Laki-laki')
    zat_besi_anak.pilih_tanngal_lahir_jun_12_2024()
    zat_besi_anak.pilih_asupan("ASI")
    zat_besi_anak.klik_lanjutkan()

    wait_10s(page)