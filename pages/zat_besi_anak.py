from playwright.sync_api import Page, expect

class ZatBesiAnak:
    def __init__(self, page: Page):
        self.page = page
    
    # Klik tombol "Cek Sekarang"
    def click_cek_sekarang(self):
        self.page.get_by_role("link", name="Cek Sekarang").click()

    # Pilih jenis kelamin
    def pilih_jenis_kelamin(self, jenis_kelamin: str):
        if jenis_kelamin.lower() not in ["laki-laki", "perempuan"]:
            raise ValueError("Jenis kelamin harus 'Laki-laki' atau 'Perempuan'")
        self.page.get_by_text(jenis_kelamin).click()
        
    # Pilih tanggal lahir
    def pilih_tanngal_lahir_jun_12_2024(self):
        # Klik input tanggal
        self.page.locator('#child_dob').click()
        # Klik header bulan/tahun ("2025") untuk buka pilihan tahun
        self.page.get_by_role("cell", name="2025").click()
        # Klik header bulan/tahun ("2025") untuk buka pilihan tahun
        self.page.get_by_role("cell", name="2025").click()
        # Pilih tahun 2024
        self.page.get_by_text("2024").click()
        # Pilih bulan Juni
        self.page.get_by_text("Jun").click()
        # Pilih tanggal 12
        self.page.get_by_role("cell", name="12").click()

    # Pilih asupan
    def pilih_asupan(self, *asupan_list):
        for asupan in asupan_list:
            locator = self.page.get_by_text(asupan, exact=True)
            locator.scroll_into_view_if_needed()
            locator.click()

    # Klik tombol lanjutkan
    def klik_lanjutkan(self):
        self.page.get_by_role("button", name="Lanjutkan").click()

    # Klik checkbox consent
    def klik_consent_checkbox(self):
        self.page.get_by_role("checkbox", name="Dengan ini bersedia untuk").click()

    # Assertions
    def is_memiliki_resiko(self):
        expect(self.page.locator("text=Memiliki Risiko")).to_be_visible(timeout=10000)
    def is_tidak_memiliki_resiko(self):
        expect(self.page.locator("text=Tidak Berisiko")).to_be_visible(timeout=10000)