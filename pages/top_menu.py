import allure

from locators.top_menu_locators import TopMenuLocators
from driver_helper import DriverHelper


class TopMenu:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на лого сайта')
    def click_site_logo(self):
        DriverHelper.wait_element_visible(self.driver, TopMenuLocators.SITE_LOGO).click()

    @allure.step('Нажимаем на лого Яндекса')
    def click_yandex_logo(self):
        DriverHelper.wait_element_clickable(self.driver, TopMenuLocators.YANDEX_LOGO).click()
