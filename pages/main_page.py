from pages.base_page import BasePage
from pages.locators.main_locators_page import MainLocatorsPage


class MainPage(BasePage):

    def __init__(self):
        self.__test = None

    @property
    def buttons(self):
        return self.page.locator('.tab_tab__1SPyG')

    def button_bulki(self):
        return self.buttons.filter(has=self.page.locator('//*[contains(text(), \'Булки\')]')).first


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

