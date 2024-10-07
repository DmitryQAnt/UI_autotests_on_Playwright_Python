import allure
from assertions.assertions import Assertions
from data.test_data import EXPECTED_BURGER_PRICE


@allure.title("Собираем бургер(проверка на Драг энд дроп)")
def test_burger_construction_is_ok(main_page):
    with allure.step("Берем булки"):
        main_page.drag_buns_to_basket()

    with allure.step("Соус"):
        main_page.drag_sauce_to_basket()

    with allure.step("Сыр"):
        main_page.drag_cheese_to_basket()

    with allure.step("Котлетос"):
        main_page.drag_fillings_to_basket()

    with allure.step("Смотрим, что цена соответствует ожидаемой"):
        Assertions.check_text(main_page.price_counter_locator, EXPECTED_BURGER_PRICE)
