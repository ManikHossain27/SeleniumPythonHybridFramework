from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestSearchProduct(BaseTest):
    driver = None

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver) # create an object of HomePage
        home_page.enter_product_into_search_box_field("HP") # enter product name in search box field
        search_page = home_page.click_on_search_button() # clicking on search button I return the object of SearchPage(self.driver)
        assert search_page.display_status_of_valid_product() # check hp product is displayed or not


    def test_search_for_a_invalid_product(self):
        # create an object of HomePage
        home_page = HomePage(self.driver)
        # enter product name in search box field
        home_page.enter_product_into_search_box_field("Honda")
        # clicking on search button I return the object of SearchPage(self.driver)
        search_page = home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product_message().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        # create an object of HomePage
        home_page = HomePage(self.driver)
        # enter product name in search box field
        home_page.enter_product_into_search_box_field("")
        # clicking on search button I return the object of SearchPage(self.driver)
        search_page = home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product_message().__eq__(expected_text)
