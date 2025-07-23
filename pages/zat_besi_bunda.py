from playwright.sync_api import Page, expect

class ZatBesiBunda:
    def __init__(self, page: Page):
        self.page = page
        
    def fill_nama_bunda(self):
        input_nama_bunda = self.page.locator('input[placeholder="Masukkan nama bunda"]')
        input_nama_bunda.fill("test wahyu hamil ticket")
    def click_condition_sedang_hamil(self):
        self.page.locator('xpath=//*[@id="formBunda"]/div[1]/div/div[1]/label/div/span').click()
    def click_condition_sedang_menyusui(self):
        self.page.locator('xpath=//*[@id="formBunda"]/div[1]/div/div[2]/label/div/span').click()
    def choose_hpht(self):
        self.page.locator('#lmp_date').click()

