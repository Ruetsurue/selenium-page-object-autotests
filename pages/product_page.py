from .base_page import BasePage
from .locators import ProductPageLocators as ppl


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ppl.ADD_PRODUCT_BUTTON).click()

    def should_be_added_to_basket_message(self):
        self.is_element_present(*ppl.PRODUCT_NAME_IN_MSG)
        product_name_on_page = self.browser.find_element(*ppl.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ppl.PRODUCT_NAME_IN_MSG).text
        error_msg = f"Product name on page and in basket-add notification do not match" \
                    f"\nExpected: '{product_name_on_page}', got: '{product_name_in_basket}'"
        assert product_name_on_page == product_name_in_basket, error_msg

    def should_be_basket_price(self):
        self.is_element_present(*ppl.PRODUCT_PRICE_IN_MSG)
        product_price_on_page = self.browser.find_element(*ppl.PRODUCT_PRICE).text
        product_price_in_msg = self.browser.find_element(*ppl.PRODUCT_PRICE_IN_MSG).text
        error_msg = f"Product price on page and in basket-add notification do not match" \
                    f"\nExpected: '{product_price_on_page}', got: '{product_price_in_msg}'"
        assert product_price_on_page == product_price_in_msg, error_msg
