import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from constants import Urls
from helpers import ElementChecker


@allure.feature("Личный кабинет")
@allure.story("Переход на страницу восстановления пароля")
class TestPasswordRecoveryPage:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recovery_page(self, browser):
        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        with allure.step("Открываем страницу входа"):
            login_page.open(Urls.LOGIN)

        with allure.step("Переходим к форме восстановления пароля"):
            login_page.go_to_forgot_password()

        with allure.step("Проверяем, что мы на странице восстановления пароля"):
            assert personal_account_page.is_recovery_page(), "Страница восстановления пароля не отображается"


@allure.feature("Личный кабинет")
@allure.story("Вход через страницу восстановления пароля")
class TestLoginFromRecovery:

    @allure.title("Вход через страницу восстановления пароля")
    def test_login_from_recovery(self, browser, test_user):
        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)

        with allure.step("Открываем страницу входа"):
            login_page.open(Urls.LOGIN)

        with allure.step("Переходим к восстановлению пароля"):
            login_page.go_to_forgot_password()

        with allure.step("Вводим email для восстановления пароля"):
            login_page.enter_email(test_user.email)

        with allure.step("Отправляем запрос на восстановление пароля"):
            login_page.submit_recovery()

        with allure.step("Проверяем переход на страницу восстановления пароля"):
            assert personal_account_page.is_reset_page(), "Страница восстановления пароля не была отображена"


@allure.feature("Личный кабинет")
@allure.story("Проверка отображения пароля")
class TestPasswordVisibility:

    @allure.title("Проверка отображения пароля")
    def test_password_visibility_toggle(self, browser, test_user):
        login_page = LoginPage(browser)
        element_checker = ElementChecker(browser)

        with allure.step("Открываем страницу входа"):
            login_page.open(Urls.LOGIN)

        with allure.step("Переходим к форме восстановления пароля"):
            login_page.go_to_forgot_password()

        with allure.step("Вводим email и отправляем запрос на восстановление"):
            login_page.enter_email(test_user.email)
            login_page.submit_recovery()

        with allure.step("Вводим пароль и проверяем его видимость"):
            login_page.enter_password_recovery(test_user.password)

            initial_type = login_page.get_password_input_type()
            allure.attach(
                body=f"Тип input до переключения: {initial_type}",
                name="Input Type Before Toggle",
                attachment_type=allure.attachment_type.TEXT
            )

            login_page.toggle_password_visibility()

            updated_type = login_page.get_password_input_type()
            allure.attach(
                body=f"Тип input после переключения: {updated_type}",
                name="Input Type After Toggle",
                attachment_type=allure.attachment_type.TEXT
            )

            assert updated_type == "text", "Поле не стало видимым (type='text') после клика"

            container_classes = login_page.get_password_container_class()
            allure.attach(
                body=f"Классы контейнера: {container_classes}",
                name="Container Classes",
                attachment_type=allure.attachment_type.TEXT
            )

            assert element_checker.has_any_class(
                container_classes,
                ["input_type_text", "input_size_active"]
            ), "Поле не получило ожидаемые классы при показе пароля"