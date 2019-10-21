import time

class CreateAccountPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, firstname):
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id("lastName").clear()
        self.driver.find_element_by_id("lastName").send_keys(lastname)

    def enter_password(self, password):
        self.driver.find_element_by_name("Passwd").clear()
        self.driver.find_element_by_name("Passwd").send_keys(password)

    def confirm_password(self, confirm_password):
        self.driver.find_element_by_name("ConfirmPasswd").clear()
        self.driver.find_element_by_name("ConfirmPasswd").send_keys(confirm_password)

    def validate_username_field(self, driver, email):
        validation_error = "Дозволені лише літери (a–z), числа (0–9) та крапки (.)."
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(email)
        self.driver.find_element_by_id("accountDetailsNext").click()

        time.sleep(1)

        assert validation_error in driver.page_source
