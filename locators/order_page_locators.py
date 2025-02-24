from selenium.webdriver.common.by import By


class OrderPageLocators:
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