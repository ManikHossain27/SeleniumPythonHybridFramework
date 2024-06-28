from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.BasePage import BasePage


def generate_email_with_time_stamp():
    time_stam = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    email = "kinam" + time_stam + "@gmail.com"
    return email


# @pytest.mark.usefixtures("setup_and_teardown")
class TestRegister(BasePage):
    driver = webdriver.Chrome

    def test_register_with_mandatory_field(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Manik")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Hossain")
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("123456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)

    def test_register_with_all_field(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Manik")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Hossain")
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("123456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("123456")
        self.driver.find_element(By.XPATH, "input[value='1'][name='newsletter']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)

    def test_register_with_existing_email(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Manik")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Hossain")
        self.driver.find_element(By.ID, "input-email").send_keys("kinam@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("123456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_warning_text)

    def test_register_without_any_input(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("")
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-telephone").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.ID, "input-confirm").send_keys("")
        #self.driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        expected_warning_privacy_policy = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_warning_privacy_policy)
        expected_first_name_warning_msg = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__contains__(expected_first_name_warning_msg)
        expected_last_name_warning_msg = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__contains__(expected_last_name_warning_msg)
        expected_email_warning_msg = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__contains__(expected_email_warning_msg)
        expected_telephone_warning_msg = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__contains__(expected_telephone_warning_msg)
        expected_password_warning_msg = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__contains__(expected_password_warning_msg)

