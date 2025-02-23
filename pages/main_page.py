import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.top_menu import TopMenu


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"
    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    faq_table = (By.XPATH, "//div[starts-with(@class,'Home_FAQ')]")
    faq_item = (By.XPATH, "//div[@class='accordion__item']")
    faq_item_title = (By.XPATH, "//div[@class='accordion__item']//div[text()='{0}']")
    faq_item_text = (
        By.XPATH, faq_item_title[1] + "/ancestor::div[@class='accordion__item']//div[@class='accordion__panel']")

    # Сколько это стоит? И как оплатить?
    def __init__(self, driver):
        super().__init__(driver)
        self.open_main_page()

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.driver.get(self.URL)
        self.wait_element_visible(TopMenu.SITE_LOGO)

    @allure.step('Скролим к вопросам')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*self.faq_item)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq)

    @allure.step('Прочитать текст для вопроса {question_title}')
    def get_faq_question_text(self, question_title):
        item_title = self.wait_element_clickable(self.format_locator(self.faq_item_title, question_title))
        item_title.click()
        item_text = self.wait_element_visible(self.format_locator(self.faq_item_text, question_title))
        return item_text.text

    @staticmethod
    def format_locator(locator, text):
        new_locator = (locator[0], locator[1].format(text))
        return new_locator
