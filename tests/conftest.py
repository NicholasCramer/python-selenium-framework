import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "edge":
        browser = webdriver.Edge()

    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get("https://www.rahulshettyacademy.com/angularpractice/")
    request.cls.browser = browser
    yield
    browser.close()
