import pytest

from pages.product_page import ProductPage

PRODUCT_PAGE_URLS = [r"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                     r"https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
                     ]


@pytest.mark.parametrize('product_url', PRODUCT_PAGE_URLS)
def test_guest_can_add_product_to_basket(browser, product_url):
    page = ProductPage(browser_obj=browser, url=product_url)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_get_code()
    page.should_be_added_to_basket_messages()
