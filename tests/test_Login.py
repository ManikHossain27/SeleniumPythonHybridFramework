from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from tests.BasePage import BasePage


def generate_email_with_time_stamp():
    timeStam = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "kinam" + timeStam + "gmail.com"


# @pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(BasePage):
    driver = None

    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("kinam@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME, "email").send_keys(generate_email_with_time_stamp())
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("kinam@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("1234567890")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_without_entering_email(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_without_entering_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME, "email").send_keys(generate_email_with_time_stamp())
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

    def test_login_without_entering_email_and_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
