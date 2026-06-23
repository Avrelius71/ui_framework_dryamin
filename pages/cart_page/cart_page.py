from pages.base_page import BasePage
from selenium.webdriver.common.by import By


empty_cart_loc = (By.CSS_SELECTOR, '.js_cart_lines')
order_overview_loc = (By.XPATH, '//h3[text()="Order overview"]')
checkout_block_loc = (By.CSS_SELECTOR, '.o_website_sale_checkout')


class CartPage(BasePage):
    page_url = '/shop/cart'

    def assert_empty_cart_message(self):
        assert self.find(empty_cart_loc).text == 'Your cart is empty!'

    def assert_order_overview_title(self):
        assert self.find(order_overview_loc).text == 'Order overview'

    def assert_checkout_block(self):
        assert self.find(checkout_block_loc).is_displayed()
