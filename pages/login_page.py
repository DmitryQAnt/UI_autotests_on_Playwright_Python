"""
This module defines the LoginPage class, which provides methods to interact with the login page of the application.
"""

from pages.base_page import BasePage
from playwright.sync_api import Locator
from pages.locators.login_locators_page import LoginLocatorsPage


class LoginPage(BasePage):
    """
    The LoginPage class encapsulates the behavior and interactions of the login page.
    It includes methods for setting user credentials and handling the login process.
    """

    @property
    def login_button_locator(self) -> Locator:
        """
        Returns the locator for the login confirmation text after a successful login.

        :return: Playwright Locator for the login confirmation text.
        """
        return self.page.locator(LoginLocatorsPage.TEXT_CONFIRMATION)

    def set_email_address(self, email_address: str) -> None:
        """
        Fills the email field with the provided email address.

        :param email_address: The email address to be entered into the login field.
        """
        self.set(LoginLocatorsPage.LOGIN_FIELD, email_address)

    def set_password(self, password: str) -> None:
        """
        Fills the password field with the provided password.

        :param password: The password to be entered into the password field.
        """
        self.set(LoginLocatorsPage.PASSWORD_FIELD, password)

    def click_login_button(self) -> None:
        """
        Clicks on the final login button to attempt user authentication.
        """
        self.click(LoginLocatorsPage.FINAL_LOGIN_BUTTON)

    def click_on_registration_button(self) -> None:
        """
        Clicks on the registration button located on the login page.
        """
        self.click(LoginLocatorsPage.REGISTRATION_BUTTON_LOGIN_PAGE)
