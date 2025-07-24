from playwright.sync_api import Page, expect

class ZatBesiBunda:
    def __init__(self, page: Page):
        self.page = page
        self.input_nama_bunda = page.locator('input[placeholder="Masukkan nama bunda"]')
        self.radio_sedang_hamil = page.locator('xpath=//*[@id="formBunda"]/div[1]/div/div[1]/label/div/span')
        self.input_tanggal_hpht = page.get_by_role("textbox", name="Contoh: 01-11-")
        self.q1_ya = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div[2]/div/label[1]')
        self.q2_ya = page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/div[2]/div/label[1]')
        self.q3_ya = page.locator('xpath=//*[@id="questions"]/div[3]/div[2]/div[2]/div/label[1]')
        self.q4_ya = page.locator('xpath=//*[@id="questions"]/div[4]/div[2]/div[2]/div/label[1]')
        self.q5_ya = page.locator('xpath=//*[@id="questions"]/div[5]/div[2]/div[2]/div/label[1]')
        self.q6_ya = page.locator('xpath=//*[@id="questions"]/div[6]/div[2]/div[2]/div/label[1]')
        self.q7_ya = page.locator('xpath=//*[@id="questions"]/div[7]/div[2]/div[2]/div/label[1]')
        self.q8_ya = page.locator('xpath=//*[@id="questions"]/div[8]/div[2]/div[2]/div/label[1]')
        self.q9_ya = page.locator('xpath=//*[@id="questions"]/div[9]/div[2]/div[2]/div/label[1]')
        self.q10_ya = page.locator('xpath=//*[@id="questions"]/div[10]/div[2]/div[2]/div/label[1]')
        self.q1_tidak = page.locator('xpath=//*[@id="questions"]/div[1]/div[2]/div[2]/div/label[2]')
        self.q2_tidak = page.locator('xpath=//*[@id="questions"]/div[2]/div[2]/div[2]/div/label[2]')
        self.q3_tidak = page.locator('xpath=//*[@id="questions"]/div[3]/div[2]/div[2]/div/label[2]')
        self.q4_tidak = page.locator('xpath=//*[@id="questions"]/div[4]/div[2]/div[2]/div/label[2]')
        self.q5_tidak = page.locator('xpath=//*[@id="questions"]/div[5]/div[2]/div[2]/div/label[2]')
        self.q6_tidak = page.locator('xpath=//*[@id="questions"]/div[6]/div[2]/div[2]/div/label[2]')
        self.q7_tidak = page.locator('xpath=//*[@id="questions"]/div[7]/div[2]/div[2]/div/label[2]')
        self.q8_tidak = page.locator('xpath=//*[@id="questions"]/div[8]/div[2]/div[2]/div/label[2]')
        self.q9_tidak = page.locator('xpath=//*[@id="questions"]/div[9]/div[2]/div[2]/div/label[2]')
        self.q10_tidak = page.locator('xpath=//*[@id="questions"]/div[10]/div[2]/div[2]/div/label[2]')

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

    def klik_lanjutkan(self):
        self.page.get_by_role("button", name="Lanjutkan").click()

    # Verifikasi bahwa navigasi berhasil
    def is_navigated_to_zat_besi_bunda(self):
        expect(self.page.locator("text=Sekitar 30% wanita usia 15–49 tahun")).to_be_visible(timeout=10000)

    # Jawab pertanyaan
    def q1_ya_click(self):
        self.q1_ya.click()
    def q2_ya_click(self):
        self.q2_ya.click()
    def q3_ya_click(self):
        self.q3_ya.click()
    def q4_ya_click(self):
        self.q4_ya.click()
    def q5_ya_click(self):
        self.q5_ya.click()
    def q6_ya_click(self):
        self.q6_ya.click()
    def q7_ya_click(self):
        self.q7_ya.click()
    def q8_ya_click(self):
        self.q8_ya.click()
    def q9_ya_click(self):
        self.q9_ya.click()
    def q10_ya_click(self):
        self.q10_ya.click()
    def q1_tidak_click(self):
        self.q1_tidak.click()
    def q2_tidak_click(self):
        self.q2_tidak.click()
    def q3_tidak_click(self):
        self.q3_tidak.click()
    def q4_tidak_click(self):
        self.q4_tidak.click()
    def q5_tidak_click(self):
        self.q5_tidak.click()
    def q6_tidak_click(self):
        self.q6_tidak.click()
    def q7_tidak_click(self):
        self.q7_tidak.click()
    def q8_tidak_click(self):
        self.q8_tidak.click()
    def q9_tidak_click(self):
        self.q9_tidak.click()
    def q10_tidak_click(self):
        self.q10_tidak.click()

    # Klik tombol submit
    def klik_submit(self):
        self.page.get_by_role("button", name="Submit").click()

    # Assertions
    def is_memiliki_resiko(self):
        expect(self.page.locator("text=Memiliki Risiko")).to_be_visible(timeout=10000)
    def is_tidak_memiliki_resiko(self):
        expect(self.page.locator("text=Tidak Berisiko")).to_be_visible(timeout=10000)