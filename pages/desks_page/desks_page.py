from pages.base_page import BasePage
from selenium.webdriver.common.by import By


customizable_desk_loc = (By.LINK_TEXT, 'Customizable Desk')
products_breadcrumb_loc = (By.XPATH, '//ol[contains(@class, "breadcrumb")]//a[@href="/shop"]')
category_title_loc = (By.XPATH, '//span[@class="d-inline-block" and text()="Desks"]')


class DesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    def clic_customizable_desk(self):
        self.find(customizable_desk_loc).click()

    def clic_products_breadcrumb(self):
        self.find(products_breadcrumb_loc).click()

    def assert_desks_title(self):
        assert self.find(category_title_loc).text == 'Desks'
