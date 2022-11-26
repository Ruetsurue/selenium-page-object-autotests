from .base_page import BasePage
from selenium.webdriver.common.by import By

LOGIN_LINK_LOCATOR = (By.ID, "login_link")


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*LOGIN_LINK_LOCATOR)
        login_link.click()

    def should_exist_login_link(self):
        assert self.is_element_present(*LOGIN_LINK_LOCATOR), "login link was not found"
