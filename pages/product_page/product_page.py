from pages.base_page import BasePage
from selenium.webdriver.common.by import By


all_products_breadcrumb_loc = (By.LINK_TEXT, 'All Products')
multimedia_breadcrumb_loc = (By.LINK_TEXT, 'Multimedia')
product_title_loc = (By.CSS_SELECTOR, 'h1[itemprop="name"]')


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def clic_all_products_breadcrumb(self):
        self.find(all_products_breadcrumb_loc).click()

    def clic_multimedia_breadcrumb(self):
        self.find(multimedia_breadcrumb_loc).click()

    def assert_product_title(self):
        assert self.find(product_title_loc).text == 'Office Design Software'
