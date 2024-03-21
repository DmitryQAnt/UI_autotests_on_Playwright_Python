from playwright.sync_api import Locator, TimeoutError as PlaywrightTimeoutError, Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def find(self, selector):
        return self.page.locator(selector)

    def click(self, locator):
        self.find(locator).click()

    def set(self, locator, value):
        self.find(locator).fill(value)

    def drag_and_drop_element(self, draggable_locator, droppable_locator):
        self.page.drag_and_drop(draggable_locator, droppable_locator)

    def wait(self, locator: Locator, timeout: int = 5000):
        try:
            locator.wait_for(timeout=timeout)
        except PlaywrightTimeoutError:
            pass
