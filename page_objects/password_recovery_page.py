import allure

from helpers import Helpers
from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.password_recovery_locators import PersonalAccount as lk


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("Переход в личный кабинет тапом по кнопке ЛК в хедере ")
    def go_to_personal_account(self):
        self.wait_element_visibility_of_element_located(lk.MY_OFFICE)
        self.click_on_element(lk.MY_OFFICE)

    @allure.title("Ждём кнопку 'Восстановить пароль', нажимаем на неё ")
    def tap_and_wait_recovery_button(self):
        self.wait_element_visibility_of_element_located(lk.RECOVERY_PASS_LINK_BUTTON)
        self.click_on_element(lk.RECOVERY_PASS_LINK_BUTTON)
        return self.find_element(lk.RECOVERY_PASS_HEADER)

    @allure.title("Вводим эмайл в поле ввода и тапаем по кнопке восстановления пароля")
    def input_email_and_push_recovery_btn(self, driver):
        self.wait_element_visibility_of_element_located(lk.EMAIL_INPUT)
        self.click_on_element(lk.EMAIL_INPUT)
        user_data = Helpers.generate_user_data()
        self.send_keys(lk.EMAIL_INPUT, user_data['email'])
        self.click_on_element(lk.RECOVERY_BUTTON)
        self.wait_element_visibility_of_element_located(lk.PASSWORD_INPUT)
        return self.find_element(lk.PASSWORD_INPUT)

    @allure.title("Ищем инпут для пароля, и вводим туда рандомный пароль")
    def find_pass_input_and_enter_pass(self, ):
        self.wait_element_visibility_of_element_located(lk.PASSWORD_INPUT)
        user_data = Helpers.generate_user_data()
        self.send_keys(lk.PASSWORD_INPUT, user_data['password'])

    @allure.step("Тапаем на иконку глаза рядом с инпутом пароля, чтобы сделать его видимым")
    def click_on_eye_icon(self):
        self.click_on_element(lk.EYE_BUTTON)
        return self.find_element(lk.VISIBLE_PASS_INPUT)
