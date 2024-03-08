import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get("https://www.rahulshettyacademy.com/angularpractice/")
    request.cls.browser = browser
    yield
    browser.close()

