import math
from typing import Union

from selenium.webdriver import Chrome, Firefox
from selenium.common import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators as bpl

IMPLICIT_TIMEOUT_DEFAULT = 10


class BasePage:
    def __init__(self, browser_obj: Union[Chrome, Firefox], url, use_implicit_wait=False, implicit_timeout=IMPLICIT_TIMEOUT_DEFAULT):
        self.browser = browser_obj
        self.url = url
        if use_implicit_wait:
            self.browser.implicitly_wait(implicit_timeout)

    def open(self):
        self.browser.get(url=self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*bpl.LOGIN_LINK_LOCATOR)
        login_link.click()

    def should_exist_login_link(self):
        assert self.is_element_present(*bpl.LOGIN_LINK_LOCATOR), "login link was not found"

    def solve_quiz_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert present")

    def is_element_present(self, search_method, selector):
        try:
            self.browser.find_element(search_method, selector)
        except NoSuchElementException:
            return False

        return True

    def is_element_not_present(self, search_method, selector, timeout):
        try:
            WebDriverWait(driver=self.browser, timeout=timeout, poll_frequency=1,
                          ignored_exceptions=None).until(EC.presence_of_element_located((search_method, selector)))
        except TimeoutException:
            return True

        return False

    def is_element_disappeared(self, search_method, selector, timeout):
        try:
            WebDriverWait(driver=self.browser, timeout=timeout, poll_frequency=1,
                          ignored_exceptions=None).until_not(EC.presence_of_element_located((search_method, selector)))

        except TimeoutException:
            return False

        return True
