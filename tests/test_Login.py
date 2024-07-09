import time

import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):
    driver = None

    @pytest.mark.parametrize("email_address,password", ExcelUtils.get_data_from_excel("ExcelFiles/Data.xlsx", "LoginTest"))
    def test_login_with_valid_credentials(self, email_address, password):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        # account_page = login_page.login_to_application("kinam@gmail.com", "123456")
        account_page = login_page.login_to_application(email_address, password)
        assert account_page.display_status_of_edit_your_account_information_option(), "Edit your account information is not displayes after successfull login"
        homepage.click_on_my_account_drop_menu()
        logout_page = account_page.select_logout_button()
        logout_page.account_logout_title_is_displayed()

    def test_login_with_invalid_email_and_valid_password(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application(self.generate_email_with_time_stamp(), "123456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application("kinam@gmail.com", "1234545456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_email(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application("", "1234545456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_password(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application("kinam@gmail.com", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_email_and_password(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)