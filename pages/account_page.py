from pages.base_page import BasePage
from pages.locators.account_locators_page import AccountLocatorPage


class AccountPage(BasePage):
    def click_on_logout_button(self):
        self.click(AccountLocatorPage.LOG_OUT)