from pages.home_page import HomePage

def test_click_artikel(page):
    home = HomePage(page)
    home.open()
    home.click_artikel_menu()

    assert "artikel" in home.current_url().lower()
