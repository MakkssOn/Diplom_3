import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.base_page import BasePage


@allure.feature("Личный кабинет")
@allure.story("Логин через личный кабинет")
class TestPersonalAccountLogin:

    @allure.title("Логин через личный кабинет")
    def test_go_to_personal_account(self, browser):
        # Получаем данные из BasePage
        test_data = BasePage.get_test_data()  # Получаем данные для теста из метода get_test_data()

        personal_account_page = PersonalAccountPage(browser)
        login_page = LoginPage(browser)

        # Логинимся с данными из test_data
        login_page.login(test_data["email"], test_data["password"])

        # Проверяем, что после логина перешли на главную страницу
        assert personal_account_page.is_main_page(), "Не удалось перейти на главную страницу после входа"


@allure.feature("Личный кабинет")
@allure.story("Вход в личный кабинет")
class TestPersonalAccountAccess:

    @allure.title("Вход в личный кабинет")
    def test_login_to_personal_account(self, browser):
        test_data = BasePage.get_test_data()
        personal_account_page = PersonalAccountPage(browser)
        login_page = LoginPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        personal_account_page.go_to_personal_account()
        assert personal_account_page.is_personal_account_page(), "Не удалось перейти в Личный кабинет"


@allure.feature("Личный кабинет")
@allure.story("Переход на Историю заказов")
class TestPersonalAccountOrderHistory:

    @allure.title("Переход на Историю заказов")
    def test_go_to_history(self, browser):
        test_data = BasePage.get_test_data()
        personal_account_page = PersonalAccountPage(browser)
        login_page = LoginPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()
        assert personal_account_page.is_oder_history_page(), "Не удалось перейти в Историю заказов"


@allure.feature("Личный кабинет")
@allure.story("Выход из личного кабинета")
class TestPersonalAccountLogout:

    @allure.title("Выход из личного кабинета")
    def test_logout(self, browser):
        test_data = BasePage.get_test_data()
        personal_account_page = PersonalAccountPage(browser)
        login_page = LoginPage(browser)
        login_page.login(test_data["email"], test_data["password"])
        login_page.go_to_personal_account()
        personal_account_page.logout()
        assert login_page.is_login_page(), "Не удалось выйти из аккаунта"






