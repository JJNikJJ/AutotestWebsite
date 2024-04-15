from base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_ITEM_QUANTITY_INPUT = (By.XPATH, "//input[contains(@class, 'qty-input')]")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")

    def set_item_quantity(self, quantity):
        quantity_input = self.driver.find_element(*self.CART_ITEM_QUANTITY_INPUT)
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def update_cart(self):
        self.driver.find_element(*self.UPDATE_CART_BUTTON).click()

    def get_total_price(self):
        return self.driver.find_element(By.CLASS_NAME, "product-subtotal").text
