from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    faq_table = (By.XPATH, "//div[starts-with(@class,'Home_FAQ')]")
    faq_item = (By.XPATH, "//div[@class='accordion__item']")
    faq_item_title = (By.XPATH, "//div[@class='accordion__item']//div[text()='{0}']")
    faq_item_text = (
        By.XPATH, faq_item_title[1] + "/ancestor::div[@class='accordion__item']//div[@class='accordion__panel']")