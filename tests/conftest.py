import pytest
from selenium import webdriver
browser = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global browser
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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:340px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/><div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra

def _capture_screenshot(name):
    browser.get_screenshot_as_file(name)
