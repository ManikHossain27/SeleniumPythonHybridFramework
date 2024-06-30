from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = (By.LINK_TEXT, "HP LP3065")
    no_product_message_xpath = "//div[@id='content']/p[2]"

    def display_status_of_valid_product(self):
        return self.display_status(self.valid_hp_product_link_text)

    def retrive_no_product_message(self):
        return self.driver.find_element(By.XPATH, self.no_product_message_xpath).text
