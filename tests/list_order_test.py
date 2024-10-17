import allure


class TestListOrderPage:

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    @allure.description("Проверяем что заказы пользака отображаются")
    def test_visible_user_order_in_list_order(self, list_order, private_office, create_user, password_recovery):

        number = private_office.auth_and_change_order(create_user, password_recovery)
        number = '#0' + number[-1]
        list_order.tap_on_order_list_button()
        order_texts = list_order.return_all_order_text()

        assert number in order_texts

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.description("Проверяем работу счетчика выполненных за все время заказов")
    def test_check_completed_orders_all_day_indicator(self, list_order, private_office, create_user, password_recovery):

        list_order.tap_on_order_list_button()
        old_nuber_orders = list_order.check_completed_orders_all_time()
        private_office.auth_and_change_order(create_user, password_recovery)
        list_order.tap_on_order_list_button()
        yang_nuber_orders = list_order.check_completed_orders_all_time()

        assert int(yang_nuber_orders) > int(old_nuber_orders)

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    @allure.description("Проверяем работу счетчика выполненных за сегодня заказов ")
    def test_check_completed_orders_today_indicator(self, list_order, private_office, create_user, password_recovery):

        list_order.tap_on_order_list_button()
        old_nuber_orders = list_order.check_completed_orders_today()
        private_office.auth_and_change_order(create_user, password_recovery)
        list_order.tap_on_order_list_button()
        yang_nuber_orders = list_order.check_completed_orders_today()

        assert int(yang_nuber_orders) > int(old_nuber_orders)

    @allure.title("После оформления заказа его номер появляется в разделе В работе.")
    @allure.description("Проверяем работу раздела готовящихся заказов")
    def test_check_create_order_progress_section(self, list_order, private_office, create_user, password_recovery):

        number = private_office.auth_and_change_order(create_user, password_recovery)
        number = '0' + number[-1]
        list_order.tap_on_order_list_button()
        list_order.return_all_order_text()
        data_orders = list_order.check_order_progress_section()

        assert number in data_orders
