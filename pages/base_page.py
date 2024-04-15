class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        '''Открытие сайта'''
        self.driver.get(url)

    def get_current_url(self):
        '''Переход по определенному URL'''
        return self.driver.current_url

    def navigate_to(self, by_locator):
        '''Навигация по основным разделам магазина'''
        self.driver.find_element(*by_locator).click()

