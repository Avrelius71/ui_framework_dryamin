from pages.base_page import BasePage
from selenium.webdriver.common.by import By


empty_cart_loc = (By.CSS_SELECTOR, '.js_cart_lines')
order_overview_loc = (By.CSS_SELECTOR, '.o_website_sale_checkout h3')
checkout_block_loc = (By.CSS_SELECTOR, '.o_website_sale_checkout')


class CartPage(BasePage):
    page_url = '/shop/cart'

    def assert_empty_cart_message(self, expected_message):
        assert self.find(empty_cart_loc).text == expected_message

    def assert_order_overview_title(self, expected_title):
        assert self.find(order_overview_loc).text == expected_title

    def assert_checkout_block(self):
        assert self.find(checkout_block_loc).is_displayed()
