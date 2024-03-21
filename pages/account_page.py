from pages.base_page import BasePage
from pages.locators.account_locators_page import AccountLocatorPage


class AccountPage(BasePage):
    @property
    def logout_button(self):
        return self.login_container.locator("//button[text()='Выход']")

    @property
    def login_container(self):
        return self.page.locator("//div[@data-test-id='bla-bal']")

    def click_on_logout_button(self):
        self.click(self.logout_button)