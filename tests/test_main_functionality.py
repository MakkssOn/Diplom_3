import allure
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from pages.base_page import BasePage

@allure.feature("Конструктор")
@allure.story("Переход в Конструктор")
class TestConstructorPage:

    @allure.title("Переход в Конструктор")
    def test_go_to_constructor(self, browser):
        test_data = BasePage.get_test_data()  # Получение тестовых данных
        login_page = LoginPage(browser)  # Создаем экземпляр страницы логина
        feed_page = FeedPage(browser)  # Создаем экземпляр страницы ленты заказов

        # Логинимся на странице
        login_page.login(test_data["email"], test_data["password"])

        # Переходим в конструктор
        feed_page.click_constructor()

        # Проверяем, что мы на странице конструктора
        assert feed_page.is_constructor_page(), "Не удалось перейти в Конструктор"


@allure.feature("Лента заказов")
@allure.story("Переход на Ленту заказов")
class TestFeedPage:

    @allure.title("Переход в Ленту заказов")
    def test_go_to_feed(self, browser):
        test_data = BasePage.get_test_data()  # Получение тестовых данных
        login_page = LoginPage(browser)  # Создаем экземпляр страницы логина
        feed_page = FeedPage(browser)  # Создаем экземпляр страницы ленты заказов

        # Логинимся на странице
        login_page.login(test_data["email"], test_data["password"])

        # Переходим на Ленту заказов
        feed_page.open_feed()

        # Проверяем, что мы на странице Ленты заказов
        assert feed_page.is_feed_page(), "Не удалось перейти на Ленту заказов"


@allure.feature("Модальные окна")
@allure.story("Клик по ингредиенту и проверка модального окна")
class TestModalWindow:

    @allure.title("Клик по ингредиенту и проверка модального окна")
    def test_click_ingredient_and_check_modal(self, browser):
        test_data = BasePage.get_test_data()
        login_page = LoginPage(browser)
        feed_page = FeedPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        feed_page.open_feed()
        feed_page.click_ingredient()
        assert feed_page.is_modal_open(), "Модальное окно не открылось"

    @allure.title("Закрытие модального окна")
    def test_close_modal_window(self, browser):
        test_data = BasePage.get_test_data()
        login_page = LoginPage(browser)
        feed_page = FeedPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        feed_page.open_feed()
        feed_page.click_ingredient()
        feed_page.close_modal()
        assert feed_page.is_modal_closed(), "Модальное окно не закрылось"


@allure.feature("Заказы")
@allure.story("Создание и проверка заказов")
class TestOrderCreation:

    @allure.title("Создание заказа")
    def test_create_order(self, browser):
        test_data = BasePage.get_test_data()
        login_page = LoginPage(browser)
        feed_page = FeedPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        feed_page.open_feed()
        feed_page.click_constructor()
        feed_page.drag_and_drop_ingredient("Флюоресцентная булка R2-D3")
        feed_page.drag_and_drop_ingredient("Соус Spicy-X")
        feed_page.drag_and_drop_ingredient("Мясо бессмертных моллюсков Protostomia")
        feed_page.create_order()
        order_number = feed_page.extract_order_number()
        assert order_number, "Номер заказа не отображается"

    @allure.title("Увеличение каунтера")
    def test_check_counters(self, browser):
        test_data = BasePage.get_test_data()
        login_page = LoginPage(browser)
        feed_page = FeedPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        feed_page.click_constructor()
        initial_counter = feed_page.get_counter()
        feed_page.drag_and_drop_ingredient("Флюоресцентная булка R2-D3")
        feed_page.drag_and_drop_ingredient("Соус Spicy-X")
        feed_page.drag_and_drop_ingredient("Мясо бессмертных моллюсков Protostomia")
        final_counter = feed_page.get_counter()
        assert final_counter == initial_counter + 2, \
            f"Ожидалось, что каунтер увеличится на 2, но было {final_counter - initial_counter}."







