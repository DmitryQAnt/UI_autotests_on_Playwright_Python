"""
This module defines the AccountPage class, which provides methods to interact with the account page, including the logout functionality.
"""

from pages.base_page import BasePage
from playwright.sync_api import Locator
from pages.locators.account_locators_page import AccountLocatorPage


class AccountPage(BasePage):
    """
    The AccountPage class encapsulates the behavior and interactions of the user account page.
    It includes methods for logging out and accessing key account-related elements.
    """

    @property
    def logout_button(self) -> Locator:
        """
        A property that returns the locator for the 'Logout' button.

        :return: A Locator object for the 'Logout' button.
        """
        return AccountLocatorPage.LOG_OUT

    def click_on_logout_button(self) -> None:
        """
        Clicks the 'Logout' button on the account page to log the user out.
        """
        self.click(self.logout_button)
