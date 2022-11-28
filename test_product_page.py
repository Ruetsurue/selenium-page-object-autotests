import pytest

from pages.product_page import ProductPage

PRODUCT_URL = r"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

PRODUCT_PAGE_URLS_PROMO = \
                    ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                     pytest.param("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail(reason="server error on adding a product to basket")),
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                     "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                     ]

@pytest.mark.skip
@pytest.mark.parametrize('product_url', PRODUCT_PAGE_URLS_PROMO)
def test_guest_can_add_product_to_basket(browser, product_url):
    page = ProductPage(browser_obj=browser, url=product_url)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_get_code()
    page.should_be_added_to_basket_messages()


@pytest.mark.xfail(reason="There SHOULD be a success msg on adding a product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_URL)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_added_to_basket_message()


def test_guest_cant_see_success_message_on_opening_page(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_URL)
    page.open()
    page.should_not_be_success_added_to_basket_message()


@pytest.mark.xfail(reason="By design success msg NEVER disappears by itself")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_URL)
    page.open()
    page.add_product_to_basket()
    page.success_added_to_basket_message_should_disappear()
