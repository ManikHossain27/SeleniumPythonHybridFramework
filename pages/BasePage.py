
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        self.get_element(locator).click()

    def clear_element_text(self, locator):
        self.get_element(locator).clear()

    def type_on_element(self, locator, text):
        self.click_on_element(locator)
        self.clear_element_text(locator)
        self.get_element(locator).send_keys(text)

    def display_status(self, locator):
        return self.get_element(locator).is_displayed()

    '''
        try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='search-results']"))
                )
            except TimeoutException:
                print("Search results not found within timeout period.")

    '''
