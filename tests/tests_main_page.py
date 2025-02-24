import allure

from driver_helper import DriverHelper
from pages.main_page import MainPage
from pages.top_menu import TopMenu


@allure.title('На главной странице кликаем на лого Яндекса, в новом окне открываемся dzen.ru')
def test_yandex_logo_opens_dzen_new_window(driver):
    main_page = MainPage(driver)
    top_menu = TopMenu(driver)
    original_window = driver.current_window_handle
    top_menu.click_yandex_logo()
    main_page.wait_until_new_window_loads(2)
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    main_page.wait_until_url_contains("https://dzen.ru/")