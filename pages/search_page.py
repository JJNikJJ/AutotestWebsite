from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")

    def search_for_item(self, item_name):
        self.driver.find_element(*self.SEARCH_INPUT).clear()
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(item_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
