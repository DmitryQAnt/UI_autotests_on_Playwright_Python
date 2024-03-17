import pytest
from playwright.sync_api import expect
import allure

from assertions.assertions import Assertions
from data.test_data import TestData
from envconfig.envconfig import BrowserSet
from pages.locators.main_locators_page import MainLocatorsPage
from pages.main_page import MainPage


class TestBurgerConstructor(BrowserSet):
    @pytest.mark.usefixtures('browser_fixture')
    @allure.title("Собираем бургер(проверка на Драг энд дроп)")
    def test_burger_construction_is_ok(self, browser_fixture):
        main_page = MainPage(browser_fixture)
        with allure.step("Берем булки"):
            main_page.drag_buns_to_basket()
        with allure.step("Соус"):
            main_page.drag_sauce_to_basket()
        with allure.step("Сыр"):
            main_page.drag_cheese_to_basket()
        with allure.step("Котлетос"):
            main_page.drag_fillings_to_basket()
        assertions = Assertions(browser_fixture)
        with allure.step("Смотрим, что цена соответствует ожидаемой"):
            assertions.check_text(MainLocatorsPage.PRICE_COUNTER, TestData.EXPECTED_BURGER_PRICE)