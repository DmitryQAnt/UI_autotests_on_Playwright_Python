from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators.main_locators_page import MainLocatorsPage


class MainPage(BasePage):

    def __init__(self, page: Page, login_page, account_page, registration_page):
        self.page = page
        self.account_page = account_page
        self.login_page = login_page
        self.registration_page = registration_page

    @property
    def price_counter_locator(self):
        return self.page.locator(MainLocatorsPage.PRICE_COUNTER)

    @property
    def start_order_locator(self):
        return self.page.locator(MainLocatorsPage.START_ORDER)

    @property
    def confirmation_button(self):
        return self.page.locator(MainLocatorsPage.CONFIRMATION_TEXT)

    def click_enter_button(self):
        self.click(MainLocatorsPage.ACCOUNT_LINK_BUTTON)

    def click_on_account_button(self):
        self.click(MainLocatorsPage.ACCOUNT_LINK_BUTTON)

    def drag_buns_to_basket(self):
        self.drag_and_drop_element(MainLocatorsPage.CRATOR_BUN, MainLocatorsPage.BASCKET_AREA)

    def drag_sauce_to_basket(self):
        self.drag_and_drop_element(MainLocatorsPage.TRADITIONAL_SAUCE, MainLocatorsPage.BASCKET_AREA)

    def drag_fillings_to_basket(self):
        self.drag_and_drop_element(MainLocatorsPage.METEORIT, MainLocatorsPage.BASCKET_AREA)

    def drag_cheese_to_basket(self):
        self.drag_and_drop_element(MainLocatorsPage.CHEESE, MainLocatorsPage.BASCKET_AREA)
