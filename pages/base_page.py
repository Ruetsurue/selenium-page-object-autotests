from selenium.common import NoSuchElementException

IMPLICIT_TIMEOUT_DEFAULT = 10


class BasePage:
    def __init__(self, browser_obj, url, timeout=IMPLICIT_TIMEOUT_DEFAULT):
        self.browser = browser_obj
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(url=self.url)

    def is_element_present(self, search_method, selector):
        try:
            self.browser.find_element(search_method, selector)
        except NoSuchElementException:
            return False

        return True
