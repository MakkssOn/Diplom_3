# api.py
import random
import string
import allure

class API:
    @staticmethod
    @allure.title("Generate user data")
    def generate_user_data():
        email = API.generate_random_string(6) + '@yandex.ru'
        password = API.generate_random_string(10)
        name = API.generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    @staticmethod
    @allure.title("Create orders")
    def created_orders(resp):
        # Здесь должна быть логика метода created_orders
        pass

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for _ in range(length))
        return random_string
