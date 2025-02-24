import random
import re
from datetime import datetime, timedelta
from enum import Enum

import allure

from data import Data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from driver_helper import DriverHelper


class COLOR(Enum):
    Black = 1
    Grey = 2

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        driver.get(Data.ORDER_PAGE_URL)
        self.order_page_is_load()
        if self.driver.find_element(*MainPageLocators.ACCEPT_COOKIE_BUTTON).is_displayed():
            self.driver.find_element(*MainPageLocators.ACCEPT_COOKIE_BUTTON).click()

    @allure.step('Ждем пока загрузиться страница заказа')
    def order_page_is_load(self):
        DriverHelper.wait_element_visible(self.driver, OrderPageLocators.NAME_INPUT)

    @allure.step('Заполняем первую страницу формы заказа.')
    def fill_first_page_of_order_form(self, name, surname, address, phone):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.select_random_metro()
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

    @allure.step('Нажимаем на кнопку Продолжить')
    def click_continue_order_button(self):
        DriverHelper.wait_element_visible(self.driver, OrderPageLocators.CONTINUE_BUTTON).click()

    @allure.step('Заполняем второю страницу формы заказа.')
    def fill_second_page_of_order_form(self, plus_days, rent_days, color, comment):
        DriverHelper.wait_element_visible(self.driver, OrderPageLocators.RENT_DAYS_LIST)
        date = datetime.now() + timedelta(days=plus_days)
        date_str = date.strftime('%d.%m.%Y')
        self.driver.find_element(*OrderPageLocators.WHEN_DELIVERY).send_keys(date_str)
        # двойной клик нужен, чтобы убрать фокус с дата-пикера и
        self.driver.find_element(*OrderPageLocators.BLACK_COLOR).click()
        self.driver.find_element(*OrderPageLocators.BLACK_COLOR).click()
        self.driver.find_element(*OrderPageLocators.RENT_DAYS_LIST).click()
        rent_days_items = self.driver.find_elements(*OrderPageLocators.RENT_DAYS_ITEMS)
        rent_days_items[rent_days - 1].click()
        selected_color = OrderPageLocators.BLACK_COLOR
        if color == COLOR.Grey:
            selected_color = OrderPageLocators.GREY_COLOR
        self.driver.find_element(*selected_color).click()
        self.driver.find_element(*OrderPageLocators.COMMENT).send_keys(comment)

    @allure.step('Нажимаем на верхнею кнопку Заказать.')
    def click_order_top_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_TOP).click()

    @allure.step('Нажимаем на нижнею кнопку Заказать.')
    def click_order_bottom_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_BOTTOM).click()

    @allure.step('Выбираем случайное метро в форме заказа.')
    def select_random_metro(self):
        self.driver.find_element(*OrderPageLocators.METRO_LIST).click()
        metro_items = self.driver.find_elements(*OrderPageLocators.METRO_ITEMS)
        selected_metro = random.choice(metro_items)
        selected_metro.click()

    @allure.step('Отправляем заказ и считываем номер заказа.')
    def accept_order_return_order_id(self):
        DriverHelper.wait_element_visible(self.driver, OrderPageLocators.YES_BUTTON).click()
        DriverHelper.wait_element_visible(self.driver, OrderPageLocators.ORDER_CREATED_TITLE).click()
        text = self.driver.find_element(*OrderPageLocators.ORDER_CREATED_TEXT).text
        return int(re.findall(r'\b\d+\b', text)[0])
