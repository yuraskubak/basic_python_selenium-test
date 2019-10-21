import time

class SignInPage():

    def __init__(self, driver):
        self.driver = driver

    def create_account(self):
        self.driver.find_element_by_id("ow250").click()

        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id='initialView']/div[2]/div[3]/div/div/span[1]/div[2]/div").click()