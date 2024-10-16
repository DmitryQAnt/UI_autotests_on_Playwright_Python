"""
This module provides test data and utility functions for generating random credentials
used in the automated testing of the Stellar Burgers application.
"""

import random
import string


def generate_random(length: int = 8) -> str:
    """
    Generates a random string of the specified length, consisting of letters and digits.

    :param length: The desired length of the random string (default is 8).

    :return: A randomly generated string containing uppercase/lowercase letters and digits.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# URL of the Stellar Burgers application
url = "https://stellarburgers.nomoreparties.site/"

# Predefined valid credentials for login tests
valid_email = "aDW6O3GS@mail.ru"
valid_password = "8F5qS733"

# Randomly generated credentials for registration tests
random_email = f'{generate_random()}@mail.ru'
random_password = generate_random()
random_name = f'Mit-{generate_random()}'

# Expected values and constants for test validation
EXPECTED_BURGER_PRICE = "9667"
ORDER_IN_PROGRESS = "Оформить заказ"
LOGIN_BUTTON = "Вход"
ORDER_CONFIRMATION = "Ваш заказ начали готовить"

# Timeouts for waiting in milliseconds
WAIT_5_SEC = 5000
WAIT_2_SEC = 2000
