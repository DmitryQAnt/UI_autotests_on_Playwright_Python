import random
import string


def generate_random(length: int = 8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


url = "https://stellarburgers.nomoreparties.site/"
valid_email = "aDW6O3GS@mail.ru"
valid_password = "8F5qS733"

random_email = f'{generate_random()}@mail.ru'
random_password = f'{generate_random()}'
random_name = f'Mit-{generate_random()}'

EXPECTED_BURGER_PRICE = "9667"
ORDER_IN_PROGRESS = "Оформить заказ"
LOGIN_BUTTON = "Вход"
ORDER_CONFIRMATION = "Ваш заказ начали готовить"
WAIT_5_SEC = 5000
WAIT_2_SEC = 2000
