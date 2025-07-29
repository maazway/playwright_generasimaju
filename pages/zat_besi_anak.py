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

    # Klik checkbox consent
    def klik_consent_checkbox(self):
        self.page.get_by_role("checkbox", name="Dengan ini bersedia untuk").click()

    # Klik tombol lanjutkan
    def klik_lanjutkan(self):
        self.page.get_by_role("button", name="Lanjutkan").click()

    # Questions
    def a1(self):
        self.page.locator('//*[@id="wrapper-answer"]/div/div[1]').click()
    def a2(self):
        self.page.locator('//*[@id="wrapper-answer"]/div/div[2]').click()
    def a3(self):
        self.page.locator('//*[@id="wrapper-answer"]/div/div[3]').click()
    def a4(self):
        self.page.locator('//*[@id="wrapper-answer"]/div/div[4]').click()

    # Klik Dapatkan Hasil
    def klik_dapatkan_hasil(self):
        self.page.get_by_role("button", name="Dapatkan Hasil").click()

    # Assertions
    def is_berisiko(self):
        expect(self.page.locator("text=Berisiko")).to_be_visible(timeout=10000)
    def is_tidak_berisiko(self):
        expect(self.page.locator("text=Tidak Berisiko")).to_be_visible(timeout=10000)

    # Scrool to text
    def scroll_to_text(self):
        self.page.locator("text=Temukan Artikel").scroll_into_view_if_needed()

    # Floating banner
    def floating_banner(self):
        return self.page.locator('//*[@id="tools-ironc-result"]/div/div/picture/img').click()
    
    # Landing page 