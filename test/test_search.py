from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.search_page import SearchPage

def test_search_for_item(driver):
    search_page = SearchPage(driver)
    search_page.open("https://demowebshop.tricentis.com/")
    search_page.search_for_item("computer")

    WebDriverWait(driver, 10).until(
        EC.url_contains("computer"),
        message="URL does not contain 'computer' after search"
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")),
        message="No products were displayed on the search results page"
    )

    assert "No products were found" not in driver.page_source, "No products found for 'computer'"

