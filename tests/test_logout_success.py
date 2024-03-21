import pytest
from playwright.sync_api import expect
import allure  # Добавлен импорт модуля allure
from envconfig.envconfig import BrowserSet
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from assertions.assertions import Assertions
from pages.locators.login_locators_page import LoginLocatorsPage


class TestLogoutSuccessful(BrowserSet):
    @pytest.mark.usefixtures('browser_fixture')
    @allure.feature("Выход из системы")
    @allure.story("Успешный выход из системы")
    def test_logout_success(self, browser_fixture):
        main_page = MainPage(browser_fixture)
        main_page.click_enter_button()
        login_page = LoginPage(browser_fixture)
        login_page.set_email_address(TestData.valid_email)
        login_page.set_password(TestData.valid_password)
        login_page.click_login_button()
        main_page.click_on_account_button()
        account_page = AccountPage(browser_fixture)
        account_page.click_on_logout_button()
        assertions = Assertions(browser_fixture)
        with allure.step('Проверяем, что кнопка "Оформить заказ" появилась'):
            assertions.check_text(LoginLocatorsPage.TEXT_CONFIRMATION, TestData.LOGIN_BUTTON)
