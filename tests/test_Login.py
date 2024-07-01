import time

from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestLogin(BaseTest):
    driver = None

    def test_login_with_valid_credentials(self):
        homepage = HomePage(self.driver)
        login_page = homepage.navigate_to_login_page()
        login_page.enter_email_address("kinam@gmail.com")
        account_page = login_page.login_to_application("kinam@gmail.com", "123456")
        assert account_page.display_status_of_edit_your_account_information_option()
        homepage.click_on_my_account_drop_menu()
        logout_page = account_page.select_logout_button()
        logout_page.account_logout_title_is_displayed()

    def test_login_with_invalid_email_and_valid_password(self):
        homepage = HomePage(self.driver)
        homepage.navigate_to_login_page()
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        homepage = HomePage(self.driver)
        homepage.navigate_to_login_page()
        self.driver.find_element(By.NAME, "email").send_keys("kinam@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("1234567890")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_without_entering_email(self):
        homepage = HomePage(self.driver)
        homepage.navigate_to_login_page()
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_without_entering_password(self):
        homepage = HomePage(self.driver)
        homepage.navigate_to_login_page()
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_without_entering_email_and_password(self):
        homepage = HomePage(self.driver)
        homepage.navigate_to_login_page()
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
