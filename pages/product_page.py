from .base_page import BasePage
from .locators import ProductPageLocators as ppl
from selenium.webdriver.support.ui import WebDriverWait

PRODUCT_PAGE_EXPLICIT_TIMEOUT = 4

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ppl.ADD_PRODUCT_BUTTON).click()

    def get_product_name(self):
        product_name_on_page = self.browser.find_element(*ppl.PRODUCT_NAME).text
        return product_name_on_page

    def get_product_price(self):
        product_price_on_page = self.browser.find_element(*ppl.PRODUCT_PRICE).text
        return product_price_on_page

    def should_be_added_to_basket_messages(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        self.should_be_product_name_message(product_name_on_page=product_name)
        self.should_be_basket_price(product_price_on_page=product_price)

    def should_be_product_name_message(self, product_name_on_page):
        self.is_element_present(*ppl.PRODUCT_NAME_IN_MSG)
        product_name_in_basket = self.browser.find_element(*ppl.PRODUCT_NAME_IN_MSG).text
        error_msg = f"Product name on page and in basket-add notification do not match" \
                    f"\nExpected: '{product_name_on_page}', got: '{product_name_in_basket}'"
        assert product_name_on_page == product_name_in_basket, error_msg

    def should_be_basket_price(self, product_price_on_page):
        self.is_element_present(*ppl.PRODUCT_PRICE_IN_MSG)
        product_price_in_msg = self.browser.find_element(*ppl.PRODUCT_PRICE_IN_MSG).text
        error_msg = f"Product price on page and in basket-add notification do not match" \
                    f"\nExpected: '{product_price_on_page}', got: '{product_price_in_msg}'"
        assert product_price_on_page == product_price_in_msg, error_msg

    def should_not_be_success_added_to_basket_message(self):
        error_msg = "Unwanted success message found"
        element_not_found = self.is_element_not_present(*ppl.SUCCESS_MESSAGE, timeout=PRODUCT_PAGE_EXPLICIT_TIMEOUT)

        assert element_not_found, error_msg

    def success_added_to_basket_message_should_disappear(self):
        error_msg = "Success message should have disappeared, but it didn't"
        element_disappeared = self.is_element_disappeared(*ppl.SUCCESS_MESSAGE, timeout=PRODUCT_PAGE_EXPLICIT_TIMEOUT)

        assert element_disappeared, error_msg
