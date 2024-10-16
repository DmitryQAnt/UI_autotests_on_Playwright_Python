"""
Successful login test
"""

import allure
from assertions.assertions import Assertions
from data.test_data import valid_email, valid_password, ORDER_IN_PROGRESS


@allure.feature("Successful Login")
def test_login_success(main_page):
    with allure.step("Clicking the 'Login' button on the main page"):
        main_page.click_enter_button()

    with allure.step("Entering email address"):
        main_page.login_page.set_email_address(valid_email)

    with allure.step("Entering password"):
        main_page.login_page.set_password(valid_password)

    with allure.step("Clicking the 'Login' button to authorize"):
        main_page.login_page.click_login_button()

    with allure.step("Checking that the 'Start Order' button appears"):
        Assertions.check_text(main_page.start_order_locator, ORDER_IN_PROGRESS)
