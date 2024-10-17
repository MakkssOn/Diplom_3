from selenium.webdriver.common.by import By


class HomeLocators:

    """ Текст кнопки Конструктор на главной странице """
    MY_CONSTRUCTOR = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2" and text() = "Конструктор"]')

    """Заголовок СОБЕРИТЕ БУРГЕР на странице конструктора """
    CONSTRUCTOR_TITLE = (By.CSS_SELECTOR, 'h1.text.text_type_main-large.mb-5.mt-10')

    """ Кнопка Ленты заказов в хедере"""
    ORDER_LIST_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"

    """Заголовок страницы с заказами """
    HEADER_ORDER_LIST = By.XPATH, "//h1[text()='Лента заказов']"

    """Карточка ингридиента на странице конструктора"""
    BUN = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"

    """Модальное окно с деталями ингридиента"""
    HEADER_MODAL = By.XPATH, "//h2[text()='Детали ингредиента']"

    """Крестик закрытия модального окна"""
    CLOSE_MODAL_BUTTON = By.XPATH, "//button[contains(@class, 'close')]"

    """Область добавления ингридиентов"""
    ADDITION_AREA_COUNTER = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"

    """Контейнер ингридиента """
    COUNTER_BUN = By.XPATH, "//p[@class='counter_counter__num__3nue1']"

    """Кнопка Оформить заказ"""
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    """Модальное окно подтверждения созданного заказа"""
    CREATE_ORDER_MODAL = By.CLASS_NAME, "Modal_modal__container__Wo2l_"
