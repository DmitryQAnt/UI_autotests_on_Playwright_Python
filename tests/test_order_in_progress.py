"""
Order initiation check test
"""

import allure
from assertions.assertions import Assertions
from data.test_data import valid_email, valid_password, ORDER_CONFIRMATION, ORDER_IN_PROGRESS
from pages.locators.main_locators_page import MainLocatorsPage


@allure.feature("Order initiation check")
def test_login_success(main_page):
    with allure.step("Clicking the 'Login' button on the main page"):
        main_page.click_enter_button()

    with allure.step("Entering email address"):
        main_page.login_page.set_email_address(valid_email)

    with allure.step("Entering password"):
        main_page.login_page.set_password(valid_password)

    with allure.step("Clicking the 'Login' button to authorize"):
        main_page.login_page.click_login_button()

    with allure.step("Clicking the 'Start Order' button"):
        main_page.click(MainLocatorsPage.START_ORDER)

    with allure.step("Waiting for the order confirmation button"):
        main_page.wait(main_page.confirmation_button)

    with allure.step("Checking that the order has started processing"):
        Assertions.check_text(main_page.confirmation_button, ORDER_CONFIRMATION)

    with allure.step("Closing the order confirmation window"):
        main_page.click(MainLocatorsPage.CLOSE_WINDOW)

    with allure.step("Checking that the order is in progress"):
        Assertions.check_text(main_page.start_order_locator, ORDER_IN_PROGRESS)
