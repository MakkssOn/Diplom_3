import random
import string
import requests

from data import Ingredients, API


class Helpers:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_user_data():
        email = Helpers.generate_random_string(6) + '@yandex.ru'
        password = Helpers.generate_random_string(10)
        name = Helpers.generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload

    def created_orders(self, resp):
        token = resp.json().get("accessToken")
        ingredients = {
            "ingredients": [Ingredients.BUN, Ingredients.KOKLETA, Ingredients.MEAT]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response_created = requests.post(API.CREATE_ORDER, headers=headers, json=ingredients)
        return response_created
