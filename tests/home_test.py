import allure
from data import Url


class TestHomePage:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверяем работу кнопки Конструктор в хедере")
    def test_switch_on_construct_by_tap_button(self, home, driver, password_recovery):

        assert home.tap_on_construct(password_recovery)

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Проверяем работу кнопки Лента заказов")
    def test_switch_on_order_list_by_tap_button(self, home, driver, password_recovery):

        assert home.tap_on_order_list_button() == Url.FEED_PAGE

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями,")
    @allure.description("Проверяем работу всплывающего окна ")
    def test_tap_on_ingridient(self, home):

        assert home.tap_on_ingredient()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("Проверяем работу кнопки закрытия модального окна")
    def test_tap_on_close_btn_on_modal(self, home):

        home.tap_on_ingredient()

        assert home.tap_on_close_btn()

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    @allure.description("Проверяем работу счетчика увеличения количества ингридиентов")
    def test_check_change_ingredients(self, home, driver):

        indicator_ingredient = home.add_items_in_order()

        assert int(indicator_ingredient[0]) == 0 and int(indicator_ingredient[1]) == 2

    @allure.title("Залогиненный пользователь может оформить заказ.")
    @allure.description("Проверяем оформление заказа авторизованным пользователем")
    def test_create_order_auth_user(self, home, private_office, create_user, password_recovery):

        private_office.authorization(create_user, password_recovery)
        home.add_items_in_order()

        assert home.tap_create_order_btn()
