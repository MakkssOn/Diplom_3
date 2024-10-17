from selenium.webdriver.common.by import By


class ListOrderLocators:

    """ Кнопка Ленты заказов в хедере"""
    ORDER_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    """Первый заказ из списка заказов"""
    FIRST_ORDER = (By.XPATH, "//div/ul/li[1]")

    """Модальное окно заказа"""
    MODAL_CONTAINER = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]")

    """Все заказы"""
    ALL_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_digits-default')]")

    """Счетчик сделанных заказов за все время"""
    IND_ORDER_ALL_TIME = (By.XPATH, ".//div/div[2]/p[2]")

    """Счетчик сделанных заказов за все сегодня"""
    IND_ORDER_TODAY_TIME = (By.XPATH, "//p[contains(@class, 'text_type_main') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    """Секция готовящихся заказов"""
    ORDERS_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]")

    """Текст в секции готовящихся заказов"""
    EMPTY_ORDERS_PROGRESS_SECTION = (By.XPATH, "//*[text() = 'Все текущие заказы готовы!']")
