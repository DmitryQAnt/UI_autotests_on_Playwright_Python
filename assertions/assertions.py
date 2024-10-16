from playwright.sync_api import expect
from playwright.sync_api import Locator


class Assertions:
    """
    A utility class that provides custom assertion methods for verifying the state of web elements.
    """

    def __init__(self, page):
        """
        Initializes the Assertions class with the given Playwright page object.

        :param page: The Playwright page object representing the current browser context.
        """
        self.page = page

    @classmethod
    def check_text(cls, locator: Locator, expected_text: str):
        """
        Verifies that the text content of the given locator matches the expected text.

        :param locator: The locator of the web element whose text content is being checked.
        :param expected_text: The expected text value that should be present in the locator.
        """
        expect(locator).to_have_text(expected_text)
