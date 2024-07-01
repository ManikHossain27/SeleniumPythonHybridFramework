import pytest
from selenium import webdriver

from utilities import ReadConfigurations

driver = None


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    browser = "kinam" # ReadConfigurations.read_configuration("basic info", "browser")
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
    base_url = "https://tutorialsninja.com/demo/" # ReadConfigurations.read_configuration("basic info", "url")
    driver.get(base_url)
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()


'''
    def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

    @pytest.fixture(scope="class")
        def setup(request):
            global driver
            browser_name=request.config.getoption("browser_name")
            if browser_name == "chrome":
                driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
            
'''