from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "Email")
    PASSWORD_INPUT = (By.NAME, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button-1.login-button")

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


