import pytest
from selenium import webdriver

from data import Data


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Data.SITE_URL)
    yield driver
    driver.quit()


def pytest_make_parametrize_id(config, val):
    return repr(val)