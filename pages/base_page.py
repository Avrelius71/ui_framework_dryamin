from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f'{self.base_url}{self.page_url}')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def assert_open(self, text):
        assert self.driver.current_url == text
