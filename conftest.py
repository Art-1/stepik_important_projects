import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language: ru or etc.")
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: ru or etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()

    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_lang)
        browser = webdriver.Firefox(firefox_profile=fp)
        yield browser
        print("\nquit browser..")
        browser.quit()