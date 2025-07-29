from pages.home_page import HomePage
from pages.zat_besi_anak import ZatBesiAnak
from helpers.login_helpers import login_valid
from helpers.login_helpers import wait_until_page_ready 
from helpers.login_helpers import wait_10s

def test_male_untick_login_berisiko(page): # Login condition
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

    zat_besi_anak.a4()
    zat_besi_anak.a4()
    zat_besi_anak.a4()
    zat_besi_anak.a4()
    zat_besi_anak.a4()
    zat_besi_anak.a4()

    zat_besi_anak.klik_dapatkan_hasil()

    zat_besi_anak.is_berisiko()

    wait_10s(page)

def test_male_untick_login_tidak_berisiko(page): # Login condition
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

    zat_besi_anak.a1()
    zat_besi_anak.a1()
    zat_besi_anak.a1()
    zat_besi_anak.a1()
    zat_besi_anak.a1()
    zat_besi_anak.a1()

    zat_besi_anak.klik_dapatkan_hasil()

    zat_besi_anak.is_tidak_berisiko()

    zat_besi_anak.scroll_to_text()

    zat_besi_anak.floating_banner()

    wait_10s(page)