import allure
from assertions.assertions import Assertions
from data.test_data import valid_email, valid_password, ORDER_IN_PROGRESS


@allure.feature("Вход в систему")
@allure.story("Успешный вход в систему")
def test_login_success(main_page):
    with allure.step("Нажимаем кнопку 'Войти' на главной странице"):
        main_page.click_enter_button()

    with allure.step("Вводим адрес электронной почты"):
        main_page.login_page.set_email_address(valid_email)

    with allure.step("Вводим пароль"):
        main_page.login_page.set_password(valid_password)

    with allure.step("Нажимаем кнопку 'Войти' для авторизации"):
        main_page.login_page.click_login_button()

    with allure.step("Проверяем, что кнопка 'Оформить заказ' появилась"):
        Assertions.check_text(main_page.start_order_locator, ORDER_IN_PROGRESS)

