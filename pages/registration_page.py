"""
This module defines the RegistrationPage class, which provides methods to interact with the registration page of the application.
"""

from pages.base_page import BasePage
from pages.locators.registration_locators_page import RegistrationLocatorsPage


class RegistrationPage(BasePage):
    """
    The RegistrationPage class encapsulates the behavior and interactions of the user registration page.
    It includes methods for setting user details and submitting the registration form.
    """

    def set_name(self, name: str) -> str:
        """
        Fills the 'Name' field with the provided name.

        :param name: The name to be entered into the 'Name' field.
        :return: The name that was entered.
        """
        self.set(RegistrationLocatorsPage.REGISTRATION_NAME_FIELD, name)
        return name

    def set_login(self, login: str) -> str:
        """
        Fills the 'Login' field with the provided email address.

        :param login: The email address to be entered into the 'Login' field.
        :return: The email address that was entered.
        """
        self.set(RegistrationLocatorsPage.REGISTRATION_EMAIL_FIELD, login)
        return login

    def set_password(self, password: str) -> str:
        """
        Fills the 'Password' field with the provided password.

        :param password: The password to be entered into the 'Password' field.
        :return: The password that was entered.
        """
        self.set(RegistrationLocatorsPage.REGISTRATION_PASSWORD_FIELD, password)
        return password

    def click_registration_button(self) -> None:
        """
        Clicks the button to submit the registration form.
        """
        self.click(RegistrationLocatorsPage.REGISTRATION_APPROVE_BUTTON)
