from pages.navigation_page import NavigationPage


def test_navigation_to_computers_positive(driver):
    nav_page = NavigationPage(driver)
    nav_page.open("https://demowebshop.tricentis.com/")
    nav_page.go_to_computers()
    assert "computers" in nav_page.get_current_url(), "Failed to navigate to computers section"


def test_navigation_to_electronics_positive(driver):
    nav_page = NavigationPage(driver)
    nav_page.open("https://demowebshop.tricentis.com/")
    nav_page.go_to_electronics()
    assert "electronics" in nav_page.get_current_url(), "Failed to navigate to electronics section"
