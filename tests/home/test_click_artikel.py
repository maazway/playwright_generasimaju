from pages.homePage import HomePage

def test_click_artikel(page):
    home = HomePage(page)
    home.open()
    home.click_artikel_menu()
