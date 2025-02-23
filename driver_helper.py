from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DriverHelper:
    DEFAULT_TIMEOUT = 5

    @staticmethod
    def wait_new_window_loads(driver, windows_number):
        WebDriverWait(driver, DriverHelper.DEFAULT_TIMEOUT).until(expected_conditions.number_of_windows_to_be(windows_number))

    @staticmethod
    def wait_until_url_contains(driver, expected_url):
        WebDriverWait(driver, DriverHelper.DEFAULT_TIMEOUT).until(expected_conditions.url_contains(expected_url))
