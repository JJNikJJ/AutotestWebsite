from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage


def test_registration_positive(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open("https://demowebshop.tricentis.com/register")

    registration_page.register("Никита", "Бушуев", "nikitabushuev_new12345@test.com", "password123456", "password123456", "male")

    WebDriverWait(driver, 10).until(EC.url_to_be("https://demowebshop.tricentis.com/registerresult/1"))

    success_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "result"))
    )
    success_message_text = success_message_element.text

    assert "Your registration completed" in success_message_text, "Регистрация не была успешной или сообщение отличается"
