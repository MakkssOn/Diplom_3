from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import allure

class BasePage:
    def __init__(self, browser, driver=None):
        """
        Инициализация базовой страницы.
        :param browser: Экземпляр WebDriver
        :param driver: Дополнительный экземпляр драйвера (опционально)
        """
        self.browser = browser
        self.driver = driver or browser
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открываем URL: {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Находим элемент по локатору {locator}")
    def find_element(self, locator):
        return self.browser.find_element(*locator)

    @allure.step("Ожидаем, пока элемент с локатором {locator} станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент с локатором {locator} не стал кликабельным в течение {timeout} секунд."
        )

    @allure.step("Кликаем по элементу с локатором {locator}")
    def click_element(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step("Ожидаем, пока элемент с локатором {locator} станет видимым")
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не виден в течение {timeout} секунд."
        )

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return self.browser.current_url

    @allure.step("Обновляем текущую страницу")
    def refresh_page(self):
        self.browser.refresh()

    @allure.step("Ожидаем, пока элемент с локатором {locator} исчезнет")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until_not(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не исчез."
        )

    @allure.step("Выполняем скрипт: {script} с аргументами {args}")
    def execute_script(self, script, *args):
        self.browser.execute_script(script, *args)

    @allure.step("Сохраняем скриншот в файл: {file_name}")
    def take_screenshot(self, file_name):
        self.browser.save_screenshot(file_name)