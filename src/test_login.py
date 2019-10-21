from selenium import webdriver
from pages.sign_in_page import SignInPage
from pages.create_account_page import CreateAccountPage


driver = webdriver.Chrome('C:/Users/y.skubak/Desktop/python_course/chromedriver.exe')
driver.implicitly_wait(3)
driver.get("https://accounts.google.com")

sign_in_page = SignInPage(driver)
sign_in_page.create_account()

user_dictionary = {'fn': 'Yurii', 'ln': 'Skubak', 'password': 'a1234567!'}
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
validation_error = "Дозволені лише літери (a–z), числа (0–9) та крапки (.)."

create_account_page = CreateAccountPage(driver)
create_account_page.enter_firstname(user_dictionary['fn'])
create_account_page.enter_lastname(user_dictionary['ln'])
create_account_page.enter_password(user_dictionary['password'])
create_account_page.confirm_password(user_dictionary['password'])

for email in email_list:
    create_account_page.validate_username_field(driver, email)

driver.quit()