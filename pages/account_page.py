from pages.base_page import BasePage
from pages.locators.account_locators_page import AccountLocatorPage


class AccountPage(BasePage):
    @property
    def logout_button(self):
        return AccountLocatorPage.LOG_OUT

    def click_on_logout_button(self):
        self.click(self.logout_button)
