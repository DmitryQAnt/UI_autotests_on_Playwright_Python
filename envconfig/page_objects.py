"""
This module contains common pytest fixtures for initializing page objects.
The fixtures are used to create instances of Page Object Model (POM) classes for use in tests.
"""

import pytest
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def main_page(start_page, login_page, account_page, registration_page):
    """
    Fixture for creating a MainPage instance with dependencies on LoginPage, AccountPage, and RegistrationPage.

    :param start_page: The initialized browser page object.
    :param login_page: The LoginPage fixture.
    :param account_page: The AccountPage fixture.
    :param registration_page: The RegistrationPage fixture.

    :return: An instance of MainPage.
    """
    return MainPage(page=start_page, login_page=login_page, account_page=account_page,
                    registration_page=registration_page)


@pytest.fixture(scope="function")
def login_page(start_page):
    """
    Fixture for creating a LoginPage instance.

    :param start_page: The initialized browser page object.

    :return: An instance of LoginPage.
    """
    return LoginPage(page=start_page)


@pytest.fixture(scope="function")
def account_page(start_page):
    """
    Fixture for creating an AccountPage instance.

    :param start_page: The initialized browser page object.

    :return: An instance of AccountPage.
    """
    return AccountPage(page=start_page)


@pytest.fixture(scope="function")
def registration_page(start_page):
    """
    Fixture for creating a RegistrationPage instance.

    :param start_page: The initialized browser page object.

    :return: An instance of RegistrationPage.
    """
    return RegistrationPage(page=start_page)
