import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--language",
                     action="store",
                     default="en",
                     help="Desired language for webpage")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     choices=["chrome", "firefox"],
                     type=str.lower,
                     help="Desired browser for test execution")


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        chrome_opts = ChromeOptions()
        chrome_opts.add_experimental_option(name="prefs",
                                            value={'intl.accept_languages': language})

        with webdriver.Chrome(options=chrome_opts) as chrome_browser:
            yield chrome_browser

    elif browser_name == "firefox":
        firefox_opts = FirefoxOptions()
        firefox_opts.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        firefox_opts.set_preference(name="intl.accept_languages",
                                    value=language)

        with webdriver.Firefox(options=firefox_opts) as firefox_browser:
            yield firefox_browser

    else:
        raise pytest.UsageError("Browser was not specified")
