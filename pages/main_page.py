import allure

from data import Data
from driver_helper import DriverHelper
from locators.main_page_locators import MainPageLocators
from locators.top_menu_locators import TopMenuLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.open_main_page()

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.driver.get(Data.SITE_URL)
        DriverHelper.wait_element_visible(self.driver, TopMenuLocators.SITE_LOGO)

    @allure.step('Скролим к вопросам')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*MainPageLocators.faq_item)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq)

    @allure.step('Прочитать текст для вопроса {question_title}')
    def get_faq_question_text(self, question_title):
        item_title = DriverHelper.wait_element_clickable(self.driver, self.format_locator(*MainPageLocators.faq_item_title, question_title))
        item_title.click()
        item_text = DriverHelper.wait_element_visible(self.driver, self.format_locator(*MainPageLocators.faq_item_text, question_title))
        return item_text.text

    @allure.step("Ждем пока будет открыто {windows_number} окна")
    def wait_until_new_window_loads(self, windows_number):
        DriverHelper.wait_new_window_loads(self.driver, windows_number)

    @allure.step("Ждем пока урл текущей страницы не будет содержать {url} ")
    def wait_until_url_contains(self, url):
        DriverHelper.wait_until_url_contains(self.driver, url)

    @staticmethod
    def format_locator(locator, text):
        new_locator = (locator[0], locator[1].format(text))
        return new_locator
