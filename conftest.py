import pytest
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from typing import Generator, Union
from selenium.webdriver.remote.webdriver import WebDriver


# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class WebDriverFactory:
    """Фабрика для создания экземпляров WebDriver с поддержкой разных браузеров."""
    
    @staticmethod
    def get_webdriver(browser_name: str) -> WebDriver:
        """
        Создает и возвращает экземпляр WebDriver для указанного браузера.
        
        Args:
            browser_name: Имя браузера ('chrome' или 'firefox')
            
        Returns:
            Экземпляр WebDriver
            
        Raises:
            ValueError: Если передан неподдерживаемый браузер
            WebDriverException: Если возникла проблема при инициализации драйвера
        """
        browser_name = browser_name.lower()
        
        try:
            if browser_name == 'firefox':
                service = FirefoxService(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=service)
            elif browser_name == 'chrome':
                service = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service)
            else:
                raise ValueError(f"Browser '{browser_name}' is not supported. Use 'chrome' or 'firefox'")
            
            return driver
        except Exception as e:
            raise RuntimeError(f"Failed to initialize {browser_name} driver: {str(e)}")


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    """
    Фикстура для инициализации и завершения работы WebDriver.
    
    Поддерживает параметризацию через pytest.mark.parametrize или --browser.
    По умолчанию использует chrome.
    """
    # Получаем имя браузера из параметра теста или из командной строки
    browser_name = getattr(request, "param", None) or request.config.getoption("--browser")
    
    driver = WebDriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    
    yield driver
    
    # Завершение работы драйвера
    try:
        driver.quit()
    except Exception as e:
        print(f"Warning: Failed to properly quit driver: {str(e)}")


def pytest_addoption(parser: pytest.Parser) -> None:
    """Добавляем кастомные параметры командной строки для pytest."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests (chrome or firefox)",
        choices=["chrome", "firefox"]
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


@pytest.fixture(scope="session", autouse=True)
def setup_environment() -> None:
    """Общая настройка окружения перед запуском тестов."""
    # Здесь можно добавить общие настройки
    pass