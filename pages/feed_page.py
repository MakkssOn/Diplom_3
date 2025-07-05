from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators import FeedPageLocators
from constants import Urls
import allure

class FeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.base_url = Urls.FEED

    @allure.step("Переход на страницу Ленты заказов")
    def open_feed(self):
        self.click_element(FeedPageLocators.FEED_LINK)

    @allure.step("Проверяем, что находимся на странице Ленты заказов")
    def is_feed_page(self):
        return "feed" in self.get_current_url()

    @allure.step("Закрываем модальное окно кликом по крестику")
    def close_modal(self):
        try:
            close_button = self.wait_for_element_to_be_clickable(FeedPageLocators.CLOSE_BUTTON_X)
            self.scroll_to_element(close_button)
            self.click_element(FeedPageLocators.CLOSE_BUTTON_X)
            self.wait_for_element_to_disappear(FeedPageLocators.CLOSE_BUTTON_X)
        except (TimeoutException, ElementClickInterceptedException) as e:
            raise AssertionError(f"Не удалось закрыть модальное окно: {str(e)}")

    @allure.step("Извлекаем номер заказа из открытого модального окна")
    def extract_order_number(self):
        try:
            modal_element = self.wait_for_element_to_be_visible(
                FeedPageLocators.ORDER_NUMBER_MODAL,
                timeout=10
            )
            
            for _ in range(30):
                order_number = modal_element.text.strip()
                if order_number.isdigit() and order_number != "9999":
                    break
                self.wait(1)
            else:
                raise AssertionError("Настоящий номер заказа не был получен")

            return order_number
        except (TimeoutException, NoSuchElementException) as e:
            self.take_screenshot("debug_order_number_issue.png")
            raise AssertionError(f"Не удалось получить номер заказа: {str(e)}")