import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

MAIN_PAGE_URL = r"http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser_obj=browser, url=MAIN_PAGE_URL, use_implicit_wait=True)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser_obj=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser_obj=browser, url=MAIN_PAGE_URL, use_implicit_wait=True)
        page.open()
        page.should_exist_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser_obj=browser, url=MAIN_PAGE_URL)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser_obj=browser, url=browser.current_url)
    page.should_be_empty_basket()
    page.should_be_only_empty_basket_msg()
