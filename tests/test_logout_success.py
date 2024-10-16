"""
Successful Logout test
"""

import allure
from assertions.assertions import Assertions
from data.test_data import valid_email, valid_password, LOGIN_BUTTON


@allure.feature("Successful Logout")
def test_logout_success(main_page):
    with allure.step("Clicking the 'Login' button on the main page"):
        main_page.click_enter_button()

    with allure.step("Entering email address"):
        main_page.login_page.set_email_address(valid_email)

    with allure.step("Entering password"):
        main_page.login_page.set_password(valid_password)

    with allure.step("Clicking the 'Login' button to authorize"):
        main_page.login_page.click_login_button()

    with allure.step("Clicking the 'Account' button"):
        main_page.click_on_account_button()

    with allure.step("Clicking the 'Logout' button"):
        main_page.account_page.click_on_logout_button()

    with allure.step("Checking that the 'Login' button appears"):
        Assertions.check_text(main_page.login_page.login_button_locator, LOGIN_BUTTON)
