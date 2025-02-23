import allure
import pytest

from RandomHelper import RandomHelper as Rh
from data import Data
from pages.main_page import MainPage
from pages.order_page import OrderPage, COLOR
from pages.top_menu import TopMenu

@allure.title("Страница Заказать открывается с главной страницы")
def test_order_page_opens_from_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    order_page = OrderPage(driver)
    order_page.order_page_is_load()
    assert "order" in driver.current_url

@allure.title("Создаем заказ с разными параметрами и нажимаем нижнею кнопку заказать")
@pytest.mark.parametrize('name, surname, address, phone, plus_days, rent_days, color, comment',
                         [
                             (Rh.get_name(), Rh.get_surname(), Rh.get_address(), "89393123123", 1, 1, COLOR.Grey,
                              "Информация для курьера"),
                             (Rh.get_name(), Rh.get_surname(), Rh.get_address(), "+89761234567", 3, 7, COLOR.Black,
                              "Информация для курьера")
                         ])
def test_create_order_by_clicking_bottom_button(driver, name, surname, address, phone, plus_days, rent_days, color,
                                                comment):
    order_page = OrderPage(driver)
    order_page.fill_first_page_of_order_form(name, surname, address, phone)
    order_page.click_continue_order_button()
    order_page.fill_second_page_of_order_form(plus_days, rent_days, color, comment)
    order_page.click_order_bottom_button()
    order_id = order_page.accept_order_return_order_id()
    assert order_id > 0

@allure.title("Создаем заказ и нажимаем верхнею кнопку Заказать")
def test_create_order_by_clicking_top_order_button(driver):
    order_page = OrderPage(driver)
    order_page.fill_first_page_of_order_form(Rh.get_name(), Rh.get_surname(), Rh.get_address(), Rh.get_phone())
    order_page.click_continue_order_button()
    order_page.fill_second_page_of_order_form(7, 3, COLOR.Black,"Информация' для курьера")
    order_page.click_order_top_button()
    order_id = order_page.accept_order_return_order_id()
    assert order_id > 0

@allure.title("Клик на лого сайта открывает главную страницу")
def test_logo_page_opens_main_page(driver):
    OrderPage(driver)
    top_menu = TopMenu(driver)
    top_menu.click_site_logo()
    assert driver.current_url == Data.SITE_URL
