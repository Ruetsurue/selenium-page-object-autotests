import math

from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

IMPLICIT_TIMEOUT_DEFAULT = 10


class BasePage:
    def __init__(self, browser_obj, url, timeout=IMPLICIT_TIMEOUT_DEFAULT):
        self.browser: Chrome = browser_obj
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(url=self.url)

    def solve_quiz_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"code: { alert_text }")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert present")

    def is_element_present(self, search_method, selector):
        try:
            self.browser.find_element(search_method, selector)
        except NoSuchElementException:
            return False

        return True
