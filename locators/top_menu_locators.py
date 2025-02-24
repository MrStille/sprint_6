from selenium.webdriver.common.by import By


class TopMenuLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    SITE_LOGO = (By.XPATH, "//a[starts-with(@class,'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[starts-with(@class,'Header_LogoYandex')]")