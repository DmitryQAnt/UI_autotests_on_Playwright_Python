from playwright.sync_api import expect

class Assertions:

    def __init__(self, page):
        self.page = page

    @classmethod
    def check_text(cls, locator, expected_text):
        # element = self.page.locator(locator)
        # actual_text = element.inner_text()
        # assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"

        expect(locator).to_have_text(expected_text)

    # def check(self, locator):
    #     self.page.expect(locator)
#
#     def check_login_success(self):
#         button_locator = self.page.locator("[role='button']").first()
        # button_locator.expect().to_have_text("Оформить заказ")
        # self.page.expect(self.page.get_by_role("button", name="Оформить заказ")).to_have_text("Оформить заказ")

