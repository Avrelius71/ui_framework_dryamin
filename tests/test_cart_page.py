class TestCartPage:
    def test_empty_cart_message(self, cart_page):
        cart_page.open_page()
        cart_page.assert_empty_cart_message()

    def test_order_overview_title(self, cart_page):
        cart_page.open_page()
        cart_page.assert_order_overview_title()

    def test_checkout_block(self, cart_page):
        cart_page.open_page()
        cart_page.assert_checkout_block()
