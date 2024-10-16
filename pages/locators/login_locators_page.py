"""
This module contains locators for the elements present on the login page of the web application.
"""


class LoginLocatorsPage:
    """
    A class containing locators for elements on the login page.
    """

    REGISTRATION_BUTTON_LOGIN_PAGE = (
        "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']"
    )
    LOGIN_FIELD = 'input[name="name"]'
    PASSWORD_FIELD = 'input[name="Пароль"]'
    FINAL_LOGIN_BUTTON = (
        "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
        "button_button_size_medium__3zxIa' and text()='Войти']"
    )
    LINK_RECOVERY_PASSWORD = (
        "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
    )
    TEXT_CONFIRMATION = "//h2[text()='Вход']"
