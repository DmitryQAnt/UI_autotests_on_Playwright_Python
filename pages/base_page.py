

class BasePage:

    def __init__(self, page):
        self.page = page

    def find(self, locator):
        return self.page.locator(locator)

    def click(self, locator):
        self.find(locator).click()

    def set(self, locator, value):
        self.find(locator).fill(value)

    def drag_and_drop_element(self, draggable_locator, droppable_locator):
        self.page.drag_and_drop(draggable_locator, droppable_locator)

    def wait(self):
        self.page.wait_for_timeout(1000)