from data import TEST_DATA
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    def __init__(self, browser, driver=None):
        """
        Инициализация базовой страницы.

        :param browser: Экземпляр WebDriver, основной интерфейс браузера.
        :param driver: Дополнительный экземпляр, если требуется специфический драйвер.
        """
        self.browser = browser  # Основной интерфейс браузера
        self.driver = driver or browser  # Используем browser, если driver не передан
        self.wait = WebDriverWait(self.driver, 10)  # Ожидания зависят от driver


    @allure.step("Открываем URL: {url}")
    def open(self, url):
        self.browser.get(url)

    @staticmethod
    @allure.step("Получаем тестовые данные")
    def get_test_data():
        return TEST_DATA

    @allure.step("Открываем базовый URL")
    def open_base_url(self):
        """
        Открывает базовый URL.
        """
        self.browser.get(self.BASE_URL)

    @allure.step("Получаем значение каунтера ингредиента для {ingredient_locator}")
    def get_ingredient_counter(self, ingredient_locator):
        """
        Получает значение каунтера ингредиента.
        """
        counter_element = self.find_element(ingredient_locator)
        return counter_element.text

    @allure.step("Находим элемент по локатору {locator}")
    def find_element(self, locator):
        """
        Находит элемент по локатору.
        """
        return self.browser.find_element(*locator)

    @allure.step("Ожидаем, пока элемент с локатором {locator} станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет кликабельным.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент с локатором {locator} не стал кликабельным в течение {timeout} секунд."
        )

    @allure.step("Кликаем по элементу с локатором {locator}")
    def click_element(self, locator):
        """
        Ожидает, пока элемент станет кликабельным, и кликает по нему.
        """
        element = self.wait_for_element_to_be_clickable(locator)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step("Вводим текст '{text}' в поле с локатором {locator}")
    def enter_text(self, locator, text):
        """
        Ожидает видимости элемента и вводит текст в соответствующее поле.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    @allure.step("Прокручиваем к элементу с локатором {locator} и кликаем по нему")
    def scroll_to_element_and_click(self, locator):
        """
        Прокручивает к элементу и кликает по нему.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step("Получаем атрибут {attribute} у элемента с локатором {locator}")
    def get_element_attribute(self, locator, attribute):
        """
        Получает значение атрибута у элемента.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)

    @allure.step("Ожидаем, пока URL не будет содержать подстроку {partial_url}")
    def wait_for_url_contains(self, partial_url, timeout=10):
        """
        Ожидает, пока текущий URL не будет содержать заданную подстроку.
        """
        try:
            self.wait.until(EC.url_contains(partial_url), message=f"URL не содержит подстроку: {partial_url}")
        except TimeoutException:
            raise AssertionError(f"URL не содержит подстроку {partial_url} в течение {timeout} секунд.")

    @allure.step("Проверяем, что элемент с локатором {locator} присутствует на странице")
    def is_element_present(self, locator, timeout=10):
        """
        Проверяет, что элемент присутствует на странице.
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Проверяем, что URL содержит подстроку {url_part}")
    def is_url_contains(self, url_part, timeout=10):
        """
        Проверяет, что URL содержит указанную подстроку.
        """
        self.wait.until(EC.url_contains(url_part))
        return url_part in self.browser.current_url

    @allure.step("Прокручиваем страницу к элементу {element}")
    def scroll_to_element(self, element):
        """
        Прокручивает страницу к элементу.
        """
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Ожидает, пока элемент станет видимым")
    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет видимым.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не появился в течение {timeout} секунд."
        )

    @allure.step("Вводим текст '{keys}' в элемент с локатором {locator}")
    def send_keys_to_element(self, locator, keys, timeout=10):
        """
        Ожидает видимости элемента и вводит текст в поле.
        """
        element = self.wait_for_element_visible(locator, timeout)
        element.send_keys(keys)

    @allure.step("Извлекаем текст элемента с локатором {locator}")
    def get_element_text(self, locator, timeout=10):
        """
        Ожидает видимости элемента и извлекает его текст.
        """
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step("Ожидаем, пока элемент с локатором {locator} исчезнет")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until_not(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не исчез."
        )

    @allure.step("Ожидаем, пока элементы с локатором {locator} будут присутствовать на странице")
    def wait_for_elements_to_be_present(self, locator, timeout=10):
        """
        Ожидает, пока элементы будут присутствовать на странице.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Ожидаем выполнения пользовательского условия")
    def wait_for_custom_condition(self, condition, timeout=10):
        """
        Ожидает пользовательского условия.
        """
        WebDriverWait(self.browser, timeout).until(condition)

    @allure.step("Кликаем по элементу с локатором: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Получаем класс элемента с локатором: {locator}")
    def get_element_class(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute("class")

    @allure.step("Прокручиваем страницу к элементу с локатором: {locator}")
    def scroll_into_view(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидаем, пока элемент с локатором {locator} станет видимым")
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет видимым.

        :param locator: Локатор элемента.
        :param timeout: Таймаут ожидания.
        :return: Веб-элемент.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не виден в течение {timeout} секунд."
        )

    @allure.step("Ожидаем, пока элемент с локатором {locator} появится в DOM")
    def wait_for_element_presence(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет доступным в DOM.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент с локатором {locator} не появился в течение {timeout} секунд."
        )

    @allure.step("Прокручиваем внутри элемента на {pixels} пикселей")
    def scroll_within_element(self, element, pixels=300):
        """
        Прокручивает внутри заданного элемента на указанное количество пикселей.
        """
        self.driver.execute_script("arguments[0].scrollTop += arguments[1];", element, pixels)

    @allure.step("Ищем элемент с текстом '{text}' внутри родительского элемента с локатором {parent_locator}")
    def find_element_by_text(self, parent_locator, text, timeout=5):
        """
        Ищет элемент с указанным текстом внутри родительского локатора.
        """
        parent_element = self.wait_for_element_presence(parent_locator)
        try:
            return parent_element.find_element(By.XPATH, f".//*[text()='{text}']")
        except NoSuchElementException:
            return None

    @allure.step("Ожидаем элемент с локатором {locator} и прокручиваем страницу к нему")
    def wait_and_scroll_to_element(self, locator, timeout=10):
        """
        Ожидает элемент и прокручивает страницу к нему.
        """
        element = self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент с локатором {locator} не найден в течение {timeout} секунд."
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    @allure.step("Ожидаем появления элемента с локатором {locator}")
    def wait_for_element_to_be_present(self, locator, timeout=10):
        """Ожидает появления элемента на странице."""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент с локатором {locator} не появился за {timeout} секунд."
        )

    @allure.step("Ожидаем, чтобы текст элемента {element} стал числом")
    def wait_for_element_text_to_be_digit(self, element, timeout=10):
        """
        Ожидает, пока текст элемента не станет числом.
        """
        try:
            self.wait.until(lambda driver: element.text.strip().isdigit(),
                            message="Текст элемента не является числом.")
            return True
        except TimeoutException:
            return False

    @allure.step("Проверяем видимость элемента с локатором {locator}")
    def is_element_visible(self, locator):
        """
        Проверяет, видим ли элемент на странице.
        """
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            print(f"Элемент с локатором {locator} не найден или не видим: {e}")
            return False

    @allure.step("Выполняем скрипт: {script} с аргументами {args}")
    def execute_script(self, script, *args):
        self.browser.execute_script(script, *args)

    @allure.step("Сохраняем скриншот в файл: {file_name}")
    def take_screenshot(self, file_name):
        self.browser.save_screenshot(file_name)

    @allure.step("Ожидаем появления элемента с локатором: {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидаем, пока элемент с локатором {locator} станет кликабельным")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидаем, что текст элемента изменится")
    def wait_for_text_to_change(self, element, timeout=10):
        """
        Ожидает, что текст элемента изменится.
        """
        initial_text = element.text.strip()
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda driver: element.text.strip() != initial_text,
                message="Текст элемента не изменился в отведённое время."
            )
        except TimeoutException:
            pass

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.browser.current_url

    @allure.step("Находим элементы с локатором {locator}")
    def find_elements(self, *locator):
        """Находит элементы на странице."""
        return self.browser.find_elements(*locator)

    @allure.step("Получаем значение CSS свойства {property_name} элемента")
    def get_element_css_property(self, element, property_name):
        """Получает значение CSS свойства элемента."""
        return element.value_of_css_property(property_name)

    @allure.step("Обновляем текущую страницу")
    def refresh_page(self):
        """Обновляет текущую страницу."""
        self.browser.refresh()

    @allure.step("Находим элемент заказа на странице с локатором: {locator}")
    def find_order_element(self, locator):
        """Находит элемент заказа на странице."""
        return self.browser.find_element(*locator)

    @allure.step("Проверяем, что элемент с локатором: {locator} отображается на странице.")
    def is_element_displayed(self, locator):
        """Проверяет, что элемент с данным локатором отображается на странице."""
        try:
            return self.browser.find_element(*locator).is_displayed()
        except:
            return False

    @allure.step("Ожидаем, пока элемент с локатором: {locator} станет невидимым.")
    def wait_for_invisibility_of_element(self, locator, timeout=10):
        """
        Ожидает, пока элемент с данным локатором станет невидимым (пропадет с экрана).
        """
        WebDriverWait(self.browser, timeout).until(
            EC.invisibility_of_element_located(locator)
        )























