from playwright.sync_api import expect


class Assertions:

    def __init__(self, page):
        self.page = page

    @classmethod
    def check_text(cls, locator, expected_text):

        expect(locator).to_have_text(expected_text)
