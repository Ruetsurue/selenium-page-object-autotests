import pytest
import time
from faker.providers import internet, misc

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

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


@pytest.mark.user_add_products
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, faker):
        page = LoginPage(browser_obj=browser, url=LoginPage.LOGIN_PAGE_URL, use_implicit_wait=True)
        page.open()
        page.should_be_login_page()

        faker.add_provider(internet)
        faker.add_provider(misc)
        email: str = faker.email()

        email_fragments = email.split('@')
        email_fragments[0] += str(time.time())[-8:]
        email = '@'.join(email_fragments)

        page.register_new_user(email=email, password=faker.password())
        page.should_be_user_authorized()

    def test_user_cant_see_success_message_on_opening_page(self, browser):
        page = ProductPage(browser_obj=browser, url=PRODUCT_URL, use_implicit_wait=True)
        page.open()
        page.should_not_be_success_added_to_basket_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser_obj=browser, url=PRODUCT_URL, use_implicit_wait=True)
        page.open()
        page.add_product_to_basket()
        page.should_be_added_to_basket_messages()


@pytest.mark.need_review
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


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_URL)
    page.open()
    page.should_exist_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser_obj=browser, url=browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser_obj=browser, url=PRODUCT_URL)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser_obj=browser, url=browser.current_url)
    page.should_be_empty_basket()
    page.should_be_only_empty_basket_msg()
