import pytest
from selenium import webdriver

from data import Data
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
   # driver.get(Data.SITE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture()
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page


def pytest_make_parametrize_id(config, val):
    return repr(val)