from playwright.sync_api import Page

class ZatBesiBunda:
    def __init__(self, page: Page):
        self.page = page
        self.input_nama_bunda = page.locator('input[placeholder="Masukkan nama bunda"]')
        self.radio_sedang_hamil = page.locator('xpath=//*[@id="formBunda"]/div[1]/div/div[1]/label/div/span')
        self.input_tanggal_hpht = page.get_by_role("textbox", name="Contoh: 01-11-")

    def fill_nama_bunda(self):
        self.input_nama_bunda.fill("test wahyu hamil ticket")

    def click_condition_sedang_hamil(self):
        self.radio_sedang_hamil.click()

    def klik_input_hpht(self):
        self.input_tanggal_hpht.click()

    def pilih_tanggal_hpht_feb_12_2025(self):
        # Klik input tanggal
        self.page.get_by_role("textbox", name="Contoh: 01-11-").click()

        # Klik header bulan/tahun ("July 2025") untuk buka pilihan bulan
        self.page.get_by_role("cell", name="2025").click()

        # Pilih bulan Februari
        self.page.get_by_text("Feb").click()

        # Pilih tanggal 12
        self.page.get_by_role("cell", name="12").click()

    def klik_consent_checkbox(self):
        self.page.get_by_role("checkbox", name="Dengan ini bersedia untuk").click()
