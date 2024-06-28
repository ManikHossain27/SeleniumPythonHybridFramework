import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from tests.BasePage import BasePage


# @pytest.mark.usefixtures("setup_and_teardown")
class TestSearchProduct(BasePage):
    driver = None

    def test_search_for_a_valid_product(self):
        # create an object of HomePage
        home_page = HomePage(self.driver)
        # enter product name in search box field
        home_page.enter_product_into_search_box_field("HP")
        # clicking on search button I return the object of SearchPage(self.driver)
        search_page = home_page.click_on_search_button()
        # check hp product is displayed or not
        assert search_page.display_status_of_valid_product()

        # self.driver.find_element(By.NAME, "search").send_keys("HP")
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        # assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_for_a_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expectedText = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/p[2]").text.__eq__(expectedText)

    def test_search_without_entering_any_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expectedText = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/p[2]").text.__eq__(expectedText)
