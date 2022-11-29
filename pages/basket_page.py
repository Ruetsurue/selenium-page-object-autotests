from .base_page import BasePage
from .locators import BasketPageLocators as bpl


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_items_not_present = self.is_element_not_present(*bpl.BASKET_ITEM,
                                                               timeout=super().EXPLICIT_TIMEOUT_DEFAULT)
        item_count = len(self.retrieve_basket_items())
        error_msg = f"Expected basket to be empty, but found { item_count } items in it"
        assert basket_items_not_present, error_msg

    def retrieve_basket_items(self):
        return self.browser.find_elements(*bpl.BASKET_ITEM)

    def retrieve_basket_text_elements(self):
        return self.browser.find_elements(*bpl.BASKET_TEXT_ELEMENTS)

    def should_be_only_empty_basket_msg(self):
        basket_text_elements = self.retrieve_basket_text_elements()
        basket_text_lines = [el.text for el in basket_text_elements]
        is_only_basket_empty_msg_present = (len(basket_text_elements) == 1)
        newline_char = '\n'
        error_msg = f"Expected only one message in empty basket. Got:'{ newline_char.join(basket_text_lines) }'"
        assert is_only_basket_empty_msg_present, error_msg
