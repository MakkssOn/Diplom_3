from selenium.webdriver.common.by import By

class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL_INPUT = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Введите новый пароль"]')
    SHOW_PASSWORD_ICON = (By.CLASS_NAME, "input__icon")
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    PASSWORD_CONTAINER = (By.CLASS_NAME, "input")
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    PASSWORD_FIELD = (By.NAME, "Пароль")

class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    ORDER_HISTORY = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выход")]')
    ORDER_HISTORY_LINK = (By.LINK_TEXT, "История заказов")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    ORDER_HISTOR = (By.XPATH, '//a[@href="/feed"]')
    PASSWORD_FIELD_RECOVERY = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@type='password']")
    HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    ACCOUNT = (By.XPATH, '//a[@href="/account/profile"]')
    ORDER_TEXTBOX = (By.CLASS_NAME, "OrderHistory_textBox__3lgbs")
    ORDER_ITEM = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    ORDER_FEED_LINK = (By.XPATH, '//p[text()="Лента Заказов"]')
    INGREDIENT = (By.CLASS_NAME, "ingredient_class")  # Пример класса
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "modal_close_icon")

class OrderHistoryLocators:
    ORDER_ITEM = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-default")
    ORDER_TEXTBOX = (By.CLASS_NAME, "OrderHistory_textBox__3lgbs")


class FeedPageLocators:
    FEED_LINK = (By.XPATH, '//a[@href="/feed"]')
    ORDER_NUMBER_IN_FEED = lambda order_number: (By.XPATH, f'//p[text()="{order_number}"]')
    CONSTRUCTOR_TAB = (By.CLASS_NAME, 'tab_tab__1SPyG')
    INGREDIENT_ITEM = (By.CLASS_NAME, "OrderHistory_img__baKNk")
    DROP_ZONE = (By.CLASS_NAME, 'App_componentContainer__2JC2W')
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_NUMBER = (By.CLASS_NAME, 'order_number')
    MODAL_TITLE = (By.CLASS_NAME, 'Modal_modal__title__2L34m')
    CLOSE_BUTTON_X = (By.XPATH, '(//button[contains(@class, "Modal_modal__close__TnseK")])[2]')
    CLOSE_MODAL_Wo = (By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_")
    ClOSE_BUTTON_FIND = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4")
    CLOSE_MODAL_W4 = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4")
    FIND_ORDER_LIST = (By.CLASS_NAME, "OrderHistory_profileList__374GU")
    ALL_TIME_ORDER_COUNT = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text_type_digits-large")
    TODAY_ORDER_COUNT = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text_type_digits-large:nth-of-type(2)")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".counter_counter__ZNLkj .counter_counter__num__3nue1")
    ORDER_ITEM = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r")
    ORDER_MODAL = (By.CLASS_NAME, "OrderDetails_modal__content")
    CONSTRUCTOR = (By.XPATH, '//a[@href="/"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close__TnseK")
    ORDER_HISTORY_LIST = (By.CLASS_NAME, "OrderHistory_profileList__374GU")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
    MODAL_ORDER_BOX = (By.CLASS_NAME, "Modal_orderBox__1xWdi")
    ORDER_NUMBER_MODAL = (By.XPATH, '//p[contains(text(), "идентификатор заказа")]/preceding-sibling::h2')
    ORDER_ITEM = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    HISTORY = (By.XPATH, '//a[text()="История заказов"]')

