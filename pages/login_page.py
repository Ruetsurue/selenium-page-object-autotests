from .base_page import BasePage
from .locators import LoginPageLocators as lpl


class LoginPage(BasePage):

    LOGIN_PAGE_URL = r"http://selenium1py.pythonanywhere.com/accounts/login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_substr = 'login'
        current_url: str = self.browser.current_url
        search_result = current_url.lower().find(login_substr)

        assert search_result > -1, f"expected '{ login_substr }' in url. found: '{ current_url }'"

    def should_be_login_form(self):
        assert self.is_element_present(*lpl.LOGIN_FORM), "login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*lpl.REGISTER_FORM), "register form not found"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*lpl.EMAIL_FIELD)
        password_field = self.browser.find_element(*lpl.PASSWORD_FIELD)
        password_repeat_field = self.browser.find_element(*lpl.PASSWORD_REPEAT_FIELD)

        email_field.send_keys(email)
        password_field.send_keys(password)
        password_repeat_field.send_keys(password)

        self.browser.find_element(*lpl.SIGNUP_BUTTON).click()
