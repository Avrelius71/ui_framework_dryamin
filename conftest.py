import pytest
from selenium import webdriver
from pages.cart_page.cart_page import CartPage
from pages.desks_page.desks_page import DesksPage
from pages.product_page.product_page import ProductPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def desks_page(driver):
    return DesksPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)
