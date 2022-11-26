
class BasePage:
    def __init__(self, browser_obj, url):
        self.browser = browser_obj
        self.url = url

    def open(self):
        self.browser.get(url=self.url)
