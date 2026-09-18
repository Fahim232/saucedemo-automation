import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", default=False,
                     help="Run the browser in headed (visible) mode")
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"],
                     help="Browser to run tests against")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    if browser == "chrome":
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if not headed:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()