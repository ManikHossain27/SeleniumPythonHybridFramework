from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:

    def generate_email_with_time_stamp(self):
        time_stam = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "kinam" + time_stam + "@gmail.com"
