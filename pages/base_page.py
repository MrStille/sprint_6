from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    driver = None
    def __init__(self, driver):
        self.driver = driver

    DEFAULT_TIMEOUT = 5

    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def wait_new_window_loads(self, windows_number):
        WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.number_of_windows_to_be(windows_number))

    def wait_until_url_contains(self, expected_url):
        WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.url_contains(expected_url))