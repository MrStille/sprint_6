import random
import re
from datetime import datetime, timedelta
from enum import Enum

import allure
from selenium.webdriver.common.by import By

from data import Data
from pages.base_page import BasePage
from pages.main_page import MainPage


class COLOR(Enum):
    Black = 1
    Grey = 2

class OrderPage(BasePage):
    URL = Data.SITE_URL + "order"

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_LIST = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_ITEMS = (By.XPATH, "//li[@class='select-search__row']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[starts-with(@class,'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[starts-with(@class,'Order_Buttons')]/button[text()='Заказать']")
    RENT_DAYS_LIST = (By.XPATH, "//div[starts-with(@class,'Dropdown-placeholder')]")
    RENT_DAYS_ITEMS = (By.XPATH, "//div[@class='Dropdown-option']")
    WHEN_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    BLACK_COLOR = (By.XPATH, "//label[@for='black']")
    GREY_COLOR = (By.XPATH, "//label[@for='grey']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINISH_ORDER_TITLE = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")

    ORDER_CREATED_TITLE = (By.XPATH, "//div[text()='Заказ оформлен']")
    ORDER_CREATED_TEXT = (By.XPATH, "//div[starts-with(@class,'Order_Text')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.get(self.URL)
        self.order_page_is_load()
        if self.driver.find_element(*MainPage.ACCEPT_COOKIE_BUTTON).is_displayed():
            self.driver.find_element(*MainPage.ACCEPT_COOKIE_BUTTON).click()

    @allure.step('Ждем пока загрузиться страница заказа')
    def order_page_is_load(self):
        self.wait_element_visible( self.NAME_INPUT)

    @allure.step('Заполняем первую страницу формы заказа.')
    def fill_first_page_of_order_form(self, name, surname, address, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.select_random_metro()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    @allure.step('Нажимаем на кнопку Продолжить')
    def click_continue_order_button(self):
        self.wait_element_visible( self.CONTINUE_BUTTON).click()

    @allure.step('Заполняем второю страницу формы заказа.')
    def fill_second_page_of_order_form(self, plus_days, rent_days, color, comment):
        self.wait_element_visible( self.RENT_DAYS_LIST)
        date = datetime.now() + timedelta(days=plus_days)
        date_str = date.strftime('%d.%m.%Y')
        self.driver.find_element(*self.WHEN_DELIVERY).send_keys(date_str)
        # двойной клик нужен, чтобы убрать фокус с дата-пикера и
        self.driver.find_element(*self.BLACK_COLOR).click()
        self.driver.find_element(*self.BLACK_COLOR).click()
        self.driver.find_element(*self.RENT_DAYS_LIST).click()
        rent_days_items = self.driver.find_elements(*self.RENT_DAYS_ITEMS)
        rent_days_items[rent_days - 1].click()
        selected_color = self.BLACK_COLOR
        if color == COLOR.Grey:
            selected_color = self.GREY_COLOR
        self.driver.find_element(*selected_color).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)

    @allure.step('Нажимаем на верхнею кнопку Заказать.')
    def click_order_top_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()

    @allure.step('Нажимаем на нижнею кнопку Заказать.')
    def click_order_bottom_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()

    @allure.step('Выбираем случайное метро в форме заказа.')
    def select_random_metro(self):
        self.driver.find_element(*self.METRO_LIST).click()
        metro_items = self.driver.find_elements(*self.METRO_ITEMS)
        selected_metro = random.choice(metro_items)
        selected_metro.click()

    @allure.step('Отправляем заказ и считываем номер заказа.')
    def accept_order_return_order_id(self):
        self.wait_element_visible( self.YES_BUTTON).click()
        self.wait_element_visible( self.ORDER_CREATED_TITLE).click()
        text = self.driver.find_element(*self.ORDER_CREATED_TEXT).text
        return int(re.findall(r'\b\d+\b', text)[0])
