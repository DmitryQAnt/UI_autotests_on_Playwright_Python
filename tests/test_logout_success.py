import allure
from assertions.assertions import Assertions
from data.test_data import valid_email, valid_password, LOGIN_BUTTON


@allure.feature("Выход из системы")
@allure.story("Успешный выход из системы")
def test_logout_success(main_page):
    with allure.step("Нажимаем кнопку 'Войти' на главной странице"):
        main_page.click_enter_button()

    with allure.step("Вводим адрес электронной почты"):
        main_page.login_page.set_email_address(valid_email)

    with allure.step("Вводим пароль"):
        main_page.login_page.set_password(valid_password)

    with allure.step("Нажимаем кнопку 'Войти' для авторизации"):
        main_page.login_page.click_login_button()

    with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
        main_page.click_on_account_button()

    with allure.step("Нажимаем на кнопку 'Выход'"):
        main_page.account_page.click_on_logout_button()

    with allure.step("Проверяем, что кнопка 'Войти' появилась"):
        Assertions.check_text(main_page.login_page.login_button_locator, LOGIN_BUTTON)

