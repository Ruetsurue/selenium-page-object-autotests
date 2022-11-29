from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket[type="submit"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_MSG = (By.CSS_SELECTOR, "#messages div.alert-success:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    PRODUCT_PRICE_IN_MSG = (By.CSS_SELECTOR, "#messages div.alert-info strong")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#messages div.alert-success")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_TEXT_ELEMENTS = (By.CSS_SELECTOR, ".page_inner #content_inner p")
