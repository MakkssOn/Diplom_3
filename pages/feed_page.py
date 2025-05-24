from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
import time
import allure
from selenium.common.exceptions import ElementClickInterceptedException



class FeedPage(BasePage):
    @allure.step("Переход на страницу Ленты заказов")
    def open_feed(self):
        """
        Открывает страницу ленты заказов.
        """
        self.click_element(FeedPageLocators.FEED_LINK)

    @allure.step("Проверяем, что находимся на странице Ленты заказов")
    def is_feed_page(self):
        """
        Проверяет, что текущий URL содержит 'feed'.
        """
        current_url = self.get_current_url()  # Используем метод из BasePage
        return "feed" in current_url

    @allure.step("Кликаем на ингредиент для открытия модального окна")
    def click_ingredient(self):
        """
        Кликает на элемент ингредиента для открытия модального окна.
        """
        self.click_element(FeedPageLocators.INGREDIENT_ITEM)

    @allure.step("Проверяем, что модальное окно открыто и видимо")
    def is_modal_open(self):
        """
        Проверяет, что модальное окно открыто и видимо.
        """
        modal_locator = FeedPageLocators.MODAL_ORDER_BOX
        modal = self.wait_for_element_to_be_visible(modal_locator)
        return modal.is_displayed()

    @allure.step("Закрываем модальное окно кликом по крестику")
    def close_modal(self):
        try:
            # Ждём появления контейнера модального окна
            self.wait_for_element_to_be_present(FeedPageLocators.CLOSE_MODAL_Wo)

            # Ждём и находим кнопку закрытия
            close_button = self.wait_for_element_to_be_clickable(FeedPageLocators.CLOSE_BUTTON_X)

            # Скроллим к кнопке и кликаем на неё
            self.scroll_to_element(close_button)

            # Кликаем по кнопке
            self.click_element(close_button)

            # Ждём, пока активный класс исчезнет, что указывает на закрытие окна
            self.wait_for_element_to_disappear(FeedPageLocators.ClOSE_BUTTON_FIND)

        except Exception as e:
            raise AssertionError(f"Не удалось закрыть модальное окно: {str(e)}")

    @allure.step("Проверяет, что модальное окно закрыто")
    def is_modal_closed(self):
        """
        Проверяет, что модальное окно закрыто, ожидая исчезновения кнопки закрытия.
        :return: True, если окно успешно закрыто, иначе False.
        """
        try:
            # Используем метод из BasePage для проверки исчезновения кнопки
            self.wait_for_element_to_disappear(FeedPageLocators.ClOSE_BUTTON_FIND)

            return True
        except AssertionError as e:

            return False

    @allure.step("Кликает на 'Конструктор'")
    def click_constructor(self):
        """
        Кликает на ссылку 'Конструктор'.
        """
        self.click_element(FeedPageLocators.CONSTRUCTOR)

    @allure.step("Проверяет, что мы находимся на главной странице")
    def is_constructor_page(self):
        return self.BASE_URL in self.get_current_url()

    @allure.step("Ожидает, пока элемент станет видимым, и скроллит до него")
    def wait_and_scroll_to_element(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет видимым, и прокручивает страницу до него.
        """
        element = self.wait_for_element_to_be_visible(locator, timeout)
        self.scroll_to_element(element)
        return element

    @allure.step("Ищет заказ в ленте заказов")
    def find_order_in_feed(self, order_number):
        """
        Ищет заказ по номеру в ленте заказов.
        """
        try:
            orders = self.wait_for_elements_to_be_present(FeedPageLocators.ORDER_ITEM)
            for order in orders:
                if order_number in order.text:

                    return True

            return False
        except TimeoutException:

            return False

    @allure.step("Открываем модальное окно с деталями заказа")
    def open_order_modal(self, order_element):
        """
        Открывает модальное окно с деталями заказа.
        """
        order_element.click()

    @allure.step("Перетаскивает ингредиент в зону сборки")
    def drag_and_drop_ingredient(self, ingredient_name):
        ingredient_locator = (By.XPATH, f"//p[contains(text(), '{ingredient_name}')]")
        ingredient = self.wait_and_scroll_to_element(ingredient_locator)
        drop_zone = self.wait_and_scroll_to_element(FeedPageLocators.DROP_ZONE)

        ActionChains(self.browser).drag_and_drop(ingredient, drop_zone).perform()

    @allure.step("Нажимает на кнопку оформления заказа")
    def create_order(self):
        """
        Нажимает на кнопку оформления заказа и ожидает завершения действия.
        """
        self.scroll_to_element_and_click(FeedPageLocators.CREATE_ORDER_BUTTON)

        # Неявное ожидание или проверка может быть заменена на более конкретную логику
        self.wait_for_custom_condition(lambda driver: True, timeout=15)

    @allure.step("Извлекает номер заказа из модального окна")
    def get_order_number(self):
        modal_title = self.wait_and_scroll_to_element(FeedPageLocators.MODAL_TITLE)
        return modal_title.text

    @allure.step("Ожидает, пока элемент исчезнет")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет невидимым или исчезнет.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Закрывает модальное окно с номером заказа после закрытия большого модального окна")
    def close_modal_for_order(self):
        """
        Закрывает модальное окно кликом по кнопке закрытия (крестику), проверяя все состояния.
        """
        try:
            # Ожидание большого модального окна

            self.wait_for_element(FeedPageLocators.MODAL_OVERLAY)


            # Ожидание появления модального окна

            self.wait_for_element(FeedPageLocators.CLOSE_MODAL_W4)


            # Находим кнопку закрытия

            close_button = self.wait_for_clickable(FeedPageLocators.CLOSE_BUTTON)


            # Скроллим к кнопке
            self.scroll_to_element(close_button)


            # Кликаем по кнопке закрытия
            try:
                close_button.click()

            except ElementClickInterceptedException:

                self.execute_script("arguments[0].click();", close_button)

            # Ожидаем исчезновения модального окна
            self.wait_for_element_to_disappear(FeedPageLocators.CLOSE_MODAL_W4)


        except Exception as e:
            # Сохранение снимка экрана для отладки
            self.take_screenshot("debug_close_modal_issue.png")

            raise AssertionError(f"Не удалось закрыть модальное окно: {str(e)}")

    @allure.step("Извлекает номер заказа из открытого модального окна")
    def extract_order_number(self):
        """
        Извлекает номер заказа из открытого модального окна.
        """


        # Ожидание появления большого модального окна
        self.wait_for_element(FeedPageLocators.MODAL_OVERLAY, timeout=10)


        # Ожидание появления модального окна

        self.wait_for_element(FeedPageLocators.CLOSE_MODAL_W4, timeout=10)


        # Ожидаем появления модального окна с идентификатором заказа
        modal_element = self.wait_for_element(
            FeedPageLocators.ORDER_NUMBER_MODAL,
            timeout=10
        )


        # Увеличиваем время ожидания для получения реального номера заказа
        max_attempts = 30  # Количество попыток
        order_number = None  # Инициализируем переменную для номера заказа

        for attempt in range(max_attempts):
            # Получаем номер заказа
            order_number = modal_element.text.strip()

            # Проверяем, что номер заказа состоит только из цифр
            if order_number.isdigit() and order_number != "9999":  # Проверяем, что это настоящий номер заказа

                break



            # Проверяем, не является ли номер заказа значением по умолчанию
            if order_number == "9999":  # Если номер по умолчанию, ждем и пытаемся снова
                self.wait_for_text_to_change(modal_element, timeout=2)
            else:
                # Если номер не изменился на корректный, выходим из цикла
                break

        # Если после всех попыток номер заказа так и не был найден, выбрасываем ошибку
        if order_number is None or not order_number.isdigit() or order_number == "9999":
            raise AssertionError(
                f"Настоящий номер заказа не был получен или номер заказа равен 9999. Получен номер: {order_number}")

        # После извлечения номера заказа, выполняем действия с кнопкой закрытия
        try:
            # Находим кнопку закрытия

            close_button = self.wait_for_clickable(FeedPageLocators.CLOSE_BUTTON)


            # Кликаем по кнопке закрытия
            close_button.click()

        except ElementClickInterceptedException:

            self.execute_script("arguments[0].click();", close_button)

        # Ожидаем исчезновения модального окна
        self.wait_for_element_to_disappear(FeedPageLocators.CLOSE_MODAL_W4)


        return order_number



    @allure.step("Переходит в личный кабинет и проверяет наличие заказа в истории")
    def check_order_in_history(self, order_number):
        """
        Проверяет наличие заказа с указанным номером в истории заказов.
        """
        # Формируем номер заказа
        search_order_number = f"#0{order_number.lstrip('#0')}"


        # Открываем раздел "История заказов"
        history_button = self.wait_for_element_to_be_clickable(FeedPageLocators.HISTORY)
        history_button.click()

        # Ожидаем появления списка заказов
        order_list = self.wait_for_element_presence(FeedPageLocators.ORDER_HISTORY_LIST)

        # Цикл для прокрутки и поиска заказа
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:


            # Ищем заказ в текущей области списка
            element = self.find_element_by_text(FeedPageLocators.ORDER_HISTORY_LIST, search_order_number)
            if element:

                return True  # Если заказ найден, возвращаем результат

            # Если заказ не найден, прокручиваем список

            self.scroll_within_element(order_list)
            attempts += 1

        # Если заказ не найден после всех попыток
        raise AssertionError(
            f"[LOG] Заказ с номером {search_order_number} не найден в истории после {max_attempts} попыток."
        )

    @allure.step("Проверяет, что заказ отображается в разделе 'В работе' с правильным цветом текста")
    def is_order_in_progress(self, order_number):
        # Убедимся, что номер заказа начинается с нуля
        if not order_number.startswith('0'):
            order_number = '0' + order_number  # Добавляем ноль, если его нет

        # Используем локатор из файла локаторов
        orders = self.find_elements(*FeedPageLocators.ORDERS_IN_PROGRESS)

        if not orders:

            return False

        for order in orders:
            if self.get_element_text(order) == order_number:
                # Получаем цвет текста элемента
                color = self.get_element_css_property(order, 'color')

                # Приводим цвет в стандартный формат (rgb)
                color = color.lower()

                # Ожидаемые цвета
                expected_color_in_progress = 'rgb(255, 255, 255)'  # Белый цвет для в работе
                expected_color_ready = 'rgb(0, 191, 255)'  # Голубой для готовых

                if color == expected_color_in_progress:
                    allure.attach(f"Заказ {order_number} в работе, цвет текста: {color}", name="Order in Progress",
                                  attachment_type=allure.attachment_type.TEXT)
                    return True
                elif color == expected_color_ready:
                    allure.attach(f"Заказ {order_number} готов, цвет текста: {color}", name="Order Ready",
                                  attachment_type=allure.attachment_type.TEXT)
                    return False  # Изменить логику в зависимости от требований
                else:
                    allure.attach(f"Заказ {order_number} имеет неожиданный цвет: {color}", name="Unexpected Color",
                                  attachment_type=allure.attachment_type.TEXT)
                    return False

        return False

    @allure.step("Обновляет текущую страницу")
    def refresh_page(self):
        self.refresh_page()

    @allure.step("Получает количество заказов из счётчиков")
    def get_order_count(self, counter_type):
        """
        Получает количество заказов по типу счётчика: 'all_time' или 'today'.
        """
        locator = None

        if counter_type == "all_time":
            locator = FeedPageLocators.ALL_TIME_ORDER_COUNT
        elif counter_type == "today":
            locator = FeedPageLocators.TODAY_ORDER_COUNT
        else:
            raise ValueError(f"Неизвестный тип счётчика: {counter_type}")

        element = self.wait_and_scroll_to_element(locator)
        try:
            return int(element.text)
        except ValueError:
            raise ValueError(f"Не удалось преобразовать текст '{element.text}' в число.")

    def get_counter(self):
        """
        Возвращает текущее значение каунтера ингредиента.
        """
        try:
            # Получаем значение каунтера и пытаемся преобразовать его в целое число
            return int(self.get_ingredient_counter(FeedPageLocators.INGREDIENT_COUNTER))
        except ValueError:
            # Если текст каунтера нельзя преобразовать в число, возвращаем 0
            return 0
        except Exception as e:
            # В случае других ошибок (например, если элемент не найден), можно логировать ошибку или вернуть 0
            return 0

    @allure.step("Находит элемент заказа")
    def find_order_element(self):
        return self.find_order_element(FeedPageLocators.ORDER_ITEM)

    @allure.step("Проверяем, что модальное окно с деталями заказа открылось")
    def is_order_modal_open(self):
        """
        Проверяет, что модальное окно с деталями заказа открыто.
        """
        return self.is_element_displayed(FeedPageLocators.ORDER_MODAL)

    @allure.step("Ожидает закрытия модального окна")
    def wait_for_modal_to_close(self):
        """
        Ожидает закрытия модального окна (его исчезновения).
        """
        self.wait_for_invisibility_of_element(FeedPageLocators.MODAL_OVERLAY)



