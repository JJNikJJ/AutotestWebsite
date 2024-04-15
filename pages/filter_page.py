from .base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class FilterPage(BasePage):
    ORDER_BY_SELECTOR = (By.ID, "products-orderby")

    def sort_products(self, order_value):
        select = Select(self.driver.find_element(*self.ORDER_BY_SELECTOR))
        select.select_by_value(order_value)

    def set_view_mode(self, mode="list"):
        # Установка режима отображения товаров (grid или list)
        select = Select(self.driver.find_element(*self.VIEW_MODE_SELECTOR))
        select.select_by_value(f"https://demowebshop.tricentis.com/desktops?viewmode={mode}")

    def set_page_size(self, size):
        # Установка количества товаров на странице
        select = Select(self.driver.find_element(*self.PAGE_SIZE_SELECTOR))
        select.select_by_value(f"https://demowebshop.tricentis.com/desktops?viewmode=list&pagesize={size}")
