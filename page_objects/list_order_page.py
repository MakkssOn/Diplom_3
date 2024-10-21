import allure
from page_objects.base_page import BasePage
from locators.list_order_locators import ListOrderLocators as order_locators


class ListOrderPage(BasePage):

    @allure.step("Тапаем на кнопку Ленты заказов ")
    def tap_on_order_list_button(self):
        self.wait_element_visibility_of_element_located(order_locators.ORDER_LIST_BUTTON)
        self.click_on_element(order_locators.ORDER_LIST_BUTTON)
        return self.get_current_url()

    @allure.step("Тапаем на плитку заказ")
    def tap_on_order_block(self):
        self.wait_element_visibility_of_element_located(order_locators.FIRST_ORDER)
        self.click_on_element(order_locators.FIRST_ORDER)
        self.wait_element_visibility_of_element_located(order_locators.MODAL_CONTAINER)
        return self.find_element(order_locators.MODAL_CONTAINER)

    @allure.step("Ищем все элементы")
    def return_all_order_text(self):
        self.wait_element_visibility_of_element_located(order_locators.ALL_ORDERS)
        return self.return_locators_text(order_locators.ALL_ORDERS)

    @allure.step("Проверяем счетчик приготовленных заказов за все время")
    def check_completed_orders_all_time(self):
        self.wait_element_visibility_of_element_located(order_locators.IND_ORDER_ALL_TIME)
        return self.find_element(order_locators.IND_ORDER_ALL_TIME).text

    @allure.step("Првоеряем счетчик выполненных заказов за сегодня")
    def check_completed_orders_today(self):
        self.wait_element_visibility_of_element_located(order_locators.IND_ORDER_TODAY_TIME)
        return self.find_element(order_locators.IND_ORDER_TODAY_TIME).text

    @allure.step("Чекаем полку с готовящимися заказами ")
    def check_order_progress_section(self):
        self.wait_element_visibility_of_element_located(order_locators.ORDERS_PROGRESS_SECTION)
        self.wait_not_visibility_of_element_located(order_locators.EMPTY_ORDERS_PROGRESS_SECTION)
        return self.return_locators_text(order_locators.ORDERS_PROGRESS_SECTION)

    def return_locators_text(self, locator):
        all_locators = self.find_all(locator)
        locator_text = []
        for order in all_locators:
            locator_text.append(order.text)
        return locator_text
