
class MainLocatorsPage:

    # Main fields and buttons
    ACCOUNT_LINK_BUTTON = "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
    LOGIN_BUTTON = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Войти в аккаунт']"
    FILLINGS_BUTTON = ".tab_tab__1SPyG:nth-child(3)"
    SAUCES_BUTTON = ".tab_tab__1SPyG:nth-child(2)"
    BUNS_BUTTON = ".tab_tab__1SPyG:nth-child(1)"
    BASCKET_AREA = ".BurgerConstructor_basket__list__l9dp_"
    PRICE_COUNTER = '//p[@class="text text_type_digits-medium mr-3"]'

    # Burger
    CRATOR_BUN = "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[2]"
    TRADITIONAL_SAUCE = "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[3]"
    METEORIT = '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]'
    CHEESE = '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa7a"]'

    # Order window
    ORDER_WINDOW = "Modal_modal__contentBox__sCy8X pt-30 pb-30"
    START_ORDER = "//button[text()='Оформить заказ']"
    CONFIRMATION_TEXT = "//p[@class='undefined text text_type_main-small mb-2']"
    CLOSE_WINDOW = '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
