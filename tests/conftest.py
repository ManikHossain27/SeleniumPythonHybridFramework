import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ReadConfigurations


# To take Screenshot only on Failure, write the below two methods (pytest_runtest_makereport, log_on_failure).
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        method_name = item.name  # get method name
        allure.attach(driver.get_screenshot_as_png(), name=f"{method_name}_failed",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()  # scope="class"
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    driver = webdriver.Chrome()
    if browser.lower().__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.lower().__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.lower().__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrom/firefox/edge")

    driver.maximize_window()
    base_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(base_url)
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()
