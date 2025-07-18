import pytest
from pages.homePage import HomePage

def test_click_masuk(page):
    home_page = HomePage(page)

    # Buka homepage
    home_page.open()

    # Klik tombol Masuk
    home_page.click_masuk_button()

    # Tunggu 3 detik jika perlu
    page.wait_for_timeout(3000)

    # Verifikasi URL tujuan
    assert "login" in home_page.current_url().lower() or "masuk" in home_page.current_url().lower()
