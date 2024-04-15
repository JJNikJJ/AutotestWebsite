from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    cart_page = CartPage(driver)
    cart_page.open("https://demowebshop.tricentis.com/")

    cart_page.add_to_cart()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "content")),
        "The confirmation message didn't appear."
    )
    assert "has been added to your cart" in driver.page_source, "Item was not added to the cart"
    cart_page.open("https://demowebshop.tricentis.com/cart")

    product_name = "14.1-inch Laptop"
    product_in_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, product_name)),
        "The product was not found in the cart."
    )
    assert product_in_cart, f"The product {product_name} was not added to the cart."
