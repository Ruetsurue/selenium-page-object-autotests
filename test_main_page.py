from pages.main_page import MainPage

LOGIN_PAGE_URL = r"http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser_obj=browser, url=LOGIN_PAGE_URL)
    main_page.open()
    main_page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser_obj=browser, url=LOGIN_PAGE_URL)
    page.open()
    page.should_exist_login_link()
