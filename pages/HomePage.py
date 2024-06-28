from selenium.webdriver.common.by import By

from pages.SearchPage import SearchPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)
