from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self,driver):
        self.driver = driver

    valid_hp_product_link_text = "HP LP3065"

    def display_status_of_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link_text).is_displayed()