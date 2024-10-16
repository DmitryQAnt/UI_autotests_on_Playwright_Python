"""
This module provides a base class for page object models to encapsulate basic browser interactions.
"""

from playwright.sync_api import Locator, TimeoutError as PlaywrightTimeoutError, Page


class BasePage:
    """
    A base page class that includes common actions for interacting with web pages using Playwright.
    """

    def __init__(self, page: Page):
        """
        Initializes the BasePage with a Playwright Page instance.

        :param page: Playwright Page object representing the web page.
        """
        self.page = page

    def find(self, selector) -> Locator:
        """
        Finds an element on the page using a locator.

        :param selector: A string representing the locator of the element to find.
        :return: Playwright Locator object representing the found element.
        """
        return self.page.locator(selector)

    def click(self, locator) -> None:
        """
        Clicks on an element located by the provided locator.

        :param locator: A string representing the locator of the element to click.
        """
        self.find(locator).click()

    def set(self, locator, value: str) -> None:
        """
        Sets the value of an input field located by the provided locator.

        :param locator: A string representing the locator of the input field.
        :param value: A string representing the value to set in the input field.
        """
        self.find(locator).fill(value)

    def drag_and_drop_element(self, draggable_locator, droppable_locator) -> None:
        """
        Drags an element from one location and drops it into another.

        :param draggable_locator: A string representing the locator of the element to drag.
        :param droppable_locator: A string representing the locator of the target element where the draggable will be dropped.
        """
        self.page.drag_and_drop(draggable_locator, droppable_locator)

    def wait(self, locator: Locator, timeout: int = 5000) -> None:
        """
        Waits for an element to appear on the page within the given timeout.

        :param locator: Playwright Locator object representing the element to wait for.
        :param timeout: An optional integer representing the timeout in milliseconds (default is 5000ms).
        :raises PlaywrightTimeoutError: If the element is not found within the timeout period.
        """
        try:
            locator.wait_for(timeout=timeout)
        except PlaywrightTimeoutError:
            pass
