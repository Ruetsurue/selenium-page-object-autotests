from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK_LOCATOR = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket[type="submit"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_MSG = (By.CSS_SELECTOR, "#messages div.alert-success:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    PRODUCT_PRICE_IN_MSG = (By.CSS_SELECTOR, "#messages div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success")
