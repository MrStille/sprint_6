import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TopMenu(BasePage):
    ORDER_TOP_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    SITE_LOGO = (By.XPATH, "//a[starts-with(@class,'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[starts-with(@class,'Header_LogoYandex')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Нажимаем на лого сайта')
    def click_site_logo(self):
        self.wait_element_visible(self.SITE_LOGO).click()

    @allure.step('Нажимаем на лого Яндекса')
    def click_yandex_logo(self):
        self.wait_element_clickable(self.YANDEX_LOGO).click()
