import pytest
import requests
from selenium import webdriver
from data import API
from helpers import Helpers
from page_objects.home_page import HomePage
from page_objects.list_order_page import ListOrderPage
from page_objects.password_recovery_page import PasswordRecoveryPage
from page_objects.private_office_page import PrivateOfficePage


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    web_driver.get("https://stellarburgers.nomoreparties.site/")

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def create_user():
    helpers = Helpers()
    user_date = helpers.generate_user_data()
    resp = requests.post(API.CREATE_USER, data=user_date)
    token = resp.json().get("accessToken")
    yield user_date, resp
    requests.delete(API.DELETE_DATA, headers={"Authorization": f'{token}'})


@pytest.fixture(scope='function')
def password_recovery(driver):
    password_recovery = PasswordRecoveryPage(driver)
    return password_recovery


@pytest.fixture(scope='function')
def private_office(driver):
    private_office = PrivateOfficePage(driver)
    return private_office


@pytest.fixture(scope='function')
def home(driver):
    home = HomePage(driver)
    return home


@pytest.fixture(scope='function')
def list_order(driver):
    list_order = ListOrderPage(driver)
    return list_order
