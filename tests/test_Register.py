from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):
    driver = None

    def test_register_with_mandatory_field(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Manik","Hossain", self.generate_email_with_time_stamp(),
                                                                 "0153456789", "123456", "123456", "no","check")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrive_account_creation_message().__eq__(expected_heading_text)
        account_page = AccountPage(self.driver)
        account_page.select_logout_button()

    def test_register_with_all_field(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/Data.xlsx","RegisterTest",2,1),
            ExcelUtils.get_cell_data("ExcelFiles/Data.xlsx","RegisterTest",2,2),
            self.generate_email_with_time_stamp(), "0153456789", "123456", "123456", "yes", "check")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrive_account_creation_message().__eq__(expected_heading_text)
        account_page = AccountPage(self.driver)
        account_page.select_logout_button()

    def test_register_with_existing_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Manik", "Hossain", "kinam@gmail.com", "0153456789",
                                                                 "123456", "123456", "yes", "check")
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_text)

    def test_register_without_any_input(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("", "", "", "", "", "", "", "")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")
