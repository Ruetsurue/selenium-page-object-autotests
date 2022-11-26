from selenium.webdriver.common.by import By

LOGIN_PAGE_URL = r"http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.get(url=LOGIN_PAGE_URL)
    login_link = browser.find_element(By.ID, "login_link")
    login_link.click()
