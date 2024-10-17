from selenium.webdriver.common.by import By


class PersonalAccount:

    """Текст кнопки Личный Кабинет на главной странице"""
    MY_OFFICE = (By.XPATH, './/a[@class="AppHeader_header__link__3D_hX"]/p[text() ="Личный Кабинет"]')

    """Хедер блока входа с текстом 'Вход' """
    LOGIN_HEADER_IN_MY_OFFICE = (By.XPATH, './/h2[text() = "Вход"]')

    """Кнопка-гиперссылка 'Восстановить пароль' на страничке регистрации пользователя """
    RECOVERY_PASS_LINK_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')

    """Хедер странички Восстановления пароля"""
    RECOVERY_PASS_HEADER = (By.XPATH, '//h2[text()="Восстановление пароля" ]')

    """Кнопка 'Восстановить' """
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    """Поле ввода для пароля """
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    """Поле ввода для эмейла """
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")

    """Иконка глаза рядом с полем ввода пароля"""
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")

    """Статус видимости у поля с паролем"""
    VISIBLE_PASS_INPUT = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
