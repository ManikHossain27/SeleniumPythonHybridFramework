from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_box_field_name = (By.NAME, "search")
        self.search_button_xpath = (By.XPATH, "//button[@class='btn btn-default btn-lg']")

    def enter_product_into_search_box_field(self, product_name):
        self.type_on_element(self.search_box_field_name, product_name)

    def click_on_search_button(self):
        self.click_on_element(self.search_button_xpath)
        return SearchPage(self.driver)
