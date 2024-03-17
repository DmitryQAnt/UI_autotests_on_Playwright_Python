from pages.base_page import BasePage
from pages.locators.registration_locators_page import RegistrationLocatorsPage


class RegistrationPage(BasePage):

    def set_name(self, name):
        self.set(RegistrationLocatorsPage.REGISTRATION_NAME_FIELD, name)
        return name

    def set_login(self, login):
        self.set(RegistrationLocatorsPage.REGISTRATION_EMAIL_FIELD, login)
        return login

    def set_password(self, password):
        self.set(RegistrationLocatorsPage.REGISTRATION_PASSWORD_FIELD, password)
        return password

    def click_registration_button(self):
        self.click(RegistrationLocatorsPage.REGISTRATION_APPROVE_BUTTON)

    def wait_for_element(self):
        self.wait()