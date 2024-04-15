# Добавление товара в корзину

from base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input[type='button'][value='Add to cart']")

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
