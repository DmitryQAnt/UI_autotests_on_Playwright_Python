"""
Burger construction test
"""

import allure
from assertions.assertions import Assertions
from data.test_data import EXPECTED_BURGER_PRICE


@allure.feature("Burger Construction (Drag and Drop test)")
def test_burger_construction_is_ok(main_page):
    with allure.step("Picking the buns"):
        main_page.drag_buns_to_basket()

    with allure.step("Adding sauce"):
        main_page.drag_sauce_to_basket()

    with allure.step("Adding cheese"):
        main_page.drag_cheese_to_basket()

    with allure.step("Adding cutlet"):
        main_page.drag_fillings_to_basket()

    with allure.step("Verifying the total price matches the expected value"):
        Assertions.check_text(main_page.price_counter_locator, EXPECTED_BURGER_PRICE)
