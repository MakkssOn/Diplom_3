from pages.base_page import BasePage
from locators import *
import allure


class PersonalAccountPage(BasePage):
    @allure.step("Проверяем, находимся ли мы на главной странице")
    def is_main_page(self):
        return self.BASE_URL in self.browser.current_url

    @allure.step("Переход на Ленту заказов")
    def go_to_feed(self):
        """
        Переход на Ленту заказов.
        """
        feed_link_locator = AccountPageLocators.ORDER_HISTOR
        self.click_element(feed_link_locator)

    @allure.step("Проверяем, что мы находимся на странице ленты заказов")
    def is_feed_page(self):
        return "feed" in self.get_current_url()

    @allure.step("Проверяем, что мы находимся на странице восстановления пароля")
    def is_recovery_page(self):
        return "forgot" in self.get_current_url()

    @allure.step("Проверяем, что мы находимся на странице смены пароля")
    def is_reset_page(self):
        """
        Проверяет, что текущий URL содержит 'reset-password'.
        """
        self.wait_for_url_contains("reset-password")
        current_url = self.get_current_url()  # Используем метод из BasePage
        allure.attach(body=f"Текущий URL: {current_url}", name="Current URL",
                      attachment_type=allure.attachment_type.TEXT)
        return "reset-password" in current_url

    def go_to_personal_account(self):
        """
        Кликает по кнопке перехода в личный кабинет и ожидает, пока не перейдем на страницу профиля.
        """
        # Кликаем по кнопке перехода в Личный кабинет с помощью нового метода
        self.click_element(AccountPageLocators.ACCOUNT_BUTTON)

        # Ожидаем, пока URL не будет содержать "/account/profile"
        self.wait_for_url_contains("/account/profile")

    @allure.step("Проверяем, что мы на странице Личного кабинета")
    def is_personal_account_page(self):
        """
        Проверяет, что мы находимся на странице Личного кабинета,
        проверяя наличие элемента и корректность URL.
        """
        # Используем метод из BasePage для проверки видимости элемента
        if self.is_element_present(AccountPageLocators.ACCOUNT):
            # Используем метод из BasePage для проверки URL
            return self.is_url_contains("/account/profile")
        return False

    @allure.step("Выход из аккаунта")
    def logout(self):
        """
        Выполняет выход из аккаунта, кликая на кнопку выхода.
        Проверяет, что после выхода происходит редирект на страницу логина.
        """
        # Ожидаем появления и доступности кнопки выхода
        logout_button = self.wait_for_element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)

        # Прокручиваем к кнопке, чтобы убедиться, что она в зоне видимости
        self.scroll_to_element(logout_button)

        # Ждем, пока кнопка станет видимой
        self.wait_for_element_to_be_visible(AccountPageLocators.LOGOUT_BUTTON)

        # Кликаем на кнопку выхода
        logout_button.click()

        # Убедимся, что мы вернулись на страницу логина
        self.wait_for_url_contains("login")

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """
        Вводит пароль в поле на странице аккаунта.
        """
        self.send_keys_to_element(AccountPageLocators.PASSWORD_FIELD, password)

    @allure.step("Переходит в историю заказов и извлекает номер заказа")
    def go_to_order_history(self):
        """
        Переходит на страницу истории заказов и извлекает номер заказа.
        """
        # Переходим к ссылке "История заказов" и кликаем по ней
        self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)

        # Извлекаем номер первого заказа из истории
        order_number = self.get_element_text(AccountPageLocators.ORDER_ITEM, timeout=15)
        return order_number

    @allure.step("Получение номера заказа из истории")
    def get_order_number(self):
        """
        Получает номер заказа из истории заказов.
        """
        order_number = self.get_element_text(AccountPageLocators.ORDER_TEXTBOX, timeout=15)

        if order_number:
            print(f"[LOG] Найден номер заказа: {order_number}")
        else:
            print("[LOG] Не удалось найти номер заказа.")

        return order_number

    @allure.step("Проверяем, что мы находимся на странице ленты заказов")
    def is_oder_history_page(self):
        """
        Проверяет, что текущий URL содержит 'history'.
        """
        current_url = self.get_current_url()  # Используем метод из BasePage
        return "history" in current_url
