from .base_page import BasePage
from selenium.webdriver.common.by import By


class NavigationPage(BasePage):
    COMPUTERS_MENU = (By.CSS_SELECTOR, "ul.top-menu a[href='/computers']")
    ELECTRONICS_MENU = (By.CSS_SELECTOR, "ul.top-menu a[href='/electronics']")
    BOOKS_MENU = (By.CSS_SELECTOR, "ul.top-menu a[href='/books']")
    APPAREL_SHOES_MENU = (By.CSS_SELECTOR, "ul.top-menu a[href='/apparel-shoes']")
    JEWELRY_MENU = (By.CSS_SELECTOR, "ul.top-menu a[href='/jewelry']")
    GIFT_CARDS_MENU = (By.CSS_SELECTOR, "ul.top-menu a[href='/gift-cards']")

    def go_to_computers(self):
        self.navigate_to(self.COMPUTERS_MENU)

    def go_to_electronics(self):
        self.navigate_to(self.ELECTRONICS_MENU)

    def go_to_books(self):
        self.navigate_to(self.BOOKS_MENU)

    def go_to_apparel_shoes(self):
        self.navigate_to(self.APPAREL_SHOES_MENU)

    def go_to_jewelry(self):
        self.navigate_to(self.JEWELRY_MENU)

    def go_to_gift_cards(self):
        self.navigate_to(self.GIFT_CARDS_MENU)
