from pages.product_page import ProductPage

PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_get_code()
    page.should_be_added_to_basket_message()
    page.should_be_basket_price()
