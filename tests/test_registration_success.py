import pytest
from playwright.sync_api import expect
import allure

from assertions.assertions import Assertions
from data.test_data import TestData
from envconfig.envconfig import BrowserSet
from pages.locators.main_locators_page import MainLocatorsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


class TestRegistrationSuccess(BrowserSet):
    @pytest.mark.usefixtures('browser_fixture')
    @allure.feature("Успешная регистрация пользователя")
    def test_login_success(self, browser_fixture):
        main_page = MainPage(browser_fixture)
        main_page.click_enter_button()
        login_page = LoginPage(browser_fixture)
        login_page.click_on_registration_button()
        registration_page = RegistrationPage(browser_fixture)
        registration_page.set_name(TestData.random_name)
        login = registration_page.set_login(TestData.random_email)
        password = registration_page.set_password(TestData.random_password)
        registration_page.click_registration_button()
        registration_page.wait()
        assertions = Assertions(browser_fixture)
        with allure.step("Логин после успешной регистрации"):
            login_page.set_email_address(login)
            login_page.set_password(password)
            login_page.click_login_button()

        with allure.step('Проверяем, что кнопка "Оформить заказ" присутствует на странице'):
            assertions.check_text(MainLocatorsPage.START_ORDER, TestData.ORDER_IN_PROGRESS)


