import allure

from helpers import Helpers
from page_objects.base_page import BasePage
from locators.private_office_locators import PrivateOffice as office_locators


class PrivateOfficePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Авторизоваться уникальным пользователем ")
    def login(self, create_user, password_recovery):
        password_recovery.go_to_personal_account()
        user_date, resp = create_user
        self.send_keys(office_locators.EMAIL_INPUT, user_date['email'])
        self.send_keys(office_locators.PASSWORD_INPUT, user_date['password'])
        self.click_on_element(office_locators.LOGIN_BUTTON)
        self.wait_element_visibility_of_element_located(office_locators.CREATE_ORDER_BUTTON)
        return user_date['email'], user_date['password']

    @allure.step("Авторизоваться")
    def authorization(self, create_user, password_recovery):
        password_recovery.go_to_personal_account()
        self.login(create_user, password_recovery)

    @allure.step("Авторизоваться и сделать заказы")
    def auth_and_change_order(self, create_user, password_recovery):
        helpers = Helpers()
        password_recovery.go_to_personal_account()
        user_date, resp = create_user
        self.send_keys(office_locators.EMAIL_INPUT, user_date['email'])
        self.send_keys(office_locators.PASSWORD_INPUT, user_date['password'])
        self.click_on_element(office_locators.LOGIN_BUTTON)
        self.wait_element_visibility_of_element_located(office_locators.CREATE_ORDER_BUTTON)
        number = helpers.created_orders(resp)
        number = str(number.json()['order']['number'])

        return user_date['email'], user_date['password'], number

    @allure.title("Открыть личный кабинет и тапнуть по истории заказов")
    def open_history_orders(self, password_recovery):
        password_recovery.go_to_personal_account()
        self.wait_element_visibility_of_element_located(office_locators.HISTORY_ORDER)
        self.click_on_element(office_locators.HISTORY_ORDER)
        self.wait_element_visibility_of_element_located(office_locators.HISTORY_ORDER)
        return self.get_current_url()

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.wait_element_visibility_of_element_located(office_locators.LOGOUT_BUTTON)
        self.click_on_element(office_locators.LOGOUT_BUTTON)
        self.wait_element_visibility_of_element_located(office_locators.LOGIN_BUTTON)
        return self.get_current_url()
