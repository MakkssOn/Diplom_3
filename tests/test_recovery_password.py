import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.base_page import BasePage


@allure.feature("Личный кабинет")
@allure.story("Переход на страницу восстановления пароля")
class TestPasswordRecoveryPage:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recovery_page(self, browser):
        # Получаем данные из BasePage
        test_data = BasePage.get_test_data()  # Получаем данные для теста из метода get_test_data()

        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        allure.step("Открываем страницу входа")
        login_page.open("https://stellarburgers.nomoreparties.site/login")

        allure.step("Переходим к форме восстановления пароля")
        login_page.go_to_forgot_password()

        allure.step("Проверяем, что мы на странице восстановления пароля")
        assert personal_account_page.is_recovery_page(), "Страница восстановления пароля не отображается"


@allure.feature("Личный кабинет")
@allure.story("Вход через страницу восстановления пароля")
class TestLoginFromRecovery:

    @allure.title("Вход через страницу восстановления пароля")
    def test_login_from_recovery(self, browser):
        test_data = BasePage.get_test_data()
        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        allure.step("Открываем страницу входа")
        login_page.open("https://stellarburgers.nomoreparties.site/login")

        allure.step("Переходим к восстановлению пароля")
        login_page.go_to_forgot_password()

        allure.step("Вводим email для восстановления пароля")
        email = test_data["email"]
        login_page.enter_email(email)

        allure.step("Отправляем запрос на восстановление пароля")
        login_page.submit_recovery()

        allure.step("Проверяем переход на страницу восстановления пароля")
        assert personal_account_page.is_reset_page(), "Страница восстановления пароля не была отображена"


@allure.feature("Личный кабинет")
@allure.story("Проверка отображения пароля")
class TestPasswordVisibility:

    @allure.title("Проверка отображения пароля")
    def test_click_button(self, browser):
        test_data = BasePage.get_test_data()
        login_page = LoginPage(browser)

        allure.step("Открываем страницу входа")
        login_page.open("https://stellarburgers.nomoreparties.site/login")

        allure.step("Переходим к форме восстановления пароля")
        login_page.go_to_forgot_password()

        allure.step("Вводим email и отправляем запрос на восстановление")
        email = test_data["email"]
        login_page.enter_email(email)
        login_page.submit_recovery()

        allure.step("Вводим пароль и проверяем его видимость")
        password = test_data["password"]
        login_page.enter_password_recovery(password)

        input_type = login_page.get_password_input_type()
        allure.attach(body=f"Тип input до переключения: {input_type}", name="Input Type Before Toggle",
                      attachment_type=allure.attachment_type.TEXT)

        login_page.toggle_password_visibility()

        input_type = login_page.get_password_input_type()
        allure.attach(body=f"Тип input после переключения: {input_type}", name="Input Type After Toggle",
                      attachment_type=allure.attachment_type.TEXT)

        assert input_type == "text", "Поле не стало видимым (type='text') после клика"

        container_class = login_page.get_password_container_class()
        allure.attach(body=f"Классы контейнера: {container_class}", name="Container Classes",
                      attachment_type=allure.attachment_type.TEXT)

        assert any(cls in container_class for cls in ["input_type_text", "input_size_active"]), \
            "Поле не получило ожидаемые классы при показе пароля"







