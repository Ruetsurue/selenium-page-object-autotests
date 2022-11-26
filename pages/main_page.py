from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK_LOCATOR)
        login_link.click()

    def should_exist_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK_LOCATOR), "login link was not found"
