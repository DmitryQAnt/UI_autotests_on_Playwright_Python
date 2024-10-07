import allure
from assertions.assertions import Assertions
from data.test_data import random_name, random_email, random_password, ORDER_IN_PROGRESS


@allure.feature("Успешная регистрация пользователя")
def test_login_success(main_page):
    with allure.step("Нажимаем кнопку 'Войти' на главной странице"):
        main_page.click_enter_button()

    with allure.step("Нажимаем кнопку 'Зарегистрироваться'"):
        main_page.login_page.click_on_registration_button()

    with allure.step("Заполняем поле 'Имя'"):
        main_page.registration_page.set_name(random_name)

    with allure.step("Заполняем поле 'Логин'"):
        login = main_page.registration_page.set_login(random_email)

    with allure.step("Заполняем поле 'Пароль'"):
        password = main_page.registration_page.set_password(random_password)

    with allure.step("Нажимаем кнопку 'Зарегистрироваться'"):
        main_page.registration_page.click_registration_button()

    with allure.step("Ожидаем подтверждение успешной регистрации"):
        main_page.wait(main_page.confirmation_button)

    with allure.step("Выполняем вход после успешной регистрации"):
        main_page.login_page.set_email_address(login)
        main_page.login_page.set_password(password)
        main_page.login_page.click_login_button()

    with allure.step('Проверяем, что кнопка "Оформить заказ" присутствует на странице'):
        Assertions.check_text(main_page.start_order_locator, ORDER_IN_PROGRESS)

