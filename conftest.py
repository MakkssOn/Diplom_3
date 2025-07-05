import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from driver_factory import WebDriverFactory

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = WebDriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use for tests"
    )
