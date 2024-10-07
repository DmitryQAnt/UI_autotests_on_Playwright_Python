# Общие ПОМы
import pytest

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def main_page(start_page, login_page, account_page, registration_page):
    return MainPage(page=start_page, login_page=login_page, account_page=account_page,
                    registration_page=registration_page)


@pytest.fixture(scope="function")
def login_page(start_page):
    return LoginPage(page=start_page)


@pytest.fixture(scope="function")
def account_page(start_page):
    return AccountPage(page=start_page)


@pytest.fixture(scope="function")
def registration_page(start_page):
    return RegistrationPage(page=start_page)
