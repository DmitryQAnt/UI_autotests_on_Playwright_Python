from pages.base_page import BasePage
from pages.locators.login_locators_page import LoginLocatorsPage


class LoginPage(BasePage):

    def set_email_address(self, email_address):
        self.set(LoginLocatorsPage.LOGIN_FIELD, email_address)

    def set_password(self, password):
        self.set(LoginLocatorsPage.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(LoginLocatorsPage.FINAL_LOGIN_BUTTON)

    def click_on_registration_button(self):
        self.click(LoginLocatorsPage.REGISTRATION_BUTTON_LOGIN_PAGE)
