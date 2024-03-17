import pytest
from playwright.sync_api import expect
import allure  # Добавлен импорт модуля allure

from assertions.assertions import Assertions
from data.test_data import TestData
from envconfig.envconfig import BrowserSet
from pages.locators.main_locators_page import MainLocatorsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage



class TestOrderInProgress(BrowserSet):
    @pytest.mark.usefixtures('browser_fixture')
    @allure.feature("Проверка начала выполнения заказа")
    def test_login_success(self, browser_fixture):
        main_page = MainPage(browser_fixture)
        main_page.click_enter_button()
        login_page = LoginPage(browser_fixture)
        login_page.set_email_address(TestData.valid_email)
        login_page.set_password(TestData.valid_password)
        login_page.click_login_button()
        main_page.click(MainLocatorsPage.START_ORDER)
        assertions = Assertions(browser_fixture)
        main_page.wait()
        with allure.step("Проверяем, что заказ начал готовиться"):
            assertions.check_text(MainLocatorsPage.CONFIRMATION_TEXT, TestData.ORDER_CONFIRMATION)

        with allure.step("Закрываем окно"):
            main_page.click(MainLocatorsPage.CLOSE_WINDOW)

        with allure.step("Проверяем, что заказ начал готовиться"):
            assertions.check_text(MainLocatorsPage.START_ORDER, TestData.ORDER_IN_PROGRESS)
