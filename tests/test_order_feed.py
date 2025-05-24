import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.feed_page import FeedPage
from pages.base_page import BasePage


@allure.feature("Лента заказов")
@allure.story("Проверка увеличения счетчиков")
class TestOrderCounters:

    @allure.title("Проверка увеличения счетчиков 'Выполнено за всё время' и 'Выполнено за сегодня'")
    def test_check_time_counter(self, browser):
        # Получаем данные из Helper
        test_data = BasePage.get_test_data()

        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        feed_page = FeedPage(browser)

        # Используем данные из test_data
        login_page.login(test_data["email"], test_data["password"])
        feed_page.open_feed()

        total_orders_before = feed_page.get_order_count("all_time")
        today_orders_before = feed_page.get_order_count("today")

        feed_page.click_constructor()
        feed_page.drag_and_drop_ingredient("Флюоресцентная булка R2-D3")
        feed_page.drag_and_drop_ingredient("Соус Spicy-X")
        feed_page.drag_and_drop_ingredient("Мясо бессмертных моллюсков Protostomia")
        feed_page.create_order()
        feed_page.close_modal_for_order()
        feed_page.open_feed()

        total_orders_after = feed_page.get_order_count("all_time")
        today_orders_after = feed_page.get_order_count("today")

        assert total_orders_after > total_orders_before, \
            f"Счётчик 'Выполнено за всё время' не увеличился. Было: {total_orders_before}, стало: {total_orders_after}"

        assert today_orders_after > today_orders_before, \
            f"Счётчик 'Выполнено за сегодня' не увеличился. Было: {today_orders_before}, стало: {today_orders_after}"


@allure.feature("Лента заказов")
@allure.story("Проверка появления заказа в разделе 'В работе'")
class TestOrderInProgress:

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_work(self, browser):
        # Получаем данные из BasePage
        test_data = BasePage.get_test_data()  # Получаем данные для теста из метода get_test_data()

        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        feed_page = FeedPage(browser)

        # Логинимся с данными из test_data
        login_page.login(test_data["email"], test_data["password"])

        feed_page.open_feed()
        feed_page.click_constructor()
        feed_page.drag_and_drop_ingredient("Флюоресцентная булка R2-D3")
        feed_page.drag_and_drop_ingredient("Соус Spicy-X")
        feed_page.drag_and_drop_ingredient("Мясо бессмертных моллюсков Protostomia")
        feed_page.create_order()

        # Извлекаем номер заказа
        order_number = feed_page.extract_order_number()

        # Переходим в раздел с заказами и обновляем страницу
        personal_account_page.go_to_feed()

        # Проверяем, что заказ появился в разделе "В работе"
        is_in_progress = feed_page.is_order_in_progress(order_number)
        assert is_in_progress, f"Заказ {order_number} не найден в 'В работе' или имеет неправильный цвет"


@allure.feature("Лента заказов")
@allure.story("Проверка отображения заказов из истории")
class TestOrderHistoryInFeed:

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_orders_from_history_displayed_in_feed(self, browser):
        # Получаем данные из BasePage
        test_data = BasePage.get_test_data()  # Получаем данные для теста из метода get_test_data()

        login_page = LoginPage(browser)
        personal_account_page = PersonalAccountPage(browser)
        feed_page = FeedPage(browser)

        # Логинимся с данными из test_data
        login_page.login(test_data["email"], test_data["password"])

        feed_page.open_feed()
        feed_page.click_constructor()
        feed_page.drag_and_drop_ingredient("Флюоресцентная булка R2-D3")
        feed_page.drag_and_drop_ingredient("Соус Spicy-X")
        feed_page.drag_and_drop_ingredient("Мясо бессмертных моллюсков Protostomia")
        feed_page.create_order()

        # Извлекаем номер заказа
        order_number = feed_page.extract_order_number()

        # Переходим в раздел «История заказов»
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()

        # Проверяем, что заказ найден в истории
        order_found = feed_page.check_order_in_history(order_number)

        # Переходим в ленту заказов и ищем заказ
        personal_account_page.go_to_feed()
        order_found_in_feed = feed_page.find_order_in_feed(order_number)

        # Проверка, что заказ отображается в ленте заказов
        assert order_found_in_feed, f"Заказ {order_number} не найден в ленте заказов."











