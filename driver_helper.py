from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverHelper:
    DEFAULT_TIMEOUT = 5

    @staticmethod
    def wait_element_visible(driver, locator):
        return WebDriverWait(driver, DriverHelper.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_element_clickable(driver, locator):
        return WebDriverWait(driver, DriverHelper.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_new_window_loads(driver, windows_number):
        WebDriverWait(driver, DriverHelper.DEFAULT_TIMEOUT).until(EC.number_of_windows_to_be(windows_number))

    @staticmethod
    def wait_until_url_contains(driver, expected_url):
        WebDriverWait(driver, DriverHelper.DEFAULT_TIMEOUT).until(EC.url_contains(expected_url))