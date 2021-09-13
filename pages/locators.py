from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "id_login-username")
    REGISTER_FORM = (By.ID, "id_registration-email")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_VALUE = (By.CLASS_NAME, 'basket-mini')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    BASKET_BOOK = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > .alertinner > strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '.btn-group > a.btn')


class BasketPageLocators:
    ITEM_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_PAGE_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
