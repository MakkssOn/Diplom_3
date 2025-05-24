from pages.base_page import BasePage
from locators import *
import allure


class LoginPage (BasePage):
    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password(self):
        """
        Кликает по ссылке для восстановления пароля.
        """
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        """
        Вводит email в соответствующее поле.
        """
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Клик на кнопку 'Восстановить'")
    def submit_recovery(self):
        """
        Кликает по кнопке восстановления пароля.
        """
        self.click_element(LoginPageLocators.RECOVER_BUTTON)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """
        Вводит пароль в соответствующее поле.
        """
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Прокручивает к иконке и кликает на неё")
    def toggle_password_visibility(self):
        """
        Прокручивает к иконке отображения пароля и кликает на неё.
        """
        self.scroll_to_element_and_click(LoginPageLocators.SHOW_PASSWORD_ICON)

    @allure.step("Возвращает значение атрибута 'type' у поля пароля.")
    def get_password_input_type(self):
        """
        Возвращает значение атрибута 'type' у поля пароля.
        """
        return self.get_element_attribute(LoginPageLocators.PASSWORD_INPUT, "type")

    @allure.step("Получение класса контейнера поля пароля")
    def get_password_container_class(self):
        """
        Возвращает значение атрибута 'class' у контейнера поля пароля.
        """
        return self.get_element_attribute(LoginPageLocators.PASSWORD_CONTAINER, "class")

    @allure.step("Переход в личный кабинет")
    def go_to_personal_account(self):
        """
        Кликает по кнопке перехода в личный кабинет.
        """
        self.click_element(LoginPageLocators.ACCOUNT_BUTTON)

    @allure.step("Клик на кнопку 'Войти'")
    def submit_login(self):
        """
        Кликает по кнопке входа.
        """
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Проверка, что мы находимся на странице логина")
    def is_login_page(self):
        """
        Проверяет, что текущий URL содержит 'login'.
        """
        current_url = self.get_current_url()  # Используем метод из BasePage
        return "login" in current_url


    def login(self, email, password):
        """Метод для выполнения логина в личный кабинет"""
        self.open_base_url()
        self.go_to_personal_account()
        self.enter_email(email)
        self.enter_password(password)  # Используем метод текущего класса
        self.submit_login()

    def get_password_input_type(self):
        return self.get_element_attribute(LoginPageLocators.PASSWORD_INPUT, "type")

    def get_password_container_class(self):
        return self.get_element_class(LoginPageLocators.PASSWORD_CONTAINER)

    @allure.step("Ввод пароля")
    def enter_password_recovery(self, password):
        """
        Вводит пароль в соответствующее поле.
        """
        self.enter_text(AccountPageLocators.PASSWORD_FIELD_RECOVERY, password)
