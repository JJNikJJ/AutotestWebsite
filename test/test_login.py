from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.open("https://demowebshop.tricentis.com/login")
    login_page.login("nikita-1707@yandex.ru", "bW4-sND-Mx3-aXc")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://demowebshop.tricentis.com/"))
    email_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.account"))
    )
    assert email_link.text == "nikita-1707@yandex.ru", f"Email после входа неверен. Ожидалось: nikita-1707@yandex.ru, получено: {email_link.text}"
    expected_url = "https://demowebshop.tricentis.com/"
    actual_url = login_page.get_current_url()
    assert actual_url == expected_url, f"URL после входа неверен. Ожидалось: {expected_url}, получено: {actual_url}"
