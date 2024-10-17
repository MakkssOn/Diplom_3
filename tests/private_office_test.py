import allure

from data import Url


class TestPrivateOffice:

    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Проверяем работу кнопки Личного Кабинета в хедере")
    def test_tap_on_private_office_button(self, driver, password_recovery):

        password_recovery.go_to_personal_account()

        assert password_recovery.get_current_url() == Url.LOGIN_PAGE

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Проверяем открытие страницы Истории заказов у авторизованного пользователя ")
    def test_transition_to_history_orders(self, private_office, create_user, password_recovery):

        private_office.auth_and_change_order(create_user, password_recovery)

        assert private_office.open_history_orders(password_recovery) == Url.HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description("Проверяем выход из аккаунта")
    def test_logout(self, private_office, create_user, password_recovery):
        private_office.login(create_user, password_recovery)
        password_recovery.go_to_personal_account()

        assert private_office.logout() == Url.LOGIN_PAGE
