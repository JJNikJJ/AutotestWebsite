from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    GENDER_MALE_RADIO = (By.ID, "gender-male")
    GENDER_FEMALE_RADIO = (By.ID, "gender-female")

    FIRSTNAME_INPUT = (By.ID, "FirstName")
    LASTNAME_INPUT = (By.ID, "LastName")

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    def select_gender(self, gender):
        if gender == "male":
            self.driver.find_element(*self.GENDER_MALE_RADIO).click()
        elif gender == "female":
            self.driver.find_element(*self.GENDER_FEMALE_RADIO).click()
        else:
            raise ValueError("Должен быть 'male' или 'female'")

    def register(self, firstname, lastname, email, password, confirm_password, gender):
        self.select_gender(gender)
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(firstname)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(lastname)

        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)

        self.driver.find_element(*self.REGISTER_BUTTON).click()

