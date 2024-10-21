import allure

from page_objects.base_page import BasePage
from locators.home_locators import HomeLocators as home_locators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Тапаем на кнопку Конструктора")
    def tap_on_construct(self, password_recovery):
        password_recovery.go_to_personal_account()
        self.find_element(home_locators.MY_CONSTRUCTOR).click()
        return self.find_element(home_locators.CONSTRUCTOR_TITLE)

    @allure.step("Тапаем на кнопку Ленты заказов ")
    def tap_on_order_list_button(self):
        self.wait_element_visibility_of_element_located(home_locators.ORDER_LIST_BUTTON)
        self.click_on_element(home_locators.ORDER_LIST_BUTTON)
        return self.get_current_url()

    @allure.step("Тапаем на ингридиент на главной странице")
    def tap_on_ingredient(self):
        self.click_on_element(home_locators.BUN)
        self.wait_element_visibility_of_element_located(home_locators.HEADER_MODAL)
        return self.find_element(home_locators.HEADER_MODAL)

    @allure.step("Тапаем на кнопку закрытия модального окна")
    def tap_on_close_btn(self):
        self.click_on_element(home_locators.CLOSE_MODAL_BUTTON)
        self.wait_not_visibility_of_element_located(home_locators.HEADER_MODAL)
        return self.find_element(home_locators.CLOSE_MODAL_BUTTON)

    @allure.step("Добавить ингредиент в заказ")
    def add_items_in_order(self):
        self.wait_element_visibility_of_element_located(home_locators.COUNTER_BUN)
        counter_ingredient = self.get_text(home_locators.COUNTER_BUN)
        self.drag_and_drop(home_locators.BUN, home_locators.ADDITION_AREA_COUNTER)
        new_counter_ingredient = self.get_text(home_locators.COUNTER_BUN)
        return counter_ingredient, new_counter_ingredient

    @allure.step("Тапнуть на кнопку «Оформить заказ")
    def tap_create_order_btn(self):
        self.wait_element_visibility_of_element_located(home_locators.CREATE_ORDER_BUTTON)
        self.click_on_element(home_locators.CREATE_ORDER_BUTTON)
        self.wait_element_visibility_of_element_located(home_locators.CREATE_ORDER_MODAL)
        return self.find_element(home_locators.CREATE_ORDER_MODAL)
