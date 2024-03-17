
class RegistrationLocatorsPage:
    REGISTRATION_APPROVE_BUTTON = "//button[text()='Зарегистрироваться']"
    REGISTRATION_PASSWORD_FIELD = "//fieldset[3]/div/div/input"
    REGISTRATION_EMAIL_FIELD = "//fieldset[2]/div/div/input"
    REGISTRATION_NAME_FIELD = "//fieldset[1]/div/div/input"
    CONFIRMATION_REGISTRATION_FIELD = "//h2[text()='Вход']"
    INCORRECT_PASSWORD_ALERT = "//p[@class='input__error text_type_main-default']"
    LINK_TO_LOGIN_PAGE = "//a[text()='Войти']"