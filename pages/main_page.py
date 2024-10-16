"""
This module defines the MainPage class, which provides methods to interact with the main page of the web app.
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from pages.locators.main_locators_page import MainLocatorsPage


class MainPage(BasePage):
    """
    The MainPage class encapsulates the behavior and interactions of the main page.
    It includes methods for interacting with various elements like buttons and performing actions such as drag-and-drop.
    """

    def __init__(self, page: Page, login_page, account_page, registration_page):
        """
        Initializes the MainPage with references to its subpages (login, account, and registration).

        :param page: Playwright Page object representing the web page.
        :param login_page: LoginPage object representing the login page.
        :param account_page: AccountPage object representing the account page.
        :param registration_page: RegistrationPage object representing the registration page.
        """
        self.page = page
        self.login_page = login_page
        self.account_page = account_page
        self.registration_page = registration_page

    @property
    def price_counter_locator(self) -> Locator:
        """
        Returns the locator for the price counter element.

        :return: Playwright Locator for the price counter.
        """
        return self.page.locator(MainLocatorsPage.PRICE_COUNTER)

    @property
    def start_order_locator(self) -> Locator:
        """
        Returns the locator for the 'Start Order' button.

        :return: Playwright Locator for the 'Start Order' button.
        """
        return self.page.locator(MainLocatorsPage.START_ORDER)

    @property
    def confirmation_button(self) -> Locator:
        """
        Returns the locator for the confirmation button after placing an order.

        :return: Playwright Locator for the confirmation button.
        """
        return self.page.locator(MainLocatorsPage.CONFIRMATION_TEXT)

    def click_enter_button(self) -> None:
        """
        Clicks on the 'Enter' button on the main page.
        """
        self.click(MainLocatorsPage.ACCOUNT_LINK_BUTTON)

    def click_on_account_button(self) -> None:
        """
        Clicks on the 'Account' button to access the account page.
        """
        self.click(MainLocatorsPage.ACCOUNT_LINK_BUTTON)

    def drag_buns_to_basket(self) -> None:
        """
        Drags the bun element into the basket area.
        """
        self.drag_and_drop_element(MainLocatorsPage.CRATOR_BUN, MainLocatorsPage.BASCKET_AREA)

    def drag_sauce_to_basket(self) -> None:
        """
        Drags the sauce element into the basket area.
        """
        self.drag_and_drop_element(MainLocatorsPage.TRADITIONAL_SAUCE, MainLocatorsPage.BASCKET_AREA)

    def drag_fillings_to_basket(self) -> None:
        """
        Drags the fillings element into the basket area.
        """
        self.drag_and_drop_element(MainLocatorsPage.METEORIT, MainLocatorsPage.BASCKET_AREA)

    def drag_cheese_to_basket(self) -> None:
        """
        Drags the cheese element into the basket area.
        """
        self.drag_and_drop_element(MainLocatorsPage.CHEESE, MainLocatorsPage.BASCKET_AREA)
