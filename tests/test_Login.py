import time

from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestLogin(BaseTest):
    driver = None

    def test_login_with_valid_credentials(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        account_page = login_page.login_to_application("kinam@gmail.com", "123456")
        assert account_page.display_status_of_edit_your_account_information_option()
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