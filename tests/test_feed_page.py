from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from page_objects.order_history_page import OrderHistoryPage
from page_objects.account_page import AccountPage
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_displaying_modal_order_details_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        feed_page.click_on_order_card()
        assert 'бургер' in feed_page.get_text_on_title_of_modal_order()

    @allure.title('Проверка отображения существующего заказа из истории пользователя в ленте')
    def test_displaying_in_feed_new_order_from_history_success(self, driver, create_user_and_order_and_delete,
                                                               set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.click_on_order_history_button()
        order_id = order_history_page.get_id_of_order_card()
        main_page.click_header_feed_button()
        assert feed_page.check_id_order_in_feed(order_id)

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_quantity_of_orders()
        main_page.click_on_button_constructor()
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_daily_quantity_of_orders()
        main_page.click_on_button_constructor()
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_daily_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    def test_displaying_new_order_in_progress_feed_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        new_order_id = main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        assert feed_page.get_order_number_in_feed_progress_section() == '0'+new_order_id
