import allure
from assertions.assertions import Assertions
from data.test_data import valid_email, valid_password, ORDER_CONFIRMATION, ORDER_IN_PROGRESS
from pages.locators.main_locators_page import MainLocatorsPage


@allure.feature("Проверка начала выполнения заказа")
def test_login_success(main_page):
    with allure.step("Нажимаем кнопку 'Войти' на главной странице"):
        main_page.click_enter_button()

    with allure.step("Вводим адрес электронной почты"):
        main_page.login_page.set_email_address(valid_email)

    with allure.step("Вводим пароль"):
        main_page.login_page.set_password(valid_password)

    with allure.step("Нажимаем кнопку 'Войти' для авторизации"):
        main_page.login_page.click_login_button()

    with allure.step("Нажимаем кнопку 'Начать заказ'"):
        main_page.click(MainLocatorsPage.START_ORDER)

    with allure.step("Ожидаем кнопку подтверждения заказа"):
        main_page.wait(main_page.confirmation_button)

    with allure.step("Проверяем, что заказ начал готовиться"):
        Assertions.check_text(main_page.confirmation_button, ORDER_CONFIRMATION)

    with allure.step("Закрываем окно подтверждения заказа"):
        main_page.click(MainLocatorsPage.CLOSE_WINDOW)

    with allure.step("Проверяем, что заказ находится в процессе выполнения"):
        Assertions.check_text(main_page.start_order_locator, ORDER_IN_PROGRESS)

