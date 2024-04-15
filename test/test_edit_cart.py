from selenium.webdriver.common.by import By
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_edit_cart_quantity(driver):
    cart_page = CartPage(driver)
    cart_page.open("https://demowebshop.tricentis.com/cart")

    cart_page.set_item_quantity(2)
    cart_page.update_cart()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.XPATH, "//input[contains(@class, 'qty-input')]"), "2")
    )

    assert "2" in cart_page.get_item_quantity(), "Quantity update in cart failed"
