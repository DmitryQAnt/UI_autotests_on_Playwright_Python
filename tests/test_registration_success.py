"""
Successful user registration test
"""

import allure
from assertions.assertions import Assertions
from data.test_data import random_name, random_email, random_password, ORDER_IN_PROGRESS


@allure.feature("Successful user registration")
def test_login_success(main_page):
    with allure.step("Clicking the 'Login' button on the main page"):
        main_page.click_enter_button()

    with allure.step("Clicking the 'Register' button"):
        main_page.login_page.click_on_registration_button()

    with allure.step("Filling in the 'Name' field"):
        main_page.registration_page.set_name(random_name)

    with allure.step("Filling in the 'Login' field"):
        login = main_page.registration_page.set_login(random_email)

    with allure.step("Filling in the 'Password' field"):
        password = main_page.registration_page.set_password(random_password)

    with allure.step("Clicking the 'Register' button"):
        main_page.registration_page.click_registration_button()

    with allure.step("Waiting for registration confirmation"):
        main_page.wait(main_page.confirmation_button)

    with allure.step("Logging in after successful registration"):
        main_page.login_page.set_email_address(login)
        main_page.login_page.set_password(password)
        main_page.login_page.click_login_button()

    with allure.step('Checking that the "Start Order" button is present on the page'):
        Assertions.check_text(main_page.start_order_locator, ORDER_IN_PROGRESS)
